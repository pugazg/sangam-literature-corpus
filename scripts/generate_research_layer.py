#!/usr/bin/env python3
"""Compatibility entry point for deterministic R0 generation on an R1 branch.

The historical implementation is preserved in generate_research_layer_r0.py.
This wrapper prevents the R0 generator from truncating append-only R1 review
history while leaving every R0 evidence writer unchanged.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import generate_research_layer_r0 as r0
from researchlib import advisory_lock


def generate(root: Path) -> dict:
    review_events = (root / "research/reviews/purananuru/review-events.ndjson").resolve()
    original_atomic_write = r0.atomic_write

    def protected_atomic_write(path: Path, text: str) -> None:
        target = Path(path).resolve()
        if target == review_events and review_events.exists():
            return
        original_atomic_write(path, text)

    r0.atomic_write = protected_atomic_write
    try:
        return r0.generate(root)
    finally:
        r0.atomic_write = original_atomic_write


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default=".")
    args = parser.parse_args()
    root = Path(args.root).resolve()
    with advisory_lock(root / "research/.generation.lock"):
        r0.schema_files(root)
        r0.vocabulary_files(root)
        summary = generate(root)
    (root / "research/.generation.lock").unlink(missing_ok=True)
    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
