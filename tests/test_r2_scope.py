import importlib.util
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
SPEC=importlib.util.spec_from_file_location("r2validator",ROOT/"scripts/validate_r2_scope.py")
MOD=importlib.util.module_from_spec(SPEC); SPEC.loader.exec_module(MOD)

def test_r2_scope_contract_passes():
    report=MOD.validate(ROOT)
    assert report["status"]=="pass", report["errors"]
    assert report["source_containers"]==9
    assert report["operational_work_units"]==18
    assert report["planned_post_core_units"]==18
    assert report["records"]==2376
    assert report["new_review_records"]==1976
    assert report["dimensions"]==29
