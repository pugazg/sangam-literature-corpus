#!/usr/bin/env python3
"""Validate R0 research evidence against immutable frozen inputs."""
from __future__ import annotations

import argparse
import json
import subprocess
from collections import Counter
from pathlib import Path

from researchlib import assertion_id, parse_poem, relationship_id, sha_file, write_json

EVIDENCE = {"SOURCE_EXPLICIT", "MECHANICALLY_DERIVED", "CROSS_TEXT", "EXTERNAL_HISTORICAL", "EDITORIAL_INFERENCE", "INTERPRETATION"}
REVIEWS = {"unreviewed", "machine_checked", "human_review_required", "reviewed", "verified", "rejected", "superseded"}
CONFIDENCE = {"high", "medium", "low"}
ALLOWED_TRANSITIONS = {("unreviewed", "machine_checked"), ("machine_checked", "human_review_required"), ("human_review_required", "reviewed"), ("reviewed", "verified"), ("reviewed", "rejected"), ("verified", "superseded"), ("rejected", "superseded")}


def load_ndjson(path: Path) -> list[dict]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def main() -> None:
    parser = argparse.ArgumentParser(); parser.add_argument("--root", default="."); parser.add_argument("--output"); args = parser.parse_args()
    root = Path(args.root).resolve(); errors, warnings = [], []
    assertions_path = root / "research/evidence/purananuru/assertions.ndjson"
    assertions = load_ndjson(assertions_path)
    ids = [x.get("assertion_id") for x in assertions]
    if len(ids) != len(set(ids)): errors.append("duplicate assertion IDs")
    required = json.loads((root / "research/schemas/assertion.schema.json").read_text())["required"]
    type_codes = {x["code"] for x in json.loads((root / "research/controlled-vocabularies/assertion-types.json").read_text())["entries"]}
    predicate_codes = {x["code"] for x in json.loads((root / "research/controlled-vocabularies/predicates.json").read_text())["entries"]}
    previous = None
    assertion_by_id = {}
    for index, value in enumerate(assertions, 1):
        missing = [key for key in required if key not in value]
        if missing: errors.append(f"assertion {index} missing keys: {missing}"); continue
        if value["assertion_id"] != assertion_id(value): errors.append(f"non-deterministic assertion ID: {value['assertion_id']}")
        if value["evidence_class"] not in EVIDENCE: errors.append(f"invalid evidence class: {value['assertion_id']}")
        if value["assertion_type"] not in type_codes: errors.append(f"invalid assertion type: {value['assertion_id']}")
        if value["predicate"] not in predicate_codes: errors.append(f"unresolved predicate vocabulary code: {value['assertion_id']}")
        if value["review_status"] not in REVIEWS or value["confidence"] not in CONFIDENCE: errors.append(f"invalid review/confidence: {value['assertion_id']}")
        if value["evidence_class"] in {"EXTERNAL_HISTORICAL", "INTERPRETATION"}: errors.append(f"forbidden R0 evidence class: {value['assertion_id']}")
        path = root / value["canonical_record_path"]
        if not path.is_file(): errors.append(f"orphan canonical path: {value['assertion_id']}"); continue
        parsed = parse_poem(path)
        if sha_file(path) != value["canonical_record_sha256"] or parsed["body_sha256"] != value["canonical_body_sha256"] or parsed["source_note_sha256"] != value["source_note_sha256"]:
            errors.append(f"canonical hash mismatch: {value['assertion_id']}")
        span = value["evidence_span"]
        if span:
            if span["start_line"] != span["end_line"] or not 1 <= span["start_line"] <= len(parsed["body_lines"]):
                errors.append(f"invalid line span: {value['assertion_id']}")
            else:
                line = parsed["body_lines"][span["start_line"] - 1]
                if not 0 <= span["start_character"] <= span["end_character"] <= len(line): errors.append(f"invalid character span: {value['assertion_id']}")
                elif line[span["start_character"]:span["end_character"]] != value["source_text"]: errors.append(f"source-text mismatch: {value['assertion_id']}")
        order = (int(value["record_id"]), value["assertion_type"], (span or {}).get("start_line", -1), (span or {}).get("start_character", -1), value["assertion_id"])
        # Generator has a controlled type order rather than lexical type order; only record order is universal here.
        if previous and order[0] < previous[0]: errors.append("unstable record ordering")
        previous = order; assertion_by_id[value["assertion_id"]] = value
    relationships = load_ndjson(root / "research/relationships/pilot/relationships.ndjson")
    relationship_ids = set()
    for rel in relationships:
        if rel["relationship_id"] != relationship_id(rel): errors.append(f"non-deterministic relationship ID: {rel['relationship_id']}")
        if rel["predicate"] not in predicate_codes: errors.append(f"unresolved relationship predicate: {rel['relationship_id']}")
        if rel["relationship_id"] in relationship_ids: errors.append(f"duplicate relationship: {rel['relationship_id']}")
        relationship_ids.add(rel["relationship_id"])
        for support in rel["supporting_assertion_ids"]:
            if support not in assertion_by_id: errors.append(f"orphan relationship support: {support}")
    events = load_ndjson(root / "research/reviews/purananuru/review-events.ndjson")
    for event in events:
        if event["assertion_id"] not in assertion_by_id: errors.append(f"orphan review assertion: {event['assertion_id']}")
        if (event["previous_status"], event["new_status"]) not in ALLOWED_TRANSITIONS: errors.append(f"invalid review transition: {event['review_event_id']}")
    tag_target = subprocess.check_output(["git", "rev-parse", "classical-tamil-corpus-v1.0.0^{}"], cwd=root, text=True).strip()
    if tag_target != "272d9d5a79d55994e2c12efacc22be20b2c88030": errors.append("frozen release tag moved")
    summary = json.loads((root / "research/evidence/purananuru/summary.json").read_text())
    if summary["records_processed"] != 400 or summary["literary_bodies_processed"] != 398 or summary["source_lost_records"] != [267, 268]: errors.append("pilot inventory mismatch")
    result = {
        "research_schema_version": "0.1.0", "programme_id": "classical-tamil-research-layer",
        "assertions_checked": len(assertions), "relationships_checked": len(relationships),
        "evidence_spans_checked": sum(bool(x["evidence_span"]) for x in assertions),
        "canonical_hashes_checked": len(assertions), "errors": errors, "warnings": warnings,
        "review_status_counts": dict(sorted(Counter(x["review_status"] for x in assertions).items())),
        "status": "pass" if not errors else "fail",
    }
    if args.output:
        write_json(root / args.output, result)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    if errors: raise SystemExit(1)


if __name__ == "__main__": main()
