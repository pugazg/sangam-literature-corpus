import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from validate_r15_tolkappiyam_production import validate  # noqa: E402


class TolkappiyamR15AProductionTests(unittest.TestCase):
    def test_01_schema_and_concept_extension_present(self):
        schema = json.loads(
            (ROOT / "research/schemas/tolkappiyam-production-review-r15.schema.json").read_text(encoding="utf-8")
        )
        self.assertEqual(schema["properties"]["schema_version"]["const"], "0.3.0")
        self.assertEqual(schema["properties"]["dimensions_considered"]["const"], 29)
        extension = json.loads(
            (ROOT / "research/concepts/classical-tamil/tolkappiyam-production-concepts-r15a.json").read_text(encoding="utf-8")
        )
        concepts = {entry["concept_id"]: entry for entry in extension["concepts"]}
        self.assertEqual(concepts["knowledge.grammar.phonology"]["dimension"], "knowledge_technology")

    def test_02_production_validator_passes(self):
        report = validate(ROOT)
        self.assertEqual(report["errors"], [])
        self.assertEqual(report["warnings"], [])
        self.assertEqual(report["canonical_dimension_count"], 29)
        self.assertEqual(report["status"], "pass")

    def test_03_benchmark_if_present_is_source_first_and_formal_only(self):
        record_dir = ROOT / "research/production/tolkappiyam/records"
        paths = sorted(record_dir.glob("[0-9][0-9][0-9][0-9].json")) if record_dir.is_dir() else []
        if not paths:
            return
        self.assertGreaterEqual(len(paths), 2)
        for rid in ("0001", "0002"):
            value = json.loads((record_dir / f"{rid}.json").read_text(encoding="utf-8"))
            self.assertEqual(value["record_id"], f"tolkappiyam-{rid}")
            self.assertEqual(len(value["dimension_reviews"]), 29)
            formal = value["concept_evidence"]
            self.assertEqual(len(formal), 1)
            self.assertEqual(formal[0]["dimension"], "knowledge_technology")
            self.assertEqual(formal[0]["concept_id"], "knowledge.grammar.phonology")
            self.assertEqual(formal[0]["evidence_class"], "GRAMMATICAL_CONCEPT_EVIDENCE")
            self.assertEqual(formal[0]["classification_basis"], "tolkappiyam_mapping")
            self.assertTrue(value["audit_control"]["checked_after_fresh_source_review"])
            self.assertFalse(value["audit_control"]["crosswalk_used_to_create_classification"])
            incidental = sum(len(review["incidental_examples"]) for review in value["dimension_reviews"])
            self.assertEqual(incidental, 0)

    def test_04_tolkappiyam_never_auto_classifies_sangam_poems(self):
        crosswalk = json.loads(
            (ROOT / "research/audits/r15-premerge/tolkappiyam/dimension-crosswalk.json").read_text(encoding="utf-8")
        )
        manifest = json.loads(
            (ROOT / "research/audits/r15-premerge/tolkappiyam/review-manifest.json").read_text(encoding="utf-8")
        )
        self.assertIn("must not be converted automatically", crosswalk["interpretation_rule"])
        self.assertFalse(manifest["auto_classify_sangam_poems"])


if __name__ == "__main__":
    unittest.main()
