#!/usr/bin/env python3
"""Source-specific multi-object pipeline for Project Madurai Pattuppāṭṭu."""
from __future__ import annotations

import collections
import csv
import hashlib
import json
import re
import unicodedata
from pathlib import Path
from typing import Any

import yaml
from bs4 import BeautifulSoup

from corpuslib import ROOT, body_hash, canonical_body_text, markdown_literary_lines, read_frontmatter, write_json, write_work_issues

SOURCE_SET = ROOT / "sources/source-metadata/pattuppattu-source-set.json"
RAW_DIR = ROOT / "sources/raw-html/pattuppattu"
PARSED = ROOT / "sources/source-metadata/pattuppattu-parsed.json"
NORMALIZED = ROOT / "sources/source-metadata/pattuppattu-normalized.json"
SOURCE_METADATA = ROOT / "sources/source-metadata/pattuppattu.json"
RAW_TEXT = ROOT / "sources/raw-txt/pattuppattu.txt"
CORPUS = ROOT / "corpus/pattuppattu"
POEMS = CORPUS / "poems"
SECTIONS = CORPUS / "sections"
VALIDATION = ROOT / "manifests/pattuppattu-validation-report.json"

LINE_MARKER_RE = re.compile(r"(?:[ \u00a0]+)(?:\.\s*)*\d{1,3}\s*$")
SEPARATOR_RE = re.compile(r"^-{3,}$")
INTERNAL_HEADING_RE = re.compile(r"^(\d+)\.\s+(.+)$")
MURUGAN_LABELS = {
    "பன்னிரு கைகள்:", "முனிவர்:", "கந்தருவர்:", "கந்தருவ மகளிர்:",
    "திருமால்:", "உத்திரன்:", ".முப்பத்து மூவர்:", "அந்தணர்:", "வேலன்:",
    "குறமகளிர்:", "முருகன் உறையும் இடங்கள்:", ".முருகாற்றுப்படுத்தல்:", "அருவி :",
}
META_LABELS = {
    "பாடியவர்": "poet",
    "பாடப்பட்டவன்": "patron",
    "திணை": "thinai",
    "துறை": "thurai",
    "பாவகை": "metre",
}


def _sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _lines(path: Path) -> list[str]:
    soup = BeautifulSoup(path.read_bytes().decode("utf-8-sig"), "lxml")
    return [x.strip() for x in soup.get_text("\n").splitlines() if x.strip()]


def verify_source_set() -> tuple[dict[str, Any], list[dict[str, Any]]]:
    source_set = json.loads(SOURCE_SET.read_text(encoding="utf-8"))
    objects = source_set["source_objects"]
    if len(objects) != 10 or [x["record_number"] for x in objects] != list(range(1, 11)):
        raise RuntimeError("Pattuppāṭṭu requires exactly ten ordered source objects")
    seen_ids: set[str] = set()
    seen_hashes: set[str] = set()
    for obj in objects:
        path = ROOT / obj["source_file"]
        if not path.is_file() or path.stat().st_size == 0:
            raise RuntimeError(f"Missing or empty source object: {path}")
        digest = _sha256(path)
        if path.stat().st_size != obj["source_bytes"] or digest != obj["source_sha256"]:
            raise RuntimeError(f"Source checksum/size mismatch: {path}")
        if obj["source_object_id"] in seen_ids:
            raise RuntimeError(f"Duplicate source object ID: {obj['source_object_id']}")
        if digest in seen_hashes:
            raise RuntimeError(f"Byte-identical source objects: {path}")
        seen_ids.add(obj["source_object_id"])
        seen_hashes.add(digest)
        raw = path.read_bytes()
        if b"<html" not in raw.lower() and b"<!doctype" not in raw.lower():
            raise RuntimeError(f"Not an HTML response body: {path}")
        raw.decode("utf-8-sig")
    return source_set, objects


