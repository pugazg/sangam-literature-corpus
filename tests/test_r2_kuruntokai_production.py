import importlib.util
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
SPEC=importlib.util.spec_from_file_location("kr2",ROOT/"scripts/validate_r2_kuruntokai_production.py")
MOD=importlib.util.module_from_spec(SPEC);SPEC.loader.exec_module(MOD)
def test_kuruntokai_r2_stabilization():
    r=MOD.validate(ROOT);assert r["status"]=="pass",r["errors"];assert r["dimensions"]==29
    if r["records_reviewed"]:
        assert r["records_reviewed"]==10
        assert r["next_record"]=="kuruntokai-011"
        assert r["observations_checked"]==114
