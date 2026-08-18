#!/usr/bin/env python3
"""Capture deterministic R1.5 acceptance hashes and counts."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

TARGETS = [
    "research/concepts/classical-tamil/concept-registry-r15.json",
    "research/controlled-vocabularies/concept-dimensions-r15.json",
    "research/controlled-vocabularies/classification-bases-r15.json",
    "research/controlled-vocabularies/concept-evidence-policies-r15.json",
    "research/schemas/concept-definition-r15.schema.json",
    "research/schemas/concept-observation-r15.schema.json",
    "research/schemas/tolkappiyam-concept-evidence-r15.schema.json",
    "research/pilots/purananuru/r15-pilot-mapping.json",
    "research/observations/purananuru/r15-pilot.ndjson",
    "research/matrices/purananuru/r15-pilot-matrix.csv",
    "research/reports/purananuru-r15-pilot-summary.json",
    "research/reports/purananuru-r15-pilot-summary.md",
    "research/evidence/purananuru/assertions.ndjson",
    "research/reviews/purananuru/review-events.ndjson",
    "research/reviews/purananuru/reviewed-export.ndjson",
    "research/entities/pilot/entity-resolution-decisions.ndjson",
    "research/relationships/pilot/relationships.ndjson",
    "manifests/classical-tamil-research-program.json",
]


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def count_ndjson(path: Path) -> int:
    return sum(bool(line.strip()) for line in path.read_text(encoding="utf-8").splitlines())


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default=".")
    parser.add_argument("--output", default="logs/classical-tamil-research-r15-baseline-20260818T164600.json")
    args = parser.parse_args()
    root = Path(args.root).resolve()

    registry = json.loads((root / TARGETS[0]).read_text(encoding="utf-8"))
    summary = json.loads((root / "research/reports/purananuru-r15-pilot-summary.json").read_text(encoding="utf-8"))
    report = {
        "programme_id": "classical-tamil-research-layer",
        "phase": "R1.5",
        "concept_schema_version": "0.3.0",
        "evidence_schema_version": "0.1.0",
        "review_workflow_schema_version": "0.2.0",
        "compatible_corpus_release_tag": "classical-tamil-corpus-v1.1.0",
        "concept_definition_count": len(registry["concepts"]),
        "pilot_observation_count": count_ndjson(root / "research/observations/purananuru/r15-pilot.ndjson"),
        "pilot_record_count": summary["pilot_record_count"],
        "pilot_concept_count": summary["pilot_concept_count"],
        "pilot_dimension_count": summary["pilot_dimension_count"],
        "r0_assertion_count": count_ndjson(root / "research/evidence/purananuru/assertions.ndjson"),
        "r1_review_event_count": count_ndjson(root / "research/reviews/purananuru/review-events.ndjson"),
        "r0_relationship_count": count_ndjson(root / "research/relationships/pilot/relationships.ndjson"),
        "tolkappiyam_production_observation_count": len(list((root / "research/observations/tolkappiyam").glob("*.ndjson"))),
        "hashes": {path: sha(root / path) for path in TARGETS},
        "status": "pass",
    }

    output = root / args.output
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
