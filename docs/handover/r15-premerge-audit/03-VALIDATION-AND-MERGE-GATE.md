# Part 3 — Validation and merge gate

## Current phase state

R1.5 remains **draft and unmerged by explicit user instruction**. The exhaustive pre-merge matrix audit has now passed its data/validation gates, but that does **not** authorize a merge. R2 must not begin.

The audit was required because the earlier bounded R1.5 pilot proved the observation model but did not prove semantic review of every Puṟanāṉūṟu poem against all 29 research dimensions.

## Exhaustive audit validator

`scripts/validate_r15_premerge_matrix_audit.py` proves:

- exactly 29 controlled dimensions;
- exactly eight ordered Puṟanāṉūṟu TSV parts covering records 1–400 exactly once;
- no unknown dimension codes;
- record 200 remains unreconstructed;
- source-lost records 267–268 remain unreconstructed;
- dimension counts match the committed ledger-derived summary;
- the frozen Puṟanāṉūṟu consolidated-source Git blob is unchanged;
- exactly 27 Tolkāppiyam இயல் ranges in canonical order;
- the ranges expand contiguously to source sequences 1–1602 exactly once;
- the frozen Tolkāppiyam consolidated-source Git blob is unchanged;
- all 29 matrix dimensions occur in the Tolkāppiyam formal crosswalk;
- every crosswalk evidence pointer resolves to an in-range இயல்/நூற்பா;
- Tolkāppiyam automatic Sangam-poem classification remains disabled.

Regression tests in `tests/test_r15_premerge_matrix_audit.py` independently enforce the main coverage boundaries.

## Successful validation record

Validated audit-data head:

`0cee016cfc7dcbdcc475ee1d4aa2e1ecf426f5ff`

GitHub Actions workflow:

- run: `32139227280`
- job: `95717654556`
- conclusion: **success**

Exhaustive matrix gate result:

- Puṟanāṉūṟu records reviewed: **400 / 400**
- research dimensions considered per Puṟanāṉūṟu record: **29 / 29**
- Tolkāppiyam இயல் reviewed: **27 / 27**
- Tolkāppiyam நூற்பா reviewed: **1,602 / 1,602**
- research dimensions considered per Tolkāppiyam நூற்பா: **29 / 29**
- Tolkāppiyam dimension crosswalk: **29 / 29**
- Tolkāppiyam support depth: **17 systematic framework / 11 explicit formal support / 1 scope-limited**
- validator errors: **0**
- validator warnings: **0**
- automatic Tolkāppiyam → Sangam classification: **disabled**

Full workflow closure:

- complete regression suite: **209 passed**
- R1 deterministic regeneration: **pass**
- R1.5 deterministic regeneration: **pass**
- R1.5 declared primary inputs preserved: **true**
- repository audit: **pass**, **8,796 files**
- Corpus 1.1.0 non-drift: **pass**
- Tolkāppiyam non-drift: **pass**
- R1 primary evidence/history/relationship non-mutation: **pass**

Durable machine-readable result:

`logs/classical-tamil-r15-premerge-matrix-audit-20260818T125336Z.json`

## Important correction caught by CI

The first exhaustive-audit run correctly failed because the hand-entered Puṟanāṉūṟu summary said `body_health = 193`, while the committed 400-record TSV ledger deterministically computed `192`. The summary was corrected to the ledger-derived value; no poem classification was changed to force a pass. The subsequent full workflow passed.

## Existing gates remain mandatory

The exhaustive audit is an **additional** gate. It does not replace:

- R0 generation/validation;
- R1 generation/validation;
- R1.5 pilot generation/validation;
- original R1.5 schema/acceptance validator;
- complete regression suite;
- R1 and R1.5 deterministic-regeneration checks;
- repository audit;
- Corpus 1.1.0/Tolkāppiyam non-drift;
- R1 primary-history non-mutation.

All of those gates passed in workflow `32139227280` on the validated audit-data head.

## Merge decision after validation

**Do not merge PR #3.** The user explicitly requested that R1.5 remain unmerged after this audit. Keep PR #3 draft.

**Do not start R2.** No R2 branch, schema, extraction, baseline, prompt execution or production dataset may be created until the user explicitly authorizes the phase transition.

Only after an explicitly authorized merge and a fresh inspection of live `main` may R2 be considered.
