#!/usr/bin/env python3
"""Explicit parsers for the Patiṉeṇkīḻkkaṇakku programme.

This module deliberately has no content-guessing fallback. Each supported work
must register an observed Project Madurai source grammar.
"""
from __future__ import annotations

import collections
import csv
import hashlib
import json
import re
import unicodedata
from pathlib import Path

import yaml
from bs4 import BeautifulSoup

from corpuslib import (ROOT, body_hash, canonical_body_text,
                       markdown_literary_lines, read_frontmatter, write_json,
                       write_text)

SOURCE_DIR = ROOT / "sources/raw-html/pathinenkilkanakku"

WORK_SPECS = {
    "tirukkural": {
        "title_tamil": "திருக்குறள்",
        "title_english": "Tirukkural",
        "project_madurai_id": "pmuni0001",
        "source_url": "https://www.projectmadurai.org/pm_etexts/utf8/pmuni0001.html",
        "source_file": "sources/raw-html/pathinenkilkanakku/pmuni0001.html",
        "source_sha256": "1d1704d1f2e6dd649d40f29253bb6cb1ac8a0e316841601e3b3223feac548f18",
        "expected_records": 1330,
        "expected_sections": 133,
        "parser": "tirukkural-pmuni0001-v1",
    },
    "naladiyar": {
        "title_tamil": "நாலடியார்",
        "title_english": "Nālāṭiyār",
        "project_madurai_id": "pmuni0016",
        "source_url": "https://www.projectmadurai.org/pm_etexts/utf8/pmuni0016.html",
        "source_file": "sources/raw-html/pathinenkilkanakku/pmuni0016.html",
        "source_sha256": "5ab43427d8a5db080e88d762bbca318ed00773c368e491ca197c4918663f6772",
        "expected_records": 400,
        "expected_sections": 40,
        "parser": "naladiyar-pmuni0016-v1",
    },
    "nanmanikkadigai": {
        "title_tamil": "நான்மணிக்கடிகை",
        "title_english": "Nāṉmaṇikkaṭigai",
        "project_madurai_id": "pmuni0047",
        "source_url": "https://www.projectmadurai.org/pm_etexts/utf8/pmuni0047.html",
        "source_file": "sources/raw-html/pathinenkilkanakku/pmuni0047.html",
        "source_sha256": "87758515c8d2888e9fc7176f960ea0693f3accd8f0c33270651104d85cf05df5",
        "expected_records": 106,
        "expected_sections": 2,
        "parser": "nanmanikkadigai-pmuni0047-v1",
    },
    "inna-narpathu": {
        "title_tamil": "இன்னா நாற்பது",
        "title_english": "Iṉṉā Nāṟpatu",
        "project_madurai_id": "pmuni0025",
        "source_url": "https://www.projectmadurai.org/pm_etexts/utf8/pmuni0025.html",
        "source_file": "sources/raw-html/pathinenkilkanakku/pmuni0025.html",
        "source_sha256": "11efaae0d942d244ec6f051905b4cb00e1f0424741dc88d1448332a6eb767b9b",
        "expected_records": 40,
        "expected_sections": 2,
        "parser": "inna-narpathu-pmuni0025-v1",
    },
    "iniyavai-narpathu": {
        "title_tamil": "இனியவை நாற்பது",
        "title_english": "Iṉiyavai Nāṟpatu",
        "project_madurai_id": "pmuni0025",
        "source_url": "https://www.projectmadurai.org/pm_etexts/utf8/pmuni0025.html",
        "source_file": "sources/raw-html/pathinenkilkanakku/pmuni0025.html",
        "source_sha256": "11efaae0d942d244ec6f051905b4cb00e1f0424741dc88d1448332a6eb767b9b",
        "expected_records": 40,
        "expected_sections": 2,
        "parser": "iniyavai-narpathu-pmuni0025-v1",
    },
    "kar-narpathu": {
        "title_tamil": "கார் நாற்பது", "title_english": "Kār Nāṟpatu",
        "project_madurai_id": "pmuni0029",
        "source_url": "https://www.projectmadurai.org/pm_etexts/utf8/pmuni0029.html",
        "source_file": "sources/raw-html/pathinenkilkanakku/pmuni0029.html",
        "source_sha256": "57ee41487ccf6a9f3550f213e08c910ea0d18def047700cd16c0c71348bfdaef",
        "expected_records": 40, "expected_sections": 1,
        "parser": "kar-narpathu-pmuni0029-v1",
    },
    "kalavazhi-narpathu": {
        "title_tamil": "களவழி நாற்பது", "title_english": "Kaḷavaḻi Nāṟpatu",
        "project_madurai_id": "pmuni0025",
        "source_url": "https://www.projectmadurai.org/pm_etexts/utf8/pmuni0025.html",
        "source_file": "sources/raw-html/pathinenkilkanakku/pmuni0025.html",
        "source_sha256": "11efaae0d942d244ec6f051905b4cb00e1f0424741dc88d1448332a6eb767b9b",
        "expected_records": 40, "expected_sections": 1,
        "parser": "kalavazhi-narpathu-pmuni0025-v1",
    },
    "aintinai-aimpathu": {
        "title_tamil": "ஐந்திணை ஐம்பது", "title_english": "Aintiṇai Aimpathu",
        "project_madurai_id": "pmuni0027",
        "source_url": "https://www.projectmadurai.org/pm_etexts/utf8/pmuni0027.html",
        "source_file": "sources/raw-html/pathinenkilkanakku/pmuni0027.html",
        "source_sha256": "3b245f0f64191e63da31b5be5954142380ac428f348d5caf04a5747511a95ad3",
        "expected_records": 50, "expected_sections": 5,
        "parser": "aintinai-aimpathu-pmuni0027-v1",
    },
    "aintinai-elupathu": {
        "title_tamil": "ஐந்திணை எழுபது", "title_english": "Aintiṇai Eḻupathu",
        "project_madurai_id": "pmuni0027",
        "source_url": "https://www.projectmadurai.org/pm_etexts/utf8/pmuni0027.html",
        "source_file": "sources/raw-html/pathinenkilkanakku/pmuni0027.html",
        "source_sha256": "3b245f0f64191e63da31b5be5954142380ac428f348d5caf04a5747511a95ad3",
        "expected_records": 70, "expected_sections": 5,
        "parser": "aintinai-elupathu-pmuni0027-v1",
    },
    "thinaimalai-nutraimbathu": {
        "title_tamil": "திணைமாலை நூற்றைம்பது", "title_english": "Tiṇaimālai Nūṟṟaimpatu",
        "project_madurai_id": "pmuni0056",
        "source_url": "https://www.projectmadurai.org/pm_etexts/utf8/pmuni0056.html",
        "source_file": "sources/raw-html/pathinenkilkanakku/pmuni0056.html",
        "source_sha256": "29c2432a335f4818ef0a650c1ff7b5cf46c8484c810f15767de80e239955e31b",
        "expected_records": 153, "expected_sections": 5,
        "parser": "thinaimalai-nutraimbathu-pmuni0056-v1",
    },
    "thinaimozhi-aimpathu": {
        "title_tamil":"திணை மொழி ஐம்பது","title_english":"Tiṇaimoḻi Aimpathu",
        "project_madurai_id":"pmuni0027","source_url":"https://www.projectmadurai.org/pm_etexts/utf8/pmuni0027.html",
        "source_file":"sources/raw-html/pathinenkilkanakku/pmuni0027.html","source_sha256":"3b245f0f64191e63da31b5be5954142380ac428f348d5caf04a5747511a95ad3",
        "expected_records":50,"expected_sections":5,"parser":"thinaimozhi-aimpathu-pmuni0027-v1"},
    "tirikatukam": {
        "title_tamil":"திரிகடுகம்","title_english":"Tirikaṭukam","project_madurai_id":"pmuni0048",
        "source_url":"https://www.projectmadurai.org/pm_etexts/utf8/pmuni0048.html",
        "source_file":"sources/raw-html/pathinenkilkanakku/pmuni0048.html","source_sha256":"c4d233ffa89b4e98bd98c2247d1611a044bc1d4f1309f0e1928ad6ab98e36f9f",
        "expected_records":100,"expected_sections":1,"parser":"tirikatukam-pmuni0048-v1"},
    "acharakkovai": {
        "title_tamil":"ஆசாரக்கோவை","title_english":"Ācārakkōvai","project_madurai_id":"pmuni0024",
        "source_url":"https://www.projectmadurai.org/pm_etexts/utf8/pmuni0024.html",
        "source_file":"sources/raw-html/pathinenkilkanakku/pmuni0024.html","source_sha256":"d9256bb5837e4934142b58bf7e5def7db794fe5620a1475d78af10adac62cb5a",
        "expected_records":100,"expected_sections":1,"parser":"acharakkovai-pmuni0024-v1"},
    "pazhamozhi-nanuru": {
        "title_tamil":"பழமொழி நானூறு","title_english":"Paḻamoḻi Nāṉūṟu","project_madurai_id":"pmuni0036",
        "source_url":"https://www.projectmadurai.org/pm_etexts/utf8/pmuni0036.html",
        "source_file":"sources/raw-html/pathinenkilkanakku/pmuni0036.html","source_sha256":"a238f6c3eb3d3645b6344c73109b02673c567ed12289a0c24c4ab203622b6122",
        "expected_records":399,"expected_sections":33,"parser":"pazhamozhi-nanuru-pmuni0036-v1"},
    "sirupanchamulam": {
        "title_tamil":"சிறுபஞ்சமூலம்","title_english":"Ciṟupañcamūlam","project_madurai_id":"pmuni0029",
        "source_url":"https://www.projectmadurai.org/pm_etexts/utf8/pmuni0029.html",
        "source_file":"sources/raw-html/pathinenkilkanakku/pmuni0029.html","source_sha256":"57ee41487ccf6a9f3550f213e08c910ea0d18def047700cd16c0c71348bfdaef",
        "expected_records":98,"expected_sections":2,"parser":"sirupanchamulam-pmuni0029-v1"},
    "muthumozhi-kanchi": {
        "title_tamil":"முதுமொழிக் காஞ்சி","title_english":"Mutumoḻik Kāñci","project_madurai_id":"pmuni0025",
        "source_url":"https://www.projectmadurai.org/pm_etexts/utf8/pmuni0025.html",
        "source_file":"sources/raw-html/pathinenkilkanakku/pmuni0025.html","source_sha256":"11efaae0d942d244ec6f051905b4cb00e1f0424741dc88d1448332a6eb767b9b",
        "expected_records":100,"expected_sections":10,"parser":"muthumozhi-kanchi-pmuni0025-v1"},
    "elati": {
        "title_tamil":"ஏலாதி","title_english":"Ēlāti","project_madurai_id":"pmuni0029",
        "source_url":"https://www.projectmadurai.org/pm_etexts/utf8/pmuni0029.html",
        "source_file":"sources/raw-html/pathinenkilkanakku/pmuni0029.html","source_sha256":"57ee41487ccf6a9f3550f213e08c910ea0d18def047700cd16c0c71348bfdaef",
        "expected_records":80,"expected_sections":1,"parser":"elati-pmuni0029-v1"},
    "kainnilai": {
        "title_tamil":"கைந்நிலை","title_english":"Kainnilai","project_madurai_id":"pmuni0051",
        "source_url":"https://www.projectmadurai.org/pm_etexts/utf8/pmuni0051.html",
        "source_file":"sources/raw-html/pathinenkilkanakku/pmuni0051.html","source_sha256":"4927a2832b00858bf358ca58120cfef4bfd1adae587cf9ea9eada98fd785b6c8",
        "expected_records":60,"expected_sections":4,"parser":"kainnilai-pmuni0051-v1"},
}


def spec(work: str) -> dict:
    try:
        return WORK_SPECS[work]
    except KeyError as exc:
        raise ValueError(f"No Patiṉeṇkīḻkkaṇakku parser profile for {work}") from exc


def work_paths(work: str) -> dict[str, Path]:
    s = spec(work)
    return {
        "raw": ROOT / s["source_file"],
        "raw_txt": ROOT / f"sources/raw-txt/{work}.txt",
        "source_metadata": ROOT / f"sources/source-metadata/{work}.json",
        "parsed": ROOT / f"sources/source-metadata/{work}-parsed.json",
        "normalized": ROOT / f"sources/source-metadata/{work}-normalized.json",
        "reconnaissance": ROOT / f"sources/source-metadata/{work}-reconnaissance.json",
        "corpus": ROOT / f"corpus/{work}",
        "poems": ROOT / f"corpus/{work}/poems",
        "sections": ROOT / f"corpus/{work}/sections",
        "metadata": ROOT / f"corpus/{work}/metadata.json",
        "full_text": ROOT / f"corpus/{work}/full-text.md",
        "structure": ROOT / f"corpus/{work}/structure-inventory.json",
        "validation": ROOT / f"manifests/{work}-validation-report.json",
    }


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def _visible_lines(raw: bytes) -> list[str]:
    soup = BeautifulSoup(raw.decode("utf-8-sig"), "lxml")
    return [x.strip() for x in soup.get_text("\n").splitlines() if x.strip()]


def _is_tirukkural_structure(line: str) -> bool:
    return bool(re.match(r"^\d+[.,]", line) and not re.search(r"\d+\s*$", line))


def parse_tirukkural(raw: bytes) -> dict:
    lines = _visible_lines(raw)
    start = lines.index("1.1.1   கடவுள் வாழ்த்து")
    end = lines.index("திருக்குறள் முற்றிற்று")
    current_major = None
    current_subdivision = None
    pending_chapter = None
    records = []
    structural = []
    buffer: list[str] = []

    for source_index, line in enumerate(lines[13:end], 13):
        # The work title is repeated immediately before each major division.
        # It is page navigation, not a line of couplet 1, 381, or 1081.
        if line == "திருக்குறள்":
            structural.append({"source_line": source_index,
                               "heading_as_printed": line,
                               "type": "repeated_work_title"})
            continue
        if line.endswith("முற்றிற்று"):
            structural.append({"source_line": source_index, "heading_as_printed": line,
                               "type": "closing"})
            continue
        if _is_tirukkural_structure(line):
            # Read every leading ordinal component; malformed source forms such
            # as ``2,3.6`` and ``3..2. 9`` may contain whitespace mid-ordinal.
            components = re.findall(r"\d+", line)
            if len(components) == 1:
                current_major = line
                kind = "major_division"
            elif len(components) == 2:
                current_subdivision = line
                kind = "subdivision"
            else:
                pending_chapter = line
                kind = "chapter"
            structural.append({"source_line": source_index,
                               "heading_as_printed": line, "type": kind})
            continue

        buffer.append(line)
        marker = re.search(r"(\d+)\s*$", line)
        if not marker:
            continue
        printed_number = int(marker.group(1))
        buffer[-1] = line[:marker.start()].replace("\u00a0", "").rstrip()
        canonical_number = len(records) + 1
        chapter_sequence = (canonical_number - 1) // 10 + 1
        chapter_start = (chapter_sequence - 1) * 10 + 1
        # The source omits a distinct 3.2.1 chapter heading before poem 1151.
        chapter_heading = pending_chapter if canonical_number == chapter_start else records[-1]["chapter_heading_as_printed"]
        if canonical_number == 1151:
            chapter_heading = None
        record = {
            "poem_number": canonical_number,
            "poem_number_as_printed": printed_number,
            "source_order": canonical_number,
            "printed_number_matches_sequence": printed_number == canonical_number,
            "lines": buffer,
            "source_note_lines": [],
            "status": "source-transcribed",
            "major_division_as_printed": current_major,
            "subdivision_as_printed": current_subdivision,
            "chapter_sequence": chapter_sequence,
            "chapter_heading_as_printed": chapter_heading,
            "position_within_chapter": (canonical_number - 1) % 10 + 1,
        }
        records.append(record)
        buffer = []
        if canonical_number == chapter_start:
            pending_chapter = None

    if buffer:
        raise ValueError(f"Unparsed Tirukkural literary fragments: {buffer}")
    if len(records) != 1330:
        raise ValueError(f"Expected 1330 Tirukkural records; found {len(records)}")

    chapters = []
    for sequence in range(1, 134):
        members = [x for x in records if x["chapter_sequence"] == sequence]
        headings = {x["chapter_heading_as_printed"] for x in members}
        chapters.append({
            "sequence": sequence,
            "poem_start": members[0]["poem_number"],
            "poem_end": members[-1]["poem_number"],
            "record_count": len(members),
            "heading_as_printed": members[0]["chapter_heading_as_printed"],
            "heading_consistent_within_group": len(headings) == 1,
            "major_division_as_printed": members[0]["major_division_as_printed"],
            "subdivision_as_printed": members[0]["subdivision_as_printed"],
            "provenance": ("Project Madurai printed chapter heading"
                           if members[0]["chapter_heading_as_printed"]
                           else "mechanically identified ten-couplet chapter; printed chapter heading absent"),
        })
    return {
        "parser": WORK_SPECS["tirukkural"]["parser"],
        "work_slug": "tirukkural",
        "title_tamil_as_printed": "திருவள்ளுவர் அருளிய திருக்குறள்",
        "records": records,
        "poems": records,
        "structure": structural,
        "chapters": chapters,
        "numbering_anomalies": [
            {"poem_number": x["poem_number"],
             "poem_number_as_printed": x["poem_number_as_printed"]}
            for x in records if not x["printed_number_matches_sequence"]
        ],
        "heading_anomalies": [
            {"condition": "malformed_printed_chapter_ordinal",
             "heading_as_printed": "2,3.6   நட்பு", "chapter_sequence": 79},
            {"condition": "printed_chapter_heading_absent",
             "heading_as_printed": None, "chapter_sequence": 116,
             "poem_start": 1151, "poem_end": 1160},
            {"condition": "malformed_printed_chapter_ordinal",
             "heading_as_printed": "3..2. 9  உறுப்புநலனழிதல்",
             "chapter_sequence": 124},
        ],
        "unparsed_fragments": [],
    }


