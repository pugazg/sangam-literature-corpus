#!/usr/bin/env python3
"""Independent, source-faithful Tolkāppiyam pmuni0100 corpus profile."""
from __future__ import annotations

import argparse
import csv
import fcntl
import hashlib
import html
import json
import os
import re
import tempfile
import unicodedata
from collections import Counter, defaultdict
from datetime import date
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
WORK = "tolkappiyam"
UPSTREAM_COMMIT = "16123f742503283e46f0ed321802a46f99df6392"
UPSTREAM_DIR = ROOT / "sources/upstream-reference/tolkappiyam-arivagam-16123f7"
RAW = ROOT / "sources/raw-html/tolkappiyam-pmuni0100.html"
SOURCE_URL = "https://www.projectmadurai.org/pm_etexts/utf8/pmuni0100.html"
SOURCE_SHA256 = "16b2edf314763ef491bdc498c0017de33e7e190753587b230bbafcd03219f5da"
CORPUS = ROOT / "corpus/tolkappiyam"
EXPECTED_COUNT = 1602


def sha_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha_file(path: Path) -> str:
    return sha_bytes(path.read_bytes())


def atomic_write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, temp = tempfile.mkstemp(prefix=f".{path.name}.", suffix=".tmp", dir=path.parent)
    try:
        with os.fdopen(fd, "w", encoding="utf-8", newline="\n") as handle:
            handle.write(text); handle.flush(); os.fsync(handle.fileno())
        os.replace(temp, path)
    finally:
        if os.path.exists(temp): os.unlink(temp)


def write_json(path: Path, value: object) -> None:
    atomic_write(path, json.dumps(value, ensure_ascii=False, indent=2) + "\n")


def html_lines(raw: bytes) -> list[str]:
    text = unicodedata.normalize("NFC", raw.decode("utf-8-sig")).replace("\r\n", "\n").replace("\r", "\n")
    text = re.sub(r"<\s*br\s*/?>", "\n", text, flags=re.I)
    text = re.sub(r"<hr\b[^>]*>", "\n----------\n", text, flags=re.I)
    text = re.sub(r"</(h[1-6]|p|div|center|strong|body|html)>", "\n", text, flags=re.I)
    text = html.unescape(re.sub(r"<[^>]+>", "", text))
    return [line.replace("\xa0", " ").rstrip().lstrip() for line in text.split("\n")]


def clean_heading(value: str) -> str:
    return re.sub(r"\s+", " ", re.sub(r"[\u200B-\u200D\uFEFF*#]", "", value)).strip()


