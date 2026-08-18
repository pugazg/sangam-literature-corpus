#!/usr/bin/env python3
"""Run and record two deterministic research-layer regeneration passes."""
from __future__ import annotations

import datetime as dt
import hashlib
import json
import os
import subprocess
import sys
from pathlib import Path


def snapshot(root: Path) -> dict[str, str]:
    research = root / "research"
    return {str(path.relative_to(root)): hashlib.sha256(path.read_bytes()).hexdigest() for path in sorted(research.rglob("*")) if path.is_file() and path.name != ".generation.lock"}


def delta(before: dict, after: dict) -> dict:
    return {"path_additions": sorted(set(after) - set(before)), "path_removals": sorted(set(before) - set(after)), "hash_changes": sorted(key for key in before.keys() & after.keys() if before[key] != after[key])}


def main() -> None:
    root = Path(__file__).resolve().parents[1]; env = os.environ | {"PYTHONDONTWRITEBYTECODE": "1"}
    initial = snapshot(root)
    subprocess.run([sys.executable, "scripts/generate_research_layer.py", "--root", "."], cwd=root, env=env, check=True, stdout=subprocess.DEVNULL)
    first = snapshot(root)
    subprocess.run([sys.executable, "scripts/generate_research_layer.py", "--root", "."], cwd=root, env=env, check=True, stdout=subprocess.DEVNULL)
    second = snapshot(root)
    first_delta, second_delta = delta(initial, first), delta(first, second)
    status = "pass" if not any(first_delta.values()) and not any(second_delta.values()) else "fail"
    now = dt.datetime.now().astimezone(); result = {"created_at": now.isoformat(), "first_regeneration": first_delta, "second_regeneration": second_delta, "status": status}
    target = root / "logs" / f"classical-tamil-research-layer-r0-idempotence-{now.strftime('%Y%m%dT%H%M%S')}.json"
    target.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
    print(json.dumps(result | {"log_path": str(target.relative_to(root))}, ensure_ascii=False, indent=2))
    if status != "pass": raise SystemExit(1)


if __name__ == "__main__": main()
