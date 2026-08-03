#!/usr/bin/env python3
"""Source-specific pipeline for Project Madurai pmuni0038 Patiṟṟuppattu."""
from __future__ import annotations
import collections, csv, hashlib, json, re, unicodedata
from pathlib import Path
from typing import Any
import yaml
from bs4 import BeautifulSoup
from corpuslib import ROOT, body_hash, canonical_body_text, markdown_literary_lines, read_frontmatter, write_json, write_work_issues

RAW=ROOT/"sources/raw-html/patirruppattu.html"
PARSED=ROOT/"sources/source-metadata/patirruppattu-parsed.json"
NORMALIZED=ROOT/"sources/source-metadata/patirruppattu-normalized.json"
SOURCE_META=ROOT/"sources/source-metadata/patirruppattu.json"
RECON=ROOT/"sources/source-metadata/patirruppattu-reconnaissance.json"
RAW_TXT=ROOT/"sources/raw-txt/patirruppattu.txt"
CORPUS=ROOT/"corpus/patirruppattu"; POEMS=CORPUS/"poems"; SECTIONS=CORPUS/"sections"
PM_ID="pmuni0038"; URL="https://www.projectmadurai.org/pm_etexts/utf8/pmuni0038.html"
EXPECTED_SHA="dc783dbf0141205625e7a27d9a14848b2dcef316e935dc66770f0ce082e012cc"; EXPECTED_BYTES=236971
GROUP_NAMES={2:"இரண்டாம் பத்து",3:"மூன்றாம் பத்து",4:"நான்காம் பத்து",5:"ஐந்தாம் பத்து",6:"ஆறாம் பத்து",7:"ஏழாம் பத்து",8:"எட்டாம் பத்து",9:"ஒன்பதாம் பத்து"}
POEM_RE=re.compile(r"^பாட்டு\s*-\s*(\d{1,3})$")
LINE_MARKER_RE=re.compile(r"(?:[ \u00a0]+)\d{1,3}\s*$")
META_RE=re.compile(r"^(துறை|வண்ணம்|தூக்கு|பெயர்)\s*[-:]\s*(.*)$")

def sha(p:Path)->str:return hashlib.sha256(p.read_bytes()).hexdigest()
def lines()->list[str]:
 s=BeautifulSoup(RAW.read_bytes().decode("utf-8-sig"),"lxml")
 return [x.strip() for x in s.get_text("\n").splitlines() if x.strip()]

def verify_source()->None:
 if not RAW.is_file() or RAW.stat().st_size!=EXPECTED_BYTES or sha(RAW)!=EXPECTED_SHA:raise RuntimeError("Patiṟṟuppattu raw source mismatch")
 RAW.read_bytes().decode("utf-8-sig")

