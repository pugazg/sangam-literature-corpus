# Documentation status — R1.5A production review

## Purpose

This file defines current operational documentation after the authorized R1.5 merge and distinguishes it from historical/control material.

## Live phase state

- repository: `pugazg/sangam-literature-corpus`
- default branch: `main`
- R1.5 merge commit on `main`: `d82f9c78f27f9c9daf8fbb913d01ddfb29bddba1`
- PR #3: merged; historical R1.5 proposal
- active research branch: `research/classical-tamil-concept-matrix-r1.5a`
- current phase: R1.5A production review
- R2: blocked / not started

R1.5A keeps concept/observation schema `0.3.0`. It changes the operational cadence for the production review; it does not open R2.

## Current production state

The exact 29-dimension production vocabulary/schema has already been aligned and validated.

Puṟanāṉūṟu production progress is the longest gap-free prefix under `research/production/purananuru/records/`.

At R1.5A start:

- 001 complete
- 002 complete
- 003 next

The new cadence is 003–010 as the stabilization batch, then 25-record batches. Records remain separate per-poem JSON files; Git publication and full CI happen once per batch.

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

R1.5A batch commits must pass:

- exact 29-dimension surface validation;
- Puṟanāṉūṟu production-prefix validation;
- R0/R1/R1.5 validators;
- full regression;
- deterministic regeneration checks;
- repository audit;
- Corpus 1.1.0/Tolkāppiyam non-drift;
- R1 primary-history preservation;
- documentation-status regression checks.

Full PR CI runs once per published batch rather than once per poem.

## Phase hold

R1.5A remains the active phase until its production-review boundary is completed/readied and the user explicitly authorizes a later transition. **Do not start R2.**