def parse_naladiyar(raw: bytes) -> dict:
    lines = _visible_lines(raw)
    start = lines.index("1. அறத்துப்பால்")
    end = next(i for i, x in enumerate(lines) if
               x.startswith("This webpage was last revised"))
    invocation = {
        "heading_as_printed": "கடவுள் வாழ்த்து",
        "lines": lines[28:32],
        "provenance": "printed by selected canonical source",
    }
    current_major = None
    current_chapter = None
    records = []
    chapters = []
    current = None
    expected = 1

    def finish():
        nonlocal current
        if current is not None:
            records.append(current)
            current = None

    for source_index, line in enumerate(lines[start:end], start):
        if line in {"1. அறத்துப்பால்", "2. பொருட்பால்", "3. காமத்துப்பால்"}:
            finish()
            current_major = line
            continue
        if re.match(r"^\d+\.\d+\s", line):
            finish()
            current_chapter = line
            chapter_number = int(re.match(r"^\d+\.(\d+)", line).group(1))
            chapters.append({
                "sequence": chapter_number,
                "heading_as_printed": line,
                "major_division_as_printed": current_major,
                "poem_start": (chapter_number - 1) * 10 + 1,
                "poem_end": chapter_number * 10,
                "record_count": 10,
                "provenance": "Project Madurai printed chapter heading",
            })
            continue
        m = re.match(r"^(\d{1,3})\.\s*(.*)$", line)
        if m and int(m.group(1)) == expected:
            finish()
            current = {
                "poem_number": expected,
                "poem_number_as_printed": int(m.group(1)),
                "source_order": expected,
                "lines": [m.group(2).strip()],
                "source_note_lines": [],
                "status": "source-transcribed",
                "major_division_as_printed": current_major,
                "chapter_sequence": (expected - 1) // 10 + 1,
                "chapter_heading_as_printed": current_chapter,
                "position_within_chapter": (expected - 1) % 10 + 1,
            }
            expected += 1
            continue
        if current is not None:
            current["lines"].append(line)
    finish()
    if len(records) != 400:
        raise ValueError(f"Expected 400 Nālāṭiyār records; found {len(records)}")
    if any(len(x["lines"]) != 4 for x in records):
        raise ValueError("Nālāṭiyār source grammar did not yield four lines per record")
    return {
        "parser": WORK_SPECS["naladiyar"]["parser"],
        "work_slug": "naladiyar",
        "title_tamil_as_printed": "நாலடியார்",
        "prefatory_text": invocation,
        "poems": records,
        "chapters": chapters,
        "numbering_anomalies": [],
        "heading_anomalies": [{
            "condition": "major_division_ordinal_mismatch",
            "heading_as_printed": "2.39 கற்புடை மகளிர்",
            "chapter_sequence": 39,
            "context": "printed under 3. காமத்துப்பால்"
        }],
        "unparsed_fragments": [],
    }


def parse_nanmanikkadigai(raw: bytes) -> dict:
    lines = _visible_lines(raw)
    start = lines.index("கடவுள் வாழ்த்து")
    end = lines.index("நான்மணிக்கடிகை முற்றிற்று.")
    records = []
    buffer = []
    current_section = None
    for line in lines[start:end]:
        if line in {"கடவுள் வாழ்த்து", "நூல்"}:
            current_section = line
            continue
        buffer.append(line)
        marker = re.search(r"(\d{1,3})\s*$", line)
        if not marker:
            continue
        printed = int(marker.group(1))
        buffer[-1] = line[:marker.start()].replace("\u00a0", "").rstrip()
        sequence = len(records) + 1
        records.append({
            "poem_number": sequence, "poem_number_as_printed": printed,
            "source_order": sequence, "lines": buffer,
            "source_note_lines": [], "status": "source-transcribed",
            "section_as_printed": current_section,
            "section_sequence": 1 if current_section == "கடவுள் வாழ்த்து" else 2,
        })
        buffer = []
    if buffer:
        raise ValueError(f"Unparsed Nāṉmaṇikkaṭigai fragments: {buffer}")
    if len(records) != 106:
        raise ValueError(f"Expected 106 Nāṉmaṇikkaṭigai records; found {len(records)}")
    anomalies = [{"poem_number": x["poem_number"],
                  "poem_number_as_printed": x["poem_number_as_printed"]}
                 for x in records if x["poem_number"] != x["poem_number_as_printed"]]
    return {
        "parser": WORK_SPECS["nanmanikkadigai"]["parser"],
        "work_slug": "nanmanikkadigai",
        "title_tamil_as_printed": "விளம்பிநாகனாரின் நான்மணிக்கடிகை",
        "poems": records,
        "sections": [
            {"sequence": 1, "heading_as_printed": "கடவுள் வாழ்த்து",
             "poem_start": 1, "poem_end": 1, "record_count": 1,
             "provenance": "Project Madurai printed heading"},
            {"sequence": 2, "heading_as_printed": "நூல்",
             "poem_start": 2, "poem_end": 106, "record_count": 105,
             "provenance": "Project Madurai printed heading"},
        ],
        "numbering_anomalies": anomalies,
        "heading_anomalies": [],
        "unparsed_fragments": [],
    }


def parse_inna_narpathu(raw: bytes) -> dict:
    lines = _visible_lines(raw)
    start = lines.index("கடவுள் வாழ்த்து", lines.index("1. இன்னா நாற்பது : கபிலர் இயற்றியது (கி பி 50-125)"))
    end = lines.index("இன்னா நாற்பது முற்றிற்று")
    nul = lines.index("நூல்", start, end)
    invocation = {
        "heading_as_printed": "கடவுள் வாழ்த்து",
        "lines": lines[start + 1:start + 5],
        "source_note_lines": [lines[start + 5]],
        "provenance": "Project Madurai printed unnumbered literary text and variant note",
    }
    records = []
    buffer = []
    for line in lines[nul + 1:end]:
        if re.match(r"^[@%&]", line):
            if not records:
                raise ValueError("Variant note precedes first Iṉṉā Nāṟpatu record")
            records[-1]["source_note_lines"].append(line)
            continue
        buffer.append(line)
        marker = re.search(r"(\d{1,2})\s*$", line)
        if not marker:
            continue
        printed = int(marker.group(1))
        buffer[-1] = line[:marker.start()].replace("\u00a0", "").rstrip()
        sequence = len(records) + 1
        records.append({
            "poem_number": sequence, "poem_number_as_printed": printed,
            "source_order": sequence, "lines": buffer, "source_note_lines": [],
            "status": "source-transcribed", "section_as_printed": "நூல்",
            "section_sequence": 2,
        })
        buffer = []
    if buffer:
        raise ValueError(f"Unparsed Iṉṉā Nāṟpatu fragments: {buffer}")
    if len(records) != 40:
        raise ValueError(f"Expected 40 Iṉṉā Nāṟpatu records; found {len(records)}")
    return {
        "parser": WORK_SPECS["inna-narpathu"]["parser"],
        "work_slug": "inna-narpathu",
        "title_tamil_as_printed": "இன்னா நாற்பது : கபிலர் இயற்றியது",
        "prefatory_text": invocation,
        "poems": records,
        "sections": [
            {"sequence": 1, "heading_as_printed": "கடவுள் வாழ்த்து",
             "record_type": "unnumbered_literary_text", "record_count": 0,
             "provenance": "Project Madurai printed heading"},
            {"sequence": 2, "heading_as_printed": "நூல்",
             "poem_start": 1, "poem_end": 40, "record_count": 40,
             "provenance": "Project Madurai printed heading"},
        ],
        "numbering_anomalies": [],
        "heading_anomalies": [],
        "unparsed_fragments": [],
    }


def parse_iniyavai_narpathu(raw: bytes) -> dict:
    lines = _visible_lines(raw)
    work_heading = "2.  இனியவை நாற்பது : பூதஞ்சேந்தனார் இயற்றியது"
    start = lines.index("கடவுள் வாழ்த்து", lines.index(work_heading))
    end = lines.index("இனியவை நாற்பது முற்றிற்று")
    nul = lines.index("நூல்", start, end)
    invocation = {"heading_as_printed": "கடவுள் வாழ்த்து",
                  "lines": lines[start + 1:nul], "source_note_lines": [],
                  "provenance": "Project Madurai printed unnumbered literary text"}
    records = []
    buffer = []
    for line in lines[nul + 1:end]:
        buffer.append(line)
        marker = re.search(r"(\d{1,2})\s*$", line)
        if not marker:
            continue
        printed = int(marker.group(1))
        buffer[-1] = line[:marker.start()].replace("\u00a0", "").rstrip()
        sequence = len(records) + 1
        records.append({"poem_number": sequence,
                        "poem_number_as_printed": printed,
                        "source_order": sequence, "lines": buffer,
                        "source_note_lines": [], "status": "source-transcribed",
                        "section_as_printed": "நூல்", "section_sequence": 2})
        buffer = []
    if buffer or len(records) != 40:
        raise ValueError(f"Iṉiyavai Nāṟpatu parse failure: {len(records)} records; residual {buffer}")
    return {"parser": WORK_SPECS["iniyavai-narpathu"]["parser"],
            "work_slug": "iniyavai-narpathu",
            "title_tamil_as_printed": work_heading,
            "prefatory_text": invocation, "poems": records,
            "sections": [
                {"sequence": 1, "heading_as_printed": "கடவுள் வாழ்த்து",
                 "record_type": "unnumbered_literary_text", "record_count": 0,
                 "provenance": "Project Madurai printed heading"},
                {"sequence": 2, "heading_as_printed": "நூல்",
                 "poem_start": 1, "poem_end": 40, "record_count": 40,
                 "provenance": "Project Madurai printed heading"}],
            "numbering_anomalies": [], "heading_anomalies": [],
            "unparsed_fragments": []}


def parse_kar_narpathu(raw: bytes) -> dict:
    lines = _visible_lines(raw)
    start = lines.index('1.  கார் மதுரைக் கண்ணங்கூத்தனார் அருளிய "கார் நாற்பது"')
    end = lines.index("கார் நாற்பது முற்றிற்று")
    source = lines[start + 2:end]
    records = []
    segment = []
    for line in source:
        segment.append(line)
        marker = re.search(r"(\d{1,2})\s*$", line)
        if not marker:
            continue
        printed = int(marker.group(1))
        segment[-1] = line[:marker.start()].replace("\u00a0", "").rstrip()
        leading_variants = []
        while segment and re.match(r"^[@%&ஃ]", segment[0]):
            leading_variants.append(segment.pop(0))
        if leading_variants:
            if not records:
                raise ValueError("Kār Nāṟpatu leading variant without previous record")
            records[-1]["source_note_lines"].extend(leading_variants)
        if len(segment) < 4:
            raise ValueError(f"Kār Nāṟpatu record {printed} has fewer than four literary lines")
        context, body = segment[:-4], segment[-4:]
        sequence = len(records) + 1
        records.append({"poem_number": sequence, "poem_number_as_printed": printed,
                        "source_order": sequence, "lines": body,
                        "source_note_lines": context, "status": "source-transcribed",
                        "section": "001-040"})
        segment = []
    if segment:
        trailing = []
        while segment and re.match(r"^[@%&ஃ]", segment[0]):
            trailing.append(segment.pop(0))
        if trailing:
            records[-1]["source_note_lines"].extend(trailing)
        if segment:
            raise ValueError(f"Unparsed Kār Nāṟpatu tail: {segment}")
    if len(records) != 40:
        raise ValueError(f"Expected 40 Kār Nāṟpatu records; found {len(records)}")
    return {"parser": WORK_SPECS["kar-narpathu"]["parser"], "work_slug": "kar-narpathu",
            "title_tamil_as_printed": 'மதுரைக் கண்ணங்கூத்தனார் அருளிய "கார் நாற்பது"',
            "poems": records,
            "sections": [{"sequence": 1, "heading_as_printed": None,
                          "poem_start": 1, "poem_end": 40, "record_count": 40,
                          "provenance": "mechanical whole-work navigation; no internal division printed"}],
            "numbering_anomalies": [], "heading_anomalies": [],
            "unparsed_fragments": []}


def parse_kalavazhi_narpathu(raw: bytes) -> dict:
    lines=_visible_lines(raw)
    start=lines.index("3.  களவழி நாற்பது - பொய்கையார் இயற்றியது")
    end=lines.index("களவழி நாற்பது முற்றிற்று")
    source=lines[start+2:end];records=[];segment=[]
    for line in source:
        segment.append(line)
        marker=re.search(r"(\d{1,2})\s*$",line)
        if not marker:continue
        printed=int(marker.group(1));segment[-1]=line[:marker.start()].replace("\u00a0","").rstrip()
        leading=[]
        while segment and re.match(r"^[@%&ஃ]",segment[0]):leading.append(segment.pop(0))
        if leading:
            if not records:raise ValueError("Kaḷavaḻi leading variant without prior record")
            records[-1]["source_note_lines"].extend(leading)
        sequence=len(records)+1
        records.append({"poem_number":sequence,"poem_number_as_printed":printed,"source_order":sequence,
          "lines":segment,"source_note_lines":[],"status":"source-transcribed","section":"001-040"})
        segment=[]
    trailing_variants=[]
    while segment and re.match(r"^[@%&ஃ]",segment[0]):trailing_variants.append(segment.pop(0))
    if trailing_variants:records[-1]["source_note_lines"].extend(trailing_variants)
    if len(records)!=40:raise ValueError(f"Expected 40 printed numbered Kaḷavaḻi records; found {len(records)}")
    if not segment:raise ValueError("Expected source-printed unnumbered concluding literary text")
    return {"parser":WORK_SPECS["kalavazhi-narpathu"]["parser"],"work_slug":"kalavazhi-narpathu",
      "title_tamil_as_printed":"களவழி நாற்பது - பொய்கையார் இயற்றியது","poems":records,
      "additional_unnumbered_literary_text":{"position":"after numbered record 40","lines":segment,
        "provenance":"printed by Project Madurai without a number; not inferred as record 41"},
      "sections":[{"sequence":1,"heading_as_printed":None,"poem_start":1,"poem_end":40,"record_count":40,
        "provenance":"mechanical whole-work navigation; no internal division printed"}],
      "numbering_anomalies":[],"heading_anomalies":[],"unparsed_fragments":[]}


