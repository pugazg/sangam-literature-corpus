#!/usr/bin/env python3
"""Generate deterministic R1 review queues and aggregate exports.

Primary review events and entity-resolution decisions are append-only inputs.
This generator never rewrites them.
"""
from __future__ import annotations

import argparse
import csv
import io
import json
from collections import defaultdict
from pathlib import Path

from researchlib import advisory_lock, atomic_write, write_json
from research_r1lib import (
    R1_PILOT_RECORDS, R1_SCHEMA_VERSION, current_statuses, load_ndjson, ndjson,
    stable_id,
)


def ensure_primary_log(path: Path) -> None:
    if not path.exists():
        atomic_write(path, "")


def generate(root: Path) -> dict:
    assertions = load_ndjson(root / "research/evidence/purananuru/assertions.ndjson")
    mentions = load_ndjson(root / "research/mentions/purananuru/mentions.ndjson")
    entities = load_ndjson(root / "research/entities/pilot/entities.ndjson")
    events_path = root / "research/reviews/purananuru/review-events.ndjson"
    decisions_path = root / "research/entities/pilot/entity-resolution-decisions.ndjson"
    ensure_primary_log(events_path)
    ensure_primary_log(decisions_path)
    events = load_ndjson(events_path)
    decisions = load_ndjson(decisions_path)

    assertions_by_id = {value["assertion_id"]: value for value in assertions}
    statuses = current_statuses(assertions, events)
    decision_by_entity: dict[str, list[dict]] = defaultdict(list)
    for decision in decisions:
        for entity_id in decision["involved_entity_ids"]:
            decision_by_entity[entity_id].append(decision)

    queue: list[dict] = []
    for mention in mentions:
        if int(mention["record_id"]) not in R1_PILOT_RECORDS:
            continue
        assertion = assertions_by_id[mention["assertion_id"]]
        row = {
            "queue_id": stable_id("queue.r1.", {"assertion_id": mention["assertion_id"]}),
            "queue_item_type": "mention",
            "work_id": "purananuru",
            "record_id": mention["record_id"],
            "assertion_id": mention["assertion_id"],
            "entity_id": None,
            "printed_form": mention["printed_form"],
            "assertion_type": mention["assertion_type"],
            "evidence_span": mention["evidence_span"],
            "source_field": assertion["source_field"],
            "source_location": assertion["source_location"],
            "current_confidence": assertion["confidence"],
            "current_review_status": statuses[mention["assertion_id"]],
            "proposed_entity_identity": None,
            "identity_state": "unresolved",
            "reviewer_type": None,
            "supporting_assertion_ids": [mention["assertion_id"]],
            "ambiguity_note": "Identity and any broader historical interpretation remain unresolved.",
            "priority": "pilot",
        }
        queue.append(row)

    for entity in entities:
        supports = sorted(entity["mention_assertions"])
        source_records = sorted({assertions_by_id[value]["record_id"] for value in supports})
        linked = decision_by_entity.get(entity["entity_id"], [])
        state = linked[-1]["identity_state"] if linked else "candidate_entity"
        row = {
            "queue_id": stable_id("queue.r1.", {"entity_id": entity["entity_id"]}),
            "queue_item_type": "entity",
            "work_id": "purananuru",
            "record_id": source_records[0] if source_records else None,
            "assertion_id": None,
            "entity_id": entity["entity_id"],
            "printed_form": entity["preferred_label"],
            "assertion_type": None,
            "evidence_span": None,
            "source_field": "derived_surface_form_group",
            "source_location": "research/entities/pilot/entities.ndjson",
            "current_confidence": None,
            "current_review_status": entity["review_status"],
            "proposed_entity_identity": None,
            "identity_state": state,
            "reviewer_type": linked[-1]["reviewer_type"] if linked else None,
            "supporting_assertion_ids": supports,
            "ambiguity_note": linked[-1]["ambiguity_note"] if linked else entity["notes"],
            "priority": "pilot",
        }
        queue.append(row)

    queue.sort(
        key=lambda value: (
            int(value["record_id"]) if value["record_id"] else 999,
            value["queue_item_type"],
            value["printed_form"],
            value["assertion_id"] or "",
            value["entity_id"] or "",
        )
    )
    atomic_write(root / "research/reviews/purananuru/review-queue.ndjson", ndjson(queue))

    reviewed = []
    for event in events:
        assertion = assertions_by_id[event["assertion_id"]]
        reviewed.append(
            {
                "assertion_id": event["assertion_id"],
                "work_id": event["work_id"],
                "record_id": event["record_id"],
                "printed_form": event["printed_form"],
                "assertion_type": assertion["assertion_type"],
                "evidence_span": event["evidence_span"],
                "source_field": event["source_field"],
                "source_location": event["source_location"],
                "current_confidence": assertion["confidence"],
                "current_review_status": event["new_status"],
                "reviewer_type": event["reviewer"]["reviewer_type"],
                "decision": event["decision"],
                "supporting_assertion_ids": event["supporting_assertion_ids"],
                "ambiguity_note": event["ambiguity_note"],
            }
        )
    reviewed.sort(key=lambda value: (int(value["record_id"]), value["assertion_id"]))
    atomic_write(root / "research/reviews/purananuru/reviewed-export.ndjson", ndjson(reviewed))

    unresolved_output = io.StringIO(newline="")
    writer = csv.writer(unresolved_output, lineterminator="\n")
    writer.writerow(
        [
            "entity_id", "preferred_label", "entity_type", "identity_state",
            "review_status", "mention_assertions", "decision_ids", "ambiguity_note",
        ]
    )
    unresolved_count = 0
    for entity in sorted(entities, key=lambda value: (value["preferred_label"], value["entity_id"])):
        linked = decision_by_entity.get(entity["entity_id"], [])
        state = linked[-1]["identity_state"] if linked else "candidate_entity"
        if state == "verified_match":
            continue
        unresolved_count += 1
        writer.writerow(
            [
                entity["entity_id"],
                entity["preferred_label"],
                entity["entity_type"],
                state,
                entity["review_status"],
                "|".join(sorted(entity["mention_assertions"])),
                "|".join(value["decision_id"] for value in linked),
                linked[-1]["ambiguity_note"] if linked else entity["notes"],
            ]
        )
    atomic_write(root / "research/reports/purananuru-r1-unresolved-entities.csv", unresolved_output.getvalue())

    summary = {
        "programme_id": "classical-tamil-research-layer",
        "phase": "R1",
        "research_schema_version": R1_SCHEMA_VERSION,
        "evidence_schema_version": "0.1.0",
        "research_status": "foundation",
        "work_id": "purananuru",
        "r0_assertion_count": len(assertions),
        "r0_mention_count": len(mentions),
        "r0_entity_sample_count": len(entities),
        "review_event_count": len(events),
        "review_queue_count": len(queue),
        "reviewed_export_count": len(reviewed),
        "entity_resolution_decision_count": len(decisions),
        "unresolved_entity_count": unresolved_count,
        "verified_identity_decision_count": sum(value["identity_state"] == "verified_match" for value in decisions),
        "external_historical_assertions": 0,
        "interpretation_assertions": 0,
        "source_release_provenance_preserved": True,
        "note": "R1 reviews source-grounded candidates only; it does not create verified historical identities.",
    }
    write_json(root / "research/reports/purananuru-r1-review-summary.json", summary)

    markdown = [
        "# Puṟanāṉūṟu R1 review summary",
        "",
        "R1 adds an append-only review workflow and explicit entity-resolution decisions without rewriting R0 evidence.",
        "",
        f"- R0 assertions preserved: {len(assertions)}",
        f"- R0 literary-body candidates: {len(mentions)}",
        f"- Review events recorded: {len(events)}",
        f"- Deterministic pilot queue entries: {len(queue)}",
        f"- Entity-resolution decisions: {len(decisions)}",
        f"- Unresolved pilot entities: {unresolved_count}",
        f"- Verified identity decisions: {summary['verified_identity_decision_count']}",
        "- External historical assertions: 0",
        "- Interpretation assertions: 0",
        "",
        "`reviewed` means that the recorded source evidence was explicitly inspected; it is not a verified historical identification.",
    ]
    atomic_write(root / "research/reports/purananuru-r1-review-summary.md", "\n".join(markdown) + "\n")

    ambiguity = [
        "# Puṟanāṉūṟu R1 ambiguity register",
        "",
        "Empty resolution fields are not evidence of historical absence. They record only that R1 has not licensed a stronger identity claim.",
        "",
        "## Standing ambiguities",
        "",
        "- The 285 R0 literary-body candidates remain source-derived candidates unless an explicit review event records a narrower review result.",
        "- Exact or normalized name equality never performs an automatic entity merge.",
        "- `POSSIBLY_SAME_AS` and the `possible_match` state are not verified identity.",
        "- Modern geography, biography, dynasty, dating, taxonomy, translation, and interpretation remain outside R1.",
        "- Records 267 and 268 remain source-lost and are not reconstructed.",
        "",
        "## Recorded entity decisions",
        "",
    ]
    if decisions:
        for decision in decisions:
            ambiguity.append(
                f"- `{decision['decision_id']}` — `{decision['operation']}` / `{decision['identity_state']}` — "
                f"{'; '.join(decision['variant_forms'])} — {decision['ambiguity_note']}"
            )
    else:
        ambiguity.append("- No entity-resolution decisions have been recorded.")
    atomic_write(root / "research/reports/purananuru-r1-ambiguity-register.md", "\n".join(ambiguity) + "\n")
    return summary


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default=".")
    args = parser.parse_args()
    root = Path(args.root).resolve()
    with advisory_lock(root / "research/.generation.lock"):
        summary = generate(root)
    (root / "research/.generation.lock").unlink(missing_ok=True)
    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
