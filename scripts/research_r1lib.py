#!/usr/bin/env python3
"""Shared R1 review and entity-resolution primitives."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

from researchlib import canonical_json

R1_SCHEMA_VERSION = "0.2.0"
REVIEWER_TYPES = {"human_editor", "assistant_assisted", "automated_system"}
ENTITY_OPERATIONS = {"retain", "possible_match", "merge", "split", "reject", "supersede"}
IDENTITY_STATES = {
    "unresolved", "candidate_entity", "possible_match", "reviewed_match",
    "verified_match", "rejected_match", "split_required", "superseded",
}
ALLOWED_REVIEW_TRANSITIONS = {
    ("unreviewed", "machine_checked"),
    ("machine_checked", "human_review_required"),
    ("human_review_required", "reviewed"),
    ("reviewed", "verified"),
    ("reviewed", "rejected"),
    ("verified", "superseded"),
    ("rejected", "superseded"),
}
R0_REVIEW_SAMPLE = (
    set(range(1, 11))
    | set(range(95, 106))
    | set(range(175, 186))
    | set(range(240, 251))
    | set(range(263, 271))
    | set(range(390, 401))
)
R1_PILOT_RECORDS = set(range(1, 26)) | R0_REVIEW_SAMPLE


def load_ndjson(path: Path) -> list[dict]:
    if not path.exists():
        return []
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def ndjson(values: list[dict]) -> str:
    return "".join(json.dumps(value, ensure_ascii=False, sort_keys=True) + "\n" for value in values)


def stable_id(prefix: str, value: object, length: int = 24) -> str:
    digest = hashlib.sha256(canonical_json(value).encode("utf-8")).hexdigest()[:length]
    return f"{prefix}{digest}"


def event_hash(event: dict) -> str:
    payload = {key: value for key, value in event.items() if key != "event_hash"}
    return hashlib.sha256(canonical_json(payload).encode("utf-8")).hexdigest()


def decision_id(value: dict) -> str:
    payload = {key: item for key, item in value.items() if key != "decision_id"}
    return stable_id("entity-decision.r1.", payload)


def current_statuses(assertions: list[dict], events: list[dict]) -> dict[str, str]:
    statuses = {value["assertion_id"]: value["review_status"] for value in assertions}
    for event in sorted(events, key=lambda value: value["sequence"]):
        statuses[event["assertion_id"]] = event["new_status"]
    return statuses


def validate_event_chain(events: list[dict]) -> list[str]:
    errors: list[str] = []
    previous_hash = None
    expected_sequence = 1
    seen_ids: set[str] = set()
    for event in events:
        event_id = event.get("review_event_id")
        if event.get("sequence") != expected_sequence:
            errors.append(f"review sequence gap at {event_id}")
        expected_sequence += 1
        if event_id in seen_ids:
            errors.append(f"duplicate review event ID: {event_id}")
        seen_ids.add(event_id)
        if event.get("previous_event_hash") != previous_hash:
            errors.append(f"review history chain mismatch: {event_id}")
        computed = event_hash(event)
        if event.get("event_hash") != computed:
            errors.append(f"review event hash mismatch: {event_id}")
        previous_hash = event.get("event_hash")
    return errors


def validate_decision_semantics(value: dict) -> list[str]:
    """Validate operation shape without inferring historical identity."""
    errors: list[str] = []
    operation = value.get("operation")
    involved = value.get("involved_entity_ids") or []
    supports = value.get("supporting_assertion_ids") or []
    variants = value.get("variant_forms") or []
    result = value.get("result_entity_id")
    decision = value.get("decision_id", "<unidentified>")
    if not supports:
        errors.append(f"entity decision lacks assertion provenance: {decision}")
    if not variants:
        errors.append(f"entity decision lacks variant forms: {decision}")
    if operation in {"possible_match", "merge"} and len(involved) < 2:
        errors.append(f"{operation} requires at least two entities: {decision}")
    if operation == "retain" and len(involved) != 1:
        errors.append(f"retain requires exactly one entity: {decision}")
    if operation == "split" and len(involved) != 1:
        errors.append(f"split requires exactly one source entity: {decision}")
    if operation in {"reject", "supersede"} and not involved:
        errors.append(f"{operation} requires at least one entity: {decision}")
    if operation == "retain" and result not in {None, involved[0] if involved else None}:
        errors.append(f"retain result must be the retained entity or null: {decision}")
    if operation == "possible_match" and result is not None:
        errors.append(f"possible_match must not manufacture a merged result entity: {decision}")
    return errors


def validate_append_only_prefix(previous: list[dict], current: list[dict]) -> bool:
    return len(current) >= len(previous) and current[: len(previous)] == previous