def parse_aintinai_aimpathu(raw: bytes) -> dict:
    lines=_visible_lines(raw)
    start=lines.index("பாயிரம்",lines.index("1. மாறன் பொறையனார்  அருளிய ஐந்திணை ஐம்பது"))
    end=lines.index("ஐந்திணை ஐம்பது முற்றிற்று")
    division_map={"முல்லை":"முல்லை","2.     குறிஞ்சி":"குறிஞ்சி","3.  மருதம்":"மருதம்","4.  பாலை":"பாலை","5.  நெய்தல்":"நெய்தல்"}
    division_lines=[i for i in range(start,end) if lines[i] in division_map]
    preface={"heading_as_printed":"பாயிரம்","lines":lines[start+1:division_lines[0]],"source_note_lines":[],
      "provenance":"Project Madurai printed unnumbered literary text"}
    records=[];divisions=[]
    for seq,di in enumerate(division_lines,1):
        dend=division_lines[seq] if seq<len(division_lines) else end
        printed=lines[di];thinai=division_map[printed]
        segment=lines[di+1:dend];first_marker=next(i for i,x in enumerate(segment) if re.search(r"\d{1,2}\s*$",x))
        description=segment[:max(0,first_marker-3)]
        # Determine the literary start from the first four-line record.
        literary_start=first_marker-3
        description=segment[:literary_start]
        verse_lines=segment[literary_start:];buf=[];members=[]
        for line in verse_lines:
            buf.append(line);m=re.search(r"(\d{1,2})\.?\s*$",line)
            if not m:continue
            printed_num=int(m.group(1));buf[-1]=line[:m.start()].replace("\u00a0","").rstrip()
            n=len(records)+1
            rec={"poem_number":n,"poem_number_as_printed":printed_num,"source_order":n,"lines":buf,
              "source_note_lines":[],"status":"source-transcribed","thinai":thinai,
              "thinai_as_printed":printed,"division_sequence":seq,"position_within_division":len(members)+1}
            records.append(rec);members.append(rec);buf=[]
        if buf:raise ValueError(f"Residual Aintiṇai Aimpathu lines in {printed}: {buf}")
        divisions.append({"sequence":seq,"heading_as_printed":printed,"thinai":thinai,
          "description_as_printed":description,"poem_start":members[0]["poem_number"],"poem_end":members[-1]["poem_number"],
          "record_count":len(members),"provenance":"Project Madurai printed division"})
    if len(records)!=50 or any(x["record_count"]!=10 for x in divisions):
        raise ValueError(f"Aintiṇai Aimpathu structure mismatch: {len(records)} records; {[x['record_count'] for x in divisions]}")
    return {"parser":WORK_SPECS["aintinai-aimpathu"]["parser"],"work_slug":"aintinai-aimpathu",
      "title_tamil_as_printed":"மாறன் பொறையனார் அருளிய ஐந்திணை ஐம்பது","prefatory_text":preface,
      "poems":records,"sections":divisions,"numbering_anomalies":[],"heading_anomalies":[],
      "unparsed_fragments":[]}


def parse_aintinai_elupathu(raw: bytes) -> dict:
    lines=_visible_lines(raw);heading="2. மூவாதியார் அருளிய ஐந்திணை எழுபது"
    start=lines.index("கடவுள் வாழ்த்து",lines.index(heading));end=lines.index("ஐந்திணை எழுபது முற்றிற்று")
    tins=["குறிஞ்சி","முல்லை","பாலை","மருதம்","நெய்தல்"];indices=[lines.index(x,start,end) for x in tins]
    pref={"heading_as_printed":"கடவுள் வாழ்த்து","lines":lines[start+1:indices[0]],"source_note_lines":[],
      "provenance":"Project Madurai printed unnumbered literary text"}
    records=[];divisions=[]
    for seq,(thinai,di) in enumerate(zip(tins,indices),1):
        dend=indices[seq] if seq<len(indices) else end
        segment=lines[di+1:dend];buf=[];members=[]
        for line in segment:
            loss=re.match(r"^(\d{1,2}),\s*(\d{1,2}).*மறைந்த",line)
            if loss:
                if buf:raise ValueError(f"Literary buffer before loss statement: {buf}")
                for n in range(int(loss.group(1)),int(loss.group(2))+1):
                    rec={"poem_number":n,"poem_number_as_printed":n,"source_order":n,"lines":[],
                      "source_note_lines":[line],"status":"source-missing","thinai":thinai,"thinai_as_printed":thinai,
                      "division_sequence":seq,"position_within_division":n-(seq-1)*14}
                    records.append(rec);members.append(rec)
                continue
            buf.append(line);m=re.search(r"(\d{1,2})\.?\s*$",line)
            if not m:continue
            printed=int(m.group(1));buf[-1]=line[:m.start()].replace("\u00a0","").rstrip();n=len(records)+1
            rec={"poem_number":n,"poem_number_as_printed":printed,"source_order":n,"lines":buf,
              "source_note_lines":[],"status":"source-transcribed","thinai":thinai,"thinai_as_printed":thinai,
              "division_sequence":seq,"position_within_division":len(members)+1}
            records.append(rec);members.append(rec);buf=[]
        if buf:raise ValueError(f"Residual Aintiṇai Eḻupathu lines: {buf}")
        divisions.append({"sequence":seq,"heading_as_printed":thinai,"thinai":thinai,
          "poem_start":(seq-1)*14+1,"poem_end":seq*14,"record_count":len(members),
          "lost_poems":[x["poem_number"] for x in members if not x["lines"]],
          "provenance":"Project Madurai printed division"})
    if len(records)!=70 or any(x["record_count"]!=14 for x in divisions):
        raise ValueError(f"Aintiṇai Eḻupathu structure mismatch: {len(records)}")
    return {"parser":WORK_SPECS["aintinai-elupathu"]["parser"],"work_slug":"aintinai-elupathu",
      "title_tamil_as_printed":heading,"prefatory_text":pref,"poems":records,"sections":divisions,
      "source_lost_poems":[25,26,69,70],"numbering_anomalies":[],"heading_anomalies":[],"unparsed_fragments":[]}


def parse_thinaimalai_nutraimbathu(raw: bytes) -> dict:
    lines=_visible_lines(raw);start=lines.index("1. குறிஞ்சி");end=lines.index("திணைமாலை நூற்றைம்பது முற்றிற்று")
    printed=["1. குறிஞ்சி","2. நெய்தல்","3. பாலை","4. முல்லை","5. மருதம்"];tins=["குறிஞ்சி","நெய்தல்","பாலை","முல்லை","மருதம்"]
    indices=[lines.index(x,start,end) for x in printed];closing_payeram=lines.index("சிறப்புப் பாயிரம்",indices[-1],end)
    records=[];divisions=[]
    for seq,(head,thinai,di) in enumerate(zip(printed,tins,indices),1):
        dend=indices[seq] if seq<len(indices) else closing_payeram;segment=lines[di+1:dend]
        description=segment[:2];buf=[];members=[]
        for line in segment[2:]:
            if re.fullmatch(r"-+", line):
                continue
            buf.append(line);m=re.search(r"\((\d{1,3})\)\s*$",line)
            if not m:continue
            printed_num=int(m.group(1));buf[-1]=line[:m.start()].replace("\u00a0","").rstrip();n=len(records)+1
            rec={"poem_number":n,"poem_number_as_printed":printed_num,"source_order":n,"lines":buf,
              "source_note_lines":[],"status":"source-transcribed","thinai":thinai,"thinai_as_printed":head,
              "division_sequence":seq,"position_within_division":len(members)+1}
            records.append(rec);members.append(rec);buf=[]
        if buf:raise ValueError(f"Residual Tiṇaimālai lines in {head}: {buf}")
        divisions.append({"sequence":seq,"heading_as_printed":head,"thinai":thinai,
          "description_as_printed":description,"poem_start":members[0]["poem_number"],"poem_end":members[-1]["poem_number"],
          "record_count":len(members),"provenance":"Project Madurai printed division"})
    if len(records)!=153:raise ValueError(f"Expected 153 printed records; found {len(records)}")
    return {"parser":WORK_SPECS["thinaimalai-nutraimbathu"]["parser"],"work_slug":"thinaimalai-nutraimbathu",
      "title_tamil_as_printed":"திணைமாலை  நூற்றைம்பது","poems":records,"sections":divisions,
      "additional_unnumbered_literary_text":{"heading_as_printed":"சிறப்புப் பாயிரம்",
        "position":"after numbered record 153","lines":lines[closing_payeram+1:end],
        "provenance":"Project Madurai printed unnumbered literary text"},
      "numbering_anomalies":[],"heading_anomalies":[],"unparsed_fragments":[]}


def _terminal_number_work(raw, work, start_text, end_text, divisions=(), prefatory=()):
    """Parse sources whose record number is a terminal layout marker."""
    all_lines=_visible_lines(raw); start=all_lines.index(start_text); end=all_lines.index(end_text,start)
    lines=all_lines[start+1:end]; records=[]; buf=[]; current=None; sections=[]
    divmap={h:(i+1,h) for i,h in enumerate(divisions)}
    pref=[]; pref_heading=None
    for line in lines:
        if line in divmap:
            current=divmap[line]
            sections.append({"sequence":current[0],"heading_as_printed":line,
                             "poem_start":len(records)+1,"provenance":"Project Madurai printed division"})
            continue
        if line in prefatory:
            pref_heading=line; continue
        m=re.search(r"(?<!\d)(\d+)\s*$",line)
        if m and int(m.group(1))==len(records)+1:
            clean=line[:m.start()].replace("\u00a0","").rstrip()
            if clean: buf.append(clean)
            n=int(m.group(1))
            records.append({"poem_number":n,"poem_number_as_printed":n,"source_order":n,
              "lines":buf,"source_note_lines":[],"status":"source-transcribed",
              "division_sequence":current[0] if current else None,
              "division_as_printed":current[1] if current else None})
            buf=[]
        elif not records and pref_heading:
            pref.append(line)
        elif line not in {"நூல்","--------------------------","-----------","----","-"}:
            buf.append(line)
    for sec in sections:
        members=[r for r in records if r["division_sequence"]==sec["sequence"]]
        sec.update({"poem_end":members[-1]["poem_number"],"record_count":len(members)})
    return {"parser":spec(work)["parser"],"work_slug":work,
      "title_tamil_as_printed":start_text,"poems":records,"sections":sections,
      "prefatory_text":{"heading_as_printed":pref_heading,"lines":pref} if pref_heading else None,
      "numbering_anomalies":[],"heading_anomalies":[],"unparsed_fragments":[]}


def parse_thinaimozhi_aimpathu(raw):
    return _terminal_number_work(raw,"thinaimozhi-aimpathu",
      "கண்ணன் சேந்தனார் இயற்றிய திணை மொழி ஐம்பது","திணை மொழி ஐம்பது முற்றிற்று",
      ("1.  குறிஞ்சி","2,  பாலை","3.  முல்லை","4.   மருதம்","5.  நெய்தல்"))


def parse_elati(raw):
    lines=_visible_lines(raw); start=lines.index('2. கணிமேதையார் அருளிய  "ஏலாதி"')
    end=lines.index("ஏலாதி முற்றிற்று",start)
    literary_start=lines.index("சென்ற புகழ்செல்வம் மீக்கூற்றம் சேவகம்",start)
    d=_terminal_number_work(raw,"elati",lines[literary_start-1],"ஏலாதி முற்றிற்று")
    d["title_tamil_as_printed"]=lines[start]
    d["prefatory_text"]={"heading_as_printed":"சிறப்புப் பாயிரம் / கடவுள் வணக்கம்",
                         "lines":lines[start+2:literary_start]}
    return d


def parse_sirupanchamulam(raw):
    return _terminal_number_work(raw,"sirupanchamulam",'3. காரியாசான்  அருளிய  "சிறு பஞ்ச மூலம்"',
      "சிறுபஞ்சமூலம் முற்றிற்று",(),("கடவுள் வாழ்த்து",))


def _heading_record_work(raw,work,start_text,end_text,heading_re,prefatory=()):
    all_lines=_visible_lines(raw); start=all_lines.index(start_text); end=all_lines.index(end_text,start)
    records=[]; current=None; pref=[]; pref_heading=None
    for line in all_lines[start+1:end]:
        m=re.match(heading_re,line)
        if m:
            if current: records.append(current)
            n=int(m.group(1)); current={"poem_number":n,"poem_number_as_printed":n,
              "source_order":len(records)+1,"heading_as_printed":line,
              "record_title_as_printed":m.group(2).strip(),"lines":[],"source_note_lines":[],
              "status":"source-transcribed"}
        elif line in prefatory and current is None: pref_heading=line
        elif current is not None:
            if line.startswith("(") and line.endswith(")"):
                current["source_note_lines"].append(line)
            else: current["lines"].append(line)
        elif pref_heading: pref.append(line)
    if current: records.append(current)
    anomalies=[{"poem_number":r["poem_number"],"heading_as_printed":r["heading_as_printed"]}
               for r in records if not re.match(rf"^{r['poem_number']}\.\s",r["heading_as_printed"])]
    return {"parser":spec(work)["parser"],"work_slug":work,"title_tamil_as_printed":start_text,
      "poems":records,"sections":[],"prefatory_text":{"heading_as_printed":pref_heading,"lines":pref} if pref_heading else None,
      "numbering_anomalies":[],"heading_anomalies":anomalies,"unparsed_fragments":[]}


def parse_tirikatukam(raw):
    lines=_visible_lines(raw); start=max(i for i,x in enumerate(lines) if x=="நல்லாதனாரின் திரிகடுகம்")
    end=lines.index("திரிகடுகம் முற்றிற்று.",start); inv=lines[start+2:start+6]
    verse=[]; titles={}
    for line in lines[start+6:end]:
        m=re.match(r"^(\d+)\.\s+(.+)$",line)
        if m: titles[int(m.group(1))]=line
        else: verse.append(line)
    records=[]
    for i in range(100):
        n=i+1; records.append({"poem_number":n,"poem_number_as_printed":n if n in titles else None,
          "source_order":n,"heading_as_printed":titles.get(n),"record_title_as_printed":
          re.sub(r"^\d+\.\s+","",titles[n]) if n in titles else None,
          "lines":verse[i*4:(i+1)*4],"source_note_lines":[],"status":"source-transcribed"})
    return {"parser":spec("tirikatukam")["parser"],"work_slug":"tirikatukam",
      "title_tamil_as_printed":lines[start],"poems":records,"sections":[],
      "prefatory_text":{"heading_as_printed":"காப்பு","lines":inv},
      "numbering_anomalies":[],"heading_anomalies":[{"poem_start":n,"type":"printed_record_heading_absent"} for n in (43,57)],
      "unparsed_fragments":[]}


def parse_acharakkovai(raw):
    lines=_visible_lines(raw); start=lines.index('பெருவாயின் முள்ளியாரின்  "ஆசாரக்கோவை"')
    end=lines.index("ஆசாரக் கோவை முற்றிற்று",start); titles={}; records=[]; pending=None
    for line in lines[start+1:end]:
        m=re.match(r"^(\d+)[.,]+\s*(.+)$",line)
        if m: titles[int(m.group(1))]=line; pending=(int(m.group(1)),line); continue
        if line.startswith("(") and line.endswith(")"):
            if pending is None and not records:
                continue
            n=(pending[0] if pending else len(records)+1)
            records.append({"poem_number":n,"poem_number_as_printed":n if pending else None,
              "source_order":n,"heading_as_printed":pending[1] if pending else None,
              "record_title_as_printed":re.sub(r"^\d+[.,]+\s*","",pending[1]) if pending else None,
              "lines":[],"source_note_lines":[line],"status":"source-transcribed"}); pending=None
        elif records: records[-1]["lines"].append(line)
    return {"parser":spec("acharakkovai")["parser"],"work_slug":"acharakkovai",
      "title_tamil_as_printed":lines[start],"poems":records,"sections":[],
      "numbering_anomalies":[],"heading_anomalies":[{"poem_start":47,"type":"printed_record_heading_absent"},
        {"poem_start":6,"type":"printed_heading_punctuation","as_printed":"6.."},
        {"poem_start":64,"type":"printed_heading_punctuation","as_printed":"64,"},
        {"poem_start":97,"type":"printed_heading_punctuation","as_printed":"97,"}],"unparsed_fragments":[]}