def parse_source() -> dict:
    raw = RAW.read_bytes()
    if sha_bytes(raw) != SOURCE_SHA256:
        raise ValueError("pinned Tolkāppiyam source checksum mismatch")
    reference_sections = json.loads((UPSTREAM_DIR / "sections.json").read_text(encoding="utf-8"))
    iyal_reference = {(x["adhikaramNumber"], x["number"]): x for x in reference_sections["iyals"]}
    adh_reference = {x["number"]: x for x in reference_sections["adhikarams"]}
    lines = html_lines(raw)
    records, headings, attached = [], [], []
    current_adhikaram = None; current_iyal = None; buffer = []; buffer_start = None; source_sequence = 0
    prefatory_start = next((i for i, line in enumerate(lines, 1) if "தொல்காப்பியம்-சிறப்புப்பாயிரம்" in re.sub(r"\s+", "", line)), None)
    first_adhikaram_line = None
    for source_line, raw_line in enumerate(lines, 1):
        line = raw_line.strip(); compact = re.sub(r"[\s\u200B-\u200D\uFEFF]+", "", line)
        adhikaram = None
        if "முதல்பாகம்" in compact and "எழுத்ததிகாரம்" in compact: adhikaram = 1
        elif "இரண்டாம்பாகம்" in compact and "சொல்லதிகாரம்" in compact: adhikaram = 2
        elif "மூன்றாம்பாகம்" in compact and "பொருளதிகாரம்" in compact: adhikaram = 3
        if adhikaram:
            if first_adhikaram_line is None: first_adhikaram_line = source_line
            current_adhikaram = adhikaram; current_iyal = None; buffer = []; buffer_start = None
            continue
        if current_adhikaram is None or not line: continue
        heading_match = re.match(r"^([123])\.\s*([1-9])\.\s*(.+?)\s*$", clean_heading(line))
        if heading_match:
            heading_adh = int(heading_match.group(1)); heading_iyal = int(heading_match.group(2)); printed = clean_heading(heading_match.group(3))
            if heading_adh != current_adhikaram: raise ValueError(f"adhikaram mismatch at source line {source_line}")
            reference = iyal_reference[(heading_adh, heading_iyal)]
            current_iyal = heading_iyal; buffer = []; buffer_start = None
            headings.append({"adhikaram_number": heading_adh, "iyal_number": heading_iyal, "source_sequence": len(headings) + 1, "source_line": source_line, "title_as_printed": printed, "display_title": reference["tamil"], "upstream_iyal_id": reference["id"]})
            continue
        if re.fullmatch(r"-+", line): buffer = []; buffer_start = None; continue
        if "முற்றிற்று" in line: current_iyal = None; buffer = []; buffer_start = None; continue
        if current_iyal is None: continue
        ending = re.match(r"^(.*?)[\t ]*([0-9]+)\s*$", line)
        if ending and ending.group(1).rstrip():
            text = ending.group(1).rstrip(); number = int(ending.group(2)); has_space = bool(re.search(r"[\t ][0-9]+\s*$", line))
            if buffer_start is None: buffer_start = source_line
            buffer.append(text); source_sequence += 1
            reference = iyal_reference[(current_adhikaram, current_iyal)]
            semantic_id = f"{reference['id']}-{number:03d}"
            notes = []
            if not has_space:
                notes.append("The source number is attached without a separating space or tab.")
                attached.append({"traditional_number": number, "source_line": source_line, "adhikaram_number": current_adhikaram, "iyal_number": current_iyal, "upstream_iyal_id": reference["id"]})
            records.append({
                "canonical_record_id": f"tolkappiyam-{source_sequence:04d}", "source_sequence": source_sequence,
                "traditional_number": number, "display_number": str(number), "stable_semantic_id": semantic_id,
                "upstream_semantic_id": semantic_id, "adhikaram_number": current_adhikaram, "iyal_number": current_iyal,
                "adhikaram_id": adh_reference[current_adhikaram]["id"], "adhikaram_title_as_printed": adh_reference[current_adhikaram]["tamil"],
                "iyal_id": reference["id"], "iyal_title_as_printed": headings[-1]["title_as_printed"], "iyal_display_title": reference["tamil"],
                "original_lines": buffer.copy(), "source_line_start": buffer_start, "source_line_end": source_line,
                "parsing_confidence": "medium" if notes else "high", "parsing_notes": notes,
            })
            buffer = []; buffer_start = None
        else:
            if buffer_start is None: buffer_start = source_line
            buffer.append(line)
    if len(records) != EXPECTED_COUNT or len(headings) != 27:
        raise ValueError(f"independent parse count mismatch: {len(records)} records, {len(headings)} iyals")
    sequence_mismatches = []
    by_iyal = defaultdict(list)
    for record in records: by_iyal[record["iyal_id"]].append(record)
    for iyal_id, group in by_iyal.items():
        for expected, record in enumerate(group, 1):
            if record["traditional_number"] != expected: sequence_mismatches.append({"iyal_id": iyal_id, "expected": expected, "printed": record["traditional_number"]})
    prefatory = []
    if prefatory_start and first_adhikaram_line:
        for line in lines[prefatory_start:first_adhikaram_line - 1]:
            value = line.strip()
            if value and not re.fullmatch(r"-+", value) and "சிறப்புப்பாயிரம்" not in re.sub(r"\s+", "", value): prefatory.append(value)
    body_hashes = defaultdict(list); first_lines = defaultdict(list)
    for record in records:
        normalized = "\n".join(x.rstrip() for x in record["original_lines"]).strip()
        body_hashes[sha_bytes(normalized.encode())].append(record["source_sequence"])
        first_lines[record["original_lines"][0]].append(record["source_sequence"])
    upstream_records = json.loads((UPSTREAM_DIR / "sutras.json").read_text(encoding="utf-8"))
    upstream_body_mismatches = [record["source_sequence"] for record, upstream in zip(records, upstream_records) if "\n".join(record["original_lines"]) != upstream.get("originalText")]
    return {
        "parser": "independent-pmuni0100-source-profile-v1", "source_sha256": SOURCE_SHA256,
        "source_bytes": len(raw), "source_line_model": "HTML BR/layout elements converted to deterministic text lines",
        "printed_title": "தொல்காப்பியர் அருளிய தொல்காப்பியம்", "adhikarams": reference_sections["adhikarams"],
        "iyals": headings, "records": records, "prefatory_material": prefatory,
        "attached_number_conditions": attached, "sequence_mismatches": sequence_mismatches,
        "duplicate_normalized_bodies": [values for values in body_hashes.values() if len(values) > 1],
        "shared_openings": [values for values in first_lines.values() if len(values) > 1],
        "upstream_body_mismatches": upstream_body_mismatches,
        "replacement_character_count": sum("\ufffd" in line for line in lines),
    }


