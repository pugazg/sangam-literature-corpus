#!/usr/bin/env python3
"""Capture immutable-work inventories and hashes before onboarding another work."""
from __future__ import annotations

import argparse
import hashlib
import json
from datetime import datetime
from pathlib import Path

import yaml


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def body_and_note(path: Path) -> tuple[str, str]:
    text = path.read_text(encoding="utf-8")
    tail = text.split("---", 2)[2]
    main, marker, note = tail.partition("## Source note (as printed)")
    body = "\n".join(x.strip() for x in main.splitlines() if x.strip() and not x.startswith("# "))
    note_text = "\n".join(x.strip() for x in note.splitlines() if x.strip()) if marker else ""
    return (hashlib.sha256(body.encode()).hexdigest(), hashlib.sha256(note_text.encode()).hexdigest())


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=".")
    ap.add_argument("--label", required=True)
    args = ap.parse_args()
    root = Path(args.root).resolve()
    result = {"created_at": datetime.now().astimezone().isoformat(), "physical_root": str(root), "works": {}}
    for work in ("natrinai", "aingurunuru", "kuruntokai", "akananuru", "purananuru"):
        corpus = root / "corpus" / work
        if not corpus.exists():
            continue
        metadata = json.loads((corpus / "metadata.json").read_text(encoding="utf-8"))
        poems = sorted((corpus / "poems").glob("*.md"))
        sections = sorted((corpus / "sections").glob("*.md"))
        bodies, notes = {}, {}
        for poem in poems:
            bodies[poem.name], notes[poem.name] = body_and_note(poem)
        raw_source = root / ("sources/purananuru.md" if work == "purananuru" else f"sources/raw-html/{work}.html")
        result["works"][work] = {
            "corpus_schema_version": metadata.get("corpus_schema_version"),
            "version_status": metadata.get("version_status"),
            "raw_source": {"path": str(raw_source.relative_to(root)), "sha256": digest(raw_source), "bytes": raw_source.stat().st_size},
            "poem_inventory": [p.name for p in poems], "section_inventory": [p.name for p in sections],
            "canonical_body_hashes": bodies, "source_note_hashes": notes,
            "whole_poem_hashes": {p.name: digest(p) for p in poems},
            "metadata_sha256": digest(corpus / "metadata.json"),
        }
    stamp = datetime.now().astimezone().strftime("%Y%m%dT%H%M%S")
    target = root / "logs" / f"{args.label}-{stamp}.json"
    if target.exists():
        raise FileExistsError(target)
    target.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(target)


if __name__ == "__main__":
    main()
