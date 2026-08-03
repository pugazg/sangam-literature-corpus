#!/usr/bin/env python3
"""Shared, source-preserving helpers for the Project Madurai corpus pipeline."""
from __future__ import annotations

import csv
import hashlib
import json
import re
import unicodedata
import warnings
from datetime import date
from pathlib import Path
from typing import Any

import yaml
from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parents[1]
SOURCE_URL = "https://www.projectmadurai.org/pm_etexts/utf8/pmuni0296.html"
WORK = "natrinai"
PM_ID = "pmuni0296"

WORK_PROFILES = {
    "natrinai": {"expected_poems": 400, "section_strategy": "fifty", "expected_sections": 8,
                  "source_url": SOURCE_URL, "pm_id": PM_ID},
    "aingurunuru": {"expected_poems": 500, "section_strategy": "pattu", "expected_sections": 50,
                     "source_url": "https://www.projectmadurai.org/pm_etexts/utf8/pmuni0028.html",
                     "pm_id": "pmuni0028"},
    "kuruntokai": {"expected_poems": 401, "section_strategy": "mechanical_fifty", "expected_sections": 9,
                    "source_url": "https://www.projectmadurai.org/pm_etexts/utf8/pmuni0110.html",
                    "pm_id": "pmuni0110"},
    "akananuru": {"expected_poems": 400, "section_strategy": "printed_divisions", "expected_sections": 3,
                   "source_url": "https://www.projectmadurai.org/pm_etexts/utf8/pmuni0229.html",
                   "pm_id": "pmuni0229"},
    "purananuru": {"expected_poems": 400, "section_strategy": "mechanical_fifty", "expected_sections": 8,
                     "source_url": "https://www.projectmadurai.org/pm_etexts/utf8/pmuni0057.html",
                     "pm_id": "pmuni0057", "source_format": "user-supplied Markdown/text export"},
    "pattuppattu": {"expected_poems": 10, "section_strategy": "long_poem_source_order", "expected_sections": 10,
                     "source_url": None, "pm_id": None, "source_format": "ten exact Project Madurai HTML response bodies"},
    "patirruppattu": {"expected_poems": 80, "section_strategy": "surviving_pattu", "expected_sections": 8,
                       "source_url": "https://www.projectmadurai.org/pm_etexts/utf8/pmuni0038.html",
                       "pm_id": "pmuni0038"},
    "paripatal": {"expected_poems": 35, "section_strategy": "printed_main_and_tirattu", "expected_sections": 2,
                  "source_url": "https://www.projectmadurai.org/pm_etexts/utf8/pmuni0087.html",
                  "pm_id": "pmuni0087"},
    "kalittokai": {"expected_poems": 150, "section_strategy": "printed_kali_divisions", "expected_sections": 6,
                   "source_url": "https://www.projectmadurai.org/pm_etexts/utf8/pmuni0221.html",
                   "pm_id": "pmuni0221"},
    "tirukkural": {"expected_poems": 1330, "section_strategy": "printed_chapters", "expected_sections": 133,
                   "source_url": "https://www.projectmadurai.org/pm_etexts/utf8/pmuni0001.html",
                   "pm_id": "pmuni0001"},
    "naladiyar": {"expected_poems": 400, "section_strategy": "printed_chapters", "expected_sections": 40,
                  "source_url": "https://www.projectmadurai.org/pm_etexts/utf8/pmuni0016.html",
                  "pm_id": "pmuni0016"},
    "nanmanikkadigai": {"expected_poems": 106, "section_strategy": "printed_invocation_and_nul", "expected_sections": 2,
                        "source_url": "https://www.projectmadurai.org/pm_etexts/utf8/pmuni0047.html",
                        "pm_id": "pmuni0047"},
    "inna-narpathu": {"expected_poems": 40, "section_strategy": "printed_invocation_and_nul", "expected_sections": 2,
                      "source_url": "https://www.projectmadurai.org/pm_etexts/utf8/pmuni0025.html",
                      "pm_id": "pmuni0025"},
    "iniyavai-narpathu": {"expected_poems": 40, "section_strategy": "printed_invocation_and_nul", "expected_sections": 2,
                          "source_url": "https://www.projectmadurai.org/pm_etexts/utf8/pmuni0025.html",
                          "pm_id": "pmuni0025"},
    "kar-narpathu": {"expected_poems": 40, "section_strategy": "mechanical_whole_work", "expected_sections": 1,
                     "source_url": "https://www.projectmadurai.org/pm_etexts/utf8/pmuni0029.html",
                     "pm_id": "pmuni0029"},
    "kalavazhi-narpathu": {"expected_poems": 40, "section_strategy": "mechanical_whole_work", "expected_sections": 1,
                           "source_url": "https://www.projectmadurai.org/pm_etexts/utf8/pmuni0025.html",
                           "pm_id": "pmuni0025"},
    "aintinai-aimpathu": {"expected_poems": 50, "section_strategy": "printed_tinai_divisions", "expected_sections": 5,
                          "source_url": "https://www.projectmadurai.org/pm_etexts/utf8/pmuni0027.html",
                          "pm_id": "pmuni0027"},
    "aintinai-elupathu": {"expected_poems": 70, "section_strategy": "printed_tinai_divisions", "expected_sections": 5,
                          "source_url": "https://www.projectmadurai.org/pm_etexts/utf8/pmuni0027.html",
                          "pm_id": "pmuni0027"},
    "thinaimalai-nutraimbathu": {"expected_poems": 153, "section_strategy": "printed_tinai_divisions", "expected_sections": 5,
                                 "source_url": "https://www.projectmadurai.org/pm_etexts/utf8/pmuni0056.html",
                                 "pm_id": "pmuni0056"},
    "thinaimozhi-aimpathu":{"expected_poems":50,"expected_sections":5,"pm_id":"pmuni0027","section_strategy":"printed_tinai_divisions"},
    "tirikatukam":{"expected_poems":100,"expected_sections":1,"pm_id":"pmuni0048","section_strategy":"mechanical_whole_work"},
    "acharakkovai":{"expected_poems":100,"expected_sections":1,"pm_id":"pmuni0024","section_strategy":"mechanical_whole_work"},
    "pazhamozhi-nanuru":{"expected_poems":399,"expected_sections":33,"pm_id":"pmuni0036","section_strategy":"printed_chapters"},
    "sirupanchamulam":{"expected_poems":98,"expected_sections":2,"pm_id":"pmuni0029","section_strategy":"printed_preface_and_nul"},
    "muthumozhi-kanchi":{"expected_poems":100,"expected_sections":10,"pm_id":"pmuni0025","section_strategy":"printed_pattu"},
    "elati":{"expected_poems":80,"expected_sections":1,"pm_id":"pmuni0029","section_strategy":"mechanical_whole_work"},
    "kainnilai":{"expected_poems":60,"expected_sections":4,"pm_id":"pmuni0051","section_strategy":"printed_tinai_divisions"},
}


