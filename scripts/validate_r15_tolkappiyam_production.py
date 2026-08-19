#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import re
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
RECORD_DIR = "research/production/tolkappiyam/records"
OBSERVATION_STREAM = "research/observations/tolkappiyam/r15-production.ndjson"
BASE_CONCEPTS = "research/concepts/classical-tamil/concept-registry-r15.json"
TOLK_CONCEPTS = "research/concepts/classical-tamil/tolkappiyam-production-concepts-r15a.json"
REVIEW_MANIFEST = "research/audits/r15-premerge/tolkappiyam/review-manifest.json"
CROSSWALK = "research/audits/r15-premerge/tolkappiyam/dimension-crosswalk.json"


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


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


def source_slice(lines: list[str], span: dict) -> str | None:
    a, b = span.get("start_line"), span.get("end_line")
    ac, bc = span.get("start_character"), span.get("end_character")
    if not all(isinstance(x, int) for x in (a, b, ac, bc)):
        return None
    if a < 1 or b < a or b > len(lines):
        return None
    if ac < 0 or ac > len(lines[a - 1]) or bc < 0 or bc > len(lines[b - 1]):
        return None
    if a == b:
        if bc < ac:
            return None
        return lines[a - 1][ac:bc]
    return "\n".join([lines[a - 1][ac:], *lines[a:b - 1], lines[b - 1][:bc]])


