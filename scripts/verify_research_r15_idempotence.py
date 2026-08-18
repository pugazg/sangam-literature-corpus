#!/usr/bin/env python3
"""Verify R1.5 deterministic regeneration without mutating evidence/review inputs."""
from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
import sys
from pathlib import Path

DETERMINISTIC = [
    "research/observations/purananuru/r15-pilot.ndjson",
    "research/matrices/purananuru/r15-pilot-matrix.csv",
    "research/reports/purananuru-r15-pilot-summary.json",
    "research/reports/purananuru-r15-pilot-summary.md",
]
PRIMARY = [
    "research/evidence/purananuru/assertions.ndjson",
    "research/reviews/purananuru/review-events.ndjson",
    "research/reviews/purananuru/reviewed-export.ndjson",
    "research/entities/pilot/entity-resolution-decisions.ndjson",
    "research/pilots/purananuru/r15-pilot-mapping.json",
    "research/concepts/classical-tamil/concept-registry-r15.json",
]


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def hashes(root: Path, paths: list[str]) -> dict[str, str]:
    return {path: sha(root / path) for path in paths}


def run(root: Path) -> None:
    subprocess.check_call(
        [sys.executable, "scripts/generate_research_r15.py", "--root", "."],
        cwd=root,
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default=".")
    parser.add_argument(
        "--output",
        default="logs/classical-tamil-research-r15-idempotence-20260818T160000.json",
    )
    args = parser.parse_args()
    root = Path(args.root).resolve()

    primary_before = hashes(root, PRIMARY)
    run(root)
    first = hashes(root, DETERMINISTIC)
    run(root)
    second = hashes(root, DETERMINISTIC)
    primary_after = hashes(root, PRIMARY)

    stable = first == second
    primary_preserved = primary_before == primary_after
    report = {
        "programme_id": "classical-tamil-research-layer",
        "phase": "R1.5",
        "concept_schema_version": "0.3.0",
        "deterministic_outputs": DETERMINISTIC,
        "first_pass_hashes": first,
        "second_pass_hashes": second,
        "byte_stable": stable,
        "primary_inputs": PRIMARY,
        "primary_input_hashes_before": primary_before,
        "primary_input_hashes_after": primary_after,
        "primary_inputs_preserved": primary_preserved,
        "status": "pass" if stable and primary_preserved else "fail",
    }

    output = root / args.output
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(
        json.dumps(report, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(json.dumps(report, ensure_ascii=False, indent=2))
    if report["status"] != "pass":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
