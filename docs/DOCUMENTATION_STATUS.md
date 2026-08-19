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

- records **001–285** form the gap-free production prefix;
- stabilization batch **003–010** is complete;
- regular 25-record batches **011–035**, **036–060**, **061–085**, **086–110**, **111–135**, **136–160**, **161–185**, **186–210**, **211–235**, **236–260**, and **261–285** are complete;
- next record: **286**;
- next planned batch: **286–310**;
- current validation: **285 reviewed / 115 remaining / 5,024 production observations / 224 tests passed**;
- canonical dimension count: **29**;
- Tolkāppiyam production observation count: **0**.

Records remain separate per-poem JSON files. The completed 261–285 review is staged in one contiguous spec: `research/production/purananuru/review-specs/261-285.json`.

## Low-latency publication method

The 261–285 batch proved that a complete 25-record batch can be staged as one contiguous reviewed spec and materialized in one workflow cycle. This is now the preferred default when the entire batch can be completed in one session.

This optimization changes only Git/materialization granularity. Every poem must still be read sequentially and source-first, all 29 dimension decisions must be complete before moving to the next poem, and the old sparse audit remains post-review control only. Split specs remain valid when a session cannot finish a full batch or when a source-state issue genuinely requires isolation.

After one-pass materialization, use targeted generated-record checks for source-loss, lacunae, source metadata/body boundaries and substantive audit differences. Then obtain the actual observation count from normal PR verification, update docs once, squash to one clean user-authored checkpoint and run exact-head final CI once.

Compact reviewed specs are source-first staging artifacts. The core materializer expands them deterministically into canonical records but must not manufacture semantic classifications. Existing R0 evidence may only be attached to a dimension already selected by fresh review, with exact source-text support inside the selected evidence span.

The range-aware driver selects the proper 50-record pre-merge audit-control part per record, including batches crossing an audit boundary. It preserves absent source-note states, blank canonical `thurai`, and exact unknown poet attribution `பெயர் தெரிந்திலது` as reviewed metadata while preventing that phrase from being treated as a person/entity. These are source-state compatibility rules, not semantic classification.

## Important fidelity/provenance checks from 261–285

- record 261 preserves `நடுகல்`, memorial naming/adornment, cattle recovery, lament, shorn hair and loss of ornaments as source-explicit memorial/mourning evidence;
- record 262 preserves `உண்டாட்டு (தலை தோற்றமுமாம்)` as alternate-thurai/classification evidence rather than normalizing it;
- record 263 preserves `தொழாதனை கழிதல் ஓம்புமதி` as memorial-stone honoring/worship and leaves bare `பாடியவர் / பாடப்பாட்டோர்` source-note labels unresolved;
- records **267–268 remain source-lost/unreconstructed**: body unavailable, thinai/thurai/poet/addressee null, only work-level `literary_domain` qualifies, and all other 28 dimensions are reviewed-empty with explicit no-reconstruction notes;
- record 272 intentionally leaves `death_mourning_memory` reviewed-empty because the body does not explicitly state death; metadata `செருவிடை வீழ்தல்` remains TT evidence only;
- record 281 preserves protective ritual/performance/wound evidence (`வேம்பு`, யாழ், ஐயவி, ஆம்பல், `காஞ்சி`, bells/smoke) without later ritual/medical-system mapping;
- record 282 remains incomplete/lacunose with null thinai/thurai; `திணையும் துறையும் தெரிந்தில.` is preserved as classification-uncertainty TIR rather than reconstructed TT;
- record 283 remains incomplete/lacunose and preserves exact `கோசர்` plus `பாண்பாட்டு (பாடாண் பாட்டும் ஆம்)` as an alternate-thurai signal without later identity/classification normalization;
- record 285 remains incomplete/lacunose; its camp, performance, warfare, wound, city/village, honor and village-grant evidence is retained without inventing a completed death claim.

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

These remain truthful records and must not be rewritten merely to imitate current state:

1. `docs/history/` — superseded prompts and phase snapshots.
2. `docs/handover/r15-premerge-audit/` — R1.5 pre-merge audit/coverage/control methodology and results.
3. release documents — immutable release snapshots.
4. durable machine logs — records of the run/head they actually describe.
5. frozen corpus/work metadata and source notes — preservation evidence.

The R1.5 pre-merge sparse ledgers remain useful only as post-review control evidence. They are not the production matrix and must not be copied mechanically.

## Source terminology boundary

`docs/SOURCE_TERMINOLOGY_POLICY.md` remains mandatory.

Classical Tamil social, ritual, learned, occupational, political, kinship and community terms remain in the exact source-supported Tamil form in source-level research descriptions. Do not silently map them to later caste, community, sectarian, hierarchy, deity, taxonomy, or modern identity categories. Later equivalence claims require a separate evidence class and independent provenance.

Source metadata, poem-body evidence and printed source-note evidence remain distinct. Null/blank canonical metadata remains null/blank. Printed names remain source mentions unless independently resolved. An explicit unknown-attribution phrase is metadata about non-identification, not itself an identity.

## Validation policy

R1.5A final batch checkpoints must pass:

- exact 29-dimension surface validation;
- Puṟanāṉūṟu production-prefix validation;
- R0/R1/R1.5 validators;
- full regression;
- deterministic R1 and R1.5 regeneration checks;
- repository audit;
- Corpus 1.1.0/Tolkāppiyam non-drift;
- R1 primary-history preservation;
- documentation continuity.

A generated bot commit is not the final checkpoint. Finish on one user-authored/squashed head parented by the previous green checkpoint and validate that exact head.

## Phase hold

R1.5A remains active. Continue Puṟanāṉūṟu sequentially from **286**; the next permitted batch is **286–310**. Prefer one contiguous 25-record reviewed spec and one materialization cycle when the whole batch can be completed in-session. Do not start the Tolkāppiyam production pass until Puṟanāṉūṟu 001–400 is complete and validated. **Do not start R2.**
