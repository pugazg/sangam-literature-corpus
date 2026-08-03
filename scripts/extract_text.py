#!/usr/bin/env python3
from __future__ import annotations
import argparse
from bs4 import BeautifulSoup
import json
from corpuslib import ensure_dirs, parse_work_html, paths, sha256, write_json, write_text

def extract(work: str, force=False, dry_run=False, verbose=False):
    if work in {"tirukkural","naladiyar","nanmanikkadigai","inna-narpathu","iniyavai-narpathu","kar-narpathu","kalavazhi-narpathu","aintinai-aimpathu","aintinai-elupathu","thinaimalai-nutraimbathu","thinaimozhi-aimpathu","tirikatukam","acharakkovai","pazhamozhi-nanuru","sirupanchamulam","muthumozhi-kanchi","elati","kainnilai"}:
        from pathinenkilkanakku_pipeline import extract as extract_pathinen
        return extract_pathinen(work, force=True, dry_run=dry_run, verbose=verbose)
    if work == "pattuppattu":
        from pattuppattu_pipeline import extract as extract_pattuppattu
        return extract_pattuppattu(force=True, dry_run=dry_run, verbose=verbose)
    if work == "patirruppattu":
        from patirruppattu_pipeline import extract as extract_patirruppattu
        return extract_patirruppattu(force=True, dry_run=dry_run, verbose=verbose)
    if work == "paripatal":
        from paripatal_pipeline import extract as extract_paripatal
        return extract_paripatal(force=True, dry_run=dry_run, verbose=verbose)
    if work == "kalittokai":
        from kalittokai_pipeline import extract as extract_kalittokai
        return extract_kalittokai(force=True, dry_run=dry_run, verbose=verbose)
    ensure_dirs(); p=paths(work); raw=p["raw_html"].read_bytes()
    if work == "purananuru":
        text=raw.decode("utf-8-sig")
    else:
        soup=BeautifulSoup(raw.decode("utf-8-sig"),"lxml")
        text=soup.get_text("\n")
    # First-pass text: entity-decoded and tags removed; otherwise not normalized.
    if dry_run: print(f"Would extract {len(raw)} source bytes"); return
    write_text(p["raw_txt"],text,force=force)
    parsed=parse_work_html(work,raw); write_json(p["parsed"],parsed,force=force)
    source_meta=json.loads(p["source_metadata"].read_text(encoding="utf-8"))
    if work == "purananuru":
        source_meta.update({"title_tamil_as_printed":"புறநானூறு", "title_romanized_as_printed":"puRanAnURu",
          "source_checksum_sha256":sha256(p["raw_html"]), "numbered_record_count":len(parsed["poems"]),
          "source_lost_poems":parsed["source_lost_poems"], "lacunose_poems":parsed["lacunose_poems"],
          "source_format":"User-supplied Markdown/text export of Project Madurai pmuni0057; not represented as raw HTML"})
        write_json(p["source_metadata"],source_meta,force=True)
        write_json(p["source_metadata"].with_name("purananuru-reconnaissance.json"), {
          "parser":parsed["parser"], "source_identifier":"pmuni0057", "source_url":source_meta["source_url"],
          "preserved_source":"sources/purananuru.md", "preserved_source_sha256":source_meta["source_checksum_sha256"],
          "source_format":source_meta["source_format"], "printed_numbered_records":400,
          "ordinary_numbered_headings":398, "source_lost_records":[267,268], "missing_canonical_numbers":parsed["missing_numbers"],
          "duplicate_numbers":parsed["duplicate_numbers"], "printed_divisions":[],
          "navigation_strategy":"mechanical 50-poem ranges", "lacunose_poems":parsed["lacunose_poems"],
          "shared_first_lines":parsed["shared_first_lines"], "duplicate_bodies":parsed["duplicate_bodies"],
          "unnumbered_invocation_present":False, "candidate_texts":[],
          "heading_anomalies":[{"poem_number":99,"printed_heading":"99.","condition":"topical title absent"}],
          "line_end_markers_detected":False,
          "html_anomalies":"Not applicable: preserved canonical input is a Markdown/text export, not raw HTML.",
          "heading_grammar":"number + topical title; followed by printed attribution/context metadata, blank line, literary body",
          "metadata_policy":"poet and tiṇai are copied only when printed; speaker remains null; addressee and tuṟai remain provenance-qualified",
          "observations":["The source explicitly prints 267- 268 கிடைத்தில.","Dot sequences inside literary bodies are preserved as printed lacuna evidence.","No source-printed anthology divisions were detected."]},force=True)
        if verbose: print(f"Detected {len(parsed['poems'])} records; lost {parsed['source_lost_poems']}; lacunose {parsed['lacunose_poems']}")
        return
    if work == "akananuru":
        source_meta.update({
          "title_tamil_as_printed":"அகநானுறு", "title_romanized_as_printed":"akanAnURu",
          "source_checksum_sha256":sha256(p["raw_html"]),
          "numbered_record_count":len(parsed["poems"]),
          "unnumbered_literary_record_count":1 if parsed.get("prefatory_text") else 0,
          "printed_divisions":parsed["printed_divisions"],
          "printed_numbering_anomalies":parsed["numbering_anomalies"],
        })
        write_json(p["source_metadata"],source_meta,force=True)
        if verbose: print(f"Detected {len(parsed['poems'])} numbered records, one unnumbered invocation, and {len(parsed['printed_divisions'])} printed divisions")
        return
    if work == "kuruntokai":
        source_meta.update({
          "title_tamil":"குறுந்தொகை", "title_romanized_as_printed":"kuRuntokai",
          "collection_as_printed":"எட்டுத்தொகை நூல்களில் ஒன்று - பல ஆசிரியர்கள்",
          "contributors_as_printed":["Etext preparation, HTML and PDF versions: Dr. K. Kalyanasundaram, Lausanne, Switzerland","Proof Reading : Ms. Sarala Sandirasegarane, Kanpur, India"],
          "rights_statement_as_printed":["© Project Madurai, 1998-2021.","You are welcome to freely distribute this file, provided this header page is kept intact"],
          "source_checksum_sha256":sha256(p["raw_html"]),
        })
        write_json(p["source_metadata"],source_meta,force=True)
        if verbose: print(f"Detected {len(parsed['poems'])} printed poem records")
        return
    if work == "aingurunuru":
        source_meta.update({
          "title_tamil":"ஐங்குறு நூறு", "title_romanized_as_printed":"aingurunUru",
          "collection_as_printed":"One of \"eTTutokai\" anthology",
          "nominal_poem_count_as_printed":"500 short poems (two are missing)",
          "ancient_compiler_as_printed":"kUdalUr kizhAr / கூடலூர் கிழார்",
          "royal_instance_as_printed":"Chera King \"yAnaikkatcEy mAntaran cEral irumporai\"",
          "electronic_text_compiler_as_printed":"வித்துவான் எம்.நாராயண வேலுப்பிள்ளை அவர்களால் தொகுக்கப்பட்டது",
          "rights_statement_as_printed":["© Project Madurai, 1998-2021.","You are welcome to freely distribute this file, provided this header page is kept intact"],
          "source_checksum_sha256":sha256(p["raw_html"]),
        })
        write_json(p["source_metadata"],source_meta,force=True)
        write_json(p["source_metadata"].with_name("aingurunuru-structure.json"), {
          "parser":parsed["parser"], "source_line_model":"HTML BR-delimited lines",
          "poem_records":len(parsed["poems"]), "pattu_groups":parsed["pattu_groups"],
          "major_divisions":parsed["major_divisions"],
          "observations":["The source prints no pattu heading before poems 1 and 11.",
            "The heading before poem 111 repeats printed ordinal 11.",
            "The heading before poem 121 is printed with ordinal 12 although its source-order group is 13.",
            "Poems 129 and 130 are explicitly labelled கிடைக்காத பாடல்."],
        },force=True)
        if verbose: print(f"Detected {len(parsed['poems'])} printed poem records and {len(parsed['pattu_groups'])} ten-poem groups")
        return
    source_meta.update({
      "title_tamil":"நற்றிணை", "title_romanized_as_printed":"naRRiNa", "collection_as_printed":"எட்டுத்தொகை - சங்க நூல்",
      "compiler_as_printed":"அறியப்படவில்லை", "patron_as_printed":"பன்னாடு தந்த மாறன் வழுதி",
      "edition_and_contributors_as_printed":[
        "Etext - adding of descriptive notes to verses, Proof reading, Web versions in TSCII & Unicode: N D LogaSundaram & his daughter Ms. Selvanayagi - Chennai",
        "Bare Etext and PDF version: Dr. K. Kalyanasundaram, Lausanne, Switzerland"
      ],
      "introductory_notes_as_printed":parsed["metadata_lines"],
      "rights_statement_as_printed":["© Project Madurai 1998 - 2008","You are welcome to freely distribute this file, provided this header page is kept intact"]
    })
    write_json(p["source_metadata"],source_meta,force=True)
    if verbose: print(f"Detected {len(parsed['poems'])} printed poem records")

if __name__ == "__main__":
    ap=argparse.ArgumentParser(); ap.add_argument("--work",required=True); ap.add_argument("--force",action="store_true"); ap.add_argument("--dry-run",action="store_true"); ap.add_argument("--verbose",action="store_true")
    a=ap.parse_args(); extract(a.work,a.force,a.dry_run,a.verbose)
