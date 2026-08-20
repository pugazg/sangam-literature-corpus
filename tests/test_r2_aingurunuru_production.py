import importlib.util
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
SPEC=importlib.util.spec_from_file_location("r2poem",ROOT/"scripts/validate_r2_poem_production.py")
MOD=importlib.util.module_from_spec(SPEC);SPEC.loader.exec_module(MOD)
def test_aingurunuru_r2_complete():
    r=MOD.validate(ROOT,"aingurunuru",500)
    assert r["status"]=="pass",r["errors"]
    assert r["dimensions"]==29
    assert r["records_reviewed"]==500
    assert r["records_remaining"]==0
    assert r["next_record"] is None
    assert r["observations_checked"]==2461
    for n in (129,130):
        record=__import__("json").loads((ROOT/f"research/production/aingurunuru/records/{n:03d}.json").read_text(encoding="utf-8"))
        assert record["source_snapshot"]["textual_status"]=="lost"
        assert record["source_snapshot"]["canonical_text_available"] is False
        assert len(record["observations"])==1
