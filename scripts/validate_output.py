#!/usr/bin/env python3
from __future__ import annotations
import argparse, collections, csv, hashlib, json, re, unicodedata
from corpuslib import body_hash, canonical_body_text, markdown_literary_lines, paths, read_frontmatter, section_name, write_work_issues, write_json

ORPHAN_TAMIL_MARK=re.compile(r"(?:^|\s)[\u0B82\u0BBE-\u0BCD\u0BD7]")

def issue(n,typ,severity,msg,md=""):
    return {"work":"natrinai","poem_number":n if n is not None else "","issue_type":typ,"severity":severity,"message":msg,
            "source_file":"sources/raw-html/natrinai.html","markdown_file":md}

def aissue(n,typ,severity,msg,md=""):
    return {"work":"aingurunuru","poem_number":n if n is not None else "","issue_type":typ,"severity":severity,"message":msg,
            "source_file":"sources/raw-html/aingurunuru.html","markdown_file":md}

def kissue(n,typ,severity,msg,md=""):
    return {"work":"kuruntokai","poem_number":n if n is not None else "","issue_type":typ,"severity":severity,"message":msg,
            "source_file":"sources/raw-html/kuruntokai.html","markdown_file":md}

def gissue(n,typ,severity,msg,md=""):
    return {"work":"akananuru","poem_number":n if n is not None else "","issue_type":typ,"severity":severity,"message":msg,
            "source_file":"sources/raw-html/akananuru.html","markdown_file":md}

def pissue(n,typ,severity,msg,md=""):
    return {"work":"purananuru","poem_number":n if n is not None else "","issue_type":typ,"severity":severity,"message":msg,
            "source_file":"sources/purananuru.md","markdown_file":md}

def validate_purananuru(work,force=False,dry_run=False,verbose=False):
    p=paths(work);issues=[];nums=[];fidelity=[];bodies=collections.defaultdict(list);firsts=collections.defaultdict(list);schema_fail=set()
    parsed=json.loads(p["normalized"].read_text(encoding="utf-8"));source={x["poem_number"]:x for x in parsed["poems"]}
    expected={f"{n:03d}.md" for n in range(1,401)};physical=[x for x in p["poems"].rglob("*") if x.is_file()];direct={x.name for x in physical if x.parent==p["poems"]}
    unexpected=sorted(str(x.relative_to(p["poems"])) for x in physical if x.parent!=p["poems"] or x.name not in expected);missing=sorted(expected-direct)
    if len(physical)!=400:issues.append(pissue(None,"physical_poem_file_count","error",f"Expected 400; found {len(physical)}"))
    for x in unexpected:issues.append(pissue(None,"unexpected_poem_filename","error",x))
    for x in missing:issues.append(pissue(None,"missing_poem_filename","error",x))
    yaml_numbers=collections.defaultdict(list)
    for md in physical:
        if md.suffix==".md":
            try:fm,_=read_frontmatter(md);yaml_numbers[int(fm["poem_number"])].append(str(md.relative_to(p["poems"])))
            except Exception as e:issues.append(pissue(None,"malformed_yaml","error",f"{md.name}: {e}"))
    for n,names in yaml_numbers.items():
        if len(names)>1:issues.append(pissue(n,"duplicate_yaml_poem_number","error",f"Declared by {names}"))
    es={f"{n:03d}-{n+49:03d}.md" for n in range(1,401,50)};sections=[x for x in p["sections"].rglob("*") if x.is_file()];sd={x.name for x in sections if x.parent==p["sections"]}
    if len(sections)!=8:issues.append(pissue(None,"physical_section_file_count","error",f"Expected 8; found {len(sections)}"))
    for x in sorted(str(x.relative_to(p["sections"])) for x in sections if x.parent!=p["sections"] or x.name not in es):issues.append(pissue(None,"unexpected_section_filename","error",x))
    for x in sorted(es-sd):issues.append(pissue(None,"missing_section_filename","error",x))
    required=["schema_version","work","work_id","poem_number","poem_number_as_printed","textual_status","canonical_text_available","candidate_texts_available","lacuna_present","lacuna_location","extraction_status","thinai","thinai_source","poet","poet_source","speaker","speaker_source","source_note_available","source_note_source"]
    for name in sorted(expected&direct):
        md=p["poems"]/name;rel=str(md.relative_to(p["corpus"].parents[1]));fm,body=read_frontmatter(md);n=int(fm["poem_number"]);nums.append(n)
        for key in required:
            if key not in fm:issues.append(pissue(n,"missing_metadata_key","error",f"Missing key {key}",rel));schema_fail.add(name)
        lines=markdown_literary_lines(body);sh=body_hash(source[n]["lines"]);mh=body_hash(lines);note=[]
        if "## Source note (as printed)" in body:note=[x.strip() for x in body.split("## Source note (as printed)",1)[1].splitlines() if x.strip()]
        nm=canonical_body_text(note)==canonical_body_text(source[n]["source_note_lines"])
        fidelity.append({"poem_number":n,"source_body_hash_sha256":sh,"markdown_body_hash_sha256":mh,"source_output_match":sh==mh,"source_note_match":nm})
        if sh!=mh:issues.append(pissue(n,"source_output_mismatch","error","Generated body differs from normalized source",rel))
        if not nm:issues.append(pissue(n,"source_note_output_mismatch","error","Generated source note differs",rel))
        if n in (267,268):
            if lines or fm.get("textual_status")!="lost" or fm.get("canonical_text_available") or fm.get("extraction_status")!="success":issues.append(pissue(n,"invalid_source_lost_status","error","Printed unavailable record must be lost with successful extraction",rel))
            issues.append(pissue(n,"source_text_lost","warning","Project Madurai prints the combined statement 267- 268 கிடைத்தில",rel))
        elif not lines:issues.append(pissue(n,"empty_poem","error","No literary text and source does not mark poem unavailable",rel))
        if source[n].get("lacuna_present"):
            if fm.get("textual_status")!="incomplete" or not fm.get("lacuna_present"):issues.append(pissue(n,"invalid_lacuna_status","error","Printed dot lacuna must remain incomplete",rel))
            issues.append(pissue(n,"textual_lacuna","info","Printed dot-sequence lacuna is preserved unchanged",rel))
        key=canonical_body_text(lines)
        if key:bodies[hashlib.sha256(key.encode()).hexdigest()].append(n);firsts[lines[0]].append(n)
    counts=collections.Counter(nums)
    for n in range(1,401):
        if n not in counts:issues.append(pissue(n,"missing_poem_number","error","No canonical record"))
    for n,c in counts.items():
        if c>1:issues.append(pissue(n,"duplicate_poem_number","error",f"Occurs {c} times"))
    for digest,ns in bodies.items():
        if len(ns)>1:issues.append(pissue(None,"duplicate_poem_body","warning",f"Identical normalized bodies {ns}; {digest}"))
    for line,ns in firsts.items():
        if len(ns)>1:issues.append(pissue(None,"shared_first_line","info",f"Shared opening {ns}; full bodies differ: {line}"))
    report={"work":work,"nominal_poem_numbers":400,"source_record_count":len(parsed["poems"]),"canonical_poem_files":len(physical),"canonical_literary_texts_available":sum(bool(x["lines"]) for x in parsed["poems"]),"source_lost_poems":[267,268],"missing_numbers":[n for n in range(1,401) if n not in counts],"duplicate_numbers":[n for n,c in counts.items() if c>1],"schema_files_checked":len(expected&direct),"schema_files_passing":len(expected&direct)-len(schema_fail),"schema_files_failing":len(schema_fail),"source_output_matches":sum(x["source_output_match"] for x in fidelity),"source_note_matches":sum(x["source_note_match"] for x in fidelity),"duplicate_full_bodies":[x for x in bodies.values() if len(x)>1],"shared_first_lines":[x for x in firsts.values() if len(x)>1],"lacunose_poems":parsed["lacunose_poems"],"navigation_sections":8,"source_output_fidelity":fidelity,"errors":sum(x["severity"]=="error" for x in issues),"warnings":sum(x["severity"]=="warning" for x in issues),"info":sum(x["severity"]=="info" for x in issues),"issues":issues}
    report["status"]="pass-with-review" if not report["errors"] else "fail"
    if dry_run:print(json.dumps(report,ensure_ascii=False,indent=2));return report
    write_json(p["validation"],report,force=True);write_json(p["validation"].with_name("purananuru-validation-report.json"),report,force=True);write_work_issues(work,issues)
    rows=list(csv.DictReader(p["poems_manifest"].open(encoding="utf-8")));bynum=collections.Counter(str(x["poem_number"]) for x in issues if x["poem_number"]!="")
    for row in rows:
        if row.get("work_slug")==work:row["issue_count"]=bynum[row["poem_number"]];row["validation_status"]="review" if int(row["issue_count"]) else "pass"
    with p["poems_manifest"].open("w",encoding="utf-8",newline="") as f:w=csv.DictWriter(f,fieldnames=rows[0].keys());w.writeheader();w.writerows(rows)
    if verbose:print(f"Validation: {report['status']}; {report['errors']} errors, {report['warnings']} warnings, {report['info']} info")
    return report

