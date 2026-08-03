#!/usr/bin/env python3
"""Source-specific, source-faithful pipeline for Project Madurai pmuni0087."""
from __future__ import annotations

import collections
import hashlib
import json
import re
import unicodedata
from pathlib import Path
from typing import Any

import yaml
from bs4 import BeautifulSoup, NavigableString

from corpuslib import (
    ROOT, body_hash, canonical_body_text, markdown_literary_lines,
    read_frontmatter, write_json, write_work_issues,
)

RAW = ROOT / "sources/raw-html/paripatal.html"
RAW_TXT = ROOT / "sources/raw-txt/paripatal.txt"
PARSED = ROOT / "sources/source-metadata/paripatal-parsed.json"
NORMALIZED = ROOT / "sources/source-metadata/paripatal-normalized.json"
SOURCE_META = ROOT / "sources/source-metadata/paripatal.json"
RECON = ROOT / "sources/source-metadata/paripatal-reconnaissance.json"
CORPUS = ROOT / "corpus/paripatal"
POEMS = CORPUS / "poems"
SECTIONS = CORPUS / "sections"
PM_ID = "pmuni0087"
URL = "https://www.projectmadurai.org/pm_etexts/utf8/pmuni0087.html"
EXPECTED_SHA = "07497b27fa06415c89e0023530d7599595521f400cc088cbaeaee9f2ea8e4fc9"
EXPECTED_BYTES = 253119

MAIN_RE = re.compile(r"^(\d{1,2})\.\s+(.+)$")
TAMIL_ORDINALS = {
    "ஐந்தாம் பாடல்": 5, "ஆறாம் பாடல்": 6, "எட்டாம் பாடல்": 8,
    "ஒன்பதாம் பாடல்": 9, "பத்தாம் பாடல்": 10,
    "பதினோராம் பாடல்": 11, "பனிரெண்டாம் பாடல்": 12,
    "பதிமூன்றாம் பாடல்": 13,
}
META_RE = re.compile(r"^(பாடியவர்|இசையமைத்தவர்|பண்)\s*::\s*(.*)$")
SEPARATOR_RE = re.compile(r"^-{5,}$")
# Project Madurai prints five-line counters using digits, sometimes preceded by dots.
LINE_MARKER_RE = re.compile(r"[ \u00a0\t]+(?:\.\s*){0,8}\d{1,3}\s*$")


def _sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def verify_source() -> None:
    if not RAW.is_file() or RAW.stat().st_size != EXPECTED_BYTES or _sha(RAW) != EXPECTED_SHA:
        raise RuntimeError("Paripāṭal raw source mismatch")
    RAW.read_bytes().decode("utf-8-sig")


def _tokens() -> list[dict[str, Any]]:
    """Return BR/newline-delimited visible strings with their source markup."""
    soup = BeautifulSoup(RAW.read_bytes().decode("utf-8-sig"), "lxml")
    out: list[dict[str, Any]] = []
    for node in soup.body.descendants:
        if not isinstance(node, NavigableString):
            continue
        parents = {p.name for p in node.parents}
        if "script" in parents or "style" in parents:
            continue
        styled = "strong" in parents or "i" in parents
        for part in str(node).splitlines():
            text = part.strip()
            if text:
                out.append({"text": text, "styled": styled,
                            "tags": sorted(x for x in parents if x)})
    return out


def _is_record_heading(token: dict[str, Any], in_tirattu: bool) -> tuple[int, str] | None:
    text = token["text"]
    if not token["styled"]:
        return None
    if in_tirattu and text in TAMIL_ORDINALS:
        return TAMIL_ORDINALS[text], text
    match = MAIN_RE.match(text)
    if match:
        number = int(match.group(1))
        if (not in_tirattu and 1 <= number <= 22) or (in_tirattu and number in {1, 2, 3, 4, 7}):
            return number, text
    return None


def _clean_body_line(text: str) -> str:
    return LINE_MARKER_RE.sub("", text).rstrip()


