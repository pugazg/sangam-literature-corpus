#!/usr/bin/env python3
from __future__ import annotations
import argparse, json
from pathlib import Path

EXPECTED = [
    ("natrinai",400),("aingurunuru",500),("kuruntokai",401),
    ("akananuru",400),("purananuru",400),("pattuppattu",10),
    ("patirruppattu",80),("paripatal",35),("kalittokai",150),
]

def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))

def validate(root: Path):
    errors = []
    scope = load(root / "research/production/r2-scope.json")
    source = load(root / "manifests/sangam-core-program.json")
    if scope.get("phase") != "R2" or scope.get("schema_version") != "0.4.0":
        errors.append("R2 phase/schema contract mismatch")
    if scope.get("authorization",{}).get("r15a_merge_commit") != "1e6684b09a5e41fc675ea3e07ba8b6a646d35830":
        errors.append("R1.5A merge authorization anchor mismatch")
    actual = [(x.get("work_id"),x.get("records")) for x in scope.get("canonical_scope_order",[])]
    source_actual = [(x.get("work_slug"),x.get("records")) for x in source.get("works",[])]
    if actual != EXPECTED or source_actual != EXPECTED:
        errors.append("nine-work canonical scope/order/count drifted")
    if scope.get("frozen_work_count") != 9 or scope.get("frozen_record_count") != 2376:
        errors.append("frozen R2 totals drifted")
    if scope.get("new_review_record_count") != 1976:
        errors.append("new-review total must exclude carried-forward Purananuru 400")
    if scope.get("canonical_dimension_count") != 29:
        errors.append("R2 must retain exact 29 dimensions")
    if scope.get("completed_foundation") != {"work_id":"purananuru","records":400,"policy":"carry_forward_without_re_review"}:
        errors.append("Purananuru carry-forward boundary drifted")
    if scope.get("active_work_id") != "kuruntokai" or scope.get("benchmark_range") != [1,2] or scope.get("stabilization_range") != [3,10]:
        errors.append("Kuruntokai benchmark/stabilization boundary drifted")
    for key in ("auto_classify_from_tolkappiyam","cross_corpus_entity_resolution","external_historical_evidence","frozen_corpus_mutation_allowed"):
        if scope.get(key) is not False:
            errors.append(f"{key} must remain false in R2")
    schema = load(root / "research/schemas/core-sangam-production-review-r2.schema.json")
    if schema.get("properties",{}).get("dimensions_considered",{}).get("const") != 29:
        errors.append("R2 record schema dimension count drifted")
    return {"phase":"R2","gate":"scope-and-contract","works":9,"records":2376,"new_review_records":1976,"dimensions":29,"errors":errors,"status":"pass" if not errors else "fail"}

def main():
    p=argparse.ArgumentParser(); p.add_argument("--root",default="."); args=p.parse_args()
    report=validate(Path(args.root).resolve()); print(json.dumps(report,ensure_ascii=False,indent=2))
    raise SystemExit(0 if report["status"]=="pass" else 1)

if __name__=="__main__": main()