def parse()->dict[str,Any]:
 verify_source(); ls=lines(); starts=[(i,int(m.group(1))) for i,x in enumerate(ls) if (m:=POEM_RE.match(x)) and 11<=int(m.group(1))<=90]
 if [n for _,n in starts]!=list(range(11,91)):raise RuntimeError("Expected source records 11 through 90")
 group_positions=[]
 for g,name in GROUP_NAMES.items():
  pos=next(i for i,x in enumerate(ls) if re.sub(r"\s+"," ",x)==name)
  group_positions.append((pos,g,name))
 poems=[]; groups=[]
 for pos,g,name in group_positions:
  next_group=next((p for p,gg,_ in group_positions if gg==g+1),next((i for i,x in enumerate(ls[pos+1:],pos+1) if x=="பத்தாம் பத்து"),len(ls)))
  intro=ls[pos+1:pos+12]
  patron_label=next((i for i,x in enumerate(intro) if x=="பாடப்பட்டோன்:"),None)
  poet_label=next((i for i,x in enumerate(intro) if x=="பாடியவர்:"),None)
  patron=intro[patron_label+1] if patron_label is not None else None
  poet=intro[poet_label+1] if poet_label is not None else None
  nums=[n for i,n in starts if pos<i<next_group]
  groups.append({"sequence":g,"heading_as_printed":name,"poem_start":min(nums),"poem_end":max(nums),"record_count":len(nums),"patron_as_printed":patron,"poet_as_printed":poet,"source":"Project Madurai printed group heading"})
 for j,(start,n) in enumerate(starts):
  stop=starts[j+1][0] if j+1<len(starts) else next(i for i,x in enumerate(ls[start+1:],start+1) if x=="(பதிகம்)")
  # A group-final poem ends before its printed பதிகம், not at the next group.
  possible=next((i for i,x in enumerate(ls[start+1:stop],start+1) if x=="(பதிகம்)"),None)
  if possible is not None:stop=possible
  block=ls[start+1:stop]
  while block and set(block[0])<={"~"}:block.pop(0)
  meta_at=next((i for i,x in enumerate(block) if META_RE.match(x)),len(block))
  body=[LINE_MARKER_RE.sub("",x).rstrip() for x in block[:meta_at] if x]
  meta=block[meta_at:]; fields={"thurai":None,"vannam":None,"thookku":None,"title_as_printed":None}
  keymap={"துறை":"thurai","வண்ணம்":"vannam","தூக்கு":"thookku","பெயர்":"title_as_printed"}
  for x in meta:
   m=META_RE.match(x)
   if m:fields[keymap[m.group(1)]]=m.group(2).strip()
  g=(n-1)//10+1; group=next(x for x in groups if x["sequence"]==g)
  poems.append({"poem_number":n,"poem_number_as_printed":n,"source_order":len(poems)+1,"printed_heading":f"பாட்டு - {n}","pattu":group["heading_as_printed"],"pattu_sequence":g,"position_within_pattu":n-(g-1)*10,
    "poet":group["poet_as_printed"],"patron":group["patron_as_printed"],**fields,"lines":body,"source_note_lines":meta,"status":"source-transcribed","source_object_id":PM_ID})
 # group பதிகம் blocks and lost-group evidence are retained structurally, not as canonical poem bodies.
 patikams=[]
 for pos,g,name in group_positions:
  p=next(i for i,x in enumerate(ls[pos:],pos) if x=="(பதிகம்)")
  end=next(i for i,x in enumerate(ls[p+1:],p+1) if "பத்து முற்றிற்று" in x)
  patikams.append({"pattu_sequence":g,"heading_as_printed":"(பதிகம்)","lines_as_printed":ls[p+1:end],"provenance":"printed by selected canonical source"})
 fragment_at=next(i for i,x in enumerate(ls) if x=="பத்தாம் பத்து")
 closing=next(i for i,x in enumerate(ls[fragment_at:],fragment_at) if "பதிற்றுப்பத்து முற்றிற்று" in x)
 return {"parser":"patirruppattu-pmuni0038-v1","work_slug":"patirruppattu","title_tamil":"பதிற்றுப்பத்து","title_english":"Patiṟṟuppattu","poems":poems,"pattu_groups":groups,
  "lost_groups":[{"sequence":1,"heading_as_printed":"முதற் பத்து","loss_as_printed":"(கிடைத்திலது)"},{"sequence":10,"heading_as_printed":"பத்தாம் பத்து","loss_as_printed":"(கிடைக்கவில்லை)"}],
  "patikams":patikams,"recovered_fragments_as_printed":ls[fragment_at+3:closing],"unparsed_fragments":[]}

def extract(force=True,dry_run=False,verbose=False):
 data=parse()
 if dry_run:print("Would extract 80 numbered records in eight surviving groups");return
 RAW_TXT.parent.mkdir(parents=True,exist_ok=True);RAW_TXT.write_text("\n".join(lines())+"\n",encoding="utf-8")
 write_json(PARSED,data,force=True)
 sm={"work":"patirruppattu","source_name":"Project Madurai","project_madurai_id":PM_ID,"source_url":URL,"source_file":"sources/raw-html/patirruppattu.html","source_bytes":EXPECTED_BYTES,"source_checksum_sha256":EXPECTED_SHA,"accessed_date":"2026-07-29","source_artifact_type":"exact HTTP HTML response body"}
 write_json(SOURCE_META,sm,force=True)
 rec={"work":"patirruppattu","parser":data["parser"],"canonical_source":sm,"printed_numbered_records":80,"number_range":[11,90],"missing_within_range":[],"duplicate_numbers":[],"surviving_pattu_groups":data["pattu_groups"],"source_lost_groups":data["lost_groups"],"patikam_count":len(data["patikams"]),"recovered_fragments_classification":"printed ancillary evidence, not numbered canonical records","navigation_strategy":"eight source-printed surviving pattu groups","commentary_present":False,"candidate_texts":[],"source_lost_numbered_records":[],"notes":["The source explicitly lacks the first and tenth pattu groups.","Records 11-90 are preserved; absent records outside that printed surviving range are not manufactured.","Printed பதிகம் blocks and recovered fragments remain structural/source evidence outside canonical poem bodies."]}
 write_json(RECON,rec,force=True)
 if verbose:print("Extracted 80 records")

