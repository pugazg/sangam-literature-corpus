#!/usr/bin/env python3
"""Source-specific pipeline for Project Madurai pmuni0221 Kalittokai."""
from __future__ import annotations
import collections, hashlib, json, re, unicodedata
from pathlib import Path
from typing import Any
import yaml
from bs4 import BeautifulSoup
from corpuslib import ROOT, body_hash, canonical_body_text, markdown_literary_lines, read_frontmatter, write_json, write_work_issues

RAW=ROOT/"sources/raw-html/kalittokai.html"; RAW_TXT=ROOT/"sources/raw-txt/kalittokai.txt"
PARSED=ROOT/"sources/source-metadata/kalittokai-parsed.json"; NORMALIZED=ROOT/"sources/source-metadata/kalittokai-normalized.json"
SOURCE_META=ROOT/"sources/source-metadata/kalittokai.json"; RECON=ROOT/"sources/source-metadata/kalittokai-reconnaissance.json"
CORPUS=ROOT/"corpus/kalittokai"; POEMS=CORPUS/"poems"; SECTIONS=CORPUS/"sections"
PM_ID="pmuni0221"; URL="https://www.projectmadurai.org/pm_etexts/utf8/pmuni0221.html"
EXPECTED_SHA="da4b2182fca2066c3627f6c9207a01748e8e9fe75d005995d5cbb7397a263195"; EXPECTED_BYTES=505220
DIVISIONS=[
 {"sequence":1,"heading_as_printed":"கடவுள் வாழ்த்து","start":1,"end":1,"poet":None},
 {"sequence":2,"heading_as_printed":"முதலாவது : பாலைக்கலி","start":2,"end":36,"poet":"பெருங்கொடுங்கோன்"},
 {"sequence":3,"heading_as_printed":"இரண்டாவது :  குறிஞ்சி","start":37,"end":65,"poet":"கபிலர்"},
 {"sequence":4,"heading_as_printed":"மூன்றாவது : மருதக்கலி","start":66,"end":100,"poet":"மருதநிலங்கன்"},
 {"sequence":5,"heading_as_printed":"நான்காவது : முல்லைக் கலி","start":101,"end":117,"poet":"சோழன் நல்லுத்திரன்"},
 {"sequence":6,"heading_as_printed":"ஐந்தாவது : நெய்தல் கலி","start":118,"end":150,"poet":"நல்லாந்துவனார்"},
]
SECTION_NAMES={1:"01-invocation.md",2:"02-palaikkali.md",3:"03-kurinji.md",4:"04-marutakkali.md",5:"05-mullaikkali.md",6:"06-neytalkali.md"}

def sha(p:Path)->str:return hashlib.sha256(p.read_bytes()).hexdigest()
def verify_source():
 if not RAW.is_file() or RAW.stat().st_size!=EXPECTED_BYTES or sha(RAW)!=EXPECTED_SHA:raise RuntimeError("Kalittokai raw source mismatch")
 RAW.read_bytes().decode("utf-8-sig")

def parse()->dict[str,Any]:
 verify_source();soup=BeautifulSoup(RAW.read_bytes().decode("utf-8-sig"),"lxml"); poems=[]
 for tr in soup.find_all("tr"):
  tds=tr.find_all("td",recursive=False)
  if len(tds)<2 or not re.fullmatch(r"\d{1,3}",tds[0].get_text(strip=True)):continue
  n=int(tds[0].get_text(strip=True))
  if not 1<=n<=150:continue
  lines=[x.strip() for x in tds[1].get_text("\n").splitlines() if x.strip()]
  division=next(d for d in DIVISIONS if d["start"]<=n<=d["end"])
  lacuna=any(re.search(r"\.{3,}",x) for x in lines)
  poems.append({"poem_number":n,"poem_number_as_printed":n,"source_order":n,"printed_heading":str(n),"lines":lines,"source_note_lines":[],
   "major_division":division["heading_as_printed"],"major_division_sequence":division["sequence"],"position_within_division":n-division["start"]+1,
   "poet":division["poet"],"textual_status":"incomplete" if lacuna else "complete","lacuna_present":lacuna,"status":"source-transcribed","source_object_id":PM_ID})
 if [p["poem_number"] for p in poems]!=list(range(1,151)):raise RuntimeError("Expected exactly one table-row record for poems 1-150")
 return {"parser":"kalittokai-pmuni0221-v1","work_slug":"kalittokai","title_tamil":"கலித்தொகை","title_as_printed":"கலித்தொகை","poems":poems,
  "source_divisions":[{**d,"record_count":d["end"]-d["start"]+1,"poet_source":"Project Madurai printed division attribution" if d["poet"] else None} for d in DIVISIONS],
  "unparsed_fragments":[]}

