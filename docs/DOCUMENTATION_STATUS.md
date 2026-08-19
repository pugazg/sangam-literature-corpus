# Documentation status — R1.5A production review

## Purpose

This file defines current operational documentation after the authorized R1.5 merge and distinguishes it from historical/control material.

## Live phase state

- repository: `pugazg/sangam-literature-corpus`
- default branch: `main`
- R1.5 merge commit on `main`: `d82f9c78f27f9c9daf8fbb913d01ddfb29bddba1`
- PR #3: merged; historical R1.5 proposal
- active research branch: `research/classical-tamil-concept-matrix-r1.5a`
- active PR: #4, draft/unmerged R1.5A proposal
- current phase: R1.5A production review
- R2: blocked / not started

R1.5A keeps concept/observation schema `0.3.0`. It changes production-review cadence, not the evidence standard or phase schema.

## Current production state

The exact 29-dimension production vocabulary/schema remains aligned and validated.

Puṟanāṉūṟu production progress is the longest gap-free prefix under `research/production/purananuru/records/`.

Current materialized and validated state:

- records **001–385** form the gap-free production prefix;
- stabilization batch **003–010** is complete;
- regular **25-record** semantic batches begin at **011–035** and are complete through **361–385**;
- next record: **386**;
- final Puṟanāṉūṟu batch: **386–400**;
- current validation: **385 reviewed / 15 remaining / 6,819 production observations / 224 tests passed**;
- canonical dimension count: **29**;
- Tolkāppiyam production observation count: **0**.

Normal PR verification workflow `32261366327` is green for the 001–385 verification tree, including R0/R1/R1.5 validators, exact 29-dimension and production-prefix gates, deterministic regeneration, repository audit, Corpus/Tolkāppiyam non-drift and R1 primary-history preservation.

## Publication method

Semantic review remains strictly poem-by-poem, sequential and source-first. The old sparse audit remains post-review control only.

The 361–385 batch was fully reviewed across all 25 poems before the 351–400 control ledger was opened. Durable publication uses five compact specs:

- `361-365.json`
- `366-370.json`
- `371-375.json`
- `376-380.json`
- `381-385.json`

This changes only Git/materialization granularity. Split specs do not permit batch semantic guessing, skipped poems, audit-first classification or reduced provenance checking. One contiguous 25-record spec remains preferred when practical.

The core materializer expands already-reviewed decisions deterministically; it must not manufacture classifications. Existing R0 evidence may attach only to a dimension already selected by fresh review with exact source-text support inside selected evidence.

The range-aware driver preserves absent source-note states, blank canonical `thurai`, and exact non-identification metadata while preventing those phrases from becoming person/entity evidence.

Currently recognized unknown-poet literals are:

- `பெயர் தெரிந்திலது`
- `பெயர் புலனாகவில்லை`
- `பாடப்பட்டோர் : பெயர்கள் தெரிந்தில`
- `, பாடப்பட்டோர், திணை, துறை தெரிந்தில`

The driver also suppresses and restores addressee `பெயர் தெரிந்திலது` during named-entity linking. These are source-state compatibility rules, not semantic classification or identity resolution.

## Important fidelity/provenance checks from 361–385