def concept_evidence_id(record_id: str, dimension: str, concept_id: str, source_location: str, surface_form: str) -> str:
    payload = {"record_id": record_id, "dimension": dimension, "concept_id": concept_id, "source_location": source_location, "surface_form": surface_form}
    raw = json.dumps(payload, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return "gram.r15." + hashlib.sha256(raw).hexdigest()[:24]


def load_concepts(root: Path) -> dict[str, dict]:
    out = {}
    for rel in (BASE_CONCEPTS, TOLK_CONCEPTS):
        data = load_json(root / rel)
        for concept in data.get("concepts", []):
            cid = concept["concept_id"]
            if cid in out:
                raise ValueError(f"duplicate concept id: {cid}")
            out[cid] = concept
    return out


def expected_structure(front: dict) -> dict:
    return {
        "canonical_record_id": front["canonical_record_id"],
        "stable_semantic_id": front["stable_semantic_id"],
        "traditional_number": front.get("traditional_number"),
        "display_number": front.get("display_number"),
        "adhikaram": {"id": front["adhikaram"]["id"], "number": front["adhikaram"]["number"], "title_as_printed": front["adhikaram"]["title_as_printed"]},
        "iyal": {"id": front["iyal"]["id"], "number": front["iyal"]["number"], "source_sequence": front["iyal"]["source_sequence"], "title_as_printed": front["iyal"]["title_as_printed"]},
    }


def validate(root: Path, write: bool = False, output: Path | None = None) -> dict:
    errors: list[str] = []
    warnings: list[str] = []
    record_dir = root / RECORD_DIR
    paths = sorted(record_dir.glob("[0-9][0-9][0-9][0-9].json")) if record_dir.is_dir() else []
    numbers = [int(path.stem) for path in paths]
    if numbers and numbers != list(range(1, max(numbers) + 1)):
        errors.append(f"Tolkappiyam production records must form a gap-free prefix from 0001; found {numbers}")

    try:
        concepts = load_concepts(root)
    except Exception as exc:
        concepts = {}
        errors.append(f"concept registry load failed: {exc}")

    manifest = load_json(root / REVIEW_MANIFEST)
    crosswalk = load_json(root / CROSSWALK)
    if manifest.get("records_reviewed") != 1602 or manifest.get("dimensions_considered_per_record") != 29:
        errors.append("Tolkappiyam control review manifest boundary drifted")
    if crosswalk.get("dimension_count") != 29 or crosswalk.get("status_counts") != {"SYSTEMATIC_FORMAL_FRAMEWORK": 17, "EXPLICIT_FORMAL_SUPPORT": 11, "FORMAL_SCOPE_LIMITED": 1}:
        errors.append("Tolkappiyam 29-dimension crosswalk boundary drifted")
    if crosswalk.get("interpretation_rule") is None:
        errors.append("Tolkappiyam crosswalk interpretation boundary is missing")

    flattened = []
    incidental_total = 0
    for expected_n, path in enumerate(paths, 1):
        value = load_json(path)
        rid = f"{expected_n:04d}"
        canonical_id = f"tolkappiyam-{rid}"
        prefix = f"{path.as_posix()}:"
        def err(message: str) -> None:
            errors.append(f"{prefix} {message}")

        if path.stem != rid:
            err(f"filename must be sequential {rid}")
        if value.get("schema_version") != "0.3.0" or value.get("phase") != "R1.5" or value.get("work_id") != "tolkappiyam":
            err("schema_version/phase/work_id mismatch")
        if value.get("record_id") != canonical_id or value.get("source_sequence") != expected_n or value.get("review_sequence_number") != expected_n:
            err("record identity/source/review sequence mismatch")
        if value.get("production_review_id") != f"tolkappiyam-r15-production-{rid}":
            err("production_review_id is not deterministic")
        if value.get("dimensions_considered") != 29:
            err("dimensions_considered must be 29")
        if value.get("review_status") != "reviewed" or value.get("empty_cell_semantics") != EMPTY:
            err("review/empty-cell contract mismatch")
        expected_next = f"tolkappiyam-{expected_n + 1:04d}" if expected_n < 1602 else None
        if value.get("next_record_allowed") != expected_next:
            err(f"next_record_allowed must be {expected_next!r}")

        src = root / f"corpus/tolkappiyam/nurpas/{rid}.md"
        if not src.is_file():
            err("frozen canonical source record missing")
            continue
        front, lines = parse_record(src)
        snap = value.get("source_snapshot", {})
        if snap.get("canonical_record_path") != f"corpus/tolkappiyam/nurpas/{rid}.md":
            err("canonical_record_path mismatch")
        if snap.get("canonical_record_sha256") != hashlib.sha256(src.read_bytes()).hexdigest():
            err("canonical_record_sha256 mismatch")
        if snap.get("canonical_body_sha256") != body_sha256(lines):
            err("canonical_body_sha256 mismatch")
        if snap.get("textual_status") != str(front.get("textual_status")):
            err("textual_status mismatch")
        if snap.get("canonical_text_available") != bool(front.get("canonical_text_available")):
            err("canonical_text_available mismatch")
        if snap.get("parsing_confidence") != str(front.get("parsing", {}).get("confidence")):
            err("parsing confidence mismatch")
        if value.get("source_structure_reviewed") != expected_structure(front):
            err("source_structure_reviewed is not an exact frozen structural copy")

        reviews = value.get("dimension_reviews", [])
        if [(r.get("ordinal"), r.get("dimension")) for r in reviews] != list(enumerate(CANONICAL, 1)):
            err("dimension_reviews must contain exact ordered 29-dimension surface")

        evidence = value.get("concept_evidence", [])
        evidence_by_id = {}
        for entry in evidence:
            eid = entry.get("concept_evidence_id")
            if eid in evidence_by_id:
                err(f"duplicate concept evidence id {eid}")
                continue
            evidence_by_id[eid] = entry
            if entry.get("schema_version") != "0.3.0" or entry.get("work_id") != "tolkappiyam":
                err(f"{eid}: evidence schema/work mismatch")
            if entry.get("record_id") != canonical_id:
                err(f"{eid}: record id mismatch")
            if entry.get("evidence_class") != "GRAMMATICAL_CONCEPT_EVIDENCE" or entry.get("classification_basis") != "tolkappiyam_mapping":
                err(f"{eid}: grammatical evidence class/basis mismatch")
            if entry.get("review_status") != "reviewed":
                err(f"{eid}: concept evidence must be reviewed")
            cid = entry.get("concept_id")
            concept = concepts.get(cid)
            if concept is None:
                err(f"{eid}: unknown controlled concept {cid}")
            elif concept.get("dimension") != entry.get("dimension"):
                err(f"{eid}: controlled concept/dimension mismatch")
            if entry.get("canonical_record_sha256") != snap.get("canonical_record_sha256"):
                err(f"{eid}: canonical record hash mismatch")
            loc = entry.get("source_location")
            match = re.fullmatch(r"markdown:canonical-body:(\d+):(\d+)-(\d+):(\d+)", str(loc))
            if not match:
                err(f"{eid}: unsupported source_location")
                continue
            span = {"start_line": int(match.group(1)), "start_character": int(match.group(2)), "end_line": int(match.group(3)), "end_character": int(match.group(4))}
            expected_text = source_slice(lines, span)
            if expected_text is None or expected_text != entry.get("surface_form"):
                err(f"{eid}: surface_form/source_location mismatch")
            expected_id = concept_evidence_id(canonical_id, entry.get("dimension"), cid, loc, entry.get("surface_form"))
            if eid != expected_id:
                err(f"{eid}: deterministic id mismatch")

        referenced = set()
        for review in reviews:
            dim = review.get("dimension")
            ids = review.get("concept_evidence_ids", [])
            incidental = review.get("incidental_examples", [])
            incidental_total += len(incidental)
            if ids and incidental:
                expected_status = "grammatical_and_incidental_evidence_recorded"
            elif ids:
                expected_status = "grammatical_concept_evidence_recorded"
            elif incidental:
                expected_status = "incidental_example_recorded"
            else:
                expected_status = "no_qualifying_evidence_identified"
            if review.get("status") != expected_status:
                err(f"{dim}: review status does not match formal/incidental evidence")
            for eid in ids:
                referenced.add(eid)
                entry = evidence_by_id.get(eid)
                if entry is None:
                    err(f"{dim}: references missing concept evidence {eid}")
                elif entry.get("dimension") != dim:
                    err(f"{dim}: references evidence from {entry.get('dimension')}")
            for example in incidental:
                span = example.get("evidence_span")
                if example.get("source_location") != "markdown:canonical-body" or not isinstance(span, dict):
                    err(f"{dim}: incidental example must use canonical-body span")
                    continue
                expected_text = source_slice(lines, span)
                if expected_text is None or expected_text != example.get("source_text"):
                    err(f"{dim}: incidental example span/source mismatch")
        if set(evidence_by_id) != referenced:
            err("concept_evidence list and dimension review references differ")

        if value.get("audit_control") != {
            "review_manifest_path": REVIEW_MANIFEST,
            "dimension_crosswalk_path": CROSSWALK,
            "checked_after_fresh_source_review": True,
            "control_role": "coverage_and_representative_formal_support_only",
            "crosswalk_used_to_create_classification": False,
        }:
            err("audit control boundary mismatch")
        flattened.extend(evidence)

    stream_path = root / OBSERVATION_STREAM
    if paths:
        if not stream_path.is_file():
            errors.append("Tolkappiyam production observation stream is missing")
        else:
            stream = [json.loads(line) for line in stream_path.read_text(encoding="utf-8").splitlines() if line.strip()]
            if stream != flattened:
                errors.append("Tolkappiyam production observation stream does not equal flattened per-record concept evidence")
    elif stream_path.exists() and stream_path.read_text(encoding="utf-8").strip():
        errors.append("Tolkappiyam observation stream is populated without production records")

    reviewed = max(numbers) if numbers else 0
    report = {
        "programme_id": "classical-tamil-research-layer",
        "phase": "R1.5",
        "gate": "tolkappiyam-29-dimension-production-prefix",
        "canonical_dimension_count": len(CANONICAL),
        "records_reviewed": reviewed,
        "records_remaining": 1602 - reviewed,
        "next_record": f"tolkappiyam-{reviewed + 1:04d}" if reviewed < 1602 else None,
        "grammatical_concept_evidence_checked": len(flattened),
        "incidental_examples_checked": incidental_total,
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
    parser.add_argument("--output")
    args = parser.parse_args()
    root = Path(args.root).resolve()
    report = validate(root, write=bool(args.output), output=(root / args.output) if args.output else None)
    print(json.dumps(report, ensure_ascii=False, indent=2))
    raise SystemExit(0 if report["status"] == "pass" else 1)


if __name__ == "__main__":
    main()