def validate_akananuru(work,force=False,dry_run=False,verbose=False):
    p=paths(work);issues=[];nums=[];fidelity=[];bodies=collections.defaultdict(list);firsts=collections.defaultdict(list);schema_failures=set()
    parsed=json.loads(p["normalized"].read_text(encoding="utf-8"));source={x["poem_number"]:x for x in parsed["poems"]}
    expected={f"{n:03d}.md" for n in range(1,401)};physical=[x for x in p["poems"].rglob("*") if x.is_file()];direct={x.name for x in physical if x.parent==p["poems"]}
    unexpected=sorted(str(x.relative_to(p["poems"])) for x in physical if x.parent!=p["poems"] or x.name not in expected);missing=sorted(expected-direct)
    if len(physical)!=400:issues.append(gissue(None,"physical_poem_file_count","error",f"Expected 400; found {len(physical)}"))
    for x in unexpected:issues.append(gissue(None,"unexpected_poem_filename","error",x))
    for x in missing:issues.append(gissue(None,"missing_poem_filename","error",x))
    yaml_numbers=collections.defaultdict(list)
    for md in physical:
        if md.suffix==".md":
            try:fm,_=read_frontmatter(md);yaml_numbers[int(fm["poem_number"])].append(str(md.relative_to(p["poems"])))
            except Exception as e:issues.append(gissue(None,"malformed_yaml","error",f"{md.name}: {e}"))
    for n,names in yaml_numbers.items():
        if len(names)>1:issues.append(gissue(n,"duplicate_yaml_poem_number","error",f"Declared by {names}"))
    es={"001-120.md","121-300.md","301-400.md"};sections=[x for x in p["sections"].rglob("*") if x.is_file()];sd={x.name for x in sections if x.parent==p["sections"]}
    if len(sections)!=3:issues.append(gissue(None,"physical_section_file_count","error",f"Expected 3 source-division files; found {len(sections)}"))
    for x in sorted(str(x.relative_to(p["sections"])) for x in sections if x.parent!=p["sections"] or x.name not in es):issues.append(gissue(None,"unexpected_section_filename","error",x))
    for x in sorted(es-sd):issues.append(gissue(None,"missing_section_filename","error",x))
    section_membership=collections.defaultdict(list)
    for section in sections:
        if section.parent==p["sections"] and section.name in es:
            for number in re.findall(r"^# அகநானுறு (\d{1,3})$",section.read_text(encoding="utf-8"),re.MULTILINE):
                section_membership[int(number)].append(section.name)
    for n in range(1,401):
        if len(section_membership[n])!=1:issues.append(gissue(n,"section_membership_anomaly","error",f"Expected one source-division section membership; found {section_membership[n]}"))
    required=["schema_version","work","work_id","poem_number","poem_number_as_printed","source_order","textual_status","canonical_text_available","candidate_texts_available","lacuna_present","lacuna_location","extraction_status","thinai","thinai_source","poet","poet_source","speaker","speaker_source","source_note_available","source_note_source","source_object_id"]
    for name in sorted(expected&direct):
        md=p["poems"]/name;rel=str(md.relative_to(p["corpus"].parents[1]));fm,body=read_frontmatter(md);n=int(fm["poem_number"]);nums.append(n)
        for key in required:
            if key not in fm:issues.append(gissue(n,"missing_metadata_key","error",f"Missing key {key}",rel));schema_failures.add(name)
        lines=markdown_literary_lines(body);sh=body_hash(source[n]["lines"]);mh=body_hash(lines);note=[]
        if "## Source note (as printed)" in body:note=[x.strip() for x in body.split("## Source note (as printed)",1)[1].splitlines() if x.strip()]
        nm=canonical_body_text(note)==canonical_body_text(source[n]["source_note_lines"])
        fidelity.append({"poem_number":n,"source_body_hash_sha256":sh,"markdown_body_hash_sha256":mh,"source_output_match":sh==mh,"source_note_match":nm})
        if sh!=mh:issues.append(gissue(n,"source_output_mismatch","error","Generated body differs from normalized source",rel))
        if not nm:issues.append(gissue(n,"source_note_output_mismatch","error","Generated source note differs",rel))
        if not lines:issues.append(gissue(n,"empty_poem","error","No literary text",rel))
        if fm.get("textual_status")!="complete" or not fm.get("canonical_text_available") or fm.get("extraction_status")!="success":issues.append(gissue(n,"invalid_textual_status","error","Printed complete record must have complete/success status",rel))
        if fm.get("poem_number_as_printed")!=source[n]["poem_number_as_printed"]:issues.append(gissue(n,"printed_number_provenance_mismatch","error","Printed record label differs from extracted source",rel))
        key=canonical_body_text(lines)
        if key:bodies[hashlib.sha256(key.encode()).hexdigest()].append(n);firsts[lines[0]].append(n)
    counts=collections.Counter(nums)
    for n in range(1,401):
        if n not in counts:issues.append(gissue(n,"missing_poem_number","error","No canonical record"))
    for n,c in counts.items():
        if c>1:issues.append(gissue(n,"duplicate_poem_number","error",f"Occurs {c} times"))
    for digest,ns in bodies.items():
        if len(ns)>1:issues.append(gissue(None,"duplicate_poem_body","warning",f"Identical normalized bodies {ns}; {digest}"))
    for line,ns in firsts.items():
        if len(ns)>1:issues.append(gissue(None,"shared_first_line","info",f"Shared opening {ns}; full bodies differ: {line}"))
    for anomaly in parsed["numbering_anomalies"]:
        issues.append(gissue(anomaly["canonical_poem_number"],"printed_numbering_anomaly","warning",f"Source-order record {anomaly['canonical_poem_number']} prints label {anomaly['poem_number_as_printed']}; preserved in poem_number_as_printed"))
    divisions=parsed["printed_divisions"]
    for d in divisions:
        members=[n for n in nums if d["poem_start"]<=n<=d["poem_end"]]
        if len(members)!=d["poem_end"]-d["poem_start"]+1:issues.append(gissue(None,"division_membership_anomaly","error",f"{d['heading_as_printed']} contains {len(members)} canonical records"))
    report={"work":work,"nominal_poem_numbers":400,"source_record_count":len(parsed["poems"]),"canonical_poem_files":len(physical),"canonical_literary_texts_available":sum(bool(x["lines"]) for x in parsed["poems"]),"source_lost_poems":[],"missing_numbers":[n for n in range(1,401) if n not in counts],"duplicate_numbers":[n for n,c in counts.items() if c>1],"printed_number_missing":parsed["printed_number_missing"],"printed_number_duplicates":parsed["printed_number_duplicates"],"numbering_anomalies":parsed["numbering_anomalies"],"schema_files_checked":len(expected&direct),"schema_files_passing":len(expected&direct)-len(schema_failures),"schema_files_failing":len(schema_failures),"source_output_matches":sum(x["source_output_match"] for x in fidelity),"source_note_matches":sum(x["source_note_match"] for x in fidelity),"duplicate_full_bodies":[x for x in bodies.values() if len(x)>1],"shared_first_lines":[x for x in firsts.values() if len(x)>1],"printed_divisions":len(divisions),"section_membership_anomalies":sum(len(section_membership[n])!=1 for n in range(1,401)),"source_output_fidelity":fidelity,"errors":sum(x["severity"]=="error" for x in issues),"warnings":sum(x["severity"]=="warning" for x in issues),"info":sum(x["severity"]=="info" for x in issues),"issues":issues}
    report["status"]="pass-with-review" if not report["errors"] else "fail"
    if dry_run:print(json.dumps(report,ensure_ascii=False,indent=2));return report
    write_json(p["validation"],report,force=True);write_json(p["validation"].with_name("akananuru-validation-report.json"),report,force=True);write_work_issues(work,issues)
    rows=list(csv.DictReader(p["poems_manifest"].open(encoding="utf-8")));bynum=collections.Counter(str(x["poem_number"]) for x in issues if x["poem_number"]!="")
    for row in rows:
        if row.get("work_slug")==work:row["issue_count"]=bynum[row["poem_number"]];row["validation_status"]="review" if int(row["issue_count"]) else "pass"
    with p["poems_manifest"].open("w",encoding="utf-8",newline="") as f:w=csv.DictWriter(f,fieldnames=rows[0].keys());w.writeheader();w.writerows(rows)
    if verbose:print(f"Validation: {report['status']}; {report['errors']} errors, {report['warnings']} warnings, {report['info']} info")
    return report

