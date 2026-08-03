#!/usr/bin/env python3
"""Run two Tolkāppiyam regenerations and compare deterministic outputs."""
from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import os
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TRACKED = [ROOT / "corpus/tolkappiyam", ROOT / "sources/raw-txt/tolkappiyam.txt", ROOT / "sources/source-metadata", ROOT / "manifests/records.csv", ROOT / "manifests/tolkappiyam-validation-report.json"]


def snapshot() -> dict[str, str]:
    result = {}
    for base in TRACKED:
        paths = [base] if base.is_file() else sorted(base.rglob("*")) if base.exists() else []
        for path in paths:
            if path.is_file() and ("tolkappiyam" in path.name or "tolkappiyam" in path.as_posix() or path.name == "records.csv"):
                result[str(path.relative_to(ROOT))] = hashlib.sha256(path.read_bytes()).hexdigest()
    return result


def delta(before: dict, after: dict) -> dict:
    return {"path_additions": sorted(set(after)-set(before)), "path_removals": sorted(set(before)-set(after)), "hash_changes": sorted(key for key in before.keys()&after.keys() if before[key]!=after[key])}


def main() -> None:
    parser=argparse.ArgumentParser();parser.add_argument("--freeze",action="store_true");args=parser.parse_args();env=os.environ|{"PYTHONDONTWRITEBYTECODE":"1"}
    initial=snapshot();cmd=[sys.executable,"scripts/tolkappiyam_pipeline.py","process"]+( ["--freeze"] if args.freeze else [] )
    subprocess.run(cmd,cwd=ROOT,env=env,check=True,stdout=subprocess.DEVNULL);first=snapshot()
    subprocess.run(cmd,cwd=ROOT,env=env,check=True,stdout=subprocess.DEVNULL);second=snapshot()
    d1,d2=delta(initial,first),delta(first,second);status="pass" if not any(d1.values()) and not any(d2.values()) else "fail"
    now=dt.datetime.now().astimezone();result={"created_at":now.isoformat(),"mode":"frozen" if args.freeze else "unfrozen","first_regeneration":d1,"second_regeneration":d2,"status":status}
    target=ROOT/"logs"/f"tolkappiyam-{'freeze-' if args.freeze else ''}idempotence-{now.strftime('%Y%m%dT%H%M%S')}.json";target.write_text(json.dumps(result,ensure_ascii=False,indent=2)+"\n",encoding="utf-8",newline="\n")
    print(json.dumps(result|{"log_path":str(target.relative_to(ROOT))},indent=2))
    if status!="pass":raise SystemExit(1)


if __name__=="__main__":main()
