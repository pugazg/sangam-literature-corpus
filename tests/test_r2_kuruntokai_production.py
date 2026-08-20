import importlib.util
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
SPEC=importlib.util.spec_from_file_location("kr2",ROOT/"scripts/validate_r2_kuruntokai_production.py")
MOD=importlib.util.module_from_spec(SPEC);SPEC.loader.exec_module(MOD)
def test_kuruntokai_r2_completion():
    r=MOD.validate(ROOT);assert r["status"]=="pass",r["errors"];assert r["dimensions"]==29
    if r["records_reviewed"]:
        assert r["records_reviewed"]==401
        assert r["records_remaining"]==0
        assert r["next_record"] is None
        assert r["observations_checked"]==4540
