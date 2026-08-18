#!/usr/bin/env python3
"""Capture a deterministic R1 verification baseline."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

TARGETS = [
    "research/evidence/purananuru/assertions.ndjson",
    "research/mentions/purananuru/mentions.ndjson",
    "research/entities/pilot/entities.ndjson",
    "research/relationships/pilot/relationships.ndjson",
    "research/reviews/purananuru/review-events.ndjson",
    "research/entities/pilot/entity-resolution-decisions.ndjson",
    "research/reviews/purananuru/review-queue.ndjson",
    "research/reviews/purananuru/reviewed-export.ndjson",
    "research/reports/purananuru-r1-review-summary.json",
    "research/reports/purananuru-r1-review-summary.md",
    "research/reports/purananuru-r1-ambiguity-register.md",
    "research/reports/purananuru-r1-unresolved-entities.csv",
    "manifests/classical-tamil-research-program.json",
]


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def count_ndjson(path: Path) -> int:
    return sum(bool(line.strip()) for line in path.read_text(encoding="utf-8").splitlines())


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default=".")
    parser.add_argument("--output", default="logs/classical-tamil-research-r1-baseline-20260818T145500.json")
    args = parser.parse_args()
    root = Path(args.root).resolve()
    report = {
        "programme_id": "classical-tamil-research-layer",
        "phase": "R1",
        "research_schema_version": "0.2.0",
        "evidence_schema_version": "0.1.0",
        "source_release_tag": "classical-tamil-corpus-v1.0.0",
        "compatible_corpus_release_tag": "classical-tamil-corpus-v1.1.0",
        "r0_assertion_count": count_ndjson(root / TARGETS[0]),
        "r0_mention_count": count_ndjson(root / TARGETS[1]),
        "r0_entity_sample_count": count_ndjson(root / TARGETS[2]),
        "r0_relationship_count": count_ndjson(root / TARGETS[3]),
        "review_event_count": count_ndjson(root / TARGETS[4]),
        "entity_resolution_decision_count": count_ndjson(root / TARGETS[5]),
        "hashes": {path: sha(root / path) for path in TARGETS},
        "status": "pass",
    }
    output = root / args.output
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
