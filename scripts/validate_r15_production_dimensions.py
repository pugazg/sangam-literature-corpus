#!/usr/bin/env python3
"""Validate the exact 29-dimension R1.5 production matrix surface.

This gate is intentionally independent of the exhaustive-audit validator. It
hard-codes the approved production dimension IDs so the audit registry,
production vocabulary, schemas, concept registry, policies, observations and
matrix cannot be collapsed together without a test failure.
"""
from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path

CANONICAL_DIMENSIONS = (
    (1, "LD", "literary_domain", "Literary domain: Akam/Puram"),
    (2, "TT", "tinai_turai", "tiṇai / tuṟai"),
    (3, "ENV", "landscape_environment", "Landscape/environment"),
    (4, "SWT", "season_weather_time", "Season/weather/time"),
    (5, "FL", "flora", "Flora"),
    (6, "FA", "fauna", "Fauna"),
    (7, "PSR", "people_social_roles", "People and social roles"),
    (8, "REL", "relationships", "Relationships"),
    (9, "ELE", "emotion_lived_experience", "Emotion/lived experience"),
    (10, "OP", "occupations_production", "Occupations and production"),
    (11, "FS", "food_subsistence", "Food and subsistence"),
    (12, "COA", "clothing_ornaments_adornment", "Clothing, ornaments, adornment"),
    (13, "MC", "material_culture_everyday_objects", "Material culture and everyday objects"),
    (14, "WW", "weapons_warfare", "Weapons and warfare"),
    (15, "MT", "mobility_transport", "Mobility and transport"),
    (16, "SBE", "settlements_built_environment", "Settlements and built environment"),
    (17, "ECO", "economy", "Economy"),
    (18, "TRD", "trade_exchange", "Trade and exchange"),
    (19, "POL", "polity_political_life", "Polity and political life"),
    (20, "CSG", "communities_social_groups", "Communities/social groups"),
    (21, "FGK", "family_gender_kinship", "Family/gender/kinship"),
    (22, "RR", "religion_ritual", "Religion/ritual"),
    (23, "DMM", "death_mourning_memory", "Death/mourning/memory"),
    (24, "AMP", "arts_music_performance", "Arts/music/performance"),
    (25, "KT", "knowledge_technology", "Knowledge/technology"),
    (26, "VEC", "values_ethical_concepts", "Values/ethical concepts"),
    (27, "BH", "body_health", "Body/health"),
    (28, "NE", "named_entities", "Named entities"),
    (29, "TIR", "textual_intertextual_relationships", "Textual/intertextual relationships"),
)

CANONICAL_IDS = tuple(value[2] for value in CANONICAL_DIMENSIONS)
CANONICAL_ID_SET = set(CANONICAL_IDS)
LEGACY_DIMENSIONS = {
    "tinai",
    "turai",
    "season_time",
    "occupation_labour",
    "economy_trade",
    "settlement_habitation",
    "family_kinship",
    "society_social_group",
    "polity_power",
    "warfare",
    "ritual_religion",
    "arts_performance",
    "body_adornment_clothing",
    "material_culture",
    "values_emotions",
    "named_entity",
}

LIVED_LIFE_DIMENSIONS = tuple(
    value
    for value in CANONICAL_IDS
    if value
    not in {
        "literary_domain",
        "tinai_turai",
        "landscape_environment",
        "named_entities",
        "textual_intertextual_relationships",
    }
)

