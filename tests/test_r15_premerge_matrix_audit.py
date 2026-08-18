import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
AUDIT = ROOT / "research/audits/r15-premerge"


def load_json(path):
    return json.loads(path.read_text(encoding="utf-8"))


def test_premerge_dimension_registry_is_exactly_29():
    data = load_json(AUDIT / "dimensions.json")
    assert data["dimension_count"] == 29
    assert len(data["dimensions"]) == 29
    assert len({row["id"] for row in data["dimensions"]}) == 29
    assert len({row["code"] for row in data["dimensions"]}) == 29


def test_purananuru_review_is_split_into_exact_400_record_ranges():
    expected = [(1, 50), (51, 100), (101, 150), (151, 200), (201, 250), (251, 300), (301, 350), (351, 400)]
    ids = []
    for start, end in expected:
        part = AUDIT / "purananuru/parts" / f"{start:03d}-{end:03d}.tsv"
        lines = part.read_text(encoding="utf-8").splitlines()
        assert lines[0] == "record_id\tqualifying_dimension_codes"
        local_ids = [int(line.split("\t", 1)[0]) for line in lines[1:]]
        assert local_ids == list(range(start, end + 1))
        ids.extend(local_ids)
    assert ids == list(range(1, 401))


def test_purananuru_source_loss_and_damage_are_not_reconstructed():
    found = {}
    for part in sorted((AUDIT / "purananuru/parts").glob("*.tsv")):
        for line in part.read_text(encoding="utf-8").splitlines()[1:]:
            record, codes = line.split("\t", 1)
            found[int(record)] = codes.split()
    assert found[200] == ["LD"]
    assert found[267] == ["LD"]
    assert found[268] == ["LD"]


def test_tolkappiyam_review_manifest_expands_exactly_to_1602():
    data = load_json(AUDIT / "tolkappiyam/review-manifest.json")
    assert data["records_reviewed"] == 1602
    assert data["dimensions_considered_per_record"] == 29
    assert data["auto_classify_sangam_poems"] is False
    assert [row["iyal"] for row in data["iyals"]] == list(range(1, 28))
    assert sum(row["record_count"] for row in data["iyals"]) == 1602
    expected = 1
    for row in data["iyals"]:
        assert row["source_sequence_start"] == expected
        assert row["source_sequence_end"] - row["source_sequence_start"] + 1 == row["record_count"]
        expected = row["source_sequence_end"] + 1
    assert expected == 1603


def test_tolkappiyam_crosswalk_covers_all_29_dimensions():
    dims = load_json(AUDIT / "dimensions.json")
    crosswalk = load_json(AUDIT / "tolkappiyam/dimension-crosswalk.json")
    assert [row["id"] for row in crosswalk["dimensions"]] == [row["id"] for row in dims["dimensions"]]
    assert all(row["evidence"] for row in crosswalk["dimensions"])
    assert crosswalk["status"] == "all_29_dimensions_have_formal_or_structural_support_with_unequal_depth"


def test_premerge_matrix_audit_validator_passes():
    result = subprocess.run(
        [sys.executable, str(ROOT / "scripts/validate_r15_premerge_matrix_audit.py"), "--root", str(ROOT)],
        cwd=ROOT,
        text=True,
        capture_output=True,
    )
    assert result.returncode == 0, result.stdout + result.stderr
    payload = json.loads(result.stdout)
    assert payload["status"] == "pass"
    assert payload["purananuru_records_reviewed"] == 400
    assert payload["tolkappiyam_nurpas_reviewed"] == 1602
