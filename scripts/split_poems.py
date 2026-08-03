#!/usr/bin/env python3
from __future__ import annotations
import argparse, json
import yaml
from corpuslib import paths, poem_markdown, section_name, write_json

def _ainguru_markdown(poem, url, source_file):
    n=poem["poem_number"]; lines=poem["lines"]; lost=not bool(lines)
    fm={"schema_version":"1.0.0","work":"ஐங்குறு நூறு","work_english":"Aiṅkuṟunūṟu","work_id":"aingurunuru","work_slug":"aingurunuru",
      "poem_number":n,"major_division":poem["major_division"],"major_division_as_printed":None,
      "major_division_source":"Mechanical hundred-poem block; no division heading printed in source",
      "pattu":poem["pattu"],"pattu_as_printed":poem["pattu_as_printed"],"pattu_sequence":poem["pattu_sequence"],
      "pattu_source":"Project Madurai heading" if poem["pattu_as_printed"] else None,
      "position_within_pattu":poem["position_within_pattu"],"thinai":None,"thinai_source":None,
      "poet":None,"poet_source":None,"speaker":None,"speaker_source":None,
      "first_line":lines[0] if lines else "","line_count":len(lines),"textual_status":"lost" if lost else "complete",
      "canonical_text_available":not lost,"candidate_texts_available":False,"lacuna_present":False,"lacuna_location":None,
      "source_note_available":bool(poem["source_note_lines"]),"source_note_source":"Project Madurai printed poem heading" if poem["source_note_lines"] else None,
      "extraction_status":"success","source":"Project Madurai","source_url":url,"project_madurai_id":"pmuni0028",
      "source_file":source_file,"language":"Tamil","script":"Tamil","status":poem["status"],"editorial_changes":False}
    y=yaml.safe_dump(fm,allow_unicode=True,sort_keys=False,default_flow_style=False).strip()
    out=f"---\n{y}\n---\n\n# ஐங்குறு நூறு {n}\n\n"+"\n".join(lines)+"\n"
    if poem["source_note_lines"]: out+="\n## Source note (as printed)\n\n"+"\n".join(poem["source_note_lines"])+"\n"
    return out

def _split_aingurunuru(p,data,source_meta,force,dry_run,verbose):
    poems=data["poems"]; url=source_meta["source_url"]; source_file="sources/raw-html/aingurunuru.html"
    if dry_run: print(f"Would write {len(poems)} poem files and 50 pattu-group sections"); return
    p["poems"].mkdir(parents=True,exist_ok=True); p["sections"].mkdir(parents=True,exist_ok=True)
    expected_poems={f"{n:03d}.md" for n in range(1,501)}
    expected_sections={f"{n:03d}-{n+9:03d}.md" for n in range(1,501,10)}
    bad=[x for x in p["poems"].rglob("*") if x.is_file() and (x.parent!=p["poems"] or x.name not in expected_poems)]
    bad += [x for x in p["sections"].rglob("*") if x.is_file() and (x.parent!=p["sections"] or x.name not in expected_sections)]
    if bad: raise RuntimeError(f"Refusing regeneration with unexpected physical files: {[str(x.relative_to(p['corpus'])) for x in bad]}")
    for poem in poems:
        target=p["poems"]/f"{poem['poem_number']:03d}.md"
        if target.exists() and not force: raise FileExistsError(f"Refusing to overwrite {target}; pass --force")
        target.write_text(_ainguru_markdown(poem,url,source_file),encoding="utf-8",newline="\n")
    full=["# ஐங்குறு நூறு — Source transcription\n\nCanonical Project Madurai transcription; no literary corrections have been applied.\n"]
    for poem in poems: full.append(_ainguru_markdown(poem,url,source_file).split("---\n",2)[-1].lstrip())
    p["full_text"].write_text("\n".join(full),encoding="utf-8",newline="\n")
    for group in data["pattu_groups"]:
        start=group["poem_start"]; selected=[x for x in poems if start<=x["poem_number"]<=group["poem_end"]]
        heading=group["printed_heading"] or f"Source group {group['source_order']} (no printed பத்து heading)"
        content=[f"# {heading}\n"]+[ _ainguru_markdown(x,url,source_file).split("---\n",2)[-1].lstrip() for x in selected]
        (p["sections"]/f"{start:03d}-{group['poem_end']:03d}.md").write_text("\n".join(content),encoding="utf-8",newline="\n")
    metadata={"corpus_schema_version":"1.0.0","version_status":"frozen","title_tamil":"ஐங்குறு நூறு","title_english":"Aiṅkuṟunūṟu","work_slug":"aingurunuru","work_id":"aingurunuru","collection":"எட்டுத்தொகை",
      "title_romanized_as_printed":"aingurunUru","ancient_compiler":"கூடலூர் கிழார்","ancient_compiler_as_printed":"கூடலூர் கிழார் / kUdalUr kizhAr",
      "patron":"யானைக்கட்சேய் மாந்தரஞ்சேரல் இரும்பொறை","patron_as_printed":"Chera King yAnaikkatcEy mAntaran cEral irumporai",
      "electronic_text_compiler":"எம். நாராயண வேலுப்பிள்ளை","electronic_text_compiler_as_printed":"வித்துவான் எம்.நாராயண வேலுப்பிள்ளை அவர்களால் தொகுக்கப்பட்டது",
      "expected_poem_count":500,"available_poem_count":sum(bool(x["lines"]) for x in poems),"missing_poems":[x["poem_number"] for x in poems if not x["lines"]],
      "pattu_group_count":len(data["pattu_groups"]),"printed_pattu_heading_count":sum(bool(x["printed_heading"]) for x in data["pattu_groups"]),
      "source_name":"Project Madurai","source_url":url,"project_madurai_id":"pmuni0028","accessed_date":source_meta["accessed_date"],
      "source_checksum_sha256":source_meta["source_checksum_sha256"],"encoding":"UTF-8","normalization":"Unicode NFC","notes":["Poems 129 and 130 are explicitly printed as unavailable.","The source omits printed pattu headings before poems 1 and 11.","Printed pattu ordinal anomalies are preserved and reported."]}
    write_json(p["metadata"],metadata,force=True)
    write_json(p["corpus"]/"pattu-inventory.json",data["pattu_groups"],force=True)
    if verbose: print(f"Wrote {len(poems)} poem files and {len(data['pattu_groups'])} structural group files")