def parse() -> dict[str, Any]:
    verify_source()
    tokens = _tokens()
    tirattu_at = next(i for i, t in enumerate(tokens) if t["text"] == "பரிபாடல்-திரட்டு")
    end_at = next(i for i, t in enumerate(tokens) if t["text"] == "(பரிபாடல் திரட்டு முற்றிற்று.)")
    starts: list[tuple[int, str, int, str]] = []
    for i, token in enumerate(tokens):
        in_tirattu = i > tirattu_at
        found = _is_record_heading(token, in_tirattu)
        if found:
            printed_number, heading = found
            starts.append((i, "tirattu" if in_tirattu else "main", printed_number, heading))
    main = [x for x in starts if x[1] == "main"]
    tirattu = [x for x in starts if x[1] == "tirattu"]
    if [x[2] for x in main] != list(range(1, 23)):
        raise RuntimeError("Expected main Paripāṭal headings 1 through 22")
    if [x[2] for x in tirattu] != list(range(1, 14)):
        raise RuntimeError("Expected Paripāṭal Tirattu printed records 1 through 13")

    records = []
    for sequence, (start, division, printed_number, printed_heading) in enumerate(starts, 1):
        stop = starts[sequence][0] if sequence < len(starts) else end_at
        block = tokens[start + 1:stop]
        body: list[str] = []
        source_notes: list[str] = []
        internal: list[dict[str, Any]] = []
        metadata = {"poet": None, "music_composer": None, "pann": None}
        in_parenthetical_note = False
        for token in block:
            text = token["text"]
            if SEPARATOR_RE.match(text) or text in {"பரிபாடல் முற்றிற்று", "பரிபாடல்-திரட்டு"}:
                continue
            match = META_RE.match(text)
            if match:
                key = {"பாடியவர்": "poet", "இசையமைத்தவர்": "music_composer", "பண்": "pann"}[match.group(1)]
                metadata[key] = match.group(2).strip()
                source_notes.append(text)
                continue
            if in_parenthetical_note or text.startswith("(") or text.startswith("இப் பகுதி") or text.startswith("இப்பாடல்"):
                source_notes.append(text)
                if text.startswith("(") and not text.endswith(")"):
                    in_parenthetical_note = True
                if in_parenthetical_note and text.endswith(")"):
                    in_parenthetical_note = False
                continue
            if token["styled"]:
                # Styled subheadings are source structure, not verse.
                if text == "கடவுள் வாழ்த்து" and sequence == 1:
                    source_notes.append(text)
                else:
                    internal.append({"sequence": len(internal) + 1,
                                     "heading_as_printed": text,
                                     "before_body_line": len(body) + 1,
                                     "provenance": "printed by selected canonical source"})
                continue
            cleaned = _clean_body_line(text)
            if cleaned:
                body.append(cleaned)
        title_as_printed = printed_heading.split(".", 1)[1].strip() if "." in printed_heading else None
        records.append({
            "poem_number": sequence,
            "poem_number_as_printed": printed_number,
            "source_order": sequence,
            "record_type": "numbered_poem" if division == "main" else "tirattu_fragment",
            "source_division": "பரிபாடல்" if division == "main" else "பரிபாடல்-திரட்டு",
            "source_division_sequence": 1 if division == "main" else 2,
            "printed_heading": printed_heading,
            "title_as_printed": title_as_printed,
            "lines": body,
            "source_note_lines": source_notes,
            "internal_structure": internal,
            **metadata,
            "textual_status": "incomplete" if division == "tirattu" or sequence == 22 else "complete",
            "lacuna_present": any(re.search(r"\.{3,}", line) for line in body),
            "status": "source-transcribed",
            "source_object_id": PM_ID,
        })
    return {
        "parser": "paripatal-pmuni0087-v1",
        "work_slug": "paripatal",
        "title_tamil": "பரிபாடல்",
        "title_as_printed": "பரிபாடல் & பரிபாடல் திரட்டு (பல ஆசிரியர்கள்)",
        "source_divisions": [
            {"sequence": 1, "heading_as_printed": "பரிபாடல்", "record_start": 1, "record_end": 22, "record_count": 22},
            {"sequence": 2, "heading_as_printed": "பரிபாடல்-திரட்டு", "record_start": 23, "record_end": 35, "record_count": 13},
        ],
        "prefatory_source_prose_and_verse": [t["text"] for t in tokens[:starts[0][0]]
                                              if t["text"] not in {"பரிபாடல்"}],
        "poems": records,
        "unparsed_fragments": [],
    }


