#!/usr/bin/env python3
"""Recursive physical repository audit; never mutates repository content."""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

import yaml

WORKS = {
    "natrinai": ({f"{n:03d}.md" for n in range(1, 401)}, {f"{n:03d}-{n+49:03d}.md" for n in range(1, 401, 50)}),
    "aingurunuru": ({f"{n:03d}.md" for n in range(1, 501)}, {f"{n:03d}-{n+9:03d}.md" for n in range(1, 501, 10)}),
    "kuruntokai": ({f"{n:03d}.md" for n in range(1, 402)},
                    {f"{n:03d}-{min(n+49,401):03d}.md" for n in range(1, 402, 50)}),
    "akananuru": ({f"{n:03d}.md" for n in range(1, 401)},
                   {"001-120.md", "121-300.md", "301-400.md"}),
    "purananuru": ({f"{n:03d}.md" for n in range(1, 401)},
                    {f"{n:03d}-{n+49:03d}.md" for n in range(1, 401, 50)}),
    "pattuppattu": ({f"{n:03d}.md" for n in range(1, 11)},
                     {"001-pmuni0067.md", "002-pmuni0063.md", "003-pmuni0064.md",
                      "004-pmuni0069.md", "005-pmuni0488.md", "006-pmuni0071.md",
                      "007-pmuni0070.md", "008-pmuni0073.md", "009-pmuni0077.md",
                      "010-pmuni0078.md"}),
    "patirruppattu": ({f"{n:03d}.md" for n in range(11, 91)},
                       {f"{g:02d}-{(g-1)*10+1:03d}-{g*10:03d}.md" for g in range(2, 10)}),
    "paripatal": ({f"{n:03d}.md" for n in range(1, 36)},
                   {"01-paripatal.md", "02-paripatal-tirattu.md"}),
    "kalittokai": ({f"{n:03d}.md" for n in range(1, 151)},
                    {"01-invocation.md", "02-palaikkali.md", "03-kurinji.md",
                     "04-marutakkali.md", "05-mullaikkali.md", "06-neytalkali.md"}),
    "tirukkural": ({f"{n:04d}.md" for n in range(1, 1331)},
                    {f"{c:03d}-{(c-1)*10+1:04d}-{c*10:04d}.md"
                     for c in range(1, 134)}),
    "naladiyar": ({f"{n:03d}.md" for n in range(1, 401)},
                   {f"{c:03d}-{(c-1)*10+1:03d}-{c*10:03d}.md"
                    for c in range(1, 41)}),
    "nanmanikkadigai": ({f"{n:03d}.md" for n in range(1, 107)},
                         {"01-invocation.md", "02-nul.md"}),
    "inna-narpathu": ({f"{n:03d}.md" for n in range(1, 41)},
                       {"01-invocation.md", "02-nul.md"}),
    "iniyavai-narpathu": ({f"{n:03d}.md" for n in range(1, 41)},
                           {"01-invocation.md", "02-nul.md"}),
    "kar-narpathu": ({f"{n:03d}.md" for n in range(1, 41)},
                      {"001-040.md"}),
    "kalavazhi-narpathu": ({f"{n:03d}.md" for n in range(1, 41)},
                            {"001-040.md"}),
    "aintinai-aimpathu": ({f"{n:03d}.md" for n in range(1, 51)},
                           {"01-mullai.md","02-kurinji.md","03-marutam.md","04-palai.md","05-neytal.md"}),
    "aintinai-elupathu": ({f"{n:03d}.md" for n in range(1, 71)},
                           {"01-kurinji.md","02-mullai.md","03-palai.md","04-marutam.md","05-neytal.md"}),
    "thinaimalai-nutraimbathu": ({f"{n:03d}.md" for n in range(1, 154)},
                                  {"01-kurinji.md","02-neytal.md","03-palai.md","04-mullai.md","05-marutam.md"}),
    "thinaimozhi-aimpathu":({f"{n:03d}.md" for n in range(1,51)},
                             {f"{i:02d}-{(i-1)*10+1:03d}-{i*10:03d}.md" for i in range(1,6)}),
    "tirikatukam":({f"{n:03d}.md" for n in range(1,101)},{"001-100.md"}),
    "acharakkovai":({f"{n:03d}.md" for n in range(1,101)},{"001-100.md"}),
    "pazhamozhi-nanuru":({f"{n:03d}.md" for n in range(1,400)},
                          {"01-001-010.md","02-011-016.md","03-017-025.md","04-026-033.md",
                           "05-034-042.md","06-043-050.md","07-051-059.md","08-060-064.md",
                           "09-065-068.md","10-069-080.md","11-081-106.md","13-107-123.md",
                           "14-124-134.md","15-135-141.md","16-142-148.md","17-149-161.md",
                           "18-162-176.md","19-177-182.md","20-183-195.md","21-196-204.md",
                           "22-205-212.md","23-213-226.md","24-227-240.md","25-241-257.md",
                           "26-258-265.md","27-266-284.md","28-285-310.md","29-311-326.md",
                           "30-327-347.md","31-348-356.md","32-357-371.md","33-372-386.md",
                           "34-387-399.md"}),
    "sirupanchamulam":({f"{n:03d}.md" for n in range(1,99)},{"01-prefatory.md","02-nul.md"}),
    "muthumozhi-kanchi":({f"{n:03d}.md" for n in range(1,101)},
                          {f"{i:02d}-{(i-1)*10+1:03d}-{i*10:03d}.md" for i in range(1,11)}),
    "elati":({f"{n:03d}.md" for n in range(1,81)},{"001-080.md"}),
    "kainnilai":({f"{n:03d}.md" for n in range(1,61)},
                  {"01-001-012.md","02-013-024.md","03-025-036.md","04-037-060.md"}),
}
EXPECTED_POEMS, EXPECTED_SECTIONS = WORKS["natrinai"]
COPY_RE = re.compile(r"^(.+?) ([2-9]\d*)\.md$")
CLUTTER_NAMES = {".DS_Store", "__pycache__", ".pytest_cache"}
CLUTTER_SUFFIXES = (".pyc", ".pyo", ".bak", ".tmp")


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def yaml_poem_number_bytes(raw: bytes) -> int | None:
    try:
        text = raw.decode("utf-8")
        parts = text.split("---", 2)
        if len(parts) != 3:
            return None
        value = yaml.safe_load(parts[1]).get("poem_number")
        return int(value) if value is not None else None
    except Exception:
        return None