def profile(work: str) -> dict[str, Any]:
    try:
        return WORK_PROFILES[work]
    except KeyError as exc:
        raise ValueError(f"Unsupported work: {work}") from exc


def paths(work: str = WORK) -> dict[str, Path]:
    raw_source = (ROOT / "sources/purananuru.md" if work == "purananuru" else
                  ROOT / "sources/raw-html/pattuppattu" if work == "pattuppattu" else
                  ROOT / f"sources/raw-html/pathinenkilkanakku/{WORK_PROFILES[work]['pm_id']}.html"
                  if work in {"tirukkural", "naladiyar", "nanmanikkadigai", "inna-narpathu", "iniyavai-narpathu", "kar-narpathu", "kalavazhi-narpathu", "aintinai-aimpathu", "aintinai-elupathu", "thinaimalai-nutraimbathu","thinaimozhi-aimpathu","tirikatukam","acharakkovai","pazhamozhi-nanuru","sirupanchamulam","muthumozhi-kanchi","elati","kainnilai"} else
                  ROOT / "sources/raw-html" / f"{work}.html")
    return {
        "raw_html": raw_source,
        "raw_txt": ROOT / "sources/raw-txt" / f"{work}.txt",
        "source_metadata": ROOT / "sources/source-metadata" / f"{work}.json",
        "parsed": ROOT / "sources/source-metadata" / f"{work}-parsed.json",
        "normalized": ROOT / "sources/source-metadata" / f"{work}-normalized.json",
        "corpus": ROOT / "corpus" / work,
        "metadata": ROOT / "corpus" / work / "metadata.json",
        "full_text": ROOT / "corpus" / work / "full-text.md",
        "poems": ROOT / "corpus" / work / "poems",
        "sections": ROOT / "corpus" / work / "sections",
        "works_manifest": ROOT / "manifests/works.json",
        "poems_manifest": ROOT / "manifests/poems.csv",
        "validation": ROOT / "manifests/validation-report.json",
        "issues": ROOT / "issues/extraction-issues.csv",
        "observations": ROOT / "issues/editorial-observations.md",
        "log": ROOT / "logs" / f"{work}.log",
    }


def ensure_dirs() -> None:
    for name in ("sources/raw-html", "sources/raw-txt", "sources/source-metadata",
                 "corpus", "manifests", "issues", "logs"):
        (ROOT / name).mkdir(parents=True, exist_ok=True)


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def write_text(path: Path, text: str, force: bool = False) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists() and not force:
        raise FileExistsError(f"Refusing to overwrite {path}; pass --force")
    path.write_text(text, encoding="utf-8", newline="\n")


