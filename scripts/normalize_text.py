#!/usr/bin/env python3
from __future__ import annotations
import argparse, json, unicodedata
from corpuslib import paths, write_json

def normalize(work: str, force=False, dry_run=False, verbose=False):
    if work in {"tirukkural","naladiyar","nanmanikkadigai","inna-narpathu","iniyavai-narpathu","kar-narpathu","kalavazhi-narpathu","aintinai-aimpathu","aintinai-elupathu","thinaimalai-nutraimbathu","thinaimozhi-aimpathu","tirikatukam","acharakkovai","pazhamozhi-nanuru","sirupanchamulam","muthumozhi-kanchi","elati","kainnilai"}:
        from pathinenkilkanakku_pipeline import normalize as normalize_pathinen
        return normalize_pathinen(work, force=True, dry_run=dry_run, verbose=verbose)
    if work == "pattuppattu":
        from pattuppattu_pipeline import normalize as normalize_pattuppattu
        return normalize_pattuppattu(force=True, dry_run=dry_run, verbose=verbose)
    if work == "patirruppattu":
        from patirruppattu_pipeline import normalize as normalize_patirruppattu
        return normalize_patirruppattu(force=True, dry_run=dry_run, verbose=verbose)
    if work == "paripatal":
        from paripatal_pipeline import normalize as normalize_paripatal
        return normalize_paripatal(force=True, dry_run=dry_run, verbose=verbose)
    if work == "kalittokai":
        from kalittokai_pipeline import normalize as normalize_kalittokai
        return normalize_kalittokai(force=True, dry_run=dry_run, verbose=verbose)
    p=paths(work); data=json.loads(p["parsed"].read_text(encoding="utf-8"))
    for poem in data["poems"]:
        poem["lines"]=[unicodedata.normalize("NFC",x.replace("\r", "" ).strip()) for x in poem["lines"]]
        poem["source_note_lines"]=[unicodedata.normalize("NFC",x.replace("\r", "").strip()) for x in poem["source_note_lines"]]
    data["normalization"]="Unicode NFC; LF line endings; duplicate blank lines removed"
    if dry_run: print(f"Would normalize {len(data['poems'])} records"); return
    write_json(p["normalized"],data,force=force)
    if verbose: print("Applied conservative Unicode NFC normalization")

if __name__ == "__main__":
    ap=argparse.ArgumentParser(); ap.add_argument("--work",required=True); ap.add_argument("--force",action="store_true"); ap.add_argument("--dry-run",action="store_true"); ap.add_argument("--verbose",action="store_true")
    a=ap.parse_args(); normalize(a.work,a.force,a.dry_run,a.verbose)
