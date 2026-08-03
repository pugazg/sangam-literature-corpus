#!/usr/bin/env python3
"""Shared deterministic primitives for the derived research layer."""
from __future__ import annotations

import contextlib
import fcntl
import hashlib
import json
import os
import re
import tempfile
import unicodedata
from pathlib import Path

import yaml

RESEARCH_SCHEMA_VERSION = "0.1.0"
PROGRAMME_ID = "classical-tamil-research-layer"


def sha_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha_file(path: Path) -> str:
    return sha_bytes(path.read_bytes())


def canonical_json(value: object) -> str:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


@contextlib.contextmanager
def advisory_lock(path: Path):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a+", encoding="utf-8") as handle:
        fcntl.flock(handle.fileno(), fcntl.LOCK_EX)
        try:
            yield
        finally:
            fcntl.flock(handle.fileno(), fcntl.LOCK_UN)


def atomic_write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, temporary = tempfile.mkstemp(prefix=f".{path.name}.", suffix=".tmp", dir=path.parent)
    try:
        with os.fdopen(fd, "w", encoding="utf-8", newline="\n") as handle:
            handle.write(text)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temporary, path)
    finally:
        if os.path.exists(temporary):
            os.unlink(temporary)


def write_json(path: Path, value: object) -> None:
    atomic_write(path, json.dumps(value, ensure_ascii=False, indent=2) + "\n")


def parse_poem(path: Path) -> dict:
    raw = path.read_text(encoding="utf-8")
    match = re.match(r"\A---\n(.*?)\n---\n(.*)\Z", raw, re.S)
    if not match:
        raise ValueError(f"malformed canonical record: {path}")
    front = yaml.safe_load(match.group(1)) or {}
    remainder = match.group(2)
    body_part, marker, note_part = remainder.partition("## Source note (as printed)")
    lines = body_part.splitlines()
    while lines and not lines[0].strip():
        lines.pop(0)
    heading = lines.pop(0) if lines and lines[0].startswith("# ") else ""
    while lines and not lines[0].strip():
        lines.pop(0)
    body = "\n".join(lines).strip("\n")
    note = note_part.strip("\n") if marker else ""
    return {
        "front": front,
        "heading": heading,
        "body": body,
        "body_lines": body.splitlines() if body else [],
        "source_note": note,
        "whole_sha256": sha_file(path),
        "body_sha256": sha_bytes(body.encode("utf-8")),
        "source_note_sha256": sha_bytes(note.encode("utf-8")),
    }


def normalize_lookup(value: str) -> str:
    value = unicodedata.normalize("NFC", value)
    value = re.sub(r"[^\w\u0B80-\u0BFF]+", " ", value, flags=re.UNICODE)
    return " ".join(value.split())


def assertion_id(assertion: dict) -> str:
    span = assertion.get("evidence_span") or {}
    basis = {
        "work_id": assertion["work_id"],
        "record_id": assertion["record_id"],
        "assertion_type": assertion["assertion_type"],
        "predicate": assertion["predicate"],
        "start_line": span.get("start_line"),
        "end_line": span.get("end_line"),
        "start_character": span.get("start_character"),
        "end_character": span.get("end_character"),
        "printed_form": assertion["normalization"]["printed_form"],
    }
    return "asrt." + sha_bytes(canonical_json(basis).encode("utf-8"))[:24]


def relationship_id(value: dict) -> str:
    basis = {key: value[key] for key in ("subject_id", "predicate", "object_id", "supporting_assertion_ids")}
    return "rel." + sha_bytes(canonical_json(basis).encode("utf-8"))[:24]
