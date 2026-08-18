#!/usr/bin/env python3
"""Verify R1 deterministic regeneration and append-only primary histories."""
from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
import sys
from pathlib import Path

DETERMINISTIC = [
    "research/reviews/purananuru/review-queue.ndjson",
    "research/reviews/purananuru/reviewed-export.ndjson",
    "research/reports/purananuru-r1-review-summary.json",
    "research/reports/purananuru-r1-review-summary.md",
    "research/reports/purananuru-r1-ambiguity-register.md",
    "research/reports/purananuru-r1-unresolved-entities.csv",
]
PRIMARY = [
    "research/reviews/purananuru/review-events.ndjson",
    "research/entities/pilot/entity-resolution-decisions.ndjson",
]


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def hashes(root: Path, paths: list[str]) -> dict[str, str]:
    return {path: sha(root / path) for path in paths}


def run(root: Path) -> None:
    subprocess.check_call([sys.executable, "scripts/generate_research_r1.py", "--root", "."], cwd=root)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default=".")
    parser.add_argument("--output", default="logs/classical-tamil-research-r1-idempotence-20260818T145500.json")
    args = parser.parse_args()
    root = Path(args.root).resolve()
    primary_before = hashes(root, PRIMARY)
    run(root)
    first = hashes(root, DETERMINISTIC)
    run(root)
    second = hashes(root, DETERMINISTIC)
    primary_after = hashes(root, PRIMARY)
    stable = first == second
    append_only_preserved = primary_before == primary_after
    report = {
        "programme_id": "classical-tamil-research-layer",
        "phase": "R1",
        "research_schema_version": "0.2.0",
        "deterministic_outputs": DETERMINISTIC,
        "first_pass_hashes": first,
        "second_pass_hashes": second,
        "byte_stable": stable,
        "primary_history_hashes_before": primary_before,
        "primary_history_hashes_after": primary_after,
        "primary_histories_preserved": append_only_preserved,
        "status": "pass" if stable and append_only_preserved else "fail",
    }
    output = root / args.output
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False, indent=2))
    if report["status"] != "pass":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
