# Part 3 — Validation and merge gate

## Current phase state

R1.5 is **not merge-ready merely because the earlier bounded pilot passed**. The exhaustive pre-merge matrix audit has reopened the completeness gate.

PR #3 must remain **draft and unmerged** until the final audit head passes all required checks. R2 must not begin.

## Exhaustive audit validator

`scripts/validate_r15_premerge_matrix_audit.py` must prove:

- exactly 29 controlled dimensions;
- exactly eight ordered Puṟanāṉūṟu TSV parts covering records 1–400 exactly once;
- no unknown dimension codes;
- record 200 remains unreconstructed;
- source-lost records 267–268 remain unreconstructed;
- dimension counts match the committed summary;
- the frozen Puṟanāṉūṟu consolidated-source Git blob is unchanged;
- exactly 27 Tolkāppiyam இயல் ranges in canonical order;
- the ranges expand contiguously to source sequences 1–1602 exactly once;
- the frozen Tolkāppiyam consolidated-source Git blob is unchanged;
- all 29 matrix dimensions occur in the Tolkāppiyam formal crosswalk;
- every crosswalk evidence pointer resolves to an in-range இயல்/நூற்பா;
- Tolkāppiyam automatic Sangam-poem classification remains disabled.

Regression tests in `tests/test_r15_premerge_matrix_audit.py` independently enforce the main coverage boundaries.

## Existing gates that remain mandatory

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

## Merge decision after validation

Even after every gate is green, **do not merge automatically**. Report the audit result to the user and leave PR #3 draft/unmerged unless the user explicitly authorizes the merge.

Only after an authorized merge and a fresh inspection of live `main` may the project consider the R2 transition.
