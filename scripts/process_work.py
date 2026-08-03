#!/usr/bin/env python3
from __future__ import annotations
import argparse
from fetch_source import fetch
from extract_text import extract
from normalize_text import normalize
from split_poems import split
from build_manifest import build
from validate_output import validate

def process(work, url=None, force=False, dry_run=False, verbose=False):
    if work == "tolkappiyam":
        if url:
            raise ValueError("Tolkāppiyam regeneration uses only the pinned preserved local source")
        if dry_run:
            print("Would regenerate 1,602 Tolkāppiyam nurpa records from pinned pmuni0100")
            return
        from tolkappiyam_pipeline import process as process_tolkappiyam
        return process_tolkappiyam()
    if url:
        fetch(url,work,force,dry_run,verbose)
        if dry_run: return
    elif dry_run:
        print(f"Would regenerate derived outputs for {work} from preserved raw HTML")
        return
    # Existing-source regeneration intentionally replaces derived artifacts but
    # never rewrites the preserved raw HTML.
    derived_force = True if not url else force
    extract(work,derived_force,False,verbose)
    normalize(work,derived_force,False,verbose)
    split(work,derived_force,False,verbose)
    build(work,derived_force,False,verbose)
    validate(work,derived_force,False,verbose)

if __name__ == "__main__":
    ap=argparse.ArgumentParser(description="Process one supported Project Madurai work")
    supported=["natrinai","aingurunuru","kuruntokai","akananuru","purananuru","pattuppattu","patirruppattu","paripatal","kalittokai","tirukkural","naladiyar","nanmanikkadigai","inna-narpathu","iniyavai-narpathu","kar-narpathu","kalavazhi-narpathu","aintinai-aimpathu","aintinai-elupathu","thinaimalai-nutraimbathu","thinaimozhi-aimpathu","tirikatukam","acharakkovai","pazhamozhi-nanuru","sirupanchamulam","muthumozhi-kanchi","elati","kainnilai","tolkappiyam"]
    ap.add_argument("work_pos",nargs="?",choices=supported,help="Regenerate from preserved raw HTML")
    ap.add_argument("--url"); ap.add_argument("--work",dest="work_opt",choices=supported)
    ap.add_argument("--force",action="store_true"); ap.add_argument("--dry-run",action="store_true"); ap.add_argument("--verbose",action="store_true")
    a=ap.parse_args(); work=a.work_opt or a.work_pos
    if not work: ap.error("provide positional WORK or --work WORK")
    if a.url and not a.work_opt: ap.error("--url requires --work")
    process(work,a.url,a.force,a.dry_run,a.verbose)
