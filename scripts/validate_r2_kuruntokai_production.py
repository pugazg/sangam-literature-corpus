#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json
from pathlib import Path
import yaml
from materialize_r2_kuruntokai_batch import CANONICAL, EMPTY, body_hash, oid, parse

def load(p): return json.loads(p.read_text(encoding="utf-8"))
def slice_text(lines,s):
    a,b,ac,bc=s["start_line"],s["end_line"],s["start_character"],s["end_character"]
    if a==b:return lines[a-1][ac:bc]
    return "\n".join([lines[a-1][ac:],*lines[a:b-1],lines[b-1][:bc]])
def validate(root):
    errors=[]; paths=sorted((root/"research/production/kuruntokai/records").glob("[0-9][0-9][0-9].json")); nums=[int(x.stem) for x in paths]
    if nums and nums!=list(range(1,max(nums)+1)): errors.append("records must form gap-free prefix from 001")
    flat=[]
    for p in paths:
        v=load(p); n=int(p.stem); rid=f"{n:03d}"; recid=f"kuruntokai-{rid}"; src=root/f"corpus/kuruntokai/poems/{rid}.md"; front,lines=parse(src)
        def err(x): errors.append(f"{p}: {x}")
        if v.get("schema_version")!="0.4.0" or v.get("phase")!="R2" or v.get("work_id")!="kuruntokai":err("contract mismatch")
        if v.get("record_id")!=recid or v.get("source_sequence")!=n or v.get("production_review_id")!=f"kuruntokai-r2-production-{rid}":err("identity mismatch")
        if v.get("dimensions_considered")!=29 or [(x.get("ordinal"),x.get("dimension")) for x in v.get("dimension_reviews",[])]!=list(enumerate(CANONICAL,1)):err("29-dimension order mismatch")
        if v.get("empty_cell_semantics")!=EMPTY or v.get("review_status")!="reviewed":err("review/empty contract mismatch")
        snap=v.get("source_snapshot",{})
        if snap.get("canonical_record_sha256")!=hashlib.sha256(src.read_bytes()).hexdigest() or snap.get("canonical_body_sha256")!=body_hash(lines):err("canonical hash mismatch")
        evidence={}
        for o in v.get("observations",[]):
            refs=o.get("evidence_refs",[]); expected=oid(recid,o.get("dimension"),o.get("classification_basis"),refs)
            if o.get("observation_id")!=expected:err("observation id mismatch")
            for r in refs:
                if r.get("source_location")=="markdown:canonical-body" and slice_text(lines,r["evidence_span"])!=r.get("source_text"):err("body span mismatch")
                if r.get("source_location","").startswith("yaml:") and front.get(r["source_field"])!=r.get("source_text"):err("metadata evidence mismatch")
            evidence[o["observation_id"]]=o
        seen=set()
        for d in v["dimension_reviews"]:
            ids=d["observation_ids"]; seen.update(ids); exp="evidence_recorded" if ids else "no_qualifying_evidence_identified"
            if d["status"]!=exp:err("dimension status mismatch")
            if any(x not in evidence or evidence[x]["dimension"]!=d["dimension"] for x in ids):err("dimension observation reference mismatch")
        if seen!=set(evidence):err("orphan observation")
        expected_next=f"kuruntokai-{n+1:03d}" if n<401 else None
        if v.get("next_record_allowed")!=expected_next:err("next-record mismatch")
        flat.extend(v["observations"])
    stream=root/"research/observations/kuruntokai/r2-production.ndjson"
    rows=[json.loads(x) for x in stream.read_text(encoding="utf-8").splitlines() if x.strip()] if stream.is_file() else []
    if rows!=flat:errors.append("flattened stream differs from records")
    return {"phase":"R2","gate":"kuruntokai-production-prefix","records_reviewed":len(paths),"records_remaining":401-len(paths),"next_record":f"kuruntokai-{len(paths)+1:03d}" if len(paths)<401 else None,"observations_checked":len(flat),"dimensions":29,"errors":errors,"status":"pass" if not errors else "fail"}
def main():
    p=argparse.ArgumentParser();p.add_argument("--root",default=".");a=p.parse_args();r=validate(Path(a.root).resolve());print(json.dumps(r,ensure_ascii=False,indent=2));raise SystemExit(0 if r["status"]=="pass" else 1)
if __name__=="__main__":main()
