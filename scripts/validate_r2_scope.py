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
    if scope.get("active_work_id") != "kalittokai" or scope.get("next_record") != "kalittokai-003" or scope.get("next_batch") != [3,10] or scope.get("benchmark_range") != [1,2] or scope.get("stabilization_range") != [3,10]:
        errors.append("Kalittokai benchmark/stabilization boundary drifted")
    completed = scope.get("completed_works", [])
    if not any(x.get("work_id") == "kuruntokai" and x.get("records") == 401 and x.get("observations") == 4540 for x in completed):
        errors.append("Kuruntokai completion boundary missing")
    if not any(x.get("work_id") == "natrinai" and x.get("records") == 400 and x.get("observations") == 6007 for x in completed):
        errors.append("Natrinai completion boundary missing")
    if not any(x.get("work_id") == "aingurunuru" and x.get("records") == 500 and x.get("observations") == 2461 and x.get("lost_records") == [129,130] for x in completed):
        errors.append("Aingurunuru completion boundary missing")
    if not any(x.get("work_id") == "akananuru" and x.get("records") == 400 and x.get("observations") == 4840 for x in completed):
        errors.append("Akananuru completion boundary missing")
    for key in ("auto_classify_from_tolkappiyam","cross_corpus_entity_resolution","external_historical_evidence","frozen_corpus_mutation_allowed"):
        if scope.get(key) is not False:
            errors.append(f"{key} must remain false in R2")
    architecture = load(root / "research/production/programmes/architecture.json")
    collections = {x.get("collection_id"): x for x in architecture.get("collections", [])}
    expected_collection_counts = {"ettuttokai": 8, "pattuppattu": 10, "patinenkilkanakku": 18}
    if {k: collections.get(k, {}).get("unit_count") for k in expected_collection_counts} != expected_collection_counts:
        errors.append("8 + 10 + 18 programme architecture count mismatch")
    units = architecture.get("units", [])
    if len(units) != 36 or len({x.get("folder") for x in units}) != 36:
        errors.append("programme work units/folders must be 36 unique entries")
    for unit in units:
        if not (root / unit.get("folder", "") / "README.md").is_file():
            errors.append(f"missing independent production folder: {unit.get('folder')}")
    pattuppattu = [x for x in units if x.get("collection_id") == "pattuppattu"]
    if [x.get("source_record") for x in pattuppattu] != [f"{n:03d}" for n in range(1, 11)]:
        errors.append("Pattuppattu must expose ten ordered independent long-work units")
    if scope.get("r2_operational_work_units") != 18 or scope.get("pattuppattu_production_policy") != "ten_independent_long_work_units":
        errors.append("R2 operational split must be 8 Ettuttokai + 10 Pattuppattu units")
    if scope.get("post_core_plan") != {"collection_id":"patinenkilkanakku","work_units":18,"status":"planned_not_activated"}:
        errors.append("Patinenkilkanakku 18-work plan boundary mismatch")
    schema = load(root / "research/schemas/core-sangam-production-review-r2.schema.json")
    if schema.get("properties",{}).get("dimensions_considered",{}).get("const") != 29:
        errors.append("R2 record schema dimension count drifted")
    return {"phase":"R2","gate":"scope-and-contract","source_containers":9,"operational_work_units":18,"planned_post_core_units":18,"records":2376,"new_review_records":1976,"dimensions":29,"errors":errors,"status":"pass" if not errors else "fail"}

def main():
    p=argparse.ArgumentParser(); p.add_argument("--root",default="."); args=p.parse_args()
    report=validate(Path(args.root).resolve()); print(json.dumps(report,ensure_ascii=False,indent=2))
    raise SystemExit(0 if report["status"]=="pass" else 1)

if __name__=="__main__": main()
