import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from validate_r15_production_dimensions import CANONICAL_IDS  # noqa: E402
from validate_r15_purananuru_production import validate  # noqa: E402


class R15PurananuruProductionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.record_001 = json.loads(
            (ROOT / "research/production/purananuru/records/001.json").read_text(encoding="utf-8")
        )

    def test_01_production_prefix_validator_passes(self):
        report = validate(ROOT)
        self.assertEqual(report["errors"], [])
        self.assertEqual(report["warnings"], [])
        self.assertEqual(report["canonical_dimension_count"], 29)
        self.assertGreaterEqual(report["records_reviewed"], 1)
        self.assertEqual(report["status"], "pass")

    def test_02_record_001_considers_exact_29_dimensions(self):
        reviews = self.record_001["dimension_reviews"]
        self.assertEqual(len(reviews), 29)
        self.assertEqual([entry["dimension"] for entry in reviews], list(CANONICAL_IDS))
        self.assertEqual(self.record_001["dimensions_considered"], 29)
        self.assertEqual(self.record_001["next_record_allowed"], "002")

    def test_03_record_001_preserves_source_terminology_boundary(self):
        serialized = json.dumps(self.record_001, ensure_ascii=False)
        self.assertIn("அந்தணர்", serialized)
        self.assertNotIn("Brahmin", serialized)
        self.assertNotIn("brahmin", serialized)
        communities = next(
            entry for entry in self.record_001["dimension_reviews"]
            if entry["dimension"] == "communities_social_groups"
        )
        self.assertEqual(communities["status"], "qualifying_evidence_recorded")

    def test_04_record_001_old_audit_used_only_as_post_review_control(self):
        control = self.record_001["audit_control"]
        self.assertTrue(control["checked_after_fresh_source_review"])
        self.assertEqual(control["comparison_status"], "exact_match")
        self.assertEqual(control["discrepancies"], [])


if __name__ == "__main__":
    unittest.main()