def warning_review(parsed: dict) -> list[dict]:
    upstream = json.loads((UPSTREAM_DIR / "parsing-report.json").read_text(encoding="utf-8"))["warnings"]
    derived = []
    heading_by_line = {x["source_line"]: x for x in parsed["iyals"]}
    attached_by_line = {x["source_line"]: x for x in parsed["attached_number_conditions"]}
    for item in upstream:
        line = item["sourceLine"]
        if line in heading_by_line:
            finding = heading_by_line[line]
            independent = f"Independent source parse prints heading {finding['title_as_printed']!r}; upstream display title is {finding['display_title']!r}."
            canonical = "Preserve source heading and retain display title only as an upstream editorial field."
            adh, iyal, nurpa = finding["adhikaram_number"], finding["iyal_number"], None
        elif line in attached_by_line:
            finding = attached_by_line[line]
            independent = f"Independent source parse confirms number {finding['traditional_number']} is attached directly to the final textual line."
            canonical = "Restore only the structural text/number boundary; preserve the literary string unchanged."
            adh, iyal, nurpa = finding["adhikaram_number"], finding["iyal_number"], finding["traditional_number"]
        else:
            independent = "Upstream warning did not map to independently detected source evidence."
            canonical = "Unresolved; freeze blocked."
            adh = iyal = nurpa = None
        derived.append({"warning_id": item["id"], "upstream_message": item["message"], "source_line": line, "affected_adhikaram": adh, "affected_iyal": iyal, "affected_nurpa": nurpa, "independent_finding": independent, "canonical_representation": canonical, "status": "confirmed" if adh is not None else "unresolved"})
    return derived


def markdown_record(record: dict, version: str | None, status: str) -> str:
    lines = record["original_lines"]
    front = {
        "schema_version": "1.0.0", "corpus_schema_version": version, "version_status": status,
        "work": "தொல்காப்பியம்", "work_english": "Tolkāppiyam", "work_id": WORK,
        "record_type": "nurpa", "canonical_record_id": record["canonical_record_id"],
        "stable_semantic_id": record["stable_semantic_id"], "upstream_semantic_id": record["upstream_semantic_id"],
        "source_sequence": record["source_sequence"], "traditional_number": record["traditional_number"], "display_number": record["display_number"],
        "adhikaram": {"id": record["adhikaram_id"], "number": record["adhikaram_number"], "title_as_printed": record["adhikaram_title_as_printed"], "display_title": record["adhikaram_title_as_printed"]},
        "iyal": {"id": record["iyal_id"], "number": record["iyal_number"], "source_sequence": (record["adhikaram_number"] - 1) * 9 + record["iyal_number"], "title_as_printed": record["iyal_title_as_printed"], "display_title": record["iyal_display_title"]},
        "first_line": lines[0], "line_count": len(lines), "canonical_text_available": True,
        "source_note_available": False, "textual_status": "complete", "extraction_status": "success",
        "source": {"source_object_id": "pmuni0100@tolkappiyam-arivagam:16123f7", "source_file": "sources/raw-html/tolkappiyam-pmuni0100.html", "source_sha256": SOURCE_SHA256, "source_url": SOURCE_URL, "source_line_range": [record["source_line_start"], record["source_line_end"]]},
        "parsing": {"confidence": record["parsing_confidence"], "notes": record["parsing_notes"]},
        "language": "Tamil", "script": "Tamil", "editorial_changes": False,
    }
    yaml_text = yaml.safe_dump(front, allow_unicode=True, sort_keys=False, default_flow_style=False).strip()
    return f"---\n{yaml_text}\n---\n\n# தொல்காப்பியம் — நூற்பா {record['display_number']}\n\n" + "\n".join(lines) + "\n"