def parse_muthumozhi_kanchi(raw):
    lines=_visible_lines(raw); start=lines.index("4.  முதுமொழிக் காஞ்சி :மதுரைக் கூடலூர் கிழார் அருளியது")
    end=lines.index("முதுமொழிக்காஞ்சி முற்றிற்று",start); records=[]; sections=[]; current=None
    for line in lines[start+1:end]:
        sm=re.match(r"^(\d+)\.\s+(.+பத்து)$",line)
        if sm and int(sm.group(1))<=10:
            current=(int(sm.group(1)),line); sections.append({"sequence":current[0],"heading_as_printed":line,
              "poem_start":len(records)+1,"provenance":"Project Madurai printed பத்து"}); continue
        m=re.match(r"^(\d+)\.\s*(.*)$",line)
        if m:
            n=int(m.group(1)); text=m.group(2).strip()
            records.append({"poem_number":n,"poem_number_as_printed":n,"source_order":n,
              "lines":[text] if text else [],"source_note_lines":[],"status":"source-transcribed",
              "division_sequence":current[0],"division_as_printed":current[1]})
        else: records[-1]["lines"].append(line)
    for sec in sections:
        ms=[r for r in records if r["division_sequence"]==sec["sequence"]]
        sec.update({"poem_end":ms[-1]["poem_number"],"record_count":len(ms)})
    return {"parser":spec("muthumozhi-kanchi")["parser"],"work_slug":"muthumozhi-kanchi",
      "title_tamil_as_printed":lines[start],"poems":records,"sections":sections,
      "numbering_anomalies":[],"heading_anomalies":[],"unparsed_fragments":[]}


def parse_pazhamozhi_nanuru(raw):
    lines=_visible_lines(raw); start=lines.index("பழமொழி நானூறு - ஆசிரியர்  மூன்றுறை அரையனார்")
    end=lines.index("பழமொழி நானூறு முற்றிற்று",start); records=[]; current=None; chapters=[]; pre=[]
    for line in lines[start+1:end]:
        cm=re.match(r"^(\d+)\.\s+(.+)$",line)
        rm=re.match(r"^(\d+)\.$",line) or re.match(r"^(\d+)$",line)
        if cm:
            chapters.append({"sequence":int(cm.group(1)),"heading_as_printed":line,
              "poem_start":(current["poem_number"]+1 if current else 1),
              "provenance":"Project Madurai printed chapter"}); continue
        expected_number=(current["poem_number"]+1 if current else 1)
        if rm and int(rm.group(1))==expected_number:
            if current: records.append(current)
            n=int(rm.group(1)); current={"poem_number":n,"poem_number_as_printed":n,
              "source_order":n,"lines":[],"source_note_lines":[],"status":"source-transcribed",
              "division_sequence":chapters[-1]["sequence"] if chapters else None,
              "division_as_printed":chapters[-1]["heading_as_printed"] if chapters else None}
        elif current: current["lines"].append(line)
        else: pre.append(line)
    if current: records.append(current)
    for i,sec in enumerate(chapters):
        ms=[r for r in records if r["division_sequence"]==sec["sequence"]]
        sec.update({"poem_end":ms[-1]["poem_number"],"record_count":len(ms)})
    return {"parser":spec("pazhamozhi-nanuru")["parser"],"work_slug":"pazhamozhi-nanuru",
      "title_tamil_as_printed":lines[start],"poems":records,"sections":chapters,
      "prefatory_text":{"heading_as_printed":"தற்சிறப்புப் பாயிரம் / கடவுள் வணக்கம்","lines":pre},
      "numbering_anomalies":[],"heading_anomalies":[{"poem_start":None,"type":"printed_chapter_12_heading_absent"}],
      "unparsed_fragments":[]}


def parse_kainnilai(raw):
    lines=_visible_lines(raw); start=lines.index("2.  புல்லங்காடனாரின் கைந்நிலை")
    end=lines.index("கைந்நிலை முற்றிற்று.",start); records=[]; current=None; sections=[]
    for line in lines[start+1:end]:
        dm=re.match(r"^(\d+)\.\s+([^0-9].+)$",line)
        if dm and int(dm.group(1))<=5:
            current_div=(int(dm.group(1)),line); sections.append({"sequence":current_div[0],"heading_as_printed":line,
              "poem_start":(current["poem_number"]+1 if current else 1),
              "provenance":"Project Madurai printed tiṇai division"}); continue
        rm=re.match(r"^(\d+)\.$",line)
        if rm:
            if current: records.append(current)
            n=int(rm.group(1)); current={"poem_number":n,"poem_number_as_printed":n,"source_order":n,
              "lines":[],"source_note_lines":[],"status":"source-transcribed",
              "division_sequence":current_div[0],"division_as_printed":current_div[1]}
        elif current:
            if line.startswith("(துறை"): current["source_note_lines"].append(line)
            elif line not in {"-"}: current["lines"].append(line)
    if current: records.append(current)
    for sec in sections:
        ms=[r for r in records if r["division_sequence"]==sec["sequence"]]
        sec.update({"poem_end":ms[-1]["poem_number"],"record_count":len(ms)})
    return {"parser":spec("kainnilai")["parser"],"work_slug":"kainnilai","title_tamil_as_printed":lines[start],
      "poems":records,"sections":sections,"numbering_anomalies":[],"heading_anomalies":[],
      "unparsed_fragments":[]}


PARSERS = {"tirukkural": parse_tirukkural, "naladiyar": parse_naladiyar,
           "nanmanikkadigai": parse_nanmanikkadigai,
           "inna-narpathu": parse_inna_narpathu,
           "iniyavai-narpathu": parse_iniyavai_narpathu,
           "kar-narpathu": parse_kar_narpathu,
           "kalavazhi-narpathu": parse_kalavazhi_narpathu,
           "aintinai-aimpathu": parse_aintinai_aimpathu,
           "aintinai-elupathu": parse_aintinai_elupathu,
           "thinaimalai-nutraimbathu": parse_thinaimalai_nutraimbathu,
           "thinaimozhi-aimpathu":parse_thinaimozhi_aimpathu,
           "tirikatukam":parse_tirikatukam,"acharakkovai":parse_acharakkovai,
           "pazhamozhi-nanuru":parse_pazhamozhi_nanuru,
           "sirupanchamulam":parse_sirupanchamulam,
           "muthumozhi-kanchi":parse_muthumozhi_kanchi,
           "elati":parse_elati,"kainnilai":parse_kainnilai}


def extract(work: str, force=True, dry_run=False, verbose=False):
    s = spec(work)
    p = work_paths(work)
    raw = p["raw"].read_bytes()
    digest = hashlib.sha256(raw).hexdigest()
    if digest != s["source_sha256"]:
        raise ValueError(f"{work} raw checksum mismatch: {digest}")
    parsed = PARSERS[work](raw)
    if dry_run:
        print(f"Would extract {len(parsed['poems'])} records from {len(raw)} bytes")
        return
    write_text(p["raw_txt"], BeautifulSoup(raw.decode("utf-8-sig"), "lxml").get_text("\n"), force=force)
    write_json(p["parsed"], parsed, force=force)
    meta = {
        "work": work,
        "programme_id": "pathinenkilkanakku",
        "project_madurai_id": s["project_madurai_id"],
        "source_url": s["source_url"],
        "source_file": s["source_file"],
        "source_artifact_type": "exact HTTP HTML response",
        "source_bytes": len(raw),
        "source_checksum_sha256": digest,
        "retrieval_date": "2026-07-29",
        "title_tamil_as_printed": parsed["title_tamil_as_printed"],
        "parser": parsed["parser"],
        "numbered_record_count": len(parsed["poems"]),
    }
    write_json(p["source_metadata"], meta, force=force)
    recon = {
        **meta,
        "source_only": True,
        "commentary_present": False,
        "number_range": [1, s["expected_records"]],
        "printed_numbered_record_count": s["expected_records"],
        "missing_canonical_numbers": [],
        "duplicate_canonical_numbers": [],
        "printed_numbering_anomalies": parsed["numbering_anomalies"],
        "source_printed_major_divisions": (
            ["1.  அறத்துப்பால்", "2.      பொருட்பால்", "3.      காமத்துப்பால்"]
            if work == "tirukkural" else
            ["1. அறத்துப்பால்", "2. பொருட்பால்", "3. காமத்துப்பால்"]
            if work == "naladiyar" else
            [x["heading_as_printed"] for x in parsed.get("sections", [])]),
        "source_printed_chapter_count": sum(bool(x["heading_as_printed"]) for x in parsed.get("chapters", [])),
        "canonical_chapter_count": len(parsed.get("chapters", [])),
        "heading_anomalies": parsed["heading_anomalies"],
        "unnumbered_literary_invocation_present": bool(parsed.get("prefatory_text")),
        "source_lost_records": parsed.get("source_lost_poems", []),
        "incomplete_records": [],
        "candidate_texts": [],
        "line_end_markers": ("Printed global couplet numbers are excluded as HTML layout markers and retained in poem_number_as_printed."
                             if work == "tirukkural" else "Numbers are printed at the start of each first literary line and removed only as record labels."),
        "html_anomalies": (["Malformed/unbalanced table-row markup", "Some literary couplets wrap to three visible lines"]
                           if work == "tirukkural" else []),
        "provenance_classification": {
            "major_divisions": "printed by selected canonical source",
            "subdivisions": "printed by selected canonical source where present",
            "chapter_headings": "printed where present",
            "canonical_sequence": "mechanically derived from source order",
            "literary_text": "printed by selected canonical source"
        }
    }
    write_json(p["reconnaissance"], recon, force=force)
    if verbose:
        print(f"Extracted {len(parsed['poems'])} Tirukkural couplets")


def normalize(work: str, force=True, dry_run=False, verbose=False):
    p = work_paths(work)
    data = json.loads(p["parsed"].read_text(encoding="utf-8"))
    for record in data["poems"]:
        record["lines"] = [unicodedata.normalize("NFC", x.replace("\r", "").strip())
                           for x in record["lines"]]
        record["source_note_lines"] = [
            unicodedata.normalize("NFC", x.replace("\r", "").strip())
            for x in record.get("source_note_lines", [])
        ]
    data["normalization"] = "Unicode NFC; LF line endings; duplicate blank lines removed"
    if dry_run:
        print(f"Would normalize {len(data['poems'])} records")
        return
    write_json(p["normalized"], data, force=force)
    if verbose:
        print("Applied conservative normalization")


def _tirukkural_markdown(record: dict, frozen=False) -> str:
    s = spec("tirukkural")
    n = record["poem_number"]
    chapter = record["chapter_sequence"]
    fm = {
        "schema_version": "1.0.0",
        "work": "திருக்குறள்",
        "work_english": "Tirukkural",
        "work_id": "tirukkural",
        "work_slug": "tirukkural",
        "programme_id": "pathinenkilkanakku",
        "record_type": "couplet",
        "poem_number": n,
        "poem_number_as_printed": record["poem_number_as_printed"],
        "poem_number_source": "Project Madurai printed line-end marker",
        "source_order": record["source_order"],
        "section": f"{chapter:03d}-{(chapter-1)*10+1:04d}-{chapter*10:04d}",
        "section_source": "Project Madurai chapter structure; chapter 116 heading absent",
        "major_division": record["major_division_as_printed"],
        "major_division_as_printed": record["major_division_as_printed"],
        "major_division_source": "Project Madurai printed heading",
        "subdivision_as_printed": record["subdivision_as_printed"],
        "subdivision_source": "Project Madurai printed heading",
        "chapter_sequence": chapter,
        "chapter_heading_as_printed": record["chapter_heading_as_printed"],
        "chapter_heading_source": ("Project Madurai printed heading"
                                   if record["chapter_heading_as_printed"] else None),
        "position_within_chapter": record["position_within_chapter"],
        "thinai": None, "thinai_source": None,
        "speaker": None, "speaker_source": None,
        "poet": None, "poet_source": None,
        "first_line": record["lines"][0],
        "line_count": len(record["lines"]),
        "textual_status": "complete",
        "canonical_text_available": True,
        "candidate_texts_available": False,
        "lacuna_present": False,
        "lacuna_location": None,
        "source_note_available": False,
        "source_note_source": None,
        "extraction_status": "success",
        "source": "Project Madurai",
        "source_url": s["source_url"],
        "project_madurai_id": s["project_madurai_id"],
        "source_object_id": s["project_madurai_id"],
        "source_file": s["source_file"],
        "language": "Tamil", "script": "Tamil",
        "status": "source-transcribed",
        "editorial_changes": False,
    }
    y = yaml.safe_dump(fm, allow_unicode=True, sort_keys=False,
                       default_flow_style=False).strip()
    return f"---\n{y}\n---\n\n# திருக்குறள் {n}\n\n" + "\n".join(record["lines"]) + "\n"


def _naladiyar_markdown(record: dict) -> str:
    s = spec("naladiyar")
    n = record["poem_number"]
    chapter = record["chapter_sequence"]
    fm = {
        "schema_version": "1.0.0", "work": "நாலடியார்",
        "work_english": "Nālāṭiyār", "work_id": "naladiyar",
        "work_slug": "naladiyar", "programme_id": "pathinenkilkanakku",
        "record_type": "quatrain", "poem_number": n,
        "poem_number_as_printed": record["poem_number_as_printed"],
        "poem_number_source": "Project Madurai printed record label",
        "source_order": record["source_order"],
        "section": f"{chapter:03d}-{(chapter-1)*10+1:03d}-{chapter*10:03d}",
        "section_source": "Project Madurai printed chapter",
        "major_division": record["major_division_as_printed"],
        "major_division_as_printed": record["major_division_as_printed"],
        "major_division_source": "Project Madurai printed heading",
        "chapter_sequence": chapter,
        "chapter_heading_as_printed": record["chapter_heading_as_printed"],
        "chapter_heading_source": "Project Madurai printed heading",
        "position_within_chapter": record["position_within_chapter"],
        "thinai": None, "thinai_source": None, "speaker": None,
        "speaker_source": None, "poet": None, "poet_source": None,
        "first_line": record["lines"][0], "line_count": len(record["lines"]),
        "textual_status": "complete", "canonical_text_available": True,
        "candidate_texts_available": False, "lacuna_present": False,
        "lacuna_location": None, "source_note_available": False,
        "source_note_source": None, "extraction_status": "success",
        "source": "Project Madurai", "source_url": s["source_url"],
        "project_madurai_id": s["project_madurai_id"],
        "source_object_id": s["project_madurai_id"],
        "source_file": s["source_file"], "language": "Tamil",
        "script": "Tamil", "status": "source-transcribed",
        "editorial_changes": False,
    }
    y = yaml.safe_dump(fm, allow_unicode=True, sort_keys=False,
                       default_flow_style=False).strip()
    return f"---\n{y}\n---\n\n# நாலடியார் {n}\n\n" + "\n".join(record["lines"]) + "\n"


