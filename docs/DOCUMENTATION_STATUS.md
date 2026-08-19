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

- records **001–185** form the gap-free production prefix;
- stabilization batch **003–010** is complete;
- regular 25-record batches **011–035**, **036–060**, **061–085**, **086–110**, **111–135**, **136–160**, and **161–185** are complete;
- next record: **186**;
- next planned batch: **186–210**;
- current validation: **185 reviewed / 215 remaining / 3,366 production observations / 224 tests passed**;
- canonical dimension count: **29**.

Records remain separate per-poem JSON files; Git publication and full CI happen once per batch.

Compact reviewed specs are source-first staging artifacts. The core materializer expands them deterministically into canonical records but must not manufacture semantic classifications. Existing R0 evidence may only be attached to a dimension already selected by fresh review, with exact source-text support inside the selected evidence span.

The range-aware driver selects the proper 50-record pre-merge audit-control part per record, including batches crossing an audit boundary. It also preserves frozen source states with no printed source-note block and blank canonical `thurai` values without inventing R0 assertions or semantic classifications.

The materializer now records an explicit discrepancy when a fresh review preserves the same qualifying dimension-code set in canonical order but the old audit lists that same set in a different order. The old audit remains post-review control only and is not normalized to become canonical.

The completed **161–185** review is staged in `161-165.json`, `166-170.json`, `171-175.json`, `176-180.json`, and `181-185.json`. Canonical production remains one `NNN.json` per poem.

Important fidelity/provenance checks from this batch:

- record 174 uses the actual 28-line canonical body boundary; terminal evidence spans end at line 28, not an out-of-range line 29;
- record 173 records the old audit's order-only `BH VEC` versus canonical `VEC BH` difference explicitly without changing the reviewed dimension set;
- record 176 keeps body-level `பாரி` / `பறம்பு` named-entity evidence as `direct_record_review` with `metadata_basis: false`; printed poet/addressee metadata remains a separate metadata-based observation.

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
2. `docs/handover/r15-premerge-audit/` — R1.5 pre-merge audit/coverage/control methodology and results. Old PR #3 merge-hold language there is historical.
3. release documents — immutable release snapshots.
4. durable machine logs — records of the run/head they actually describe.
5. frozen corpus/work metadata and source notes — preservation evidence.

The R1.5 pre-merge sparse ledgers remain useful only as post-review control evidence. They are not the production matrix and must not be copied mechanically.

## Source terminology boundary

`docs/SOURCE_TERMINOLOGY_POLICY.md` remains mandatory.

Classical Tamil social, ritual, learned, occupational, political, kinship and community terms remain in the exact source-supported Tamil form in source-level research descriptions. Do not silently map them to later caste, community, sectarian, hierarchy, or modern identity categories. Later equivalence claims require a separate evidence class and independent provenance.

Source metadata, poem-body evidence, and printed source-note evidence remain distinct. Null/blank canonical metadata remains null/blank. Printed names remain source mentions unless independently resolved.

## Validation policy

R1.5A batch checkpoints must pass:

- exact 29-dimension surface validation;
- Puṟanāṉūṟu production-prefix validation;
- R0/R1/R1.5 validators;
- full regression;
- deterministic R1 and R1.5 regeneration checks;
- repository audit;
- Corpus 1.1.0/Tolkāppiyam non-drift;
- R1 primary-history preservation;
- documentation-status regression checks.

Full PR CI runs once per published batch rather than once per poem. A generated bot commit is not the final checkpoint if the normal PR workflow does not execute on it; finish on a user-authored/squashed head and validate that exact head.

## Phase hold

R1.5A remains the active phase. Continue Puṟanāṉūṟu sequentially from **186**; the next permitted batch is **186–210**. Do not start the Tolkāppiyam production pass until Puṟanāṉūṟu 001–400 is complete and validated. **Do not start R2.**