def _extract_metadata(lines: list[str], separator_index: int) -> tuple[list[str], dict[str, str | None]]:
    intro = lines[:separator_index]
    fields: dict[str, str | None] = {v: None for v in META_LABELS.values()}
    for line in intro:
        for label, key in META_LABELS.items():
            if line.startswith(label):
                value = re.sub(rf"^{re.escape(label)}\s*::?\s*", "", line).strip()
                fields[key] = value or None
    return intro, fields


def _parse_source_only(obj: dict[str, Any], lines: list[str]) -> dict[str, Any]:
    colophon_at = next(i for i, x in enumerate(lines) if "முற்றிற்று" in x)
    total_at = next(i for i, x in enumerate(lines[:colophon_at]) if x.startswith("மொத்த"))
    separator_at = next(i for i in range(total_at + 1, colophon_at)
                        if SEPARATOR_RE.match(lines[i].replace(" ", "")))
    intro, fields = _extract_metadata(lines, separator_at)
    source_body = lines[separator_at + 1:colophon_at]
    body: list[str] = []
    internal: list[dict[str, Any]] = []
    for value in source_body:
        heading = INTERNAL_HEADING_RE.match(value)
        structural = obj["source_object_id"] == "pmuni0067" and (heading or value in MURUGAN_LABELS)
        if structural:
            internal.append({
                "sequence": len(internal) + 1,
                "heading_as_printed": value,
                "start_line": len(body) + 1,
                "provenance": "printed by selected canonical source",
            })
            continue
        body.append(LINE_MARKER_RE.sub("", value).rstrip())
    for i, entry in enumerate(internal):
        entry["end_line"] = (internal[i + 1]["start_line"] - 1) if i + 1 < len(internal) else len(body)
    return {
        "poem_number": obj["record_number"],
        "record_type": "long_poem",
        "title": obj["work_title_tamil"],
        "title_as_printed": obj["work_title_as_printed"],
        "printed_intro_lines": intro,
        **fields,
        "lines": body,
        "source_note_lines": [],
        "colophon_as_printed": lines[colophon_at],
        "internal_structure": internal,
        "commentary_present": False,
    }


def _parse_mullai(obj: dict[str, Any], lines: list[str]) -> dict[str, Any]:
    heading_at = next(i for i, x in enumerate(lines) if i > 16 and x == "முல்லைப்பாட்டு")
    commentary_at = next(i for i, x in enumerate(lines[heading_at + 1:], heading_at + 1)
                         if INTERNAL_HEADING_RE.match(x))
    source_body = lines[heading_at + 1:commentary_at]
    body = [LINE_MARKER_RE.sub("", x).rstrip() for x in source_body]
    colophon = next((x for x in lines[commentary_at:] if "நப்பூதனார் பாடிய முல்லைப்பாட்டிற்கு" in x), None)
    return {
        "poem_number": obj["record_number"],
        "record_type": "long_poem",
        "title": obj["work_title_tamil"],
        "title_as_printed": obj["work_title_as_printed"],
        "printed_intro_lines": lines[16:heading_at + 1],
        "poet": "காவிரிப்பூம்பட்டினத்துப் பொன்வாணிகனார் மகனார் நப்பூதனார்",
        "patron": None,
        "thinai": None,
        "thurai": None,
        "metre": None,
        "lines": body,
        "source_note_lines": [],
        "colophon_as_printed": colophon,
        "internal_structure": [],
        "commentary_present": True,
        "commentary_boundary": {
            "literary_start_as_printed": source_body[0],
            "literary_end_as_printed": source_body[-1],
            "commentary_first_line_as_printed": lines[commentary_at],
        },
    }