def normalize(force=True,dry_run=False,verbose=False):
 d=json.load(open(PARSED))
 for p in d["poems"]:
  p["lines"]=[unicodedata.normalize("NFC",x) for x in p["lines"]];p["source_note_lines"]=[unicodedata.normalize("NFC",x) for x in p["source_note_lines"]]
 d["normalization"]="Unicode NFC; LF; HTML entities decoded; trailing five-line layout numbers removed"
 if not dry_run:write_json(NORMALIZED,d,force=True)

def md(p):
 fm={"schema_version":"1.0.0","work":"பதிற்றுப்பத்து","work_english":"Patiṟṟuppattu","work_id":"patirruppattu","work_slug":"patirruppattu","record_type":"numbered_poem","poem_number":p["poem_number"],"poem_number_as_printed":p["poem_number_as_printed"],"source_order":p["source_order"],"section":f"{p['pattu_sequence']:02d}-pattu","section_source":"Project Madurai printed pattu heading","pattu":p["pattu"],"pattu_sequence":p["pattu_sequence"],"position_within_pattu":p["position_within_pattu"],"thinai":None,"thinai_source":None,"speaker":None,"speaker_source":None,"poet":p["poet"],"poet_source":"Project Madurai printed group metadata","patron":p["patron"],"patron_source":"Project Madurai printed group metadata","thurai":p["thurai"],"title_as_printed":p["title_as_printed"],"first_line":p["lines"][0] if p["lines"] else "","line_count":len(p["lines"]),"textual_status":"complete","canonical_text_available":True,"candidate_texts_available":False,"lacuna_present":False,"lacuna_location":None,"source_note_available":bool(p["source_note_lines"]),"source_note_source":"Project Madurai printed poem metadata","extraction_status":"success","source":"Project Madurai","source_url":URL,"project_madurai_id":PM_ID,"source_object_id":PM_ID,"source_file":"sources/raw-html/patirruppattu.html","source_sha256":EXPECTED_SHA,"language":"Tamil","script":"Tamil","status":"source-transcribed","editorial_changes":False}
 y=yaml.safe_dump(fm,allow_unicode=True,sort_keys=False).strip();out=f"---\n{y}\n---\n\n# பதிற்றுப்பத்து {p['poem_number']}\n\n"+"\n".join(p["lines"])+"\n"
 if p["source_note_lines"]:out+="\n## Source note (as printed)\n\n"+"\n".join(p["source_note_lines"])+"\n"
 return out

def split(force=True,dry_run=False,verbose=False):
 d=json.load(open(NORMALIZED)); poems=d["poems"]
 if dry_run:print("Would write 80 records and eight source-group sections");return
 POEMS.mkdir(parents=True,exist_ok=True);SECTIONS.mkdir(parents=True,exist_ok=True)
 ep={f"{n:03d}.md" for n in range(11,91)};es={f"{g:02d}-{(g-1)*10+1:03d}-{g*10:03d}.md" for g in range(2,10)}
 bad=[x for x in POEMS.rglob("*") if x.is_file() and (x.parent!=POEMS or x.name not in ep)]+[x for x in SECTIONS.rglob("*") if x.is_file() and (x.parent!=SECTIONS or x.name not in es)]
 if bad:raise RuntimeError(f"Unexpected physical files: {bad}")
 for p in poems:(POEMS/f"{p['poem_number']:03d}.md").write_text(md(p),encoding="utf-8",newline="\n")
 for g in range(2,10):
  ps=[p for p in poems if p["pattu_sequence"]==g];(SECTIONS/f"{g:02d}-{ps[0]['poem_number']:03d}-{ps[-1]['poem_number']:03d}.md").write_text(f"# {ps[0]['pattu']}\n\nProject Madurai source-printed group.\n\n"+"\n".join(md(p).split("---\n",2)[-1].lstrip() for p in ps),encoding="utf-8")
 (CORPUS/"full-text.md").write_text("# பதிற்றுப்பத்து — source transcription\n\n"+"\n".join(md(p).split("---\n",2)[-1].lstrip() for p in poems),encoding="utf-8")
 write_json(CORPUS/"structure-inventory.json",{"surviving_pattu_groups":d["pattu_groups"],"lost_groups":d["lost_groups"],"patikams":d["patikams"],"recovered_fragments_as_printed":d["recovered_fragments_as_printed"]},force=True)
 meta={"corpus_schema_version":"1.0.0","version_status":"frozen","title_tamil":"பதிற்றுப்பத்து","title_english":"Patiṟṟuppattu","work_slug":"patirruppattu","work_id":"patirruppattu","collection":"எட்டுத்தொகை","expected_poem_count":80,"numbered_poem_record_count":80,"available_poem_count":80,"missing_poems":[],"source_lost_groups":[1,10],"source_name":"Project Madurai","source_url":URL,"project_madurai_id":PM_ID,"source_file":"sources/raw-html/patirruppattu.html","source_checksum_sha256":EXPECTED_SHA,"source_bytes":EXPECTED_BYTES,"accessed_date":"2026-07-29","encoding":"UTF-8","normalization":"Unicode NFC","source_structure":{"surviving_pattu_groups":8,"numbered_range":[11,90],"navigation_sections":8},"notes":["First and tenth pattu groups are explicitly unavailable in the source.","Recovered fragments printed after the tenth-group loss notice are preserved structurally and not promoted to numbered canonical records.","Version 1.0.0 freezes pmuni0038, records 11-90, eight surviving groups, lost-group representation, பதிகம் and fragment separation, canonical bodies, source notes, provenance and validation expectations."]}
 write_json(CORPUS/"metadata.json",meta,force=True)