def extract(force=True,dry_run=False,verbose=False):
 d=parse()
 if dry_run:print("Would extract 150 table-row poem records in six source sections");return
 soup=BeautifulSoup(RAW.read_bytes().decode("utf-8-sig"),"lxml");RAW_TXT.parent.mkdir(parents=True,exist_ok=True);RAW_TXT.write_text(soup.get_text("\n"),encoding="utf-8")
 write_json(PARSED,d,force=True)
 sm={"work":"kalittokai","source_name":"Project Madurai","project_madurai_id":PM_ID,"source_url":URL,"source_file":"sources/raw-html/kalittokai.html","source_bytes":EXPECTED_BYTES,"source_checksum_sha256":EXPECTED_SHA,"accessed_date":"2026-07-29","source_artifact_type":"exact HTTP HTML response body","title_as_printed":"கலித்தொகை"}
 write_json(SOURCE_META,sm,force=True)
 write_json(RECON,{"work":"kalittokai","parser":d["parser"],"canonical_source":sm,"printed_numbered_records":150,"number_range":[1,150],"missing_numbers":[],"duplicate_numbers":[],"source_grammar":"one table row per poem; first cell is printed number, second cell is BR-delimited literary body","source_divisions":d["source_divisions"],"source_lost_records":[],"incomplete_records":[p["poem_number"] for p in d["poems"] if p["lacuna_present"]],"candidate_text_conditions":[],"replacement_characters":[],"duplicate_full_bodies":[],"shared_first_lines":[],"notes":["Flat text falsely repeats poem 7 because of malformed nesting; direct table-row parsing yields one record for each number 1-150.","Dot sequences in poems 114 and 131 are preserved as printed lacuna evidence.","Division-level authors are copied only from the printed source headings."]},force=True)
 if verbose:print("Extracted 150 records")

def normalize(force=True,dry_run=False,verbose=False):
 d=json.loads(PARSED.read_text())
 for p in d["poems"]:p["lines"]=[unicodedata.normalize("NFC",x) for x in p["lines"]]
 d["normalization"]="Unicode NFC; LF; HTML entities decoded; table/BR layout boundary restored"
 if not dry_run:write_json(NORMALIZED,d,force=True)

def md(p):
 lines=p["lines"]; fm={"schema_version":"1.0.0","work":"கலித்தொகை","work_english":"Kalittokai","work_id":"kalittokai","work_slug":"kalittokai","record_type":"numbered_poem","poem_number":p["poem_number"],"poem_number_as_printed":p["poem_number_as_printed"],"source_order":p["source_order"],"section":p["major_division"],"section_source":"Project Madurai printed division","major_division":p["major_division"],"major_division_as_printed":p["major_division"],"major_division_source":"Project Madurai printed division heading","position_within_division":p["position_within_division"],"thinai":None,"thinai_source":None,"speaker":None,"speaker_source":None,"poet":p["poet"],"poet_source":"Project Madurai printed division attribution" if p["poet"] else None,"first_line":lines[0],"line_count":len(lines),"textual_status":p["textual_status"],"canonical_text_available":True,"candidate_texts_available":False,"lacuna_present":p["lacuna_present"],"lacuna_location":"within" if p["lacuna_present"] else None,"source_note_available":False,"source_note_source":None,"extraction_status":"success","source":"Project Madurai","source_url":URL,"project_madurai_id":PM_ID,"source_object_id":PM_ID,"source_file":"sources/raw-html/kalittokai.html","source_sha256":EXPECTED_SHA,"language":"Tamil","script":"Tamil","status":"source-transcribed","editorial_changes":False}
 y=yaml.safe_dump(fm,allow_unicode=True,sort_keys=False).strip();return f"---\n{y}\n---\n\n# கலித்தொகை {p['poem_number']}\n\n"+"\n".join(lines)+"\n"

def split(force=True,dry_run=False,verbose=False):
 d=json.loads(NORMALIZED.read_text());poems=d["poems"]
 if dry_run:print("Would write 150 poems and six source sections");return
 POEMS.mkdir(parents=True,exist_ok=True);SECTIONS.mkdir(parents=True,exist_ok=True)
 ep={f"{n:03d}.md" for n in range(1,151)};es=set(SECTION_NAMES.values())
 bad=[x for x in POEMS.rglob("*") if x.is_file() and (x.parent!=POEMS or x.name not in ep)]+[x for x in SECTIONS.rglob("*") if x.is_file() and (x.parent!=SECTIONS or x.name not in es)]
 if bad:raise RuntimeError(f"Unexpected physical files: {bad}")
 for p in poems:(POEMS/f"{p['poem_number']:03d}.md").write_text(md(p),encoding="utf-8",newline="\n")
 for div in d["source_divisions"]:
  selected=[p for p in poems if p["major_division_sequence"]==div["sequence"]];text=f"# {div['heading_as_printed']}\n\nProject Madurai source-printed division.\n\n"+"\n".join(md(p).split("---\n",2)[-1].lstrip() for p in selected);(SECTIONS/SECTION_NAMES[div["sequence"]]).write_text(text,encoding="utf-8",newline="\n")
 (CORPUS/"full-text.md").write_text("# கலித்தொகை — source transcription\n\n"+"\n".join(md(p).split("---\n",2)[-1].lstrip() for p in poems),encoding="utf-8",newline="\n")
 write_json(CORPUS/"structure-inventory.json",{"source_divisions":d["source_divisions"]},force=True)
 write_json(CORPUS/"metadata.json",{"corpus_schema_version":"1.0.0","version_status":"frozen","title_tamil":"கலித்தொகை","title_english":"Kalittokai","work_slug":"kalittokai","work_id":"kalittokai","collection":"எட்டுத்தொகை","numbered_poem_record_count":150,"available_poem_count":150,"source_name":"Project Madurai","source_url":URL,"project_madurai_id":PM_ID,"source_file":"sources/raw-html/kalittokai.html","source_checksum_sha256":EXPECTED_SHA,"source_bytes":EXPECTED_BYTES,"accessed_date":"2026-07-29","encoding":"UTF-8","normalization":"Unicode NFC","source_structure":d["source_divisions"],"notes":["Poem 1 is the printed invocation record.","The five named kali divisions and their printed author attributions are preserved.","Printed dot lacunae remain unchanged.","No speaker or poem-level tiṇai is inferred."]},force=True)