def parse_all() -> dict[str, Any]:
    source_set, objects = verify_source_set()
    poems: list[dict[str, Any]] = []
    raw_text_parts: list[str] = []
    for obj in objects:
        path = ROOT / obj["source_file"]
        lines = _lines(path)
        raw_text_parts.extend([f"===== {obj['source_object_id']} =====", *lines, ""])
        poem = _parse_mullai(obj, lines) if obj["source_object_id"] == "pmuni0488" else _parse_source_only(obj, lines)
        poem.update({
            "source_object_id": obj["source_object_id"],
            "source_object_order": obj["source_order"],
            "source_file": obj["source_file"],
            "source_url": obj["source_url"],
            "source_sha256": obj["source_sha256"],
            "edition_type": obj["edition_type"],
            "status": "source-transcribed",
        })
        poems.append(poem)
    return {
        "parser": "pattuppattu-multi-object-v1",
        "title_tamil": "பத்துப்பாட்டு",
        "title_english": "Pattuppāṭṭu",
        "work_slug": "pattuppattu",
        "poems": poems,
        "source_objects": objects,
        "raw_text": "\n".join(raw_text_parts),
        "source_structure": "ten independently sourced long-poem records",
        "unparsed_fragments": [],
    }


def extract(force: bool = True, dry_run: bool = False, verbose: bool = False) -> None:
    data = parse_all()
    if dry_run:
        print("Would extract 10 independently preserved Pattuppāṭṭu source objects")
        return
    RAW_TEXT.parent.mkdir(parents=True, exist_ok=True)
    RAW_TEXT.write_text(data.pop("raw_text"), encoding="utf-8", newline="\n")
    write_json(PARSED, data, force=force)
    meta = {
        "work": "pattuppattu",
        "source_name": "Project Madurai",
        "accessed_date": "2026-07-28",
        "source_artifact_type": "ten exact HTTP HTML response bodies",
        "source_set_file": str(SOURCE_SET.relative_to(ROOT)),
        "source_objects": data["source_objects"],
        "individual_checksums_authoritative": True,
    }
    write_json(SOURCE_METADATA, meta, force=True)
    if verbose:
        print("Extracted ten Pattuppāṭṭu long-poem records")


def normalize(force: bool = True, dry_run: bool = False, verbose: bool = False) -> None:
    data = json.loads(PARSED.read_text(encoding="utf-8"))
    for poem in data["poems"]:
        for key in ("lines", "source_note_lines", "printed_intro_lines"):
            poem[key] = [unicodedata.normalize("NFC", x.replace("\r", "").strip()) for x in poem.get(key, [])]
    data["normalization"] = "Unicode NFC; LF line endings; HTML entity decoding; line-end layout numbers removed"
    if dry_run:
        print("Would normalize ten Pattuppāṭṭu records")
        return
    write_json(NORMALIZED, data, force=force)
    if verbose:
        print("Normalized ten Pattuppāṭṭu records conservatively")


def _markdown(poem: dict[str, Any]) -> str:
    fm = {
        "schema_version": "1.0.0",
        "work": "பத்துப்பாட்டு",
        "work_english": "Pattuppāṭṭu",
        "work_id": "pattuppattu",
        "work_slug": "pattuppattu",
        "record_type": "long_poem",
        "poem_number": poem["poem_number"],
        "poem_number_as_printed": None,
        "source_order": poem["source_object_order"],
        "section": f"{poem['poem_number']:03d}-{poem['title']}",
        "section_source": "Generated source-order navigation for one canonical long poem",
        "title": poem["title"],
        "title_as_printed": poem["title_as_printed"],
        "thinai": poem.get("thinai"),
        "thinai_source": "Project Madurai printed metadata" if poem.get("thinai") else None,
        "speaker": None,
        "speaker_source": None,
        "poet": poem.get("poet"),
        "poet_source": "Project Madurai printed metadata or colophon" if poem.get("poet") else None,
        "patron": poem.get("patron"),
        "patron_source": "Project Madurai printed metadata" if poem.get("patron") else None,
        "first_line": poem["lines"][0] if poem["lines"] else "",
        "line_count": len(poem["lines"]),
        "textual_status": "complete",
        "canonical_text_available": True,
        "candidate_texts_available": False,
        "lacuna_present": False,
        "lacuna_location": None,
        "source_note_available": False,
        "source_note_source": None,
        "extraction_status": "success",
        "internal_structure_available": bool(poem["internal_structure"]),
        "commentary_present": poem["commentary_present"],
        "commentary_source": poem["source_object_id"] if poem["commentary_present"] else None,
        "source": "Project Madurai",
        "source_url": poem["source_url"],
        "project_madurai_id": poem["source_object_id"],
        "source_object_id": poem["source_object_id"],
        "source_object_order": poem["source_object_order"],
        "source_file": poem["source_file"],
        "source_sha256": poem["source_sha256"],
        "language": "Tamil",
        "script": "Tamil",
        "status": "source-transcribed",
        "editorial_changes": False,
    }
    y = yaml.safe_dump(fm, allow_unicode=True, sort_keys=False).strip()
    return f"---\n{y}\n---\n\n# {poem['title']}\n\n" + "\n".join(poem["lines"]) + "\n"


