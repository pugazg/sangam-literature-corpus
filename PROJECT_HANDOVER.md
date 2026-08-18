# Sangam Literature Corpus — Project Handover

## Authoritative current state

Repository: `pugazg/sangam-literature-corpus`

Default branch: `main`

Active research branch: `research/classical-tamil-concept-matrix-r1.5`

Active pull request: **PR #3** — R1.5 Classical Tamil Concept Matrix Foundation.

**PR #3 is to remain open, draft, and unmerged until the user explicitly authorizes merge. R2 is blocked and has not started; do not start R2 before that authorization and a fresh inspection of live `main`.**

At the documentation audit, GitHub exposed only `main` and the R1.5 research branch. Earlier R0/R1 branches were deleted after their work was preserved. Do not recreate or depend on those deleted branches.

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

## Strengthened R1.5 production review

The user has approved a stronger pre-merge standard before PR #3 can be considered for merge.

The exact 29-dimension audit registry at `research/audits/r15-premerge/dimensions.json` is now the target production matrix surface.

The older production vocabulary `research/controlled-vocabularies/concept-dimensions-r15.json` is still a coarser 22-dimension model. The next implementation activity is to align that production vocabulary/schema to the exact 29 dimensions and prevent future collapse through tests/validation.

After schema alignment is green:

1. review Puṟanāṉūṟu records 1–400 sequentially;
2. for every poem, read the complete source record, consider all 29 dimensions, and write its durable production matrix/review state before moving to the next poem;
3. after the Puṟanāṉūṟu production pass is complete and validated, review all 1,602 Tolkāppiyam நூற்பா across all 27 இயல் in the same record-by-record manner;
4. keep Tolkāppiyam grammatical/poetics evidence separate from Sangam literary-world observations and distinguish grammatical concept evidence from incidental examples;
5. commits may be batched deterministically, but the durable ledger must prove individual record completion.

The authoritative detailed contract is `docs/handover/r15-premerge-audit/04-29-DIMENSION-PRODUCTION-REVIEW.md`.

This remains R1.5. R2 must not start.

## Source terminology rule

`docs/SOURCE_TERMINOLOGY_POLICY.md` is mandatory.

Retain the exact Tamil term printed by the relevant source. For example, மரபியல் நூற்பா 71 uses `அந்தணர்`, while நூற்பா 72 uses `அரசர்`. Do not silently replace source terms with later identity, hierarchy, sectarian, modern-community, or external-influence labels.

Any later historical equivalence claim must be a separately classified external-evidence or interpretive assertion with independent provenance.

## Validation state

The documentation-audit head before this new continuation contract passed the R0/R1/R1.5 validators, exhaustive matrix validator, 216-test regression suite, deterministic regeneration checks, repository audit, Corpus 1.1.0/Tolkāppiyam non-drift, and R1 primary-history preservation.

The new continuation-document changes must also pass fresh CI. The live PR check state is authoritative; do not treat an older embedded workflow ID as permanent final status.

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
12. `docs/handover/r15-premerge-audit/04-29-DIMENSION-PRODUCTION-REVIEW.md`
13. `research/audits/r15-premerge/dimensions.json`
14. `research/controlled-vocabularies/concept-dimensions-r15.json`
15. `research/README.md`

Files under `docs/history/` are historical snapshots. They may mention old branches, earlier phase boundaries, or superseded prompts and must not be executed as current instructions.

Release documents and durable machine logs remain historical records and are not rewritten merely to make old run IDs look current.

## Next permitted activity

1. inspect live PR #3/branch/check state and confirm PR #3 remains open, draft, and unmerged;
2. read `NEXT_CHAT_PROMPT.md` and `04-29-DIMENSION-PRODUCTION-REVIEW.md` completely;
3. align the production concept-dimension vocabulary/schema from 22 coarse dimensions to the exact canonical 29-dimension surface;
4. add/update tests and validators to prevent regression/collapse;
5. require fresh full CI and non-drift validation;
6. once green, begin Puṟanāṉūṟu record 001 and proceed sequentially, writing the durable matrix state after each poem;
7. complete and validate Puṟanāṉūṟu before beginning the equivalent Tolkāppiyam நூற்பா-by-நூற்பா production pass.

R2 is blocked. **Do not start R2 and do not merge PR #3 merely because checks pass.**
