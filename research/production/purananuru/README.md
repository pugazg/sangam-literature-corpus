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

Current materialized gap-free prefix: **001–260**.

- benchmark: 001–002;
- stabilization batch: **003–010** complete;
- regular 25-record batches: **011–035**, **036–060**, **061–085**, **086–110**, **111–135**, **136–160**, **161–185**, **186–210**, **211–235**, **236–260** complete;
- next record: **261**;
- next batch: **261–285**.

Current validated figures: **260 reviewed / 140 remaining / 4,628 production observations / 29 canonical dimensions / 224 tests passed**.

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

Completed 236–260 specs are:

- `236-240.json`
- `241-245.json`
- `246-250.json`
- `251-255.json`
- `256-260.json`

Spec splitting is only a compact staging detail; canonical production remains one separate `NNN.json` per poem and each completed 25-record activity is published as one final checkpoint.

`scripts/materialize_r15a_purananuru_batch.py` deterministically expands already-reviewed semantic decisions into canonical production records. It computes evidence spans, source/R0 blob identities, deterministic observation IDs, dimension-review rows, and post-review audit discrepancies.

`scripts/materialize_r15a_purananuru_batch_driver.py` is the range-aware orchestration/source-state compatibility layer. It selects the correct 50-record audit-control TSV for each record, safely handles a reviewed spec crossing an audit-part boundary, accepts a genuinely absent printed source-note block, preserves a blank canonical `thurai` without inventing a `TURAI_VALUE` assertion, and preserves exact `பெயர் தெரிந்திலது` unknown-poet metadata while excluding that non-identity phrase from named-entity linking. These compatibility rules only represent frozen source states; they do not classify semantics.

Neither script is an automatic semantic classifier. A pre-existing R0 body assertion may be auto-attached only when its assertion type belongs to the dimension already selected by fresh review and its exact source text occurs inside the already-selected source evidence.

The materializer records audit differences explicitly after fresh review. An order-only difference between canonical dimension order and the old control ledger is recorded as a discrepancy without changing the fresh semantic set or rewriting the control audit.

## Source-state lessons from 236–260

- Record 236 preserves `கேண்மை`, `நட்பு`, `குறவர்` and body/source-note `பாரி` provenance without later identity expansion.
- Record 237 keeps deceased `வெளிமான்` distinct from addressee `இளவெளிமான்`; `கூற்றம்` / `ஊழ்` remain source language.
- Record 238 preserves the source-note quotation/comment on `கண்ணில் ஊமன் கடற் பட்டாங்கு` as textual evidence separate from the body.
- Record 241 preserves `வச்சிரத் தடக்கை நெடியோன் கோயிலுள்` without later named-deity identification.
- Record 242 preserves source-note alternate attribution `கடவாயில் நல்லாதனார் பாடியது என்பதும் பாடம்` as textual-variant evidence without replacing canonical poet metadata.
- Record 243 treats `நடுக்குற்று` / `சிலசொல்` as aging/body evidence rather than manufacturing death from the `கையறுநிலை` label.
- Record 244 is incomplete/lacunose with null thinai/thurai/poet/addressee metadata. Only surviving `பாணர்`, `விறலியர்`, `இரவல் மாக்கள்`, `வண்டு`, and `தொடி` evidence is classified; title/tradition does not reconstruct death.
- Records 246–247 preserve exact `உயவற் பெண்டிரேம்`, `கணவன்`, `கானவர்`, `அணங்குடை முன்றில்`, `கொழுநன்`, and `இன்னுயிர் நடுங்கும்` without later named-practice, legal-status or sectarian inference.
- Record 249 preserves incomplete/lacuna state, alternate poet attribution, and the printed Nacciṉārkkiṉiyar/Tolkāppiyam citation as TIR only; Tolkāppiyam does not auto-classify the poem.
- Records 251–252 preserve source signs of `தாபத வாகை`, including `புரிசடை` / `சடை`, fire, plant gathering and exact `வேட்டுவன்`, without later religious-order mapping.
- Record 254 preserves exact `என் மகன்`, `அன்னை`, `கிளை`, and `மள்ள`.
- Record 255 preserves `அறனில் கூற்றே` without later deity mapping.
- Records 256–257 preserve literal `பெயர் தெரிந்திலது` in `source_metadata_reviewed.poet_as_printed` while `named_entities` remains reviewed-empty. The phrase denotes unknown attribution and is not itself a person/entity.
- Record 259 preserves exact `மறவர்` and comparison-term `புலைத்தி` without later caste/community substitution.
- Record 260 preserves canonical `கரந்தை (பாடாண் திணையுமாம்) / கையறுநிலை செருவிடை வீழ்தல்` plus printed source-note alternatives `கையறு நிலையுமாம்`, `பாண்பாட்டுமாம்`, and `பாடாண் பாட்டுமாம்` as separate TT/TIR evidence without normalization.

Earlier provenance and terminology guardrails remain binding, including record 176 and all 186–235 source-state lessons.

## R1.5A cadence

The review is sequential; repository publication is batched.

- benchmark: 001–002;
- completed stabilization batch: **003–010**;
- completed regular batches: **011–035**, **036–060**, **061–085**, **086–110**, **111–135**, **136–160**, **161–185**, **186–210**, **211–235**, **236–260**;
- next batch: **261–285**;
- subsequent cadence: **286–310, 311–335, ...**;
- final batch ends exactly at 400;
- one deterministic multi-file Git checkpoint per completed batch;
- full PR CI/non-drift once per published batch, not once per poem;
- if the active work session cannot complete a planned batch, checkpoint the completed contiguous prefix.

**Records 267–268 are source-lost and must remain unreconstructed during the 261–285 batch.**

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
