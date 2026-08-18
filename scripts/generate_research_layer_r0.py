#!/usr/bin/env python3
"""Generate the deterministic Puṟanāṉūṟu R0 evidence pilot."""
from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
import re
from collections import Counter, defaultdict
from pathlib import Path

from researchlib import (
    PROGRAMME_ID, RESEARCH_SCHEMA_VERSION, advisory_lock, assertion_id,
    atomic_write, normalize_lookup, parse_poem, relationship_id, sha_file,
    write_json,
)

ASSERTION_ORDER = [
    "POET_ATTRIBUTION", "PATRON_OR_ADDRESSEE", "TINI_VALUE", "TURAI_VALUE",
    "SOURCE_CONTEXT_NOTE", "TEXTUAL_CONDITION", "PERSON_MENTION", "RULER_MENTION",
    "PLACE_MENTION", "REGION_MENTION", "WATER_BODY_MENTION", "MOUNTAIN_OR_HILL_MENTION",
    "COMMUNITY_MENTION", "OCCUPATION_MENTION", "KINSHIP_MENTION", "FLORA_MENTION",
    "FAUNA_MENTION", "COMMODITY_MENTION", "GIFT_MENTION", "ECONOMIC_ACTIVITY",
    "WARFARE_MENTION", "POLITICAL_RELATION", "SOCIAL_PRACTICE", "MUSIC_OR_PERFORMANCE",
]
ORDER_INDEX = {value: index for index, value in enumerate(ASSERTION_ORDER)}

SEED_TERMS = {
    "WATER_BODY_MENTION": ["கடல்", "ஆறு"],
    "MOUNTAIN_OR_HILL_MENTION": ["மலை", "குன்று"],
    "COMMUNITY_MENTION": ["பாணர்", "மறவர்"],
    "OCCUPATION_MENTION": ["உழவர்", "மீனவர்"],
    "KINSHIP_MENTION": ["தாய்", "தந்தை", "மகன்", "மகள்"],
    "FLORA_MENTION": ["மரம்", "மலர்", "நெல்", "பனை", "வேங்கை", "முல்லை"],
    "FAUNA_MENTION": ["யானை", "களிறு", "புலி", "மான்", "குதிரை", "மீன்"],
    "COMMODITY_MENTION": ["உப்பு", "முத்து", "பொன்"],
    "GIFT_MENTION": ["பரிசில்", "ஈகை"],
    "ECONOMIC_ACTIVITY": ["உழவு", "வாணிகம்", "வரி"],
    "WARFARE_MENTION": ["போர்", "படை", "வாள்", "வேல்", "முரசு"],
    "POLITICAL_RELATION": ["அரசன்", "வேந்தன்", "மன்னன்"],
    "SOCIAL_PRACTICE": ["நடுகல்", "தானம்"],
    "MUSIC_OR_PERFORMANCE": ["யாழ்", "பாடல்", "கூத்து"],
}


