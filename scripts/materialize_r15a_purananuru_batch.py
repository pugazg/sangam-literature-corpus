#!/usr/bin/env python3
from __future__ import annotations
import argparse, csv, hashlib, json, subprocess
from pathlib import Path
import yaml

CANONICAL = [
("LD","literary_domain"),("TT","tinai_turai"),("ENV","landscape_environment"),("SWT","season_weather_time"),
("FL","flora"),("FA","fauna"),("PSR","people_social_roles"),("REL","relationships"),("ELE","emotion_lived_experience"),
("OP","occupations_production"),("FS","food_subsistence"),("COA","clothing_ornaments_adornment"),
("MC","material_culture_everyday_objects"),("WW","weapons_warfare"),("MT","mobility_transport"),
("SBE","settlements_built_environment"),("ECO","economy"),("TRD","trade_exchange"),
("POL","polity_political_life"),("CSG","communities_social_groups"),("FGK","family_gender_kinship"),
("RR","religion_ritual"),("DMM","death_mourning_memory"),("AMP","arts_music_performance"),
("KT","knowledge_technology"),("VEC","values_ethical_concepts"),("BH","body_health"),("NE","named_entities"),
("TIR","textual_intertextual_relationships"),
]
EMPTY = "No qualifying evidence identified in this reviewed source record; never evidence of historical absence."
AUDIT = "research/audits/r15-premerge/purananuru/parts/001-050.tsv"

