#!/usr/bin/env python3
"""Validate the complete R1.5 model boundary and the gated R1.5A production continuation."""
from __future__ import annotations

import argparse
import json
from pathlib import Path

from research_r1lib import load_ndjson
from validate_research_r15 import validate as validate_pilot

REGISTRY = "research/concepts/classical-tamil/concept-registry-r15.json"
DIMENSIONS = "research/controlled-vocabularies/concept-dimensions-r15.json"
BASES = "research/controlled-vocabularies/classification-bases-r15.json"
POLICIES = "research/controlled-vocabularies/concept-evidence-policies-r15.json"
TOLK_SCHEMA = "research/schemas/tolkappiyam-concept-evidence-r15.schema.json"
TOLK_README = "research/observations/tolkappiyam/README.md"
ASSERTIONS = "research/evidence/purananuru/assertions.ndjson"
ENTITIES = "research/entities/pilot/entities.ndjson"
RELATIONSHIPS = "research/relationships/pilot/relationships.ndjson"
OBSERVATIONS = "research/observations/purananuru/r15-pilot.ndjson"
PURANANURU_PRODUCTION = "research/production/purananuru/records"
TOLK_OBSERVATION_DIR = "research/observations/tolkappiyam"

REQUIRED_FOUNDATION = {
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
    "literary.turai",
    "literary.turai.uncertain",
    "literary.turai.not_applicable",
    "landscape.classical",
    "landscape.kurinji",
    "landscape.mullai",
    "landscape.marutam",
    "landscape.neytal",
    "landscape.palai",
    "entity.named",
    "entity.person",
    "entity.place",
    "entity.polity",
    "entity.community",
    "entity.deity",
    "entity.uncertain",
}