def write_json(path: Path, data: Any, force: bool = True) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists() and not force:
        raise FileExistsError(f"Refusing to overwrite {path}; pass --force")
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def normalized_line(text: str) -> str:
    return unicodedata.normalize("NFC", text.replace("\r\n", "\n").replace("\r", "\n")).strip()


HEADING_RE = re.compile(r"^(\d{1,3})(?:\s+|\.\s*)(.*)$")


def recognize_poem_heading(text: str) -> tuple[int, str | None, str | None] | None:
    """Recognize the printed Naṟṟiṇai heading without changing its number."""
    m = HEADING_RE.match(" ".join(text.strip().split()))
    if not m:
        return None
    number, rest = int(m.group(1)), m.group(2).strip()
    if not 1 <= number <= 400:
        return None
    if "மூலபாடம் மறைந்து போனது" in rest:
        return number, None, None
    parts = re.split(r"\s+-\s+", rest, maxsplit=1)
    thinai = parts[0].strip(" -") or None
    poet = parts[1].strip() if len(parts) == 2 else None
    if poet in {"(?)", "?"}:
        poet = None
    return number, thinai, poet


def element_lines(tag) -> list[str]:
    return [line.strip() for line in tag.get_text("\n").splitlines() if line.strip()]


def parse_natrinai_html(raw: bytes) -> dict[str, Any]:
    """Parse only the observed pmuni0296 HTML structure."""
    html = raw.decode("utf-8-sig")
    soup = BeautifulSoup(html, "lxml")
    p_tags = soup.find_all("p")
    poems: list[dict[str, Any]] = []
    unparsed: list[str] = []
    current: dict[str, Any] | None = None

    prefatory = {"heading": "கடவுள் வாழ்த்து", "lines": [], "poet": "பாரதம் பாடிய பெருந்தேவனார்"}
    invocation_label = soup.find(string=lambda s: s and s.strip() == "கடவுள் வாழ்த்து")
    if invocation_label:
        candidate = invocation_label.find_next("p")
        while candidate is not None and not element_lines(candidate):
            candidate = candidate.find_next("p")
        if candidate is not None:
            prefatory["lines"] = element_lines(candidate)

    closing_marker = None
    for p in p_tags:
        lines = element_lines(p)
        if not lines:
            continue
        heading = recognize_poem_heading(lines[0])
        if heading:
            if current:
                poems.append(current)
            number, thinai, poet = heading
            current = {
                "poem_number": number,
                "printed_heading": lines[0],
                "thinai": thinai,
                "poet": poet,
                "lines": [],
                "source_note_lines": [],
                "status": "source-transcribed",
            }
            if number == 234:
                current["status"] = "source-missing"
            continue
        if current is None:
            continue
        small = p.find("small")
        if small:
            current["source_note_lines"].extend(element_lines(small))
        else:
            # Literary text is printed in the paragraph after the heading.
            # The conjectural material following lost poem 234 is retained
            # as a source note, not silently assigned as canonical poem text.
            if current["poem_number"] == 234:
                current["source_note_lines"].extend(lines)
            elif not current["lines"]:
                current["lines"].extend(lines)
            elif lines == ["நற்றிணை முற்றும்"]:
                closing_marker = lines[0]
            else:
                unparsed.extend(lines)
    if current:
        poems.append(current)

    # BeautifulSoup exposes a few nested/cumulative p nodes in malformed HTML;
    # keep the first occurrence of each printed heading and report duplicates.
    unique: list[dict[str, Any]] = []
    seen: set[int] = set()
    duplicate_nodes: list[int] = []
    for poem in poems:
        n = poem["poem_number"]
        if n in seen:
            duplicate_nodes.append(n)
        else:
            seen.add(n)
            unique.append(poem)

    metadata_lines = []
    marker = soup.find(string=lambda s: s and "இத்தொகை தொகுப்பித்தோன்" in s)
    if marker and marker.parent:
        metadata_lines = element_lines(marker.parent)
        if "கடவுள் வாழ்த்து" in metadata_lines:
            metadata_lines = metadata_lines[:metadata_lines.index("கடவுள் வாழ்த்து")]
    return {
        "parser": "natrinai-pmuni0296-v1",
        "title_tamil": "நற்றிணை",
        "title_english": "Naṟṟiṇai",
        "work_slug": WORK,
        "metadata_lines": metadata_lines,
        "prefatory_text": prefatory,
        "closing_marker": closing_marker,
        "poems": unique,
        "duplicate_html_nodes_ignored": duplicate_nodes,
        "unparsed_fragments": unparsed,
    }


AINGURU_POEM_RE = re.compile(r"^(\d{1,3})\.\s*(.*)$")
AINGURU_PATTu_RE = re.compile(r"^(?:(\d{1,2})\.?\s*)?(.+பத்து)\.?$")


