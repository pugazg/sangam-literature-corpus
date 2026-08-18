import hashlib
import json
import subprocess
import sys
import tempfile
import threading
import unicodedata
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from researchlib import advisory_lock, assertion_id, atomic_write, normalize_lookup, parse_poem  # noqa: E402


def ndjson(path):
    return [json.loads(x) for x in path.read_text(encoding="utf-8").splitlines() if x]


class ResearchLayerTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.assertions = ndjson(ROOT / "research/evidence/purananuru/assertions.ndjson")
        cls.by_record = {}
        for value in cls.assertions:
            cls.by_record.setdefault(value["record_id"], []).append(value)

    def test_01_frozen_release_tag(self):
        value = subprocess.check_output(["git", "rev-parse", "classical-tamil-corpus-v1.0.0^{}"], cwd=ROOT, text=True).strip()
        self.assertEqual(value, "272d9d5a79d55994e2c12efacc22be20b2c88030")

    def test_02_canonical_input_hash(self):
        value = self.assertions[0]
        self.assertEqual(value["canonical_record_sha256"], hashlib.sha256((ROOT / value["canonical_record_path"]).read_bytes()).hexdigest())

    def test_03_assertion_schema_required(self):
        required = json.loads((ROOT / "research/schemas/assertion.schema.json").read_text())["required"]
        self.assertFalse(set(required) - set(self.assertions[0]))

    def test_04_deterministic_assertion_id(self):
        self.assertEqual(self.assertions[0]["assertion_id"], assertion_id(self.assertions[0]))

    def test_05_evidence_span(self):
        candidate = next(x for x in self.assertions if x["evidence_span"])
        parsed = parse_poem(ROOT / candidate["canonical_record_path"])
        span = candidate["evidence_span"]
        line = parsed["body_lines"][span["start_line"] - 1]
        self.assertEqual(line[span["start_character"]:span["end_character"]], candidate["source_text"])

    def test_06_tamil_unicode_nfc(self):
        self.assertEqual(normalize_lookup("  தமிழ்! "), unicodedata.normalize("NFC", "தமிழ்"))

    def test_07_printed_form_preserved(self):
        value = next(x for x in self.assertions if x["assertion_type"] == "POET_ATTRIBUTION")
        self.assertEqual(value["source_text"], value["normalization"]["printed_form"])

    def test_08_normalized_form_separate(self):
        self.assertIn("normalization", self.assertions[0])
        self.assertIn("normalized_form", self.assertions[0]["normalization"])

    def test_09_metadata_assertions(self):
        self.assertTrue(any(x["source_location"].startswith("yaml:") for x in self.assertions))

    def test_10_source_lost_267(self):
        parsed = parse_poem(ROOT / "corpus/purananuru/poems/267.md")
        self.assertEqual(parsed["body"], "")
        self.assertTrue(any(x["source_text"] == "lost" for x in self.by_record["267"]))

    def test_11_source_lost_268(self):
        parsed = parse_poem(ROOT / "corpus/purananuru/poems/268.md")
        self.assertEqual(parsed["body"], "")
        self.assertFalse(any(x["source_field"] == "canonical_body" for x in self.by_record["268"]))

    def test_12_null_field_handling(self):
        self.assertFalse(any(x["source_text"] in {None, ""} for x in self.assertions))

    def test_13_poet_attributions(self):
        self.assertEqual(sum(x["assertion_type"] == "POET_ATTRIBUTION" for x in self.assertions), 386)
        self.assertTrue(all(x["source_note_reference"] == "## Source note (as printed)" for x in self.assertions if x["assertion_type"] == "POET_ATTRIBUTION"))

    def test_14_addressees(self):
        self.assertEqual(sum(x["assertion_type"] == "PATRON_OR_ADDRESSEE" for x in self.assertions), 233)

    def test_15_tinai(self):
        self.assertEqual(sum(x["assertion_type"] == "TINI_VALUE" for x in self.assertions), 386)

    def test_16_turai(self):
        self.assertEqual(sum(x["assertion_type"] == "TURAI_VALUE" for x in self.assertions), 386)

    def test_17_literary_candidates(self):
        self.assertEqual(sum(x["source_field"] == "canonical_body" for x in self.assertions), 285)

    def test_18_no_apparatus_leakage(self):
        self.assertFalse(any("apparatus/" in x["canonical_record_path"] for x in self.assertions))

    def test_19_no_external_evidence(self):
        self.assertFalse(any(x["evidence_class"] == "EXTERNAL_HISTORICAL" for x in self.assertions))

    def test_20_relationship_provenance(self):
        ids = {x["assertion_id"] for x in self.assertions}
        relations = ndjson(ROOT / "research/relationships/pilot/relationships.ndjson")
        self.assertTrue(all(set(x["supporting_assertion_ids"]) <= ids for x in relations))

    def test_21_entity_ambiguity(self):
        entities = ndjson(ROOT / "research/entities/pilot/entities.ndjson")
        self.assertTrue(all(x["review_status"] == "human_review_required" and x["modern_identification"] is None for x in entities))

    def test_22_append_only_review_events(self):
        events = ndjson(ROOT / "research/reviews/purananuru/review-events.ndjson")
        self.assertTrue(events)
        self.assertEqual([x["sequence"] for x in events], list(range(1, len(events) + 1)))

    def test_23_invalid_transition_defined(self):
        from validate_research_layer import ALLOWED_TRANSITIONS
        self.assertNotIn(("machine_checked", "verified"), ALLOWED_TRANSITIONS)

    def test_24_duplicate_assertions(self):
        ids = [x["assertion_id"] for x in self.assertions]
        self.assertEqual(len(ids), len(set(ids)))

    def test_25_orphan_paths(self):
        self.assertTrue(all((ROOT / x["canonical_record_path"]).is_file() for x in self.assertions))

    def test_26_deterministic_record_order(self):
        values = [int(x["record_id"]) for x in self.assertions]
        self.assertEqual(values, sorted(values))

    def test_27_utf8(self):
        (ROOT / "research/evidence/purananuru/assertions.ndjson").read_bytes().decode("utf-8")

    def test_28_atomic_write(self):
        with tempfile.TemporaryDirectory() as directory:
            target = Path(directory) / "x"
            atomic_write(target, "தமிழ்\n")
            self.assertEqual(target.read_text(), "தமிழ்\n")

    def test_29_concurrent_lock(self):
        with tempfile.TemporaryDirectory() as directory:
            lock = Path(directory) / "lock"
            order = []

            def worker(value):
                with advisory_lock(lock):
                    order.append(value)

            threads = [threading.Thread(target=worker, args=(x,)) for x in range(4)]
            for x in threads:
                x.start()
            for x in threads:
                x.join()
            self.assertEqual(sorted(order), [0, 1, 2, 3])

    def test_30_no_temp_files(self):
        self.assertFalse(list((ROOT / "research").rglob("*.tmp")))

    def test_31_inventory(self):
        self.assertEqual(len(list((ROOT / "research/evidence/purananuru/records").glob("*.ndjson"))), 400)

    def test_32_source_note_hash(self):
        value = self.assertions[0]
        parsed = parse_poem(ROOT / value["canonical_record_path"])
        self.assertEqual(value["source_note_sha256"], parsed["source_note_sha256"])

    def test_33_csv_header(self):
        self.assertTrue((ROOT / "research/evidence/purananuru/assertions.csv").read_text(encoding="utf-8").startswith("assertion_id,"))

    def test_34_extracted_at_is_deterministic_null(self):
        self.assertTrue(all(x["extracted_at"] is None for x in self.assertions))

    def test_35_pilot_scope_only(self):
        self.assertEqual({x["work_id"] for x in self.assertions}, {"purananuru"})


if __name__ == "__main__":
    unittest.main()
