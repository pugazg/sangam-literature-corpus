import importlib.util
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
SPEC=importlib.util.spec_from_file_location("r2poem",ROOT/"scripts/validate_r2_poem_production.py")
MOD=importlib.util.module_from_spec(SPEC);SPEC.loader.exec_module(MOD)
def test_natrinai_r2_completion():
    r=MOD.validate(ROOT,"natrinai",400)
    assert r["status"]=="pass",r["errors"]
    assert r["dimensions"]==29
    assert r["records_reviewed"]==400
    assert r["records_remaining"]==0
    assert r["next_record"] is None
    assert r["observations_checked"]==6007
