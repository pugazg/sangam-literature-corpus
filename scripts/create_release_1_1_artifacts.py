#!/usr/bin/env python3
"""Create the additive 28-work Classical Tamil Corpus 1.1.0 checkpoint files."""
from __future__ import annotations

import csv
import datetime as dt
import hashlib
import json
import re
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
VERSION = "1.1.0"
SOURCE = ROOT / "sources/raw-html/tolkappiyam-pmuni0100.html"


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def dump(path: Path, value: object) -> None:
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")


def record_parts(path: Path) -> tuple[dict, str, str]:
    text = path.read_text(encoding="utf-8")
    match = re.match(r"\A---\n(.*?)\n---\n(.*)\Z", text, re.S)
    if not match:
        raise ValueError(f"malformed canonical record: {path}")
    front = yaml.safe_load(match.group(1)) or {}
    body_part, marker, note_part = match.group(2).partition("## Source note (as printed)")
    lines = body_part.splitlines()
    if lines and lines[0].startswith("# "):
        lines = lines[1:]
    return front, "\n".join(lines).strip("\n"), note_part.strip("\n") if marker else ""


def write_csv(path: Path, rows: list[dict]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]), lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def create_fingerprint(release_path: Path) -> str:
    output = ROOT / "manifests/repository-content-hashes-1.1.0.sha256"
    roots = ("apparatus", "corpus", "docs", "issues", "manifests", "scripts", "sources", "tests")
    root_files = (".gitignore", "README.md", "requirements.txt")
    excluded = {output.name}

    def included(path: Path) -> bool:
        rel = path.relative_to(ROOT)
        if path.name in excluded or any(part in {".git", "__pycache__", ".pytest_cache"} for part in rel.parts):
            return False
        if path.name.startswith(".") or path.suffix in {".lock", ".tmp", ".pyc", ".bak"}:
            return False
        return not (rel.parts[0] == "manifests" and path.name.endswith("-validation-report.json"))

    release = json.loads(release_path.read_text(encoding="utf-8"))
    projection = dict(release)
    for key in ("repository_content_manifest_sha256", "release_content_commit", "release_content_tree", "release_checkpoint_commit", "release_checkpoint_tree"):
        projection[key] = None
    projection_bytes = (json.dumps(projection, ensure_ascii=False, sort_keys=True, separators=(",", ":")) + "\n").encode()
    paths = [p for root in roots for p in (ROOT / root).rglob("*") if p.is_file() and included(p)]
    paths.extend(ROOT / name for name in root_files)
    lines = []
    for path in sorted(paths, key=lambda p: p.relative_to(ROOT).as_posix()):
        rel = path.relative_to(ROOT).as_posix()
        digest = hashlib.sha256(projection_bytes if path == release_path else path.read_bytes()).hexdigest()
        suffix = " [canonical projection; self-referential and commit fields null]" if path == release_path else ""
        lines.append(f"{digest}  {rel}{suffix}")
    output.write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")
    fingerprint = sha(output)
    release["repository_content_manifest_sha256"] = fingerprint
    dump(release_path, release)
    return fingerprint


