#!/usr/bin/env python3
"""Validate the bounded R1.5 Classical Tamil concept-matrix pilot."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

from generate_research_r15 import (
    CONCEPT_REGISTRY,
    MATRIX,
    OBSERVATIONS,
    PILOT_MAPPING,
    R15_SCHEMA_VERSION,
    REVIEWED_EXPORT,
    SUMMARY_JSON,
    build_matrix,
    build_observations,
    build_summary,
    observation_id,
)
from research_r1lib import load_ndjson

ASSERTION_SHA256 = "39f22d32948a112c65c712991023d33fcd171d5cd502cf767fdfd2fe91771b65"
DIMENSIONS_VOCAB = "research/controlled-vocabularies/concept-dimensions-r15.json"
BASES_VOCAB = "research/controlled-vocabularies/classification-bases-r15.json"
ASSERTIONS = "research/evidence/purananuru/assertions.ndjson"


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def validate(root: Path, write: bool = False, output: Path | None = None) -> dict:
    errors: list[str] = []
    warnings: list[str] = []

    registry = load_json(root / CONCEPT_REGISTRY)
    pilot = load_json(root / PILOT_MAPPING)
    dimensions_vocab = load_json(root / DIMENSIONS_VOCAB)
    bases_vocab = load_json(root / BASES_VOCAB)
    reviewed = load_ndjson(root / REVIEWED_EXPORT)
    committed_observations = load_ndjson(root / OBSERVATIONS)
    assertions = load_ndjson(root / ASSERTIONS)

    dimensions = {value["code"] for value in dimensions_vocab["entries"]}
    bases = {value["code"] for value in bases_vocab["entries"]}
    concepts = {value["concept_id"]: value for value in registry["concepts"]}
    assertion_ids = {value["assertion_id"] for value in assertions}
    reviewed_by_id = {value["assertion_id"]: value for value in reviewed}

    if registry.get("schema_version") != R15_SCHEMA_VERSION:
        errors.append("concept registry schema version is not 0.3.0")
    if dimensions_vocab.get("version") != R15_SCHEMA_VERSION:
        errors.append("concept-dimension vocabulary version is not 0.3.0")
    if bases_vocab.get("version") != R15_SCHEMA_VERSION:
        errors.append("classification-basis vocabulary version is not 0.3.0")
    if pilot.get("schema_version") != R15_SCHEMA_VERSION:
        errors.append("pilot mapping schema version is not 0.3.0")

    concept_ids = [value["concept_id"] for value in registry["concepts"]]
    if len(concept_ids) != len(set(concept_ids)):
        errors.append("duplicate concept IDs")
    for concept in registry["concepts"]:
        if concept["dimension"] not in dimensions:
            errors.append(f"unknown concept dimension: {concept['concept_id']}")
        parent = concept.get("parent_concept_id")
        if parent is not None and parent not in concepts:
            errors.append(f"missing parent concept: {concept['concept_id']} -> {parent}")

    required_foundation = {
        "literary.domain.akam",
        "literary.domain.puram",
        "literary.domain.uncertain",
        "literary.domain.not_applicable",
        "literary.tinai.kurinji",
        "literary.tinai.mullai",
        "literary.tinai.marutam",
        "literary.tinai.neytal",
        "literary.tinai.palai",
        "literary.tinai.kaikkilai",
        "literary.tinai.peruntinai",
    }
    missing_foundation = sorted(required_foundation - set(concepts))
    if missing_foundation:
        errors.append(f"missing required R1.5 foundation concepts: {missing_foundation}")

    basis = pilot.get("classification_basis")
    if basis not in bases:
        errors.append(f"unknown pilot classification basis: {basis}")

    mappings = pilot.get("mappings", [])
    mapping_assertions = [value["assertion_id"] for value in mappings]
    if len(mappings) != 8:
        errors.append(f"bounded pilot must contain exactly 8 mappings, found {len(mappings)}")
    if len(mapping_assertions) != len(set(mapping_assertions)):
        errors.append("duplicate assertion IDs in pilot mapping")
    for mapping in mappings:
        assertion_id_value = mapping["assertion_id"]
        if assertion_id_value not in assertion_ids:
            errors.append(f"pilot mapping assertion missing from R0 evidence: {assertion_id_value}")
        if assertion_id_value not in reviewed_by_id:
            errors.append(f"pilot mapping assertion missing from R1 reviewed export: {assertion_id_value}")
            continue
        reviewed_row = reviewed_by_id[assertion_id_value]
        if reviewed_row["assertion_type"] != mapping["expected_assertion_type"]:
            errors.append(f"assertion-type mismatch: {assertion_id_value}")
        if reviewed_row["printed_form"] != mapping["expected_printed_form"]:
            errors.append(f"printed-form mismatch: {assertion_id_value}")
        if mapping["concept_id"] not in concepts:
            errors.append(f"mapping references unknown concept: {mapping['concept_id']}")

    try:
        expected_observations = build_observations(root)
    except Exception as exc:
        errors.append(f"observation generation failed: {exc}")
        expected_observations = []

    if committed_observations != expected_observations:
        errors.append("committed R1.5 observations differ from deterministic generation")

    seen_observation_ids: set[str] = set()
    for value in committed_observations:
        oid = value["observation_id"]
        if oid in seen_observation_ids:
            errors.append(f"duplicate observation ID: {oid}")
        seen_observation_ids.add(oid)
        expected_id = observation_id(
            value["supporting_assertion_ids"][0],
            value["concept_id"],
            value["classification_basis"],
        )
        if oid != expected_id:
            errors.append(f"non-deterministic observation ID: {oid}")
        if value["concept_id"] not in concepts:
            errors.append(f"observation references unknown concept: {oid}")
        elif value["dimension"] != concepts[value["concept_id"]]["dimension"]:
            errors.append(f"observation dimension disagrees with registry: {oid}")
        if value["classification_basis"] not in bases:
            errors.append(f"unknown observation classification basis: {oid}")
        if value["dimension"] not in dimensions:
            errors.append(f"unknown observation dimension: {oid}")
        if value["evidence_class"] != "SOURCE_EXPLICIT":
            errors.append(f"pilot observation is not SOURCE_EXPLICIT: {oid}")
        if value["review_status"] != "reviewed":
            errors.append(f"pilot observation is not explicitly reviewed: {oid}")
        if value["reviewer_type"] != "assistant_assisted":
            errors.append(f"pilot reviewer provenance drift: {oid}")
        if value["confidence"] != "medium":
            errors.append(f"pilot confidence drift: {oid}")
        supports = value["supporting_assertion_ids"]
        if len(supports) != 1 or supports[0] not in assertion_ids:
            errors.append(f"invalid assertion provenance: {oid}")
        source = reviewed_by_id.get(supports[0])
        if source:
            for field, source_field in (
                ("work_id", "work_id"),
                ("record_id", "record_id"),
                ("surface_form", "printed_form"),
                ("source_assertion_type", "assertion_type"),
                ("evidence_span", "evidence_span"),
                ("source_field", "source_field"),
                ("source_location", "source_location"),
            ):
                if value[field] != source[source_field]:
                    errors.append(f"source provenance mismatch for {field}: {oid}")
        if value["historical_identity_status"] == "verified_external":
            errors.append(f"R1.5 pilot must not verify historical identity: {oid}")
        if value["concept_id"] == "polity.ruler":
            if value["historical_identity_status"] != "unresolved":
                errors.append(f"ruler observation identity must remain unresolved: {oid}")
        elif value["historical_identity_status"] != "not_applicable":
            errors.append(f"non-ruler pilot observation should not create identity state: {oid}")

    expected_matrix = build_matrix(expected_observations)
    if (root / MATRIX).read_text(encoding="utf-8") != expected_matrix:
        errors.append("committed R1.5 matrix differs from deterministic generation")

    expected_summary = build_summary(expected_observations)
    committed_summary = load_json(root / SUMMARY_JSON)
    if committed_summary != expected_summary:
        errors.append("committed R1.5 summary differs from deterministic generation")

    if sha(root / ASSERTIONS) != ASSERTION_SHA256:
        errors.append("R0 assertion file hash changed")
    if any(value["evidence_class"] == "EXTERNAL_HISTORICAL" for value in committed_observations):
        errors.append("R1.5 pilot contains external-historical observations")
    if any(value["evidence_class"] == "INTERPRETATION" for value in committed_observations):
        errors.append("R1.5 pilot contains interpretation observations")

    report = {
        "programme_id": "classical-tamil-research-layer",
        "phase": "R1.5",
        "concept_schema_version": R15_SCHEMA_VERSION,
        "evidence_schema_version": "0.1.0",
        "review_workflow_schema_version": "0.2.0",
        "concept_definitions_checked": len(concepts),
        "pilot_mappings_checked": len(mappings),
        "observations_checked": len(committed_observations),
        "matrix_rows_checked": max(0, len((root / MATRIX).read_text(encoding="utf-8").splitlines()) - 1),
        "r0_assertion_count_checked": len(assertions),
        "r0_assertion_sha256": sha(root / ASSERTIONS),
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
    parser.add_argument("--output", default="logs/classical-tamil-research-r15-validation-20260818T160000.json")
    args = parser.parse_args()
    root = Path(args.root).resolve()
    report = validate(root, write=True, output=root / args.output)
    print(json.dumps(report, ensure_ascii=False, indent=2))
    if report["status"] != "pass":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
