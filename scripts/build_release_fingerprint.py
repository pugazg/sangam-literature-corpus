#!/usr/bin/env python3
"""Create the deterministic Classical Tamil Corpus 1.0.0 fingerprint."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "manifests/repository-content-hashes-1.0.0.sha256"
RELEASE = ROOT / "manifests/classical-tamil-corpus-release-1.0.0.json"

INCLUDED_ROOTS = ("apparatus", "corpus", "docs", "issues", "manifests", "scripts", "sources", "tests")
INCLUDED_ROOT_FILES = (".gitignore", "README.md", "requirements.txt")
EXCLUDED_NAMES = {OUTPUT.name}
EXCLUDED_SUFFIXES = (".lock", ".tmp", ".pyc", ".bak")


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def canonical_release_manifest() -> bytes:
    value = json.loads(RELEASE.read_text(encoding="utf-8"))
    for key in (
        "repository_content_manifest_sha256", "release_content_commit",
        "release_content_tree", "release_checkpoint_commit", "release_checkpoint_tree",
    ):
        value[key] = None
    return (json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")) + "\n").encode("utf-8")


def included(path: Path) -> bool:
    rel = path.relative_to(ROOT)
    if rel.parts[0] not in INCLUDED_ROOTS or path.name in EXCLUDED_NAMES:
        return False
    if any(part in {".git", "__pycache__", ".pytest_cache"} for part in rel.parts):
        return False
    if path.name.startswith(".") or path.name.endswith(EXCLUDED_SUFFIXES):
        return False
    if rel.parts[0] == "manifests" and path.name.endswith("-validation-report.json"):
        return False
    return True


def main() -> None:
    lines = []
    paths = [p for root in INCLUDED_ROOTS for p in (ROOT / root).rglob("*") if p.is_file() and included(p)]
    paths.extend(ROOT / name for name in INCLUDED_ROOT_FILES)
    for path in sorted(paths, key=lambda p: p.relative_to(ROOT).as_posix()):
        rel = path.relative_to(ROOT).as_posix()
        if path == RELEASE:
            lines.append(f"{digest(canonical_release_manifest())}  {rel} [canonical projection; self-referential and commit fields null]")
        else:
            lines.append(f"{digest(path.read_bytes())}  {rel}")
    OUTPUT.write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")
    manifest_sha = digest(OUTPUT.read_bytes())
    release = json.loads(RELEASE.read_text(encoding="utf-8"))
    release["repository_content_manifest_sha256"] = manifest_sha
    RELEASE.write_text(json.dumps(release, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
    print(json.dumps({"entries": len(lines), "repository_content_manifest_sha256": manifest_sha}, indent=2))


if __name__ == "__main__":
    main()
