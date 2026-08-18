#!/usr/bin/env python3
"""Validate the exhaustive R1.5 pre-merge matrix audit without editing corpus data."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
from collections import Counter
from pathlib import Path

AUDIT = Path("research/audits/r15-premerge")
PART_RANGES = [(1, 50), (51, 100), (101, 150), (151, 200), (201, 250), (251, 300), (301, 350), (351, 400)]
EVIDENCE_RE = re.compile(r"^iyal(\d+):nurpa(\d+)$")
ALLOWED_TOLK_PRESENCE = {"SYSTEMATIC_FORMAL_FRAMEWORK", "EXPLICIT_FORMAL_SUPPORT", "FORMAL_SCOPE_LIMITED"}


def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def git_blob_sha(path: Path) -> str:
    data = path.read_bytes()
    header = f"blob {len(data)}\0".encode("ascii")
    return hashlib.sha1(header + data).hexdigest()


def validate(root: Path) -> dict:
    errors: list[str] = []
    warnings: list[str] = []
    audit_root = root / AUDIT

    dims = load_json(audit_root / "dimensions.json")
    dim_rows = dims.get("dimensions", [])
    dim_ids = [row["id"] for row in dim_rows]
    code_to_id = {row["code"]: row["id"] for row in dim_rows}
    if dims.get("dimension_count") != 29 or len(dim_rows) != 29 or len(set(dim_ids)) != 29:
        errors.append("dimension registry must contain exactly 29 unique dimensions")

    poem_rows: dict[int, list[str]] = {}
    for start, end in PART_RANGES:
        part = audit_root / "purananuru" / "parts" / f"{start:03d}-{end:03d}.tsv"
        if not part.exists():
            errors.append(f"missing Puṟanāṉūṟu audit part: {part.relative_to(root)}")
            continue
        with part.open(encoding="utf-8", newline="") as fh:
            reader = csv.DictReader(fh, delimiter="\t")
            if reader.fieldnames != ["record_id", "qualifying_dimension_codes"]:
                errors.append(f"unexpected TSV header in {part.relative_to(root)}")
                continue
            seen_here = []
            for row in reader:
                record_id = int(row["record_id"])
                seen_here.append(record_id)
                if record_id in poem_rows:
                    errors.append(f"duplicate Puṟanāṉūṟu audit record {record_id}")
                codes = row["qualifying_dimension_codes"].split()
                unknown = [code for code in codes if code not in code_to_id]
                if unknown:
                    errors.append(f"record {record_id} has unknown dimension codes: {unknown}")
                if "LD" not in codes:
                    errors.append(f"record {record_id} lacks reviewed work-level literary-domain classification")
                poem_rows[record_id] = codes
            if seen_here != list(range(start, end + 1)):
                errors.append(f"{part.relative_to(root)} does not contain the exact ordered range {start}-{end}")

    if sorted(poem_rows) != list(range(1, 401)):
        errors.append("Puṟanāṉūṟu audit must cover each record 1-400 exactly once")

    for special in (200, 267, 268):
        if poem_rows.get(special) != ["LD"]:
            errors.append(f"Puṟanāṉūṟu special record {special} must not receive reconstructed body dimensions")

    computed_counts = Counter(code_to_id[code] for codes in poem_rows.values() for code in codes if code in code_to_id)
    psummary = load_json(audit_root / "purananuru" / "dimension-summary.json")
    if psummary.get("records_reviewed") != 400 or psummary.get("dimensions_considered_per_record") != 29:
        errors.append("Puṟanāṉūṟu summary must declare 400 records × 29 dimensions reviewed")
    if psummary.get("source_lost_records") != [267, 268]:
        errors.append("Puṟanāṉūṟu source-lost boundary must remain 267-268")
    if psummary.get("damaged_or_unreadable_records") != [200]:
        errors.append("Puṟanāṉūṟu damaged audit boundary must explicitly retain record 200")
    if dict(computed_counts) != psummary.get("dimension_record_counts"):
        errors.append("Puṟanāṉūṟu dimension counts do not match the eight reviewed TSV parts")
    psource = root / psummary["source_path"]
    if git_blob_sha(psource) != psummary.get("source_blob_sha"):
        errors.append("Puṟanāṉūṟu frozen consolidated-source blob SHA drifted")

    tmanifest = load_json(audit_root / "tolkappiyam" / "review-manifest.json")
    tiyals = tmanifest.get("iyals", [])
    if tmanifest.get("records_reviewed") != 1602 or tmanifest.get("dimensions_considered_per_record") != 29:
        errors.append("Tolkāppiyam manifest must declare 1,602 நூற்பா × 29 dimensions reviewed")
    if tmanifest.get("auto_classify_sangam_poems") is not False:
        errors.append("Tolkāppiyam evidence must never auto-classify Sangam poems")
    if len(tiyals) != 27 or [row.get("iyal") for row in tiyals] != list(range(1, 28)):
        errors.append("Tolkāppiyam audit manifest must contain exact iyal order 1-27")

    expected_sequence = 1
    expanded_count = 0
    iyal_by_id = {}
    for row in tiyals:
        iyal = row["iyal"]
        count = row["record_count"]
        start = row["source_sequence_start"]
        end = row["source_sequence_end"]
        iyal_by_id[iyal] = row
        if start != expected_sequence or end - start + 1 != count:
            errors.append(f"Tolkāppiyam iyal {iyal} has a non-contiguous or inconsistent source-sequence range")
        expected_sequence = end + 1
        expanded_count += count
    if expanded_count != 1602 or expected_sequence != 1603:
        errors.append("Tolkāppiyam 27-iyal manifest does not expand exactly to source sequences 1-1602")

    tsource = root / tmanifest["source_path"]
    if git_blob_sha(tsource) != tmanifest.get("source_blob_sha"):
        errors.append("Tolkāppiyam frozen consolidated-source blob SHA drifted")

    crosswalk = load_json(audit_root / "tolkappiyam" / "dimension-crosswalk.json")
    xrows = crosswalk.get("dimensions", [])
    xids = [row.get("id") for row in xrows]
    if crosswalk.get("dimension_count") != 29 or xids != dim_ids:
        errors.append("Tolkāppiyam dimension crosswalk must match the controlled 29-dimension registry in order")
    for row in xrows:
        if row.get("presence") not in ALLOWED_TOLK_PRESENCE:
            errors.append(f"invalid Tolkāppiyam presence level for {row.get('id')}")
        refs = row.get("evidence", [])
        if not refs:
            errors.append(f"Tolkāppiyam dimension {row.get('id')} lacks representative formal evidence")
        for ref in refs:
            match = EVIDENCE_RE.match(ref)
            if not match:
                errors.append(f"invalid Tolkāppiyam evidence reference: {ref}")
                continue
            iyal, local = map(int, match.groups())
            meta = iyal_by_id.get(iyal)
            if not meta or local < 1 or local > meta["record_count"]:
                errors.append(f"out-of-range Tolkāppiyam evidence reference: {ref}")

    status_counts = Counter(row.get("presence") for row in xrows)
    if dict(status_counts) != crosswalk.get("status_counts"):
        errors.append("Tolkāppiyam crosswalk status counts do not match its entries")

    return {
        "audit_schema_version": "0.1.0",
        "gate": "r15_premerge_exhaustive_matrix_audit",
        "dimension_count": len(dim_rows),
        "purananuru_records_reviewed": len(poem_rows),
        "purananuru_dimension_counts": dict(computed_counts),
        "purananuru_source_lost_records": [267, 268],
        "tolkappiyam_iyals_reviewed": len(tiyals),
        "tolkappiyam_nurpas_reviewed": expanded_count,
        "tolkappiyam_crosswalk_dimensions": len(xrows),
        "tolkappiyam_crosswalk_status_counts": dict(status_counts),
        "tolkappiyam_auto_classify_sangam_poems": tmanifest.get("auto_classify_sangam_poems"),
        "errors": errors,
        "warnings": warnings,
        "status": "pass" if not errors else "fail",
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default=".")
    parser.add_argument("--output")
    args = parser.parse_args()
    result = validate(Path(args.root).resolve())
    rendered = json.dumps(result, ensure_ascii=False, indent=2) + "\n"
    if args.output:
        output = Path(args.output)
        if not output.is_absolute():
            output = Path(args.root) / output
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(rendered, encoding="utf-8")
    print(rendered, end="")
    return 0 if result["status"] == "pass" else 1


if __name__ == "__main__":
    raise SystemExit(main())
