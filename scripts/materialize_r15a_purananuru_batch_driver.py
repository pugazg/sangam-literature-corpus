#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import tempfile
from pathlib import Path

import materialize_r15a_purananuru_batch as core

AUDIT_DIR = "research/audits/r15-premerge/purananuru/parts"


def audit_path_for_record(record_id: str) -> str:
    n = int(record_id)
    if not 1 <= n <= 400:
        raise ValueError(f"record id out of Puṟanāṉūṟu audit range: {record_id}")
    start = ((n - 1) // 50) * 50 + 1
    end = min(start + 49, 400)
    return f"{AUDIT_DIR}/{start:03d}-{end:03d}.tsv"


def materialize(root: Path, spec_path: Path) -> None:
    spec = json.loads(spec_path.read_text(encoding="utf-8"))
    records = spec.get("records", {})
    if not records:
        raise ValueError(f"{spec_path}: no records")

    groups: dict[str, dict[str, dict]] = {}
    for record_id, cfg in sorted(records.items()):
        groups.setdefault(audit_path_for_record(record_id), {})[record_id] = cfg

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
