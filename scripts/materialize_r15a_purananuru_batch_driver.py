#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import tempfile
from pathlib import Path

import yaml

import materialize_r15a_purananuru_batch as core

AUDIT_DIR = "research/audits/r15-premerge/purananuru/parts"
_EMPTY_SHA256 = hashlib.sha256(b"").hexdigest()
_ORIGINAL_LOAD_R0 = core.load_r0
_BLANK_THURAI_RECORDS: set[str] = set()
_UNKNOWN_POET_RECORDS: dict[str, str] = {}
_UNKNOWN_POET_VALUES = {
    "பெயர் தெரிந்திலது",
    "பெயர் புலனாகவில்லை",
}


def audit_path_for_record(record_id: str) -> str:
    n = int(record_id)
    if not 1 <= n <= 400:
        raise ValueError(f"record id out of Puṟanāṉūṟu audit range: {record_id}")
    start = ((n - 1) // 50) * 50 + 1
    end = min(start + 49, 400)
    return f"{AUDIT_DIR}/{start:03d}-{end:03d}.tsv"


def parse_record_compat(path: Path):
    """Preserve frozen source states that the core parser historically assumed away."""
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        raise ValueError(f"{path}: missing YAML frontmatter")
    _, rest = text.split("---\n", 1)
    front_text, rest = rest.split("\n---\n", 1)
    front = yaml.safe_load(front_text)

    marker = "\n## Source note (as printed)\n"
    if marker in rest:
        body_part, note_part = rest.split(marker, 1)
        source_note = note_part.strip()
    else:
        body_part = rest
        source_note = ""

    body_lines = body_part.splitlines()
    while body_lines and not body_lines[0].startswith("# "):
        body_lines.pop(0)
    if body_lines and body_lines[0].startswith("# "):
        body_lines.pop(0)
    body_lines = [line for line in body_lines if line != ""]

    poet_as_printed = front.get("poet_as_printed")
    if poet_as_printed in _UNKNOWN_POET_VALUES:
        _UNKNOWN_POET_RECORDS[path.stem] = poet_as_printed
        front = dict(front)
        # These literal source values explicitly say that the poet's name is
        # unknown. Treat them as absent for core named-entity linking, then
        # restore the exact printed metadata value in the production record.
        front["poet_as_printed"] = None

    if front.get("thurai") == "":
        _BLANK_THURAI_RECORDS.add(path.stem)
        front = dict(front)
        # A blank canonical field has no R0 TURAI_VALUE assertion. Treat it as
        # absent for core linking, then restore the exact blank value in output.
        front["thurai"] = None

    return front, body_lines, source_note


def load_r0_compat(path: Path):
    rows = _ORIGINAL_LOAD_R0(path)
    if (
        rows
        and rows[0].get("source_note_sha256") == _EMPTY_SHA256
        and not any(row.get("source_field") == "source_note" for row in rows)
    ):
        # In-memory guard only. The sentinel is not persisted, has no assertion
        # id, and cannot participate in AUTO_R0_TYPES or semantic classification.
        rows = list(rows)
        rows.append(
            {
                "assertion_type": "__NO_PRINTED_SOURCE_NOTE__",
                "source_field": "source_note",
                "source_text": "",
            }
        )
    return rows


def _write_record(path: Path, data: dict) -> None:
    path.write_text(
        json.dumps(data, ensure_ascii=False, separators=(",", ":")) + "\n",
        encoding="utf-8",
    )


def _restore_blank_thurai(root: Path, grouped_records: dict[str, dict]) -> None:
    for record_id in sorted(_BLANK_THURAI_RECORDS.intersection(grouped_records)):
        path = root / "research/production/purananuru/records" / f"{record_id}.json"
        data = json.loads(path.read_text(encoding="utf-8"))
        data["source_metadata_reviewed"]["thurai_as_printed"] = ""
        _write_record(path, data)


def _restore_unknown_poet(root: Path, grouped_records: dict[str, dict]) -> None:
    for record_id in sorted(set(_UNKNOWN_POET_RECORDS).intersection(grouped_records)):
        path = root / "research/production/purananuru/records" / f"{record_id}.json"
        data = json.loads(path.read_text(encoding="utf-8"))
        data["source_metadata_reviewed"]["poet_as_printed"] = _UNKNOWN_POET_RECORDS[record_id]
        _write_record(path, data)


def materialize(root: Path, spec_path: Path) -> None:
    spec = json.loads(spec_path.read_text(encoding="utf-8"))
    records = spec.get("records", {})
    if not records:
        raise ValueError(f"{spec_path}: no records")

    groups: dict[str, dict[str, dict]] = {}
    for record_id, cfg in sorted(records.items()):
        groups.setdefault(audit_path_for_record(record_id), {})[record_id] = cfg

    core.parse_record = parse_record_compat
    core.load_r0 = load_r0_compat

    for audit_path, grouped_records in groups.items():
        core.AUDIT = audit_path
        grouped_spec = {
            "schema_version": spec.get("schema_version", "0.1.0"),
            "batch_id": f"{spec.get('batch_id', spec_path.stem)}-{Path(audit_path).stem}",
            "records": grouped_records,
        }
        with tempfile.NamedTemporaryFile(
            mode="w", encoding="utf-8", suffix=".json", dir=root, delete=False
        ) as handle:
            json.dump(grouped_spec, handle, ensure_ascii=False, separators=(",", ":"))
            temp_path = Path(handle.name)
        try:
            core.materialize(root, temp_path)
            _restore_blank_thurai(root, grouped_records)
            _restore_unknown_poet(root, grouped_records)
        finally:
            temp_path.unlink(missing_ok=True)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default=".")
    parser.add_argument("--spec", required=True)
    args = parser.parse_args()
    root = Path(args.root).resolve()
    materialize(root, (root / args.spec).resolve())


if __name__ == "__main__":
    main()