def schema_files(root: Path) -> None:
    common = {
        "$schema": "https://json-schema.org/draft/2020-12/schema",
        "type": "object",
        "additionalProperties": True,
    }
    assertion = common | {
        "$id": "assertion.schema.json",
        "required": ["assertion_id", "research_schema_version", "programme_id", "work_id", "record_id", "canonical_record_path", "canonical_record_sha256", "canonical_body_sha256", "source_note_sha256", "assertion_type", "evidence_class", "subject", "predicate", "object", "source_text", "evidence_span", "source_field", "source_location", "source_note_reference", "extraction_method", "extractor_version", "confidence", "review_status", "normalization", "notes"],
        "properties": {
            "assertion_id": {"type": "string", "pattern": "^asrt\\.[0-9a-f]{24}$"},
            "evidence_class": {"enum": ["SOURCE_EXPLICIT", "MECHANICALLY_DERIVED", "CROSS_TEXT", "EXTERNAL_HISTORICAL", "EDITORIAL_INFERENCE", "INTERPRETATION"]},
            "review_status": {"enum": ["unreviewed", "machine_checked", "human_review_required", "reviewed", "verified", "rejected", "superseded"]},
            "confidence": {"enum": ["high", "medium", "low"]},
        },
    }
    mention = common | {"$id": "mention.schema.json", "required": ["assertion_id", "work_id", "record_id", "printed_form", "assertion_type", "evidence_span", "review_status"]}
    entity = common | {"$id": "entity.schema.json", "required": ["entity_id", "preferred_label", "entity_type", "mention_assertions", "review_status", "modern_identification"]}
    relationship = common | {"$id": "relationship.schema.json", "required": ["relationship_id", "subject_id", "predicate", "object_id", "supporting_assertion_ids", "evidence_class", "review_status"]}
    review = common | {"$id": "review-event.schema.json", "required": ["review_event_id", "assertion_id", "previous_status", "new_status", "decision", "reviewer", "reviewed_at", "notes"]}
    for name, value in (("assertion", assertion), ("mention", mention), ("entity", entity), ("relationship", relationship), ("review-event", review)):
        write_json(root / "research/schemas" / f"{name}.schema.json", value)


def vocab_entry(code: str, definition: str) -> dict:
    return {"code": code, "label": code.replace("_", " ").title(), "definition": definition, "broader_term": None, "narrower_terms": [], "status": "active", "introduced_in_version": RESEARCH_SCHEMA_VERSION, "notes": None}


def vocabulary_files(root: Path) -> None:
    values = {
        "assertion-types": [(x, "A source assertion or reviewable mention-candidate category.") for x in ASSERTION_ORDER],
        "evidence-classes": [(x, "Primary provenance class; confidence is recorded separately.") for x in ["SOURCE_EXPLICIT", "MECHANICALLY_DERIVED", "CROSS_TEXT", "EXTERNAL_HISTORICAL", "EDITORIAL_INFERENCE", "INTERPRETATION"]],
        "entity-types": [(x, "A non-identifying pilot entity category.") for x in ["PERSON", "RULER_OR_ADDRESSEE", "PLACE", "CONCEPT"]],
        "predicates": [(x, "Assertion or relationship predicate supported by explicit provenance.") for x in ["ATTRIBUTED_TO", "MENTIONS_PERSON", "ADDRESSED_TO", "ASSOCIATED_WITH_TINAI", "ASSOCIATED_WITH_TURAI", "HAS_PRINTED_TITLE", "HAS_TEXTUAL_STATUS", "HAS_PRINTED_SOURCE_NOTE", "MENTIONS_CANDIDATE", "MENTIONS_COMMUNITY", "MENTIONS_OCCUPATION", "MENTIONS_FLORA", "MENTIONS_FAUNA", "MENTIONS_COMMODITY", "MENTIONS_WARFARE", "MENTIONS_SOCIAL_PRACTICE", "POSSIBLY_SAME_AS"]],
        "review-statuses": [(x, "Append-only review workflow state.") for x in ["unreviewed", "machine_checked", "human_review_required", "reviewed", "verified", "rejected", "superseded"]],
        "confidence-levels": [(x, "Confidence in extraction or boundary, independent of evidence class.") for x in ["high", "medium", "low"]],
    }
    for name, entries in values.items():
        write_json(root / "research/controlled-vocabularies" / f"{name}.json", {"vocabulary": name, "version": RESEARCH_SCHEMA_VERSION, "entries": [vocab_entry(*entry) for entry in entries]})
    seed = []
    for assertion_type, terms in SEED_TERMS.items():
        for term in terms:
            seed.append({"printed_form": term, "assertion_type": assertion_type, "status": "pilot-candidate", "evidence_class": "SOURCE_EXPLICIT", "classification_review": "human_review_required"})
    write_json(root / "research/controlled-vocabularies/mention-seed-lexicon.json", {"version": RESEARCH_SCHEMA_VERSION, "scope": "purananuru R0 exact-token candidate extraction", "entries": seed})