def parse_aingurunuru_html(raw: bytes) -> dict[str, Any]:
    """Parse the observed flat-BR structure of Project Madurai pmuni0028."""
    soup = BeautifulSoup(raw.decode("utf-8-sig"), "lxml")
    all_lines = [x.strip() for x in soup.get_text("\n").splitlines() if x.strip()]
    start = next(i for i, x in enumerate(all_lines) if AINGURU_POEM_RE.match(x) and x.startswith("1."))
    end = next(i for i, x in enumerate(all_lines[start:], start) if "ஐங்குறு நூறு முற்றிற்று" in x)
    lines = all_lines[start:end]
    poems: list[dict[str, Any]] = []
    headings: list[dict[str, Any]] = []
    current: dict[str, Any] | None = None
    pending_pattu: dict[str, Any] | None = None
    for line in lines:
        pm = AINGURU_PATTu_RE.match(line)
        if pm and len(line) < 100:
            printed_ordinal = int(pm.group(1)) if pm.group(1) else None
            printed_heading = line
            normalized_heading = re.sub(r"\s+", " ", pm.group(2)).strip().rstrip(".")
            pending_pattu = {"printed_heading": printed_heading, "normalized_heading": normalized_heading,
                             "printed_ordinal": printed_ordinal}
            continue
        m = AINGURU_POEM_RE.match(line)
        bare = re.match(r"^(\d{1,3})$", line)
        if not m and bare:
            m = bare
        if m:
            if current is not None:
                poems.append(current)
            number = int(m.group(1))
            if not 1 <= number <= 500:
                continue
            pattu_sequence = (number - 1) // 10 + 1
            if number % 10 == 1:
                if pending_pattu:
                    group = dict(pending_pattu)
                    pending_pattu = None
                else:
                    group = {"printed_heading": None, "normalized_heading": None, "printed_ordinal": None}
                group.update({"source_order": pattu_sequence, "poem_start": number,
                              "poem_end": min(number + 9, 500)})
                headings.append(group)
            group = headings[-1]
            note = (m.group(2) if m.lastindex and m.lastindex >= 2 else "").strip()
            lost = "கிடைக்காத பாடல்" in note
            current = {
                "poem_number": number, "printed_heading": line,
                "lines": [], "source_note_lines": [note] if lost else [],
                "status": "source-missing" if lost else "source-transcribed",
                "pattu_sequence": pattu_sequence, "position_within_pattu": (number - 1) % 10 + 1,
                "pattu": group["normalized_heading"], "pattu_as_printed": group["printed_heading"],
                "pattu_printed_ordinal": group["printed_ordinal"],
                "major_division": f"{((number-1)//100)*100+1:03d}-{min(((number-1)//100)*100+100,500):03d}",
            }
            continue
        if current is not None:
            current["lines"].append(line)
    if current is not None:
        poems.append(current)
    counts = {n: sum(1 for p in poems if p["poem_number"] == n) for n in range(1, 501)}
    for group in headings:
        members = [p for p in poems if p["pattu_sequence"] == group["source_order"]]
        group["poem_record_count"] = len(members)
        group["lost_poems"] = [p["poem_number"] for p in members if not p["lines"]]
        expected = group["source_order"]
        group["ordinal_consistent"] = group["printed_ordinal"] in (None, expected)
    return {
        "parser": "aingurunuru-pmuni0028-v1", "title_tamil": "ஐங்குறு நூறு",
        "title_english": "Aiṅkuṟunūṟu", "work_slug": "aingurunuru",
        "poems": poems, "pattu_groups": headings,
        "major_divisions": [{"sequence": i, "poem_start": (i-1)*100+1, "poem_end": i*100,
                             "name": None, "source": "mechanical hundred-poem block; source prints no division heading"}
                            for i in range(1, 6)],
        "missing_numbers": [n for n, c in counts.items() if c == 0],
        "duplicate_numbers": [n for n, c in counts.items() if c > 1],
        "unparsed_fragments": [],
    }


def parse_work_html(work: str, raw: bytes) -> dict[str, Any]:
    parsers = {"natrinai": parse_natrinai_html, "aingurunuru": parse_aingurunuru_html,
               "kuruntokai": parse_kuruntokai_html, "akananuru": parse_akananuru_html,
               "purananuru": parse_purananuru_text}
    try:
        return parsers[work](raw)
    except KeyError as exc:
        raise ValueError(f"Unsupported work: {work}") from exc


PURANANURU_HEADING_RE = re.compile(r"^(\d{1,3})\.\s*(.*)$")
PURANANURU_LOST_RE = re.compile(r"^267-\s*268\s+கிடைத்தில\s*$")
PURANANURU_LACUNA_RE = re.compile(r"(?:\.\s*){3,}")