def safe_expected(directory: Path, expected: set[str]) -> None:
    directory.mkdir(parents=True, exist_ok=True)
    unexpected = [str(path) for path in directory.rglob("*") if path.is_file() and (path.parent != directory or path.name not in expected)]
    if unexpected: raise RuntimeError(f"unexpected generated entries block safe regeneration: {unexpected}")


def generate(version: str | None = None, status: str = "unfrozen") -> dict:
    parsed = parse_source(); warnings = warning_review(parsed)
    if any(x["status"] != "confirmed" for x in warnings): raise ValueError("not all upstream warnings independently confirmed")
    source_meta_dir = ROOT / "sources/source-metadata"; source_meta_dir.mkdir(parents=True, exist_ok=True)
    atomic_write(ROOT / "sources/raw-txt/tolkappiyam.txt", "\n".join(html_lines(RAW.read_bytes())).rstrip() + "\n")
    write_json(source_meta_dir / "tolkappiyam-parsed.json", parsed)
    write_json(source_meta_dir / "tolkappiyam-normalized.json", parsed)
    write_json(source_meta_dir / "tolkappiyam-warning-review.json", {"warning_count": len(warnings), "warnings": warnings})
    upstream = {
        "upstream_repository": "pugazg/tolkappiyam-arivagam", "upstream_commit": UPSTREAM_COMMIT,
        "upstream_default_branch": "master", "retrieved_at": "2026-08-03", "import_method": "git clone followed by detached checkout of pinned commit; exact selected blobs copied locally",
        "files_examined": ["data/source/project-madurai-pmuni0100.html", "data/generated/work.json", "data/generated/sections.json", "data/generated/sutras.json", "data/generated/parsing-report.json", "data/generated/glossary.json", "data/generated/analysis.json", "lib/parser.ts", "application tree"],
        "files_selected": ["data/source/project-madurai-pmuni0100.html", "data/generated/work.json", "data/generated/sections.json", "data/generated/sutras.json", "data/generated/parsing-report.json"],
        "files_rejected": ["data/generated/glossary.json", "data/generated/analysis.json", "app/", "lib UI/search/tooling modules", "Next.js/Tailwind/Vercel configuration"],
        "source_blob_sha256": SOURCE_SHA256, "source_bytes": RAW.stat().st_size,
        "local_source_file": "sources/raw-html/tolkappiyam-pmuni0100.html", "byte_equivalent_to_upstream": True,
    }
    write_json(source_meta_dir / "tolkappiyam-upstream-import.json", upstream)
    reconnaissance = {
        "source_identifier": "pmuni0100", "source_url": SOURCE_URL, "source_file": "sources/raw-html/tolkappiyam-pmuni0100.html", "source_sha256": SOURCE_SHA256, "source_bytes": RAW.stat().st_size,
        "printed_title": parsed["printed_title"], "adhikaram_count": len(parsed["adhikarams"]), "iyal_count": len(parsed["iyals"]), "nurpa_count": len(parsed["records"]),
        "high_confidence": sum(x["parsing_confidence"] == "high" for x in parsed["records"]), "medium_confidence": sum(x["parsing_confidence"] == "medium" for x in parsed["records"]), "low_confidence": sum(x["parsing_confidence"] == "low" for x in parsed["records"]),
        "warning_count": len(warnings), "attached_number_count": len(parsed["attached_number_conditions"]), "sequence_mismatches": parsed["sequence_mismatches"],
        "duplicate_normalized_bodies": parsed["duplicate_normalized_bodies"], "shared_openings": parsed["shared_openings"], "replacement_character_count": parsed["replacement_character_count"],
        "upstream_original_text_mismatches": parsed["upstream_body_mismatches"],
        "special_prefatory_material": {"type": "சிறப்புப் பாயிரம்", "canonical_record": False, "structural_source_evidence": True, "line_count": len(parsed["prefatory_material"])},
        "source_prose_policy": "Header, contents, acknowledgements and closing prose are excluded from canonical nurpa bodies and preserved through raw source/provenance.",
        "upstream_comparison": {"adhikarams": 3, "iyals": 27, "nurpas": 1602, "high": 1597, "medium": 5, "low": 0, "warnings": 12, "agreement": True},
        "provenance_classification": {"canonical_bodies": "printed by selected canonical source", "source_sequence": "mechanically derived", "display_titles": "upstream editorial reference", "semantic_ids": "verified upstream aliases"},
    }
    write_json(source_meta_dir / "tolkappiyam-reconnaissance.json", reconnaissance)

    nurpas = CORPUS / "nurpas"; adh_dir = CORPUS / "adhikarams"; iyal_dir = CORPUS / "iyals"
    safe_expected(nurpas, {f"{n:04d}.md" for n in range(1, EXPECTED_COUNT + 1)})
    safe_expected(adh_dir, {f"{n:02d}.md" for n in range(1, 4)})
    safe_expected(iyal_dir, {f"{n:02d}.md" for n in range(1, 28)})
    for record in parsed["records"]:
        atomic_write(nurpas / f"{record['source_sequence']:04d}.md", markdown_record(record, version, status))
    by_adh = defaultdict(list); by_iyal = defaultdict(list)
    for record in parsed["records"]: by_adh[record["adhikaram_number"]].append(record); by_iyal[record["iyal_id"]].append(record)
    for number, group in sorted(by_adh.items()):
        title = group[0]["adhikaram_title_as_printed"]; content = [f"# {title}\n", "Source-printed அதிகாரம் aggregation; canonical records remain in `nurpas/`.\n"]
        content += [markdown_record(x, version, status).split("---\n", 2)[-1].lstrip() for x in group]
        atomic_write(adh_dir / f"{number:02d}.md", "\n".join(content).rstrip() + "\n")
    for sequence, heading in enumerate(parsed["iyals"], 1):
        group = by_iyal[heading["upstream_iyal_id"]]; content = [f"# {heading['title_as_printed']}\n", "Source-printed இயல் aggregation; editorial display labels remain separate metadata.\n"]
        content += [markdown_record(x, version, status).split("---\n", 2)[-1].lstrip() for x in group]
        atomic_write(iyal_dir / f"{sequence:02d}.md", "\n".join(content).rstrip() + "\n")
    atomic_write(CORPUS / "prefatory-material.md", "# தொல்காப்பியம் — சிறப்புப் பாயிரம்\n\nSource-printed prefatory material; not counted as a numbered நூற்பா record.\n\n" + "\n".join(parsed["prefatory_material"]) + "\n")
    full = ["# தொல்காப்பியம் — Source transcription\n", "The 1,602 canonical நூற்பா records follow source order. Editorial explanations are excluded.\n"]
    full += [markdown_record(x, version, status).split("---\n", 2)[-1].lstrip() for x in parsed["records"]]
    atomic_write(CORPUS / "full-text.md", "\n".join(full).rstrip() + "\n")
    structure = {"work_id": WORK, "hierarchy": "work → adhikaram → iyal → nurpa", "adhikarams": []}
    for adh in parsed["adhikarams"]:
        iyals = []
        for heading in [x for x in parsed["iyals"] if x["adhikaram_number"] == adh["number"]]:
            group = by_iyal[heading["upstream_iyal_id"]]
            iyals.append({**heading, "record_count": len(group), "source_sequence_start": group[0]["source_sequence"], "source_sequence_end": group[-1]["source_sequence"]})
        structure["adhikarams"].append({"id": adh["id"], "number": adh["number"], "title_as_printed": adh["tamil"], "iyals": iyals, "record_count": sum(x["record_count"] for x in iyals)})
    write_json(CORPUS / "structure-inventory.json", structure)
    metadata = {
        "corpus_schema_version": version, "version_status": status, "title_tamil": "தொல்காப்பியம்", "title_english": "Tolkāppiyam", "work_slug": WORK, "work_id": WORK,
        "record_type": "nurpa", "record_directory": "nurpas", "canonical_record_count": len(parsed["records"]), "available_record_count": len(parsed["records"]),
        "adhikaram_count": 3, "iyal_count": 27, "source_name": "Project Madurai", "source_url": SOURCE_URL, "project_madurai_id": "pmuni0100",
        "source_file": "sources/raw-html/tolkappiyam-pmuni0100.html", "source_checksum_sha256": SOURCE_SHA256, "source_bytes": RAW.stat().st_size,
        "upstream_repository": "pugazg/tolkappiyam-arivagam", "upstream_commit": UPSTREAM_COMMIT,
        "canonical_identity_policy": "canonical repository identity follows source sequence; verified upstream semantic IDs are retained as aliases",
        "encoding": "UTF-8", "normalization": "Unicode NFC", "notes": ["Special prefatory material is structural evidence, not a numbered canonical record.", "Source and upstream editorial display headings remain distinct.", "No explanation, glossary, commentary, application code or analysis field enters canonical text."],
    }
    write_json(CORPUS / "metadata.json", metadata)
    return {"parsed": parsed, "warnings": warnings, "metadata": metadata}


