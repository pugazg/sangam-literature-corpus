#!/usr/bin/env python3
"""Validate R1 append-only review and entity-resolution outputs."""
from __future__ import annotations

import argparse
import json
from pathlib import Path

from research_r1lib import (
    ALLOWED_REVIEW_TRANSITIONS, ENTITY_OPERATIONS, IDENTITY_STATES,
    REVIEWER_TYPES, current_statuses, decision_id, load_ndjson,
    validate_decision_semantics, validate_event_chain,
)

REVIEW_REQUIRED = {
    "review_event_id", "event_version", "sequence", "work_id", "record_id",
    "assertion_id", "assertion_type", "printed_form", "evidence_span",
    "source_field", "source_location", "previous_status", "new_status",
    "decision", "reviewer", "decision_rationale", "supporting_assertion_ids",
    "ambiguity_note", "verification_scope", "reviewed_at",
    "previous_event_hash", "event_hash", "notes",
}
DECISION_REQUIRED = {
    "decision_id", "decision_version", "work_id", "operation", "identity_state",
    "involved_entity_ids", "variant_forms", "supporting_assertion_ids",
    "reviewer_type", "decision_rationale", "ambiguity_note", "result_entity_id",
}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default=".")
    parser.add_argument("--output")
    args = parser.parse_args()
    root = Path(args.root).resolve()
    errors: list[str] = []
    warnings: list[str] = []

    assertions = load_ndjson(root / "research/evidence/purananuru/assertions.ndjson")
    assertion_by_id = {value["assertion_id"]: value for value in assertions}
    if len(assertion_by_id) != 2867:
        errors.append(f"R0 assertion identity count changed: {len(assertion_by_id)}")

    entities = load_ndjson(root / "research/entities/pilot/entities.ndjson")
    entity_by_id = {value["entity_id"]: value for value in entities}
    if len(entity_by_id) != 43:
        errors.append(f"R0 entity sample count changed: {len(entity_by_id)}")

    relationships = load_ndjson(root / "research/relationships/pilot/relationships.ndjson")
    if len(relationships) != 51:
        errors.append(f"R0 relationship count changed: {len(relationships)}")
    for relation in relationships:
        if relation["object_id"] not in entity_by_id:
            errors.append(f"orphan relationship entity: {relation['relationship_id']}")
        for support in relation["supporting_assertion_ids"]:
            if support not in assertion_by_id:
                errors.append(f"orphan relationship assertion: {support}")

    events = load_ndjson(root / "research/reviews/purananuru/review-events.ndjson")
    errors.extend(validate_event_chain(events))
    status_cursor = {value["assertion_id"]: value["review_status"] for value in assertions}
    for event in events:
        missing = REVIEW_REQUIRED - set(event)
        if missing:
            errors.append(f"review event missing keys {sorted(missing)}: {event.get('review_event_id')}")
            continue
        assertion = assertion_by_id.get(event["assertion_id"])
        if assertion is None:
            errors.append(f"orphan review assertion: {event['assertion_id']}")
            continue
        reviewer = event["reviewer"]
        if set(reviewer) != {"reviewer_id", "reviewer_type"} or reviewer["reviewer_type"] not in REVIEWER_TYPES:
            errors.append(f"invalid reviewer identity/type: {event['review_event_id']}")
        transition = (event["previous_status"], event["new_status"])
        if transition not in ALLOWED_REVIEW_TRANSITIONS:
            errors.append(f"illegal review transition: {event['review_event_id']}")
        if status_cursor[event["assertion_id"]] != event["previous_status"]:
            errors.append(f"review event previous status mismatch: {event['review_event_id']}")
        status_cursor[event["assertion_id"]] = event["new_status"]
        if event["printed_form"] != assertion["source_text"]:
            errors.append(f"review printed form mismatch: {event['review_event_id']}")
        if event["evidence_span"] != assertion["evidence_span"]:
            errors.append(f"review evidence span mismatch: {event['review_event_id']}")
        if event["source_field"] != assertion["source_field"] or event["source_location"] != assertion["source_location"]:
            errors.append(f"review source location mismatch: {event['review_event_id']}")
        if not event["supporting_assertion_ids"]:
            errors.append(f"review event lacks assertion provenance: {event['review_event_id']}")
        if not set(event["supporting_assertion_ids"]) <= assertion_by_id.keys():
            errors.append(f"orphan review support: {event['review_event_id']}")
        if event["new_status"] == "verified" and event["decision"] != "verify":
            errors.append(f"verified state lacks explicit verification decision: {event['review_event_id']}")

    decisions = load_ndjson(root / "research/entities/pilot/entity-resolution-decisions.ndjson")
    seen_decisions: set[str] = set()
    for value in decisions:
        missing = DECISION_REQUIRED - set(value)
        if missing:
            errors.append(f"entity decision missing keys {sorted(missing)}: {value.get('decision_id')}")
            continue
        if value["decision_id"] in seen_decisions:
            errors.append(f"duplicate entity decision: {value['decision_id']}")
        seen_decisions.add(value["decision_id"])
        if value["decision_id"] != decision_id(value):
            errors.append(f"non-deterministic entity decision ID: {value['decision_id']}")
        if value["operation"] not in ENTITY_OPERATIONS:
            errors.append(f"invalid entity operation: {value['decision_id']}")
        if value["identity_state"] not in IDENTITY_STATES:
            errors.append(f"invalid identity state: {value['decision_id']}")
        if value["reviewer_type"] not in REVIEWER_TYPES:
            errors.append(f"invalid entity decision reviewer type: {value['decision_id']}")
        errors.extend(validate_decision_semantics(value))
        for entity_id in value["involved_entity_ids"]:
            if entity_id not in entity_by_id:
                errors.append(f"orphan entity decision target: {entity_id}")
        for support in value["supporting_assertion_ids"]:
            if support not in assertion_by_id:
                errors.append(f"orphan entity decision support: {support}")
        if value["result_entity_id"] is not None and value["result_entity_id"] not in entity_by_id:
            errors.append(f"orphan entity decision result: {value['result_entity_id']}")
        if value["identity_state"] == "verified_match":
            errors.append(f"R1 pilot must not create verified historical identity: {value['decision_id']}")

    queue = load_ndjson(root / "research/reviews/purananuru/review-queue.ndjson")
    queue_ids = [value["queue_id"] for value in queue]
    if len(queue_ids) != len(set(queue_ids)):
        errors.append("duplicate review queue IDs")
    expected_order = sorted(
        queue,
        key=lambda value: (
            int(value["record_id"]) if value["record_id"] else 999,
            value["queue_item_type"],
            value["printed_form"],
            value["assertion_id"] or "",
            value["entity_id"] or "",
        ),
    )
    if queue != expected_order:
        errors.append("review queue ordering is not deterministic")
    statuses = current_statuses(assertions, events)
    for row in queue:
        if row["assertion_id"] is not None:
            if row["assertion_id"] not in assertion_by_id:
                errors.append(f"orphan queue assertion: {row['queue_id']}")
            elif row["current_review_status"] != statuses[row["assertion_id"]]:
                errors.append(f"stale queue review status: {row['queue_id']}")
        if row["entity_id"] is not None and row["entity_id"] not in entity_by_id:
            errors.append(f"orphan queue entity: {row['queue_id']}")
        for support in row["supporting_assertion_ids"]:
            if support not in assertion_by_id:
                errors.append(f"orphan queue support: {row['queue_id']}")

    manifest = json.loads((root / "manifests/classical-tamil-research-program.json").read_text(encoding="utf-8"))
    if manifest.get("phase") != "R1" or manifest.get("research_schema_version") != "0.2.0":
        errors.append("research programme manifest is not R1/0.2.0")
    if manifest.get("evidence_schema_version") != "0.1.0":
        errors.append("R0 evidence schema identity was not preserved")
    if manifest.get("source_release_commit") != "272d9d5a79d55994e2c12efacc22be20b2c88030":
        errors.append("R0 source-release provenance changed")
    if manifest.get("compatible_corpus_release_tag") != "classical-tamil-corpus-v1.1.0":
        errors.append("current corpus compatibility tag missing")

    compatibility = json.loads(
        (root / "logs/classical-tamil-research-r0-to-corpus-1.1.0-compatibility-20260818T145500.json").read_text(encoding="utf-8")
    )
    if compatibility.get("status") != "pass":
        errors.append("R0-to-1.1.0 compatibility gate is not pass")

    result = {
        "programme_id": "classical-tamil-research-layer",
        "phase": "R1",
        "research_schema_version": "0.2.0",
        "r0_assertions_checked": len(assertions),
        "relationships_checked": len(relationships),
        "review_events_checked": len(events),
        "entity_decisions_checked": len(decisions),
        "review_queue_entries_checked": len(queue),
        "errors": errors,
        "warnings": warnings,
        "status": "pass" if not errors else "fail",
    }
    if args.output:
        path = root / args.output
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, ensure_ascii=False, indent=2))
    if errors:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
