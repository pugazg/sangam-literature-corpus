import csv
import hashlib
import json
import subprocess
import sys
import unittest
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from corpuslib import profile  # noqa: E402
from tolkappiyam_pipeline import RAW, SOURCE_SHA256, parse_source, record_body, validate  # noqa: E402


class TolkappiyamTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.parsed = parse_source()
        cls.report = json.loads((ROOT / "manifests/tolkappiyam-validation-report.json").read_text())
        cls.upstream = json.loads((ROOT / "sources/source-metadata/tolkappiyam-upstream-import.json").read_text())

    def test_01_upstream_commit_pin(self):
        self.assertEqual(self.upstream["upstream_commit"], "16123f742503283e46f0ed321802a46f99df6392")

    def test_02_exact_upstream_source_blob(self):
        self.assertEqual(self.upstream["source_blob_sha256"], SOURCE_SHA256)

    def test_03_local_source_checksum(self):
        self.assertEqual(hashlib.sha256(RAW.read_bytes()).hexdigest(), SOURCE_SHA256)

    def test_04_upstream_local_byte_equivalence(self):
        self.assertTrue(self.upstream["byte_equivalent_to_upstream"]); self.assertEqual(RAW.stat().st_size, 384080)

    def test_05_three_adhikarams(self):
        self.assertEqual(len(self.parsed["adhikarams"]), 3)

    def test_06_twenty_seven_iyals(self):
        self.assertEqual(len(self.parsed["iyals"]), 27)

    def test_07_independent_nurpa_count(self):
        self.assertEqual(len(self.parsed["records"]), 1602)

    def test_08_stable_semantic_ids(self):
        ids=[x["stable_semantic_id"] for x in self.parsed["records"]]; self.assertEqual(len(ids),len(set(ids)))

    def test_09_duplicate_canonical_ids(self):
        ids=[x["canonical_record_id"] for x in self.parsed["records"]]; self.assertEqual(len(ids),len(set(ids)))

    def test_10_source_sequence(self):
        self.assertEqual([x["source_sequence"] for x in self.parsed["records"]],list(range(1,1603)))

    def test_11_traditional_number_restarts(self):
        self.assertEqual(sum(x["traditional_number"]==1 for x in self.parsed["records"]),27)

    def test_12_source_editorial_heading_separation(self):
        changed=[x for x in self.parsed["iyals"] if x["title_as_printed"]!=x["display_title"]]; self.assertEqual(len(changed),7)

    def test_13_all_twelve_warnings(self):
        review=json.loads((ROOT/"sources/source-metadata/tolkappiyam-warning-review.json").read_text()); self.assertEqual(review["warning_count"],12);self.assertTrue(all(x["status"]=="confirmed" for x in review["warnings"]))

    def test_14_attached_number_parsing(self):
        self.assertEqual(len(self.parsed["attached_number_conditions"]),5)

    def test_15_special_prefatory_material(self):
        self.assertTrue(self.parsed["prefatory_material"]); self.assertTrue((ROOT/"corpus/tolkappiyam/prefatory-material.md").is_file())

    def test_16_original_lines(self):
        first=self.parsed["records"][0]; self.assertEqual(first["original_lines"][0],"எழுத்து எனப்படுப")

    def test_17_source_output_equality(self):
        self.assertEqual(self.report["source_output_matches"],1602)

    def test_18_source_note_equality(self):
        self.assertEqual(self.report["source_note_matches"],1602)

    def test_19_no_explanation_leakage(self):
        text=(ROOT/"corpus/tolkappiyam/nurpas/0001.md").read_text(); self.assertNotIn("simpleTamilExplanation",text);self.assertNotIn("englishExplanation",text)

    def test_20_no_commentary_leakage(self):
        self.assertNotIn("commentaryReferences",(ROOT/"corpus/tolkappiyam/nurpas/0001.md").read_text())

    def test_21_no_glossary_leakage(self):
        self.assertNotIn("gloss",yaml.safe_load((ROOT/"corpus/tolkappiyam/nurpas/0001.md").read_text().split("---",2)[1]))

    def test_22_no_application_dependency(self):
        imported=self.upstream["files_selected"]; self.assertFalse(any(x.startswith("app/") for x in imported))

    def test_23_unknown_work_fails(self):
        with self.assertRaises(ValueError): profile("unknown-tamil-work")

    def test_24_utf8(self):
        RAW.read_bytes().decode("utf-8")

    def test_25_records_manifest_inventory(self):
        rows=list(csv.DictReader((ROOT/"manifests/records.csv").open())); self.assertEqual(len(rows),7234); self.assertEqual(sum(x["work_id"]=="tolkappiyam" for x in rows),1602)

    def test_26_no_temporary_manifest(self):
        self.assertFalse(list((ROOT/"manifests").glob("*.lock")));self.assertFalse(list((ROOT/"manifests").glob("*.tmp")))

    def test_27_physical_nurpa_inventory(self):
        self.assertEqual(len(list((ROOT/"corpus/tolkappiyam/nurpas").glob("*.md"))),1602);self.assertFalse((ROOT/"corpus/tolkappiyam/poems").exists())

    def test_28_upstream_original_text_comparison(self):
        self.assertEqual(self.parsed["upstream_body_mismatches"],[])

    def test_29_validation(self):
        self.assertEqual(validate(write=False)["status"],"pass")

    def test_30_r0_research_identity_preserved_after_branch_cleanup(self):
        report=json.loads((ROOT/"logs/classical-tamil-research-r0-to-corpus-1.1.0-compatibility-20260818T145500.json").read_text())
        self.assertEqual(report["r0_commit"],"7087626347b56e0145ab69b2fb7ef355f6bc07d5d")
        self.assertTrue(report["verification"]["r0_research_subtree_ported_byte_identically"])
        self.assertTrue(report["verification"]["r0_assertion_ids_and_evidence_spans_preserved"])
        self.assertEqual(report["status"],"pass")


if __name__=="__main__":unittest.main()