def split(force: bool = True, dry_run: bool = False, verbose: bool = False) -> None:
    data = json.loads(NORMALIZED.read_text(encoding="utf-8"))
    if dry_run:
        print("Would write 10 long-poem records and 10 source-order navigation sections")
        return
    POEMS.mkdir(parents=True, exist_ok=True)
    SECTIONS.mkdir(parents=True, exist_ok=True)
    expected_poems = {f"{n:03d}.md" for n in range(1, 11)}
    expected_sections = {f"{n:03d}-{data['poems'][n-1]['source_object_id']}.md" for n in range(1, 11)}
    unexpected = [p for p in POEMS.rglob("*") if p.is_file() and (p.parent != POEMS or p.name not in expected_poems)]
    unexpected += [p for p in SECTIONS.rglob("*") if p.is_file() and (p.parent != SECTIONS or p.name not in expected_sections)]
    if unexpected:
        raise RuntimeError(f"Refusing regeneration with unexpected physical files: {[str(x.relative_to(CORPUS)) for x in unexpected]}")
    rendered = []
    structure = []
    for poem in data["poems"]:
        text = _markdown(poem)
        name = f"{poem['poem_number']:03d}.md"
        (POEMS / name).write_text(text, encoding="utf-8", newline="\n")
        section_name = f"{poem['poem_number']:03d}-{poem['source_object_id']}.md"
        (SECTIONS / section_name).write_text(
            f"# {poem['title']}\n\nGenerated navigation mirror of canonical record `{name}`; it is not an additional ancient division.\n\n"
            + "\n".join(poem["lines"]) + "\n", encoding="utf-8", newline="\n")
        rendered.append(text.split("---\n", 2)[-1].lstrip())
        structure.append({
            "record_number": poem["poem_number"],
            "title_as_printed": poem["title_as_printed"],
            "source_object_id": poem["source_object_id"],
            "internal_structure": poem["internal_structure"],
            "commentary_present": poem["commentary_present"],
            "colophon_as_printed": poem.get("colophon_as_printed"),
        })
    (CORPUS / "full-text.md").write_text(
        "# பத்துப்பாட்டு — source transcription\n\nTen source-ordered long-poem records. Generated navigation is not source-printed anthology structure.\n\n"
        + "\n".join(rendered), encoding="utf-8", newline="\n")
    write_json(CORPUS / "structure-inventory.json", {"records": structure}, force=True)
    source_set = json.loads(SOURCE_SET.read_text(encoding="utf-8"))
    metadata = {
        "corpus_schema_version": "1.0.0",
        "version_status": "frozen",
        "title_tamil": "பத்துப்பாட்டு",
        "title_english": "Pattuppāṭṭu",
        "work_slug": "pattuppattu",
        "work_id": "pattuppattu",
        "collection": "பத்துப்பாட்டு",
        "expected_poem_count": 10,
        "numbered_poem_record_count": 10,
        "available_poem_count": 10,
        "missing_poems": [],
        "source_name": "Project Madurai",
        "source_model": "ten independently preserved source objects",
        "source_set_file": str(SOURCE_SET.relative_to(ROOT)),
        "source_objects": source_set["source_objects"],
        "individual_checksums_authoritative": True,
        "accessed_date": "2026-07-28",
        "encoding": "UTF-8",
        "normalization": "Unicode NFC; HTML entity decoding; LF; source layout line numbers removed",
        "navigation_sections": {"type": "one generated source-order mirror per long poem", "count": 10},
        "declared_and_extracted_line_counts": [
            {"source_object_id": "pmuni0067", "declared_line_count_as_printed": 317, "extracted_literary_line_count": 317},
            {"source_object_id": "pmuni0063", "declared_line_count_as_printed": 248, "extracted_literary_line_count": 248},
            {"source_object_id": "pmuni0064", "declared_line_count_as_printed": 269, "extracted_literary_line_count": 269},
            {"source_object_id": "pmuni0069", "declared_line_count_as_printed": 500, "extracted_literary_line_count": 501},
            {"source_object_id": "pmuni0488", "declared_line_count_as_printed": 103, "extracted_literary_line_count": 103},
            {"source_object_id": "pmuni0071", "declared_line_count_as_printed": 782, "extracted_literary_line_count": 782},
            {"source_object_id": "pmuni0070", "declared_line_count_as_printed": 188, "extracted_literary_line_count": 188},
            {"source_object_id": "pmuni0073", "declared_line_count_as_printed": 261, "extracted_literary_line_count": 262},
            {"source_object_id": "pmuni0077", "declared_line_count_as_printed": 301, "extracted_literary_line_count": 302},
            {"source_object_id": "pmuni0078", "declared_line_count_as_printed": 583, "extracted_literary_line_count": 583}
        ],
        "notes": [
            "Internal headings remain subordinate structure and never become anthology-level records.",
            "pmuni0488 is commentary-bearing; only its contiguous literary block enters the canonical body.",
            "The Project Madurai pages print declared line counts that differ by one from the independently extracted BR-delimited literary lines in three records. The corpus preserves all printed literary lines and records the discrepancies without speculative line merging.",
            "Version 1.0.0 freezes the ten source identities and checksums, record order and mapping, canonical bodies and provenance, Mullai commentary boundary, nineteen-heading Murugan structure, navigation strategy, line-count discrepancies, validation expectations, physical inventory and deterministic regeneration."
        ],
    }
    write_json(CORPUS / "metadata.json", metadata, force=True)
    if verbose:
        print("Wrote ten Pattuppāṭṭu records and ten navigation sections")