def audit(root: Path) -> dict:
    root = root.resolve()
    reports={}; all_identical=[]; all_conflicting=[]; overall_fail=False
    for work,(expected_poems,expected_sections) in WORKS.items():
        corpus=root/"corpus"/work
        if not corpus.exists():
            if work in {"aingurunuru", "kuruntokai", "akananuru"}: continue
            reports[work]={"status":"fail","reason":"missing corpus directory"}; overall_fail=True; continue
        poems=corpus/"poems"; sections=corpus/"sections"
        poem_files=sorted(x for x in poems.rglob("*") if x.is_file()); poem_md=[x for x in poem_files if x.suffix==".md"]
        section_files=sorted(x for x in sections.rglob("*") if x.is_file()); section_md=[x for x in section_files if x.suffix==".md"]
        readable=poem_md+section_md
        with ThreadPoolExecutor(max_workers=64) as pool: raw=dict(zip(readable,pool.map(lambda x:x.read_bytes(),readable)))
        direct={x.name for x in poem_md if x.parent==poems}; unexpected=sorted(str(x.relative_to(poems)) for x in poem_files if x.parent!=poems or x.name not in expected_poems); missing=sorted(expected_poems-direct)
        bynum=defaultdict(list)
        for x in poem_md:
            n=yaml_poem_number_bytes(raw[x])
            if n is not None: bynum[n].append(str(x.relative_to(root)))
        dup={str(n):v for n,v in sorted(bynum.items()) if len(v)>1}
        identical=[]; conflicting=[]
        for x in readable:
            m=COPY_RE.match(x.name)
            if not m: continue
            canonical=x.with_name(m.group(1)+".md"); rec={"copy":str(x.relative_to(root)),"canonical":str(canonical.relative_to(root)),"copy_bytes":x.stat().st_size,"canonical_exists":canonical.exists()}
            if canonical.exists(): rec.update({"canonical_bytes":canonical.stat().st_size,"copy_sha256":hashlib.sha256(raw[x]).hexdigest(),"canonical_sha256":hashlib.sha256(raw.get(canonical,canonical.read_bytes())).hexdigest()})
            (identical if canonical.exists() and rec["copy_sha256"]==rec["canonical_sha256"] else conflicting).append(rec)
        sdirect={x.name for x in section_md if x.parent==sections}; sunexpected=sorted(str(x.relative_to(sections)) for x in section_files if x.parent!=sections or x.name not in expected_sections); smissing=sorted(expected_sections-sdirect)
        fail=bool(len(poem_md)!=len(expected_poems) or unexpected or missing or dup or identical or conflicting or len(section_md)!=len(expected_sections) or sunexpected or smissing)
        reports[work]={"poem_markdown_count":len(poem_md),"expected_poem_filenames":len(expected_poems),"missing_poem_filenames":missing,"unexpected_poem_filenames":unexpected,"duplicate_yaml_poem_numbers":dup,"section_markdown_count":len(section_md),"expected_section_count":len(expected_sections),"missing_section_filenames":smissing,"unexpected_section_filenames":sunexpected,"status":"fail" if fail else "pass"}
        all_identical+=identical; all_conflicting+=conflicting; overall_fail|=fail
    all_files=sorted(p for p in root.rglob("*") if p.is_file())
    clutter = sorted(str(p.relative_to(root)) for p in root.rglob("*") if (p.relative_to(root).parts and p.relative_to(root).parts[0] == "quarantine") or p.name in CLUTTER_NAMES or (p.is_file() and p.name.endswith(CLUTTER_SUFFIXES)) or (p.is_file() and any(tag in p.name for tag in ("-old.md", "-copy.md"))))
    overall_fail|=bool(clutter)
    result={"resolved_physical_root":str(root),"total_files":len(all_files),"works":reports,"sha256_identical_copies":all_identical,"conflicting_copies":all_conflicting,"cache_backup_temporary_files":clutter,"status":"fail" if overall_fail else "pass"}
    # Backward-compatible Naṟṟiṇai summary fields retained for existing tests/tools.
    if "natrinai" in reports:
        n=reports["natrinai"]; result.update({"poem_markdown_count":n["poem_markdown_count"],"expected_poem_filenames":n["expected_poem_filenames"],"missing_poem_filenames":n["missing_poem_filenames"],"unexpected_poem_filenames":n["unexpected_poem_filenames"],"duplicate_yaml_poem_numbers":n["duplicate_yaml_poem_numbers"],"section_markdown_count":n["section_markdown_count"],"missing_section_filenames":n["missing_section_filenames"],"unexpected_section_filenames":n["unexpected_section_filenames"]})
    return result

    # Legacy single-work implementation retained below only as unreachable
    # context for old line-oriented tooling.
    poems = root / "corpus/natrinai/poems"
    sections = root / "corpus/natrinai/sections"
    all_files = sorted(p for p in root.rglob("*") if p.is_file())
    poem_files = sorted(p for p in poems.rglob("*") if p.is_file()) if poems.exists() else []
    poem_md = [p for p in poem_files if p.suffix == ".md"]
    section_files = sorted(p for p in sections.rglob("*") if p.is_file()) if sections.exists() else []
    section_md = [p for p in section_files if p.suffix == ".md"]
    readable = poem_md + section_md
    with ThreadPoolExecutor(max_workers=64) as pool:
        raw_by_path = dict(zip(readable, pool.map(lambda path: path.read_bytes(), readable)))
    direct_poem_names = {p.name for p in poem_md if p.parent == poems}
    unexpected_poems = sorted(str(p.relative_to(poems)) for p in poem_files
                              if p.parent != poems or p.name not in EXPECTED_POEMS)
    missing_poems = sorted(EXPECTED_POEMS - direct_poem_names)

    by_number: dict[int, list[str]] = defaultdict(list)
    for path in poem_md:
        number = yaml_poem_number_bytes(raw_by_path[path])
        if number is not None:
            by_number[number].append(str(path.relative_to(root)))
    duplicate_numbers = {str(k): v for k, v in sorted(by_number.items()) if len(v) > 1}

    identical, conflicting = [], []
    for path in poem_md + ([p for p in sections.rglob("*.md")] if sections.exists() else []):
        match = COPY_RE.match(path.name)
        if not match:
            continue
        canonical = path.with_name(match.group(1) + ".md")
        record = {
            "copy": str(path.relative_to(root)),
            "canonical": str(canonical.relative_to(root)),
            "copy_bytes": path.stat().st_size,
            "canonical_exists": canonical.exists(),
        }
        if canonical.exists():
            record.update({"canonical_bytes": canonical.stat().st_size,
                           "copy_sha256": hashlib.sha256(raw_by_path[path]).hexdigest(),
                           "canonical_sha256": hashlib.sha256(raw_by_path[canonical] if canonical in raw_by_path else canonical.read_bytes()).hexdigest()})
        if canonical.exists() and record["copy_sha256"] == record["canonical_sha256"]:
            identical.append(record)
        else:
            conflicting.append(record)

    direct_section_names = {p.name for p in section_md if p.parent == sections}
    unexpected_sections = sorted(str(p.relative_to(sections)) for p in section_files
                                 if p.parent != sections or p.name not in EXPECTED_SECTIONS)
    missing_sections = sorted(EXPECTED_SECTIONS - direct_section_names)

    clutter = sorted(str(p.relative_to(root)) for p in root.rglob("*")
                     if (p.relative_to(root).parts and p.relative_to(root).parts[0] == "quarantine")
                     or p.name in CLUTTER_NAMES or (p.is_file() and p.name.endswith(CLUTTER_SUFFIXES))
                     or (p.is_file() and any(tag in p.name for tag in ("-old.md", "-copy.md"))))
    failures = bool(len(poem_md) != 400 or unexpected_poems or missing_poems or duplicate_numbers
                    or conflicting or identical or len(section_md) != 8 or unexpected_sections
                    or missing_sections or clutter)
    return {
        "resolved_physical_root": str(root),
        "total_files": len(all_files),
        "poem_markdown_count": len(poem_md),
        "expected_poem_filenames": 400,
        "missing_poem_filenames": missing_poems,
        "unexpected_poem_filenames": unexpected_poems,
        "duplicate_yaml_poem_numbers": duplicate_numbers,
        "sha256_identical_copies": identical,
        "conflicting_copies": conflicting,
        "section_markdown_count": len(section_md),
        "expected_section_filenames": sorted(EXPECTED_SECTIONS),
        "missing_section_filenames": missing_sections,
        "unexpected_section_filenames": unexpected_sections,
        "cache_backup_temporary_files": clutter,
        "status": "fail" if failures else "pass",
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", type=Path, default=Path("."))
    ap.add_argument("--json-out", type=Path)
    args = ap.parse_args()
    report = audit(args.root)
    rendered = json.dumps(report, ensure_ascii=False, indent=2)
    print(rendered)
    if args.json_out:
        args.json_out.parent.mkdir(parents=True, exist_ok=True)
        args.json_out.write_text(rendered + "\n", encoding="utf-8")
    return 0 if report["status"] == "pass" else 1


if __name__ == "__main__":
    sys.exit(main())