def validate(dry_run=False,verbose=False):
 d=json.load(open(NORMALIZED));src={p["poem_number"]:p for p in d["poems"]};issues=[];fidelity=[];required=["schema_version","work","work_id","poem_number","textual_status","canonical_text_available","extraction_status","source_object_id","pattu","pattu_sequence","position_within_pattu","source_note_available"]
 ep={f"{n:03d}.md" for n in range(11,91)};es={f"{g:02d}-{(g-1)*10+1:03d}-{g*10:03d}.md" for g in range(2,10)}
 phys=[x for x in POEMS.rglob("*") if x.is_file()];secs=[x for x in SECTIONS.rglob("*") if x.is_file()];schema=0;hashes=collections.defaultdict(list);nums=[]
 def add(n,t,m):issues.append({"work":"patirruppattu","poem_number":n,"issue_type":t,"severity":"error","message":m,"source_file":"","markdown_file":""})
 if len(phys)!=80 or {x.name for x in phys if x.parent==POEMS}!=ep:add(None,"physical_poem_inventory","Expected exactly 011.md-090.md")
 if len(secs)!=8 or {x.name for x in secs if x.parent==SECTIONS}!=es:add(None,"physical_section_inventory","Expected eight surviving pattu sections")
 for name in sorted(ep):
  path=POEMS/name;fm,b=read_frontmatter(path);n=fm["poem_number"];nums.append(n);missing=[k for k in required if k not in fm]
  if missing:add(n,"missing_schema_keys",str(missing))
  else:schema+=1
  ml=markdown_literary_lines(b);sh=body_hash(src[n]["lines"]);mh=body_hash(ml);note=[]
  if "## Source note (as printed)" in b:note=[x.strip() for x in b.split("## Source note (as printed)",1)[1].splitlines() if x.strip()]
  nm=canonical_body_text(note)==canonical_body_text(src[n]["source_note_lines"]);fidelity.append({"poem_number":n,"source_body_hash_sha256":sh,"markdown_body_hash_sha256":mh,"source_output_match":sh==mh,"source_note_match":nm});hashes[mh].append(n)
  if sh!=mh:add(n,"source_output_mismatch","body mismatch")
  if not nm:add(n,"source_note_output_mismatch","note mismatch")
 dup=[v for v in hashes.values() if len(v)>1]
 if dup:add(None,"duplicate_poem_body",str(dup))
 report={"work":"patirruppattu","source_record_count":80,"canonical_poem_files":len(phys),"canonical_literary_texts_available":80,"source_lost_groups":[1,10],"navigation_sections":len(secs),"schema_files_checked":80,"schema_files_passing":schema,"schema_files_failing":80-schema,"source_output_matches":sum(x["source_output_match"] for x in fidelity),"source_note_matches":sum(x["source_note_match"] for x in fidelity),"duplicate_full_bodies":dup,"source_output_fidelity":fidelity,"errors":len(issues),"warnings":0,"info":2,"issues":issues,"status":"pass" if not issues else "fail"}
 if not dry_run:write_json(ROOT/"manifests/patirruppattu-validation-report.json",report,force=True);write_json(ROOT/"manifests/validation-report.json",report,force=True);write_work_issues("patirruppattu",issues)
 if verbose:print(f"Validation {report['status']}: {report['errors']} errors")
 return report
