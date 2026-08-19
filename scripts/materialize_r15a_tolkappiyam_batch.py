#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
from pathlib import Path

import yaml

CANONICAL = [
    "literary_domain","tinai_turai","landscape_environment","season_weather_time","flora","fauna",
    "people_social_roles","relationships","emotion_lived_experience","occupations_production","food_subsistence",
    "clothing_ornaments_adornment","material_culture_everyday_objects","weapons_warfare","mobility_transport",
    "settlements_built_environment","economy","trade_exchange","polity_political_life","communities_social_groups",
    "family_gender_kinship","religion_ritual","death_mourning_memory","arts_music_performance",
    "knowledge_technology","values_ethical_concepts","body_health","named_entities","textual_intertextual_relationships",
]
EMPTY = "No qualifying evidence identified in this reviewed நூற்பா; never evidence of historical absence."
REVIEW_MANIFEST = "research/audits/r15-premerge/tolkappiyam/review-manifest.json"
CROSSWALK = "research/audits/r15-premerge/tolkappiyam/dimension-crosswalk.json"
BASE_CONCEPTS = "research/concepts/classical-tamil/concept-registry-r15.json"
TOLK_CONCEPTS = "research/concepts/classical-tamil/tolkappiyam-production-concepts-r15a.json"
RECORD_DIR = "research/production/tolkappiyam/records"
OBSERVATION_STREAM = "research/observations/tolkappiyam/r15-production.ndjson"