def validate(dry_run: bool = False, verbose: bool = False) -> dict[str, Any]:
    data = json.loads(NORMALIZED.read_text(encoding="utf-8"))
    source = {p["poem_number"]: p for p in data["poems"]}
    expected_poems = {f"{n:03d}.md" for n in range(1, 11)}
    expected_sections = {f"{p['poem_number']:03d}-{p['source_object_id']}.md" for p in data["poems"]}
    physical = [p for p in POEMS.rglob("*") if p.is_file()]
    sections = [p for p in SECTIONS.rglob("*") if p.is_file()]
    issues: list[dict[str, Any]] = []
    fidelity = []
    required = [
        "schema_version", "work", "work_id", "poem_number", "record_type", "textual_status",
        "canonical_text_available", "candidate_texts_available", "lacuna_present", "lacuna_location",
        "extraction_status", "thinai", "thinai_source", "poet", "poet_source", "speaker",
        "speaker_source", "source_note_available", "source_note_source", "source_object_id",
        "source_object_order", "source_sha256", "commentary_present",
    ]
    direct = {p.name for p in physical if p.parent == POEMS}
    unexpected = [str(p.relative_to(POEMS)) for p in physical if p.parent != POEMS or p.name not in expected_poems]
    sec_direct = {p.name for p in sections if p.parent == SECTIONS}
    sec_unexpected = [str(p.relative_to(SECTIONS)) for p in sections if p.parent != SECTIONS or p.name not in expected_sections]
    def add(n, kind, message):
        issues.append({"work": "pattuppattu", "poem_number": n, "issue_type": kind, "severity": "error",
                       "message": message, "source_file": "", "markdown_file": ""})
    if len(physical) != 10 or direct != expected_poems or unexpected:
        add(None, "physical_poem_inventory", f"count={len(physical)} missing={sorted(expected_poems-direct)} unexpected={unexpected}")
    if len(sections) != 10 or sec_direct != expected_sections or sec_unexpected:
        add(None, "physical_section_inventory", f"count={len(sections)} missing={sorted(expected_sections-sec_direct)} unexpected={sec_unexpected}")
    seen_numbers = collections.defaultdict(list)
    hashes = collections.defaultdict(list)
    schema_pass = 0
    for name in sorted(expected_poems):
        path = POEMS / name
        if not path.is_file():
            continue
        fm, body = read_frontmatter(path)
        n = int(fm["poem_number"])
        seen_numbers[n].append(name)
        missing_keys = [k for k in required if k not in fm]
        if missing_keys:
            add(n, "missing_schema_keys", str(missing_keys))
        else:
            schema_pass += 1
        md_lines = markdown_literary_lines(body)
        sh = body_hash(source[n]["lines"])
        mh = body_hash(md_lines)
        note_lines = []
        if "## Source note (as printed)" in body:
            note_lines = [x.strip() for x in body.split("## Source note (as printed)", 1)[1].splitlines() if x.strip()]
        note_match = canonical_body_text(note_lines) == canonical_body_text(source[n]["source_note_lines"])
        fidelity.append({"poem_number": n, "source_body_hash_sha256": sh, "markdown_body_hash_sha256": mh,
                         "source_output_match": sh == mh, "source_note_match": note_match})
        if sh != mh:
            add(n, "source_output_mismatch", "Canonical body differs from extracted source block")
        if not note_match:
            add(n, "source_note_output_mismatch", "Source note differs from extracted source-note representation")
        hashes[mh].append(n)
        if not md_lines:
            add(n, "empty_canonical_body", "Long-poem record has no canonical literary text")
        if fm["source_sha256"] != source[n]["source_sha256"]:
            add(n, "source_checksum_mismatch", "Poem provenance checksum differs from selected source object")
    for n, names in seen_numbers.items():
        if len(names) > 1:
            add(n, "duplicate_yaml_poem_number", str(names))
    duplicates = [ns for ns in hashes.values() if len(ns) > 1]
    if duplicates:
        add(None, "duplicate_poem_body", str(duplicates))
    report = {
        "work": "pattuppattu",
        "source_record_count": len(data["poems"]),
        "canonical_poem_files": len(physical),
        "navigation_sections": len(sections),
        "schema_files_checked": len(expected_poems & direct),
        "schema_files_passing": schema_pass,
        "schema_files_failing": len(expected_poems & direct) - schema_pass,
        "source_output_matches": sum(x["source_output_match"] for x in fidelity),
        "source_note_matches": sum(x["source_note_match"] for x in fidelity),
        "duplicate_full_bodies": duplicates,
        "source_output_fidelity": fidelity,
        "errors": len(issues),
        "warnings": 0,
        "info": 0,
        "issues": issues,
        "status": "pass" if not issues else "fail",
    }
    if not dry_run:
        write_json(VALIDATION, report, force=True)
        write_json(ROOT / "manifests/validation-report.json", report, force=True)
        write_work_issues("pattuppattu", issues)
    if verbose:
        print(f"Validation: {report['status']}; {report['errors']} errors")
    return report