AUDIT_REGISTRY = "research/audits/r15-premerge/dimensions.json"
PRODUCTION_VOCAB = "research/controlled-vocabularies/concept-dimensions-r15.json"
POLICIES = "research/controlled-vocabularies/concept-evidence-policies-r15.json"
CONCEPT_REGISTRY = "research/concepts/classical-tamil/concept-registry-r15.json"
CONCEPT_DEFINITION_SCHEMA = "research/schemas/concept-definition-r15.schema.json"
CONCEPT_OBSERVATION_SCHEMA = "research/schemas/concept-observation-r15.schema.json"
TOLKAPPIYAM_SCHEMA = "research/schemas/tolkappiyam-concept-evidence-r15.schema.json"
PILOT_OBSERVATIONS = "research/observations/purananuru/r15-pilot.ndjson"
PILOT_MATRIX = "research/matrices/purananuru/r15-pilot-matrix.csv"


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def load_ndjson(path: Path) -> list[dict]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def validate(root: Path, write: bool = False, output: Path | None = None) -> dict:
    errors: list[str] = []
    warnings: list[str] = []

    audit = load_json(root / AUDIT_REGISTRY)
    vocab = load_json(root / PRODUCTION_VOCAB)
    policies = load_json(root / POLICIES)
    registry = load_json(root / CONCEPT_REGISTRY)
    concept_schema = load_json(root / CONCEPT_DEFINITION_SCHEMA)
    observation_schema = load_json(root / CONCEPT_OBSERVATION_SCHEMA)
    tolk_schema = load_json(root / TOLKAPPIYAM_SCHEMA)
    observations = load_ndjson(root / PILOT_OBSERVATIONS)

    expected_audit = [
        {"ordinal": ordinal, "code": audit_code, "id": dimension_id, "label": label}
        for ordinal, audit_code, dimension_id, label in CANONICAL_DIMENSIONS
    ]
    if audit.get("dimension_count") != 29:
        errors.append("audit registry dimension_count must remain exactly 29")
    if audit.get("dimensions") != expected_audit:
        errors.append("audit registry no longer matches the approved exact 29-dimension surface")

    entries = vocab.get("entries", [])
    if vocab.get("version") != "0.3.0":
        errors.append("production dimension vocabulary version must remain 0.3.0 during R1.5")
    if len(entries) != 29:
        errors.append(f"production dimension vocabulary must contain exactly 29 entries, found {len(entries)}")
    expected_vocab = [
        {"ordinal": ordinal, "code": dimension_id, "audit_code": audit_code, "label": label}
        for ordinal, audit_code, dimension_id, label in CANONICAL_DIMENSIONS
    ]
    if entries != expected_vocab:
        errors.append("production dimension vocabulary is not an exact ordered projection of the 29-dimension registry")

    for schema_name, schema in (
        ("concept definition", concept_schema),
        ("concept observation", observation_schema),
    ):
        enum = schema.get("properties", {}).get("dimension", {}).get("enum")
        if enum != list(CANONICAL_IDS):
            errors.append(f"{schema_name} schema dimension enum must be the exact ordered 29-dimension list")

    tolk_required = set(tolk_schema.get("required", []))
    if "dimension" not in tolk_required:
        errors.append("Tolkāppiyam concept-evidence schema must require an explicit dimension")
    tolk_enum = tolk_schema.get("properties", {}).get("dimension", {}).get("enum")
    if tolk_enum != list(CANONICAL_IDS):
        errors.append("Tolkāppiyam concept-evidence schema must expose the exact 29-dimension enum")

    concepts = {value["concept_id"]: value for value in registry.get("concepts", [])}
    concept_dimensions = {value.get("dimension") for value in concepts.values()}
    unknown_concept_dimensions = sorted(value for value in concept_dimensions if value not in CANONICAL_ID_SET)
    if unknown_concept_dimensions:
        errors.append(f"concept registry contains non-canonical dimensions: {unknown_concept_dimensions}")
    legacy_concept_dimensions = sorted(concept_dimensions & LEGACY_DIMENSIONS)
    if legacy_concept_dimensions:
        errors.append(f"concept registry still contains legacy coarse dimensions: {legacy_concept_dimensions}")

    expected_concept_dimensions = {
        "literary.tinai": "tinai_turai",
        "literary.turai": "tinai_turai",
        "entity.named": "named_entities",
        "economy.commodity.gold": "economy",
        "warfare.weapon.sword": "weapons_warfare",
        "society.community.panar": "communities_social_groups",
        "occupation.agriculture.uzhavar": "occupations_production",
        "polity.ruler": "polity_political_life",
    }
    for concept_id, expected_dimension in expected_concept_dimensions.items():
        concept = concepts.get(concept_id)
        if concept is None:
            errors.append(f"required existing concept is missing during dimension migration: {concept_id}")
        elif concept.get("dimension") != expected_dimension:
            errors.append(
                f"concept dimension migration mismatch: {concept_id} -> {concept.get('dimension')} (expected {expected_dimension})"
            )

    lived_life_rules = [rule for rule in policies.get("rules", []) if rule.get("family") == "lived_life"]
    if len(lived_life_rules) != 1:
        errors.append("there must be exactly one lived_life evidence-policy rule")
    else:
        policy_dimensions = tuple(lived_life_rules[0].get("dimensions", []))
        if policy_dimensions != LIVED_LIFE_DIMENSIONS:
            errors.append("lived_life evidence-policy dimensions are not aligned to the canonical non-structural matrix surface")
    for rule in policies.get("rules", []):
        for dimension in rule.get("dimensions", []):
            if dimension not in CANONICAL_ID_SET:
                errors.append(f"evidence policy references non-canonical dimension: {rule.get('family')} -> {dimension}")

    for observation in observations:
        dimension = observation.get("dimension")
        concept_id = observation.get("concept_id")
        if dimension not in CANONICAL_ID_SET:
            errors.append(f"pilot observation uses non-canonical dimension: {observation.get('observation_id')} -> {dimension}")
        concept = concepts.get(concept_id)
        if concept is None:
            errors.append(f"pilot observation references missing concept: {observation.get('observation_id')} -> {concept_id}")
        elif dimension != concept.get("dimension"):
            errors.append(f"pilot observation dimension disagrees with concept registry: {observation.get('observation_id')}")

    with (root / PILOT_MATRIX).open(encoding="utf-8", newline="") as handle:
        matrix_rows = list(csv.DictReader(handle))
    for row in matrix_rows:
        dimension = row.get("dimension")
        concept_id = row.get("concept_id")
        if dimension not in CANONICAL_ID_SET:
            errors.append(f"pilot matrix uses non-canonical dimension: {row.get('record_id')} -> {dimension}")
        concept = concepts.get(concept_id)
        if concept is not None and dimension != concept.get("dimension"):
            errors.append(f"pilot matrix dimension disagrees with concept registry: {row.get('record_id')} / {concept_id}")

    report = {
        "programme_id": "classical-tamil-research-layer",
        "phase": "R1.5",
        "gate": "production-dimension-alignment",
        "canonical_dimension_count": len(CANONICAL_DIMENSIONS),
        "production_vocabulary_dimension_count": len(entries),
        "concept_definitions_checked": len(concepts),
        "pilot_observations_checked": len(observations),
        "pilot_matrix_rows_checked": len(matrix_rows),
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
    parser.add_argument("--output", default="logs/classical-tamil-research-r15-production-dimensions.json")
    args = parser.parse_args()
    root = Path(args.root).resolve()
    report = validate(root, write=True, output=root / args.output)
    print(json.dumps(report, ensure_ascii=False, indent=2))
    if report["status"] != "pass":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