def sha256_bytes(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()

def git_blob(path: Path, root: Path) -> str:
    return subprocess.check_output(["git","hash-object",str(path.relative_to(root))],cwd=root,text=True).strip()

def parse_record(path: Path):
    text=path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        raise ValueError(f"{path}: missing YAML frontmatter")
    _, rest=text.split("---\n",1)
    front_text, rest=rest.split("\n---\n",1)
    front=yaml.safe_load(front_text)
    body_part, note_part=rest.split("\n## Source note (as printed)\n",1)
    body_lines=body_part.splitlines()
    while body_lines and not body_lines[0].startswith("# "): body_lines.pop(0)
    if body_lines and body_lines[0].startswith("# "): body_lines.pop(0)
    body_lines=[x for x in body_lines if x!=""]
    return front, body_lines, note_part.strip()

def load_r0(path: Path):
    rows=[json.loads(x) for x in path.read_text(encoding="utf-8").splitlines() if x.strip()]
    if not rows: raise ValueError(f"{path}: empty R0")
    return rows

def find_assertion(rows, typ, field=None, text=None):
    matches=[]
    for a in rows:
        if a.get("assertion_type") != typ: continue
        if field is not None and a.get("source_field") != field: continue
        if text is not None and a.get("source_text") != text: continue
        matches.append(a)
    if len(matches)!=1:
        raise ValueError(f"R0 assertion match {typ}/{field}/{text!r}: found {len(matches)}")
    return matches[0]["assertion_id"]

def evidence_ref(sel, front, lines, source_note):
    kind=sel[0]
    if kind=="line":
        n=sel[1]; text=lines[n-1]
        return {"source_field":"canonical_body","source_location":"markdown:canonical-body",
                "evidence_span":{"start_line":n,"start_character":0,"end_line":n,"end_character":len(text)},"source_text":text}
    if kind=="range":
        a,b=sel[1],sel[2]
        return {"source_field":"canonical_body","source_location":"markdown:canonical-body",
                "evidence_span":{"start_line":a,"start_character":0,"end_line":b,"end_character":len(lines[b-1])},
                "source_text":"\n".join(lines[a-1:b])}
    if kind=="span":
        n,a,b=sel[1],sel[2],sel[3]; text=lines[n-1][a:b]
        return {"source_field":"canonical_body","source_location":"markdown:canonical-body",
                "evidence_span":{"start_line":n,"start_character":a,"end_line":n,"end_character":b},"source_text":text}
    if kind=="yaml":
        field=sel[1]
        return {"source_field":field,"source_location":f"yaml:{field}","evidence_span":None,"source_text":front.get(field)}
    if kind=="source_note":
        return {"source_field":"source_note","source_location":"markdown:source-note","evidence_span":None,"source_text":source_note}
    raise ValueError(f"unknown evidence selector {sel}")

def observation_id(record_id, dimension, basis, refs):
    payload={"record_id":record_id,"dimension":dimension,"classification_basis":basis,"evidence_refs":refs}
    raw=json.dumps(payload,ensure_ascii=False,sort_keys=True,separators=(",",":")).encode("utf-8")
    return "obs.prod.r15."+hashlib.sha256(raw).hexdigest()[:24]

def mkobs(rid, dimension, refs, cfg, supporting):
    basis=cfg.get("basis") or ("reviewed_source_assertion" if supporting and not cfg.get("mixed") else "direct_record_review")
    if dimension in {"polity_political_life","named_entities","tinai_turai"} and cfg.get("metadata_basis"):
        basis="source_metadata_explicit"
    provenance=("mixed_existing_r0_and_direct_r15_source_review" if cfg.get("mixed")
                else "existing_r0_assertion_linked" if supporting
                else "direct_r15_source_review_no_prior_assertion")
    hist=cfg.get("historical_identity_status","not_applicable")
    note=cfg.get("note") or ("Printed identity retained; no external historical resolution." if hist=="unresolved"
         else "Source-explicit evidence retained conservatively; no external expansion." if cfg.get("confidence")=="medium"
         else "Source-explicit evidence retained without external expansion.")
    return {
      "observation_id":observation_id(rid,dimension,basis,refs),"dimension":dimension,"concept_id":cfg.get("concept_id"),
      "evidence_class":"SOURCE_EXPLICIT","classification_basis":basis,"evidence_refs":refs,
      "supporting_assertion_ids":supporting,"assertion_provenance_status":provenance,
      "confidence":cfg.get("confidence","high"),"review_status":"reviewed","reviewer_type":"assistant_assisted",
      "historical_identity_status":hist,"note":note,
    }

def audit_codes(root: Path, rid: str):
    with (root/AUDIT).open(encoding="utf-8",newline="") as f:
        for row in csv.DictReader(f,delimiter="\t"):
            if row["record_id"]==rid: return row["qualifying_dimension_codes"].split()
    raise ValueError(f"no audit row {rid}")

def materialize(root: Path, spec_path: Path):
    spec=json.loads(spec_path.read_text(encoding="utf-8"))
    outdir=root/"research/production/purananuru/records"; outdir.mkdir(parents=True,exist_ok=True)
    for rid,cfg in sorted(spec["records"].items()):
        n=int(rid)
        src=root/f"corpus/purananuru/poems/{rid}.md"
        r0p=root/f"research/evidence/purananuru/records/{rid}.ndjson"
        front, lines, source_note=parse_record(src)
        r0=load_r0(r0p); first=r0[0]
        if sha256_bytes(src)!=first["canonical_record_sha256"]: raise ValueError(f"{rid}: canonical hash drift")
        if source_note!=next(a["source_text"] for a in r0 if a.get("source_field")=="source_note"): raise ValueError(f"{rid}: source note mismatch")
        observations=[]
        refs=[{"source_field":"work","source_location":"yaml:work","evidence_span":None,"source_text":front["work"]}]
        observations.append({
          "observation_id":observation_id(rid,"literary_domain","work_level_classification",refs),
          "dimension":"literary_domain","concept_id":"literary.domain.puram","evidence_class":"SOURCE_EXPLICIT",
          "classification_basis":"work_level_classification","evidence_refs":refs,"supporting_assertion_ids":[],
          "assertion_provenance_status":"direct_r15_source_review_no_prior_assertion","confidence":"high",
          "review_status":"reviewed","reviewer_type":"assistant_assisted","historical_identity_status":"not_applicable",
          "note":"Work-level Puram classification; not a poem-body claim."
        })
        for field,typ in (("thinai_as_printed","TINI_VALUE"),("thurai","TURAI_VALUE")):
            val=front.get(field)
            if val is not None:
                refs=[evidence_ref(["yaml",field],front,lines,source_note)]
                aid=find_assertion(r0,typ,field=field,text=val)
                observations.append(mkobs(rid,"tinai_turai",refs,{"metadata_basis":True},[aid]))
        for dimension,dcfg in cfg["dimensions"].items():
            refs=[evidence_ref(x,front,lines,source_note) for x in dcfg["e"]]
            supporting=[]
            if "r0" in dcfg:
                m=dcfg["r0"]
                supporting=[find_assertion(r0,m["type"],m.get("field"),m.get("text"))]
            observations.append(mkobs(rid,dimension,refs,dcfg,supporting))
        refs=[]; supporting=[]
        if front.get("poet_as_printed") is not None:
            refs.append(evidence_ref(["yaml","poet_as_printed"],front,lines,source_note))
            supporting.append(find_assertion(r0,"POET_ATTRIBUTION","poet_as_printed",front["poet_as_printed"]))
        if front.get("addressee_as_printed") is not None:
            refs.append(evidence_ref(["yaml","addressee_as_printed"],front,lines,source_note))
            supporting.append(find_assertion(r0,"PATRON_OR_ADDRESSEE","addressee_as_printed",front["addressee_as_printed"]))
        if cfg.get("named_source_note"):
            refs.append(evidence_ref(["source_note"],front,lines,source_note))
            supporting.append(find_assertion(r0,"SOURCE_CONTEXT_NOTE","source_note",source_note))
        if refs:
            observations.append(mkobs(rid,"named_entities",refs,{"metadata_basis":True,"historical_identity_status":"unresolved",
                "note":cfg.get("named_note","Printed identity retained; no external historical resolution.")},supporting))
        bydim={d:[] for _,d in CANONICAL}
        for o in observations: bydim[o["dimension"]].append(o["observation_id"])
        reviews=[]
        empty_notes=cfg.get("empty_notes",{})
        for ordinal,(_,dim) in enumerate(CANONICAL,1):
            q=bool(bydim[dim])
            reviews.append({"ordinal":ordinal,"dimension":dim,
              "status":"qualifying_evidence_recorded" if q else "no_qualifying_evidence_identified",
              "observation_ids":bydim[dim],
              "review_note":"Qualifying source evidence recorded." if q else empty_notes.get(dim,"No qualifying evidence identified.")})
        fresh=[code for code,dim in CANONICAL if bydim[dim]]
        old=audit_codes(root,rid)
        discrepancies=[]
        added=[x for x in fresh if x not in old]; removed=[x for x in old if x not in fresh]
        if added: discrepancies.append("Fresh review adds: "+" ".join(added)+".")
        if removed: discrepancies.append("Fresh review omits control-only: "+" ".join(removed)+".")
        rec={
          "schema_version":"0.3.0","phase":"R1.5","production_review_id":f"purananuru-r15-production-{rid}",
          "work_id":"purananuru","record_id":rid,"record_number":n,"review_sequence_number":n,
          "source_snapshot":{"canonical_record_path":f"corpus/purananuru/poems/{rid}.md",
            "canonical_record_git_blob_sha":git_blob(src,root),"canonical_record_sha256":first["canonical_record_sha256"],
            "canonical_body_sha256":first["canonical_body_sha256"],"source_note_sha256":first["source_note_sha256"],
            "r0_assertion_record_path":f"research/evidence/purananuru/records/{rid}.ndjson",
            "r0_assertion_record_git_blob_sha":git_blob(r0p,root),"textual_status":str(front["textual_status"]),
            "canonical_text_available":bool(front["canonical_text_available"]),"lacuna_present":bool(front["lacuna_present"])},
          "source_metadata_reviewed":{"title_as_printed":front.get("title_as_printed"),"poet_as_printed":front.get("poet_as_printed"),
            "addressee_as_printed":front.get("addressee_as_printed"),"thinai_as_printed":front.get("thinai_as_printed"),
            "thurai_as_printed":front.get("thurai")},
          "dimensions_considered":29,"dimension_reviews":reviews,"observations":observations,
          "review_status":"reviewed","reviewer_type":"assistant_assisted","empty_cell_semantics":EMPTY,
          "audit_control":{"path":AUDIT,"prior_qualifying_dimension_codes":old,"checked_after_fresh_source_review":True,
            "comparison_status":"exact_match" if fresh==old else "review_differs_from_audit","discrepancies":discrepancies},
          "next_record_allowed":f"{n+1:03d}" if n<400 else None
        }
        (outdir/f"{rid}.json").write_text(json.dumps(rec,ensure_ascii=False,separators=(",",":"))+"\n",encoding="utf-8")
        print(f"{rid}: {len(observations)} observations; {' '.join(fresh)}")

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--root",default=".")
    ap.add_argument("--spec",required=True)
    a=ap.parse_args()
    root=Path(a.root).resolve()
    materialize(root,(root/a.spec).resolve())

if __name__=="__main__": main()