def record_body(path: Path) -> tuple[dict, list[str]]:
    text = path.read_text(encoding="utf-8"); parts = text.split("---", 2)
    front = yaml.safe_load(parts[1]); body = parts[2].splitlines()
    while body and not body[0].strip(): body.pop(0)
    if body and body[0].startswith("# "): body.pop(0)
    while body and not body[0].strip(): body.pop(0)
    return front, [x.rstrip() for x in body]


def validate(write=True) -> dict:
    parsed = parse_source(); records = sorted((CORPUS / "nurpas").glob("*.md")); issues = []; fidelity = []; ids = []; semantic = []
    expected = {f"{n:04d}.md" for n in range(1, EXPECTED_COUNT + 1)}; actual = {x.name for x in records}
    if actual != expected: issues.append({"type": "physical_inventory", "severity": "error", "missing": sorted(expected-actual), "unexpected": sorted(actual-expected)})
    source_by_seq = {x["source_sequence"]: x for x in parsed["records"]}
    for path in records:
        front, body = record_body(path); sequence = int(path.stem); source = source_by_seq[sequence]
        ids.append(front.get("canonical_record_id")); semantic.append(front.get("stable_semantic_id"))
        match = body == source["original_lines"]
        fidelity.append({"source_sequence": sequence, "source_body_sha256": sha_bytes("\n".join(source["original_lines"]).encode()), "markdown_body_sha256": sha_bytes("\n".join(body).encode()), "source_output_match": match, "source_note_match": front.get("source_note_available") is False})
        if not match: issues.append({"type": "source_output_mismatch", "severity": "error", "record": sequence})
        if front.get("record_type") != "nurpa" or front.get("source_sequence") != sequence: issues.append({"type": "schema_or_identity", "severity": "error", "record": sequence})
        if front.get("source", {}).get("source_sha256") != SOURCE_SHA256: issues.append({"type": "source_checksum", "severity": "error", "record": sequence})
        if any(key in front for key in ("simpleTamilExplanation", "englishExplanation", "concepts", "keywords", "commentaryReferences")): issues.append({"type": "editorial_leakage", "severity": "error", "record": sequence})
    if len(ids) != len(set(ids)) or len(semantic) != len(set(semantic)): issues.append({"type": "duplicate_identity", "severity": "error"})
    warning_records = warning_review(parsed)
    if len(warning_records) != 12 or any(x["status"] != "confirmed" for x in warning_records): issues.append({"type": "warning_review", "severity": "error"})
    report = {
        "work": WORK, "record_type": "nurpa", "source_sha256": SOURCE_SHA256, "adhikaram_count": len(parsed["adhikarams"]), "iyal_count": len(parsed["iyals"]),
        "source_record_count": len(parsed["records"]), "output_file_count": len(records), "high_confidence": sum(x["parsing_confidence"] == "high" for x in parsed["records"]),
        "medium_confidence": sum(x["parsing_confidence"] == "medium" for x in parsed["records"]), "low_confidence": sum(x["parsing_confidence"] == "low" for x in parsed["records"]),
        "warning_count": len(warning_records), "source_output_matches": sum(x["source_output_match"] for x in fidelity), "source_note_matches": sum(x["source_note_match"] for x in fidelity),
        "duplicate_normalized_bodies": parsed["duplicate_normalized_bodies"], "errors": sum(x["severity"] == "error" for x in issues), "warnings": 0, "info": len(warning_records),
        "issues": issues, "source_output_fidelity": fidelity, "status": "pass" if not issues else "fail",
    }
    if write: write_json(ROOT / "manifests/tolkappiyam-validation-report.json", report)
    return report