def validate_kuruntokai(work,force=False,dry_run=False,verbose=False):
    p=paths(work);issues=[];nums=[];fidelity=[];bodies=collections.defaultdict(list);firsts=collections.defaultdict(list)
    parsed=json.loads(p["normalized"].read_text(encoding="utf-8"));source={x["poem_number"]:x for x in parsed["poems"]}
    expected={f"{n:03d}.md" for n in range(1,402)};physical=[x for x in p["poems"].rglob("*") if x.is_file()];direct={x.name for x in physical if x.parent==p["poems"]}
    unexpected=sorted(str(x.relative_to(p["poems"])) for x in physical if x.parent!=p["poems"] or x.name not in expected);missing=sorted(expected-direct)
    if len(physical)!=401:issues.append(kissue(None,"physical_poem_file_count","error",f"Expected 401; found {len(physical)}"))
    for x in unexpected:issues.append(kissue(None,"unexpected_poem_filename","error",x))
    for x in missing:issues.append(kissue(None,"missing_poem_filename","error",x))
    yaml_numbers=collections.defaultdict(list)
    for md in physical:
        if md.suffix==".md":
            try:fm,_=read_frontmatter(md);yaml_numbers[int(fm["poem_number"])].append(str(md.relative_to(p["poems"])))
            except Exception as e:issues.append(kissue(None,"malformed_yaml","error",f"{md.name}: {e}"))
    for n,names in yaml_numbers.items():
        if len(names)>1:issues.append(kissue(n,"duplicate_yaml_poem_number","error",f"Declared by {names}"))
    es={f"{n:03d}-{min(n+49,401):03d}.md" for n in range(1,402,50)};sections=[x for x in p["sections"].rglob("*") if x.is_file()];sd={x.name for x in sections if x.parent==p["sections"]}
    if len(sections)!=9:issues.append(kissue(None,"physical_section_file_count","error",f"Expected 9; found {len(sections)}"))
    for x in sorted(str(x.relative_to(p["sections"])) for x in sections if x.parent!=p["sections"] or x.name not in es):issues.append(kissue(None,"unexpected_section_filename","error",x))
    for x in sorted(es-sd):issues.append(kissue(None,"missing_section_filename","error",x))
    required=["schema_version","work","work_id","poem_number","textual_status","canonical_text_available","candidate_texts_available","lacuna_present","lacuna_location","extraction_status","thinai","thinai_source","poet","poet_source","speaker","speaker_source","source_note_available","source_note_source"]
    for name in sorted(expected&direct):
        md=p["poems"]/name;rel=str(md.relative_to(p["corpus"].parents[1]));fm,body=read_frontmatter(md);n=int(fm["poem_number"]);nums.append(n)
        for key in required:
            if key not in fm:issues.append(kissue(n,"missing_metadata_key","error",f"Missing key {key}",rel))
        lines=markdown_literary_lines(body);sh=body_hash(source[n]["lines"]);mh=body_hash(lines);note=[]
        if "## Source note (as printed)" in body:note=[x.strip() for x in body.split("## Source note (as printed)",1)[1].splitlines() if x.strip()]
        nm=canonical_body_text(note)==canonical_body_text(source[n]["source_note_lines"]);fidelity.append({"poem_number":n,"source_body_hash_sha256":sh,"markdown_body_hash_sha256":mh,"source_output_match":sh==mh,"source_note_match":nm})
        if sh!=mh:issues.append(kissue(n,"source_output_mismatch","error","Generated body differs from normalized source",rel))
        if not nm:issues.append(kissue(n,"source_note_output_mismatch","error","Generated source note differs",rel))
        if not lines:issues.append(kissue(n,"empty_poem","error","No literary text",rel))
        key=canonical_body_text(lines)
        if key:bodies[hashlib.sha256(key.encode()).hexdigest()].append(n);firsts[lines[0]].append(n)
    counts=collections.Counter(nums)
    for n in range(1,402):
        if n not in counts:issues.append(kissue(n,"missing_poem_number","error","No canonical record"))
    for n,c in counts.items():
        if c>1:issues.append(kissue(n,"duplicate_poem_number","error",f"Occurs {c} times"))
    for d,ns in bodies.items():
        if len(ns)>1:issues.append(kissue(None,"duplicate_poem_body","warning",f"Identical bodies {ns}; {d}"))
    for line,ns in firsts.items():
        if len(ns)>1:issues.append(kissue(None,"shared_first_line","info",f"Shared opening {ns}; full bodies differ: {line}"))
    issues += [kissue(29,"printed_heading_anomaly","info","Speaker/context is printed as தலைன் கூற்று; preserved unchanged"),kissue(396,"printed_heading_anomaly","info","Tiṇai is printed as பாால; preserved unchanged")]
    unknown=[x["poem_number"] for x in parsed["poems"] if x["poet"] is None]
    report={"work":work,"nominal_poem_numbers":401,"source_record_count":len(parsed["poems"]),"canonical_poem_files":len(physical),"canonical_literary_texts_available":sum(bool(x["lines"]) for x in parsed["poems"]),"source_lost_poems":[],"missing_numbers":[n for n in range(1,402) if n not in counts],"duplicate_numbers":[n for n,c in counts.items() if c>1],"source_output_matches":sum(x["source_output_match"] for x in fidelity),"source_note_matches":sum(x["source_note_match"] for x in fidelity),"duplicate_full_bodies":[x for x in bodies.values() if len(x)>1],"shared_first_lines":[x for x in firsts.values() if len(x)>1],"unknown_poet_placeholders":unknown,"navigation_sections":9,"source_output_fidelity":fidelity,"errors":sum(x["severity"]=="error" for x in issues),"warnings":sum(x["severity"]=="warning" for x in issues),"info":sum(x["severity"]=="info" for x in issues),"issues":issues}
    report["status"]="pass-with-review" if not report["errors"] else "fail"
    if dry_run:print(json.dumps(report,ensure_ascii=False,indent=2));return report
    write_json(p["validation"],report,force=True);write_json(p["validation"].with_name("kuruntokai-validation-report.json"),report,force=True);write_work_issues(work,issues)
    rows=list(csv.DictReader(p["poems_manifest"].open(encoding="utf-8")));bynum=collections.Counter(str(x["poem_number"]) for x in issues if x["poem_number"]!="")
    for row in rows:
        if row.get("work_slug")==work:row["issue_count"]=bynum[row["poem_number"]];row["validation_status"]="review" if int(row["issue_count"]) else "pass"
    with p["poems_manifest"].open("w",encoding="utf-8",newline="") as f:w=csv.DictWriter(f,fieldnames=rows[0].keys());w.writeheader();w.writerows(rows)
    if verbose:print(f"Validation: {report['status']}; {report['errors']} errors, {report['warnings']} warnings, {report['info']} info")
    return report

