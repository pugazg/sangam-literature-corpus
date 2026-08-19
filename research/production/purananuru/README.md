# Puṟanāṉūṟu R1.5A production review ledger

This directory is the durable record-by-record production layer built on the merged R1.5 exact 29-dimension foundation.

## Hard boundaries

- Current phase: R1.5A. It is not R2.
- R1.5 merged into `main` at `d82f9c78f27f9c9daf8fbb913d01ddfb29bddba1`.
- `corpus/purananuru/` is frozen source material and is never edited by this review.
- The earlier sparse audit under `research/audits/r15-premerge/purananuru/` is post-review control evidence, not the production dataset.
- The Tolkāppiyam production pass must not begin until all 400 Puṟanāṉūṟu records are complete and validated.
- `docs/SOURCE_TERMINOLOGY_POLICY.md` is mandatory.

## Canonical ledger

Each reviewed poem is stored as one file under `research/production/purananuru/records/NNN.json`.

Progress is the longest gap-free prefix beginning at `001`; prose status is not the authoritative progress counter.

Current materialized gap-free prefix: **001–335**.

- benchmark: 001–002;
- stabilization batch: **003–010** complete;
- regular **25-record** batches: **011–035**, **036–060**, **061–085**, **086–110**, **111–135**, **136–160**, **161–185**, **186–210**, **211–235**, **236–260**, **261–285**, **286–310**, **311–335** complete;
- next record: **336**;
- next batch: **336–360**.

Current validated figures: **335 reviewed / 65 remaining / 5,866 production observations / 29 canonical dimensions / 224 tests passed**.

Before record `NNN+1` is read, that record's complete semantic decision state must already be complete. Git publication/materialization may batch already-completed records.

Every record must identify the exact frozen source and R0 snapshot, consider all 29 dimensions, distinguish qualifying evidence from reviewed-empty states, retain exact source Tamil/spans, preserve metadata/body/source-note distinctions, keep printed names unresolved unless separately resolved, preserve damaged/source-lost states without reconstruction, and compare the old audit only after fresh source review.

## Reviewed batch specs and materialization

Compact source-first reviewed specs live under `research/production/purananuru/review-specs/`.

The completed 311–335 publication used:

- `311-315.json`
- `316-320.json`
- `321-325.json`
- `326-330.json`
- `331-335.json`

All 25 poems were semantically reviewed sequentially and source-first before the audit was opened. The five-spec publication was chosen only to keep connector writes manageable and to isolate validation of record 323's new unknown-attribution source state.

The 261–285 and 286–310 batches prove that one contiguous 25-record spec + one materialization cycle is safe when practical. Split specs remain valid when technical/source-state isolation is useful. **This never batches semantic review.**

`scripts/materialize_r15a_purananuru_batch.py` deterministically expands already-reviewed decisions into canonical records. It is not a classifier.

`scripts/materialize_r15a_purananuru_batch_driver.py` is the range-aware source-state compatibility layer. It handles audit-part selection, absent source-note blocks, blank canonical `thurai`, and exact unknown-poet/non-identification metadata without allowing those phrases to become named entities.

Current exact literals handled by the driver:

- `பெயர் தெரிந்திலது`
- `பெயர் புலனாகவில்லை`
- `பாடப்பட்டோர் : பெயர்கள் தெரிந்தில`

The driver temporarily exposes null only to core named-entity linking, then restores the exact printed value in `source_metadata_reviewed.poet_as_printed`. This is source-state compatibility only.

A pre-existing R0 body assertion may attach only when its type belongs to a dimension already selected by fresh review and its exact source text occurs inside selected evidence.

## Source-state lessons from 311–335

- 311 preserves exact `புலைத்தி` without later identity substitution.
- 312 preserves absent source note and null thinai/thurai/poet/addressee; body `கடன்` duties, craft and warfare do not reconstruct metadata.
- 313 preserves exact `இரவன் மாக்கள்`, `உமணர்`, `உப்பொய் சாகாட்டு`; no wider market system is inferred.
- 315 separates printed poet/`பாடப்பட்டோன்` attribution from body `நெடுமான் அஞ்சி` and records the relation as TIR.
- 317, 321, 328, 333, 334 and 335 remain incomplete/lacunose and are not reconstructed.
- 319 preserves exact `யாம் க·டு உண்டென` without silent repair.
- 322 preserves `கரும்பின் எந்திரம்` and `கண்படை ஈயா` as source-explicit technology/body-state evidence.
- 323 preserves `பாடப்பட்டோர் : பெயர்கள் தெரிந்தில` and `பாடியவர் பாடப்பட்டோர் : பெயர்கள் தெரிந்தில.` as unresolved attribution; `named_entities` remains reviewed-empty.
- 324 preserves exact `வேட்டுவர்`, `இடையன்`, `பாணர்`.
- 327–328 and 333 preserve exact `பெயர் தெரிந்திலது` without manufacturing identities.
- 329 preserves `நடுகல்`, `நாட்பலி`, water, ghee/fragrance and smoke as an explicit memorial-stone ritual sequence without later doctrinal expansion.
- 331 preserves alternate poet reading `உறையூர் முது கூற்றனார் எனவும் பாடம்` as TIR and keeps `போகுபலி வெண்சோறு` source-bound.
- 332 preserves exact `மறவன்` as source martial/social terminology.
- 335 retains only surviving plant names (`குருந்து`, `முல்லை`, `வரகு`, `தினை`, `கொள்ளு`, `அவரை`), preserves exact `துடியன், பாணன், பறையன், கடம்பன்`, and treats `கல்லே பரவின் ... நெல்உகுத்துப் பரவும் கடவுளும் இலவே` as this poem's own memorial-worship/deity language rather than a generalized historical absence claim.

Earlier provenance and terminology guardrails remain binding, including record 176, damaged record 200 and source-lost records 267–268.

## R1.5A cadence

The review is sequential; repository publication is batched.

- benchmark: 001–002;
- completed stabilization batch: **003–010**;
- completed regular **25-record** batches: **011–035**, **036–060**, **061–085**, **086–110**, **111–135**, **136–160**, **161–185**, **186–210**, **211–235**, **236–260**, **261–285**, **286–310**, **311–335**;
- next batch: **336–360**;
- subsequent cadence: **361–385, 386–400**;
- final batch ends exactly at 400;
- prefer one contiguous 25-record spec when practical, but split specs may be used for technical/source-state isolation;
- one clean user-authored/squashed Git checkpoint per completed batch;
- full final PR CI/non-drift on the exact squashed head.

This cadence must never be used to skip sequential semantic review or copy the control ledger into production.

## Evidence and empty-cell semantics

For `canonical_body` evidence, spans are 1-based poem-body line numbers with 0-based Unicode character offsets. `source_text` must reproduce the frozen source slice exactly. Metadata evidence uses its exact source field/location.

`no_qualifying_evidence_identified` means only that completed review found no qualifying evidence for that dimension in that source record. It never asserts historical absence.

## Validation

At each final batch checkpoint run at minimum:

```bash
python3 scripts/validate_research_r15_dimensions.py --root .
python3 scripts/validate_r15_purananuru_production.py --root .
pytest -q
```

The full PR workflow additionally covers R0/R1/R1.5 validation, deterministic R1/R1.5 regeneration, repository audit, Corpus 1.1.0/Tolkāppiyam non-drift, R1 history preservation and documentation continuity.