def _split_naladiyar(work, p, data, frozen, verbose):
    records = data["poems"]
    expected_poems = {f"{n:03d}.md" for n in range(1, 401)}
    expected_sections = {
        f"{c:03d}-{(c-1)*10+1:03d}-{c*10:03d}.md" for c in range(1, 41)}
    p["poems"].mkdir(parents=True, exist_ok=True)
    p["sections"].mkdir(parents=True, exist_ok=True)
    bad = [x for x in p["poems"].rglob("*") if x.is_file() and
           (x.parent != p["poems"] or x.name not in expected_poems)]
    bad += [x for x in p["sections"].rglob("*") if x.is_file() and
            (x.parent != p["sections"] or x.name not in expected_sections)]
    if bad:
        raise RuntimeError(f"Refusing regeneration with unexpected physical files: {bad}")
    for record in records:
        (p["poems"] / f"{record['poem_number']:03d}.md").write_text(
            _naladiyar_markdown(record), encoding="utf-8", newline="\n")
    pref = data["prefatory_text"]
    full = ["# நாலடியார் — Project Madurai source transcription\n",
            f"## {pref['heading_as_printed']}\n\n" + "\n".join(pref["lines"]) + "\n"]
    for chapter in data["chapters"]:
        full.append(f"## {chapter['heading_as_printed']}\n")
        selected = [x for x in records if x["chapter_sequence"] == chapter["sequence"]]
        full.extend(_naladiyar_markdown(x).split("---\n", 2)[-1].lstrip()
                    for x in selected)
        content = [f"# {chapter['heading_as_printed']}\n",
                   "Project Madurai source-printed chapter.\n"]
        content.extend(_naladiyar_markdown(x).split("---\n", 2)[-1].lstrip()
                       for x in selected)
        filename = f"{chapter['sequence']:03d}-{chapter['poem_start']:03d}-{chapter['poem_end']:03d}.md"
        (p["sections"] / filename).write_text("\n".join(content), encoding="utf-8", newline="\n")
    p["full_text"].write_text("\n".join(full), encoding="utf-8", newline="\n")
    write_json(p["structure"], {"major_divisions": [
        {"sequence": 1, "heading_as_printed": "1. அறத்துப்பால்", "poem_start": 1, "poem_end": 130},
        {"sequence": 2, "heading_as_printed": "2. பொருட்பால்", "poem_start": 131, "poem_end": 370},
        {"sequence": 3, "heading_as_printed": "3. காமத்துப்பால்", "poem_start": 371, "poem_end": 400}],
        "chapters": data["chapters"], "heading_anomalies": data["heading_anomalies"],
        "prefatory_text": data["prefatory_text"]}, force=True)
    sm = json.loads(p["source_metadata"].read_text(encoding="utf-8"))
    write_json(p["metadata"], {
        "corpus_schema_version": "1.0.0" if frozen else None,
        "version_status": "frozen" if frozen else "unfrozen",
        "title_tamil": "நாலடியார்", "title_english": "Nālāṭiyār",
        "work_slug": work, "work_id": work,
        "programme_id": "pathinenkilkanakku",
        "author": None, "author_as_printed": "பல ஆசிரியர்கள் / composed by several authors",
        "numbered_poem_record_count": 400, "available_poem_count": 400,
        "missing_poems": [], "unnumbered_literary_record_count": 1,
        "printed_major_division_count": 3, "chapter_count": 40,
        "source_name": "Project Madurai", "source_url": spec(work)["source_url"],
        "project_madurai_id": spec(work)["project_madurai_id"],
        "accessed_date": sm["retrieval_date"],
        "source_checksum_sha256": sm["source_checksum_sha256"],
        "encoding": "UTF-8", "normalization": "Unicode NFC",
        "notes": ["The unnumbered கடவுள் வாழ்த்து is preserved at work level.",
                  "The printed chapter heading 2.39 occurs under 3. காமத்துப்பால் and is not repaired."]
    }, force=True)
    if not (p["corpus"] / "README.md").exists():
        (p["corpus"] / "README.md").write_text(
            "# நாலடியார் (Nālāṭiyār)\n\nUnfrozen source-faithful onboarding from Project Madurai `pmuni0016`.\n",
            encoding="utf-8", newline="\n")
    if verbose:
        print("Wrote 400 quatrain files and 40 source chapter sections")


def _nanmanikkadigai_markdown(record: dict) -> str:
    s = spec("nanmanikkadigai")
    n = record["poem_number"]
    fm = {
        "schema_version": "1.0.0", "work": "நான்மணிக்கடிகை",
        "work_english": "Nāṉmaṇikkaṭigai", "work_id": "nanmanikkadigai",
        "work_slug": "nanmanikkadigai", "programme_id": "pathinenkilkanakku",
        "record_type": "verse", "poem_number": n,
        "poem_number_as_printed": record["poem_number_as_printed"],
        "poem_number_source": "Project Madurai printed line-end marker",
        "source_order": record["source_order"],
        "section": "01-invocation" if record["section_sequence"] == 1 else "02-nul",
        "section_as_printed": record["section_as_printed"],
        "section_source": "Project Madurai printed heading",
        "thinai": None, "thinai_source": None, "speaker": None,
        "speaker_source": None, "poet": None, "poet_source": None,
        "first_line": record["lines"][0], "line_count": len(record["lines"]),
        "textual_status": "complete", "canonical_text_available": True,
        "candidate_texts_available": False, "lacuna_present": False,
        "lacuna_location": None, "source_note_available": False,
        "source_note_source": None, "extraction_status": "success",
        "source": "Project Madurai", "source_url": s["source_url"],
        "project_madurai_id": s["project_madurai_id"],
        "source_object_id": s["project_madurai_id"],
        "source_file": s["source_file"], "language": "Tamil",
        "script": "Tamil", "status": "source-transcribed",
        "editorial_changes": False,
    }
    y = yaml.safe_dump(fm, allow_unicode=True, sort_keys=False).strip()
    return f"---\n{y}\n---\n\n# நான்மணிக்கடிகை {n}\n\n" + "\n".join(record["lines"]) + "\n"


def _split_nanmanikkadigai(work, p, data, frozen, verbose):
    records = data["poems"]
    expected_poems = {f"{n:03d}.md" for n in range(1, 107)}
    expected_sections = {"01-invocation.md", "02-nul.md"}
    p["poems"].mkdir(parents=True, exist_ok=True)
    p["sections"].mkdir(parents=True, exist_ok=True)
    bad = [x for x in p["poems"].rglob("*") if x.is_file() and
           (x.parent != p["poems"] or x.name not in expected_poems)]
    bad += [x for x in p["sections"].rglob("*") if x.is_file() and
            (x.parent != p["sections"] or x.name not in expected_sections)]
    if bad:
        raise RuntimeError(f"Refusing regeneration with unexpected physical files: {bad}")
    for record in records:
        (p["poems"] / f"{record['poem_number']:03d}.md").write_text(
            _nanmanikkadigai_markdown(record), encoding="utf-8", newline="\n")
    full = ["# நான்மணிக்கடிகை — Project Madurai source transcription\n"]
    for section in data["sections"]:
        selected = [x for x in records if x["section_sequence"] == section["sequence"]]
        full.append(f"## {section['heading_as_printed']}\n")
        full.extend(_nanmanikkadigai_markdown(x).split("---\n", 2)[-1].lstrip()
                    for x in selected)
        content = [f"# {section['heading_as_printed']}\n",
                   "Project Madurai source-printed division.\n"]
        content.extend(_nanmanikkadigai_markdown(x).split("---\n", 2)[-1].lstrip()
                       for x in selected)
        name = "01-invocation.md" if section["sequence"] == 1 else "02-nul.md"
        (p["sections"] / name).write_text("\n".join(content), encoding="utf-8", newline="\n")
    p["full_text"].write_text("\n".join(full), encoding="utf-8", newline="\n")
    write_json(p["structure"], {"sections": data["sections"]}, force=True)
    sm = json.loads(p["source_metadata"].read_text(encoding="utf-8"))
    write_json(p["metadata"], {
        "corpus_schema_version": "1.0.0" if frozen else None,
        "version_status": "frozen" if frozen else "unfrozen",
        "title_tamil": "நான்மணிக்கடிகை", "title_english": "Nāṉmaṇikkaṭigai",
        "work_slug": work, "work_id": work, "programme_id": "pathinenkilkanakku",
        "author": "விளம்பிநாகனார்", "author_as_printed": "விளம்பிநாகனார்",
        "numbered_poem_record_count": 106, "available_poem_count": 106,
        "missing_poems": [], "printed_section_count": 2,
        "source_name": "Project Madurai", "source_url": spec(work)["source_url"],
        "project_madurai_id": spec(work)["project_madurai_id"],
        "accessed_date": sm["retrieval_date"], "source_checksum_sha256": sm["source_checksum_sha256"],
        "encoding": "UTF-8", "normalization": "Unicode NFC",
        "notes": ["The source numbers the invocation as record 1 and continues through record 106.",
                  "கடவுள் வாழ்த்து and நூல் are preserved as source-printed divisions."]
    }, force=True)
    if not (p["corpus"] / "README.md").exists():
        (p["corpus"] / "README.md").write_text(
            "# நான்மணிக்கடிகை (Nāṉmaṇikkaṭigai)\n\nUnfrozen source-faithful onboarding from Project Madurai `pmuni0047`.\n",
            encoding="utf-8", newline="\n")
    if verbose:
        print("Wrote 106 verse files and 2 source-printed sections")


def _inna_markdown(record: dict) -> str:
    s = spec("inna-narpathu")
    n = record["poem_number"]
    fm = {
        "schema_version": "1.0.0", "work": "இன்னா நாற்பது",
        "work_english": "Iṉṉā Nāṟpatu", "work_id": "inna-narpathu",
        "work_slug": "inna-narpathu", "programme_id": "pathinenkilkanakku",
        "record_type": "verse", "poem_number": n,
        "poem_number_as_printed": record["poem_number_as_printed"],
        "poem_number_source": "Project Madurai printed line-end marker",
        "source_order": record["source_order"], "section": "02-nul",
        "section_as_printed": "நூல்", "section_source": "Project Madurai printed heading",
        "thinai": None, "thinai_source": None, "speaker": None,
        "speaker_source": None, "poet": None, "poet_source": None,
        "first_line": record["lines"][0], "line_count": len(record["lines"]),
        "textual_status": "complete", "canonical_text_available": True,
        "candidate_texts_available": bool(record["source_note_lines"]),
        "lacuna_present": False, "lacuna_location": None,
        "source_note_available": bool(record["source_note_lines"]),
        "source_note_source": ("Project Madurai printed பாட வேற்றுமை note"
                               if record["source_note_lines"] else None),
        "extraction_status": "success", "source": "Project Madurai",
        "source_url": s["source_url"], "project_madurai_id": s["project_madurai_id"],
        "source_object_id": s["project_madurai_id"], "source_file": s["source_file"],
        "language": "Tamil", "script": "Tamil", "status": "source-transcribed",
        "editorial_changes": False,
    }
    y = yaml.safe_dump(fm, allow_unicode=True, sort_keys=False).strip()
    out = f"---\n{y}\n---\n\n# இன்னா நாற்பது {n}\n\n" + "\n".join(record["lines"]) + "\n"
    if record["source_note_lines"]:
        out += "\n## Source note (as printed)\n\n" + "\n".join(record["source_note_lines"]) + "\n"
    return out


def _split_inna(work, p, data, frozen, verbose):
    records = data["poems"]
    expected_poems = {f"{n:03d}.md" for n in range(1, 41)}
    expected_sections = {"01-invocation.md", "02-nul.md"}
    p["poems"].mkdir(parents=True, exist_ok=True)
    p["sections"].mkdir(parents=True, exist_ok=True)
    bad = [x for x in p["poems"].rglob("*") if x.is_file() and
           (x.parent != p["poems"] or x.name not in expected_poems)]
    bad += [x for x in p["sections"].rglob("*") if x.is_file() and
            (x.parent != p["sections"] or x.name not in expected_sections)]
    if bad:
        raise RuntimeError(f"Refusing regeneration with unexpected physical files: {bad}")
    for record in records:
        (p["poems"] / f"{record['poem_number']:03d}.md").write_text(
            _inna_markdown(record), encoding="utf-8", newline="\n")
    pref = data["prefatory_text"]
    inv = (f"# {pref['heading_as_printed']}\n\n" + "\n".join(pref["lines"]) +
           "\n\n## Source note (as printed)\n\n" + "\n".join(pref["source_note_lines"]) + "\n")
    (p["sections"] / "01-invocation.md").write_text(inv, encoding="utf-8", newline="\n")
    body = ["# நூல்\n\nProject Madurai source-printed division.\n"]
    body.extend(_inna_markdown(x).split("---\n", 2)[-1].lstrip() for x in records)
    (p["sections"] / "02-nul.md").write_text("\n".join(body), encoding="utf-8", newline="\n")
    p["full_text"].write_text("# இன்னா நாற்பது — Project Madurai source transcription\n\n" +
                              inv + "\n" + "\n".join(body), encoding="utf-8", newline="\n")
    write_json(p["structure"], {"sections": data["sections"],
                                "prefatory_text": pref}, force=True)
    sm = json.loads(p["source_metadata"].read_text(encoding="utf-8"))
    write_json(p["metadata"], {
        "corpus_schema_version": "1.0.0" if frozen else None,
        "version_status": "frozen" if frozen else "unfrozen",
        "title_tamil": "இன்னா நாற்பது", "title_english": "Iṉṉā Nāṟpatu",
        "work_slug": work, "work_id": work, "programme_id": "pathinenkilkanakku",
        "author": "கபிலர்", "author_as_printed": "கபிலர்",
        "numbered_poem_record_count": 40, "available_poem_count": 40,
        "missing_poems": [], "unnumbered_literary_record_count": 1,
        "source_name": "Project Madurai", "source_url": spec(work)["source_url"],
        "project_madurai_id": spec(work)["project_madurai_id"],
        "source_scope": "First work bounded within combined Project Madurai object",
        "accessed_date": sm["retrieval_date"], "source_checksum_sha256": sm["source_checksum_sha256"],
        "encoding": "UTF-8", "normalization": "Unicode NFC",
        "notes": ["The unnumbered கடவுள் வாழ்த்து is preserved at work level.",
                  "Printed variant notes marked @, %, and & remain source notes and do not alter canonical bodies."]
    }, force=True)
    if not (p["corpus"] / "README.md").exists():
        (p["corpus"] / "README.md").write_text(
            "# இன்னா நாற்பது (Iṉṉā Nāṟpatu)\n\nUnfrozen source-faithful onboarding from the bounded first work in Project Madurai `pmuni0025`.\n",
            encoding="utf-8", newline="\n")
    if verbose:
        print("Wrote 40 verse files and 2 source-printed sections")


def _iniyavai_markdown(record: dict) -> str:
    s = spec("iniyavai-narpathu")
    n = record["poem_number"]
    fm = {
        "schema_version": "1.0.0", "work": "இனியவை நாற்பது",
        "work_english": "Iṉiyavai Nāṟpatu", "work_id": "iniyavai-narpathu",
        "work_slug": "iniyavai-narpathu", "programme_id": "pathinenkilkanakku",
        "record_type": "verse", "poem_number": n,
        "poem_number_as_printed": record["poem_number_as_printed"],
        "poem_number_source": "Project Madurai printed line-end marker",
        "source_order": n, "section": "02-nul", "section_as_printed": "நூல்",
        "section_source": "Project Madurai printed heading",
        "thinai": None, "thinai_source": None, "speaker": None,
        "speaker_source": None, "poet": None, "poet_source": None,
        "first_line": record["lines"][0], "line_count": len(record["lines"]),
        "textual_status": "complete", "canonical_text_available": True,
        "candidate_texts_available": False, "lacuna_present": False,
        "lacuna_location": None, "source_note_available": False,
        "source_note_source": None, "extraction_status": "success",
        "source": "Project Madurai", "source_url": s["source_url"],
        "project_madurai_id": s["project_madurai_id"],
        "source_object_id": s["project_madurai_id"], "source_file": s["source_file"],
        "language": "Tamil", "script": "Tamil", "status": "source-transcribed",
        "editorial_changes": False}
    y = yaml.safe_dump(fm, allow_unicode=True, sort_keys=False).strip()
    return f"---\n{y}\n---\n\n# இனியவை நாற்பது {n}\n\n" + "\n".join(record["lines"]) + "\n"


def _split_iniyavai(work, p, data, frozen, verbose):
    records = data["poems"]
    ep = {f"{n:03d}.md" for n in range(1, 41)}
    es = {"01-invocation.md", "02-nul.md"}
    p["poems"].mkdir(parents=True, exist_ok=True); p["sections"].mkdir(parents=True, exist_ok=True)
    bad = [x for x in p["poems"].rglob("*") if x.is_file() and (x.parent != p["poems"] or x.name not in ep)]
    bad += [x for x in p["sections"].rglob("*") if x.is_file() and (x.parent != p["sections"] or x.name not in es)]
    if bad: raise RuntimeError(f"Refusing regeneration with unexpected physical files: {bad}")
    for r in records:
        (p["poems"]/f"{r['poem_number']:03d}.md").write_text(_iniyavai_markdown(r),encoding="utf-8",newline="\n")
    pref=data["prefatory_text"]
    inv=f"# {pref['heading_as_printed']}\n\n"+"\n".join(pref["lines"])+"\n"
    (p["sections"]/"01-invocation.md").write_text(inv,encoding="utf-8",newline="\n")
    body=["# நூல்\n\nProject Madurai source-printed division.\n"]+[_iniyavai_markdown(x).split("---\n",2)[-1].lstrip() for x in records]
    (p["sections"]/"02-nul.md").write_text("\n".join(body),encoding="utf-8",newline="\n")
    p["full_text"].write_text("# இனியவை நாற்பது — Project Madurai source transcription\n\n"+inv+"\n"+"\n".join(body),encoding="utf-8",newline="\n")
    write_json(p["structure"],{"sections":data["sections"],"prefatory_text":pref},force=True)
    sm=json.loads(p["source_metadata"].read_text(encoding="utf-8"))
    write_json(p["metadata"],{"corpus_schema_version":"1.0.0" if frozen else None,"version_status":"frozen" if frozen else "unfrozen",
      "title_tamil":"இனியவை நாற்பது","title_english":"Iṉiyavai Nāṟpatu","work_slug":work,"work_id":work,"programme_id":"pathinenkilkanakku",
      "author":"பூதஞ்சேந்தனார்","author_as_printed":"பூதஞ்சேந்தனார்","numbered_poem_record_count":40,"available_poem_count":40,"missing_poems":[],
      "unnumbered_literary_record_count":1,"source_name":"Project Madurai","source_url":spec(work)["source_url"],"project_madurai_id":"pmuni0025",
      "source_scope":"Second work bounded within combined Project Madurai object","accessed_date":sm["retrieval_date"],"source_checksum_sha256":sm["source_checksum_sha256"],
      "encoding":"UTF-8","normalization":"Unicode NFC","notes":["The unnumbered கடவுள் வாழ்த்து is preserved at work level."]},force=True)
    if not (p["corpus"]/"README.md").exists():(p["corpus"]/"README.md").write_text("# இனியவை நாற்பது (Iṉiyavai Nāṟpatu)\n\nUnfrozen source-faithful onboarding from the bounded second work in Project Madurai `pmuni0025`.\n",encoding="utf-8",newline="\n")
    if verbose:print("Wrote 40 verse files and 2 source-printed sections")


