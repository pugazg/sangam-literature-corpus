# Puṟanāṉūṟu R1.5A production review ledger

This directory is the durable record-by-record production layer built on the merged R1.5 exact 29-dimension foundation.

## Hard boundaries

- Current phase: R1.5A. It is not R2.
- R1.5 merged into `main` at `d82f9c78f27f9c9daf8fbb913d01ddfb29bddba1`.
- `corpus/purananuru/` is frozen source material and is never edited by this review.
- The earlier sparse audit under `research/audits/r15-premerge/purananuru/` is a coverage/control artifact, not the production observation dataset.
- The Tolkāppiyam production pass must not begin until all 400 Puṟanāṉūṟu records are complete and validated.
- `docs/SOURCE_TERMINOLOGY_POLICY.md` is mandatory.

## Canonical ledger

Each reviewed poem is stored as one file under:

`research/production/purananuru/records/NNN.json`

Progress is the longest gap-free prefix beginning at `001`; prose status is not the authoritative progress counter.

Current materialized gap-free prefix: **001–210**.

- benchmark: 001–002;
- stabilization batch: **003–010** complete;
- regular 25-record batches: **011–035**, **036–060**, **061–085**, **086–110**, **111–135**, **136–160**, **161–185**, **186–210** complete;
- next record: **211**;
- next batch: **211–235**.

Current validated figures: **210 reviewed / 190 remaining / 3,736 production observations / 29 canonical dimensions / 224 tests passed**.

Before record `NNN+1` is read, that record's complete semantic decision state must already be durably staged. Git publication may batch several already-completed records.

Every record must:

1. identify the exact frozen canonical record and R0 assertion snapshot;
2. consider the exact 29 canonical dimensions in registry order;
3. distinguish qualifying evidence from reviewed-empty dimensions;
4. retain exact source Tamil and body-relative line/character spans for body evidence;
5. retain real R0 assertion IDs where an existing assertion genuinely supports the already-reviewed production observation;
6. mark genuinely new semantic evidence as `direct_r15_source_review_no_prior_assertion` rather than inventing an R0 assertion;
7. preserve source metadata/body/source-note provenance distinctions;
8. keep printed names as source mentions unless separately resolved through permitted external evidence;
9. preserve damaged/source-lost states without reconstruction;
10. compare against the old sparse audit only after the fresh source review is complete.

## Reviewed batch specs and materialization

Compact source-first reviewed batch specs live under:

`research/production/purananuru/review-specs/`

Completed 186–210 specs are:

- `186-190.json`
- `191-195.json`
- `196-200.json`
- `201-205.json`
- `206-210.json`

Spec splitting is only a compact staging detail; canonical production remains one separate `NNN.json` per poem and each completed 25-record activity is published as one final checkpoint.

`scripts/materialize_r15a_purananuru_batch.py` deterministically expands already-reviewed semantic decisions into canonical production records. It computes evidence spans, source/R0 blob identities, deterministic observation IDs, dimension-review rows, and post-review audit discrepancies.

`scripts/materialize_r15a_purananuru_batch_driver.py` is the range-aware orchestration/source-state compatibility layer. It selects the correct 50-record audit-control TSV for each record, safely handles a reviewed spec crossing an audit-part boundary, accepts a genuinely absent printed source-note block, and preserves a blank canonical `thurai` without inventing a `TURAI_VALUE` assertion. These compatibility rules only represent frozen source states; they do not classify semantics.

Neither script is an automatic semantic classifier. A pre-existing R0 body assertion may be auto-attached only when its assertion type belongs to the dimension already selected by fresh review and its exact source text occurs inside the already-selected source evidence.

The materializer records audit differences explicitly after fresh review. An order-only difference between canonical dimension order and the old control ledger is recorded as a discrepancy without changing the fresh semantic set or rewriting the control audit.

## Source-state lessons from 186–210

- Record 194 preserves null thinai/thurai/poet metadata and no source-note block; nothing is invented.
- Record 195 preserves `கணிச்சிக் கூர்ம்படைக் கடுந்திறல் ஒருவன்` as source death/religious imagery without later named-deity identification.
- Record 200's frozen canonical body consists only of `???` / `???`; only work-level `literary_domain` qualifies and all other 28 dimensions are explicitly reviewed-empty without reconstructing from the title or external tradition.
- Record 201 preserves exact `அந்தணன்`, `புலவன்`, `வேளிருள் வேளே`, and `பாண்கடன்`; body-level `பறம்பு` / `பாரி` / `துவரை` remain direct source-review named-entity evidence. Genuine matching body R0 support may be attached, while printed poet/addressee metadata remains a separate metadata observation.
- Record 202 preserves exact `வேட்டுவர்` and `தொல்குடி`; tiger-striped comparison stays imagery rather than evidence of an actual tiger occurrence; `புகழ்ந்த செய்யுள்` is explicit textual/intertextual evidence.
- Records 205–206 preserve exact `வேட்டுவ`, `பரிசிலர்`, and `மரங்கொல் தச்சன்`.
- Record 207 preserves `ஆளி` as source creature/animal imagery without modern taxonomic or mythological equivalence.
- Record 208 records `வாணிகப் பரிசிலன் அல்லேன்` as direct `trade_exchange` evidence without expanding it into an inferred market system.
- Record 210 preserves `கூற்றம்` as source death-agent/religious imagery without later deity/doctrine mapping.

Earlier provenance and terminology guardrails remain binding, including the record-176 body/metadata named-entity distinction.

## R1.5A cadence

The review is sequential; repository publication is batched.

- benchmark: 001–002;
- completed stabilization batch: **003–010**;
- completed regular batches: **011–035**, **036–060**, **061–085**, **086–110**, **111–135**, **136–160**, **161–185**, **186–210**;
- next batch: **211–235**;
- subsequent cadence: **236–260, ...**;
- final batch ends exactly at 400;
- one deterministic multi-file Git checkpoint per completed batch;
- full PR CI/non-drift once per published batch, not once per poem;
- if the active work session cannot complete a planned batch, checkpoint the completed contiguous prefix.

This cadence must never be used to skip sequential semantic review or to copy the control ledger into production.

## Evidence spans

For `canonical_body` evidence, `evidence_span.start_line` and `end_line` are 1-based poem-body line numbers. Character offsets are 0-based Unicode string positions within the cited body lines. `source_text` must reproduce the frozen source slice exactly.

Metadata evidence uses its exact YAML field/source location and may have a null body span.

## Empty-cell semantics

`no_qualifying_evidence_identified` means only that the completed review found no qualifying evidence for that dimension in that source record. It never asserts historical absence.

## Validation

At each batch checkpoint run:

```bash
python3 scripts/validate_research_r15_dimensions.py --root .
python3 scripts/validate_r15_purananuru_production.py --root .
pytest -q
```

The full PR workflow additionally covers R0/R1/R1.5 validation, deterministic R1 and R1.5 regeneration, repository audit, Corpus 1.1.0/Tolkāppiyam non-drift, R1 history preservation, and documentation continuity.
