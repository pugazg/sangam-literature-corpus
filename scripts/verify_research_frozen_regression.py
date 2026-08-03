#!/usr/bin/env python3
"""Compare all frozen corpus inputs with the pre-research hash baseline."""
from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import re
from pathlib import Path


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def poem_parts(path: Path) -> tuple[str, str]:
    text = path.read_text(encoding="utf-8")
    rest = re.match(r"\A---\n.*?\n---\n(.*)\Z", text, re.S).group(1)
    body_part, marker, note = rest.partition("## Source note (as printed)")
    lines = body_part.splitlines()
    while lines and not lines[0].strip(): lines.pop(0)
    if lines and lines[0].startswith("# "): lines.pop(0)
    while lines and not lines[0].strip(): lines.pop(0)
    return "\n".join(lines).strip("\n"), note.strip("\n") if marker else ""


def delta(before: dict, after: dict) -> list[str]:
    return sorted(set(before) ^ set(after)) + sorted(key for key in before.keys() & after.keys() if before[key] != after[key])


def main() -> None:
    parser = argparse.ArgumentParser(); parser.add_argument("--root", default="."); parser.add_argument("--baseline", required=True); parser.add_argument("--write-log", action="store_true"); args = parser.parse_args()
    root = Path(args.root).resolve(); baseline = json.loads((root / args.baseline).read_text(encoding="utf-8")); changes = {}
    works_manifest = json.loads((root / "manifests/works.json").read_text(encoding="utf-8"))
    for item in works_manifest:
        work = item["work_slug"]; prior = baseline["works"][work]; corpus = root / "corpus" / work
        poems = sorted((corpus / "poems").glob("*.md")); sections = sorted((corpus / "sections").glob("*.md")) if (corpus / "sections").exists() else []
        bodies, notes, whole = {}, {}, {}
        for path in poems:
            body, note = poem_parts(path); bodies[path.name] = hashlib.sha256(body.encode()).hexdigest(); notes[path.name] = hashlib.sha256(note.encode()).hexdigest(); whole[path.name] = sha(path)
        structure = {str(path.relative_to(root)): sha(path) for path in sorted(corpus.glob("*inventory*.json"))}
        metadata = json.loads((corpus / "metadata.json").read_text(encoding="utf-8"))
        changes[work] = {
            "canonical_body_changes": delta(prior["canonical_body_sha256"], bodies),
            "source_note_changes": delta(prior["source_note_sha256"], notes),
            "whole_record_changes": delta(prior["whole_record_sha256"], whole),
            "poem_inventory_change": prior["poem_inventory"] != [p.name for p in poems],
            "section_inventory_change": prior["section_inventory"] != [p.name for p in sections],
            "structure_changes": delta(prior["structural_inventory_sha256"], structure),
            "version_change": prior["corpus_schema_version"] != metadata.get("corpus_schema_version") or prior["version_status"] != metadata.get("version_status"),
            "source_checksum_change": prior["source_checksum_sha256"] != metadata.get("source_checksum_sha256"),
        }
    failures = {work: value for work, value in changes.items() if any(value.values())}
    result = {
        "created_at": dt.datetime.now().astimezone().isoformat(), "baseline": args.baseline,
        "work_count": len(changes), "canonical_record_count": sum(len(x["whole_record_sha256"]) for x in baseline["works"].values()),
        "combined_manifest_change": baseline["combined_manifest_sha256"] != sha(root / "manifests/poems.csv"),
        "work_failures": failures, "status": "pass" if not failures and baseline["combined_manifest_sha256"] == sha(root / "manifests/poems.csv") else "fail",
    }
    if args.write_log:
        stamp = dt.datetime.now().astimezone().strftime("%Y%m%dT%H%M%S"); target = root / "logs" / f"classical-tamil-research-frozen-regression-{stamp}.json"; target.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n"); result["log_path"] = str(target.relative_to(root))
    print(json.dumps(result, ensure_ascii=False, indent=2))
    if result["status"] != "pass": raise SystemExit(1)


if __name__ == "__main__": main()
