import csv, json, shutil, sys, tempfile, unicodedata, unittest
from unittest import mock
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"scripts"))
from corpuslib import body_hash, parse_aingurunuru_html, parse_akananuru_html, parse_kuruntokai_html, parse_natrinai_html, parse_purananuru_text, parse_work_html, poem_markdown, read_frontmatter, recognize_poem_heading
from audit_repository import audit
from pattuppattu_pipeline import parse_all, verify_source_set
from patirruppattu_pipeline import parse as parse_patirruppattu
from paripatal_pipeline import parse as parse_paripatal
from kalittokai_pipeline import parse as parse_kalittokai
from pathinenkilkanakku_pipeline import (parse_naladiyar,
                                         parse_nanmanikkadigai,
                                         parse_inna_narpathu,
                                         parse_iniyavai_narpathu,
                                         parse_kar_narpathu,
                                         parse_kalavazhi_narpathu,
                                         parse_aintinai_aimpathu,
                                         parse_aintinai_elupathu,
                                         parse_thinaimalai_nutraimbathu,
                                         parse_thinaimozhi_aimpathu,
                                         parse_tirikatukam, parse_acharakkovai,
                                         parse_pazhamozhi_nanuru,
                                         parse_sirupanchamulam,
                                         parse_muthumozhi_kanchi,
                                         parse_elati, parse_kainnilai,
                                         parse_tirukkural)
from build_manifest import FIELDS, POLICY_VERSION, aggregate_all, canonical_row_key

FIX=Path(__file__).parent/"fixtures/natrinai_sample.html"

