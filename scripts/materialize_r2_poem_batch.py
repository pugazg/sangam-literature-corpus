#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json, subprocess
from pathlib import Path
import yaml

CANONICAL=["literary_domain","tinai_turai","landscape_environment","season_weather_time","flora","fauna","people_social_roles","relationships","emotion_lived_experience","occupations_production","food_subsistence","clothing_ornaments_adornment","material_culture_everyday_objects","weapons_warfare","mobility_transport","settlements_built_environment","economy","trade_exchange","polity_political_life","communities_social_groups","family_gender_kinship","religion_ritual","death_mourning_memory","arts_music_performance","knowledge_technology","values_ethical_concepts","body_health","named_entities","textual_intertextual_relationships"]
EMPTY="No qualifying evidence identified in this reviewed source record; never evidence of historical absence."

def sha(path): return hashlib.sha256(path.read_bytes()).hexdigest()
def blob(path,root): return subprocess.check_output(["git","hash-object",str(path.relative_to(root))],cwd=root,text=True).strip()
def parse(path):
    text=path.read_text(encoding="utf-8"); _,rest=text.split("---\n",1); front_text,rest=rest.split("\n---\n",1)
    front=yaml.safe_load(front_text); raw=rest.splitlines()
    while raw and not raw[0].startswith("# "): raw.pop(0)
    if raw: raw.pop(0)
    body=[]; sections={}; active=None
    for line in raw:
        if line.startswith("## "):
            active=line[3:].strip(); sections[active]=[]; continue
        if active is None:
            if line!="": body.append(line)
        elif line!="": sections[active].append(line)
    return front,body,sections
def body_hash(lines): return hashlib.sha256(("\n".join(lines)+"\n").encode()).hexdigest()
def bref(sel,lines):
    if sel[0]=="line": a=b=sel[1]
    elif sel[0]=="range": a,b=sel[1],sel[2]
    else: raise ValueError(f"unsupported selector {sel}")
    return {"source_field":"canonical_body","source_location":"markdown:canonical-body","evidence_span":{"start_line":a,"start_character":0,"end_line":b,"end_character":len(lines[b-1])},"source_text":"\n".join(lines[a-1:b])}
def mvalue(field,front,sections):
    if field=="source_note_as_printed": return "\n".join(sections.get("Source note (as printed)",[]))
    return front.get(field)
def mref(field,front,sections):
    value=mvalue(field,front,sections)
    if field=="source_note_as_printed":
        lines=sections.get("Source note (as printed)",[])
        span={"start_line":1,"start_character":0,"end_line":len(lines),"end_character":len(lines[-1])} if lines else None
        return {"source_field":field,"source_location":"markdown:source-note","evidence_span":span,"source_text":value}
    return {"source_field":field,"source_location":f"yaml:{field}","evidence_span":None,"source_text":value}
def oid(record_id,dim,basis,refs):
    raw=json.dumps({"record_id":record_id,"dimension":dim,"classification_basis":basis,"evidence_refs":refs},ensure_ascii=False,sort_keys=True,separators=(",",":")).encode()
    return "obs.prod.r2."+hashlib.sha256(raw).hexdigest()[:24]
def obs(record_id,dim,refs,basis="direct_record_review",concept=None,confidence="high",hist="not_applicable",note="Source-explicit evidence retained without external expansion."):
    return {"observation_id":oid(record_id,dim,basis,refs),"dimension":dim,"concept_id":concept,"evidence_class":"SOURCE_EXPLICIT","classification_basis":basis,"evidence_refs":refs,"confidence":confidence,"review_status":"reviewed","reviewer_type":"assistant_assisted","historical_identity_status":hist,"note":note}
def flatten(root,work_id):
    rows=[]
    for path in sorted((root/f"research/production/{work_id}/records").glob("[0-9][0-9][0-9].json")):
        rows.extend(json.loads(path.read_text(encoding="utf-8"))["observations"])
    out=root/f"research/observations/{work_id}/r2-production.ndjson"; out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text("".join(json.dumps(x,ensure_ascii=False,separators=(",",":"))+"\n" for x in rows),encoding="utf-8")