REQUIRED_POLICY_FAMILIES = {
    "literary_domain",
    "tinai",
    "turai",
    "landscape_environment",
    "named_entity",
    "lived_life",
}


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def validate(root: Path, write: bool = False, output: Path | None = None) -> dict:
    errors: list[str] = []
    warnings: list[str] = []

    pilot_report = validate_pilot(root)
    if pilot_report["status"] != "pass":
        errors.append("base R1.5 pilot validator failed")
        errors.extend(f"pilot: {value}" for value in pilot_report["errors"])

    registry = load_json(root / REGISTRY)
    dimensions_vocab = load_json(root / DIMENSIONS)
    bases_vocab = load_json(root / BASES)
    policies = load_json(root / POLICIES)
    tolk_schema = load_json(root / TOLK_SCHEMA)
    assertions = load_ndjson(root / ASSERTIONS)
    entities = load_ndjson(root / ENTITIES)
    relationships = load_ndjson(root / RELATIONSHIPS)
    observations = load_ndjson(root / OBSERVATIONS)

    concepts = {value["concept_id"]: value for value in registry["concepts"]}
    dimensions = {value["code"] for value in dimensions_vocab["entries"]}
    bases = {value["code"] for value in bases_vocab["entries"]}
    assertion_ids = {value["assertion_id"] for value in assertions}
    entity_ids = {value["entity_id"] for value in entities}

    missing = sorted(REQUIRED_FOUNDATION - set(concepts))
    if missing:
        errors.append(f"missing complete R1.5 foundation concepts: {missing}")

    policy_families = {value["family"] for value in policies.get("rules", [])}
    missing_policy = sorted(REQUIRED_POLICY_FAMILIES - policy_families)
    if missing_policy:
        errors.append(f"missing R1.5 evidence-policy families: {missing_policy}")
    if policies.get("version") != "0.3.0":
        errors.append("R1.5 evidence-policy vocabulary version is not 0.3.0")

    for rule in policies.get("rules", []):
        for basis in rule.get("allowed_classification_bases", []):
            if basis not in bases:
                errors.append(f"evidence policy references unknown classification basis: {rule['family']} -> {basis}")
        if rule["family"] == "lived_life":
            for dimension in rule.get("dimensions", []):
                if dimension not in dimensions:
                    errors.append(f"lived-life policy references unknown dimension: {dimension}")

    if tolk_schema.get("properties", {}).get("schema_version", {}).get("const") != "0.3.0":
        errors.append("Tolkappiyam concept-evidence schema version is not 0.3.0")
    if tolk_schema.get("properties", {}).get("work_id", {}).get("const") != "tolkappiyam":
        errors.append("Tolkappiyam concept-evidence schema does not pin work_id")
    if tolk_schema.get("properties", {}).get("evidence_class", {}).get("const") != "GRAMMATICAL_CONCEPT_EVIDENCE":
        errors.append("Tolkappiyam concept stream does not pin GRAMMATICAL_CONCEPT_EVIDENCE")
    if tolk_schema.get("properties", {}).get("classification_basis", {}).get("const") != "tolkappiyam_mapping":
        errors.append("Tolkappiyam concept stream does not pin tolkappiyam_mapping")
    if not (root / TOLK_README).is_file():
        errors.append("Tolkappiyam concept-stream boundary documentation is missing")

    purananuru_records = sorted((root / PURANANURU_PRODUCTION).glob("[0-9][0-9][0-9].json"))
    purananuru_complete = len(purananuru_records) == 400 and (root / PURANANURU_PRODUCTION / "400.json").is_file()
    populated_tolk = sorted((root / TOLK_OBSERVATION_DIR).glob("*.ndjson"))
    tolk_observation_count = 0
    for path in populated_tolk:
        tolk_observation_count += len([line for line in path.read_text(encoding="utf-8").splitlines() if line.strip()])
    if populated_tolk and not purananuru_complete:
        errors.append("Tolkappiyam production observations are blocked until the Puṟanāṉūṟu 001–400 production corpus is complete")

    orphan_observation_assertions: list[str] = []
    orphan_observation_concepts: list[str] = []
    for observation in observations:
        if observation["concept_id"] not in concepts:
            orphan_observation_concepts.append(observation["observation_id"])
        for assertion_id in observation["supporting_assertion_ids"]:
            if assertion_id not in assertion_ids:
                orphan_observation_assertions.append(observation["observation_id"])
    if orphan_observation_assertions:
        errors.append(f"orphan observation assertions: {sorted(orphan_observation_assertions)}")
    if orphan_observation_concepts:
        errors.append(f"orphan observation concepts: {sorted(orphan_observation_concepts)}")

    orphan_relationship_assertions: list[str] = []
    orphan_relationship_entities: list[str] = []
    invalid_relationship_subjects: list[str] = []
    for relationship in relationships:
        rid = relationship["relationship_id"]
        for assertion_id in relationship.get("supporting_assertion_ids", []):
            if assertion_id not in assertion_ids:
                orphan_relationship_assertions.append(rid)
        if relationship.get("object_id") not in entity_ids:
            orphan_relationship_entities.append(rid)
        subject = relationship.get("subject_id", "")
        if not subject.startswith("record:purananuru:"):
            invalid_relationship_subjects.append(rid)
        else:
            try:
                record_number = int(subject.rsplit(":", 1)[1])
            except ValueError:
                invalid_relationship_subjects.append(rid)
            else:
                if not 1 <= record_number <= 400:
                    invalid_relationship_subjects.append(rid)

    if orphan_relationship_assertions:
        errors.append(f"orphan relationship assertions: {sorted(orphan_relationship_assertions)}")
    if orphan_relationship_entities:
        errors.append(f"orphan relationship entities: {sorted(orphan_relationship_entities)}")
    if invalid_relationship_subjects:
        errors.append(f"invalid relationship record subjects: {sorted(invalid_relationship_subjects)}")

    report = {
        "programme_id": "classical-tamil-research-layer",
        "phase": "R1.5",
        "gate": "acceptance",
        "concept_schema_version": "0.3.0",
        "foundation_concepts_required": len(REQUIRED_FOUNDATION),
        "foundation_concepts_present": len(REQUIRED_FOUNDATION & set(concepts)),
        "evidence_policy_families_checked": len(policy_families),
        "tolkappiyam_stream_schema_present": (root / TOLK_SCHEMA).is_file(),
        "purananuru_production_complete": purananuru_complete,
        "tolkappiyam_production_observation_count": tolk_observation_count,
        "observations_checked": len(observations),
        "relationships_checked": len(relationships),
        "orphan_observation_assertion_count": len(orphan_observation_assertions),
        "orphan_observation_concept_count": len(orphan_observation_concepts),
        "orphan_relationship_assertion_count": len(orphan_relationship_assertions),
        "orphan_relationship_entity_count": len(orphan_relationship_entities),
        "invalid_relationship_subject_count": len(invalid_relationship_subjects),
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
    parser.add_argument("--output", default="logs/classical-tamil-research-r15-acceptance-20260818T164600.json")
    args = parser.parse_args()
    root = Path(args.root).resolve()
    report = validate(root, write=True, output=root / args.output)
    print(json.dumps(report, ensure_ascii=False, indent=2))
    if report["status"] != "pass":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
