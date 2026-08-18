#!/usr/bin/env python3
"""Generate deterministic R1.5 concept observations and a bounded matrix pilot.

R1.5 is a derived layer over immutable R0 evidence and append-only R1 review
history. This generator reads the R1 reviewed export plus an explicit pilot
mapping and never writes canonical corpus, source, assertion, review-event, or
entity-resolution paths.
"""
from __future__ import annotations

import argparse
import csv
import io
import json
from collections import defaultdict
from pathlib import Path

from researchlib import advisory_lock, atomic_write, write_json
from research_r1lib import load_ndjson, ndjson, stable_id

R15_SCHEMA_VERSION = "0.3.0"
PILOT_MAPPING = "research/pilots/purananuru/r15-pilot-mapping.json"
REVIEWED_EXPORT = "research/reviews/purananuru/reviewed-export.ndjson"
CONCEPT_REGISTRY = "research/concepts/classical-tamil/concept-registry-r15.json"
OBSERVATIONS = "research/observations/purananuru/r15-pilot.ndjson"
MATRIX = "research/matrices/purananuru/r15-pilot-matrix.csv"
SUMMARY_JSON = "research/reports/purananuru-r15-pilot-summary.json"
SUMMARY_MD = "research/reports/purananuru-r15-pilot-summary.md"


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def observation_id(assertion_id: str, concept_id: str, classification_basis: str) -> str:
    return stable_id(
        "obs.r15.",
        {
            "assertion_id": assertion_id,
            "concept_id": concept_id,
            "classification_basis": classification_basis,
        },
    )


def build_observations(root: Path) -> list[dict]:
    registry = load_json(root / CONCEPT_REGISTRY)
    pilot = load_json(root / PILOT_MAPPING)
    reviewed = load_ndjson(root / REVIEWED_EXPORT)

    concepts = {value["concept_id"]: value for value in registry["concepts"]}
    reviewed_by_assertion = {value["assertion_id"]: value for value in reviewed}
    observations: list[dict] = []

    for mapping in pilot["mappings"]:
        assertion_id = mapping["assertion_id"]
        if assertion_id not in reviewed_by_assertion:
            raise ValueError(f"R1.5 pilot mapping references non-reviewed assertion: {assertion_id}")
        row = reviewed_by_assertion[assertion_id]
        if row["assertion_type"] != mapping["expected_assertion_type"]:
            raise ValueError(f"assertion type drift for {assertion_id}")
        if row["printed_form"] != mapping["expected_printed_form"]:
            raise ValueError(f"printed-form drift for {assertion_id}")
        concept_id = mapping["concept_id"]
        if concept_id not in concepts:
            raise ValueError(f"unknown R1.5 concept: {concept_id}")
        concept = concepts[concept_id]
        basis = pilot["classification_basis"]
        observations.append(
            {
                "schema_version": R15_SCHEMA_VERSION,
                "observation_id": observation_id(assertion_id, concept_id, basis),
                "work_id": row["work_id"],
                "record_id": row["record_id"],
                "concept_id": concept_id,
                "dimension": concept["dimension"],
                "surface_form": row["printed_form"],
                "source_assertion_type": row["assertion_type"],
                "evidence_span": row["evidence_span"],
                "source_field": row["source_field"],
                "source_location": row["source_location"],
                "evidence_class": "SOURCE_EXPLICIT",
                "classification_basis": basis,
                "supporting_assertion_ids": row["supporting_assertion_ids"],
                "confidence": row["current_confidence"],
                "review_status": row["current_review_status"],
                "reviewer_type": row["reviewer_type"],
                "historical_identity_status": mapping["historical_identity_status"],
                "ambiguity_note": row["ambiguity_note"],
            }
        )

    observations.sort(
        key=lambda value: (
            int(value["record_id"]),
            value["concept_id"],
            value["observation_id"],
        )
    )
    return observations