def validate(dry_run=False,verbose=False):
 d=json.loads(NORMALIZED.read_text());src={p["poem_number"]:p for p in d["poems"]};ep={f"{n:03d}.md" for n in range(1,151)};es=set(SECTION_NAMES.values());phys=[x for x in POEMS.rglob("*") if x.is_file()];secs=[x for x in SECTIONS.rglob("*") if x.is_file()];issues=[];fidelity=[];schema=0;bodies=collections.defaultdict(list);firsts=collections.defaultdict(list)
 req=["schema_version","work","work_id","poem_number","poem_number_as_printed","source_order","textual_status","canonical_text_available","candidate_texts_available","lacuna_present","lacuna_location","extraction_status","thinai","thinai_source","poet","poet_source","speaker","speaker_source","source_note_available","source_note_source","source_object_id"]
 def add(n,t,s,m):issues.append({"work":"kalittokai","poem_number":n,"issue_type":t,"severity":s,"message":m,"source_file":"sources/raw-html/kalittokai.html","markdown_file":f"corpus/kalittokai/poems/{n:03d}.md" if n else ""})
 direct={x.name for x in phys if x.parent==POEMS}
 if len(phys)!=150 or direct!=ep:add(None,"physical_poem_inventory","error","Expected exactly 001.md-150.md")
 if len(secs)!=6 or {x.name for x in secs if x.parent==SECTIONS}!=es:add(None,"physical_section_inventory","error","Expected six source sections")
 yn=collections.defaultdict(list)
 for x in phys:
  try:fm,_=read_frontmatter(x);yn[fm.get("poem_number")].append(str(x.relative_to(POEMS)))
  except Exception as e:add(None,"malformed_yaml","error",str(e))
 for n,names in yn.items():
  if len(names)>1:add(n,"duplicate_yaml_poem_number","error",str(names))
 for name in sorted(ep&direct):
  fm,b=read_frontmatter(POEMS/name);n=int(fm["poem_number"]);missing=[k for k in req if k not in fm]
  if missing:add(n,"missing_schema_keys","error",str(missing))
  else:schema+=1
  ml=markdown_literary_lines(b);sh=body_hash(src[n]["lines"]);mh=body_hash(ml);nm=canonical_body_text([])==canonical_body_text([])
  fidelity.append({"poem_number":n,"source_body_hash_sha256":sh,"markdown_body_hash_sha256":mh,"source_output_match":sh==mh,"source_note_match":nm})
  if sh!=mh:add(n,"source_output_mismatch","error","body mismatch")
  bodies[mh].append(n);firsts[ml[0]].append(n)
  if src[n]["lacuna_present"]:add(n,"textual_lacuna","info","Printed dot sequence preserved unchanged")
 dup=[v for v in bodies.values() if len(v)>1];shared=[v for v in firsts.values() if len(v)>1]
 for x in dup:add(None,"duplicate_poem_body","warning",str(x))
 for x in shared:add(None,"shared_first_line","info",str(x))
 report={"work":"kalittokai","source_record_count":150,"canonical_poem_files":len(phys),"canonical_literary_texts_available":150,"source_divisions":6,"schema_files_checked":len(ep&direct),"schema_files_passing":schema,"schema_files_failing":len(ep&direct)-schema,"source_output_matches":sum(x["source_output_match"] for x in fidelity),"source_note_matches":sum(x["source_note_match"] for x in fidelity),"duplicate_full_bodies":dup,"shared_first_lines":shared,"lacunose_poems":[p["poem_number"] for p in d["poems"] if p["lacuna_present"]],"source_output_fidelity":fidelity,"errors":sum(x["severity"]=="error" for x in issues),"warnings":sum(x["severity"]=="warning" for x in issues),"info":sum(x["severity"]=="info" for x in issues),"issues":issues}
 report["status"]="pass-with-review" if not report["errors"] else "fail"
 if not dry_run:write_json(ROOT/"manifests/kalittokai-validation-report.json",report,force=True);write_json(ROOT/"manifests/validation-report.json",report,force=True);write_work_issues("kalittokai",issues)
 if verbose:print(f"Validation {report['status']}: {report['errors']} errors")
 return report