def validate_aingurunuru(work, force=False, dry_run=False, verbose=False):
    p=paths(work); issues=[]; nums=[]; fidelity=[]; bodies=collections.defaultdict(list); firsts=collections.defaultdict(list)
    parsed=json.loads(p["normalized"].read_text(encoding="utf-8")); source={x["poem_number"]:x for x in parsed["poems"]}
    expected={f"{n:03d}.md" for n in range(1,501)}; physical=[x for x in p["poems"].rglob("*") if x.is_file()]
    direct={x.name for x in physical if x.parent==p["poems"]}; unexpected=sorted(str(x.relative_to(p["poems"])) for x in physical if x.parent!=p["poems"] or x.name not in expected)
    missing=sorted(expected-direct)
    if len(physical)!=500: issues.append(aissue(None,"physical_poem_file_count","error",f"Expected exactly 500 physical files; found {len(physical)}"))
    for x in unexpected: issues.append(aissue(None,"unexpected_poem_filename","error",x))
    for x in missing: issues.append(aissue(None,"missing_poem_filename","error",x))
    yaml_numbers=collections.defaultdict(list)
    for md in physical:
        if md.suffix==".md":
            try:
                fm,_=read_frontmatter(md); yaml_numbers[int(fm["poem_number"])].append(str(md.relative_to(p["poems"])))
            except Exception as e: issues.append(aissue(None,"malformed_yaml","error",f"{md.name}: {e}"))
    for n,names in yaml_numbers.items():
        if len(names)>1: issues.append(aissue(n,"duplicate_yaml_poem_number","error",f"Declared by {names}"))
    expected_sections={f"{n:03d}-{n+9:03d}.md" for n in range(1,501,10)}; sections=[x for x in p["sections"].rglob("*") if x.is_file()]
    section_names={x.name for x in sections if x.parent==p["sections"]}
    if len(sections)!=50: issues.append(aissue(None,"physical_section_file_count","error",f"Expected 50 pattu-group files; found {len(sections)}"))
    for x in sorted(str(x.relative_to(p["sections"])) for x in sections if x.parent!=p["sections"] or x.name not in expected_sections): issues.append(aissue(None,"unexpected_section_filename","error",x))
    for x in sorted(expected_sections-section_names): issues.append(aissue(None,"missing_section_filename","error",x))
    required=["schema_version","work","work_id","poem_number","textual_status","canonical_text_available","candidate_texts_available","lacuna_present","lacuna_location","extraction_status","thinai","thinai_source","poet","poet_source","speaker","speaker_source","source_note_available","source_note_source"]
    for name in sorted(expected & direct):
        md=p["poems"]/name; rel=str(md.relative_to(p["corpus"].parents[1])); fm,body=read_frontmatter(md); n=int(fm["poem_number"]); nums.append(n)
        for key in required:
            if key not in fm: issues.append(aissue(n,"missing_metadata_key","error",f"Missing key {key}",rel))
        poem_lines=markdown_literary_lines(body); sh=body_hash(source[n]["lines"]); mh=body_hash(poem_lines)
        note_lines=[]
        if "## Source note (as printed)" in body: note_lines=[x.strip() for x in body.split("## Source note (as printed)",1)[1].splitlines() if x.strip()]
        note_match=canonical_body_text(note_lines)==canonical_body_text(source[n]["source_note_lines"])
        fidelity.append({"poem_number":n,"source_body_hash_sha256":sh,"markdown_body_hash_sha256":mh,"source_output_match":sh==mh,"source_note_match":note_match})
        if sh!=mh: issues.append(aissue(n,"source_output_mismatch","error","Generated body differs from normalized extracted source",rel))
        if not note_match: issues.append(aissue(n,"source_note_output_mismatch","error","Generated source note differs from extracted note",rel))
        if n in (129,130):
            if poem_lines or fm.get("textual_status")!="lost" or fm.get("canonical_text_available") or fm.get("extraction_status")!="success": issues.append(aissue(n,"invalid_source_lost_status","error","Explicitly unavailable poem must be a successfully extracted lost record",rel))
            issues.append(aissue(n,"source_text_lost","warning","Project Madurai explicitly prints கிடைக்காத பாடல்",rel))
        elif not poem_lines: issues.append(aissue(n,"empty_poem","error","No literary lines and source does not mark poem unavailable",rel))
        if "\ufffd" in md.read_text(encoding="utf-8"): issues.append(aissue(n,"unicode_replacement_character","error","U+FFFD found",rel))
        key=canonical_body_text(poem_lines)
        if key: bodies[hashlib.sha256(key.encode()).hexdigest()].append(n); firsts[poem_lines[0]].append(n)
    counts=collections.Counter(nums)
    for n in range(1,501):
        if n not in counts: issues.append(aissue(n,"missing_poem_number","error","No canonical record"))
    for n,c in counts.items():
        if c>1: issues.append(aissue(n,"duplicate_poem_number","error",f"Number occurs {c} times"))
    for digest,ns in bodies.items():
        if len(ns)>1: issues.append(aissue(None,"duplicate_poem_body","warning",f"Identical normalized full bodies in poems {ns}; SHA-256 {digest}"))
    for line,ns in firsts.items():
        if len(ns)>1: issues.append(aissue(None,"shared_first_line","info",f"Shared opening in poems {ns}; full bodies differ: {line}"))
    groups=parsed["pattu_groups"]
    for g in groups:
        if g["poem_record_count"]!=10: issues.append(aissue(None,"pattu_membership_anomaly","error",f"Group {g['source_order']} contains {g['poem_record_count']} records"))
        if not g["ordinal_consistent"]: issues.append(aissue(None,"pattu_ordinal_inconsistency","info",f"Source-order group {g['source_order']} prints ordinal {g['printed_ordinal']}: {g['printed_heading']}"))
        if not g["printed_heading"]: issues.append(aissue(None,"pattu_heading_absent","info",f"No printed pattu heading before poem {g['poem_start']}"))
    report={"work":work,"nominal_poem_numbers":500,"source_record_count":len(parsed["poems"]),"canonical_poem_files":len(physical),
      "canonical_literary_texts_available":sum(bool(x["lines"]) for x in parsed["poems"]),"source_lost_poems":[x["poem_number"] for x in parsed["poems"] if not x["lines"]],
      "missing_numbers":[n for n in range(1,501) if n not in counts],"duplicate_numbers":[n for n,c in counts.items() if c>1],
      "sequence_breaks":[{"after":a,"before":b} for a,b in zip(sorted(set(nums)),sorted(set(nums))[1:]) if b!=a+1],
      "source_output_matches":sum(x["source_output_match"] for x in fidelity),"source_note_matches":sum(x["source_note_match"] for x in fidelity),
      "duplicate_full_bodies":[ns for ns in bodies.values() if len(ns)>1],"shared_first_lines":[ns for ns in firsts.values() if len(ns)>1],
      "pattu_groups":len(groups),"printed_pattu_headings":sum(bool(g["printed_heading"]) for g in groups),
      "pattu_membership_anomalies":sum(g["poem_record_count"]!=10 for g in groups),"source_output_fidelity":fidelity,
      "errors":sum(x["severity"]=="error" for x in issues),"warnings":sum(x["severity"]=="warning" for x in issues),"info":sum(x["severity"]=="info" for x in issues),"issues":issues}
    report["status"]="pass-with-review" if not report["errors"] else "fail"
    if dry_run: print(json.dumps(report,ensure_ascii=False,indent=2)); return report
    write_json(p["validation"],report,force=True); write_json(p["validation"].with_name("aingurunuru-validation-report.json"),report,force=True); write_work_issues(work,issues)
    rows=list(csv.DictReader(p["poems_manifest"].open(encoding="utf-8"))); bynum=collections.Counter(str(x["poem_number"]) for x in issues if x["poem_number"]!="")
    for row in rows:
        if row.get("work_slug")==work: row["issue_count"]=bynum[row["poem_number"]]; row["validation_status"]="review" if int(row["issue_count"]) else "pass"
    with p["poems_manifest"].open("w",encoding="utf-8",newline="") as f:
        w=csv.DictWriter(f,fieldnames=rows[0].keys()); w.writeheader(); w.writerows(rows)
    if verbose: print(f"Validation: {report['status']}; {report['errors']} errors, {report['warnings']} warnings, {report['info']} info")
    return report

