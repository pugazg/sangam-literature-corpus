#!/usr/bin/env python3
"""Validate the sequential Puṟanāṉūṟu R1.5 29-dimension production ledger."""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
from pathlib import Path

from researchlib import parse_poem, sha_file
from validate_r15_production_dimensions import CANONICAL_DIMENSIONS, CANONICAL_IDS

RECORD_DIR = "research/production/purananuru/records"
CONCEPT_REGISTRY = "research/concepts/classical-tamil/concept-registry-r15.json"
CLASSIFICATION_BASES = "research/controlled-vocabularies/classification-bases-r15.json"
EMPTY_SEMANTICS = "No qualifying evidence identified in this reviewed source record; never evidence of historical absence."

DIMENSION_TO_AUDIT_CODE = {dimension_id: audit_code for _, audit_code, dimension_id, _ in CANONICAL_DIMENSIONS}
EXPECTED_DIMENSION_ROWS = [(ordinal, dimension_id) for ordinal, _, dimension_id, _ in CANONICAL_DIMENSIONS]


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def load_ndjson(path: Path) -> list[dict]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def production_observation_id(record_id: str, dimension: str, classification_basis: str, evidence_refs: list[dict]) -> str:
    payload = {
        "record_id": record_id,
        "dimension": dimension,
        "classification_basis": classification_basis,
        "evidence_refs": evidence_refs,
    }
    raw = json.dumps(payload, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return "obs.prod.r15." + hashlib.sha256(raw).hexdigest()[:24]


def body_slice(lines: list[str], span: dict) -> str | None:
    start_line = span.get("start_line")
    end_line = span.get("end_line")
    start_character = span.get("start_character")
    end_character = span.get("end_character")
    if not all(isinstance(value, int) for value in (start_line, end_line, start_character, end_character)):
        return None
    if start_line < 1 or end_line < start_line or end_line > len(lines):
        return None
    first = lines[start_line - 1]
    last = lines[end_line - 1]
    if start_character < 0 or start_character > len(first) or end_character < 0 or end_character > len(last):
        return None
    if start_line == end_line:
        if end_character < start_character:
            return None
        return first[start_character:end_character]
    pieces = [first[start_character:]]
    pieces.extend(lines[start_line:end_line - 1])
    pieces.append(last[:end_character])
    return "\n".join(pieces)


def audit_codes(root: Path, path_text: str, record_id: str) -> list[str] | None:
    path = root / path_text
    if not path.is_file():
        return None
    with path.open(encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle, delimiter="\t")
        for row in reader:
            if row.get("record_id") == record_id:
                return (row.get("qualifying_dimension_codes") or "").split()
    return None


def validate_record(root: Path, path: Path, expected_number: int, concepts: dict[str, dict], bases: set[str]) -> tuple[list[str], int]:
    errors: list[str] = []
    observation_count = 0
    value = load_json(path)
    record_id = f"{expected_number:03d}"
    prefix = f"{path.as_posix()}:"

    def error(message: str) -> None:
        errors.append(f"{prefix} {message}")

    if path.stem != record_id:
        error(f"filename must match sequential record {record_id}")
    if value.get("schema_version") != "0.3.0" or value.get("phase") != "R1.5" or value.get("work_id") != "purananuru":
        error("schema_version/phase/work_id contract mismatch")
    if value.get("record_id") != record_id or value.get("record_number") != expected_number or value.get("review_sequence_number") != expected_number:
        error("record identity or review sequence does not match filename/prefix position")
    if value.get("production_review_id") != f"purananuru-r15-production-{record_id}":
        error("production_review_id is not deterministic")
    if value.get("dimensions_considered") != 29:
        error("dimensions_considered must be exactly 29")
    if value.get("review_status") != "reviewed":
        error("record must be durably reviewed before the next record is allowed")
    if value.get("empty_cell_semantics") != EMPTY_SEMANTICS:
        error("empty-cell semantics changed")

    expected_next = f"{expected_number + 1:03d}" if expected_number < 400 else None
    if value.get("next_record_allowed") != expected_next:
        error(f"next_record_allowed must be {expected_next!r}")

    source = value.get("source_snapshot", {})
    expected_source_path = f"corpus/purananuru/poems/{record_id}.md"
    if source.get("canonical_record_path") != expected_source_path:
        error(f"canonical_record_path must be {expected_source_path}")
        parsed = None
    else:
        canonical_path = root / expected_source_path
        if not canonical_path.is_file():
            error("canonical source record is missing")
            parsed = None
        else:
            parsed = parse_poem(canonical_path)
            if sha_file(canonical_path) != source.get("canonical_record_sha256"):
                error("canonical_record_sha256 does not match frozen source bytes")
            if parsed.get("body_sha256") != source.get("canonical_body_sha256"):
                error("canonical_body_sha256 does not match frozen source body")
            if parsed.get("source_note_sha256") != source.get("source_note_sha256"):
                error("source_note_sha256 does not match frozen source note")
            front = parsed.get("front", {})
            if source.get("textual_status") != str(front.get("textual_status")):
                error("textual_status does not match frozen source metadata")
            if source.get("canonical_text_available") != bool(front.get("canonical_text_available")):
                error("canonical_text_available does not match frozen source metadata")
            if source.get("lacuna_present") != bool(front.get("lacuna_present")):
                error("lacuna_present does not match frozen source metadata")

            reviewed_metadata = value.get("source_metadata_reviewed", {})
            expected_metadata = {
                "title_as_printed": front.get("title_as_printed"),
                "poet_as_printed": front.get("poet_as_printed"),
                "addressee_as_printed": front.get("addressee_as_printed"),
                "thinai_as_printed": front.get("thinai_as_printed"),
                "thurai_as_printed": front.get("thurai"),
            }
            if reviewed_metadata != expected_metadata:
                error("source_metadata_reviewed is not an exact frozen-field copy")

    assertion_path_text = source.get("r0_assertion_record_path")
    expected_assertion_path = f"research/evidence/purananuru/records/{record_id}.ndjson"
    assertion_ids: set[str] = set()
    if assertion_path_text != expected_assertion_path:
        error(f"r0_assertion_record_path must be {expected_assertion_path}")
    else:
        assertion_path = root / expected_assertion_path
        if not assertion_path.is_file():
            error("R0 assertion record is missing")
        else:
            assertions = load_ndjson(assertion_path)
            assertion_ids = {entry.get("assertion_id") for entry in assertions}
            if any(entry.get("canonical_record_sha256") != source.get("canonical_record_sha256") for entry in assertions):
                error("R0 assertions and production source snapshot disagree on canonical record hash")

    reviews = value.get("dimension_reviews", [])
    actual_dimension_rows = [(entry.get("ordinal"), entry.get("dimension")) for entry in reviews]
    if actual_dimension_rows != EXPECTED_DIMENSION_ROWS:
        error("dimension_reviews must contain the exact ordered 29-dimension registry")

    observations = value.get("observations", [])
    observation_count = len(observations)
    observation_by_id: dict[str, dict] = {}
    for observation in observations:
        observation_id = observation.get("observation_id")
        if observation_id in observation_by_id:
            error(f"duplicate production observation_id {observation_id}")
            continue
        observation_by_id[observation_id] = observation
        dimension = observation.get("dimension")
        if dimension not in set(CANONICAL_IDS):
            error(f"observation {observation_id} uses non-canonical dimension {dimension}")
        basis = observation.get("classification_basis")
        if basis not in bases:
            error(f"observation {observation_id} uses unknown classification basis {basis}")
        expected_id = production_observation_id(record_id, dimension, basis, observation.get("evidence_refs", []))
        if observation_id != expected_id:
            error(f"observation {observation_id} is not deterministically derived from record/dimension/basis/evidence")

        concept_id = observation.get("concept_id")
        if concept_id is not None:
            concept = concepts.get(concept_id)
            if concept is None:
                error(f"observation {observation_id} references unknown concept {concept_id}")
            elif concept.get("dimension") != dimension:
                error(f"observation {observation_id} concept/dimension mismatch")

        supporting = observation.get("supporting_assertion_ids", [])
        unknown_assertions = sorted(set(supporting) - assertion_ids)
        if unknown_assertions:
            error(f"observation {observation_id} invents or mislinks R0 assertion IDs: {unknown_assertions}")
        provenance = observation.get("assertion_provenance_status")
        if provenance == "direct_r15_source_review_no_prior_assertion" and supporting:
            error(f"observation {observation_id} claims no prior assertion but links one")
        if provenance in {"existing_r0_assertion_linked", "mixed_existing_r0_and_direct_r15_source_review"} and not supporting:
            error(f"observation {observation_id} claims R0 linkage without an assertion ID")

        refs = observation.get("evidence_refs", [])
        if not refs:
            error(f"observation {observation_id} has no source evidence refs")
        for ref in refs:
            if parsed is None:
                continue
            source_location = ref.get("source_location")
            source_field = ref.get("source_field")
            span = ref.get("evidence_span")
            source_text = ref.get("source_text")
            if source_location == "markdown:canonical-body":
                if span is None:
                    error(f"observation {observation_id} canonical-body evidence is missing its span")
                    continue
                expected_text = body_slice(parsed.get("body_lines", []), span)
                if expected_text is None or source_text != expected_text:
                    error(f"observation {observation_id} canonical-body source_text/span mismatch")
            elif source_location == "markdown:source-note":
                if span is not None or source_text != parsed.get("source_note"):
                    error(f"observation {observation_id} source-note evidence mismatch")
            elif isinstance(source_location, str) and source_location.startswith("yaml:"):
                if span is not None:
                    error(f"observation {observation_id} YAML evidence must not use a body span")
                if source_text != parsed.get("front", {}).get(source_field):
                    error(f"observation {observation_id} YAML source_text does not match {source_field}")
            else:
                error(f"observation {observation_id} has unsupported source_location {source_location}")

    referenced_observation_ids: set[str] = set()
    qualifying_dimensions: list[str] = []
    for review in reviews:
        ids = review.get("observation_ids", [])
        dimension = review.get("dimension")
        status = review.get("status")
        if status == "qualifying_evidence_recorded":
            qualifying_dimensions.append(dimension)
            if not ids:
                error(f"dimension {dimension} is qualifying but has no observation")
        elif status == "no_qualifying_evidence_identified" and ids:
            error(f"dimension {dimension} is reviewed-empty but references observations")
        for observation_id in ids:
            referenced_observation_ids.add(observation_id)
            observation = observation_by_id.get(observation_id)
            if observation is None:
                error(f"dimension {dimension} references missing observation {observation_id}")
            elif observation.get("dimension") != dimension:
                error(f"dimension {dimension} references observation from {observation.get('dimension')}")
    unreferenced = sorted(set(observation_by_id) - referenced_observation_ids)
    if unreferenced:
        error(f"production observations are not referenced by dimension_reviews: {unreferenced}")

    control = value.get("audit_control", {})
    prior_codes = audit_codes(root, control.get("path", ""), record_id)
    if prior_codes is None:
        error("audit control row could not be loaded")
    else:
        if control.get("prior_qualifying_dimension_codes") != prior_codes:
            error("audit_control prior codes are not an exact copy of the old audit row")
        fresh_codes = [DIMENSION_TO_AUDIT_CODE[dimension] for dimension in qualifying_dimensions]
        if fresh_codes == prior_codes:
            if control.get("comparison_status") != "exact_match" or control.get("discrepancies") != []:
                error("audit comparison is an exact match but is not recorded as such")
        else:
            if control.get("comparison_status") != "review_differs_from_audit" or not control.get("discrepancies"):
                error("fresh review differs from audit; discrepancies must be recorded explicitly")
    if control.get("checked_after_fresh_source_review") is not True:
        error("old audit must be checked only as a post-review control")

    return errors, observation_count


def validate(root: Path, write: bool = False, output: Path | None = None) -> dict:
    errors: list[str] = []
    warnings: list[str] = []
    record_dir = root / RECORD_DIR
    record_paths = sorted(record_dir.glob("[0-9][0-9][0-9].json")) if record_dir.is_dir() else []
    numbers = [int(path.stem) for path in record_paths]
    if not numbers:
        errors.append("no Puṟanāṉūṟu production records are present")
    else:
        expected = list(range(1, max(numbers) + 1))
        if numbers != expected:
            errors.append(f"production records must form a gap-free sequential prefix from 001; found {numbers}")

    registry = load_json(root / CONCEPT_REGISTRY)
    concepts = {entry["concept_id"]: entry for entry in registry.get("concepts", [])}
    basis_vocab = load_json(root / CLASSIFICATION_BASES)
    bases = {entry["code"] for entry in basis_vocab.get("entries", [])}
    if "direct_record_review" not in bases:
        errors.append("classification vocabulary must include direct_record_review for full semantic production work")

    observation_total = 0
    for expected_number, path in enumerate(record_paths, 1):
        current_errors, current_observations = validate_record(root, path, expected_number, concepts, bases)
        errors.extend(current_errors)
        observation_total += current_observations

    reviewed = max(numbers) if numbers else 0
    report = {
        "programme_id": "classical-tamil-research-layer",
        "phase": "R1.5",
        "gate": "purananuru-29-dimension-production-prefix",
        "canonical_dimension_count": len(CANONICAL_IDS),
        "records_reviewed": reviewed,
        "records_remaining": 400 - reviewed,
        "next_record": f"{reviewed + 1:03d}" if 0 < reviewed < 400 else None,
        "production_observations_checked": observation_total,
        "errors": errors,
        "warnings": warnings,
        "status": "pass" if not errors else "fail",
    }
    if write:
        if output is None:
            raise ValueError("output is required when write=True")
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return report


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default=".")
    parser.add_argument("--output", default="logs/classical-tamil-r15-purananuru-production-validation.json")
    args = parser.parse_args()
    root = Path(args.root).resolve()
    report = validate(root, write=True, output=root / args.output)
    print(json.dumps(report, ensure_ascii=False, indent=2))
    if report["status"] != "pass":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