- 361 preserves null thinai/thurai/addressee plus frozen non-identification poet/source-note wording; no TT or named entity is manufactured.
- 362 preserves exact `அந்தணாளர்`, `நான்மறை`, `அறம்`, `பொருள்` without later identity/doctrinal mapping.
- 363 preserves exact `இழி பிறப்பினோன்` as source social/funerary wording only.
- 366 remains incomplete/lacunose; `தருமபுத்திரன்` is an unresolved printed addressee.
- 367 preserves `நோற்றோர்`, `பார்ப்பார்`, `நல்வினை`, `இருபிறப்பாளர்`, `முத்தீ`; its `சிறப்பு` note is source-context/TIR rather than external history.
- 368 keeps the source statement that the fallen ruler was still alive as source-reported battlefield-loss context, not verified historical death.
- 370–371 remain incomplete/lacunose and are not reconstructed; 371 `பறை` remains the printed instrument term.
- 372 preserves `மறக்கள வேள்வி`, `மாமறி பிண்டம்`, `வாலுவன்`, `வதுவை விழவு`, `பூதநீர்` without later doctrinal expansion.
- 373 keeps canonical `வாகை / மறக்களவழி` and source-note `ஏர்க்கள உருவகமும் ஆம்` as additional TT/TIR without overwrite.
- 374 preserves `புலிப்பற் றாலி` source-bound.
- 375 preserves `ஏரின் வாழ்நர்`, `குடிமுறை` without later community substitution.
- 376/379 preserve `எந்தை` as father-like patron language, not genealogy; 379 `இலங்கை` remains unresolved.
- 377 treats gem/gold/pearl as gifts, not inferred transactional long-distance trade.
- 378 preserves `தென் பரதவர்`, `வட வடுகர்`; its Rama–Sita narrative comparison is intertextual evidence, not historical verification.
- 380 preserves null metadata, absent source note and lacunae without reconstruction.
- 381 separates father-like `எந்தை` from explicit `கரும்பன் ஊரன் காதல் மகனே` kinship evidence.
- 383 preserves addressee `பெயர் தெரிந்திலது`; body `அவியன்` remains separately unresolved and source-note `கொள்ளலும் பொருந்தும்` remains conjectural TIR.
- 383–385 preserve `வெள்ளி` as source celestial/prognostic/time wording without modern astronomical equivalence or validated causal weather theory.
- 384 preserves exact `உழவர்`.
- 385 keeps `காவிரி அணையும் தாழ்நீர்ப் படப்பை` / rice cultivation as source water-management/agricultural evidence and printed names unresolved.

Earlier source-terminology and provenance guardrails remain binding.

## Current operational documents

The current authority set is:

- `README.md`
- `PROJECT_GUIDELINES.md`
- `PROJECT_HANDOVER.md`
- `NEXT_CHAT_PROMPT.md`
- `docs/DOCUMENTATION_STATUS.md`
- `docs/SOURCE_TERMINOLOGY_POLICY.md`
- `docs/CLASSICAL_TAMIL_RESEARCH_MATRIX.md`
- `docs/classical-tamil-research-layer.md`
- `docs/handover/r15a-production-review/README.md`
- `research/production/purananuru/README.md`
- `research/audits/r15-premerge/dimensions.json`
- `research/controlled-vocabularies/concept-dimensions-r15.json`
- `research/README.md`

## Historical / control documents

Historical handovers, release snapshots, durable machine logs and the R1.5 pre-merge audit remain truthful records of their own boundaries and must not be rewritten merely to imitate current state. The old sparse ledgers are post-review control evidence, not the production matrix.

## Source terminology boundary

`docs/SOURCE_TERMINOLOGY_POLICY.md` remains mandatory.

Classical Tamil social, ritual, learned, occupational, political, kinship and community terms remain in the exact source-supported Tamil form. Do not silently map them to later caste, community, sectarian, hierarchy, deity, taxonomy or modern identity categories. Source metadata, poem-body evidence and printed source-note evidence remain distinct. Null/blank canonical metadata remains null/blank. Printed names remain source mentions unless independently resolved. An explicit unknown-attribution phrase is metadata about non-identification, not itself an identity.

## Validation policy

R1.5A final batch checkpoints must pass exact 29-dimension surface validation, Puṟanāṉūṟu production-prefix validation, R0/R1/R1.5 validators, full regression, deterministic R1/R1.5 regeneration, repository audit, Corpus/Tolkāppiyam non-drift, R1 primary-history preservation and documentation continuity.

A generated bot commit is not the final checkpoint. Finish on one user-authored/squashed head parented by the previous green checkpoint and validate that exact head.

## Phase hold

R1.5A remains active. The next permitted Puṟanāṉūṟu activity is the final **386–400** batch. Do not start the Tolkāppiyam production pass until Puṟanāṉūṟu 001–400 is complete and validated. **Do not start R2.**
