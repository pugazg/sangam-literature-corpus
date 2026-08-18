# Sangam Literature Corpus — Project Handover

## Authoritative current state

Repository: `pugazg/sangam-literature-corpus`

Default branch: `main`

Active research branch: `research/classical-tamil-concept-matrix-r1.5`

Active pull request: **PR #3** — R1.5 Classical Tamil Concept Matrix Foundation.

**PR #3 is to remain open, draft, and unmerged until the user explicitly authorizes merge. R2 is blocked and has not started; do not start R2 before that authorization and a fresh inspection of live `main`.**

At the documentation audit, GitHub exposes only `main` and the R1.5 research branch. Earlier R0/R1 branches were deleted after their work was preserved. Do not recreate or depend on those deleted branches.

## Frozen corpus

Current release: **Classical Tamil Corpus 1.1.0**.

- 28 frozen works
- 7,234 canonical records
- 5,632 poem records
- 1,602 Tolkāppiyam நூற்பா
- fingerprint: `4ca530d3a836341b5abaa395af97cf7307529ced04dd40dec17b1a010949abca`
- release content commit: `89e75678b4c35401801a0052ecb8a495d1805dd5`
- release checkpoint commit: `51c65b36d07ecf604c11d8cc6399ad40ab7e7086`
- tag: `classical-tamil-corpus-v1.1.0`

The preservation layer is frozen. R1.5 documentation/research changes must not alter canonical corpus/source/apparatus release content.

## Research identity

### R0 — preserved evidence schema `0.1.0`

- assertions: 2,867
- literary-body candidates: 285
- pilot surface-form entities: 43
- relationships: 51
- assertion evidence class: `SOURCE_EXPLICIT`
- external-historical assertions: 0
- interpretation assertions: 0

R0 originated against Corpus 1.0.0 and was reconciled byte-identically onto the 1.1.0 repository base. Its original assertion identity/provenance remains preserved.

### R1 — preserved workflow schema `0.2.0`

- append-only review events: 8
- entity-resolution decisions: 3
- reviewed export rows: 8
- verified historical identities: 0

R1 is complete and merged into `main`. Review histories remain append-only.

### R1.5 — current concept schema `0.3.0`

R1.5 introduces:

- 36 concept definitions;
- explicit classification-basis vocabulary;
- concept-evidence policies;
- Akam/Puram foundation;
- seven tiṇai categories;
- first-class tuṟai states;
- five landscape concept families;
- named-entity families;
- lived-life dimensions;
- a separate Tolkāppiyam grammatical/poetics concept-evidence contract;
- a bounded Puṟanāṉūṟu production pilot of 8 provenance-bearing observations across 6 records.

All 8 pilot observations remain `SOURCE_EXPLICIT` and `reviewed`. There are no external-historical or interpretive pilot observations and no verified historical identities.

`இறைவன்` and `ஆய்` remain generic ruler-role observations with unresolved historical identity.

## Exhaustive R1.5 pre-merge audit

The bounded pilot proved the schema but did not prove semantic coverage of every record. The merge boundary was therefore reopened for exhaustive review.

Completed audit boundary:

### Puṟanāṉūṟu

- 400 / 400 records read sequentially;
- all 29 controlled dimensions considered for every record;
- eight 50-record sparse TSV ledger parts;
- record 200 remains damaged/unreconstructed;
- records 267–268 remain source-lost/unreconstructed;
- empty cells never mean historical absence.

### Tolkāppiyam

- 27 / 27 இயல் reviewed;
- 1,602 / 1,602 நூற்பா read in context;
- all 29 dimensions considered;
- formal crosswalk covers all 29 dimensions at unequal depth;
- automatic Tolkāppiyam → Sangam poem classification remains disabled.

The audit ledger records review coverage and qualifying dimensions. It is not itself a bulk production-observation dataset.

## Source terminology rule

`docs/SOURCE_TERMINOLOGY_POLICY.md` is mandatory.

Retain the exact Tamil term printed by the relevant source. For example, மரபியல் நூற்பா 71 uses `அந்தணர்`, while நூற்பா 72 uses `அரசர்`. Do not silently replace source terms with later caste, sectarian, modern-community, hierarchy, or external-influence identities.

Any later historical equivalence claim must be a separately classified external-evidence or interpretive assertion with independent provenance.

## Validation state

The R1.5 PR workflow has passed the exhaustive matrix validator, complete regression suite, R1/R1.5 deterministic-regeneration checks, repository audit, Corpus 1.1.0/Tolkāppiyam non-drift, and R1 primary-history non-mutation on the validated pre-documentation head.

Documentation cleanup is intentionally CI-validated again after changes. The live PR check state is authoritative; do not treat an older embedded workflow ID as permanent “final” status.

## Current documentation authority

Read these current documents in order:

1. `docs/DOCUMENTATION_STATUS.md`
2. `docs/SOURCE_TERMINOLOGY_POLICY.md`
3. `PROJECT_HANDOVER.md`
4. `PROJECT_GUIDELINES.md`
5. `NEXT_CHAT_PROMPT.md`
6. `docs/CLASSICAL_TAMIL_RESEARCH_MATRIX.md`
7. `docs/classical-tamil-research-layer.md`
8. `docs/handover/r15-premerge-audit/README.md`
9. `docs/handover/r15-premerge-audit/01-PURANANURU.md`
10. `docs/handover/r15-premerge-audit/02-TOLKAPPIYAM.md`
11. `docs/handover/r15-premerge-audit/03-VALIDATION-AND-MERGE-GATE.md`
12. `research/README.md`

Files under `docs/history/` are historical snapshots. They may mention old branches, earlier phase boundaries, or superseded prompts and must not be executed as current instructions.

Release documents and durable machine logs remain historical records and are not rewritten merely to make old run IDs look current.

## Next permitted activity

1. verify the documentation-audit CI on the current PR head;
2. confirm PR #3 is still open, draft, and unmerged;
3. report the audit result to the user;
4. await explicit merge authorization.

R2 is blocked. **Do not start R2 and do not merge PR #3 merely because all checks pass.**