def parse_purananuru_text(raw: bytes) -> dict[str, Any]:
    """Parse the user-preserved text export of Project Madurai pmuni0057."""
    lines = raw.decode("utf-8-sig").replace("\r\n", "\n").replace("\r", "\n").split("\n")
    starts: list[tuple[int, int, str]] = []
    lost_at = None
    for index, value in enumerate(lines):
        stripped = value.strip()
        match = PURANANURU_HEADING_RE.match(stripped)
        if match and 1 <= int(match.group(1)) <= 400:
            starts.append((index, int(match.group(1)), stripped))
        elif PURANANURU_LOST_RE.match(stripped):
            lost_at = index
    boundaries = sorted([(i, "poem", n, heading) for i, n, heading in starts] +
                        ([(lost_at, "lost", None, lines[lost_at].strip())] if lost_at is not None else []))
    poems: list[dict[str, Any]] = []
    unparsed: list[str] = []
    for position, (start, kind, number, heading) in enumerate(boundaries):
        stop = boundaries[position + 1][0] if position + 1 < len(boundaries) else next(
            (i for i in range(start + 1, len(lines)) if lines[i].strip() == "புறநானூறு முற்றும்."), len(lines))
        if kind == "lost":
            for lost_number in (267, 268):
                poems.append({"poem_number": lost_number, "poem_number_as_printed": f"267-268",
                              "printed_heading": heading, "title_as_printed": None,
                              "poet": None, "poet_as_printed": None, "addressee_as_printed": None,
                              "thinai": None, "thinai_as_printed": None, "thurai": None,
                              "printed_metadata_lines": [], "lines": [], "source_note_lines": [heading],
                              "status": "source-missing", "lacuna_present": False})
            continue
        block = lines[start + 1:stop]
        while block and not block[0].strip(): block.pop(0)
        metadata, body = [], []
        blank_at = next((i for i, value in enumerate(block) if not value.strip()), None)
        if blank_at is not None and any(x.strip() for x in block[blank_at + 1:]):
            metadata = [x.strip() for x in block[:blank_at] if x.strip()]
            body = [x.strip() for x in block[blank_at + 1:] if x.strip()]
        else:
            # Several source records omit the blank layout boundary.  Metadata
            # still has explicit Tamil labels; restore only that boundary.
            label_re = re.compile(r"^(?:பாடியவர்|பாடப்பட்டோன்|திணை|துறை|குறிப்பு|சிறப்பு)\s*[:;：]?")
            last_meta = max((i for i, value in enumerate(block) if label_re.match(value.strip())), default=-1)
            continuation_re = re.compile(r"^(?:வள்ளை|துறை|சிறப்பு|குறிப்பு)\s*[:;：]|^\(")
            while last_meta >= 0 and last_meta + 1 < len(block) and continuation_re.match(block[last_meta + 1].strip()):
                last_meta += 1
            metadata = [x.strip() for x in block[:last_meta + 1] if x.strip()]
            body = [x.strip() for x in block[last_meta + 1:] if x.strip()]
        fields = {"poet": None, "poet_as_printed": None, "addressee_as_printed": None,
                  "thinai": None, "thinai_as_printed": None, "thurai": None}
        joined = "\n".join(metadata)
        poet_line = next((x for x in metadata if x.startswith("பாடியவர்")), None)
        if poet_line:
            printed = re.sub(r"^பாடியவர்\s*[:：]?\s*", "", poet_line).strip().rstrip(".")
            fields["poet_as_printed"] = printed or None
            fields["poet"] = None if not printed or "தெரிந்தில" in printed else printed
        addressee_line = next((x for x in metadata if x.startswith("பாடப்பட்டோன்")), None)
        if addressee_line:
            printed_addressee = re.sub(r"^பாடப்பட்டோன்\s*[:：]?\s*", "", addressee_line).strip().rstrip(".")
            fields["addressee_as_printed"] = printed_addressee or None
        thinai = re.search(r"திணை\s*[:;：]\s*([^.;\n]+)", joined)
        if thinai:
            fields["thinai_as_printed"] = thinai.group(1).strip()
            fields["thinai"] = fields["thinai_as_printed"]
        thurai = re.search(r"துறை\s*[:;：]\s*([^.;\n]+)", joined)
        if thurai: fields["thurai"] = thurai.group(1).strip()
        poems.append({"poem_number": number, "poem_number_as_printed": number,
                      "printed_heading": heading, "title_as_printed": heading.split(".", 1)[1].strip(),
                      **fields, "printed_metadata_lines": metadata, "lines": body,
                      "source_note_lines": metadata, "status": "source-transcribed",
                      "lacuna_present": any(PURANANURU_LACUNA_RE.search(x) for x in body)})
    poems.sort(key=lambda x: x["poem_number"])
    counts = {n: sum(p["poem_number"] == n for p in poems) for n in range(1, 401)}
    firsts: dict[str, list[int]] = {}; bodies: dict[str, list[int]] = {}
    for poem in poems:
        if poem["lines"]:
            firsts.setdefault(poem["lines"][0], []).append(poem["poem_number"])
            bodies.setdefault(body_hash(poem["lines"]), []).append(poem["poem_number"])
    return {"parser": "purananuru-pmuni0057-text-export-v1", "title_tamil": "புறநானூறு",
            "title_english": "Puṟanāṉūṟu", "work_slug": "purananuru", "poems": poems,
            "missing_numbers": [n for n, c in counts.items() if c == 0],
            "duplicate_numbers": [n for n, c in counts.items() if c > 1],
            "source_lost_poems": [267, 268],
            "lacunose_poems": [p["poem_number"] for p in poems if p["lacuna_present"]],
            "shared_first_lines": [v for v in firsts.values() if len(v) > 1],
            "duplicate_bodies": [v for v in bodies.values() if len(v) > 1],
            "source_structure": {"printed_divisions": [], "navigation_strategy": "mechanical 50-poem ranges"},
            "unparsed_fragments": unparsed}