def materialize(root,spec_path):
    spec=json.loads(spec_path.read_text(encoding="utf-8")); work_id=spec["work_id"]; maximum=int(spec["work_record_count"])
    if spec.get("schema_version")!="0.4.0" or spec.get("phase")!="R2": raise ValueError("spec contract mismatch")
    outdir=root/f"research/production/{work_id}/records"; outdir.mkdir(parents=True,exist_ok=True)
    for rid,cfg in sorted(spec["records"].items()):
        n=int(rid); src=root/f"corpus/{work_id}/poems/{rid}.md"; front,lines,sections=parse(src); record_id=f"{work_id}-{rid}"
        observations=[]; reviewed=[]
        for key,dim in (("literary_domain","literary_domain"),("tinai","tinai_turai")):
            d=cfg["metadata"][key]; value=mvalue(d["field"],front,sections)
            if value not in (None,"") and d.get("concept_id") is not None:
                refs=[mref(d["field"],front,sections)]
                observations.append(obs(record_id,dim,refs,d["basis"],d.get("concept_id"),confidence=d.get("confidence","high"),note=d.get("note","Source-explicit metadata retained.")))
                role="source_explicit_evidence"
            else: role="reviewed_empty_or_unresolved"
            reviewed.append({"source_field":d["field"],"source_text":value,"classification_role":role})
        d=cfg["metadata"]["speaker"]; value=mvalue(d["field"],front,sections)
        if value not in (None,"") and d.get("roles"):
            refs=[mref(d["field"],front,sections)]
            for dim in d["roles"]: observations.append(obs(record_id,dim,refs,d.get("basis","source_metadata_explicit"),confidence=d.get("confidence","high"),note=d["note"]))
            role="source_explicit_evidence"
        else: role="reviewed_empty_or_unresolved"
        reviewed.append({"source_field":d["field"],"source_text":value,"classification_role":role})
        d=cfg["metadata"]["poet"]; value=mvalue(d["field"],front,sections)
        if value not in (None,""):
            refs=[mref(d["field"],front,sections)]
            observations.append(obs(record_id,d["dimension"],refs,d.get("basis","source_metadata_explicit"),hist=d["historical_identity_status"],note=d.get("note","Printed poet attribution retained as an unresolved mention.")))
            role="unresolved_mention"
        else: role="reviewed_empty_or_unresolved"
        reviewed.append({"source_field":d["field"],"source_text":value,"classification_role":role})
        reviewed.append({"source_field":"section","source_text":front.get("section"),"classification_role":"mechanical_navigation_only"})
        for dim,dcfg in cfg["dimensions"].items():
            refs=[bref(x,lines) for x in dcfg["e"]]
            observations.append(obs(record_id,dim,refs,confidence=dcfg.get("confidence","high"),hist=dcfg.get("historical_identity_status","not_applicable"),note=dcfg["note"]))
        bydim={d:[] for d in CANONICAL}
        for o in observations: bydim[o["dimension"]].append(o["observation_id"])
        reviews=[{"ordinal":i,"dimension":d,"status":"evidence_recorded" if bydim[d] else "no_qualifying_evidence_identified","observation_ids":bydim[d],"review_note":"Qualifying source evidence recorded." if bydim[d] else "No qualifying evidence identified."} for i,d in enumerate(CANONICAL,1)]
        rec={"schema_version":"0.4.0","phase":"R2","production_review_id":f"{work_id}-r2-production-{rid}","work_id":work_id,"record_id":record_id,"source_sequence":n,
          "source_snapshot":{"canonical_record_path":f"corpus/{work_id}/poems/{rid}.md","canonical_record_git_blob_sha":blob(src,root),"canonical_record_sha256":sha(src),"canonical_body_sha256":body_hash(lines),"textual_status":str(front["textual_status"]),"canonical_text_available":bool(front["canonical_text_available"])},
          "source_metadata_reviewed":reviewed,"dimensions_considered":29,"dimension_reviews":reviews,"observations":observations,"review_status":"reviewed","reviewer_type":"assistant_assisted","empty_cell_semantics":EMPTY,"next_record_allowed":f"{work_id}-{n+1:03d}" if n<maximum else None}
        (outdir/f"{rid}.json").write_text(json.dumps(rec,ensure_ascii=False,separators=(",",":"))+"\n",encoding="utf-8")
        print(json.dumps({"work":work_id,"record":rid,"observations":len(observations)},ensure_ascii=False))
    flatten(root,work_id)
def main():
    p=argparse.ArgumentParser();p.add_argument("--root",default=".");p.add_argument("--spec",required=True);a=p.parse_args();root=Path(a.root).resolve();materialize(root,(root/a.spec).resolve())
if __name__=="__main__":main()
