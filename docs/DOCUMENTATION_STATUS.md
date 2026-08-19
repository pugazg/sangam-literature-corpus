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

- records **001–260** form the gap-free production prefix;
- stabilization batch **003–010** is complete;
- regular 25-record batches **011–035**, **036–060**, **061–085**, **086–110**, **111–135**, **136–160**, **161–185**, **186–210**, **211–235**, and **236–260** are complete;
- next record: **261**;
- next planned batch: **261–285**;
- current validation: **260 reviewed / 140 remaining / 4,628 production observations / 224 tests passed**;
- canonical dimension count: **29**.

Records remain separate per-poem JSON files; Git publication and full CI happen once per batch.

Compact reviewed specs are source-first staging artifacts. The core materializer expands them deterministically into canonical records but must not manufacture semantic classifications. Existing R0 evidence may only be attached to a dimension already selected by fresh review, with exact source-text support inside the selected evidence span.

The range-aware driver selects the proper 50-record pre-merge audit-control part per record, including batches crossing an audit boundary. It preserves absent source-note states, blank canonical `thurai`, and exact unknown poet attribution `பெயர் தெரிந்திலது` as reviewed metadata while preventing that phrase from being treated as a person/entity. These are source-state compatibility rules, not semantic classification.

The completed **236–260** review is staged in `236-240.json`, `241-245.json`, `246-250.json`, `251-255.json`, and `256-260.json`. Canonical production remains one `NNN.json` per poem.

Important fidelity/provenance checks from this batch:

- record 242 preserves source-note alternate attribution `கடவாயில் நல்லாதனார் பாடியது என்பதும் பாடம்` as TIR rather than normalized poet metadata;
- record 244 remains an incomplete/lacunose fragment with null thinai/thurai/poet/addressee metadata; only surviving source evidence is classified and no death is reconstructed from title/tradition;
- record 249 preserves its lacuna and explicit Nacciṉārkkiṉiyar/Tolkāppiyam source-note citation as textual/intertextual evidence only; the citation does not auto-classify the poem;
- records 251–252 preserve `தாபத வாகை` source signs and exact `வேட்டுவன்` without later religious-order mapping;
- records 256–257 preserve literal `பெயர் தெரிந்திலது` in reviewed metadata while keeping `named_entities` reviewed-empty because the phrase explicitly denotes unknown authorship;
- record 259 preserves exact `மறவர்` and comparison-term `புலைத்தி` without later caste/community substitution;
- record 260 preserves canonical and source-note alternate `திணை/துறை` readings separately as TT/TIR evidence without normalization.

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

Source metadata, poem-body evidence, and printed source-note evidence remain distinct. Null/blank canonical metadata remains null/blank. Printed names remain source mentions unless independently resolved. An explicit unknown-attribution phrase is metadata about non-identification, not itself an identity.

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

R1.5A remains the active phase. Continue Puṟanāṉūṟu sequentially from **261**; the next permitted batch is **261–285**. **Records 267–268 are source-lost and must remain unreconstructed.** Do not start the Tolkāppiyam production pass until Puṟanāṉūṟu 001–400 is complete and validated. **Do not start R2.**