def sha256_bytes(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def git_blob(path: Path, root: Path) -> str:
    return subprocess.check_output(
        ["git", "hash-object", str(path.relative_to(root))], cwd=root, text=True
    ).strip()


def parse_record(path: Path) -> tuple[dict, list[str]]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        raise ValueError(f"{path}: missing YAML frontmatter")
    _, rest = text.split("---\n", 1)
    front_text, rest = rest.split("\n---\n", 1)
    front = yaml.safe_load(front_text)
    body_lines = rest.splitlines()
    while body_lines and not body_lines[0].startswith("# "):
        body_lines.pop(0)
    if body_lines and body_lines[0].startswith("# "):
        body_lines.pop(0)
    body_lines = [line for line in body_lines if line != ""]
    return front, body_lines


def body_sha256(lines: list[str]) -> str:
    return hashlib.sha256(("\n".join(lines) + "\n").encode("utf-8")).hexdigest()


def evidence_ref(selector: list, lines: list[str]) -> dict:
    kind = selector[0]
    if kind == "line":
        n = selector[1]
        text = lines[n - 1]
        span = {"start_line": n, "start_character": 0, "end_line": n, "end_character": len(text)}
    elif kind == "range":
        a, b = selector[1], selector[2]
        text = "\n".join(lines[a - 1:b])
        span = {"start_line": a, "start_character": 0, "end_line": b, "end_character": len(lines[b - 1])}
    elif kind == "span":
        n, a, b = selector[1], selector[2], selector[3]
        text = lines[n - 1][a:b]
        span = {"start_line": n, "start_character": a, "end_line": n, "end_character": b}
    else:
        raise ValueError(f"unsupported Tolkappiyam evidence selector: {selector!r}")
    return {"source_location": "markdown:canonical-body", "evidence_span": span, "source_text": text}


def location_string(ref: dict) -> str:
    span = ref["evidence_span"]
    return (
        "markdown:canonical-body:"
        f"{span['start_line']}:{span['start_character']}-"
        f"{span['end_line']}:{span['end_character']}"
    )


def concept_evidence_id(record_id: str, dimension: str, concept_id: str, ref: dict) -> str:
    payload = {
        "record_id": record_id,
        "dimension": dimension,
        "concept_id": concept_id,
        "source_location": location_string(ref),
        "surface_form": ref["source_text"],
    }
    raw = json.dumps(payload, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return "gram.r15." + hashlib.sha256(raw).hexdigest()[:24]


def load_concepts(root: Path) -> dict[str, dict]:
    concepts: dict[str, dict] = {}
    for rel in (BASE_CONCEPTS, TOLK_CONCEPTS):
        value = json.loads((root / rel).read_text(encoding="utf-8"))
        for entry in value.get("concepts", []):
            cid = entry["concept_id"]
            if cid in concepts:
                raise ValueError(f"duplicate concept id across registries: {cid}")
            concepts[cid] = entry
    return concepts


def structure(front: dict) -> dict:
    return {
        "canonical_record_id": front["canonical_record_id"],
        "stable_semantic_id": front["stable_semantic_id"],
        "traditional_number": front.get("traditional_number"),
        "display_number": front.get("display_number"),
        "adhikaram": {
            "id": front["adhikaram"]["id"],
            "number": front["adhikaram"]["number"],
            "title_as_printed": front["adhikaram"]["title_as_printed"],
        },
        "iyal": {
            "id": front["iyal"]["id"],
            "number": front["iyal"]["number"],
            "source_sequence": front["iyal"]["source_sequence"],
            "title_as_printed": front["iyal"]["title_as_printed"],
        },
    }


def flatten_observations(root: Path) -> None:
    rows = []
    for path in sorted((root / RECORD_DIR).glob("[0-9][0-9][0-9][0-9].json")):
        value = json.loads(path.read_text(encoding="utf-8"))
        rows.extend(value.get("concept_evidence", []))
    out = root / OBSERVATION_STREAM
    out.parent.mkdir(parents=True, exist_ok=True)
    text = "".join(json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n" for row in rows)
    out.write_text(text, encoding="utf-8")


def materialize(root: Path, spec_path: Path) -> list[Path]:
    spec = json.loads(spec_path.read_text(encoding="utf-8"))
    records = spec.get("records", {})
    ids = sorted(records)
    if not ids:
        raise ValueError(f"{spec_path}: no records")
    nums = [int(rid) for rid in ids]
    if nums != list(range(nums[0], nums[-1] + 1)):
        raise ValueError(f"{spec_path}: record ids must form one contiguous source-sequence batch")

    outdir = root / RECORD_DIR
    outdir.mkdir(parents=True, exist_ok=True)
    existing = sorted(int(path.stem) for path in outdir.glob("[0-9][0-9][0-9][0-9].json"))
    expected_start = existing[-1] + 1 if existing else 1
    if nums[0] != expected_start:
        raise ValueError(f"{spec_path}: next allowed source sequence is {expected_start:04d}, not {nums[0]:04d}")

    concepts = load_concepts(root)
    written: list[Path] = []
    for rid, cfg in sorted(records.items()):
        n = int(rid)
        src = root / f"corpus/tolkappiyam/nurpas/{rid}.md"
        front, lines = parse_record(src)
        canonical_id = f"tolkappiyam-{rid}"
        if front.get("canonical_record_id") != canonical_id or front.get("source_sequence") != n:
            raise ValueError(f"{rid}: frozen canonical identity/source sequence mismatch")

        formal_cfg = cfg.get("formal_evidence", {})
        incidental_cfg = cfg.get("incidental_examples", {})
        unknown = (set(formal_cfg) | set(incidental_cfg)) - set(CANONICAL)
        if unknown:
            raise ValueError(f"{rid}: unknown dimensions {sorted(unknown)}")

        concept_evidence = []
        formal_by_dim = {dimension: [] for dimension in CANONICAL}
        incidental_by_dim = {dimension: [] for dimension in CANONICAL}

        for dimension, entries in formal_cfg.items():
            for entry in entries:
                concept_id = entry["concept_id"]
                concept = concepts.get(concept_id)
                if concept is None:
                    raise ValueError(f"{rid}: unknown controlled concept {concept_id}")
                if concept.get("dimension") != dimension:
                    raise ValueError(f"{rid}: concept {concept_id} does not belong to {dimension}")
                ref = evidence_ref(entry["e"], lines)
                evidence_id = concept_evidence_id(canonical_id, dimension, concept_id, ref)
                evidence = {
                    "schema_version": "0.3.0",
                    "concept_evidence_id": evidence_id,
                    "work_id": "tolkappiyam",
                    "record_id": canonical_id,
                    "concept_id": concept_id,
                    "dimension": dimension,
                    "surface_form": ref["source_text"],
                    "source_location": location_string(ref),
                    "evidence_class": "GRAMMATICAL_CONCEPT_EVIDENCE",
                    "classification_basis": "tolkappiyam_mapping",
                    "canonical_record_sha256": sha256_bytes(src),
                    "confidence": entry.get("confidence", "high"),
                    "review_status": "reviewed",
                    "notes": entry.get("note"),
                }
                concept_evidence.append(evidence)
                formal_by_dim[dimension].append(evidence_id)

        for dimension, entries in incidental_cfg.items():
            for entry in entries:
                ref = evidence_ref(entry["e"], lines)
                incidental_by_dim[dimension].append({**ref, "note": entry["note"]})

        reviews = []
        empty_notes = cfg.get("empty_notes", {})
        for ordinal, dimension in enumerate(CANONICAL, 1):
            formal_ids = formal_by_dim[dimension]
            incidental = incidental_by_dim[dimension]
            if formal_ids and incidental:
                status = "grammatical_and_incidental_evidence_recorded"
                default_note = "Formal grammatical concept evidence and incidental examples recorded separately."
            elif formal_ids:
                status = "grammatical_concept_evidence_recorded"
                default_note = "Qualifying grammatical/poetics concept evidence recorded."
            elif incidental:
                status = "incidental_example_recorded"
                default_note = "Incidental example recorded; it is not promoted to a historical or lived-life concept claim."
            else:
                status = "no_qualifying_evidence_identified"
                default_note = "No qualifying evidence identified."
            reviews.append({
                "ordinal": ordinal,
                "dimension": dimension,
                "status": status,
                "concept_evidence_ids": formal_ids,
                "incidental_examples": incidental,
                "review_note": empty_notes.get(dimension, default_note),
            })

        record = {
            "schema_version": "0.3.0",
            "phase": "R1.5",
            "production_review_id": f"tolkappiyam-r15-production-{rid}",
            "work_id": "tolkappiyam",
            "record_id": canonical_id,
            "source_sequence": n,
            "review_sequence_number": n,
            "source_snapshot": {
                "canonical_record_path": f"corpus/tolkappiyam/nurpas/{rid}.md",
                "canonical_record_git_blob_sha": git_blob(src, root),
                "canonical_record_sha256": sha256_bytes(src),
                "canonical_body_sha256": body_sha256(lines),
                "textual_status": str(front["textual_status"]),
                "canonical_text_available": bool(front["canonical_text_available"]),
                "parsing_confidence": str(front["parsing"]["confidence"]),
            },
            "source_structure_reviewed": structure(front),
            "dimensions_considered": 29,
            "dimension_reviews": reviews,
            "concept_evidence": concept_evidence,
            "review_status": "reviewed",
            "reviewer_type": "assistant_assisted",
            "empty_cell_semantics": EMPTY,
            "audit_control": {
                "review_manifest_path": REVIEW_MANIFEST,
                "dimension_crosswalk_path": CROSSWALK,
                "checked_after_fresh_source_review": True,
                "control_role": "coverage_and_representative_formal_support_only",
                "crosswalk_used_to_create_classification": False,
            },
            "next_record_allowed": f"tolkappiyam-{n + 1:04d}" if n < 1602 else None,
        }
        out = outdir / f"{rid}.json"
        out.write_text(json.dumps(record, ensure_ascii=False, separators=(",", ":")) + "\n", encoding="utf-8")
        written.append(out)

    flatten_observations(root)
    return written


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default=".")
    parser.add_argument("--spec", required=True)
    args = parser.parse_args()
    root = Path(args.root).resolve()
    written = materialize(root, (root / args.spec).resolve())
    print(json.dumps({"records_materialized": [path.stem for path in written]}, ensure_ascii=False))


if __name__ == "__main__":
    main()
