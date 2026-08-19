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

Current materialized gap-free prefix: **001–385**.

- benchmark: 001–002;
- stabilization batch: **003–010** complete;
- regular **25-record** semantic batches begin at **011–035** and are complete through **361–385**;
- next record: **386**;
- final Puṟanāṉūṟu batch: **386–400**.

Current validated figures: **385 reviewed / 15 remaining / 6,819 production observations / 29 canonical dimensions / 224 tests passed**.

Before record `NNN+1` is read, that record's complete semantic decision state must already be complete. Git publication/materialization may batch already-completed records.

Every record must identify the exact frozen source and R0 snapshot, consider all 29 dimensions, distinguish qualifying evidence from reviewed-empty states, retain exact source Tamil/spans, preserve metadata/body/source-note distinctions, keep printed names unresolved unless separately resolved, preserve damaged/source-lost states without reconstruction, and compare the old audit only after fresh source review.

## Reviewed batch specs and materialization

Compact source-first reviewed specs live under `research/production/purananuru/review-specs/`.

The completed 361–385 publication uses:

- `361-365.json`
- `366-370.json`
- `371-375.json`
- `376-380.json`
- `381-385.json`

All 25 poems were semantically reviewed sequentially/source-first before the 351–400 control ledger was opened. The five-spec publication only isolates technical/source-state boundaries; **this never batches semantic review**.

The 261–285 and 286–310 batches prove one contiguous 25-record spec + one materialization cycle is safe when practical. Split specs remain valid when technical/source-state isolation is useful.

`scripts/materialize_r15a_purananuru_batch.py` deterministically expands already-reviewed decisions into canonical records. It is not a classifier.

`scripts/materialize_r15a_purananuru_batch_driver.py` is the range-aware source-state compatibility layer. It handles audit-part selection, absent source-note blocks, blank canonical `thurai`, and exact non-identification metadata without allowing those phrases to become named entities.

Current unknown-poet literals handled by the driver are:

- `பெயர் தெரிந்திலது`
- `பெயர் புலனாகவில்லை`
- `பாடப்பட்டோர் : பெயர்கள் தெரிந்தில`
- `, பாடப்பட்டோர், திணை, துறை தெரிந்தில`

The driver also suppresses and restores addressee `பெயர் தெரிந்திலது` during core named-entity linking. These are source-state compatibility rules only.

A pre-existing R0 body assertion may attach only when its type belongs to a dimension already selected by fresh review and its exact source text occurs inside selected evidence.

## Source-state lessons from 361–385

- 361 preserves null thinai/thurai/addressee and frozen non-identification poet/source-note wording; no TT classification or named entity is manufactured.
- 362 preserves exact `அந்தணாளர்`, `நான்மறை`, `அறம்`, `பொருள்` without later identity/doctrinal expansion.
- 363 preserves exact `இழி பிறப்பினோன்` only as source social/funerary wording.
- 366 remains incomplete/lacunose; `தருமபுத்திரன்` stays an unresolved printed addressee.
- 367 preserves `நோற்றோர்`, `பார்ப்பார்`, `நல்வினை`, `இருபிறப்பாளர்`, `முத்தீ`; its three-ruler `சிறப்பு` is source-context/TIR, not verified external history.
- 368 preserves the source statement that the fallen ruler was still alive as source-reported battlefield-loss context, not verified historical death.
- 370–371 remain incomplete/lacunose and are not reconstructed; 371 `பறை` is retained as the printed instrument term.
- 372 preserves `மறக்கள வேள்வி`, `மாமறி பிண்டம்`, `வாலுவன்`, `வதுவை விழவு`, `பூதநீர்` as source battle-ritual vocabulary without later doctrinal equivalence.
- 373 keeps canonical `வாகை / மறக்களவழி`; printed `ஏர்க்கள உருவகமும் ஆம்` is additional TT/TIR and does not overwrite metadata.
- 374 preserves `புலிப்பற் றாலி` as source adornment wording.
- 375 preserves `ஏரின் வாழ்நர்`, `குடிமுறை` without later community substitution.
- 376 and 379 keep `எந்தை` as father-like patron language rather than genealogy; 379 `இலங்கை` remains unresolved.
- 377 treats mountain gem, sea gold and pearl as gifts rather than inferred transactional long-distance trade.
- 378 preserves exact `தென் பரதவர்`, `வட வடுகர்`; the Rama–Sita–`அரக்கன்`–monkey comparison is narrative intertext, not historical verification.
- 380 preserves null thinai/thurai/poet/addressee, absent source note and lacunae without reconstruction.
- 381 distinguishes father-like `எந்தை` from explicit `கரும்பன் ஊரன் காதல் மகனே` kinship evidence.
- 383 restores addressee `பெயர் தெரிந்திலது`; body `அவியன்` remains separately unresolved and source-note `கொள்ளலும் பொருந்தும்` remains conjectural TIR.
- 383–385 preserve `வெள்ளி` only as source celestial/prognostic/time wording without modern astronomical equivalence or validated causal weather theory.
- 384 preserves exact `உழவர்`.
- 385 keeps `காவிரி அணையும் தாழ்நீர்ப் படப்பை` / rice cultivation as source water-management/agricultural evidence and printed names unresolved.

Earlier provenance and terminology guardrails remain binding, including record 176, damaged record 200 and source-lost records 267–268.

## R1.5A cadence

The review is sequential; repository publication is batched.

- benchmark: 001–002;
- completed stabilization batch: **003–010**;
- regular **25-record** semantic batches begin at **011–035** and are complete through **361–385**;
- final Puṟanāṉūṟu batch: **386–400**;
- final batch ends exactly at 400;
- the final batch has 15 records but still uses the same poem-by-poem source-first semantic-review standard;
- split specs may be used for technical/source-state isolation;
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