class PipelineTests(unittest.TestCase):
    def test_combined_manifest_identity_and_order(self):
        rows=list(csv.DictReader((Path(__file__).parents[1]/"manifests/poems.csv").open(encoding="utf-8")))
        self.assertEqual(len(rows),5632)
        self.assertEqual(len({canonical_row_key(x) for x in rows}),5632)
        order={x["work_slug"]:i for i,x in enumerate(json.loads((Path(__file__).parents[1]/"manifests/works.json").read_text()))}
        keys=[(order[x["work_slug"]],int(x.get("source_order") or x["poem_number"]),x["markdown_file"]) for x in rows]
        self.assertEqual(keys,sorted(keys))

    def test_combined_manifest_header_and_newlines(self):
        p=Path(__file__).parents[1]/"manifests/poems.csv";b=p.read_bytes()
        self.assertNotIn(b"\r\n",b);self.assertEqual(b.splitlines()[0].decode(),",".join(FIELDS));b.decode("utf-8")

    def test_manifest_aggregation_is_byte_idempotent(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)/"poems.csv";aggregate_all(p);a=p.read_bytes();aggregate_all(p);self.assertEqual(a,p.read_bytes())
            self.assertFalse(list(Path(d).glob("*.lock")));self.assertFalse(list(Path(d).glob("*.tmp")))

    def test_manifest_writer_has_atomic_locking(self):
        import inspect,build_manifest
        src=inspect.getsource(build_manifest.aggregate_all)
        self.assertIn("os.replace",src);self.assertIn("fcntl.flock",src);self.assertIn("os.fsync",src)
        self.assertEqual(POLICY_VERSION,"repository-canonical-order-v1")
    def test_tirukkural_source_inventory_and_structure(self):
        raw=(Path(__file__).parents[1]/"sources/raw-html/pathinenkilkanakku/pmuni0001.html").read_bytes()
        parsed=parse_tirukkural(raw)
        self.assertEqual(len(parsed["poems"]),1330)
        self.assertEqual(len(parsed["chapters"]),133)
        self.assertEqual([x["record_count"] for x in parsed["chapters"]], [10]*133)

    def test_tirukkural_repeated_title_is_not_literary_text(self):
        raw=(Path(__file__).parents[1]/"sources/raw-html/pathinenkilkanakku/pmuni0001.html").read_bytes()
        parsed=parse_tirukkural(raw)
        for n in (1,381,1081):
            self.assertNotIn("திருக்குறள்", parsed["poems"][n-1]["lines"])

    def test_tirukkural_printed_number_anomalies_preserved(self):
        raw=(Path(__file__).parents[1]/"sources/raw-html/pathinenkilkanakku/pmuni0001.html").read_bytes()
        parsed=parse_tirukkural(raw)
        self.assertEqual(
            [(x["poem_number"],x["poem_number_as_printed"]) for x in parsed["poems"]
             if not x["printed_number_matches_sequence"]],
            [(72,71),(753,752),(781,7811),(1293,12983)])

    def test_tirukkural_heading_anomalies_preserved(self):
        raw=(Path(__file__).parents[1]/"sources/raw-html/pathinenkilkanakku/pmuni0001.html").read_bytes()
        parsed=parse_tirukkural(raw)
        self.assertEqual(parsed["poems"][780]["chapter_heading_as_printed"],"2,3.6   நட்பு")
        self.assertIsNone(parsed["poems"][1150]["chapter_heading_as_printed"])
        self.assertEqual(parsed["poems"][1230]["chapter_heading_as_printed"],
                         "3..2. 9  உறுப்புநலனழிதல்")

    def test_naladiyar_inventory_invocation_and_chapters(self):
        raw=(Path(__file__).parents[1]/"sources/raw-html/pathinenkilkanakku/pmuni0016.html").read_bytes()
        parsed=parse_naladiyar(raw)
        self.assertEqual(len(parsed["poems"]),400)
        self.assertEqual(len(parsed["chapters"]),40)
        self.assertEqual(len(parsed["prefatory_text"]["lines"]),4)
        self.assertTrue(all(len(x["lines"])==4 for x in parsed["poems"]))

    def test_naladiyar_printed_239_heading_is_not_repaired(self):
        raw=(Path(__file__).parents[1]/"sources/raw-html/pathinenkilkanakku/pmuni0016.html").read_bytes()
        parsed=parse_naladiyar(raw)
        self.assertEqual(parsed["poems"][380]["major_division_as_printed"],"3. காமத்துப்பால்")
        self.assertEqual(parsed["poems"][380]["chapter_heading_as_printed"],"2.39 கற்புடை மகளிர்")

    def test_nanmanikkadigai_source_numbers_invocation_as_record_one(self):
        raw=(Path(__file__).parents[1]/"sources/raw-html/pathinenkilkanakku/pmuni0047.html").read_bytes()
        parsed=parse_nanmanikkadigai(raw)
        self.assertEqual(len(parsed["poems"]),106)
        self.assertEqual(parsed["poems"][0]["section_as_printed"],"கடவுள் வாழ்த்து")
        self.assertEqual(parsed["poems"][1]["section_as_printed"],"நூல்")
        self.assertEqual([x["poem_number_as_printed"] for x in parsed["poems"]],
                         list(range(1,107)))

    def test_inna_narpathu_bounded_records_and_variant_notes(self):
        raw=(Path(__file__).parents[1]/"sources/raw-html/pathinenkilkanakku/pmuni0025.html").read_bytes()
        parsed=parse_inna_narpathu(raw)
        self.assertEqual(len(parsed["poems"]),40)
        self.assertEqual(len(parsed["prefatory_text"]["lines"]),4)
        self.assertEqual(parsed["prefatory_text"]["source_note_lines"],
                         ["@பொற்பன வெள்ளியை             %மன்றப்பின்னாது"])
        self.assertEqual(parsed["poems"][0]["source_note_lines"],["@ ஊணின்னாது"])
        self.assertNotIn("இனியவை நாற்பது", " ".join(
            line for poem in parsed["poems"] for line in poem["lines"]))

    def test_iniyavai_narpathu_bounded_inventory(self):
        raw=(Path(__file__).parents[1]/"sources/raw-html/pathinenkilkanakku/pmuni0025.html").read_bytes()
        parsed=parse_iniyavai_narpathu(raw)
        self.assertEqual(len(parsed["poems"]),40)
        self.assertEqual(len(parsed["prefatory_text"]["lines"]),4)
        self.assertEqual(parsed["poems"][0]["lines"][0],"பிச்சைபுக் காயினுங் கற்றல் மிகஇனிதே")
        self.assertNotIn("களவழி நாற்பது"," ".join(
            line for poem in parsed["poems"] for line in poem["lines"]))

    def test_kar_narpathu_context_and_variants_are_source_notes(self):
        raw=(Path(__file__).parents[1]/"sources/raw-html/pathinenkilkanakku/pmuni0029.html").read_bytes()
        parsed=parse_kar_narpathu(raw)
        self.assertEqual(len(parsed["poems"]),40)
        self.assertEqual(len(parsed["poems"][0]["lines"]),4)
        self.assertIn("தோழி தலைமகட்குப் பருவங்காட்டி வற்புறுத்தது",
                      parsed["poems"][0]["source_note_lines"])
        self.assertIn("@  தீம்பொழல் வீழ       ஃ  பொழுது",
                      parsed["poems"][0]["source_note_lines"])
        self.assertIsNone(parsed["sections"][0]["heading_as_printed"])

    def test_kalavazhi_unumbered_concluding_text_not_inferred_as_41(self):
        raw=(Path(__file__).parents[1]/"sources/raw-html/pathinenkilkanakku/pmuni0025.html").read_bytes()
        parsed=parse_kalavazhi_narpathu(raw)
        self.assertEqual(len(parsed["poems"]),40)
        self.assertEqual(len(parsed["additional_unnumbered_literary_text"]["lines"]),5)
        self.assertEqual(parsed["additional_unnumbered_literary_text"]["lines"][-1],
                         "கூடாரை யட்ட களத்து.")
        self.assertEqual(parsed["additional_unnumbered_literary_text"]["provenance"],
                         "printed by Project Madurai without a number; not inferred as record 41")

    def test_aintinai_aimpathu_five_printed_divisions(self):
        raw=(Path(__file__).parents[1]/"sources/raw-html/pathinenkilkanakku/pmuni0027.html").read_bytes()
        parsed=parse_aintinai_aimpathu(raw)
        self.assertEqual(len(parsed["poems"]),50)
        self.assertEqual([x["record_count"] for x in parsed["sections"]],[10]*5)
        self.assertEqual([x["thinai"] for x in parsed["sections"]],
                         ["முல்லை","குறிஞ்சி","மருதம்","பாலை","நெய்தல்"])
        self.assertEqual(len(parsed["prefatory_text"]["lines"]),4)

    def test_aintinai_elupathu_four_source_lost_records(self):
        raw=(Path(__file__).parents[1]/"sources/raw-html/pathinenkilkanakku/pmuni0027.html").read_bytes()
        parsed=parse_aintinai_elupathu(raw)
        self.assertEqual(len(parsed["poems"]),70)
        self.assertEqual(parsed["source_lost_poems"],[25,26,69,70])
        for n in parsed["source_lost_poems"]:
            self.assertEqual(parsed["poems"][n-1]["lines"],[])
            self.assertEqual(parsed["poems"][n-1]["status"],"source-missing")
        self.assertEqual([x["record_count"] for x in parsed["sections"]],[14]*5)

    def test_thinaimalai_actual_153_record_inventory(self):
        raw=(Path(__file__).parents[1]/"sources/raw-html/pathinenkilkanakku/pmuni0056.html").read_bytes()
        parsed=parse_thinaimalai_nutraimbathu(raw)
        self.assertEqual(len(parsed["poems"]),153)
        self.assertEqual([x["record_count"] for x in parsed["sections"]],
                         [31,31,30,31,30])
        self.assertEqual(parsed["additional_unnumbered_literary_text"]["heading_as_printed"],
                         "சிறப்புப் பாயிரம்")
        self.assertEqual(len(parsed["additional_unnumbered_literary_text"]["lines"]),4)

    def test_remaining_programme_source_grammars(self):
        root=Path(__file__).parents[1]/"sources/raw-html/pathinenkilkanakku"
        cases=[
          (parse_thinaimozhi_aimpathu,"pmuni0027.html",50,5),
          (parse_tirikatukam,"pmuni0048.html",100,0),
          (parse_acharakkovai,"pmuni0024.html",100,0),
          (parse_pazhamozhi_nanuru,"pmuni0036.html",399,33),
          (parse_sirupanchamulam,"pmuni0029.html",98,0),
          (parse_muthumozhi_kanchi,"pmuni0025.html",100,10),
          (parse_elati,"pmuni0029.html",80,0),
          (parse_kainnilai,"pmuni0051.html",60,4)]
        for parser,name,count,sections in cases:
            parsed=parser((root/name).read_bytes())
            self.assertEqual(len(parsed["poems"]),count)
            self.assertEqual(len(parsed["sections"]),sections)
            self.assertTrue(all(x["lines"] for x in parsed["poems"]))

    def test_printed_heading_absences_are_not_invented(self):
        root=Path(__file__).parents[1]/"sources/raw-html/pathinenkilkanakku"
        tri=parse_tirikatukam((root/"pmuni0048.html").read_bytes())
        self.assertIsNone(tri["poems"][42]["heading_as_printed"])
        self.assertIsNone(tri["poems"][56]["heading_as_printed"])
        ach=parse_acharakkovai((root/"pmuni0024.html").read_bytes())
        self.assertIsNone(ach["poems"][46]["heading_as_printed"])

    def test_pazhamozhi_printed_inventory_is_explicit(self):
        raw=(Path(__file__).parents[1]/"sources/raw-html/pathinenkilkanakku/pmuni0036.html").read_bytes()
        parsed=parse_pazhamozhi_nanuru(raw)
        self.assertEqual([p["poem_number"] for p in parsed["poems"]],list(range(1,400)))
        self.assertNotIn(12,[x["sequence"] for x in parsed["sections"]])

    def test_kainnilai_does_not_invent_fifth_heading(self):
        raw=(Path(__file__).parents[1]/"sources/raw-html/pathinenkilkanakku/pmuni0051.html").read_bytes()
        parsed=parse_kainnilai(raw)
        self.assertEqual(len(parsed["sections"]),4)
        self.assertEqual(parsed["sections"][-1]["record_count"],24)

    def test_poem_number_recognition(self): self.assertEqual(recognize_poem_heading("125.குறிஞ்சி - (?)")[0],125)
    def test_tamil_heading_recognition(self): self.assertEqual(recognize_poem_heading("1 குறிஞ்சி - கபிலர்"),(1,"குறிஞ்சி","கபிலர்"))
    def test_section_heading_recognition(self): self.assertIsNone(recognize_poem_heading("நூல்"))
    def test_preserves_tamil(self):
        d=parse_natrinai_html(FIX.read_bytes()); self.assertEqual(d["poems"][0]["lines"][0],"நின்ற சொல்லர் நீடுதோறு இனியர்")
    def test_prefatory_heading_recognition(self):
        raw="<p>கடவுள் வாழ்த்து</p><p>மா நிலம் சேவடி ஆக தூநீர்</p><p>1 குறிஞ்சி - கபிலர்</p><p>வரி</p>".encode()
        self.assertEqual(parse_natrinai_html(raw)["prefatory_text"]["lines"],["மா நிலம் சேவடி ஆக தூநீர்"])
    def test_unicode_normalization(self): self.assertEqual(unicodedata.normalize("NFC","கொ"),"கொ")
    def test_boilerplate_removal(self):
        d=parse_natrinai_html(FIX.read_bytes()); self.assertNotIn("Project Madurai"," ".join(d["poems"][0]["lines"]))
    def test_duplicate_number_detection_fixture(self):
        d=parse_natrinai_html(b"<p>1 x - y</p><p>a</p><p>1 x - y</p><p>b</p>"); self.assertEqual(d["duplicate_html_nodes_ignored"],[1])
    def test_missing_number_detection(self):
        nums={p["poem_number"] for p in parse_natrinai_html(FIX.read_bytes())["poems"]}; self.assertEqual([n for n in range(1,5) if n not in nums],[3])
    def test_frontmatter_generation(self):
        poem=parse_natrinai_html(FIX.read_bytes())["poems"][0]; md=poem_markdown(poem,"https://example.test","source.html"); self.assertIn("poem_number: 1",md)
    def test_manifest_columns(self):
        expected="work work_id work_slug poem_number poem_number_as_printed source_order section major_division major_division_as_printed pattu pattu_sequence position_within_pattu thinai speaker poet first_line line_count textual_status canonical_text_available candidate_texts_available lacuna_present lacuna_location source_note_available extraction_status body_hash_sha256 normalized_body_duplicate shared_first_line source_body_hash_sha256 markdown_body_hash_sha256 source_output_match source_url source_object_id source_file markdown_file validation_status issue_count notes".split()
        from build_manifest import FIELDS; self.assertEqual(FIELDS,expected)

    def test_poem_234_lost_not_extraction_failure(self):
        fm,body=read_frontmatter(Path(__file__).parents[1]/"corpus/natrinai/poems/234.md")
        self.assertEqual(fm["textual_status"],"lost"); self.assertFalse(fm["canonical_text_available"])
        self.assertTrue(fm["candidate_texts_available"]); self.assertEqual(fm["extraction_status"],"success")

    def test_poem_234_candidates_only_in_source_note(self):
        _,body=read_frontmatter(Path(__file__).parents[1]/"corpus/natrinai/poems/234.md")
        canonical,note=body.split("## Source note (as printed)",1)
        self.assertNotIn("சான்றோர் வருந்திய வருத்தமும்",canonical); self.assertIn("சான்றோர் வருந்திய வருத்தமும்",note)
        self.assertIn("நெருநலும் முன்னாள் எல்லையும் ஒருசிறை",note)

    def test_poem_385_incomplete_and_placeholders_preserved(self):
        fm,body=read_frontmatter(Path(__file__).parents[1]/"corpus/natrinai/poems/385.md")
        self.assertEqual(fm["textual_status"],"incomplete"); self.assertTrue(fm["lacuna_present"])
        self.assertEqual(fm["lacuna_location"],"ending"); self.assertIn("- - - - - - - -",body)

    def test_shared_first_lines_are_info(self):
        report=json.loads((Path(__file__).parents[1]/"manifests/natrinai-validation-report.json").read_text())
        shared=[x for x in report["issues"] if x["issue_type"]=="shared_first_line"]
        self.assertEqual(len(shared),4); self.assertTrue(all(x["severity"]=="info" for x in shared))

    def test_different_full_bodies_are_not_duplicates(self):
        root=Path(__file__).parents[1]/"corpus/natrinai/poems"
        for a,b in [(7,268),(15,203),(153,346),(205,399)]:
            _,ba=read_frontmatter(root/f"{a:03d}.md"); _,bb=read_frontmatter(root/f"{b:03d}.md")
            self.assertNotEqual(body_hash([x for x in ba.splitlines() if x and not x.startswith("#")]),
                                body_hash([x for x in bb.splitlines() if x and not x.startswith("#")]))

    def test_source_to_markdown_fidelity(self):
        report=json.loads((Path(__file__).parents[1]/"manifests/natrinai-validation-report.json").read_text())
        self.assertEqual(len(report["source_output_fidelity"]),400)
        self.assertTrue(all(x["source_output_match"] and x["source_note_match"] for x in report["source_output_fidelity"]))

    def test_field_provenance(self):
        fm,_=read_frontmatter(Path(__file__).parents[1]/"corpus/natrinai/poems/008.md")
        self.assertEqual(fm["thinai_source"],"Project Madurai heading")
        self.assertEqual(fm["poet_source"],"Project Madurai heading marked uncertain")
        self.assertEqual(fm["poet_as_printed"],"(?)"); self.assertIsNone(fm["speaker_source"])

    def test_apparatus_cannot_replace_canonical_text(self):
        apparatus=json.loads((Path(__file__).parents[1]/"apparatus/natrinai/source-comparison.json").read_text())
        self.assertFalse(apparatus["canonical_corpus_modified"])
        self.assertTrue(all("canonical_text" not in record for record in apparatus["records"]))
        self.assertTrue(all("No change" in record["canonical_action"] or "Retain" in record["canonical_action"] for record in apparatus["records"]))

    def test_readme_required_sections(self):
        text=(Path(__file__).parents[1]/"README.md").read_text()
        required=["Project purpose","Python and installation","Repository tree","Commands","Raw-source preservation",
                  "Unicode normalization","Poem splitting","Poem metadata","Manifests","Validation rules",
                  "Severity levels","Manual review process","External comparison sources","Adding the next Project Madurai work",
                  "Canonical transcription versus editorial apparatus"]
        for heading in required: self.assertIn(heading,text)

    def test_recursive_audit_rejects_copy_suffixes_with_complete_canonical_inventory(self):
        fixture=Path(__file__).parent/"fixtures/duplicate_inventory"
        with tempfile.TemporaryDirectory() as td:
            root=Path(td); poems=root/"corpus/natrinai/poems"; sections=root/"corpus/natrinai/sections"
            poems.mkdir(parents=True); sections.mkdir(parents=True)
            template="---\npoem_number: {number}\n---\n\n# Test {number}\n\nவரி\n"
            for number in range(1,401):
                (poems/f"{number:03d}.md").write_text(template.format(number=number),encoding="utf-8")
            for start in range(1,401,50):
                (sections/f"{start:03d}-{start+49:03d}.md").write_text("# section\n",encoding="utf-8")
            for source in fixture.glob("*.md"):
                shutil.copy2(source,poems/source.name)
            report=audit(root)
            self.assertEqual(report["status"],"fail")
            self.assertEqual(report["poem_markdown_count"],403)
            self.assertEqual(sorted(report["unexpected_poem_filenames"]),["002 2.md","003 2.md","003 3.md"])
            self.assertEqual(set(report["duplicate_yaml_poem_numbers"]),{"2","3"})

    def test_recursive_audit_rejects_nested_poem_copy(self):
        with tempfile.TemporaryDirectory() as td:
            root=Path(td);poems=root/"corpus/natrinai/poems";sections=root/"corpus/natrinai/sections"
            poems.mkdir(parents=True);sections.mkdir(parents=True)
            template="---\npoem_number: {number}\n---\n\n# Test {number}\n\nவரி\n"
            for number in range(1,401):(poems/f"{number:03d}.md").write_text(template.format(number=number),encoding="utf-8")
            for start in range(1,401,50):(sections/f"{start:03d}-{start+49:03d}.md").write_text("# section\n",encoding="utf-8")
            nested=poems/"nested";nested.mkdir();(nested/"002.md").write_text(template.format(number=2),encoding="utf-8")
            report=audit(root)
            self.assertEqual(report["status"],"fail")
            self.assertIn("nested/002.md",report["unexpected_poem_filenames"])
            self.assertEqual(report["duplicate_yaml_poem_numbers"]["2"],["corpus/natrinai/poems/002.md","corpus/natrinai/poems/nested/002.md"])

    def test_aingurunuru_source_parses_all_records(self):
        raw=(Path(__file__).parents[1]/"sources/raw-html/aingurunuru.html").read_bytes()
        parsed=parse_aingurunuru_html(raw)
        self.assertEqual(len(parsed["poems"]),500); self.assertEqual(parsed["missing_numbers"],[])

    def test_aingurunuru_pattu_headings_and_membership(self):
        parsed=parse_aingurunuru_html((Path(__file__).parents[1]/"sources/raw-html/aingurunuru.html").read_bytes())
        self.assertEqual(len(parsed["pattu_groups"]),50)
        p21=parsed["poems"][20]; self.assertEqual(p21["pattu"],"கள்வன் பத்து"); self.assertEqual(p21["position_within_pattu"],1)
        self.assertTrue(all(g["poem_record_count"]==10 for g in parsed["pattu_groups"]))

    def test_aingurunuru_lost_records(self):
        for n in (129,130):
            fm,body=read_frontmatter(Path(__file__).parents[1]/f"corpus/aingurunuru/poems/{n:03d}.md")
            self.assertEqual(fm["textual_status"],"lost"); self.assertFalse(fm["canonical_text_available"])
            self.assertEqual(fm["extraction_status"],"success"); self.assertIn("கிடைக்காத பாடல்",body)

    def test_aingurunuru_body_and_note_fidelity(self):
        r=json.loads((Path(__file__).parents[1]/"manifests/aingurunuru-validation-report.json").read_text())
        self.assertEqual(r["source_output_matches"],500); self.assertEqual(r["source_note_matches"],500)

    def test_aingurunuru_bare_470_heading_preserved(self):
        fm,body=read_frontmatter(Path(__file__).parents[1]/"corpus/aingurunuru/poems/470.md")
        self.assertEqual(fm["poem_number"],470); self.assertIn("இருநிலம் குளிர்ப்ப வீசி அல்கலும்",body)

    def test_aingurunuru_ordinal_anomalies_not_repaired(self):
        inv=json.loads((Path(__file__).parents[1]/"corpus/aingurunuru/pattu-inventory.json").read_text())
        self.assertEqual(inv[11]["printed_ordinal"],11); self.assertFalse(inv[11]["ordinal_consistent"])
        self.assertEqual(inv[12]["printed_ordinal"],12); self.assertFalse(inv[12]["ordinal_consistent"])

    def test_natrinai_integrity_snapshot_still_matches(self):
        snap=json.loads((Path(__file__).parents[1]/"logs/natrinai-pre-aingurunuru-integrity.json").read_text())
        import hashlib
        root=Path(__file__).parents[1]/"corpus/natrinai/poems"
        for n,h in snap["body_hashes"].items():
            _,body=read_frontmatter(root/f"{int(n):03d}.md")
            lines=[x.strip() for x in body.split("## Source note (as printed)",1)[0].splitlines() if x.strip() and not x.startswith("# ")]
            self.assertEqual(body_hash(lines),h)

    def test_kuruntokai_complete_number_inventory(self):
        p=parse_kuruntokai_html((Path(__file__).parents[1]/"sources/raw-html/kuruntokai.html").read_bytes())
        self.assertEqual(len(p["poems"]),401);self.assertEqual(p["missing_numbers"],[]);self.assertEqual(p["duplicate_numbers"],[])

    def test_kuruntokai_heading_fields_preserve_anomalies(self):
        p=parse_kuruntokai_html((Path(__file__).parents[1]/"sources/raw-html/kuruntokai.html").read_bytes())
        self.assertEqual(p["poems"][28]["speaker"],"தலைன் கூற்று")
        self.assertEqual(p["poems"][395]["thinai"],"பாால")

    def test_kuruntokai_layout_only_attribution_split(self):
        p=parse_kuruntokai_html((Path(__file__).parents[1]/"sources/raw-html/kuruntokai.html").read_bytes())
        for n,poet in [(105,"நக்கீரர்"),(180,"கச்சிப்பேட்டு நன்னாகையார்")]:
            self.assertEqual(p["poems"][n-1]["poet"],poet);self.assertFalse(p["poems"][n-1]["lines"][-1].startswith("-"))

    def test_kuruntokai_unknown_poet_placeholder_is_null(self):
        fm,_=read_frontmatter(Path(__file__).parents[1]/"corpus/kuruntokai/poems/191.md")
        self.assertIsNone(fm["poet"]);self.assertEqual(fm["poet_as_printed"],"-..........");self.assertIn("placeholder",fm["poet_source"])

    def test_kuruntokai_fidelity_and_shared_openings(self):
        r=json.loads((Path(__file__).parents[1]/"manifests/kuruntokai-validation-report.json").read_text())
        self.assertEqual(r["source_output_matches"],401);self.assertEqual(r["source_note_matches"],401)
        self.assertEqual(r["duplicate_full_bodies"],[]);self.assertEqual(r["shared_first_lines"],[[104,287],[246,313]])

    def test_kuruntokai_navigation_is_mechanical(self):
        fm,_=read_frontmatter(Path(__file__).parents[1]/"corpus/kuruntokai/poems/401.md")
        self.assertEqual(fm["section"],"401-401");self.assertIn("Mechanical navigation",fm["section_source"])

    def test_akananuru_source_parses_complete_inventory(self):
        p=parse_akananuru_html((Path(__file__).parents[1]/"sources/raw-html/akananuru.html").read_bytes())
        self.assertEqual(len(p["poems"]),400);self.assertEqual(p["canonical_missing_numbers"],[])
        self.assertEqual([x["poem_number"] for x in p["poems"]],list(range(1,401)))

    def test_akananuru_invocation_and_printed_divisions(self):
        p=parse_akananuru_html((Path(__file__).parents[1]/"sources/raw-html/akananuru.html").read_bytes())
        self.assertEqual(p["prefatory_text"]["number_as_printed"],0)
        self.assertEqual(len(p["prefatory_text"]["lines"]),16)
        self.assertEqual([(x["poem_start"],x["poem_end"]) for x in p["printed_divisions"]],[(1,120),(121,300),(301,400)])

    def test_akananuru_printed_number_anomalies_preserved(self):
        p=parse_akananuru_html((Path(__file__).parents[1]/"sources/raw-html/akananuru.html").read_bytes())
        self.assertEqual(p["printed_number_missing"],[131,319]);self.assertEqual(p["printed_number_duplicates"],[130,318])
        self.assertEqual(p["poems"][130]["poem_number_as_printed"],130)
        self.assertEqual(p["poems"][318]["poem_number_as_printed"],318)

    def test_akananuru_malformed_record_174_is_not_lost(self):
        p=parse_akananuru_html((Path(__file__).parents[1]/"sources/raw-html/akananuru.html").read_bytes())
        self.assertEqual(p["poems"][173]["poem_number"],174);self.assertEqual(p["poems"][173]["poem_number_as_printed"],174)
        self.assertTrue(p["poems"][173]["lines"])

    def test_akananuru_layout_markers_and_ellipsis_policy(self):
        p=parse_akananuru_html((Path(__file__).parents[1]/"sources/raw-html/akananuru.html").read_bytes())
        for n in (129,246,399):self.assertNotRegex(p["poems"][n-1]["lines"][-1],r"\.\s*\d+-\d+$")
        self.assertTrue(any("..." in line for line in p["poems"][142]["lines"]))
        self.assertTrue(any("..." in line for line in p["poems"][353]["lines"]))

    def test_akananuru_shared_opening_not_duplicate_body(self):
        p=parse_akananuru_html((Path(__file__).parents[1]/"sources/raw-html/akananuru.html").read_bytes())
        self.assertEqual(p["shared_first_lines"],[[121,122]]);self.assertEqual(p["duplicate_bodies"],[])

    def test_akananuru_generated_schema_and_fidelity(self):
        fm,_=read_frontmatter(Path(__file__).parents[1]/"corpus/akananuru/poems/131.md")
        self.assertEqual(fm["poem_number"],131);self.assertEqual(fm["poem_number_as_printed"],130)
        self.assertIsNone(fm["thinai"]);self.assertIsNone(fm["speaker"]);self.assertIsNone(fm["poet"])
        r=json.loads((Path(__file__).parents[1]/"manifests/akananuru-validation-report.json").read_text())
        self.assertEqual(r["source_output_matches"],400);self.assertEqual(r["source_note_matches"],400)

    def test_akananuru_source_division_files_are_exact(self):
        root=Path(__file__).parents[1]/"corpus/akananuru/sections"
        self.assertEqual({x.name for x in root.glob("*.md")},{"001-120.md","121-300.md","301-400.md"})

    def test_purananuru_complete_record_inventory_and_losses(self):
        parsed=parse_purananuru_text((Path(__file__).parents[1]/"sources/purananuru.md").read_bytes())
        self.assertEqual(len(parsed["poems"]),400);self.assertEqual(parsed["missing_numbers"],[])
        self.assertEqual(parsed["source_lost_poems"],[267,268])

    def test_purananuru_printed_metadata_and_null_speaker(self):
        fm,_=read_frontmatter(Path(__file__).parents[1]/"corpus/purananuru/poems/002.md")
        self.assertEqual(fm["thinai"],"பாடாண்");self.assertEqual(fm["poet"],"முரஞ்சியூர் முடிநாகராயர்")
        self.assertIsNone(fm["speaker"])

    def test_purananuru_lost_and_lacuna_evidence(self):
        for n in (267,268):
            fm,body=read_frontmatter(Path(__file__).parents[1]/f"corpus/purananuru/poems/{n:03d}.md")
            self.assertEqual(fm["textual_status"],"lost");self.assertFalse(fm["canonical_text_available"])
            self.assertIn("267- 268 கிடைத்தில",body)
        fm,body=read_frontmatter(Path(__file__).parents[1]/"corpus/purananuru/poems/340.md")
        self.assertEqual(fm["textual_status"],"incomplete");self.assertTrue(fm["lacuna_present"]);self.assertIn(".. ..",body)

    def test_purananuru_fidelity_and_mechanical_sections(self):
        report=json.loads((Path(__file__).parents[1]/"manifests/purananuru-validation-report.json").read_text())
        self.assertEqual(report["source_output_matches"],400);self.assertEqual(report["source_note_matches"],400);self.assertEqual(report["errors"],0)
        root=Path(__file__).parents[1]/"corpus/purananuru/sections"
        self.assertEqual({x.name for x in root.glob("*.md")},{f"{n:03d}-{n+49:03d}.md" for n in range(1,401,50)})

    def test_pattuppattu_ten_source_objects_in_canonical_order(self):
        _,objects=verify_source_set()
        self.assertEqual(len(objects),10)
        self.assertEqual([x["record_number"] for x in objects],list(range(1,11)))
        self.assertEqual([x["source_object_id"] for x in objects],
                         ["pmuni0067","pmuni0063","pmuni0064","pmuni0069","pmuni0488",
                          "pmuni0071","pmuni0070","pmuni0073","pmuni0077","pmuni0078"])

    def test_pattuppattu_individual_source_checksums_are_pinned(self):
        _,objects=verify_source_set()
        self.assertEqual(len({x["source_sha256"] for x in objects}),10)
        self.assertTrue(all(len(x["source_sha256"])==64 for x in objects))

    def test_pattuppattu_checksum_mismatch_fails(self):
        with mock.patch("pattuppattu_pipeline._sha256",return_value="0"*64):
            with self.assertRaisesRegex(RuntimeError,"checksum/size mismatch"):
                verify_source_set()

    def test_pattuppattu_missing_source_object_fails(self):
        original=Path.is_file
        def selective(path):
            return False if path.name=="pmuni0067.html" else original(path)
        with mock.patch.object(Path,"is_file",selective):
            with self.assertRaisesRegex(RuntimeError,"Missing or empty source object"):
                verify_source_set()

    def test_pattuppattu_duplicate_source_object_id_fails(self):
        import pattuppattu_pipeline as pp
        source=json.loads(pp.SOURCE_SET.read_text(encoding="utf-8"))
        source["source_objects"][1]["source_object_id"]=source["source_objects"][0]["source_object_id"]
        with tempfile.TemporaryDirectory() as td:
            candidate=Path(td)/"source-set.json"
            candidate.write_text(json.dumps(source,ensure_ascii=False),encoding="utf-8")
            with mock.patch.object(pp,"SOURCE_SET",candidate):
                with self.assertRaisesRegex(RuntimeError,"Duplicate source object ID"):
                    pp.verify_source_set()

    def test_pattuppattu_one_long_poem_per_record(self):
        parsed=parse_all()
        self.assertEqual(len(parsed["poems"]),10)
        self.assertTrue(all(x["record_type"]=="long_poem" and x["lines"] for x in parsed["poems"]))

    def test_pattuppattu_mullai_commentary_is_excluded(self):
        mullai=parse_all()["poems"][4]
        self.assertEqual(len(mullai["lines"]),103)
        self.assertTrue(mullai["commentary_present"])
        self.assertEqual(mullai["lines"][-1],"வினைவிளங்கு நெடுந்தேர் பூண்ட மாவே.")
        self.assertNotIn(mullai["commentary_boundary"]["commentary_first_line_as_printed"],mullai["lines"])

    def test_pattuppattu_tirumurukarruppatai_internal_structure(self):
        first=parse_all()["poems"][0]
        self.assertEqual(len(first["lines"]),317)
        numbered=[x for x in first["internal_structure"] if x["heading_as_printed"][0].isdigit()]
        self.assertEqual(len(numbered),6)
        self.assertEqual(numbered[0]["heading_as_printed"],"1. திருப்பரங்குன்றம்")
        self.assertEqual(numbered[-1]["heading_as_printed"],"6. பழமுதிர் சோலை")

    def test_pattuppattu_layout_numbers_are_not_literary_text(self):
        for poem in parse_all()["poems"]:
            self.assertTrue(all(not __import__("re").search(r"[ \u00a0]+(?:\.\s*)*\d{1,3}$",line)
                                for line in poem["lines"]))

    def test_pattuppattu_generated_schema_and_provenance(self):
        for n in range(1,11):
            fm,_=read_frontmatter(Path(__file__).parents[1]/f"corpus/pattuppattu/poems/{n:03d}.md")
            self.assertEqual(fm["record_type"],"long_poem")
            self.assertEqual(fm["source_object_order"],n)
            self.assertEqual(len(fm["source_sha256"]),64)
            self.assertEqual(fm["extraction_status"],"success")

    def test_pattuppattu_fidelity(self):
        report=json.loads((Path(__file__).parents[1]/"manifests/pattuppattu-validation-report.json").read_text())
        self.assertEqual(report["source_output_matches"],10)
        self.assertEqual(report["source_note_matches"],10)
        self.assertEqual(report["duplicate_full_bodies"],[])

    def test_pattuppattu_navigation_inventory(self):
        names={x.name for x in (Path(__file__).parents[1]/"corpus/pattuppattu/sections").glob("*.md")}
        self.assertEqual(names,{"001-pmuni0067.md","002-pmuni0063.md","003-pmuni0064.md",
                                "004-pmuni0069.md","005-pmuni0488.md","006-pmuni0071.md",
                                "007-pmuni0070.md","008-pmuni0073.md","009-pmuni0077.md",
                                "010-pmuni0078.md"})

    def test_pattuppattu_is_frozen(self):
        metadata=json.loads((Path(__file__).parents[1]/"corpus/pattuppattu/metadata.json").read_text())
        self.assertEqual(metadata["corpus_schema_version"],"1.0.0")
        self.assertEqual(metadata["version_status"],"frozen")

    def test_patirruppattu_surviving_inventory(self):
        parsed=parse_patirruppattu()
        self.assertEqual([x["poem_number"] for x in parsed["poems"]],list(range(11,91)))
        self.assertEqual([(x["sequence"],x["record_count"]) for x in parsed["pattu_groups"]],[(n,10) for n in range(2,10)])

    def test_patirruppattu_lost_groups_not_manufactured(self):
        parsed=parse_patirruppattu()
        self.assertEqual([x["sequence"] for x in parsed["lost_groups"]],[1,10])
        self.assertEqual(len(parsed["poems"]),80)

    def test_patirruppattu_group_and_poem_metadata(self):
        parsed=parse_patirruppattu();p=parsed["poems"][0]
        self.assertEqual(p["pattu_sequence"],2);self.assertEqual(p["position_within_pattu"],1)
        self.assertEqual(p["poet"],"குமட்டூர்க் கண்ணனார்")
        self.assertEqual(p["title_as_printed"],"புண்ணுமிழ் குருதி (அடி 8)")

    def test_patirruppattu_fragments_are_not_poems(self):
        parsed=parse_patirruppattu()
        self.assertTrue(parsed["recovered_fragments_as_printed"])
        self.assertFalse(any(x["poem_number"]>90 for x in parsed["poems"]))

    def test_paripatal_main_and_tirattu_inventory(self):
        parsed=parse_paripatal()
        self.assertEqual(len(parsed["poems"]),35)
        self.assertEqual([x["poem_number_as_printed"] for x in parsed["poems"][:22]],list(range(1,23)))
        self.assertEqual([x["poem_number_as_printed"] for x in parsed["poems"][22:]],list(range(1,14)))

    def test_paripatal_tirattu_is_separate_source_division(self):
        parsed=parse_paripatal()
        self.assertTrue(all(x["record_type"]=="numbered_poem" for x in parsed["poems"][:22]))
        self.assertTrue(all(x["record_type"]=="tirattu_fragment" for x in parsed["poems"][22:]))
        self.assertEqual([x["record_count"] for x in parsed["source_divisions"]],[22,13])

    def test_paripatal_markup_boundaries_and_fidelity(self):
        parsed=parse_paripatal()
        self.assertNotIn("அரு மறைப் பொருள்",parsed["poems"][0]["lines"])
        self.assertIn("அரு மறைப் பொருள்",[x["heading_as_printed"] for x in parsed["poems"][0]["internal_structure"]])
        report=json.loads((Path(__file__).parents[1]/"manifests/paripatal-validation-report.json").read_text())
        self.assertEqual((report["source_output_matches"],report["source_note_matches"]),(35,35))

    def test_frontmatter_delimiter_is_line_anchored(self):
        fm,_=read_frontmatter(Path(__file__).parents[1]/"corpus/paripatal/poems/008.md")
        self.assertEqual(fm["line_count"],131)
        self.assertIn("---",fm["first_line"])

    def test_kalittokai_table_row_inventory(self):
        parsed=parse_kalittokai()
        self.assertEqual([x["poem_number"] for x in parsed["poems"]],list(range(1,151)))
        self.assertEqual(len(parsed["poems"]),150)

    def test_kalittokai_source_divisions(self):
        parsed=parse_kalittokai()
        self.assertEqual([(x["start"],x["end"],x["record_count"]) for x in parsed["source_divisions"]],
                         [(1,1,1),(2,36,35),(37,65,29),(66,100,35),(101,117,17),(118,150,33)])
        self.assertEqual(parsed["poems"][36]["poet"],"கபிலர்")

    def test_kalittokai_printed_lacunae(self):
        parsed=parse_kalittokai()
        lacunae=[x["poem_number"] for x in parsed["poems"] if x["lacuna_present"]]
        self.assertEqual(lacunae,[114,131])
        self.assertTrue(any("..." in line for line in parsed["poems"][113]["lines"]))

    def test_pattuppattu_declared_line_count_discrepancies_are_explicit(self):
        metadata=json.loads((Path(__file__).parents[1]/"corpus/pattuppattu/metadata.json").read_text())
        pairs={x["source_object_id"]:(x["declared_line_count_as_printed"],x["extracted_literary_line_count"])
               for x in metadata["declared_and_extracted_line_counts"]}
        self.assertEqual(pairs["pmuni0069"],(500,501))
        self.assertEqual(pairs["pmuni0073"],(261,262))
        self.assertEqual(pairs["pmuni0077"],(301,302))

    def test_unknown_work_parser_dispatch_fails(self):
        with self.assertRaises(ValueError):parse_work_html("unsupported-work",b"")

if __name__=="__main__": unittest.main()
