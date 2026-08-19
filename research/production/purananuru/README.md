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

Current materialized gap-free prefix: **001–360**.

- benchmark: 001–002;
- stabilization batch: **003–010** complete;
- regular **25-record** semantic batches begin at **011–035** and continue through **336–360**;
- next record: **361**;
- next batch: **361–385**.

Current validated figures: **360 reviewed / 40 remaining / 6,304 production observations / 29 canonical dimensions / 224 tests passed**.

Before record `NNN+1` is read, that record's complete semantic decision state must already be complete. Git publication/materialization may batch already-completed records.

Every record must identify the exact frozen source and R0 snapshot, consider all 29 dimensions, distinguish qualifying evidence from reviewed-empty states, retain exact source Tamil/spans, preserve metadata/body/source-note distinctions, keep printed names unresolved unless separately resolved, preserve damaged/source-lost states without reconstruction, and compare the old audit only after fresh source review.

## Reviewed batch specs and materialization

Compact source-first reviewed specs live under `research/production/purananuru/review-specs/`.

The completed 336–360 publication uses:

- `336-340.json`
- `341-343.json`
- `344-345.json`
- `346-350.json`
- `351-355.json`
- `356-360.json`

All 25 poems were semantically reviewed sequentially and source-first before either old control ledger was opened. The 344–345 mini-batch isolates its composite printed attribution and alternate thinai/thurai source note. A malformed construction-only oversized spec and temporary debug workflow/log were removed and are not part of the durable production state.

The 261–285 and 286–310 batches prove that one contiguous 25-record spec + one materialization cycle is safe when practical. Split specs remain valid when technical/source-state isolation is useful. **This never batches semantic review.**

`scripts/materialize_r15a_purananuru_batch.py` deterministically expands already-reviewed decisions into canonical records. It is not a classifier.

`scripts/materialize_r15a_purananuru_batch_driver.py` is the range-aware source-state compatibility layer. It handles audit-part selection, absent source-note blocks, blank canonical `thurai`, and exact unknown-poet/non-identification metadata without allowing those phrases to become named entities.

Current exact literals handled by the driver remain:

- `பெயர் தெரிந்திலது`
- `பெயர் புலனாகவில்லை`
- `பாடப்பட்டோர் : பெயர்கள் தெரிந்தில`

No new driver literal was required for 344–345. Their frozen `poet_as_printed` remains intact; the reviewed named-entity note distinguishes named poet `அடைநெடுங் கல்வியார்` from explicitly unknown `பாடப்பட்டோன்`.

A pre-existing R0 body assertion may attach only when its type belongs to a dimension already selected by fresh review and its exact source text occurs inside selected evidence.

## Source-state lessons from 336–360

- 336 preserves exact `மறவர்` and `அறன்இலன்` without later identity-system expansion.
- 337 is incomplete/lacunose and is not reconstructed; `சோணாட்டு`, `பாரி`, `பறம்பு` remain unresolved source mentions.
- 338 preserves the printed `சிறப்பு` note around `நெடுவேள் ஆதன்` / `போந்தை` as source-context/TIR evidence distinct from the body.
- 339–340 preserve exact unknown poet `பெயர் தெரிந்திலது`; `named_entities` stays reviewed-empty; 339 preserves exact `கோவலர்`.
- 341 preserves `வாரா உலகம்` as source other-world/death language without later doctrinal expansion.
- 343 records fish-for-rice exchange, ship-borne gold and mountain/sea goods without inferring a wider market system; `குட்டுவன்` / `முசிறி` remain unresolved.
- 344–345 preserve `அடைநெடுங் கல்வியார் பாடப்பட்டோன்: பெயர் தெரிந்திலது` as a named poet plus explicitly unidentified sung person, not one composite identity. Their alternate source-note `வாகை / மூதின் முல்லை` classification is additional TT/TIR and does not overwrite canonical `காஞ்சி / மகட்பாற் காஞ்சி`.
- 346–347 remain incomplete/lacunose and are not reconstructed; 347 keeps `அகுதை`, `கூடல்` unresolved and `நறுங் கள்ளின்` source-bound.
- 348 preserves `பாண் சேரி`, `தண்ணுமை`, `தழும்பன்`, `ஊணூர்` without later community expansion.
- 349 preserves exact `அணங்கு` only as source destructive/sacred-power wording without later deity/doctrine identification.
- 352 preserves `இடையிடை சிதைவுற்ற செய்யுள் இது` and `சிறப்பு: தித்தன் காலத்து உறந்தையின் நெல் வளம்.` without reconstructing damaged lines.
- 353 preserves exact `தொல்குடி`; `பஞ்சியும் களையாப் புண்ணர்` remains source body/care evidence without later community or modern medical-system mapping.
- 355 preserves unknown poet, thurai literally `பெயர் தெரிந்திலது`, and `தோற்றக் கிடையாத போயின செய்யுள் இது.` as source-loss/TIR evidence; no lost text is reconstructed.
- 356 preserves `ஈம விளக்கு`, `சுடலை`, ash/bones, ghost-women imagery and tears as source funerary/death evidence without later doctrinal expansion.
- 358 preserves `தவம்` and canonical `மனையறம், துறவறம்` as source ethical/ascetic vocabulary without importing a later doctrinal system.
- 360 preserves exact `புலையன்` without later caste/community equivalence and keeps cremation/funerary-food context source-bound.

Earlier provenance and terminology guardrails remain binding, including record 176, damaged record 200 and source-lost records 267–268.

## R1.5A cadence

The review is sequential; repository publication is batched.

- benchmark: 001–002;
- completed stabilization batch: **003–010**;
- regular **25-record** semantic batches begin at **011–035** and are complete through **336–360**;
- next batch: **361–385**;
- final Puṟanāṉūṟu batch: **386–400**;
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
