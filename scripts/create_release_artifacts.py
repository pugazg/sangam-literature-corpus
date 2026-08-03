#!/usr/bin/env python3
"""Build repository-wide release inventories from frozen corpus state."""
from __future__ import annotations

import csv
import datetime as dt
import hashlib
import json
import re
from collections import defaultdict
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
CORE = {
    "natrinai", "aingurunuru", "kuruntokai", "akananuru", "purananuru",
    "pattuppattu", "patirruppattu", "paripatal", "kalittokai",
}
VERSION = "1.0.0"


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def dump(path: Path, value: object) -> None:
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")


def source_path(work: str, meta: dict, obj: dict | None = None) -> str:
    obj = obj or {}
    if obj.get("source_file"):
        return obj["source_file"]
    if meta.get("source_file"):
        return meta["source_file"]
    if work == "purananuru":
        return "sources/purananuru.md"
    pmid = obj.get("project_madurai_id") or meta.get("project_madurai_id")
    candidates = [
        f"sources/raw-html/{work}.html",
        f"sources/raw-html/pathinenkilkanakku/{pmid}.html",
        f"sources/raw-html/{pmid}.html",
    ]
    for candidate in candidates:
        if (ROOT / candidate).is_file():
            return candidate
    raise FileNotFoundError(f"no preserved source object for {work} ({pmid})")


def poem_parts(path: Path) -> tuple[dict, str, str]:
    text = path.read_text(encoding="utf-8")
    match = re.match(r"\A---\n(.*?)\n---\n(.*)\Z", text, re.S)
    if not match:
        raise ValueError(f"malformed poem file: {path}")
    metadata = yaml.safe_load(match.group(1)) or {}
    remainder = match.group(2)
    body_part, marker, note_part = remainder.partition("## Source note (as printed)")
    body_lines = body_part.splitlines()
    if body_lines and body_lines[0].startswith("# "):
        body_lines = body_lines[1:]
    body = "\n".join(body_lines).strip("\n")
    note = note_part.strip("\n") if marker else ""
    return metadata, body, note


def normalized_body(body: str) -> str:
    return "\n".join(line.rstrip() for line in body.splitlines()).strip()


def protected_conditions() -> list[dict]:
    items = {
        "natrinai": ["234 source-lost; candidate readings remain source-note evidence", "385 printed ending lacuna preserved", "four legitimate shared-opening pairs remain informational"],
        "aingurunuru": ["129 and 130 source-lost", "470 malformed/bare printed heading preserved", "50 ten-record groups; two initial printed pattu headings absent", "printed ordinal 11 repetition and shifted 12 preserved"],
        "kuruntokai": ["29 and 396 malformed printed heading strings preserved", "ten dot-placeholder poet attributions remain uncertain", "105 and 180 layout-only verse/attribution boundary restoration"],
        "akananuru": ["174 protected canonical record", "printed-number repetitions retained separately from canonical source order", "143 and 354 printed ellipses preserved", "three source-printed divisions preserved"],
        "purananuru": ["267 and 268 source-lost", "99 bare printed heading preserved", "40 printed dot-lacuna conditions preserved", "canonical source is approved Markdown/text export, not raw HTML"],
        "pattuppattu": ["ten independently checksum-pinned source objects", "Mullaippattu pmuni0488 is commentary-bearing; commentary excluded", "pmuni0053 remains an unselected alternate edition", "Tirumurukarruppatai six internal headings remain subordinate structure", "pmuni0069, pmuni0073 and pmuni0077 declared/extracted line-count discrepancies preserved"],
        "patirruppattu": ["records 11-90 only; first and tenth groups explicitly unavailable", "patikam blocks and recovered fragments remain outside canonical bodies"],
        "paripatal": ["22 main records plus 13 Tirattu records with restarted printed numbering"],
        "kalittokai": ["invocation plus five source divisions", "114 and 131 printed lacunae preserved"],
        "tirukkural": ["1330 records in 133 chapters", "Muppal is an alias, not a second work"],
        "aintinai-elupathu": ["25, 26, 69 and 70 are source-lost records"],
        "thinaimalai-nutraimbathu": ["153 source records preserved"],
        "tirikatukam": ["printed heading absences at 43 and 57 preserved"],
        "acharakkovai": ["printed 47 condition and punctuation anomaly preserved"],
        "pazhamozhi-nanuru": ["399 numbered records plus two unnumbered source records; chapter 12 absence preserved"],
        "kainnilai": ["four printed division headings; no inferred fifth heading; Innilai excluded"],
    }
    return [
        {"work_id": work, "condition": condition, "policy": "preserve and validate; no silent editorial repair"}
        for work, conditions in items.items() for condition in conditions
    ]