def _kar_markdown(record: dict) -> str:
    s=spec("kar-narpathu");n=record["poem_number"]
    fm={"schema_version":"1.0.0","work":"கார் நாற்பது","work_english":"Kār Nāṟpatu",
      "work_id":"kar-narpathu","work_slug":"kar-narpathu","programme_id":"pathinenkilkanakku",
      "record_type":"verse","poem_number":n,"poem_number_as_printed":record["poem_number_as_printed"],
      "poem_number_source":"Project Madurai printed line-end marker","source_order":n,
      "section":"001-040","section_source":"Mechanical whole-work navigation; no internal division printed",
      "thinai":None,"thinai_source":None,"speaker":None,"speaker_source":None,
      "poet":None,"poet_source":None,"first_line":record["lines"][0],"line_count":len(record["lines"]),
      "textual_status":"complete","canonical_text_available":True,"candidate_texts_available":False,
      "lacuna_present":False,"lacuna_location":None,"source_note_available":bool(record["source_note_lines"]),
      "source_note_source":"Project Madurai printed dramatic-context prose and/or variant note" if record["source_note_lines"] else None,
      "extraction_status":"success","source":"Project Madurai","source_url":s["source_url"],
      "project_madurai_id":"pmuni0029","source_object_id":"pmuni0029","source_file":s["source_file"],
      "language":"Tamil","script":"Tamil","status":"source-transcribed","editorial_changes":False}
    y=yaml.safe_dump(fm,allow_unicode=True,sort_keys=False).strip()
    out=f"---\n{y}\n---\n\n# கார் நாற்பது {n}\n\n"+"\n".join(record["lines"])+"\n"
    if record["source_note_lines"]:out+="\n## Source note (as printed)\n\n"+"\n".join(record["source_note_lines"])+"\n"
    return out


def _split_kar(work,p,data,frozen,verbose):
    records=data["poems"];ep={f"{n:03d}.md" for n in range(1,41)};es={"001-040.md"}
    p["poems"].mkdir(parents=True,exist_ok=True);p["sections"].mkdir(parents=True,exist_ok=True)
    bad=[x for x in p["poems"].rglob("*") if x.is_file() and (x.parent!=p["poems"] or x.name not in ep)]
    bad += [x for x in p["sections"].rglob("*") if x.is_file() and (x.parent!=p["sections"] or x.name not in es)]
    if bad:raise RuntimeError(f"Refusing regeneration with unexpected physical files: {bad}")
    for r in records:(p["poems"]/f"{r['poem_number']:03d}.md").write_text(_kar_markdown(r),encoding="utf-8",newline="\n")
    body=["# கார் நாற்பது 001–040\n\nMechanical whole-work navigation; the source prints no internal division.\n"]+[_kar_markdown(x).split("---\n",2)[-1].lstrip() for x in records]
    (p["sections"]/"001-040.md").write_text("\n".join(body),encoding="utf-8",newline="\n")
    p["full_text"].write_text("# கார் நாற்பது — Project Madurai source transcription\n\n"+"\n".join(body),encoding="utf-8",newline="\n")
    write_json(p["structure"],{"sections":data["sections"]},force=True)
    sm=json.loads(p["source_metadata"].read_text(encoding="utf-8"))
    write_json(p["metadata"],{"corpus_schema_version":"1.0.0" if frozen else None,"version_status":"frozen" if frozen else "unfrozen",
      "title_tamil":"கார் நாற்பது","title_english":"Kār Nāṟpatu","work_slug":work,"work_id":work,"programme_id":"pathinenkilkanakku",
      "author":"மதுரைக் கண்ணங்கூத்தனார்","author_as_printed":"மதுரைக் கண்ணங்கூத்தனார்","numbered_poem_record_count":40,
      "available_poem_count":40,"missing_poems":[],"source_name":"Project Madurai","source_url":spec(work)["source_url"],
      "project_madurai_id":"pmuni0029","source_scope":"First work bounded within combined Project Madurai object",
      "accessed_date":sm["retrieval_date"],"source_checksum_sha256":sm["source_checksum_sha256"],"encoding":"UTF-8","normalization":"Unicode NFC",
      "navigation_sections":{"type":"mechanical whole-work","count":1},
      "notes":["Printed dramatic-context prose and variant lines remain source notes; speaker is not inferred.","No internal work division is printed."]},force=True)
    if not (p["corpus"]/"README.md").exists():(p["corpus"]/"README.md").write_text("# கார் நாற்பது (Kār Nāṟpatu)\n\nUnfrozen source-faithful onboarding from the bounded first work in Project Madurai `pmuni0029`.\n",encoding="utf-8",newline="\n")
    if verbose:print("Wrote 40 verse files and one mechanical navigation section")


def _kalavazhi_markdown(record):
    s=spec("kalavazhi-narpathu");n=record["poem_number"]
    fm={"schema_version":"1.0.0","work":"களவழி நாற்பது","work_english":"Kaḷavaḻi Nāṟpatu",
      "work_id":"kalavazhi-narpathu","work_slug":"kalavazhi-narpathu","programme_id":"pathinenkilkanakku",
      "record_type":"verse","poem_number":n,"poem_number_as_printed":record["poem_number_as_printed"],
      "poem_number_source":"Project Madurai printed line-end marker","source_order":n,"section":"001-040",
      "section_source":"Mechanical whole-work navigation; no internal division printed",
      "thinai":None,"thinai_source":None,"speaker":None,"speaker_source":None,"poet":None,"poet_source":None,
      "first_line":record["lines"][0],"line_count":len(record["lines"]),"textual_status":"complete",
      "canonical_text_available":True,"candidate_texts_available":False,"lacuna_present":False,"lacuna_location":None,
      "source_note_available":bool(record["source_note_lines"]),"source_note_source":"Project Madurai printed variant note" if record["source_note_lines"] else None,
      "extraction_status":"success","source":"Project Madurai","source_url":s["source_url"],"project_madurai_id":"pmuni0025",
      "source_object_id":"pmuni0025","source_file":s["source_file"],"language":"Tamil","script":"Tamil","status":"source-transcribed","editorial_changes":False}
    y=yaml.safe_dump(fm,allow_unicode=True,sort_keys=False).strip()
    out=f"---\n{y}\n---\n\n# களவழி நாற்பது {n}\n\n"+"\n".join(record["lines"])+"\n"
    if record["source_note_lines"]:out+="\n## Source note (as printed)\n\n"+"\n".join(record["source_note_lines"])+"\n"
    return out


def _split_kalavazhi(work,p,data,frozen,verbose):
    records=data["poems"];ep={f"{n:03d}.md" for n in range(1,41)};es={"001-040.md"}
    p["poems"].mkdir(parents=True,exist_ok=True);p["sections"].mkdir(parents=True,exist_ok=True)
    bad=[x for x in p["poems"].rglob("*") if x.is_file() and (x.parent!=p["poems"] or x.name not in ep)]
    bad += [x for x in p["sections"].rglob("*") if x.is_file() and (x.parent!=p["sections"] or x.name not in es)]
    if bad:raise RuntimeError(f"Refusing regeneration with unexpected physical files: {bad}")
    for r in records:(p["poems"]/f"{r['poem_number']:03d}.md").write_text(_kalavazhi_markdown(r),encoding="utf-8",newline="\n")
    tail=data["additional_unnumbered_literary_text"]
    body=["# களவழி நாற்பது 001–040\n\nMechanical navigation; no source division is asserted.\n"]+[_kalavazhi_markdown(x).split("---\n",2)[-1].lstrip() for x in records]
    body += ["## Unnumbered concluding literary text (as printed)\n\n"+"\n".join(tail["lines"])+"\n"]
    (p["sections"]/"001-040.md").write_text("\n".join(body),encoding="utf-8",newline="\n")
    p["full_text"].write_text("# களவழி நாற்பது — Project Madurai source transcription\n\n"+"\n".join(body),encoding="utf-8",newline="\n")
    write_json(p["structure"],{"sections":data["sections"],"additional_unnumbered_literary_text":tail},force=True)
    sm=json.loads(p["source_metadata"].read_text(encoding="utf-8"))
    write_json(p["metadata"],{"corpus_schema_version":"1.0.0" if frozen else None,"version_status":"frozen" if frozen else "unfrozen",
      "title_tamil":"களவழி நாற்பது","title_english":"Kaḷavaḻi Nāṟpatu","work_slug":work,"work_id":work,"programme_id":"pathinenkilkanakku",
      "author":"பொய்கையார்","author_as_printed":"பொய்கையார்","numbered_poem_record_count":40,"available_poem_count":40,"missing_poems":[],
      "unnumbered_literary_record_count":1,"source_name":"Project Madurai","source_url":spec(work)["source_url"],"project_madurai_id":"pmuni0025",
      "source_scope":"Third work bounded within combined Project Madurai object","accessed_date":sm["retrieval_date"],
      "source_checksum_sha256":sm["source_checksum_sha256"],"encoding":"UTF-8","normalization":"Unicode NFC",
      "notes":["Five unnumbered literary lines follow printed record 40; they are preserved at work level and are not inferred as record 41.",
               "Printed variant lines remain source notes."]},force=True)
    if not (p["corpus"]/"README.md").exists():(p["corpus"]/"README.md").write_text("# களவழி நாற்பது (Kaḷavaḻi Nāṟpatu)\n\nUnfrozen source-faithful onboarding from the bounded third work in Project Madurai `pmuni0025`.\n",encoding="utf-8",newline="\n")
    if verbose:print("Wrote 40 numbered verse files, one mechanical section, and preserved the unnumbered concluding text")


def _aintinai_aimpathu_markdown(record):
    s=spec("aintinai-aimpathu");n=record["poem_number"];d=record["division_sequence"]
    names={1:"mullai",2:"kurinji",3:"marutam",4:"palai",5:"neytal"}
    fm={"schema_version":"1.0.0","work":"ஐந்திணை ஐம்பது","work_english":"Aintiṇai Aimpathu",
      "work_id":"aintinai-aimpathu","work_slug":"aintinai-aimpathu","programme_id":"pathinenkilkanakku",
      "record_type":"verse","poem_number":n,"poem_number_as_printed":record["poem_number_as_printed"],
      "poem_number_source":"Project Madurai printed line-end marker","source_order":n,
      "section":f"{d:02d}-{names[d]}","section_source":"Project Madurai printed tiṇai division",
      "thinai":record["thinai"],"thinai_as_printed":record["thinai_as_printed"],"thinai_source":"Project Madurai printed division heading",
      "speaker":None,"speaker_source":None,"poet":None,"poet_source":None,
      "position_within_division":record["position_within_division"],"first_line":record["lines"][0],"line_count":len(record["lines"]),
      "textual_status":"complete","canonical_text_available":True,"candidate_texts_available":False,"lacuna_present":False,
      "lacuna_location":None,"source_note_available":False,"source_note_source":None,"extraction_status":"success",
      "source":"Project Madurai","source_url":s["source_url"],"project_madurai_id":"pmuni0027","source_object_id":"pmuni0027",
      "source_file":s["source_file"],"language":"Tamil","script":"Tamil","status":"source-transcribed","editorial_changes":False}
    y=yaml.safe_dump(fm,allow_unicode=True,sort_keys=False).strip()
    return f"---\n{y}\n---\n\n# ஐந்திணை ஐம்பது {n}\n\n"+"\n".join(record["lines"])+"\n"


def _split_aintinai_aimpathu(work,p,data,frozen,verbose):
    records=data["poems"];names={1:"mullai",2:"kurinji",3:"marutam",4:"palai",5:"neytal"}
    ep={f"{n:03d}.md" for n in range(1,51)};es={f"{i:02d}-{names[i]}.md" for i in range(1,6)}
    p["poems"].mkdir(parents=True,exist_ok=True);p["sections"].mkdir(parents=True,exist_ok=True)
    bad=[x for x in p["poems"].rglob("*") if x.is_file() and (x.parent!=p["poems"] or x.name not in ep)]
    bad += [x for x in p["sections"].rglob("*") if x.is_file() and (x.parent!=p["sections"] or x.name not in es)]
    if bad:raise RuntimeError(f"Refusing regeneration with unexpected physical files: {bad}")
    for r in records:(p["poems"]/f"{r['poem_number']:03d}.md").write_text(_aintinai_aimpathu_markdown(r),encoding="utf-8",newline="\n")
    pref=data["prefatory_text"];full=["# ஐந்திணை ஐம்பது — Project Madurai source transcription\n",f"## {pref['heading_as_printed']}\n\n"+"\n".join(pref["lines"])+"\n"]
    for d in data["sections"]:
        selected=[x for x in records if x["division_sequence"]==d["sequence"]]
        text=[f"# {d['heading_as_printed']}\n"]+d["description_as_printed"]+[""]+[_aintinai_aimpathu_markdown(x).split("---\n",2)[-1].lstrip() for x in selected]
        (p["sections"]/f"{d['sequence']:02d}-{names[d['sequence']]}.md").write_text("\n".join(text),encoding="utf-8",newline="\n")
        full += ["## "+d["heading_as_printed"]+"\n"]+d["description_as_printed"]+[_aintinai_aimpathu_markdown(x).split("---\n",2)[-1].lstrip() for x in selected]
    p["full_text"].write_text("\n".join(full),encoding="utf-8",newline="\n")
    write_json(p["structure"],{"prefatory_text":pref,"divisions":data["sections"]},force=True)
    sm=json.loads(p["source_metadata"].read_text(encoding="utf-8"))
    write_json(p["metadata"],{"corpus_schema_version":"1.0.0" if frozen else None,"version_status":"frozen" if frozen else "unfrozen",
      "title_tamil":"ஐந்திணை ஐம்பது","title_english":"Aintiṇai Aimpathu","work_slug":work,"work_id":work,"programme_id":"pathinenkilkanakku",
      "author":"மாறன் பொறையனார்","author_as_printed":"மாறன் பொறையனார்","numbered_poem_record_count":50,"available_poem_count":50,
      "missing_poems":[],"unnumbered_literary_record_count":1,"printed_division_count":5,"source_name":"Project Madurai",
      "source_url":spec(work)["source_url"],"project_madurai_id":"pmuni0027","source_scope":"First selected work bounded within combined Project Madurai object",
      "accessed_date":sm["retrieval_date"],"source_checksum_sha256":sm["source_checksum_sha256"],"encoding":"UTF-8","normalization":"Unicode NFC",
      "notes":["The unnumbered பாயிரம் is preserved at work level.","Five printed tiṇai divisions each contain ten records.","Division descriptions remain in the structural inventory; speaker is not inferred."]},force=True)
    if not (p["corpus"]/"README.md").exists():(p["corpus"]/"README.md").write_text("# ஐந்திணை ஐம்பது (Aintiṇai Aimpathu)\n\nUnfrozen source-faithful onboarding from the bounded first selected work in Project Madurai `pmuni0027`.\n",encoding="utf-8",newline="\n")
    if verbose:print("Wrote 50 verse files and 5 source-printed tiṇai sections")


