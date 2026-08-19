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

- records **001–360** form the gap-free production prefix;
- stabilization batch **003–010** is complete;
- semantic batches through **336–360** are complete;
- next record: **361**;
- next planned batch: **361–385**;
- current validation: **360 reviewed / 40 remaining / 6,304 production observations / 224 tests passed**;
- canonical dimension count: **29**;
- Tolkāppiyam production observation count: **0**.

Normal PR verification workflow `32254779147` is green for the 001–360 verification tree, including R0/R1/R1.5 validators, exact 29-dimension and production-prefix gates, deterministic regeneration, repository audit, Corpus/Tolkāppiyam non-drift and R1 primary-history preservation.

## Publication method

Semantic review remains strictly poem-by-poem, sequential and source-first. The old sparse audit remains post-review control only.

The 336–360 batch was fully reviewed across all 25 poems before either control ledger was opened. Durable publication uses six compact specs:

- `336-340.json`
- `341-343.json`
- `344-345.json`
- `346-350.json`
- `351-355.json`
- `356-360.json`

The 344–345 mini-batch isolates a composite printed attribution plus alternate classification. Construction-only malformed/debug artifacts were removed and are not part of the durable batch state.

This changes only Git/materialization granularity. Split specs do not permit batch semantic guessing, skipped poems, audit-first classification or reduced provenance checking. One contiguous 25-record spec remains preferred when practical.

The core materializer expands already-reviewed decisions deterministically; it must not manufacture classifications. Existing R0 evidence may attach only to a dimension already selected by fresh review with exact source-text support inside selected evidence.

The range-aware driver preserves absent source-note states, blank canonical `thurai`, and exact unknown-poet/non-identification literals while preventing those phrases from becoming person/entity evidence.

Currently recognized exact literals remain:

- `பெயர் தெரிந்திலது`
- `பெயர் புலனாகவில்லை`
- `பாடப்பட்டோர் : பெயர்கள் தெரிந்தில`

No new driver rule was required for 344–345; their frozen composite attribution is preserved intact and semantically scoped in the reviewed observation note.

## Important fidelity/provenance checks from 336–360

- 336 preserves exact `மறவர்` and `அறன்இலன்` without later identity-system expansion;
- 337, 339–341, 346–347 and 352–355 where source damage/lacuna occurs remain source-bounded and are not reconstructed;
- 338 preserves the printed `சிறப்பு` note about `நெடுவேள் ஆதன்` / `போந்தை` as source-context/TIR evidence distinct from the body;
- 339–340 preserve exact `பெயர் தெரிந்திலது` without manufacturing named entities; 339 preserves exact `கோவலர்`;
- 341 preserves `வாரா உலகம்` as source other-world/death language without later doctrinal mapping;
- 343 records fish-for-rice exchange, ship-borne gold and mountain/sea goods without inferring a wider market system;
- 344–345 preserve `அடைநெடுங் கல்வியார் பாடப்பட்டோன்: பெயர் தெரிந்திலது` as named poet plus unknown sung person, not one composite identity; alternate `வாகை / மூதின் முல்லை` remains additional TT/TIR rather than replacing canonical `காஞ்சி / மகட்பாற் காஞ்சி`;
- 348 preserves `பாண் சேரி`, `தண்ணுமை`, `தழும்பன்`, `ஊணூர்` source-bounded;
- 349 preserves exact `அணங்கு` without later deity/doctrine identification;
- 352 preserves explicit `இடையிடை சிதைவுற்ற செய்யுள் இது` and the printed `சிறப்பு` note without reconstructing damaged lines;
- 353 preserves exact `தொல்குடி` and `பஞ்சியும் களையாப் புண்ணர்` without later community/medical-system mapping;
- 355 preserves poet and thurai `பெயர் தெரிந்திலது` plus `தோற்றக் கிடையாத போயின செய்யுள் இது.` as source-loss/TIR evidence, with no reconstruction;
- 356 preserves `ஈம விளக்கு`, `சுடலை`, ash/bones, ghost-women imagery and tears as source funerary/death evidence;
- 358 preserves `தவம்` and canonical `மனையறம், துறவறம்` without importing a later doctrinal system;
- 360 preserves exact `புலையன்` without later caste/community equivalence and keeps the funerary-food context source-bound.

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

R1.5A remains active. Continue Puṟanāṉūṟu sequentially from **361**; the next permitted batch is **361–385**. Do not start the Tolkāppiyam production pass until Puṟanāṉūṟu 001–400 is complete and validated. **Do not start R2.**
