import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from validate_r15_production_dimensions import (  # noqa: E402
    CANONICAL_DIMENSIONS,
    CANONICAL_IDS,
    LIVED_LIFE_DIMENSIONS,
    validate,
)


class R15ProductionDimensionTests(unittest.TestCase):
    def test_01_exact_29_dimension_contract_is_literal_and_ordered(self):
        self.assertEqual(len(CANONICAL_DIMENSIONS), 29)
        self.assertEqual(len(CANONICAL_IDS), 29)
        self.assertEqual(len(set(CANONICAL_IDS)), 29)
        self.assertEqual(CANONICAL_IDS[0], "literary_domain")
        self.assertEqual(CANONICAL_IDS[-1], "textual_intertextual_relationships")

    def test_02_non_collapsible_boundaries_remain_separate(self):
        expected_separate = {
            "economy",
            "trade_exchange",
            "emotion_lived_experience",
            "values_ethical_concepts",
            "body_health",
            "clothing_ornaments_adornment",
            "people_social_roles",
            "communities_social_groups",
            "family_gender_kinship",
        }
        self.assertTrue(expected_separate <= set(CANONICAL_IDS))
        self.assertEqual(len(LIVED_LIFE_DIMENSIONS), 24)

    def test_03_repository_alignment_validator_passes(self):
        report = validate(ROOT)
        self.assertEqual(report["errors"], [])
        self.assertEqual(report["warnings"], [])
        self.assertEqual(report["canonical_dimension_count"], 29)
        self.assertEqual(report["production_vocabulary_dimension_count"], 29)
        self.assertEqual(report["status"], "pass")


if __name__ == "__main__":
    unittest.main()