def _aintinai_elupathu_markdown(record):
    s=spec("aintinai-elupathu");n=record["poem_number"];lost=not bool(record["lines"])
    names={1:"kurinji",2:"mullai",3:"palai",4:"marutam",5:"neytal"};d=record["division_sequence"]
    fm={"schema_version":"1.0.0","work":"ஐந்திணை எழுபது","work_english":"Aintiṇai Eḻupathu",
      "work_id":"aintinai-elupathu","work_slug":"aintinai-elupathu","programme_id":"pathinenkilkanakku",
      "record_type":"verse","poem_number":n,"poem_number_as_printed":record["poem_number_as_printed"],
      "poem_number_source":"Project Madurai printed number or explicit combined loss statement","source_order":n,
      "section":f"{d:02d}-{names[d]}","section_source":"Project Madurai printed tiṇai division",
      "thinai":record["thinai"],"thinai_as_printed":record["thinai_as_printed"],"thinai_source":"Project Madurai printed division heading",
      "speaker":None,"speaker_source":None,"poet":None,"poet_source":None,"position_within_division":record["position_within_division"],
      "first_line":record["lines"][0] if record["lines"] else "","line_count":len(record["lines"]),
      "textual_status":"lost" if lost else "complete","canonical_text_available":not lost,"candidate_texts_available":False,
      "lacuna_present":False,"lacuna_location":None,"source_note_available":bool(record["source_note_lines"]),
      "source_note_source":"Project Madurai printed combined loss statement" if record["source_note_lines"] else None,
      "extraction_status":"success","source":"Project Madurai","source_url":s["source_url"],"project_madurai_id":"pmuni0027",
      "source_object_id":"pmuni0027","source_file":s["source_file"],"language":"Tamil","script":"Tamil",
      "status":record["status"],"editorial_changes":False}
    y=yaml.safe_dump(fm,allow_unicode=True,sort_keys=False).strip()
    out=f"---\n{y}\n---\n\n# ஐந்திணை எழுபது {n}\n\n"+"\n".join(record["lines"])+"\n"
    if record["source_note_lines"]:out+="\n## Source note (as printed)\n\n"+"\n".join(record["source_note_lines"])+"\n"
    return out


def _split_aintinai_elupathu(work,p,data,frozen,verbose):
    records=data["poems"];names={1:"kurinji",2:"mullai",3:"palai",4:"marutam",5:"neytal"}
    ep={f"{n:03d}.md" for n in range(1,71)};es={f"{i:02d}-{names[i]}.md" for i in range(1,6)}
    p["poems"].mkdir(parents=True,exist_ok=True);p["sections"].mkdir(parents=True,exist_ok=True)
    bad=[x for x in p["poems"].rglob("*") if x.is_file() and (x.parent!=p["poems"] or x.name not in ep)]
    bad += [x for x in p["sections"].rglob("*") if x.is_file() and (x.parent!=p["sections"] or x.name not in es)]
    if bad:raise RuntimeError(f"Refusing regeneration with unexpected physical files: {bad}")
    for r in records:(p["poems"]/f"{r['poem_number']:03d}.md").write_text(_aintinai_elupathu_markdown(r),encoding="utf-8",newline="\n")
    pref=data["prefatory_text"];full=["# ஐந்திணை எழுபது — Project Madurai source transcription\n",f"## {pref['heading_as_printed']}\n\n"+"\n".join(pref["lines"])+"\n"]
    for d in data["sections"]:
        selected=[x for x in records if x["division_sequence"]==d["sequence"]]
        text=[f"# {d['heading_as_printed']}\n"]+[_aintinai_elupathu_markdown(x).split("---\n",2)[-1].lstrip() for x in selected]
        (p["sections"]/f"{d['sequence']:02d}-{names[d['sequence']]}.md").write_text("\n".join(text),encoding="utf-8",newline="\n")
        full += ["## "+d["heading_as_printed"]+"\n"]+[_aintinai_elupathu_markdown(x).split("---\n",2)[-1].lstrip() for x in selected]
    p["full_text"].write_text("\n".join(full),encoding="utf-8",newline="\n")
    write_json(p["structure"],{"prefatory_text":pref,"divisions":data["sections"]},force=True)
    sm=json.loads(p["source_metadata"].read_text(encoding="utf-8"))
    write_json(p["metadata"],{"corpus_schema_version":"1.0.0" if frozen else None,"version_status":"frozen" if frozen else "unfrozen",
      "title_tamil":"ஐந்திணை எழுபது","title_english":"Aintiṇai Eḻupathu","work_slug":work,"work_id":work,"programme_id":"pathinenkilkanakku",
      "author":"மூவாதியார்","author_as_printed":"மூவாதியார்","numbered_poem_record_count":70,"available_poem_count":66,
      "missing_poems":[25,26,69,70],"unnumbered_literary_record_count":1,"printed_division_count":5,"source_name":"Project Madurai",
      "source_url":spec(work)["source_url"],"project_madurai_id":"pmuni0027","source_scope":"Second selected work bounded within combined Project Madurai object",
      "accessed_date":sm["retrieval_date"],"source_checksum_sha256":sm["source_checksum_sha256"],"encoding":"UTF-8","normalization":"Unicode NFC",
      "notes":["The unnumbered கடவுள் வாழ்த்து is preserved at work level.","Records 25, 26, 69, and 70 are explicitly printed as lost; their canonical bodies remain empty.","Five printed tiṇai divisions each contain fourteen record identities."]},force=True)
    if not (p["corpus"]/"README.md").exists():(p["corpus"]/"README.md").write_text("# ஐந்திணை எழுபது (Aintiṇai Eḻupathu)\n\nUnfrozen source-faithful onboarding from the bounded second selected work in Project Madurai `pmuni0027`.\n",encoding="utf-8",newline="\n")
    if verbose:print("Wrote 70 record files and 5 source-printed tiṇai sections")


def _thinaimalai_markdown(record):
    s=spec("thinaimalai-nutraimbathu");n=record["poem_number"];d=record["division_sequence"]
    names={1:"kurinji",2:"neytal",3:"palai",4:"mullai",5:"marutam"}
    fm={"schema_version":"1.0.0","work":"திணைமாலை நூற்றைம்பது","work_english":"Tiṇaimālai Nūṟṟaimpatu",
      "work_id":"thinaimalai-nutraimbathu","work_slug":"thinaimalai-nutraimbathu","programme_id":"pathinenkilkanakku",
      "record_type":"verse","poem_number":n,"poem_number_as_printed":record["poem_number_as_printed"],
      "poem_number_source":"Project Madurai printed parenthesized line-end marker","source_order":n,
      "section":f"{d:02d}-{names[d]}","section_source":"Project Madurai printed tiṇai division",
      "thinai":record["thinai"],"thinai_as_printed":record["thinai_as_printed"],"thinai_source":"Project Madurai printed division heading",
      "speaker":None,"speaker_source":None,"poet":None,"poet_source":None,"position_within_division":record["position_within_division"],
      "first_line":record["lines"][0],"line_count":len(record["lines"]),"textual_status":"complete","canonical_text_available":True,
      "candidate_texts_available":False,"lacuna_present":False,"lacuna_location":None,"source_note_available":False,
      "source_note_source":None,"extraction_status":"success","source":"Project Madurai","source_url":s["source_url"],
      "project_madurai_id":"pmuni0056","source_object_id":"pmuni0056","source_file":s["source_file"],
      "language":"Tamil","script":"Tamil","status":"source-transcribed","editorial_changes":False}
    y=yaml.safe_dump(fm,allow_unicode=True,sort_keys=False).strip()
    return f"---\n{y}\n---\n\n# திணைமாலை நூற்றைம்பது {n}\n\n"+"\n".join(record["lines"])+"\n"


def _split_thinaimalai(work,p,data,frozen,verbose):
    records=data["poems"];names={1:"kurinji",2:"neytal",3:"palai",4:"mullai",5:"marutam"}
    ep={f"{n:03d}.md" for n in range(1,154)};es={f"{i:02d}-{names[i]}.md" for i in range(1,6)}
    p["poems"].mkdir(parents=True,exist_ok=True);p["sections"].mkdir(parents=True,exist_ok=True)
    bad=[x for x in p["poems"].rglob("*") if x.is_file() and (x.parent!=p["poems"] or x.name not in ep)]
    bad += [x for x in p["sections"].rglob("*") if x.is_file() and (x.parent!=p["sections"] or x.name not in es)]
    if bad:raise RuntimeError(f"Refusing regeneration with unexpected physical files: {bad}")
    for r in records:(p["poems"]/f"{r['poem_number']:03d}.md").write_text(_thinaimalai_markdown(r),encoding="utf-8",newline="\n")
    full=["# திணைமாலை நூற்றைம்பது — Project Madurai source transcription\n"]
    for d in data["sections"]:
        selected=[x for x in records if x["division_sequence"]==d["sequence"]]
        text=[f"# {d['heading_as_printed']}\n"]+d["description_as_printed"]+[""]+[_thinaimalai_markdown(x).split("---\n",2)[-1].lstrip() for x in selected]
        (p["sections"]/f"{d['sequence']:02d}-{names[d['sequence']]}.md").write_text("\n".join(text),encoding="utf-8",newline="\n")
        full += ["## "+d["heading_as_printed"]+"\n"]+d["description_as_printed"]+[_thinaimalai_markdown(x).split("---\n",2)[-1].lstrip() for x in selected]
    extra=data["additional_unnumbered_literary_text"]
    full += [f"## {extra['heading_as_printed']}\n\n"+"\n".join(extra["lines"])+"\n"]
    p["full_text"].write_text("\n".join(full),encoding="utf-8",newline="\n")
    write_json(p["structure"],{"divisions":data["sections"],
      "additional_unnumbered_literary_text":extra},force=True)
    sm=json.loads(p["source_metadata"].read_text(encoding="utf-8"))
    write_json(p["metadata"],{"corpus_schema_version":"1.0.0" if frozen else None,"version_status":"frozen" if frozen else "unfrozen",
      "title_tamil":"திணைமாலை நூற்றைம்பது","title_english":"Tiṇaimālai Nūṟṟaimpatu","work_slug":work,"work_id":work,
      "programme_id":"pathinenkilkanakku","author":"கணிமேதாவியார்","author_as_printed":"கணிமேதாவியார்",
      "nominal_count_from_title":150,"numbered_poem_record_count":153,"available_poem_count":153,"missing_poems":[],
      "unnumbered_literary_record_count":1,
      "printed_division_count":5,"source_name":"Project Madurai","source_url":spec(work)["source_url"],"project_madurai_id":"pmuni0056",
      "accessed_date":sm["retrieval_date"],"source_checksum_sha256":sm["source_checksum_sha256"],"encoding":"UTF-8","normalization":"Unicode NFC",
      "notes":["The selected source prints 153 numbered records despite the nominal count in the title; all 153 are retained.","Five printed tiṇai divisions contain 31, 31, 30, 31, and 30 records.","A concluding unnumbered சிறப்புப் பாயிரம் is preserved at work level.","Printed division descriptions remain structural evidence; speaker is not inferred."]},force=True)
    if not (p["corpus"]/"README.md").exists():(p["corpus"]/"README.md").write_text("# திணைமாலை நூற்றைம்பது (Tiṇaimālai Nūṟṟaimpatu)\n\nUnfrozen source-faithful onboarding from Project Madurai `pmuni0056`.\n",encoding="utf-8",newline="\n")
    if verbose:print("Wrote 153 verse files and 5 source-printed tiṇai sections")


def _generic_record_markdown(work, record):
    s=spec(work); n=record["poem_number"]; note=record.get("source_note_lines",[])
    fm={"schema_version":"1.0.0","work":s["title_tamil"],"work_english":s["title_english"],
      "work_id":work,"work_slug":work,"programme_id":"pathinenkilkanakku","record_type":"verse",
      "poem_number":n,"poem_number_as_printed":record.get("poem_number_as_printed",n),
      "poem_number_source":"Project Madurai printed record marker","source_order":record.get("source_order",n),
      "section":record.get("division_sequence"),"section_source":"Project Madurai printed structure" if record.get("division_sequence") else "mechanically generated navigation",
      "section_as_printed":record.get("division_as_printed"),"thinai":None,"thinai_source":None,
      "speaker":None,"speaker_source":None,"poet":None,"poet_source":None,
      "record_title_as_printed":record.get("record_title_as_printed"),
      "record_title_source":"Project Madurai printed heading" if record.get("record_title_as_printed") else None,
      "first_line":record["lines"][0] if record["lines"] else "","line_count":len(record["lines"]),
      "textual_status":"complete","canonical_text_available":True,"candidate_texts_available":False,
      "lacuna_present":any("..." in x for x in record["lines"]),"lacuna_location":None,
      "source_note_available":bool(note),"source_note_source":"Project Madurai printed prose" if note else None,
      "extraction_status":"success","source":"Project Madurai","source_url":s["source_url"],
      "project_madurai_id":s["project_madurai_id"],"source_object_id":s["project_madurai_id"],
      "source_file":s["source_file"],"language":"Tamil","script":"Tamil","status":"source-transcribed",
      "editorial_changes":False}
    y=yaml.safe_dump(fm,allow_unicode=True,sort_keys=False).strip()
    out=f"---\n{y}\n---\n\n# {s['title_tamil']} {n}\n\n"+"\n".join(record["lines"])+"\n"
    if note: out+="\n## Source note (as printed)\n\n"+"\n".join(note)+"\n"
    return out


def _generic_sections(work,data):
    sections=data.get("sections",[]); expected=spec(work)["expected_sections"]
    if sections:
        return [(f"{x['sequence']:02d}-{x['poem_start']:03d}-{x['poem_end']:03d}.md",x,
                 [r for r in data["poems"] if r.get("division_sequence")==x["sequence"]])
                for x in sections]
    if expected==2 and data.get("prefatory_text"):
        return [("01-prefatory.md",{"heading_as_printed":data["prefatory_text"]["heading_as_printed"]},[]),
                ("02-nul.md",{"heading_as_printed":"நூல்"},data["poems"])]
    return [(f"001-{len(data['poems']):03d}.md",{"heading_as_printed":"Mechanical navigation"},data["poems"])]


def _split_generic(work,p,data,frozen,verbose):
    records=data["poems"]; width=4 if len(records)>999 else 3
    section_defs=_generic_sections(work,data)
    ep={f"{n:0{width}d}.md" for n in range(1,len(records)+1)}
    es={x[0] for x in section_defs}
    p["poems"].mkdir(parents=True,exist_ok=True);p["sections"].mkdir(parents=True,exist_ok=True)
    bad=[x for x in p["poems"].rglob("*") if x.is_file() and (x.parent!=p["poems"] or x.name not in ep)]
    bad += [x for x in p["sections"].rglob("*") if x.is_file() and (x.parent!=p["sections"] or x.name not in es)]
    if bad: raise RuntimeError(f"Refusing regeneration with unexpected physical files: {bad}")
    for r in records:(p["poems"]/f"{r['poem_number']:0{width}d}.md").write_text(_generic_record_markdown(work,r),encoding="utf-8",newline="\n")
    full=[f"# {spec(work)['title_tamil']} — Project Madurai source transcription\n"]
    if data.get("prefatory_text"):
        q=data["prefatory_text"]; full += [f"## {q['heading_as_printed']}\n\n"+"\n".join(q["lines"])+"\n"]
    for filename,sec,members in section_defs:
        content=[f"# {sec['heading_as_printed']}\n"]
        if not members and data.get("prefatory_text"): content += data["prefatory_text"]["lines"]
        else: content += [_generic_record_markdown(work,r).split("---\n",2)[-1].lstrip() for r in members]
        (p["sections"]/filename).write_text("\n".join(content),encoding="utf-8",newline="\n")
        if members: full += [f"## {sec['heading_as_printed']}\n"]+content[1:]
    p["full_text"].write_text("\n".join(full),encoding="utf-8",newline="\n")
    write_json(p["structure"],{"sections":data.get("sections",[]),"navigation_files":[x[0] for x in section_defs],
      "prefatory_text":data.get("prefatory_text")},force=True)
    sm=json.loads(p["source_metadata"].read_text(encoding="utf-8")); s=spec(work)
    write_json(p["metadata"],{"corpus_schema_version":"1.0.0" if frozen else None,
      "version_status":"frozen" if frozen else "unfrozen","title_tamil":s["title_tamil"],
      "title_english":s["title_english"],"work_slug":work,"work_id":work,"programme_id":"pathinenkilkanakku",
      "numbered_poem_record_count":len(records),"available_poem_count":len(records),"missing_poems":[],
      "printed_division_count":len(data.get("sections",[])),"source_name":"Project Madurai",
      "source_url":s["source_url"],"project_madurai_id":s["project_madurai_id"],
      "accessed_date":sm["retrieval_date"],"source_checksum_sha256":sm["source_checksum_sha256"],
      "encoding":"UTF-8","normalization":"Unicode NFC",
      "notes":["Source-specific grammar is documented in the reconnaissance record.","No controlled metadata is inferred from prose."]},force=True)
    readme=p["corpus"]/"README.md"
    if not readme.exists(): readme.write_text(f"# {s['title_tamil']} ({s['title_english']})\n\nUnfrozen source-faithful onboarding from Project Madurai `{s['project_madurai_id']}`.\n",encoding="utf-8",newline="\n")
    if verbose: print(f"Wrote {len(records)} records and {len(section_defs)} sections")