def make_assertion(path: Path, parsed: dict, record_id: str, assertion_type: str, predicate: str, printed: str, source_field: str, source_location: str, span: dict | None, review: str, confidence: str, notes: str | None = None) -> dict:
    value = {
        "assertion_id": "",
        "research_schema_version": RESEARCH_SCHEMA_VERSION,
        "programme_id": PROGRAMME_ID,
        "work_id": "purananuru",
        "record_id": record_id,
        "canonical_record_path": path.as_posix(),
        "canonical_record_sha256": parsed["whole_sha256"],
        "canonical_body_sha256": parsed["body_sha256"],
        "source_note_sha256": parsed["source_note_sha256"],
        "assertion_type": assertion_type,
        "evidence_class": "SOURCE_EXPLICIT",
        "subject": f"record:purananuru:{record_id}",
        "predicate": predicate,
        "object": printed,
        "source_text": printed,
        "evidence_span": span,
        "source_field": source_field,
        "source_location": source_location,
        "source_note_reference": "## Source note (as printed)" if source_field == "source_note" else None,
        "extraction_method": "exact frozen-field copy" if span is None else "exact token/span match in frozen canonical body",
        "extractor_version": RESEARCH_SCHEMA_VERSION,
        "extracted_at": None,
        "confidence": confidence,
        "review_status": review,
        "reviewer": None,
        "reviewed_at": None,
        "normalization": {"printed_form": printed, "normalized_form": normalize_lookup(printed), "normalization_method": "Unicode NFC; punctuation-to-space and whitespace collapse for lookup only"},
        "notes": notes,
    }
    value["assertion_id"] = assertion_id(value)
    return value


def exact_token_spans(lines: list[str], term: str):
    pattern = re.compile(rf"(?<![\u0B80-\u0BFF]){re.escape(term)}(?![\u0B80-\u0BFF])")
    for line_no, line in enumerate(lines, 1):
        for match in pattern.finditer(line):
            yield {"start_line": line_no, "end_line": line_no, "start_character": match.start(), "end_character": match.end()}


def metadata_assertions(path: Path, parsed: dict, record_id: str) -> list[dict]:
    front = parsed["front"]
    result = []
    specs = [
        ("poet_as_printed", "POET_ATTRIBUTION", "ATTRIBUTED_TO"),
        ("addressee_as_printed", "PATRON_OR_ADDRESSEE", "ADDRESSED_TO"),
        ("thinai_as_printed", "TINI_VALUE", "ASSOCIATED_WITH_TINAI"),
        ("thurai", "TURAI_VALUE", "ASSOCIATED_WITH_TURAI"),
        ("title_as_printed", "SOURCE_CONTEXT_NOTE", "HAS_PRINTED_TITLE"),
    ]
    for field, kind, predicate in specs:
        printed = front.get(field)
        if printed not in (None, ""):
            assertion = make_assertion(path, parsed, record_id, kind, predicate, str(printed), field, f"yaml:{field}", None, "machine_checked", "high")
            if field in {"poet_as_printed", "addressee_as_printed", "thinai_as_printed", "thurai"}:
                assertion["source_note_reference"] = "## Source note (as printed)"
            result.append(assertion)
    status = str(front.get("textual_status"))
    result.append(make_assertion(path, parsed, record_id, "TEXTUAL_CONDITION", "HAS_TEXTUAL_STATUS", status, "textual_status", "yaml:textual_status", None, "machine_checked", "high"))
    if parsed["source_note"]:
        result.append(make_assertion(path, parsed, record_id, "SOURCE_CONTEXT_NOTE", "HAS_PRINTED_SOURCE_NOTE", parsed["source_note"], "source_note", "markdown:source-note", None, "machine_checked", "high"))
    return result


