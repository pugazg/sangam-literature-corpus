import hashlib
import json
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from generate_research_r1 import generate as generate_r1  # noqa: E402
from research_r1lib import (  # noqa: E402
    ALLOWED_REVIEW_TRANSITIONS,
    ENTITY_OPERATIONS,
    decision_id,
    load_ndjson,
    validate_decision_semantics,
    validate_event_chain,
)


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


class ResearchR1Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.assertions = load_ndjson(ROOT / "research/evidence/purananuru/assertions.ndjson")
        cls.assertion_ids = {value["assertion_id"] for value in cls.assertions}
        cls.events = load_ndjson(ROOT / "research/reviews/purananuru/review-events.ndjson")
        cls.decisions = load_ndjson(ROOT / "research/entities/pilot/entity-resolution-decisions.ndjson")

    def test_01_compatibility_gate(self):
        report = json.loads((ROOT / "logs/classical-tamil-research-r0-to-corpus-1.1.0-compatibility-20260818T145500.json").read_text(encoding="utf-8"))
        self.assertEqual(report["status"], "pass")
        self.assertEqual(report["current_corpus_release_tag"], "classical-tamil-corpus-v1.1.0")
        self.assertFalse(report["verification"]["canonical_corpus_mutation"])

    def test_02_r0_assertion_identity_preserved(self):
        path = ROOT / "research/evidence/purananuru/assertions.ndjson"
        self.assertEqual(len(self.assertions), 2867)
        self.assertEqual(sha(path), "39f22d32948a112c65c712991023d33fcd171d5cd502cf767fdfd2fe91771b65")

    def test_03_r1_review_schema(self):
        schema = json.loads((ROOT / "research/schemas/review-event-r1.schema.json").read_text(encoding="utf-8"))
        self.assertEqual(schema["properties"]["event_version"]["const"], "0.2.0")
        self.assertIn("reviewer", schema["required"])
        self.assertIn("event_hash", schema["required"])

    def test_04_reviewer_types(self):
        vocab = json.loads((ROOT / "research/controlled-vocabularies/reviewer-types.json").read_text(encoding="utf-8"))
        codes = {value["code"] for value in vocab["entries"]}
        self.assertEqual(codes, {"human_editor", "assistant_assisted", "automated_system"})
        self.assertTrue(all(event["reviewer"]["reviewer_type"] == "assistant_assisted" for event in self.events))

    def test_05_review_transitions_legal(self):
        self.assertTrue(self.events)
        self.assertTrue(all((event["previous_status"], event["new_status"]) in ALLOWED_REVIEW_TRANSITIONS for event in self.events))

    def test_06_no_machine_checked_to_verified(self):
        self.assertNotIn(("machine_checked", "verified"), ALLOWED_REVIEW_TRANSITIONS)
        self.assertNotIn(("human_review_required", "verified"), ALLOWED_REVIEW_TRANSITIONS)

    def test_07_review_event_chain(self):
        self.assertEqual(validate_event_chain(self.events), [])
        self.assertEqual([event["sequence"] for event in self.events], list(range(1, len(self.events) + 1)))

    def test_08_merge_operation_semantics(self):
        self.assertIn("merge", ENTITY_OPERATIONS)
        valid = {
            "decision_id": "synthetic-merge",
            "operation": "merge",
            "involved_entity_ids": ["e1", "e2"],
            "variant_forms": ["a", "b"],
            "supporting_assertion_ids": ["asrt.x"],
            "result_entity_id": "e1",
        }
        invalid = valid | {"involved_entity_ids": ["e1"]}
        self.assertEqual(validate_decision_semantics(valid), [])
        self.assertTrue(validate_decision_semantics(invalid))

    def test_09_split_operation_semantics(self):
        self.assertIn("split", ENTITY_OPERATIONS)
        valid = {
            "decision_id": "synthetic-split",
            "operation": "split",
            "involved_entity_ids": ["e1"],
            "variant_forms": ["a"],
            "supporting_assertion_ids": ["asrt.x"],
            "result_entity_id": None,
        }
        invalid = valid | {"involved_entity_ids": ["e1", "e2"]}
        self.assertEqual(validate_decision_semantics(valid), [])
        self.assertTrue(validate_decision_semantics(invalid))

    def test_10_reject_and_supersede_operations_supported(self):
        self.assertIn("reject", ENTITY_OPERATIONS)
        self.assertIn("supersede", ENTITY_OPERATIONS)
        for operation in ("reject", "supersede"):
            value = {
                "decision_id": f"synthetic-{operation}",
                "operation": operation,
                "involved_entity_ids": ["e1"],
                "variant_forms": ["a"],
                "supporting_assertion_ids": ["asrt.x"],
                "result_entity_id": None,
            }
            self.assertEqual(validate_decision_semantics(value), [])

    def test_11_possible_is_not_verified(self):
        states = {decision["identity_state"] for decision in self.decisions}
        self.assertIn("possible_match", states)
        self.assertNotIn("verified_match", states)
        for decision in self.decisions:
            self.assertEqual(validate_decision_semantics(decision), [])

    def test_12_unreviewed_mentions_retained(self):
        mentions = load_ndjson(ROOT / "research/mentions/purananuru/mentions.ndjson")
        self.assertEqual(len(mentions), 285)
        self.assertEqual(len({value["assertion_id"] for value in mentions}), 285)

    def test_13_review_queue_deterministic_order(self):
        queue = load_ndjson(ROOT / "research/reviews/purananuru/review-queue.ndjson")
        expected = sorted(queue, key=lambda value: (int(value["record_id"]) if value["record_id"] else 999, value["queue_item_type"], value["printed_form"], value["assertion_id"] or "", value["entity_id"] or ""))
        self.assertEqual(queue, expected)
        self.assertEqual(len({value["queue_id"] for value in queue}), len(queue))

    def test_14_entity_decision_ids_deterministic(self):
        self.assertTrue(self.decisions)
        self.assertTrue(all(value["decision_id"] == decision_id(value) for value in self.decisions))

    def test_15_all_resolution_support_exists(self):
        for decision in self.decisions:
            self.assertTrue(set(decision["supporting_assertion_ids"]) <= self.assertion_ids)

    def test_16_generator_does_not_mutate_corpus(self):
        targets = [
            ROOT / "corpus/purananuru/poems/003.md",
            ROOT / "corpus/purananuru/poems/267.md",
            ROOT / "corpus/tolkappiyam/nurpas/0001.md",
        ]
        before = {path: sha(path) for path in targets}
        generate_r1(ROOT)
        after = {path: sha(path) for path in targets}
        self.assertEqual(before, after)

    def test_17_r1_idempotent_and_primary_logs_preserved(self):
        deterministic = [
            ROOT / "research/reviews/purananuru/review-queue.ndjson",
            ROOT / "research/reviews/purananuru/reviewed-export.ndjson",
            ROOT / "research/reports/purananuru-r1-review-summary.json",
            ROOT / "research/reports/purananuru-r1-review-summary.md",
            ROOT / "research/reports/purananuru-r1-ambiguity-register.md",
            ROOT / "research/reports/purananuru-r1-unresolved-entities.csv",
        ]
        primary = [
            ROOT / "research/reviews/purananuru/review-events.ndjson",
            ROOT / "research/entities/pilot/entity-resolution-decisions.ndjson",
        ]
        primary_before = {path: sha(path) for path in primary}
        generate_r1(ROOT)
        first = {path: sha(path) for path in deterministic}
        generate_r1(ROOT)
        second = {path: sha(path) for path in deterministic}
        primary_after = {path: sha(path) for path in primary}
        self.assertEqual(first, second)
        self.assertEqual(primary_before, primary_after)

    def test_18_corpus_tree_matches_1_1_0(self):
        subprocess.check_call(["git", "diff", "--quiet", "classical-tamil-corpus-v1.1.0", "--", "corpus", "sources", "apparatus"], cwd=ROOT)

    def test_19_tolkappiyam_matches_1_1_0(self):
        subprocess.check_call(["git", "diff", "--quiet", "classical-tamil-corpus-v1.1.0", "--", "corpus/tolkappiyam", "apparatus/tolkappiyam"], cwd=ROOT)

    def test_20_shared_manifests_match_1_1_0(self):
        subprocess.check_call(["git", "diff", "--quiet", "classical-tamil-corpus-v1.1.0", "--", "manifests/poems.csv", "manifests/records.csv"], cwd=ROOT)

    def test_21_r0_generator_protects_review_history(self):
        source = (ROOT / "scripts/generate_research_layer.py").read_text(encoding="utf-8")
        self.assertIn("import generate_research_layer_r0 as r0", source)
        self.assertIn("if target == review_events and review_events.exists():", source)
        self.assertNotIn('atomic_write(root / "research/reviews/purananuru/review-events.ndjson", "")', source)


if __name__ == "__main__":
    unittest.main()