KURUNTOKAI_HEADING_RE = re.compile(r"^(\d{1,3})\.\s*(.+?)\s+-\s+(.+)$")


def parse_kuruntokai_html(raw: bytes) -> dict[str, Any]:
    """Parse the observed flat-BR grammar of Project Madurai pmuni0110."""
    soup = BeautifulSoup(raw.decode("utf-8-sig"), "lxml")
    lines = [x.strip() for x in soup.get_text("\n").splitlines() if x.strip()]
    invocation_at = next(i for i, x in enumerate(lines) if x == "கடவுள் வாழ்த்து")
    end = next(i for i, x in enumerate(lines) if "குறுந்தொகை முற்றிற்று" in x)
    content = lines[invocation_at:end]
    heading_positions = []
    for i, line in enumerate(content):
        m = KURUNTOKAI_HEADING_RE.match(line)
        if m and 1 <= int(m.group(1)) <= 401:
            heading_positions.append((i, m))
    invocation_lines = content[1:heading_positions[0][0]]
    invocation_poet = invocation_lines.pop() if invocation_lines and invocation_lines[-1].lstrip().startswith("-") else None
    poems = []
    for j, (start, match) in enumerate(heading_positions):
        stop = heading_positions[j + 1][0] if j + 1 < len(heading_positions) else len(content)
        block = content[start + 1:stop]
        # Poems 105 and 180 print the poet on the same HTML line as the final verse.
        if block:
            joined = re.match(r"^(.*?\.)(?:\s|\u00a0)+(-[^-].+)$", block[-1])
            if joined:
                block[-1:] = [joined.group(1).strip(), joined.group(2).strip()]
        poet_as_printed = block.pop().strip() if block and block[-1].lstrip().startswith("-") else None
        poet_value = poet_as_printed.lstrip("-").strip().rstrip(".") if poet_as_printed else None
        if poet_value is not None and not poet_value.strip("."):
            poet_value = None
        poems.append({"poem_number": int(match.group(1)), "printed_heading": content[start],
                      "thinai": match.group(2).strip(), "speaker": match.group(3).strip(),
                      "poet": poet_value, "poet_as_printed": poet_as_printed,
                      "lines": block, "source_note_lines": [], "status": "source-transcribed"})
    counts = {n: sum(p["poem_number"] == n for p in poems) for n in range(1, 402)}
    firsts: dict[str, list[int]] = {}
    bodies: dict[str, list[int]] = {}
    for poem in poems:
        if poem["lines"]:
            firsts.setdefault(poem["lines"][0], []).append(poem["poem_number"])
            bodies.setdefault(body_hash(poem["lines"]), []).append(poem["poem_number"])
    return {"parser": "kuruntokai-pmuni0110-v1", "title_tamil": "குறுந்தொகை",
            "title_english": "Kuruntokai", "work_slug": "kuruntokai", "poems": poems,
            "prefatory_text": {"heading": "கடவுள் வாழ்த்து", "lines": invocation_lines,
                               "poet_as_printed": invocation_poet},
            "missing_numbers": [n for n, c in counts.items() if c == 0],
            "duplicate_numbers": [n for n, c in counts.items() if c > 1],
            "shared_first_lines": [ns for ns in firsts.values() if len(ns) > 1],
            "duplicate_bodies": [ns for ns in bodies.values() if len(ns) > 1],
            "source_structure": {"printed_divisions": [], "navigation_strategy": "mechanical 50-poem ranges"},
            "unparsed_fragments": []}