def extract(force=True, dry_run=False, verbose=False):
    data = parse()
    if dry_run:
        print("Would extract 22 main poems and 13 Tirattu fragment records")
        return
    RAW_TXT.parent.mkdir(parents=True, exist_ok=True)
    RAW_TXT.write_text("\n".join(t["text"] for t in _tokens()) + "\n", encoding="utf-8")
    write_json(PARSED, data, force=True)
    source_meta = {
        "work": "paripatal", "source_name": "Project Madurai",
        "project_madurai_id": PM_ID, "source_url": URL,
        "source_file": "sources/raw-html/paripatal.html",
        "source_bytes": EXPECTED_BYTES, "source_checksum_sha256": EXPECTED_SHA,
        "accessed_date": "2026-07-29",
        "source_artifact_type": "exact HTTP HTML response body",
        "title_as_printed": data["title_as_printed"],
    }
    write_json(SOURCE_META, source_meta, force=True)
    write_json(RECON, {
        "work": "paripatal", "parser": data["parser"], "canonical_source": source_meta,
        "printed_main_records": 22, "printed_tirattu_records": 13,
        "canonical_source_order_records": 35,
        "numbering_policy": "Canonical sequence 1-35; printed number retained independently. Tirattu restarts at 1.",
        "source_divisions": data["source_divisions"],
        "source_lost_records": [],
        "incomplete_records": [p["poem_number"] for p in data["poems"] if p["textual_status"] == "incomplete"],
        "records_with_dot_lacunae": [p["poem_number"] for p in data["poems"] if p["lacuna_present"]],
        "candidate_text_conditions": [],
        "commentary_present": False,
        "internal_heading_count": sum(len(p["internal_structure"]) for p in data["poems"]),
        "source_grammar": "BR/newline-flat HTML; styled record/internal headings; plain verse; explicit attribution fields",
        "notes": [
            "The Tirattu is a separately printed source division containing thirteen fragment records.",
            "Tamil ordinal headings in Tirattu are preserved as printed and mapped only to their explicit ordinal.",
            "Source editorial/recovery notes are preserved as source notes and excluded from literary bodies.",
            "Styled topical subheadings are preserved in structure inventory and excluded from literary bodies.",
        ],
    }, force=True)
    if verbose:
        print("Extracted 35 source-order records")


def normalize(force=True, dry_run=False, verbose=False):
    data = json.loads(PARSED.read_text(encoding="utf-8"))
    for poem in data["poems"]:
        poem["lines"] = [unicodedata.normalize("NFC", x) for x in poem["lines"]]
        poem["source_note_lines"] = [unicodedata.normalize("NFC", x) for x in poem["source_note_lines"]]
    data["normalization"] = "Unicode NFC; LF; HTML entities decoded; five-line layout counters removed"
    if not dry_run:
        write_json(NORMALIZED, data, force=True)


def _markdown(poem: dict[str, Any]) -> str:
    lines = poem["lines"]
    fm = {
        "schema_version": "1.0.0", "work": "பரிபாடல்", "work_english": "Paripāṭal",
        "work_id": "paripatal", "work_slug": "paripatal",
        "record_type": poem["record_type"], "poem_number": poem["poem_number"],
        "poem_number_as_printed": poem["poem_number_as_printed"],
        "source_order": poem["source_order"], "section": poem["source_division"],
        "section_source": "Project Madurai printed source division",
        "source_division": poem["source_division"],
        "source_division_sequence": poem["source_division_sequence"],
        "title_as_printed": poem["title_as_printed"],
        "thinai": None, "thinai_source": None, "speaker": None, "speaker_source": None,
        "poet": poem["poet"], "poet_source": "Project Madurai printed attribution" if poem["poet"] else None,
        "music_composer": poem["music_composer"],
        "music_composer_source": "Project Madurai printed attribution" if poem["music_composer"] else None,
        "pann": poem["pann"], "pann_source": "Project Madurai printed attribution" if poem["pann"] else None,
        "first_line": lines[0] if lines else "", "line_count": len(lines),
        "textual_status": poem["textual_status"], "canonical_text_available": bool(lines),
        "candidate_texts_available": False, "lacuna_present": poem["lacuna_present"],
        "lacuna_location": "within" if poem["lacuna_present"] else None,
        "source_note_available": bool(poem["source_note_lines"]),
        "source_note_source": "Project Madurai printed metadata/editorial note" if poem["source_note_lines"] else None,
        "internal_structure_available": bool(poem["internal_structure"]),
        "extraction_status": "success", "source": "Project Madurai", "source_url": URL,
        "project_madurai_id": PM_ID, "source_object_id": PM_ID,
        "source_file": "sources/raw-html/paripatal.html", "source_sha256": EXPECTED_SHA,
        "language": "Tamil", "script": "Tamil", "status": "source-transcribed",
        "editorial_changes": False,
    }
    yaml_text = yaml.safe_dump(fm, allow_unicode=True, sort_keys=False).strip()
    out = f"---\n{yaml_text}\n---\n\n# பரிபாடல் {poem['poem_number']}\n\n" + "\n".join(lines) + "\n"
    if poem["source_note_lines"]:
        out += "\n## Source note (as printed)\n\n" + "\n".join(poem["source_note_lines"]) + "\n"
    return out