def _kuruntokai_markdown(poem,url,source_file):
    n=poem["poem_number"]; lines=poem["lines"]; unknown=poem["poet"] is None
    start=((n-1)//50)*50+1; section=f"{start:03d}-{min(start+49,401):03d}"
    fm={"schema_version":"1.0.0","work":"குறுந்தொகை","work_english":"Kuruntokai","work_id":"kuruntokai","work_slug":"kuruntokai",
      "poem_number":n,"section":section,"section_source":"Mechanical navigation range; no source division printed",
      "thinai":poem["thinai"],"thinai_as_printed":poem["thinai"],"thinai_source":"Project Madurai poem heading",
      "speaker":poem["speaker"],"speaker_as_printed":poem["speaker"],"speaker_source":"Project Madurai poem heading",
      "poet":poem["poet"],"poet_as_printed":poem["poet_as_printed"],
      "poet_source":"Project Madurai printed attribution placeholder" if unknown else "Project Madurai printed attribution",
      "first_line":lines[0] if lines else "","line_count":len(lines),"textual_status":"complete","canonical_text_available":True,
      "candidate_texts_available":False,"lacuna_present":False,"lacuna_location":None,"source_note_available":False,"source_note_source":None,
      "extraction_status":"success","source":"Project Madurai","source_url":url,"project_madurai_id":"pmuni0110","source_file":source_file,
      "language":"Tamil","script":"Tamil","status":poem["status"],"editorial_changes":False}
    y=yaml.safe_dump(fm,allow_unicode=True,sort_keys=False,default_flow_style=False).strip()
    return f"---\n{y}\n---\n\n# குறுந்தொகை {n}\n\n"+"\n".join(lines)+"\n"

def _split_kuruntokai(p,data,source_meta,force,dry_run,verbose):
    poems=data["poems"];url=source_meta["source_url"];source_file="sources/raw-html/kuruntokai.html"
    if dry_run: print(f"Would write {len(poems)} poem files and 9 mechanical sections");return
    p["poems"].mkdir(parents=True,exist_ok=True);p["sections"].mkdir(parents=True,exist_ok=True)
    ep={f"{n:03d}.md" for n in range(1,402)};es={f"{n:03d}-{min(n+49,401):03d}.md" for n in range(1,402,50)}
    bad=[x for x in p["poems"].rglob("*") if x.is_file() and (x.parent!=p["poems"] or x.name not in ep)]
    bad += [x for x in p["sections"].rglob("*") if x.is_file() and (x.parent!=p["sections"] or x.name not in es)]
    if bad: raise RuntimeError(f"Refusing regeneration with unexpected physical files: {[str(x.relative_to(p['corpus'])) for x in bad]}")
    for poem in poems:(p["poems"]/f"{poem['poem_number']:03d}.md").write_text(_kuruntokai_markdown(poem,url,source_file),encoding="utf-8",newline="\n")
    pref=data["prefatory_text"];full=["# குறுந்தொகை — Source transcription\n",f"## {pref['heading']}\n\n"+"\n".join(pref["lines"])+"\n\n"+(pref.get("poet_as_printed") or "")+"\n"]
    full += [_kuruntokai_markdown(x,url,source_file).split("---\n",2)[-1].lstrip() for x in poems]
    p["full_text"].write_text("\n".join(full),encoding="utf-8",newline="\n")
    for start in range(1,402,50):
        end=min(start+49,401);selected=[x for x in poems if start<=x["poem_number"]<=end]
        content=[f"# குறுந்தொகை {start:03d}–{end:03d}\n\nMechanical navigation range; no source division is asserted.\n"]
        content += [_kuruntokai_markdown(x,url,source_file).split("---\n",2)[-1].lstrip() for x in selected]
        (p["sections"]/f"{start:03d}-{end:03d}.md").write_text("\n".join(content),encoding="utf-8",newline="\n")
    meta={"corpus_schema_version":"1.0.0","version_status":"frozen","title_tamil":"குறுந்தொகை","title_english":"Kuruntokai","work_slug":"kuruntokai","work_id":"kuruntokai","collection":"எட்டுத்தொகை","title_romanized_as_printed":"kuRuntokai","expected_poem_count":401,"available_poem_count":401,"missing_poems":[],"source_name":"Project Madurai","source_url":url,"project_madurai_id":"pmuni0110","accessed_date":source_meta["accessed_date"],"source_checksum_sha256":source_meta["source_checksum_sha256"],"encoding":"UTF-8","normalization":"Unicode NFC","navigation_sections":{"type":"mechanical","range_size":50,"count":9},"notes":["The source prints no anthology divisions.","Tiṇai and speaker/context are copied from headings; poet attribution is printed after each poem.","Printed heading and attribution anomalies are preserved.","Version 1.0.0 freezes the verified source-faithful transcription and provenance representation; it does not assert that Project Madurai is a critical edition or that printed anomalies are philologically correct."]}
    write_json(p["metadata"],meta,force=True)
    if verbose:print(f"Wrote {len(poems)} poem files and 9 mechanical navigation sections")

def _akananuru_markdown(poem,url,source_file):
    n=poem["poem_number"]; lines=poem["lines"]
    ranges={1:"001-120",2:"121-300",3:"301-400"}
    section=ranges[poem["major_division_sequence"]]
    fm={"schema_version":"1.0.0","work":"அகநானுறு","work_english":"Akanāṉūṟu","work_id":"akananuru","work_slug":"akananuru",
      "poem_number":n,"poem_number_as_printed":poem["poem_number_as_printed"],"poem_number_source":"Project Madurai printed record label",
      "source_order":poem["source_order"],"section":section,"section_source":"Project Madurai printed macro-division",
      "major_division":poem["major_division"],"major_division_as_printed":poem["major_division_as_printed"],
      "major_division_source":"Project Madurai printed division heading",
      "thinai":None,"thinai_source":None,"speaker":None,"speaker_source":None,"poet":None,"poet_source":None,"poet_as_printed":None,
      "first_line":lines[0] if lines else "","line_count":len(lines),"textual_status":"complete","canonical_text_available":True,
      "candidate_texts_available":False,"lacuna_present":False,"lacuna_location":None,"source_note_available":False,"source_note_source":None,
      "extraction_status":"success","source":"Project Madurai","source_url":url,"project_madurai_id":"pmuni0229",
      "source_object_id":"pmuni0229","source_object_order":1,"source_file":source_file,
      "language":"Tamil","script":"Tamil","status":poem["status"],"editorial_changes":False}
    y=yaml.safe_dump(fm,allow_unicode=True,sort_keys=False,default_flow_style=False).strip()
    return f"---\n{y}\n---\n\n# அகநானுறு {n}\n\n"+"\n".join(lines)+"\n"

def _split_akananuru(p,data,source_meta,force,dry_run,verbose):
    poems=data["poems"]; url=source_meta["source_url"]; source_file="sources/raw-html/akananuru.html"
    divisions=data["printed_divisions"]
    if dry_run: print(f"Would write {len(poems)} poem files and {len(divisions)} source-printed division sections"); return
    p["poems"].mkdir(parents=True,exist_ok=True); p["sections"].mkdir(parents=True,exist_ok=True)
    ep={f"{n:03d}.md" for n in range(1,401)}; es={"001-120.md","121-300.md","301-400.md"}
    bad=[x for x in p["poems"].rglob("*") if x.is_file() and (x.parent!=p["poems"] or x.name not in ep)]
    bad += [x for x in p["sections"].rglob("*") if x.is_file() and (x.parent!=p["sections"] or x.name not in es)]
    if bad: raise RuntimeError(f"Refusing regeneration with unexpected physical files: {[str(x.relative_to(p['corpus'])) for x in bad]}")
    for poem in poems:
        (p["poems"]/f"{poem['poem_number']:03d}.md").write_text(_akananuru_markdown(poem,url,source_file),encoding="utf-8",newline="\n")
    pref=data.get("prefatory_text") or {}
    full=["# அகநானுறு — Source transcription\n\nCanonical Project Madurai pmuni0229 transcription; no literary corrections have been applied.\n"]
    if pref:
        full.append(f"## {pref['heading']}\n\n"+"\n".join(pref["lines"])+"\n")
    for division in divisions:
        full.append(f"## {division['heading_as_printed']}\n")
        full += [_akananuru_markdown(x,url,source_file).split("---\n",2)[-1].lstrip() for x in poems if division["poem_start"]<=x["poem_number"]<=division["poem_end"]]
    p["full_text"].write_text("\n".join(full),encoding="utf-8",newline="\n")
    for division in divisions:
        selected=[x for x in poems if division["poem_start"]<=x["poem_number"]<=division["poem_end"]]
        content=[f"# {division['heading_as_printed']}\n\nProject Madurai source-printed macro-division.\n"]
        content += [_akananuru_markdown(x,url,source_file).split("---\n",2)[-1].lstrip() for x in selected]
        name=f"{division['poem_start']:03d}-{division['poem_end']:03d}.md"
        (p["sections"]/name).write_text("\n".join(content),encoding="utf-8",newline="\n")
    metadata={"corpus_schema_version":"1.0.0","version_status":"frozen","title_tamil":"அகநானுறு","title_tamil_normalized":"அகநானூறு",
      "title_english":"Akanāṉūṟu","work_slug":"akananuru","work_id":"akananuru","collection":"எட்டுத்தொகை",
      "title_romanized_as_printed":"akanAnURu","expected_poem_count":400,"numbered_poem_record_count":400,
      "available_poem_count":400,"missing_poems":[],"source_name":"Project Madurai","source_url":url,"project_madurai_id":"pmuni0229",
      "accessed_date":source_meta["accessed_date"],"source_checksum_sha256":source_meta["source_checksum_sha256"],
      "source_objects":source_meta["source_objects"],"encoding":"UTF-8","normalization":"Unicode NFC",
      "printed_division_count":3,"printed_numbering_anomalies":data["numbering_anomalies"],
      "notes":["The source prints an unnumbered literary invocation as record 0.",
        "The second records printed 130 and 318 occupy source-order positions 131 and 319; printed labels remain in provenance.",
        "The source prints no poem-level tiṇai, speaker/context, or poet attribution.",
        "Line-end numbers are HTML layout markers and are excluded from canonical literary bodies.",
        "Version 1.0.0 freezes the verified source-faithful transcription, source-order identity policy, exact printed-number provenance, record 0 handling, printed macrostructure, layout-marker exclusion, unresolved printed ellipses, and deterministic validation expectations; it does not assert a critical edition or infer absent poem-level metadata."]}
    write_json(p["metadata"],metadata,force=True)
    write_json(p["corpus"]/"structure-inventory.json",divisions,force=True)
    readme=p["corpus"]/"README.md"
    if not readme.exists():
        readme.write_text("# அகநானுறு (Akanāṉūṟu)\n\nUnfrozen onboarding transcription from Project Madurai `pmuni0229`. See `metadata.json` and the source reconnaissance record for provenance.\n",encoding="utf-8",newline="\n")
    if verbose: print(f"Wrote {len(poems)} poem files and {len(divisions)} source-printed division sections")

def _purananuru_markdown(poem,url,source_file):
    n=poem["poem_number"]; lines=poem["lines"]; lost=not bool(lines)
    start=((n-1)//50)*50+1; section=f"{start:03d}-{min(start+49,400):03d}"
    lacuna=bool(poem.get("lacuna_present"))
    fm={"schema_version":"1.0.0","work":"புறநானூறு","work_english":"Puṟanāṉūṟu","work_id":"purananuru","work_slug":"purananuru",
      "poem_number":n,"poem_number_as_printed":poem.get("poem_number_as_printed"),"poem_number_source":"Project Madurai printed heading or combined loss statement",
      "title_as_printed":poem.get("title_as_printed"),"section":section,"section_source":"Mechanical navigation range; no source division printed",
      "thinai":poem.get("thinai"),"thinai_as_printed":poem.get("thinai_as_printed"),"thinai_source":"Project Madurai printed metadata" if poem.get("thinai_as_printed") else None,
      "thurai":poem.get("thurai"),"thurai_source":"Project Madurai printed metadata" if poem.get("thurai") else None,
      "speaker":None,"speaker_source":None,"poet":poem.get("poet"),"poet_as_printed":poem.get("poet_as_printed"),
      "poet_source":"Project Madurai printed attribution" if poem.get("poet_as_printed") else None,
      "addressee_as_printed":poem.get("addressee_as_printed"),"addressee_source":"Project Madurai printed metadata" if poem.get("addressee_as_printed") else None,
      "first_line":lines[0] if lines else "","line_count":len(lines),"textual_status":"lost" if lost else "incomplete" if lacuna else "complete",
      "canonical_text_available":not lost,"candidate_texts_available":False,"lacuna_present":lacuna,"lacuna_location":"unspecified" if lacuna else None,
      "source_note_available":bool(poem["source_note_lines"]),"source_note_source":"Project Madurai printed heading metadata or loss statement" if poem["source_note_lines"] else None,
      "extraction_status":"success","source":"Project Madurai","source_url":url,"project_madurai_id":"pmuni0057","source_file":source_file,
      "language":"Tamil","script":"Tamil","status":poem["status"],"editorial_changes":False}
    y=yaml.safe_dump(fm,allow_unicode=True,sort_keys=False,default_flow_style=False).strip()
    out=f"---\n{y}\n---\n\n# புறநானூறு {n}\n\n"+"\n".join(lines)+"\n"
    if poem["source_note_lines"]: out+="\n## Source note (as printed)\n\n"+"\n".join(poem["source_note_lines"])+"\n"
    return out

def _split_purananuru(p,data,source_meta,force,dry_run,verbose):
    poems=data["poems"];url=source_meta["source_url"];source_file="sources/purananuru.md"
    if dry_run: print(f"Would write {len(poems)} poem files and 8 mechanical sections");return
    p["poems"].mkdir(parents=True,exist_ok=True);p["sections"].mkdir(parents=True,exist_ok=True)
    ep={f"{n:03d}.md" for n in range(1,401)};es={f"{n:03d}-{n+49:03d}.md" for n in range(1,401,50)}
    bad=[x for x in p["poems"].rglob("*") if x.is_file() and (x.parent!=p["poems"] or x.name not in ep)]
    bad += [x for x in p["sections"].rglob("*") if x.is_file() and (x.parent!=p["sections"] or x.name not in es)]
    if bad: raise RuntimeError(f"Refusing regeneration with unexpected physical files: {[str(x.relative_to(p['corpus'])) for x in bad]}")
    for poem in poems:(p["poems"]/f"{poem['poem_number']:03d}.md").write_text(_purananuru_markdown(poem,url,source_file),encoding="utf-8",newline="\n")
    full=["# புறநானூறு — Source transcription\n\nCanonical transcription from the preserved Project Madurai pmuni0057 text export; no literary corrections have been applied.\n"]
    full += [_purananuru_markdown(x,url,source_file).split("---\n",2)[-1].lstrip() for x in poems]
    p["full_text"].write_text("\n".join(full),encoding="utf-8",newline="\n")
    for start in range(1,401,50):
        end=start+49; selected=[x for x in poems if start<=x["poem_number"]<=end]
        content=[f"# புறநானூறு {start:03d}–{end:03d}\n\nMechanical navigation range; no source division is asserted.\n"]
        content += [_purananuru_markdown(x,url,source_file).split("---\n",2)[-1].lstrip() for x in selected]
        (p["sections"]/f"{start:03d}-{end:03d}.md").write_text("\n".join(content),encoding="utf-8",newline="\n")
    metadata={"corpus_schema_version":"1.0.0","version_status":"frozen","title_tamil":"புறநானூறு","title_english":"Puṟanāṉūṟu","work_slug":"purananuru","work_id":"purananuru","collection":"எட்டுத்தொகை","title_romanized_as_printed":"puRanAnURu","expected_poem_count":400,"numbered_poem_record_count":400,"available_poem_count":398,"missing_poems":[267,268],"source_name":"Project Madurai","source_url":url,"project_madurai_id":"pmuni0057","accessed_date":source_meta["accessed_date"],"source_checksum_sha256":source_meta["source_checksum_sha256"],"source_format":source_meta["source_format"],"canonical_source_decision":"Option B — exact supplied Markdown/text export approved as frozen canonical artifact","canonical_source_provenance_record":"sources/source-metadata/purananuru-freeze-provenance.json","encoding":"UTF-8","normalization":"Unicode NFC","navigation_sections":{"type":"mechanical","range_size":50,"count":8},"notes":["The preserved canonical input is the checksum-pinned user-supplied Markdown/text export, not raw HTML.","The source explicitly prints 267- 268 கிடைத்தில; both records are retained with empty canonical bodies.","Printed dot sequences are preserved and represented as textual incompleteness without reconstruction.","No source-printed anthology divisions were detected.","Version 1.0.0 freezes this exact source artifact, canonical bodies, printed metadata provenance, textual-status representation, mechanical navigation strategy, and validation expectations; it does not claim raw-HTML preservation or critical-edition authority."]}
    write_json(p["metadata"],metadata,force=True)
    if verbose:print(f"Wrote {len(poems)} poem files and 8 mechanical navigation sections")

def split(work: str, force=False, dry_run=False, verbose=False):
    if work in {"tirukkural","naladiyar","nanmanikkadigai","inna-narpathu","iniyavai-narpathu","kar-narpathu","kalavazhi-narpathu","aintinai-aimpathu","aintinai-elupathu","thinaimalai-nutraimbathu","thinaimozhi-aimpathu","tirikatukam","acharakkovai","pazhamozhi-nanuru","sirupanchamulam","muthumozhi-kanchi","elati","kainnilai"}:
        from pathinenkilkanakku_pipeline import split as split_pathinen
        return split_pathinen(work, force=True, dry_run=dry_run, verbose=verbose)
    if work == "pattuppattu":
        from pattuppattu_pipeline import split as split_pattuppattu
        return split_pattuppattu(force=True, dry_run=dry_run, verbose=verbose)
    if work == "patirruppattu":
        from patirruppattu_pipeline import split as split_patirruppattu
        return split_patirruppattu(force=True, dry_run=dry_run, verbose=verbose)
    if work == "paripatal":
        from paripatal_pipeline import split as split_paripatal
        return split_paripatal(force=True, dry_run=dry_run, verbose=verbose)
    if work == "kalittokai":
        from kalittokai_pipeline import split as split_kalittokai
        return split_kalittokai(force=True, dry_run=dry_run, verbose=verbose)
    p=paths(work); data=json.loads(p["normalized"].read_text(encoding="utf-8")); source_meta=json.loads(p["source_metadata"].read_text(encoding="utf-8"))
    if work == "aingurunuru": return _split_aingurunuru(p,data,source_meta,force,dry_run,verbose)
    if work == "kuruntokai": return _split_kuruntokai(p,data,source_meta,force,dry_run,verbose)
    if work == "akananuru": return _split_akananuru(p,data,source_meta,force,dry_run,verbose)
    if work == "purananuru": return _split_purananuru(p,data,source_meta,force,dry_run,verbose)
    poems=data["poems"]; url=source_meta["source_url"]; source_file=str(p["raw_html"].relative_to(p["raw_html"].parents[2]))
    if dry_run: print(f"Would write {len(poems)} poem files and 8 sections"); return
    p["poems"].mkdir(parents=True,exist_ok=True); p["sections"].mkdir(parents=True,exist_ok=True)
    expected_poems={f"{n:03d}.md" for n in range(1,401)}
    expected_sections={f"{n:03d}-{n+49:03d}.md" for n in range(1,401,50)}
    unexpected_poems=[x for x in p["poems"].rglob("*") if x.is_file() and (x.parent!=p["poems"] or x.name not in expected_poems)]
    unexpected_sections=[x for x in p["sections"].rglob("*") if x.is_file() and (x.parent!=p["sections"] or x.name not in expected_sections)]
    if unexpected_poems or unexpected_sections:
        names=[str(x.relative_to(p["corpus"])) for x in unexpected_poems+unexpected_sections]
        raise RuntimeError(f"Refusing regeneration with unexpected physical files: {names}")
    for poem in poems:
        target=p["poems"]/f"{poem['poem_number']:03d}.md"
        if target.exists() and not force: raise FileExistsError(f"Refusing to overwrite {target}; pass --force")
        target.write_text(poem_markdown(poem,url,source_file),encoding="utf-8",newline="\n")
    preface=data.get("prefatory_text",{})
    preface_md=f"## {preface.get('heading','கடவுள் வாழ்த்து')}\n\n"+"\n".join(preface.get("lines",[]))+f"\n\n{preface.get('poet','')}\n"
    intro="# நற்றிணை — Source transcription\n\nCanonical transcription extracted from the Project Madurai source. No literary corrections have been applied.\n\n"+preface_md
    full=[intro]
    for poem in poems: full.append(poem_markdown(poem,url,source_file).split("---\n",2)[-1].lstrip())
    p["full_text"].write_text("\n".join(full),encoding="utf-8",newline="\n")
    for start in range(1,401,50):
        selected=[x for x in poems if start<=x["poem_number"]<=start+49]
        content=[f"# நற்றிணை {start:03d}–{min(start+49,400):03d}\n"]
        content += [poem_markdown(x,url,source_file).split("---\n",2)[-1].lstrip() for x in selected]
        (p["sections"]/f"{section_name(start)}.md").write_text("\n".join(content),encoding="utf-8",newline="\n")
    metadata={"corpus_schema_version":"1.0.0","version_status":"frozen","title_tamil":"நற்றிணை","title_english":"Naṟṟiṇai","work_slug":work,"collection":"எட்டுத்தொகை",
      "compiler":"அறியப்படவில்லை","editor":["N D LogaSundaram","Ms. Selvanayagi","Dr. K. Kalyanasundaram"],"patron":"பன்னாடு தந்த மாறன் வழுதி","expected_poem_count":400,
      "available_poem_count":sum(bool(x["lines"]) for x in poems),"missing_poems":[x["poem_number"] for x in poems if not x["lines"]],
      "source_name":"Project Madurai","source_url":url,"project_madurai_id":source_meta["project_madurai_id"],
      "accessed_date":source_meta["accessed_date"],"source_checksum_sha256":source_meta["source_checksum_sha256"],
      "encoding":"UTF-8","normalization":"Unicode NFC","notes":["Source states poem 234 is lost and prints conjectural candidate material separately.","Source states the latter part of poem 385 is lost.","Tiṇai and poet values are copied only from printed poem headings."]}
    write_json(p["metadata"],metadata,force=True)
    # Curated work documentation is not generated output. Seed it only when a
    # new work directory has no README; never overwrite it during regeneration.
    work_readme=p["corpus"]/"README.md"
    if not work_readme.exists():
        readme=f"# நற்றிணை (Naṟṟiṇai)\n\nSource-preserving transcription from [{url}]({url}). See `metadata.json` for provenance and checksum.\n"
        work_readme.write_text(readme,encoding="utf-8",newline="\n")
    if verbose: print(f"Wrote {len(poems)} poem files")

if __name__ == "__main__":
    ap=argparse.ArgumentParser(); ap.add_argument("--work",required=True); ap.add_argument("--force",action="store_true"); ap.add_argument("--dry-run",action="store_true"); ap.add_argument("--verbose",action="store_true")
    a=ap.parse_args(); split(a.work,a.force,a.dry_run,a.verbose)