AKANANURU_RECORD_RE = re.compile(
    r'<tr><td\s+width="50"\s+valign="top">\s*(\d{1,3})\s*<td\s+width="400">',
    re.IGNORECASE,
)
AKANANURU_LAYOUT_MARKER_RE = re.compile(r"\s*\.\s*\d{1,3}-\d+\s*$")


def parse_akananuru_html(raw: bytes) -> dict[str, Any]:
    """Parse the table-based source-only Project Madurai pmuni0229 edition.

    The page prints one record table per poem.  Record 174 starts as another
    row inside malformed table markup, so parsing is anchored on the repeated
    number/body-cell grammar rather than on DOM table boundaries.  Source-order
    record numbers remain canonical; the two duplicated printed labels are
    retained separately as evidence.
    """
    html = raw.decode("utf-8-sig")
    matches = list(AKANANURU_RECORD_RE.finditer(html))
    records: list[dict[str, Any]] = []
    for source_order, match in enumerate(matches):
        stop = matches[source_order + 1].start() if source_order + 1 < len(matches) else len(html)
        fragment = html[match.start():stop]
        # Each fragment is deliberately incomplete/malformed source markup.
        # lxml recovers the sibling cells correctly; suppress only its known
        # BeautifulSoup strip_cdata deprecation noise for these local parses.
        with warnings.catch_warnings():
            warnings.filterwarnings("ignore", message="The 'strip_cdata' option.*", category=DeprecationWarning)
            soup = BeautifulSoup("<table>" + fragment + "</table>", "lxml")
        cells = soup.find_all("td")
        lines: list[str] = []
        for cell in cells[1:]:
            value = cell.get_text("\n", strip=True)
            if not value or re.fullmatch(r"\d+", value):
                continue
            for line in value.splitlines():
                line = AKANANURU_LAYOUT_MARKER_RE.sub("", line.strip())
                if line:
                    lines.append(line)
        printed_number = int(match.group(1))
        if source_order == 0:
            canonical_number = 0
        else:
            canonical_number = source_order
        records.append({
            "poem_number": canonical_number,
            "poem_number_as_printed": printed_number,
            "printed_heading": str(printed_number),
            "source_order": source_order,
            "lines": lines,
            "source_note_lines": [],
            "status": "source-transcribed",
        })

    invocation = records[0] if records and records[0]["poem_number"] == 0 else None
    poems = records[1:] if invocation else records
    divisions = [
        {"sequence": 1, "heading_as_printed": "1.  களிற்றியாணை நிரை", "normalized_structural_label": "களிற்றியாணை நிரை",
         "poem_start": 1, "poem_end": 120, "heading_source": "Project Madurai printed division heading"},
        {"sequence": 2, "heading_as_printed": "2.  மணிமிடை பவளம்", "normalized_structural_label": "மணிமிடை பவளம்",
         "poem_start": 121, "poem_end": 300, "heading_source": "Project Madurai printed division heading"},
        {"sequence": 3, "heading_as_printed": "3.  நித்திலக்கோவை", "normalized_structural_label": "நித்திலக்கோவை",
         "poem_start": 301, "poem_end": 400, "heading_source": "Project Madurai printed division heading"},
    ]
    for poem in poems:
        division = next(d for d in divisions if d["poem_start"] <= poem["poem_number"] <= d["poem_end"])
        poem["major_division"] = division["normalized_structural_label"]
        poem["major_division_as_printed"] = division["heading_as_printed"]
        poem["major_division_sequence"] = division["sequence"]

    firsts: dict[str, list[int]] = {}
    bodies: dict[str, list[int]] = {}
    for poem in poems:
        if poem["lines"]:
            firsts.setdefault(poem["lines"][0], []).append(poem["poem_number"])
            bodies.setdefault(body_hash(poem["lines"]), []).append(poem["poem_number"])
    printed = [p["poem_number_as_printed"] for p in poems]
    return {
        "parser": "akananuru-pmuni0229-v1",
        "title_tamil": "அகநானுறு",
        "title_english": "Akanāṉūṟu",
        "work_slug": "akananuru",
        "poems": poems,
        "prefatory_text": ({"heading": "Unnumbered record 0 / கடவுள் வாழ்த்து",
                            "number_as_printed": 0, "lines": invocation["lines"]} if invocation else None),
        "printed_divisions": divisions,
        "printed_number_missing": [n for n in range(1, 401) if n not in printed],
        "printed_number_duplicates": sorted(n for n in set(printed) if printed.count(n) > 1),
        "canonical_missing_numbers": [n for n in range(1, 401) if n not in {p["poem_number"] for p in poems}],
        "canonical_duplicate_numbers": [],
        "numbering_anomalies": [
            {"canonical_poem_number": p["poem_number"], "poem_number_as_printed": p["poem_number_as_printed"],
             "source_order": p["source_order"]}
            for p in poems if p["poem_number"] != p["poem_number_as_printed"]
        ],
        "shared_first_lines": [ns for ns in firsts.values() if len(ns) > 1],
        "duplicate_bodies": [ns for ns in bodies.values() if len(ns) > 1],
        "unparsed_fragments": [],
    }