def split(force=True, dry_run=False, verbose=False):
    data = json.loads(NORMALIZED.read_text(encoding="utf-8"))
    poems = data["poems"]
    if dry_run:
        print("Would write 35 records and two source-division sections")
        return
    POEMS.mkdir(parents=True, exist_ok=True)
    SECTIONS.mkdir(parents=True, exist_ok=True)
    expected_poems = {f"{n:03d}.md" for n in range(1, 36)}
    expected_sections = {"01-paripatal.md", "02-paripatal-tirattu.md"}
    bad = [x for x in POEMS.rglob("*") if x.is_file() and (x.parent != POEMS or x.name not in expected_poems)]
    bad += [x for x in SECTIONS.rglob("*") if x.is_file() and (x.parent != SECTIONS or x.name not in expected_sections)]
    if bad:
        raise RuntimeError(f"Unexpected physical files: {bad}")
    for poem in poems:
        (POEMS / f"{poem['poem_number']:03d}.md").write_text(_markdown(poem), encoding="utf-8", newline="\n")
    section_map = {1: "01-paripatal.md", 2: "02-paripatal-tirattu.md"}
    for division in data["source_divisions"]:
        selected = [p for p in poems if p["source_division_sequence"] == division["sequence"]]
        content = f"# {division['heading_as_printed']}\n\nProject Madurai source-printed division.\n\n"
        content += "\n".join(_markdown(p).split("---\n", 2)[-1].lstrip() for p in selected)
        (SECTIONS / section_map[division["sequence"]]).write_text(content, encoding="utf-8", newline="\n")
    (CORPUS / "full-text.md").write_text(
        "# பரிபாடல் — source transcription\n\n" +
        "\n".join(_markdown(p).split("---\n", 2)[-1].lstrip() for p in poems),
        encoding="utf-8", newline="\n")
    write_json(CORPUS / "structure-inventory.json", {
        "source_divisions": data["source_divisions"],
        "records": [{
            "canonical_sequence": p["poem_number"],
            "poem_number_as_printed": p["poem_number_as_printed"],
            "printed_heading": p["printed_heading"],
            "record_type": p["record_type"],
            "source_division": p["source_division"],
            "internal_structure": p["internal_structure"],
        } for p in poems],
    }, force=True)
    write_json(CORPUS / "metadata.json", {
        "corpus_schema_version": "1.0.0", "version_status": "frozen",
        "title_tamil": "பரிபாடல்", "title_english": "Paripāṭal",
        "title_as_printed": data["title_as_printed"], "work_slug": "paripatal",
        "work_id": "paripatal", "collection": "எட்டுத்தொகை",
        "numbered_poem_record_count": 35, "main_poem_count": 22,
        "tirattu_fragment_count": 13, "available_poem_count": 35,
        "source_name": "Project Madurai", "source_url": URL,
        "project_madurai_id": PM_ID, "source_file": "sources/raw-html/paripatal.html",
        "source_checksum_sha256": EXPECTED_SHA, "source_bytes": EXPECTED_BYTES,
        "accessed_date": "2026-07-29", "encoding": "UTF-8",
        "normalization": "Unicode NFC",
        "source_structure": data["source_divisions"],
        "notes": [
            "Canonical record numbering is source order across two printed divisions.",
            "The Tirattu restarts printed numbering; poem_number_as_printed preserves that numbering.",
            "No conventional classifications are inferred.",
            "Version 1.0.0 freezes pmuni0087, its checksum, the 22+13 source-order record model, canonical bodies, source notes, printed metadata, source divisions and validation expectations.",
        ],
    }, force=True)


