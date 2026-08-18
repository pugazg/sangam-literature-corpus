#!/usr/bin/env python3
"""Capture immutable frozen-corpus inputs before derived research generation."""
from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import re
import subprocess
from pathlib import Path

import yaml


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def poem_parts(path: Path) -> tuple[str, str]:
    text = path.read_text(encoding="utf-8")
    match = re.match(r"\A---\n.*?\n---\n(.*)\Z", text, re.S)
    if not match:
        raise ValueError(f"malformed frozen record: {path}")
    remainder = match.group(1)
    body_part, marker, note_part = remainder.partition("## Source note (as printed)")
    lines = body_part.splitlines()
    while lines and not lines[0].strip():
        lines.pop(0)
    if lines and lines[0].startswith("# "):
        lines = lines[1:]
    while lines and not lines[0].strip():
        lines.pop(0)
    return "\n".join(lines).strip("\n"), note_part.strip("\n") if marker else ""


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default=".")
    args = parser.parse_args()
    root = Path(args.root).resolve()
    now = dt.datetime.now().astimezone()
    works = json.loads((root / "manifests/works.json").read_text(encoding="utf-8"))
    snapshot = {}
    for item in works:
        work = item["work_slug"]
        corpus = root / "corpus" / work
        metadata = json.loads((corpus / "metadata.json").read_text(encoding="utf-8"))
        poems = sorted((corpus / "poems").glob("*.md"))
        sections = sorted((corpus / "sections").glob("*.md")) if (corpus / "sections").exists() else []
        body, note, whole = {}, {}, {}
        for path in poems:
            poem_body, source_note = poem_parts(path)
            body[path.name] = hashlib.sha256(poem_body.encode("utf-8")).hexdigest()
            note[path.name] = hashlib.sha256(source_note.encode("utf-8")).hexdigest()
            whole[path.name] = sha(path)
        structures = {
            str(path.relative_to(root)): sha(path)
            for path in sorted(corpus.glob("*inventory*.json"))
        }
        source_hash = metadata.get("source_checksum_sha256")
        source_objects = metadata.get("source_objects") or []
        snapshot[work] = {
            "corpus_schema_version": metadata.get("corpus_schema_version"),
            "version_status": metadata.get("version_status"),
            "source_checksum_sha256": source_hash,
            "source_object_sha256": {
                obj.get("source_file", obj.get("source_object_id", str(index))): obj.get("source_sha256") or obj.get("sha256")
                for index, obj in enumerate(source_objects, 1)
            },
            "poem_inventory": [p.name for p in poems],
            "section_inventory": [p.name for p in sections],
            "canonical_body_sha256": body,
            "source_note_sha256": note,
            "whole_record_sha256": whole,
            "structural_inventory_sha256": structures,
        }
    tag = "classical-tamil-corpus-v1.0.0"
    result = {
        "created_at": now.isoformat(),
        "purpose": "pre-research immutable frozen-corpus baseline",
        "physical_repository_path": str(root),
        "source_release_tag": tag,
        "source_release_commit": subprocess.check_output(["git", "rev-parse", f"{tag}^{{}}"], cwd=root, text=True).strip(),
        "source_release_content_commit": "7266a9fcb76568806b371cb31ec47f6aad6b285a",
        "repository_content_fingerprint": sha(root / "manifests/repository-content-hashes-1.0.0.sha256"),
        "combined_manifest_sha256": sha(root / "manifests/poems.csv"),
        "work_count": len(works),
        "canonical_record_count": sum(len(x["poem_inventory"]) for x in snapshot.values()),
        "works": snapshot,
    }
    target = root / "logs" / f"pre-research-layer-frozen-baseline-{now.strftime('%Y%m%dT%H%M%S')}.json"
    target.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
    print(target.relative_to(root))


if __name__ == "__main__":
    main()