def frontmatter(poem: dict[str, Any], source_url: str, source_file: str) -> dict[str, Any]:
    lines = poem["lines"]
    number = poem["poem_number"]
    textual_status = "lost" if number == 234 else "incomplete" if number == 385 else "complete"
    poet_uncertain = poem["poet"] is None and "(?)" in poem.get("printed_heading", "")
    return {
        "work": "நற்றிணை",
        "work_english": "Naṟṟiṇai",
        "work_slug": WORK,
        "poem_number": poem["poem_number"],
        "section": section_name(poem["poem_number"]),
        "thinai": poem["thinai"],
        "thinai_source": "Project Madurai heading" if poem["thinai"] else None,
        "speaker": None,
        "speaker_source": None,
        "poet": poem["poet"],
        "poet_source": "Project Madurai heading marked uncertain" if poet_uncertain else "Project Madurai heading" if poem["poet"] else None,
        "poet_as_printed": "(?)" if poet_uncertain else poem["poet"],
        "first_line": lines[0] if lines else "",
        "line_count": len(lines),
        "textual_status": textual_status,
        "canonical_text_available": number != 234,
        "candidate_texts_available": number == 234,
        "lacuna_present": number == 385,
        "lacuna_location": "ending" if number == 385 else None,
        "source_note_available": bool(poem["source_note_lines"]),
        "source_note_source": "Project Madurai printed prose" if poem["source_note_lines"] else None,
        "extraction_status": "success",
        "source": "Project Madurai",
        "source_url": source_url,
        "project_madurai_id": PM_ID,
        "source_file": source_file,
        "language": "Tamil",
        "script": "Tamil",
        "status": poem["status"],
        "editorial_changes": False,
    }


def canonical_body_text(lines: list[str]) -> str:
    """Apply only permitted canonical body transformations."""
    cleaned = [unicodedata.normalize("NFC", line.replace("\r", "").strip()) for line in lines]
    return "\n".join(line for line in cleaned if line)


def body_hash(lines: list[str]) -> str:
    return hashlib.sha256(canonical_body_text(lines).encode("utf-8")).hexdigest()


def markdown_literary_lines(markdown_body: str) -> list[str]:
    """Return only literary lines, excluding YAML, headings and printed prose note."""
    main = markdown_body.split("## Source note (as printed)", 1)[0]
    return [line.strip() for line in main.splitlines()
            if line.strip() and not line.startswith("# ")]


def section_name(number: int) -> str:
    start = ((number - 1) // 50) * 50 + 1
    return f"{start:03d}-{min(start + 49, 400):03d}"


def poem_markdown(poem: dict[str, Any], source_url: str, source_file: str) -> str:
    fm = yaml.safe_dump(frontmatter(poem, source_url, source_file), allow_unicode=True,
                        sort_keys=False, default_flow_style=False).strip()
    body = "\n".join(poem["lines"])
    out = f"---\n{fm}\n---\n\n# நற்றிணை {poem['poem_number']}\n\n{body}\n"
    if poem["source_note_lines"]:
        out += "\n## Source note (as printed)\n\n" + "\n".join(poem["source_note_lines"]) + "\n"
    return out


def read_frontmatter(path: Path) -> tuple[dict[str, Any], str]:
    text = path.read_text(encoding="utf-8")
    match = re.match(r"\A---[ \t]*\n(.*?)^---[ \t]*\n", text, re.MULTILINE | re.DOTALL)
    if not match:
        raise ValueError("missing YAML delimiters")
    return yaml.safe_load(match.group(1)), text[match.end():]


ISSUE_FIELDS = ["work", "poem_number", "issue_type", "severity", "message", "source_file", "markdown_file"]


def write_issues(rows: list[dict[str, Any]]) -> None:
    p = paths()["issues"]
    p.parent.mkdir(parents=True, exist_ok=True)
    with p.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=ISSUE_FIELDS)
        w.writeheader()
        w.writerows(rows)


def write_work_issues(work: str, rows: list[dict[str, Any]]) -> None:
    """Replace one work's issue rows while retaining every other corpus."""
    p = paths()["issues"]
    retained: list[dict[str, Any]] = []
    if p.exists():
        with p.open(encoding="utf-8", newline="") as f:
            retained = [row for row in csv.DictReader(f) if row.get("work") != work]
    write_issues(retained + rows)


def today() -> str:
    return date.today().isoformat()