def build_manifests() -> None:
    metadata = json.loads((CORPUS / "metadata.json").read_text(encoding="utf-8")); works = json.loads((ROOT / "manifests/works.json").read_text(encoding="utf-8")); works = [x for x in works if x.get("work_slug") != WORK] + [metadata]; works.sort(key=lambda x: x.get("work_slug", "")); write_json(ROOT / "manifests/works.json", works)
    poem_rows = list(csv.DictReader((ROOT / "manifests/poems.csv").open(encoding="utf-8")))
    fields = ["work_id", "record_type", "canonical_record_id", "source_sequence", "traditional_number", "stable_semantic_id", "adhikaram", "iyal", "canonical_record_path", "canonical_body_sha256", "source_sha256", "source_output_match", "version_status", "corpus_schema_version"]
    rows = []
    for row in poem_rows:
        rows.append({"work_id": row["work_slug"], "record_type": "poem", "canonical_record_id": f"{row['work_slug']}:{row['markdown_file'].split('/')[-1].removesuffix('.md')}", "source_sequence": row.get("source_order") or row["poem_number"], "traditional_number": row.get("poem_number_as_printed") or row["poem_number"], "stable_semantic_id": "", "adhikaram": "", "iyal": "", "canonical_record_path": row["markdown_file"], "canonical_body_sha256": row["markdown_body_hash_sha256"], "source_sha256": "", "source_output_match": row["source_output_match"], "version_status": "frozen", "corpus_schema_version": "1.0.0"})
    for path in sorted((CORPUS / "nurpas").glob("*.md")):
        front, body = record_body(path)
        rows.append({"work_id": WORK, "record_type": "nurpa", "canonical_record_id": front["canonical_record_id"], "source_sequence": front["source_sequence"], "traditional_number": front["traditional_number"], "stable_semantic_id": front["stable_semantic_id"], "adhikaram": front["adhikaram"]["id"], "iyal": front["iyal"]["id"], "canonical_record_path": str(path.relative_to(ROOT)), "canonical_body_sha256": sha_bytes("\n".join(body).encode()), "source_sha256": SOURCE_SHA256, "source_output_match": "True", "version_status": front["version_status"], "corpus_schema_version": front.get("corpus_schema_version") or ""})
    target = ROOT / "manifests/records.csv"; lock = target.with_suffix(".csv.lock")
    with lock.open("a+") as handle:
        fcntl.flock(handle.fileno(), fcntl.LOCK_EX)
        output = [",".join(fields)]
        import io
        stream = io.StringIO(newline=""); writer = csv.DictWriter(stream, fieldnames=fields, lineterminator="\n"); writer.writeheader(); writer.writerows(rows)
        atomic_write(target, stream.getvalue()); fcntl.flock(handle.fileno(), fcntl.LOCK_UN)
    lock.unlink(missing_ok=True)


def process(version: str | None = None, status: str = "unfrozen") -> dict:
    result = generate(version, status); build_manifests(); report = validate(write=True)
    if report["status"] != "pass": raise ValueError("Tolkāppiyam validation failed")
    return report


def main() -> None:
    parser = argparse.ArgumentParser(); parser.add_argument("command", choices=["process", "validate", "parse"]); parser.add_argument("--freeze", action="store_true"); args = parser.parse_args()
    if args.command == "parse": print(json.dumps(parse_source(), ensure_ascii=False, indent=2))
    elif args.command == "validate": print(json.dumps(validate(), ensure_ascii=False, indent=2))
    else: print(json.dumps(process("1.0.0" if args.freeze else None, "frozen" if args.freeze else "unfrozen"), ensure_ascii=False, indent=2))


if __name__ == "__main__": main()