def build_matrix(observations: list[dict]) -> str:
    groups: dict[tuple[str, str, str, str], list[dict]] = defaultdict(list)
    for value in observations:
        groups[
            (
                value["work_id"],
                value["record_id"],
                value["dimension"],
                value["concept_id"],
            )
        ].append(value)

    output = io.StringIO(newline="")
    writer = csv.writer(output, lineterminator="\n")
    writer.writerow(
        [
            "work_id",
            "record_id",
            "dimension",
            "concept_id",
            "observation_count",
            "surface_forms",
            "observation_ids",
            "supporting_assertion_ids",
            "evidence_classes",
            "review_statuses",
        ]
    )
    for key, values in sorted(
        groups.items(),
        key=lambda item: (int(item[0][1]), item[0][2], item[0][3]),
    ):
        writer.writerow(
            [
                *key,
                len(values),
                "|".join(sorted({value["surface_form"] for value in values})),
                "|".join(value["observation_id"] for value in values),
                "|".join(
                    sorted(
                        {
                            assertion_id
                            for value in values
                            for assertion_id in value["supporting_assertion_ids"]
                        }
                    )
                ),
                "|".join(sorted({value["evidence_class"] for value in values})),
                "|".join(sorted({value["review_status"] for value in values})),
            ]
        )
    return output.getvalue()


def build_summary(observations: list[dict]) -> dict:
    return {
        "programme_id": "classical-tamil-research-layer",
        "phase": "R1.5",
        "concept_schema_version": R15_SCHEMA_VERSION,
        "evidence_schema_version": "0.1.0",
        "review_workflow_schema_version": "0.2.0",
        "work_id": "purananuru",
        "pilot_id": "purananuru-r15-reviewed-eight",
        "pilot_observation_count": len(observations),
        "pilot_record_count": len({value["record_id"] for value in observations}),
        "pilot_concept_count": len({value["concept_id"] for value in observations}),
        "pilot_dimension_count": len({value["dimension"] for value in observations}),
        "source_explicit_observation_count": sum(
            value["evidence_class"] == "SOURCE_EXPLICIT" for value in observations
        ),
        "reviewed_observation_count": sum(
            value["review_status"] == "reviewed" for value in observations
        ),
        "unresolved_identity_observation_count": sum(
            value["historical_identity_status"] == "unresolved"
            for value in observations
        ),
        "external_historical_observation_count": sum(
            value["evidence_class"] == "EXTERNAL_HISTORICAL"
            for value in observations
        ),
        "interpretation_observation_count": sum(
            value["evidence_class"] == "INTERPRETATION" for value in observations
        ),
        "verified_historical_identity_count": sum(
            value["historical_identity_status"] == "verified_external"
            for value in observations
        ),
        "empty_cell_semantics": (
            "No qualifying evidence is currently recorded; not evidence of historical absence."
        ),
        "status": "pilot_foundation",
    }


def build_summary_markdown(summary: dict) -> str:
    return "\n".join(
        [
            "# Puṟanāṉūṟu R1.5 concept-matrix pilot",
            "",
            "R1.5 introduces an evidence-backed observation layer between reviewed assertions and generated research matrices. It does not rewrite R0 evidence or R1 review history.",
            "",
            f"- Pilot source: `{REVIEWED_EXPORT}`",
            f"- Pilot observations: {summary['pilot_observation_count']}",
            f"- Records represented: {summary['pilot_record_count']}",
            f"- Controlled concepts represented: {summary['pilot_concept_count']}",
            f"- Matrix dimensions represented: {summary['pilot_dimension_count']}",
            f"- Source-explicit observations: {summary['source_explicit_observation_count']}",
            f"- Reviewed observations: {summary['reviewed_observation_count']}",
            f"- Unresolved historical-identity observations: {summary['unresolved_identity_observation_count']}",
            f"- External-historical observations: {summary['external_historical_observation_count']}",
            f"- Interpretation observations: {summary['interpretation_observation_count']}",
            f"- Verified historical identities: {summary['verified_historical_identity_count']}",
            "",
            "The two ruler observations remain generic `polity.ruler` concept memberships with unresolved historical identity. A matrix cell is a derived view over observations. An empty cell means only that qualifying evidence is not currently recorded; it does not establish historical absence.",
            "",
            "This bounded pilot is a schema/provenance test. It is not corpus-wide R2 extraction.",
            "",
        ]
    )


def generate(root: Path) -> dict:
    observations = build_observations(root)
    atomic_write(root / OBSERVATIONS, ndjson(observations))
    atomic_write(root / MATRIX, build_matrix(observations))
    summary = build_summary(observations)
    write_json(root / SUMMARY_JSON, summary)
    atomic_write(root / SUMMARY_MD, build_summary_markdown(summary))
    return summary


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default=".")
    args = parser.parse_args()
    root = Path(args.root).resolve()
    with advisory_lock(root / "research/.generation-r15.lock"):
        summary = generate(root)
    (root / "research/.generation-r15.lock").unlink(missing_ok=True)
    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
