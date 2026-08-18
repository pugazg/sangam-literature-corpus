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

Current materialized state:

- records **001–035** form the gap-free production prefix;
- stabilization batch **003–010** is complete;
- first regular 25-record batch **011–035** is complete;
- next record: **036**;
- next planned batch: **036–060**.

The operational cadence is now 25-record batches after the completed 003–010 stabilization batch. Records remain separate per-poem JSON files; Git publication and full CI happen once per batch.

Compact reviewed specs are source-first staging artifacts. The materializer expands them deterministically into the canonical records but must not manufacture semantic classifications. Existing R0 evidence may only be attached to a dimension that has already been selected by fresh review, with exact source-text support inside the selected evidence span.

The materialization workflow processes only review-spec files changed in its triggering commit, preventing later tooling changes from silently rewriting completed batches.

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

Classical Tamil social, ritual, learned, occupational, political, kinship and community terms remain in the exact source-supported Tamil form in source-level research descriptions. Later equivalence claims are separate evidence classes with independent provenance.

## Validation policy

R1.5A batch checkpoints must pass:

- exact 29-dimension surface validation;
- Puṟanāṉūṟu production-prefix validation;
- R0/R1/R1.5 validators;
- full regression;
- deterministic regeneration checks;
- repository audit;
- Corpus 1.1.0/Tolkāppiyam non-drift;
- R1 primary-history preservation;
- documentation-status regression checks.

Full PR CI runs once per published batch rather than once per poem. A generated bot commit is not the final checkpoint if the normal PR workflow does not execute on it; finish on a user-authored/squashed head and validate that exact head.

## Phase hold

R1.5A remains the active phase until its production-review boundary is completed/readied and the user explicitly authorizes a later transition. **Do not start R2.**