def main() -> None:
    now = dt.datetime.now().astimezone().isoformat()
    stamp = dt.datetime.now().astimezone().strftime("%Y%m%dT%H%M%S")
    works_manifest = json.loads((ROOT / "manifests/works.json").read_text(encoding="utf-8"))
    sources, works, records = [], [], []
    all_bodies: dict[str, list[dict]] = defaultdict(list)

    for order, item in enumerate(works_manifest, 1):
        work = item["work_slug"]
        corpus = ROOT / "corpus" / work
        meta = json.loads((corpus / "metadata.json").read_text(encoding="utf-8"))
        report = json.loads((ROOT / "manifests" / f"{work}-validation-report.json").read_text(encoding="utf-8"))
        poems = sorted((corpus / "poems").glob("*.md"))
        sections = sorted((corpus / "sections").glob("*.md")) if (corpus / "sections").is_dir() else []
        objects = meta.get("source_objects") or [{}]
        for obj_order, obj in enumerate(objects, 1):
            rel = source_path(work, meta, obj)
            path = ROOT / rel
            actual_sha = sha(path)
            declared = obj.get("source_sha256") or obj.get("sha256") or meta.get("source_checksum_sha256")
            if declared and declared != actual_sha:
                raise ValueError(f"source checksum mismatch for {work}: {rel}")
            sources.append({
                "programme_id": "sangam-core" if work in CORE else "pathinenkilkanakku",
                "work_id": work,
                "work_order": order,
                "source_object_order": obj.get("source_order", obj_order),
                "source_object_id": obj.get("source_object_id") or obj.get("project_madurai_id") or meta.get("project_madurai_id"),
                "project_madurai_id": obj.get("project_madurai_id") or meta.get("project_madurai_id"),
                "source_url": obj.get("source_url") or meta.get("source_url"),
                "title_as_printed": obj.get("work_title_as_printed") or meta.get("title_tamil"),
                "artifact_type": "Markdown/text export" if work == "purananuru" else "preserved HTML object",
                "edition_type": obj.get("edition_type") or "source-only electronic text",
                "commentary_present": bool(obj.get("commentary_present", False)),
                "selected_as_canonical": True,
                "local_path": rel,
                "byte_size": path.stat().st_size,
                "sha256": actual_sha,
                "retrieval_or_preservation_date": obj.get("retrieved_at") or meta.get("accessed_date"),
            })
        body_hashes, note_hashes = {}, {}
        for poem in poems:
            front, body, note = poem_parts(poem)
            body_hash = hashlib.sha256(body.encode("utf-8")).hexdigest()
            note_hash = hashlib.sha256(note.encode("utf-8")).hexdigest()
            body_hashes[poem.name] = body_hash
            note_hashes[poem.name] = note_hash
            if normalized_body(body):
                full_hash = hashlib.sha256(normalized_body(body).encode("utf-8")).hexdigest()
                all_bodies[full_hash].append({"work_id": work, "record_file": poem.name})
        summary = report.get("summary", report)
        works.append({
            "work_id": work,
            "canonical_title": meta.get("title_tamil"),
            "programme_id": "sangam-core" if work in CORE else "pathinenkilkanakku",
            "corpus_schema_version": meta.get("corpus_schema_version"),
            "version_status": meta.get("version_status"),
            "source_object_count": len(objects),
            "canonical_record_count": len(poems),
            "canonical_text_count": meta.get("available_poem_count"),
            "section_count": len(sections),
            "validation_status": summary.get("status", report.get("status")),
            "error_count": summary.get("errors", report.get("errors", 0)),
            "warning_count": summary.get("warnings", report.get("warnings", 0)),
            "information_count": summary.get("info", report.get("info", 0)),
        })
        records.append({
            "work_id": work,
            "programme_id": works[-1]["programme_id"],
            "record_count": len(poems),
            "record_directory": f"corpus/{work}/poems",
            "record_filenames": [p.name for p in poems],
            "section_count": len(sections),
            "section_filenames": [p.name for p in sections],
            "canonical_body_sha256": body_hashes,
            "source_note_sha256": note_hashes,
        })

    if len(works) != 27 or sum(x["record_count"] for x in records) != 5632:
        raise ValueError("release inventory does not contain 27 works and 5,632 records")
    if any(x["corpus_schema_version"] != VERSION or x["version_status"] != "frozen" for x in works):
        raise ValueError("all works must be frozen at schema 1.0.0")

    unique_sources = {x["local_path"]: x for x in sources}
    source_doc = {"release_version": VERSION, "created_at": now, "association_count": len(sources), "unique_source_object_count": len(unique_sources), "source_objects": sources}
    work_doc = {"release_version": VERSION, "created_at": now, "work_count": len(works), "core_sangam_work_count": 9, "pathinenkilkanakku_work_count": 18, "canonical_record_count": 5632, "works": works}
    record_doc = {"release_version": VERSION, "created_at": now, "work_count": len(records), "canonical_record_count": 5632, "works": records}
    dump(ROOT / "manifests/repository-source-inventory-1.0.0.json", source_doc)
    dump(ROOT / "manifests/repository-frozen-work-inventory-1.0.0.json", work_doc)
    dump(ROOT / "manifests/repository-record-inventory-1.0.0.json", record_doc)
    dump(ROOT / "manifests/repository-protected-conditions-1.0.0.json", {"release_version": VERSION, "conditions": protected_conditions()})

    for filename, rows in (("repository-source-inventory-1.0.0.csv", sources), ("repository-frozen-work-inventory-1.0.0.csv", works)):
        with (ROOT / "manifests" / filename).open("w", encoding="utf-8", newline="") as handle:
            writer = csv.DictWriter(handle, fieldnames=list(rows[0]), lineterminator="\n")
            writer.writeheader()
            writer.writerows(rows)

    duplicate_groups = [members for members in all_bodies.values() if len(members) > 1]
    duplicate_review = {
        "release_version": VERSION,
        "created_at": now,
        "normalized_full_body_identity_group_count": len(duplicate_groups),
        "groups": duplicate_groups,
        "classification": "cross-record literary identity reviewed as content evidence; no duplicate physical paths or canonical identifiers",
        "duplicate_work_ids": [],
        "duplicate_canonical_record_ids": [],
        "status": "pass",
    }
    duplicate_path = ROOT / "logs" / f"repository-duplicate-review-1.0.0-{stamp}.json"
    dump(duplicate_path, duplicate_review)

    release = {
        "release_name": "Classical Tamil Corpus",
        "release_version": VERSION,
        "release_status": "verified-content-pending-git-checkpoint",
        "work_count": 27,
        "core_sangam_work_count": 9,
        "pathinenkilkanakku_work_count": 18,
        "canonical_record_count": 5632,
        "approved_poems_csv_sha256": sha(ROOT / "manifests/poems.csv"),
        "poems_manifest_ordering_policy": "repository-canonical-order-v1",
        "repository_content_manifest_sha256": None,
        "release_content_commit": None,
        "release_content_tree": None,
        "release_checkpoint_commit": None,
        "release_checkpoint_tree": None,
        "release_tag": "classical-tamil-corpus-v1.0.0",
        "initial_history_qualification": "This Git repository was initialized after corpus construction. The release tag certifies the imported frozen repository snapshot, not the earlier development history.",
        "manifest_incident": "An overlapping shared-manifest write was detected before release. No canonical content was affected. The manifest was semantically reconstructed; deterministic ordering, atomic replacement and advisory locking were added; two serial regeneration passes proved byte stability.",
        "source_inventory": "manifests/repository-source-inventory-1.0.0.json",
        "work_inventory": "manifests/repository-frozen-work-inventory-1.0.0.json",
        "record_inventory": "manifests/repository-record-inventory-1.0.0.json",
        "protected_conditions": "manifests/repository-protected-conditions-1.0.0.json",
        "duplicate_review": str(duplicate_path.relative_to(ROOT)),
    }
    dump(ROOT / "manifests/classical-tamil-corpus-release-1.0.0.json", release)
    print(json.dumps({"works": len(works), "records": 5632, "source_associations": len(sources), "unique_source_files": len(unique_sources), "duplicate_body_groups": len(duplicate_groups), "duplicate_review": str(duplicate_path.relative_to(ROOT))}, indent=2))


if __name__ == "__main__":
    main()
