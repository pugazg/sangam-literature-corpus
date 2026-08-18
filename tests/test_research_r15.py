import hashlib
import json
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from generate_research_r15 import (  # noqa: E402
    build_matrix,
    build_observations,
    generate as generate_r15,
    observation_id,
)
from research_r1lib import load_ndjson  # noqa: E402
from validate_research_r15 import validate as validate_r15  # noqa: E402


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


class ResearchR15Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.registry = json.loads(
            (ROOT / "research/concepts/classical-tamil/concept-registry-r15.json").read_text(encoding="utf-8")
        )
        cls.pilot = json.loads(
            (ROOT / "research/pilots/purananuru/r15-pilot-mapping.json").read_text(encoding="utf-8")
        )
        cls.observations = load_ndjson(ROOT / "research/observations/purananuru/r15-pilot.ndjson")
        cls.reviewed = load_ndjson(ROOT / "research/reviews/purananuru/reviewed-export.ndjson")
        cls.assertions = load_ndjson(ROOT / "research/evidence/purananuru/assertions.ndjson")

    def test_01_version_boundaries(self):
        schema = json.loads(
            (ROOT / "research/schemas/concept-observation-r15.schema.json").read_text(encoding="utf-8")
        )
        self.assertEqual(schema["properties"]["schema_version"]["const"], "0.3.0")
        self.assertEqual(self.registry["schema_version"], "0.3.0")
        self.assertEqual(self.pilot["schema_version"], "0.3.0")
        r1 = json.loads((ROOT / "research/reports/purananuru-r1-review-summary.json").read_text(encoding="utf-8"))
        self.assertEqual(r1["research_schema_version"], "0.2.0")
        self.assertEqual(r1["evidence_schema_version"], "0.1.0")

    def test_02_matrix_semantics_are_not_boolean_absence_claims(self):
        semantics = self.registry["semantics"]
        self.assertIn("derived view", semantics["matrix_cell"])
        self.assertIn("not evidence of historical absence", semantics["empty_cell"])

    def test_03_literary_domain_foundation_present(self):
        concepts = {value["concept_id"] for value in self.registry["concepts"]}
        self.assertTrue(
            {
                "literary.domain.akam",
                "literary.domain.puram",
                "literary.domain.uncertain",
                "literary.domain.not_applicable",
            }
            <= concepts
        )

    def test_04_tinai_foundation_present_without_record_assignment(self):
        concepts = {value["concept_id"] for value in self.registry["concepts"]}
        expected = {
            "literary.tinai.kurinji",
            "literary.tinai.mullai",
            "literary.tinai.marutam",
            "literary.tinai.neytal",
            "literary.tinai.palai",
            "literary.tinai.kaikkilai",
            "literary.tinai.peruntinai",
        }
        self.assertTrue(expected <= concepts)
        self.assertFalse(any(value["dimension"] == "tinai" for value in self.observations))

    def test_05_bounded_pilot_counts(self):
        self.assertEqual(len(self.pilot["mappings"]), 8)
        self.assertEqual(len(self.observations), 8)
        self.assertEqual(len({value["record_id"] for value in self.observations}), 6)
        self.assertEqual(len({value["concept_id"] for value in self.observations}), 7)
        self.assertEqual(len({value["dimension"] for value in self.observations}), 7)

    def test_06_every_observation_is_assertion_provenanced(self):
        assertion_ids = {value["assertion_id"] for value in self.assertions}
        for value in self.observations:
            self.assertEqual(len(value["supporting_assertion_ids"]), 1)
            self.assertIn(value["supporting_assertion_ids"][0], assertion_ids)

    def test_07_exact_source_fields_and_spans_preserved(self):
        reviewed = {value["assertion_id"]: value for value in self.reviewed}
        for value in self.observations:
            source = reviewed[value["supporting_assertion_ids"][0]]
            self.assertEqual(value["surface_form"], source["printed_form"])
            self.assertEqual(value["evidence_span"], source["evidence_span"])
            self.assertEqual(value["source_field"], source["source_field"])
            self.assertEqual(value["source_location"], source["source_location"])

    def test_08_observation_ids_are_deterministic(self):
        ids = []
        for value in self.observations:
            expected = observation_id(
                value["supporting_assertion_ids"][0],
                value["concept_id"],
                value["classification_basis"],
            )
            self.assertEqual(value["observation_id"], expected)
            ids.append(expected)
        self.assertEqual(len(ids), len(set(ids)))

    def test_09_pilot_claim_types_remain_source_explicit(self):
        self.assertTrue(all(value["evidence_class"] == "SOURCE_EXPLICIT" for value in self.observations))
        self.assertTrue(all(value["review_status"] == "reviewed" for value in self.observations))
        self.assertTrue(all(value["reviewer_type"] == "assistant_assisted" for value in self.observations))
        self.assertFalse(any(value["evidence_class"] == "EXTERNAL_HISTORICAL" for value in self.observations))
        self.assertFalse(any(value["evidence_class"] == "INTERPRETATION" for value in self.observations))

    def test_10_ruler_identity_remains_unresolved(self):
        rulers = [value for value in self.observations if value["concept_id"] == "polity.ruler"]
        self.assertEqual(len(rulers), 2)
        self.assertEqual({value["surface_form"] for value in rulers}, {"இறைவன்", "ஆய்"})
        self.assertTrue(all(value["historical_identity_status"] == "unresolved" for value in rulers))
        self.assertFalse(any(value["historical_identity_status"] == "verified_external" for value in self.observations))

    def test_11_committed_outputs_match_generator(self):
        expected = build_observations(ROOT)
        self.assertEqual(self.observations, expected)
        expected_matrix = build_matrix(expected)
        self.assertEqual(
            (ROOT / "research/matrices/purananuru/r15-pilot-matrix.csv").read_text(encoding="utf-8"),
            expected_matrix,
        )

    def test_12_generator_preserves_primary_evidence_and_review_inputs(self):
        primary = [
            ROOT / "research/evidence/purananuru/assertions.ndjson",
            ROOT / "research/reviews/purananuru/review-events.ndjson",
            ROOT / "research/reviews/purananuru/reviewed-export.ndjson",
            ROOT / "research/entities/pilot/entity-resolution-decisions.ndjson",
        ]
        before = {path: sha(path) for path in primary}
        generate_r15(ROOT)
        after = {path: sha(path) for path in primary}
        self.assertEqual(before, after)

    def test_13_r0_assertion_identity_still_preserved(self):
        self.assertEqual(len(self.assertions), 2867)
        self.assertEqual(
            sha(ROOT / "research/evidence/purananuru/assertions.ndjson"),
            "39f22d32948a112c65c712991023d33fcd171d5cd502cf767fdfd2fe91771b65",
        )

    def test_14_validator_passes(self):
        report = validate_r15(ROOT)
        self.assertEqual(report["errors"], [])
        self.assertEqual(report["warnings"], [])
        self.assertEqual(report["status"], "pass")

    def test_15_frozen_corpus_tree_unchanged(self):
        subprocess.check_call(
            [
                "git",
                "diff",
                "--quiet",
                "classical-tamil-corpus-v1.1.0",
                "--",
                "corpus",
                "sources",
                "apparatus",
                "manifests/poems.csv",
                "manifests/records.csv",
            ],
            cwd=ROOT,
        )


if __name__ == "__main__":
    unittest.main()