def split(work: str, force=True, dry_run=False, verbose=False):
    p = work_paths(work)
    data = json.loads(p["normalized"].read_text(encoding="utf-8"))
    records = data["poems"]
    existing_metadata = (json.loads(p["metadata"].read_text(encoding="utf-8"))
                         if p["metadata"].exists() else {})
    frozen = (existing_metadata.get("corpus_schema_version") == "1.0.0"
              and existing_metadata.get("version_status") == "frozen")
    if work == "naladiyar":
        if dry_run:
            print("Would write 400 quatrain files and 40 chapter sections")
            return
        return _split_naladiyar(work, p, data, frozen, verbose)
    if work == "nanmanikkadigai":
        if dry_run:
            print("Would write 106 verse files and 2 source-printed sections")
            return
        return _split_nanmanikkadigai(work, p, data, frozen, verbose)
    if work == "inna-narpathu":
        if dry_run:
            print("Would write 40 verse files and 2 source-printed sections")
            return
        return _split_inna(work, p, data, frozen, verbose)
    if work == "iniyavai-narpathu":
        if dry_run: print("Would write 40 verse files and 2 source-printed sections"); return
        return _split_iniyavai(work,p,data,frozen,verbose)
    if work == "kar-narpathu":
        if dry_run:print("Would write 40 verse files and one section");return
        return _split_kar(work,p,data,frozen,verbose)
    if work == "kalavazhi-narpathu":
        if dry_run:print("Would write 40 numbered verse files and one section");return
        return _split_kalavazhi(work,p,data,frozen,verbose)
    if work == "aintinai-aimpathu":
        if dry_run:print("Would write 50 verse files and 5 source sections");return
        return _split_aintinai_aimpathu(work,p,data,frozen,verbose)
    if work == "aintinai-elupathu":
        if dry_run:print("Would write 70 record files and 5 source sections");return
        return _split_aintinai_elupathu(work,p,data,frozen,verbose)
    if work == "thinaimalai-nutraimbathu":
        if dry_run:print("Would write 153 verse files and 5 source sections");return
        return _split_thinaimalai(work,p,data,frozen,verbose)
    if work in {"thinaimozhi-aimpathu","tirikatukam","acharakkovai","pazhamozhi-nanuru",
                "sirupanchamulam","muthumozhi-kanchi","elati","kainnilai"}:
        if dry_run: print(f"Would write {len(records)} records"); return
        return _split_generic(work,p,data,frozen,verbose)
    expected_poems = {f"{n:04d}.md" for n in range(1, 1331)}
    expected_sections = {
        f"{c:03d}-{(c-1)*10+1:04d}-{c*10:04d}.md" for c in range(1, 134)}
    if dry_run:
        print("Would write 1330 couplet files and 133 chapter section files")
        return
    p["poems"].mkdir(parents=True, exist_ok=True)
    p["sections"].mkdir(parents=True, exist_ok=True)
    bad = [x for x in p["poems"].rglob("*") if x.is_file() and
           (x.parent != p["poems"] or x.name not in expected_poems)]
    bad += [x for x in p["sections"].rglob("*") if x.is_file() and
            (x.parent != p["sections"] or x.name not in expected_sections)]
    if bad:
        raise RuntimeError("Refusing regeneration with unexpected physical files: " +
                           repr([str(x.relative_to(p["corpus"])) for x in bad]))
    for record in records:
        (p["poems"] / f"{record['poem_number']:04d}.md").write_text(
            _tirukkural_markdown(record), encoding="utf-8", newline="\n")
    full = ["# திருக்குறள் — Project Madurai source transcription\n"]
    for chapter in data["chapters"]:
        heading = chapter["heading_as_printed"] or \
            f"Chapter {chapter['sequence']} (printed chapter heading absent)"
        full.append(f"## {heading}\n")
        full.extend(_tirukkural_markdown(x).split("---\n", 2)[-1].lstrip()
                    for x in records if x["chapter_sequence"] == chapter["sequence"])
    p["full_text"].write_text("\n".join(full), encoding="utf-8", newline="\n")
    for chapter in data["chapters"]:
        selected = [x for x in records
                    if x["chapter_sequence"] == chapter["sequence"]]
        heading = chapter["heading_as_printed"] or \
            f"Chapter {chapter['sequence']} — printed heading absent"
        content = [f"# {heading}\n",
                   chapter["provenance"] + ".\n"]
        content.extend(_tirukkural_markdown(x).split("---\n", 2)[-1].lstrip()
                       for x in selected)
        filename = (f"{chapter['sequence']:03d}-"
                    f"{chapter['poem_start']:04d}-{chapter['poem_end']:04d}.md")
        (p["sections"] / filename).write_text(
            "\n".join(content), encoding="utf-8", newline="\n")
    write_json(p["structure"], {
        "major_divisions": [
            {"sequence": 1, "heading_as_printed": "1.  அறத்துப்பால்", "poem_start": 1, "poem_end": 380},
            {"sequence": 2, "heading_as_printed": "2.      பொருட்பால்", "poem_start": 381, "poem_end": 1080},
            {"sequence": 3, "heading_as_printed": "3.      காமத்துப்பால்", "poem_start": 1081, "poem_end": 1330}
        ],
        "chapters": data["chapters"],
        "heading_anomalies": data["heading_anomalies"],
        "numbering_anomalies": data["numbering_anomalies"],
    }, force=True)
    source_meta = json.loads(p["source_metadata"].read_text(encoding="utf-8"))
    metadata = {
        "corpus_schema_version": "1.0.0" if frozen else None,
        "version_status": "frozen" if frozen else "unfrozen",
        "title_tamil": "திருக்குறள்",
        "title_english": "Tirukkural",
        "work_slug": work,
        "work_id": work,
        "programme_id": "pathinenkilkanakku",
        "aliases": ["முப்பால்"],
        "author": "திருவள்ளுவர்",
        "author_as_printed": "திருவள்ளுவர்",
        "numbered_poem_record_count": 1330,
        "available_poem_count": 1330,
        "missing_poems": [],
        "printed_major_division_count": 3,
        "chapter_count": 133,
        "printed_chapter_heading_count": 132,
        "source_name": "Project Madurai",
        "source_url": spec(work)["source_url"],
        "project_madurai_id": spec(work)["project_madurai_id"],
        "accessed_date": source_meta["retrieval_date"],
        "source_checksum_sha256": source_meta["source_checksum_sha256"],
        "encoding": "UTF-8",
        "normalization": "Unicode NFC",
        "notes": [
            "Muppāl is an alias, not a separate corpus work.",
            "Global line-end couplet numbers are represented in provenance, not literary bodies.",
            "Four printed numbering anomalies and three chapter-heading anomalies are preserved.",
            "No commentary is present in the selected source."
        ]
    }
    write_json(p["metadata"], metadata, force=True)
    readme = p["corpus"] / "README.md"
    if not readme.exists():
        readme.write_text(
            "# திருக்குறள் (Tirukkural)\n\n"
            "Unfrozen source-faithful onboarding from Project Madurai `pmuni0001`. "
            "The 1,330 couplets are grouped by the 133 source chapter positions. "
            "See `metadata.json`, `structure-inventory.json`, and the reconnaissance record.\n",
            encoding="utf-8", newline="\n")
    if verbose:
        print("Wrote 1330 couplet files and 133 chapter sections")


def validate(work: str, dry_run=False, verbose=False) -> dict:
    p = work_paths(work)
    data = json.loads(p["normalized"].read_text(encoding="utf-8"))
    source = {x["poem_number"]: x for x in data["poems"]}
    total = spec(work)["expected_records"]
    width = 4 if total > 999 else 3
    expected = {f"{n:0{width}d}.md" for n in range(1, total + 1)}
    expected_sections = ({
        f"{c:03d}-{(c-1)*10+1:04d}-{c*10:04d}.md" for c in range(1, 134)}
        if work == "tirukkural" else
        {f"{c:03d}-{(c-1)*10+1:03d}-{c*10:03d}.md" for c in range(1, 41)}
        if work == "naladiyar" else {"001-040.md"}
        if work in {"kar-narpathu","kalavazhi-narpathu"} else
        {"01-mullai.md","02-kurinji.md","03-marutam.md","04-palai.md","05-neytal.md"}
        if work == "aintinai-aimpathu" else
        {"01-kurinji.md","02-mullai.md","03-palai.md","04-marutam.md","05-neytal.md"}
        if work == "aintinai-elupathu" else
        {"01-kurinji.md","02-neytal.md","03-palai.md","04-mullai.md","05-marutam.md"}
        if work == "thinaimalai-nutraimbathu" else
        {x[0] for x in _generic_sections(work,data)}
        if work in {"thinaimozhi-aimpathu","tirikatukam","acharakkovai","pazhamozhi-nanuru",
                    "sirupanchamulam","muthumozhi-kanchi","elati","kainnilai"}
        else {"01-invocation.md", "02-nul.md"})
    physical = [x for x in p["poems"].rglob("*") if x.is_file()]
    sections = [x for x in p["sections"].rglob("*") if x.is_file()]
    direct = {x.name for x in physical if x.parent == p["poems"]}
    sdirect = {x.name for x in sections if x.parent == p["sections"]}
    issues = []
    fidelity = []
    bodies = collections.defaultdict(list)
    firsts = collections.defaultdict(list)
    required = [
        "schema_version", "work", "work_id", "poem_number",
        "textual_status", "canonical_text_available",
        "candidate_texts_available", "lacuna_present", "lacuna_location",
        "extraction_status", "thinai", "thinai_source", "poet",
        "poet_source", "speaker", "speaker_source", "source_note_available",
        "source_note_source", "source_object_id", "poem_number_as_printed"
    ]
    if work in {"tirukkural", "naladiyar"}:
        required += ["chapter_sequence", "chapter_heading_as_printed"]
    elif work in {"nanmanikkadigai", "inna-narpathu", "iniyavai-narpathu"}:
        required += ["section_as_printed"]
    def add(n, typ, severity, message, md=None):
        issues.append({"work": work, "poem_number": n, "issue_type": typ,
                       "severity": severity, "message": message,
                       "markdown_file": md or ""})
    if len(physical) != total:
        add(None, "physical_poem_file_count", "error",
            f"Expected {total} files; found {len(physical)}")
    for name in sorted(expected - direct):
        add(None, "missing_poem_filename", "error", name)
    for x in physical:
        if x.parent != p["poems"] or x.name not in expected:
            add(None, "unexpected_poem_filename", "error",
                str(x.relative_to(p["poems"])))
    expected_section_count = spec(work)["expected_sections"]
    if len(sections) != expected_section_count:
        add(None, "physical_section_file_count", "error",
            f"Expected {expected_section_count} sections; found {len(sections)}")
    for name in sorted(expected_sections - sdirect):
        add(None, "missing_section_filename", "error", name)
    for x in sections:
        if x.parent != p["sections"] or x.name not in expected_sections:
            add(None, "unexpected_section_filename", "error",
                str(x.relative_to(p["sections"])))
    declared = collections.defaultdict(list)
    for md in physical:
        if md.suffix != ".md":
            continue
        try:
            fm, body = read_frontmatter(md)
            declared[int(fm["poem_number"])].append(str(md.relative_to(p["poems"])))
        except Exception as exc:
            add(None, "malformed_yaml", "error", f"{md}: {exc}")
            continue
        n = int(fm["poem_number"])
        for key in required:
            if key not in fm:
                add(n, "missing_metadata_key", "error", key, str(md))
        lines = markdown_literary_lines(body)
        sh = body_hash(source[n]["lines"])
        mh = body_hash(lines)
        note_lines = []
        if "## Source note (as printed)" in body:
            note_lines = [x.strip() for x in
                          body.split("## Source note (as printed)", 1)[1].splitlines()
                          if x.strip()]
        note_match = (canonical_body_text(note_lines) ==
                      canonical_body_text(source[n].get("source_note_lines", [])))
        fidelity.append({"poem_number": n, "source_body_hash_sha256": sh,
                         "markdown_body_hash_sha256": mh,
                         "source_output_match": sh == mh,
                         "source_note_match": note_match})
        if sh != mh:
            add(n, "source_output_mismatch", "error", "Body differs", str(md))
        if not note_match:
            add(n, "source_note_output_mismatch", "error",
                "Source note differs", str(md))
        if not lines:
            if (fm.get("textual_status") == "lost" and
                    fm.get("canonical_text_available") is False and
                    fm.get("extraction_status") == "success" and
                    not source[n]["lines"]):
                add(n, "source_text_lost", "warning",
                    "Selected source explicitly marks this record lost", str(md))
            else:
                add(n, "empty_record", "error",
                    "Canonical literary body is empty without source-lost status", str(md))
        else:
            key = canonical_body_text(lines)
            bodies[hashlib.sha256(key.encode()).hexdigest()].append(n)
            firsts[lines[0]].append(n)
    for n, names in declared.items():
        if len(names) > 1:
            add(n, "duplicate_yaml_poem_number", "error", repr(names))
    for digest, nums in bodies.items():
        if len(nums) > 1:
            add(None, "duplicate_poem_body", "warning", f"{nums}: {digest}")
    for line, nums in firsts.items():
        if len(nums) > 1:
            add(None, "shared_first_line", "info", f"{nums}: {line}")
    for anomaly in data["numbering_anomalies"]:
        add(anomaly["poem_number"], "printed_numbering_anomaly", "info",
            f"Printed {anomaly['poem_number_as_printed']}; source-order identity {anomaly['poem_number']}")
    for anomaly in data["heading_anomalies"]:
        add(anomaly.get("poem_start"), "printed_heading_anomaly", "info",
            json.dumps(anomaly, ensure_ascii=False))
    report = {
        "work": work,
        "source_record_count": len(source),
        "canonical_poem_files": len(physical),
        "canonical_literary_texts_available": sum(bool(x["lines"]) for x in source.values()),
        "missing_numbers": sorted(set(range(1, total + 1)) - set(declared)),
        "duplicate_numbers": sorted(n for n, names in declared.items() if len(names) > 1),
        "section_count": len(sections),
        "hardened_schema_files_checked": len(physical),
        "source_output_matches": sum(x["source_output_match"] for x in fidelity),
        "source_note_matches": sum(x["source_note_match"] for x in fidelity),
        "duplicate_full_bodies": [x for x in bodies.values() if len(x) > 1],
        "shared_first_lines": [x for x in firsts.values() if len(x) > 1],
        "source_output_fidelity": fidelity,
        "errors": sum(x["severity"] == "error" for x in issues),
        "warnings": sum(x["severity"] == "warning" for x in issues),
        "info": sum(x["severity"] == "info" for x in issues),
        "issues": issues,
    }
    report["status"] = ("fail" if report["errors"] else
                        "pass-with-review" if issues else "pass")
    if dry_run:
        print(json.dumps(report, ensure_ascii=False, indent=2))
        return report
    write_json(p["validation"], report, force=True)
    if verbose:
        print(f"Validation: {report['status']}; {report['errors']} errors")
    return report