def validate(work: str, force=False, dry_run=False, verbose=False):
    if work == "tolkappiyam":
        from tolkappiyam_pipeline import validate as validate_tolkappiyam
        report = validate_tolkappiyam(write=not dry_run)
        if verbose:
            print(f"Validation: {report['status']}; {report['errors']} errors")
        return report
    if work in {"tirukkural","naladiyar","nanmanikkadigai","inna-narpathu","iniyavai-narpathu","kar-narpathu","kalavazhi-narpathu","aintinai-aimpathu","aintinai-elupathu","thinaimalai-nutraimbathu","thinaimozhi-aimpathu","tirikatukam","acharakkovai","pazhamozhi-nanuru","sirupanchamulam","muthumozhi-kanchi","elati","kainnilai"}:
        from pathinenkilkanakku_pipeline import validate as validate_pathinen
        return validate_pathinen(work, dry_run=dry_run, verbose=verbose)
    if work == "pattuppattu":
        from pattuppattu_pipeline import validate as validate_pattuppattu
        return validate_pattuppattu(dry_run=dry_run, verbose=verbose)
    if work == "patirruppattu":
        from patirruppattu_pipeline import validate as validate_patirruppattu
        return validate_patirruppattu(dry_run=dry_run, verbose=verbose)
    if work == "paripatal":
        from paripatal_pipeline import validate as validate_paripatal
        return validate_paripatal(dry_run=dry_run, verbose=verbose)
    if work == "kalittokai":
        from kalittokai_pipeline import validate as validate_kalittokai
        return validate_kalittokai(dry_run=dry_run, verbose=verbose)
    if work == "purananuru": return validate_purananuru(work,force,dry_run,verbose)
    if work == "akananuru": return validate_akananuru(work,force,dry_run,verbose)
    if work == "aingurunuru": return validate_aingurunuru(work,force,dry_run,verbose)
    if work == "kuruntokai": return validate_kuruntokai(work,force,dry_run,verbose)
    p=paths(work); issues=[]; records=[]; bodies={}; firsts=collections.defaultdict(list); nums=[]
    parsed=json.loads(p["normalized"].read_text(encoding="utf-8")); source_by_number={x["poem_number"]:x for x in parsed["poems"]}
    fidelity=[]
    expected_names={f"{n:03d}.md" for n in range(1,401)}
    actual_files=[x for x in p["poems"].rglob("*") if x.is_file()]
    direct_names={x.name for x in actual_files if x.parent==p["poems"]}
    unexpected_names=sorted(str(x.relative_to(p["poems"])) for x in actual_files
                            if x.parent!=p["poems"] or x.name not in expected_names)
    missing_names=sorted(expected_names-direct_names)
    files=sorted(p["poems"]/name for name in expected_names if (p["poems"]/name).is_file())
    if len(actual_files)!=400:
        issues.append(issue(None,"physical_poem_file_count","error",f"Expected exactly 400 physical files; found {len(actual_files)}"))
    for name in unexpected_names: issues.append(issue(None,"unexpected_poem_filename","error",name))
    for name in missing_names: issues.append(issue(None,"missing_poem_filename","error",name))
    all_yaml_numbers=collections.defaultdict(list)
    for candidate in actual_files:
        if candidate.suffix!=".md": continue
        try:
            candidate_fm,_=read_frontmatter(candidate)
            if candidate_fm.get("poem_number") is not None:
                all_yaml_numbers[int(candidate_fm["poem_number"])].append(str(candidate.relative_to(p["poems"])))
        except Exception:
            pass
    for number,names in sorted(all_yaml_numbers.items()):
        if len(names)>1:
            issues.append(issue(number,"duplicate_yaml_poem_number","error",f"Declared by {names}"))
    expected_sections={f"{n:03d}-{n+49:03d}.md" for n in range(1,401,50)}
    section_files=[x for x in p["sections"].rglob("*") if x.is_file()]
    direct_section_names={x.name for x in section_files if x.parent==p["sections"]}
    unexpected_sections=sorted(str(x.relative_to(p["sections"])) for x in section_files
                               if x.parent!=p["sections"] or x.name not in expected_sections)
    missing_sections=sorted(expected_sections-direct_section_names)
    if len(section_files)!=8:
        issues.append(issue(None,"physical_section_file_count","error",f"Expected exactly 8 physical files; found {len(section_files)}"))
    for name in unexpected_sections: issues.append(issue(None,"unexpected_section_filename","error",name))
    for name in missing_sections: issues.append(issue(None,"missing_section_filename","error",name))
    for md in files:
        rel=str(md.relative_to(p["corpus"].parents[1]))
        try: fm,body=read_frontmatter(md)
        except Exception as e: issues.append(issue(None,"malformed_yaml","error",str(e),rel)); continue
        required=["work","work_slug","poem_number","source_url","source_file","language","script","status",
                  "textual_status","canonical_text_available","candidate_texts_available","lacuna_present","extraction_status"]
        for k in required:
            if fm.get(k) in (None,""): issues.append(issue(fm.get("poem_number"),"missing_metadata","error",f"Missing {k}",rel))
        n=fm["poem_number"]; nums.append(n); poem_lines=markdown_literary_lines(body); source=source_by_number[n]
        source_hash=body_hash(source["lines"]); markdown_hash=body_hash(poem_lines); match=source_hash==markdown_hash
        note_lines=[]
        if "## Source note (as printed)" in body:
            note_lines=[x.strip() for x in body.split("## Source note (as printed)",1)[1].splitlines() if x.strip()]
        note_match=canonical_body_text(note_lines)==canonical_body_text(source["source_note_lines"])
        fidelity.append({"poem_number":n,"source_body_hash_sha256":source_hash,"markdown_body_hash_sha256":markdown_hash,
                         "source_output_match":match,"source_note_match":note_match})
        if not match: issues.append(issue(n,"source_output_mismatch","error","Generated literary body differs from normalized extracted source block",rel))
        if not note_match: issues.append(issue(n,"source_note_output_mismatch","error","Generated source note differs from normalized extracted source note",rel))
        if not poem_lines:
            if n==234:
                issues.append(issue(n,"source_text_lost","warning","Canonical anthology text is lost; Project Madurai supplies two conjectural candidate texts in its printed note",rel))
            else: issues.append(issue(n,"empty_poem","error","No literary lines",rel))
        if n==234 and (fm["textual_status"]!="lost" or fm["canonical_text_available"] or not fm["candidate_texts_available"] or fm["extraction_status"]!="success"):
            issues.append(issue(n,"invalid_textual_status","error","Poem 234 must be lost with candidates and successful extraction",rel))
        if n==385:
            if fm["textual_status"]!="incomplete" or not fm["canonical_text_available"] or not fm["lacuna_present"] or fm["lacuna_location"]!="ending":
                issues.append(issue(n,"invalid_textual_status","error","Poem 385 must be incomplete with an ending lacuna",rel))
            issues.append(issue(n,"textual_lacuna","info","Project Madurai marks the ending as incomplete and preserves printed dash placeholders",rel))
        if len(poem_lines)<5 and n!=234: issues.append(issue(n,"unexpectedly_short","warning",f"Only {len(poem_lines)} lines",rel))
        if len(poem_lines)>50: issues.append(issue(n,"unexpectedly_long","warning",f"{len(poem_lines)} lines",rel))
        if "\ufffd" in md.read_text(encoding="utf-8"): issues.append(issue(n,"unicode_replacement_character","error","U+FFFD found",rel))
        for line in poem_lines:
            if unicodedata.normalize("NFC",line)!=line: issues.append(issue(n,"not_nfc","error","Line is not NFC",rel)); break
            if ORPHAN_TAMIL_MARK.search(line): issues.append(issue(n,"possible_broken_tamil_combining_sequence","warning",f"Possible orphan mark in: {line}",rel)); break
        expected_section=section_name(n)
        if fm.get("section")!=expected_section: issues.append(issue(n,"section_range_inconsistency","error",f"Expected {expected_section}",rel))
        bodykey=canonical_body_text(poem_lines)
        if bodykey: bodies.setdefault(hashlib.sha256(bodykey.encode()).hexdigest(),[]).append(n)
        if poem_lines: firsts[poem_lines[0]].append(n)
        records.append((n,rel))
    counts=collections.Counter(nums)
    for n,c in counts.items():
        if c>1: issues.append(issue(n,"duplicate_poem_number","error",f"Number occurs {c} times"))
    for n in range(1,401):
        if n not in counts: issues.append(issue(n,"missing_poem_number","error","No Markdown file"))
    for digest,ns in bodies.items():
        if len(ns)>1: issues.append(issue(None,"duplicate_poem_body","warning",f"Identical normalized full bodies in poems {ns}; SHA-256 {digest}"))
    for first,ns in firsts.items():
        if len(ns)>1: issues.append(issue(None,"shared_first_line","info",f"Legitimate shared opening in poems {ns}; subsequent text differs: {first}"))
    if len(parsed["poems"])!=len(files): issues.append(issue(None,"source_output_count_mismatch","error",f"Parsed {len(parsed['poems'])}; files {len(files)}"))
    for fragment in parsed.get("unparsed_fragments",[]): issues.append(issue(None,"unparsed_source_fragment","warning",fragment[:300]))
    report={"work":work,"source_record_count":len(parsed["poems"]),"output_file_count":len(files),"expected_poem_count":400,
      "available_text_count":sum(1 for n,_ in records if n!=234),"issue_count":len(issues),
      "errors":sum(x["severity"]=="error" for x in issues),"warnings":sum(x["severity"]=="warning" for x in issues),
      "info":sum(x["severity"]=="info" for x in issues),
      "missing_numbers":[n for n in range(1,401) if n not in counts],"duplicate_numbers":[n for n,c in counts.items() if c>1],
      "sequence_breaks":[{"after":a,"before":b} for a,b in zip(sorted(set(nums)),sorted(set(nums))[1:]) if b!=a+1],
      "duplicate_markdown_filenames":unexpected_names,
      "unexpected_poem_filenames":unexpected_names,"missing_poem_filenames":missing_names,
      "physical_poem_file_count":len(actual_files),"duplicate_yaml_poem_numbers":{str(n):v for n,v in all_yaml_numbers.items() if len(v)>1},
      "physical_section_file_count":len(section_files),"unexpected_section_filenames":unexpected_sections,"missing_section_filenames":missing_sections,
      "known_source_missing_text":[234],"source_output_fidelity":fidelity,
      "status":"pass-with-review" if not any(x["severity"]=="error" for x in issues) else "fail","issues":issues}
    if dry_run: print(json.dumps(report,ensure_ascii=False,indent=2)); return report
    write_json(p["validation"],report,force=True); write_json(p["validation"].with_name("natrinai-validation-report.json"),report,force=True); write_work_issues(work,issues)
    # Update manifest validation columns.
    rows=list(csv.DictReader(p["poems_manifest"].open(encoding="utf-8"))); bynum=collections.Counter(str(x["poem_number"]) for x in issues)
    for row in rows:
        if row.get("work_slug")==work:
            row["issue_count"]=bynum[row["poem_number"]]; row["validation_status"]="review" if int(row["issue_count"]) else "pass"
    with p["poems_manifest"].open("w",encoding="utf-8",newline="") as f:
        w=csv.DictWriter(f,fieldnames=rows[0].keys()); w.writeheader(); w.writerows(rows)
    if verbose: print(f"Validation: {report['status']}; {report['errors']} errors, {report['warnings']} warnings, {report['info']} info")
    return report

if __name__ == "__main__":
    ap=argparse.ArgumentParser(); ap.add_argument("--work",required=True); ap.add_argument("--force",action="store_true"); ap.add_argument("--dry-run",action="store_true"); ap.add_argument("--verbose",action="store_true")
    a=ap.parse_args(); validate(a.work,a.force,a.dry_run,a.verbose)