def main() -> None:
    now = dt.datetime.now().astimezone().isoformat()
    old_sources = json.loads((ROOT / "manifests/repository-source-inventory-1.0.0.json").read_text(encoding="utf-8"))
    old_works = json.loads((ROOT / "manifests/repository-frozen-work-inventory-1.0.0.json").read_text(encoding="utf-8"))
    old_records = json.loads((ROOT / "manifests/repository-record-inventory-1.0.0.json").read_text(encoding="utf-8"))
    old_protected = json.loads((ROOT / "manifests/repository-protected-conditions-1.0.0.json").read_text(encoding="utf-8"))
    meta = json.loads((ROOT / "corpus/tolkappiyam/metadata.json").read_text(encoding="utf-8"))
    report = json.loads((ROOT / "manifests/tolkappiyam-validation-report.json").read_text(encoding="utf-8"))
    if meta.get("corpus_schema_version") != "1.0.0" or meta.get("version_status") != "frozen":
        raise ValueError("Tolkappiyam must be independently frozen before repository release")
    if sha(SOURCE) != "16b2edf314763ef491bdc498c0017de33e7e190753587b230bbafcd03219f5da":
        raise ValueError("Tolkappiyam source checksum mismatch")

    files = sorted((ROOT / "corpus/tolkappiyam/nurpas").glob("*.md"))
    if [p.name for p in files] != [f"{n:04d}.md" for n in range(1, 1603)]:
        raise ValueError("Tolkappiyam physical record inventory mismatch")
    bodies, notes = {}, {}
    for path in files:
        front, body, note = record_parts(path)
        if front.get("canonical_record_id") != f"tolkappiyam-{int(path.stem):04d}":
            raise ValueError(f"canonical ID mismatch: {path}")
        bodies[path.name] = hashlib.sha256(body.encode()).hexdigest()
        notes[path.name] = hashlib.sha256(note.encode()).hexdigest()

    source_row = {
        "programme_id": "tolkappiyam-grammar",
        "work_id": "tolkappiyam",
        "work_order": 28,
        "source_object_order": 1,
        "source_object_id": "pmuni0100@16123f742503283e46f0ed321802a46f99df6392",
        "project_madurai_id": "pmuni0100",
        "source_url": "https://www.projectmadurai.org/pm_etexts/utf8/pmuni0100.html",
        "title_as_printed": meta.get("title_tamil"),
        "artifact_type": "preserved HTML object imported byte-identically from pinned upstream commit",
        "edition_type": "source-only electronic text",
        "commentary_present": False,
        "selected_as_canonical": True,
        "local_path": "sources/raw-html/tolkappiyam-pmuni0100.html",
        "byte_size": SOURCE.stat().st_size,
        "sha256": sha(SOURCE),
        "retrieval_or_preservation_date": "2026-08-03",
    }
    sources = old_sources["source_objects"] + [source_row]
    work_row = {
        "work_id": "tolkappiyam", "canonical_title": meta.get("title_tamil"),
        "programme_id": "tolkappiyam-grammar", "corpus_schema_version": "1.0.0",
        "version_status": "frozen", "source_object_count": 1,
        "canonical_record_count": 1602, "canonical_text_count": 1602,
        "section_count": 30, "validation_status": "pass",
        "error_count": 0, "warning_count": 0, "information_count": 12,
    }
    works = sorted(old_works["works"] + [work_row], key=lambda row: row["work_id"])
    record_row = {
        "work_id": "tolkappiyam", "programme_id": "tolkappiyam-grammar",
        "record_count": 1602, "record_directory": "corpus/tolkappiyam/nurpas",
        "record_filenames": [p.name for p in files], "section_count": 30,
        "section_filenames": [f"adhikarams/{n:02d}.md" for n in range(1, 4)] + [f"iyals/{n:02d}.md" for n in range(1, 28)],
        "canonical_body_sha256": bodies, "source_note_sha256": notes,
    }
    records = sorted(old_records["works"] + [record_row], key=lambda row: row["work_id"])
    if len(works) != 28 or sum(row["record_count"] for row in records) != 7234:
        raise ValueError("release inventory must contain 28 works and 7,234 records")

    source_doc = {"release_version": VERSION, "created_at": now, "association_count": len(sources), "unique_source_object_count": len({r["local_path"] for r in sources}), "source_objects": sources}
    work_doc = {"release_version": VERSION, "created_at": now, "work_count": 28, "core_sangam_work_count": 9, "pathinenkilkanakku_work_count": 18, "tolkappiyam_work_count": 1, "canonical_record_count": 7234, "works": works}
    record_doc = {"release_version": VERSION, "created_at": now, "work_count": 28, "canonical_record_count": 7234, "works": records}
    protected = old_protected["conditions"] + [{"work_id": "tolkappiyam", "condition": "exact pinned pmuni0100 source; 3 adhikaram, 27 iyal and 1,602 nurpa; twelve warnings preserved; source/editorial headings separated", "policy": "preserve and validate; no web-application or editorial-field leakage"}]
    dump(ROOT / "manifests/repository-source-inventory-1.1.0.json", source_doc)
    dump(ROOT / "manifests/repository-frozen-work-inventory-1.1.0.json", work_doc)
    dump(ROOT / "manifests/repository-record-inventory-1.1.0.json", record_doc)
    dump(ROOT / "manifests/repository-protected-conditions-1.1.0.json", {"release_version": VERSION, "conditions": protected})
    write_csv(ROOT / "manifests/repository-source-inventory-1.1.0.csv", sources)
    write_csv(ROOT / "manifests/repository-frozen-work-inventory-1.1.0.csv", works)

    release_path = ROOT / "manifests/classical-tamil-corpus-release-1.1.0.json"
    release = {
        "release_name": "Classical Tamil Corpus", "release_version": VERSION,
        "release_status": "verified-content-pending-git-checkpoint", "work_count": 28,
        "canonical_record_count": 7234, "poem_record_count": 5632, "nurpa_record_count": 1602,
        "approved_poems_csv_sha256": sha(ROOT / "manifests/poems.csv"),
        "records_csv_sha256": sha(ROOT / "manifests/records.csv"),
        "repository_content_manifest_sha256": None,
        "release_content_commit": None, "release_content_tree": None,
        "release_checkpoint_commit": None, "release_checkpoint_tree": None,
        "release_tag": "classical-tamil-corpus-v1.1.0",
        "previous_release_tag": "classical-tamil-corpus-v1.0.0",
        "source_inventory": "manifests/repository-source-inventory-1.1.0.json",
        "work_inventory": "manifests/repository-frozen-work-inventory-1.1.0.json",
        "record_inventory": "manifests/repository-record-inventory-1.1.0.json",
        "protected_conditions": "manifests/repository-protected-conditions-1.1.0.json",
        "rights_review": "docs/source-rights-and-redistribution-review.md",
    }
    dump(release_path, release)
    fingerprint = create_fingerprint(release_path)
    print(json.dumps({"works": 28, "records": 7234, "sources": len(sources), "fingerprint": fingerprint}, indent=2))


if __name__ == "__main__":
    main()