def body_candidates(path: Path, parsed: dict, record_id: str, person_forms: set[str], ruler_forms: set[str]) -> list[dict]:
    result = []
    terms = [(kind, term) for kind, values in SEED_TERMS.items() for term in values]
    terms += [("PERSON_MENTION", term) for term in sorted(person_forms)]
    terms += [("RULER_MENTION", term) for term in sorted(ruler_forms)]
    seen = set()
    for kind, term in terms:
        for span in exact_token_spans(parsed["body_lines"], term):
            key = (kind, term, tuple(span.values()))
            if key in seen:
                continue
            seen.add(key)
            result.append(make_assertion(path, parsed, record_id, kind, "MENTIONS_CANDIDATE", term, "canonical_body", "markdown:canonical-body", span, "human_review_required", "medium", "Exact printed-form candidate only; classification and identity are not human-verified."))
    return result


def assertion_sort(value: dict):
    span = value.get("evidence_span") or {}
    return (int(value["record_id"]), ORDER_INDEX.get(value["assertion_type"], 999), span.get("start_line", -1), span.get("start_character", -1), value["normalization"]["printed_form"], value["assertion_id"])


def ndjson(values: list[dict]) -> str:
    return "".join(json.dumps(value, ensure_ascii=False, sort_keys=True) + "\n" for value in values)


