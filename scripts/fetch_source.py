#!/usr/bin/env python3
from __future__ import annotations
import argparse, ssl, urllib.request
import certifi
from pathlib import Path
from corpuslib import ensure_dirs, paths, sha256, today, write_json

def fetch(url: str, work: str, force: bool = False, dry_run: bool = False, verbose: bool = False):
    ensure_dirs(); p = paths(work); target = p["raw_html"]
    if target.exists() and not force:
        raise FileExistsError(f"Refusing to overwrite {target}; pass --force")
    if dry_run:
        print(f"Would fetch {url} -> {target}"); return
    req = urllib.request.Request(url, headers={"User-Agent": "sangam-text-corpus/0.1 source preservation"})
    context = ssl.create_default_context(cafile=certifi.where())
    with urllib.request.urlopen(req, timeout=60, context=context) as response:
        raw = response.read()
    target.parent.mkdir(parents=True, exist_ok=True); target.write_bytes(raw)
    meta = {"source_url": url, "accessed_date": today(), "project_madurai_id": Path(url).stem,
            "raw_source_file": str(target.relative_to(target.parents[2])), "source_checksum_sha256": sha256(target),
            "content_length_bytes": len(raw), "http_content_type": "text/html", "raw_source_modified": False}
    write_json(p["source_metadata"], meta, force=True)
    if verbose: print(f"Saved {len(raw)} bytes; SHA-256 {meta['source_checksum_sha256']}")

if __name__ == "__main__":
    ap=argparse.ArgumentParser(); ap.add_argument("--url",required=True); ap.add_argument("--work",required=True)
    ap.add_argument("--force",action="store_true"); ap.add_argument("--dry-run",action="store_true"); ap.add_argument("--verbose",action="store_true")
    a=ap.parse_args(); fetch(a.url,a.work,a.force,a.dry_run,a.verbose)
