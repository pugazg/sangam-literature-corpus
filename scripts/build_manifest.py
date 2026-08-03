#!/usr/bin/env python3
"""Deterministic, atomic repository-wide manifest aggregation."""
from __future__ import annotations
import argparse,csv,fcntl,json,os,tempfile
from pathlib import Path
from corpuslib import ROOT,body_hash,markdown_literary_lines,paths,read_frontmatter,write_json

FIELDS=["work","work_id","work_slug","poem_number","poem_number_as_printed","source_order","section","major_division","major_division_as_printed","pattu","pattu_sequence","position_within_pattu","thinai","speaker","poet","first_line","line_count","textual_status","canonical_text_available","candidate_texts_available","lacuna_present","lacuna_location","source_note_available","extraction_status","body_hash_sha256","normalized_body_duplicate","shared_first_line","source_body_hash_sha256","markdown_body_hash_sha256","source_output_match","source_url","source_object_id","source_file","markdown_file","validation_status","issue_count","notes"]
POLICY_VERSION="repository-canonical-order-v1"
def canonical_row_key(row):return (row["work_slug"],row["markdown_file"])
def _rows(work):
 p=paths(work); parsed=json.loads(p["normalized"].read_text(encoding="utf-8")); source={int(x["poem_number"]):x for x in parsed["poems"]}; rows=[]
 for md in sorted(p["poems"].glob("*.md")):
  fm,body=read_frontmatter(md); src=source[int(fm["poem_number"])]; ml=markdown_literary_lines(body); sh=body_hash(src["lines"]);mh=body_hash(ml)
  rows.append({"work":fm["work"],"work_id":fm.get("work_id",work),"work_slug":work,"poem_number":fm["poem_number"],"poem_number_as_printed":fm.get("poem_number_as_printed"),"source_order":fm.get("source_order"),"section":fm.get("section"),"major_division":fm.get("major_division"),"major_division_as_printed":fm.get("major_division_as_printed"),"pattu":fm.get("pattu"),"pattu_sequence":fm.get("pattu_sequence"),"position_within_pattu":fm.get("position_within_pattu"),"thinai":fm.get("thinai"),"speaker":fm.get("speaker"),"poet":fm.get("poet"),"first_line":fm["first_line"],"line_count":fm["line_count"],"textual_status":fm["textual_status"],"canonical_text_available":fm["canonical_text_available"],"candidate_texts_available":fm["candidate_texts_available"],"lacuna_present":fm["lacuna_present"],"lacuna_location":fm["lacuna_location"],"source_note_available":fm["source_note_available"],"extraction_status":fm["extraction_status"],"body_hash_sha256":mh,"normalized_body_duplicate":False,"shared_first_line":False,"source_body_hash_sha256":sh,"markdown_body_hash_sha256":mh,"source_output_match":sh==mh,"source_url":fm["source_url"],"source_object_id":fm.get("source_object_id",fm.get("project_madurai_id")),"source_file":fm["source_file"],"markdown_file":str(md.relative_to(ROOT)),"validation_status":"pending","issue_count":0,"notes":""})
 bc={};fc={}
 for x in rows:
  if x["canonical_text_available"]:bc[x["body_hash_sha256"]]=bc.get(x["body_hash_sha256"],0)+1
  if x["first_line"]:fc[x["first_line"]]=fc.get(x["first_line"],0)+1
 for x in rows:x["normalized_body_duplicate"]=bool(x["canonical_text_available"] and bc.get(x["body_hash_sha256"],0)>1);x["shared_first_line"]=bool(x["first_line"] and fc.get(x["first_line"],0)>1)
 return rows
def aggregate_all(target=None):
 target=Path(target or ROOT/'manifests/poems.csv'); works=json.loads((ROOT/'manifests/works.json').read_text(encoding='utf-8')); order={x['work_slug']:i for i,x in enumerate(works)};rows=[]
 for x in works:
  if x.get('record_directory','poems')=='poems':rows.extend(_rows(x['work_slug']))
 rows.sort(key=lambda r:(order[r['work_slug']],int(r.get('source_order') or r['poem_number']),r['markdown_file']))
 keys=[canonical_row_key(x) for x in rows]
 if len(rows)!=5632 or len(set(keys))!=len(rows):raise ValueError(f'invalid canonical rows: {len(rows)} rows, {len(set(keys))} keys')
 target.parent.mkdir(parents=True,exist_ok=True);lock=target.with_suffix(target.suffix+'.lock')
 with lock.open('a+') as lf:
  fcntl.flock(lf,fcntl.LOCK_EX)
  tmp=None
  try:
   with tempfile.NamedTemporaryFile('w',encoding='utf-8',newline='',dir=target.parent,prefix='.poems.',suffix='.tmp',delete=False) as f:
    tmp=Path(f.name);w=csv.DictWriter(f,fieldnames=FIELDS,lineterminator='\n');w.writeheader();w.writerows(rows);f.flush();os.fsync(f.fileno())
   data=tmp.read_bytes();data.decode('utf-8');check=list(csv.DictReader(data.decode('utf-8').splitlines()))
   if len(check)!=5632:raise ValueError('temporary manifest failed validation')
   os.replace(tmp,target);tmp=None
  finally:
   if tmp and tmp.exists():tmp.unlink()
   fcntl.flock(lf,fcntl.LOCK_UN)
 lock.unlink(missing_ok=True)
 return rows
def build(work,force=False,dry_run=False,verbose=False):
 p=paths(work);metadata=json.loads(p['metadata'].read_text(encoding='utf-8'));works=[]
 if p['works_manifest'].exists():works=[x for x in json.loads(p['works_manifest'].read_text(encoding='utf-8')) if x.get('work_slug')!=work]
 works.append(metadata);works.sort(key=lambda x:x.get('work_slug',''));write_json(p['works_manifest'],works,force=True)
 if dry_run:return
 rows=aggregate_all()
 if verbose:print(f'Manifest contains {len(rows)} rows ({POLICY_VERSION})')
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--work');ap.add_argument('--all',action='store_true');ap.add_argument('--force',action='store_true');ap.add_argument('--dry-run',action='store_true');ap.add_argument('--verbose',action='store_true');a=ap.parse_args()
 if a.all:aggregate_all()
 elif a.work:build(a.work,a.force,a.dry_run,a.verbose)
 else:ap.error('--work or --all is required')