def generate(root: Path) -> dict:
    poems = sorted((root / "corpus/purananuru/poems").glob("*.md"))
    if len(poems) != 400:
        raise ValueError("Puṟanāṉūṟu must have exactly 400 frozen records")
    parsed_records = [(path.relative_to(root), parse_poem(path)) for path in poems]
    poet_forms = {str(parsed["front"].get("poet_as_printed")) for _, parsed in parsed_records if parsed["front"].get("poet_as_printed")}
    ruler_forms = {str(parsed["front"].get("addressee_as_printed")) for _, parsed in parsed_records if parsed["front"].get("addressee_as_printed")}
    assertions = []
    for path, parsed in parsed_records:
        record_id = f"{int(parsed['front']['poem_number']):03d}"
        current = metadata_assertions(path, parsed, record_id)
        if parsed["body"]:
            current.extend(body_candidates(path, parsed, record_id, poet_forms, ruler_forms))
        current.sort(key=assertion_sort)
        assertions.extend(current)
        atomic_write(root / f"research/evidence/purananuru/records/{record_id}.ndjson", ndjson(current))
    assertions.sort(key=assertion_sort)
    ids = [x["assertion_id"] for x in assertions]
    if len(ids) != len(set(ids)):
        raise ValueError("duplicate deterministic assertion IDs")
    atomic_write(root / "research/evidence/purananuru/assertions.ndjson", ndjson(assertions))

    columns = ["assertion_id", "work_id", "record_id", "assertion_type", "evidence_class", "predicate", "source_text", "source_field", "source_location", "start_line", "end_line", "start_character", "end_character", "confidence", "review_status", "canonical_record_path", "canonical_record_sha256"]
    output = io.StringIO(newline="")
    writer = csv.DictWriter(output, fieldnames=columns, lineterminator="\n")
    writer.writeheader()
    for value in assertions:
        span = value.get("evidence_span") or {}
        writer.writerow({key: span.get(key) if key in span else value.get(key) for key in columns})
    atomic_write(root / "research/evidence/purananuru/assertions.csv", output.getvalue())

    poets = [x for x in assertions if x["assertion_type"] == "POET_ATTRIBUTION"]
    atomic_write(root / "research/evidence/purananuru/poet-attributions.ndjson", ndjson(poets))
    mentions = [x for x in assertions if x["source_field"] == "canonical_body"]
    mention_rows = [{"assertion_id": x["assertion_id"], "work_id": x["work_id"], "record_id": x["record_id"], "printed_form": x["normalization"]["printed_form"], "normalized_form": x["normalization"]["normalized_form"], "assertion_type": x["assertion_type"], "evidence_span": x["evidence_span"], "review_status": x["review_status"]} for x in mentions]
    atomic_write(root / "research/mentions/purananuru/mentions.ndjson", ndjson(mention_rows))

    sample_assertions = [x for x in assertions if int(x["record_id"]) <= 25 and x["assertion_type"] in {"POET_ATTRIBUTION", "PATRON_OR_ADDRESSEE", "PERSON_MENTION", "RULER_MENTION"}]
    grouped = defaultdict(list)
    for value in sample_assertions:
        entity_type = "RULER_OR_ADDRESSEE" if value["assertion_type"] in {"PATRON_OR_ADDRESSEE", "RULER_MENTION"} else "PERSON"
        grouped[(entity_type, value["normalization"]["printed_form"])].append(value["assertion_id"])
    entities = []
    for (entity_type, printed), mention_ids in sorted(grouped.items()):
        entity_id = "entity.pilot." + hashlib.sha256(f"{entity_type}|{printed}".encode()).hexdigest()[:16]
        entities.append({"entity_id": entity_id, "preferred_label": printed, "entity_type": entity_type, "mention_assertions": sorted(set(mention_ids)), "review_status": "human_review_required", "modern_identification": None, "notes": "Surface-form entity only; no claim that variant forms or repeated names denote one historical person."})
    atomic_write(root / "research/entities/pilot/entities.ndjson", ndjson(entities))
    entity_by_assertion = {assertion: entity["entity_id"] for entity in entities for assertion in entity["mention_assertions"]}
    relationships = []
    by_id = {x["assertion_id"]: x for x in assertions}
    pred = {"POET_ATTRIBUTION": "ATTRIBUTED_TO", "PATRON_OR_ADDRESSEE": "ADDRESSED_TO", "PERSON_MENTION": "MENTIONS_PERSON", "RULER_MENTION": "MENTIONS_PERSON"}
    for assertion, entity_id in sorted(entity_by_assertion.items()):
        source = by_id[assertion]
        relation = {"relationship_id": "", "subject_id": source["subject"], "predicate": pred[source["assertion_type"]], "object_id": entity_id, "supporting_assertion_ids": [assertion], "evidence_class": source["evidence_class"], "review_status": "human_review_required"}
        relation["relationship_id"] = relationship_id(relation)
        relationships.append(relation)
    atomic_write(root / "research/relationships/pilot/relationships.ndjson", ndjson(relationships))
    atomic_write(root / "research/reviews/purananuru/review-events.ndjson", "")

    type_counts = Counter(x["assertion_type"] for x in assertions)
    evidence_counts = Counter(x["evidence_class"] for x in assertions)
    review_counts = Counter(x["review_status"] for x in assertions)
    records_with = {x["record_id"] for x in assertions}
    summary = {
        "programme_id": PROGRAMME_ID, "research_schema_version": RESEARCH_SCHEMA_VERSION,
        "research_status": "pilot", "work_id": "purananuru", "records_processed": 400,
        "literary_bodies_processed": 398, "source_lost_records": [267, 268],
        "assertion_count": len(assertions), "mention_count": len(mentions),
        "entity_sample_count": len(entities), "relationship_count": len(relationships),
        "assertions_by_type": dict(sorted(type_counts.items())), "assertions_by_evidence_class": dict(sorted(evidence_counts.items())),
        "review_status_counts": dict(sorted(review_counts.items())),
        "records_with_no_assertions": [f"{x:03d}" for x in range(1, 401) if f"{x:03d}" not in records_with],
        "external_historical_assertions": 0, "interpretation_assertions": 0,
        "warning": "Candidate counts are textual evidence records, not historical fact or resolved-entity counts.",
    }
    write_json(root / "research/evidence/purananuru/summary.json", summary)
    write_json(root / "research/reports/purananuru-extraction-summary.json", summary)
    md = ["# Puṟanāṉūṟu R0 extraction summary", "", "This is derived evidence, not a corrected text, translation, or historical interpretation.", "", f"- Records processed: 400", f"- Literary bodies processed: 398", f"- Source-lost records: 267, 268", f"- Assertions: {len(assertions)}", f"- Literary-body mention candidates: {len(mentions)}", f"- Pilot entities: {len(entities)}", f"- Pilot relationships: {len(relationships)}", "", "All literary-body candidates require human review. Counts do not represent historical facts."]
    atomic_write(root / "research/reports/purananuru-extraction-summary.md", "\n".join(md) + "\n")
    coverage = io.StringIO(newline=""); cw = csv.writer(coverage, lineterminator="\n"); cw.writerow(["assertion_type", "count", "evidence_class", "default_review_status"])
    for kind, count in sorted(type_counts.items(), key=lambda x: ORDER_INDEX.get(x[0], 999)):
        cw.writerow([kind, count, "SOURCE_EXPLICIT", "human_review_required" if kind.endswith("MENTION") or kind in {"ECONOMIC_ACTIVITY", "POLITICAL_RELATION", "SOCIAL_PRACTICE", "MUSIC_OR_PERFORMANCE"} else "machine_checked"])
    atomic_write(root / "research/reports/purananuru-coverage-by-assertion-type.csv", coverage.getvalue())
    unresolved = io.StringIO(newline=""); uw = csv.writer(unresolved, lineterminator="\n"); uw.writerow(["assertion_id", "record_id", "assertion_type", "printed_form", "start_line", "start_character", "review_status"])
    for value in mentions:
        span = value["evidence_span"]; uw.writerow([value["assertion_id"], value["record_id"], value["assertion_type"], value["source_text"], span["start_line"], span["start_character"], value["review_status"]])
    atomic_write(root / "research/reports/purananuru-unresolved-mentions.csv", unresolved.getvalue())
    atomic_write(root / "research/reports/purananuru-ambiguity-register.md", "# Puṟanāṉūṟu R0 ambiguity register\n\n- Every literary-body category match is a candidate requiring human review.\n- Surface-form entities do not assert historical identity.\n- Variant poet and addressee forms are not merged.\n- Modern geographic and taxonomic identifications remain null.\n- The forty printed lacuna conditions remain corpus evidence and are not reconstructed.\n- Records 267 and 268 are source-lost and have no literary-body candidates.\n")

    sample_numbers = sorted(set(range(1, 11)) | set(range(95, 106)) | set(range(175, 186)) | set(range(240, 251)) | set(range(263, 271)) | set(range(390, 401)))
    by_record = defaultdict(list)
    for value in assertions: by_record[int(value["record_id"])].append(value)
    review_md = ["# Puṟanāṉūṟu deterministic pilot review sample", "", "No entry in this sample is automatically human-verified.", ""]
    parsed_by_no = {int(p["front"]["poem_number"]): p for _, p in parsed_records}
    for number in sample_numbers:
        parsed = parsed_by_no[number]
        review_md += [f"## Record {number}", "", "### Canonical body", "", parsed["body"] or "_[Source-lost: no canonical literary body]_", "", "### Extracted assertions", ""]
        for value in by_record[number]:
            span = value.get("evidence_span")
            location = f"line {span['start_line']}, characters {span['start_character']}–{span['end_character']}" if span else value["source_location"]
            review_md.append(f"- `{value['assertion_type']}` — `{value['source_text']}` — {location}; confidence `{value['confidence']}`; status `{value['review_status']}`")
        review_md.append("")
    atomic_write(root / "research/reviews/purananuru/pilot-review-sample.md", "\n".join(review_md).rstrip() + "\n")
    return summary


def main() -> None:
    parser = argparse.ArgumentParser(); parser.add_argument("--root", default="."); args = parser.parse_args()
    root = Path(args.root).resolve()
    with advisory_lock(root / "research/.generation.lock"):
        schema_files(root); vocabulary_files(root); summary = generate(root)
    (root / "research/.generation.lock").unlink(missing_ok=True)
    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__": main()
