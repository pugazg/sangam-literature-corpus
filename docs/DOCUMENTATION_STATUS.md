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

- records **001–335** form the gap-free production prefix;
- stabilization batch **003–010** is complete;
- regular **25-record** batches **011–035**, **036–060**, **061–085**, **086–110**, **111–135**, **136–160**, **161–185**, **186–210**, **211–235**, **236–260**, **261–285**, **286–310**, and **311–335** are complete;
- next record: **336**;
- next planned batch: **336–360**;
- current validation: **335 reviewed / 65 remaining / 5,866 production observations / 224 tests passed**;
- canonical dimension count: **29**;
- Tolkāppiyam production observation count: **0**.

Normal PR verification workflow `32248997542` is green for the 001–335 verification tree, including R0/R1/R1.5 validators, deterministic regeneration, repository audit, corpus/Tolkāppiyam non-drift and R1 primary-history preservation.

## Publication method

Semantic review remains strictly poem-by-poem, sequential and source-first. The old sparse audit remains post-review control only.

The 261–285 and 286–310 batches proved one contiguous 25-record reviewed spec + one materialization cycle. The 311–335 batch was also fully reviewed across all 25 poems before the audit was opened, but was published as five 5-record specs (`311-315.json` through `331-335.json`) to keep connector writes manageable and to validate record 323's new source-state case in sequence.

This changes only Git/materialization granularity. Split specs do not permit batch semantic guessing, skipped poems, audit-first classification or reduced provenance checking. One contiguous 25-record spec remains preferred when practical.

The core materializer expands already-reviewed decisions deterministically; it must not manufacture classifications. Existing R0 evidence may attach only to a dimension already selected by fresh review with exact source-text support inside selected evidence.

The range-aware driver preserves absent source-note states, blank canonical `thurai`, and exact unknown-poet/non-identification literals while preventing those phrases from becoming person/entity evidence.

Currently recognized exact literals:

- `பெயர் தெரிந்திலது`
- `பெயர் புலனாகவில்லை`
- `பாடப்பட்டோர் : பெயர்கள் தெரிந்தில`

They are restored verbatim into `source_metadata_reviewed.poet_as_printed` after core materialization. This is source-state compatibility, not semantic classification.

## Important fidelity/provenance checks from 311–335

- 311 preserves exact `புலைத்தி` without later identity substitution;
- 312 preserves null thinai/thurai/poet/addressee plus absent source note while classifying the body duty/craft/warfare evidence independently;
- 313 preserves exact `இரவன் மாக்கள்`, `உமணர்` and `உப்பொய் சாகாட்டு` without extrapolating a wider market system;
- 315 keeps printed poet/`பாடப்பட்டோன்` attribution separate from body `நெடுமான் அஞ்சி`;
- 317, 321, 328, 333, 334 and 335 remain incomplete/lacunose and are not reconstructed;
- 319 preserves exact canonical `யாம் க·டு உண்டென` without silent repair;
- 322 preserves `கரும்பின் எந்திரம்` and `கண்படை ஈயா` as source-explicit technology/body-state evidence;
- 323 preserves `பாடப்பட்டோர் : பெயர்கள் தெரிந்தில` and `பாடியவர் பாடப்பட்டோர் : பெயர்கள் தெரிந்தில.` as unresolved attribution; `named_entities` remains reviewed-empty;
- 324 preserves exact `வேட்டுவர்`, `இடையன்`, `பாணர்`;
- 327–328 and 333 preserve exact `பெயர் தெரிந்திலது` without manufacturing entities;
- 329 preserves the `நடுகல்` / `நாட்பலி` / water / ghee-fragrance / smoke memorial ritual sequence without later doctrinal expansion;
- 331 preserves `உறையூர் முது கூற்றனார் எனவும் பாடம்` as TIR and treats `போகுபலி வெண்சோறு` as source offering language only;
- 332 preserves exact `மறவன்`;
- 335 retains only surviving plant names, preserves exact `துடியன், பாணன், பறையன், கடம்பன்`, and treats `கல்லே பரவின் ... நெல்உகுத்துப் பரவும் கடவுளும் இலவே` as the poem's own memorial-worship/deity language rather than a generalized historical absence claim.

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

R1.5A remains active. Continue Puṟanāṉūṟu sequentially from **336**; the next permitted batch is **336–360**. Do not start the Tolkāppiyam production pass until Puṟanāṉūṟu 001–400 is complete and validated. **Do not start R2.**
