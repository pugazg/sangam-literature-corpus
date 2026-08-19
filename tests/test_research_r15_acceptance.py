import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from validate_research_r15_acceptance import REQUIRED_FOUNDATION, validate  # noqa: E402


class ResearchR15AcceptanceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.registry = json.loads(
            (ROOT / "research/concepts/classical-tamil/concept-registry-r15.json").read_text(encoding="utf-8")
        )
        cls.policies = json.loads(
            (ROOT / "research/controlled-vocabularies/concept-evidence-policies-r15.json").read_text(encoding="utf-8")
        )
        cls.tolk_schema = json.loads(
            (ROOT / "research/schemas/tolkappiyam-concept-evidence-r15.schema.json").read_text(encoding="utf-8")
        )

    def test_01_complete_foundation_concepts_present(self):
        concepts = {value["concept_id"] for value in self.registry["concepts"]}
        self.assertTrue(REQUIRED_FOUNDATION <= concepts)

    def test_02_turai_is_first_class_foundation(self):
        concepts = {value["concept_id"]: value for value in self.registry["concepts"]}
        self.assertEqual(concepts["literary.turai"]["dimension"], "tinai_turai")
        self.assertEqual(concepts["literary.tinai"]["dimension"], "tinai_turai")
        self.assertNotEqual(concepts["literary.turai"]["concept_id"], concepts["literary.tinai"]["concept_id"])
        self.assertEqual(concepts["literary.turai.uncertain"]["parent_concept_id"], "literary.turai")
        self.assertEqual(concepts["literary.turai.not_applicable"]["parent_concept_id"], "literary.turai")

    def test_03_five_landscape_families_are_not_tinai_assignments(self):
        concepts = {value["concept_id"]: value for value in self.registry["concepts"]}
        for name in ("kurinji", "mullai", "marutam", "neytal", "palai"):
            value = concepts[f"landscape.{name}"]
            self.assertEqual(value["dimension"], "landscape_environment")
            self.assertEqual(value["parent_concept_id"], "landscape.classical")
        observations = (ROOT / "research/observations/purananuru/r15-pilot.ndjson").read_text(encoding="utf-8")
        self.assertNotIn('"concept_id": "landscape.', observations)

    def test_04_named_entity_family_does_not_resolve_identity(self):
        concepts = {value["concept_id"] for value in self.registry["concepts"]}
        self.assertTrue({"entity.named", "entity.person", "entity.place", "entity.polity", "entity.community", "entity.deity", "entity.uncertain"} <= concepts)
        self.assertIn("Mention classification is separate from historical identity resolution", json.dumps(self.policies, ensure_ascii=False))

    def test_05_tolkappiyam_stream_is_separate_and_population_is_prerequisite_gated(self):
        props = self.tolk_schema["properties"]
        self.assertEqual(props["work_id"]["const"], "tolkappiyam")
        self.assertEqual(props["evidence_class"]["const"], "GRAMMATICAL_CONCEPT_EVIDENCE")
        self.assertEqual(props["classification_basis"]["const"], "tolkappiyam_mapping")
        self.assertTrue((ROOT / "research/observations/tolkappiyam/README.md").is_file())
        populated = list((ROOT / "research/observations/tolkappiyam").glob("*.ndjson"))
        if populated:
            records = list((ROOT / "research/production/purananuru/records").glob("[0-9][0-9][0-9].json"))
            self.assertEqual(len(records), 400)
            self.assertTrue((ROOT / "research/production/purananuru/records/400.json").is_file())

    def test_06_evidence_policy_families_present(self):
        families = {value["family"] for value in self.policies["rules"]}
        self.assertTrue({"literary_domain", "tinai", "turai", "landscape_environment", "named_entity", "lived_life"} <= families)

    def test_07_acceptance_validator_passes(self):
        report = validate(ROOT)
        self.assertEqual(report["errors"], [])
        self.assertEqual(report["warnings"], [])
        self.assertEqual(report["status"], "pass")
        self.assertEqual(report["orphan_observation_assertion_count"], 0)
        self.assertEqual(report["orphan_observation_concept_count"], 0)
        self.assertEqual(report["orphan_relationship_assertion_count"], 0)
        self.assertEqual(report["orphan_relationship_entity_count"], 0)
        self.assertEqual(report["invalid_relationship_subject_count"], 0)


if __name__ == "__main__":
    unittest.main()
