# Part 3 — Validation and merge gate

## Current phase state

R1.5 remains **draft and unmerged by explicit user instruction**. The exhaustive pre-merge audit passed its data/validation gates. A documentation synchronization pass is also required to prevent stale branch/phase instructions from surviving into the merge boundary.

Technical success never authorizes merge. R2 remains blocked.

## Exhaustive audit validator

`scripts/validate_r15_premerge_matrix_audit.py` enforces:

- exactly 29 controlled dimensions;
- eight ordered Puṟanāṉūṟu TSV parts covering records 1–400 exactly once;
- no unknown dimension codes;
- record 200 remains unreconstructed;
- records 267–268 remain source-lost/unreconstructed;
- ledger counts match the committed summary;
- frozen Puṟanāṉūṟu source blob is unchanged;
- exactly 27 Tolkāppiyam இயல் ranges covering source sequences 1–1602 exactly once;
- frozen Tolkāppiyam source blob is unchanged;
- all 29 dimensions occur in the Tolkāppiyam formal crosswalk;
- every representative crosswalk pointer resolves;
- automatic Tolkāppiyam → Sangam poem classification is disabled.

## Complete CI gate

The PR workflow must pass all of the following on the current head:

1. regenerate preserved R0 evidence;
2. regenerate R1 derived review exports;
3. regenerate R1.5 pilot outputs;
4. validate R0 compatibility;
5. validate R1 workflow;
6. validate R1.5 pilot;
7. validate R1.5 acceptance/orphan-reference boundary;
8. validate the exhaustive pre-merge matrix audit;
9. run the complete regression suite;
10. verify R1 deterministic regeneration;
11. verify R1.5 deterministic regeneration and primary-input preservation;
12. audit the repository;
13. prove Corpus 1.1.0 and Tolkāppiyam non-drift;
14. prove R1 primary evidence/history/relationship non-mutation;
15. enforce documentation-status regression checks.

The live PR check result is the authoritative current validation record. Older workflow IDs and durable logs remain historical evidence and should not be rewritten to masquerade as the newest run.

## Documentation gate

Active current documents must not instruct a future worker to:

- use deleted R0/R1 branches as current branches;
- restart completed R0/R1 work;
- treat R1.5 as merely a future phase;
- start R2 before authorization;
- use the former repository name as current authority.

Historical prompts remain under `docs/history/` and are non-executable provenance.

## Merge decision

**Do not merge PR #3.** Keep it open and draft until the user explicitly authorizes merge.

**Do not start R2.** No R2 branch, schema, extraction, baseline, prompt execution, or production dataset may be created before an authorized merge and fresh inspection of live `main`.