def validate(dry_run=False, verbose=False):
    data = json.loads(NORMALIZED.read_text(encoding="utf-8"))
    source = {p["poem_number"]: p for p in data["poems"]}
    expected = {f"{n:03d}.md" for n in range(1, 36)}
    expected_sections = {"01-paripatal.md", "02-paripatal-tirattu.md"}
    physical = [x for x in POEMS.rglob("*") if x.is_file()]
    sections = [x for x in SECTIONS.rglob("*") if x.is_file()]
    issues: list[dict[str, Any]] = []
    fidelity = []
    bodies = collections.defaultdict(list)
    firsts = collections.defaultdict(list)
    schema_pass = 0
    required = [
        "schema_version", "work", "work_id", "record_type", "poem_number",
        "poem_number_as_printed", "source_order", "textual_status",
        "canonical_text_available", "candidate_texts_available", "lacuna_present",
        "lacuna_location", "extraction_status", "thinai", "thinai_source",
        "poet", "poet_source", "speaker", "speaker_source",
        "source_note_available", "source_note_source", "source_object_id",
    ]
    def add(n, kind, severity, message):
        issues.append({"work": "paripatal", "poem_number": n, "issue_type": kind,
                       "severity": severity, "message": message,
                       "source_file": "sources/raw-html/paripatal.html",
                       "markdown_file": f"corpus/paripatal/poems/{n:03d}.md" if n else ""})
    direct = {x.name for x in physical if x.parent == POEMS}
    if len(physical) != 35 or direct != expected:
        add(None, "physical_poem_inventory", "error", "Expected exactly 001.md through 035.md")
    if len(sections) != 2 or {x.name for x in sections if x.parent == SECTIONS} != expected_sections:
        add(None, "physical_section_inventory", "error", "Expected exactly two source-division sections")
    yaml_numbers = collections.defaultdict(list)
    for path in physical:
        try:
            fm, _ = read_frontmatter(path)
            yaml_numbers[fm.get("poem_number")].append(str(path.relative_to(POEMS)))
        except Exception as exc:
            add(None, "malformed_yaml", "error", f"{path}: {exc}")
    for number, names in yaml_numbers.items():
        if len(names) > 1:
            add(number, "duplicate_yaml_poem_number", "error", str(names))
    for name in sorted(expected & direct):
        path = POEMS / name
        fm, markdown = read_frontmatter(path)
        number = int(fm["poem_number"])
        missing = [key for key in required if key not in fm]
        if missing:
            add(number, "missing_schema_keys", "error", str(missing))
        else:
            schema_pass += 1
        markdown_lines = markdown_literary_lines(markdown)
        source_hash = body_hash(source[number]["lines"])
        markdown_hash = body_hash(markdown_lines)
        note_lines = []
        if "## Source note (as printed)" in markdown:
            note_lines = [x.strip() for x in markdown.split("## Source note (as printed)", 1)[1].splitlines() if x.strip()]
        note_match = canonical_body_text(note_lines) == canonical_body_text(source[number]["source_note_lines"])
        fidelity.append({"poem_number": number, "source_body_hash_sha256": source_hash,
                         "markdown_body_hash_sha256": markdown_hash,
                         "source_output_match": source_hash == markdown_hash,
                         "source_note_match": note_match})
        if source_hash != markdown_hash:
            add(number, "source_output_mismatch", "error", "Generated literary body differs")
        if not note_match:
            add(number, "source_note_output_mismatch", "error", "Generated source note differs")
        bodies[markdown_hash].append(number)
        if markdown_lines:
            firsts[markdown_lines[0]].append(number)
    duplicate_bodies = [v for v in bodies.values() if len(v) > 1]
    for group in duplicate_bodies:
        add(None, "duplicate_poem_body", "warning", str(group))
    shared = [v for v in firsts.values() if len(v) > 1]
    for group in shared:
        add(None, "shared_first_line", "info", str(group))
    report = {
        "work": "paripatal", "source_record_count": 35,
        "main_poem_records": 22, "tirattu_fragment_records": 13,
        "canonical_poem_files": len(physical),
        "canonical_literary_texts_available": sum(bool(p["lines"]) for p in data["poems"]),
        "source_divisions": 2, "schema_files_checked": len(expected & direct),
        "schema_files_passing": schema_pass,
        "schema_files_failing": len(expected & direct) - schema_pass,
        "source_output_matches": sum(x["source_output_match"] for x in fidelity),
        "source_note_matches": sum(x["source_note_match"] for x in fidelity),
        "duplicate_full_bodies": duplicate_bodies, "shared_first_lines": shared,
        "source_output_fidelity": fidelity,
        "errors": sum(x["severity"] == "error" for x in issues),
        "warnings": sum(x["severity"] == "warning" for x in issues),
        "info": sum(x["severity"] == "info" for x in issues),
        "issues": issues,
    }
    report["status"] = "pass-with-review" if not report["errors"] else "fail"
    if not dry_run:
        write_json(ROOT / "manifests/paripatal-validation-report.json", report, force=True)
        write_json(ROOT / "manifests/validation-report.json", report, force=True)
        write_work_issues("paripatal", issues)
    if verbose:
        print(f"Validation {report['status']}: {report['errors']} errors")
    return report
