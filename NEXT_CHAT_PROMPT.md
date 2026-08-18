# Next Chat Prompt — R1.5 exhaustive pre-merge matrix audit

<!-- R15_PREMERGE_EXHAUSTIVE_AUDIT_ACTIVE_20260818 -->

Treat current GitHub state as authoritative.

**Do not merge PR #3. Do not start R2.** The earlier bounded R1.5 pilot passed its original gates, but the user reopened the merge boundary to require exhaustive semantic/matrix coverage verification.

## Mandatory startup

Read completely before changing the repository:

1. `docs/SOURCE_TERMINOLOGY_POLICY.md`
2. `docs/handover/r15-premerge-audit/README.md`
3. `docs/handover/r15-premerge-audit/01-PURANANURU.md`
4. `docs/handover/r15-premerge-audit/02-TOLKAPPIYAM.md`
5. `docs/handover/r15-premerge-audit/03-VALIDATION-AND-MERGE-GATE.md`
6. `research/audits/r15-premerge/README.md`
7. `research/audits/r15-premerge/dimensions.json`
8. all eight files under `research/audits/r15-premerge/purananuru/parts/`
9. `research/audits/r15-premerge/purananuru/dimension-summary.json`
10. `research/audits/r15-premerge/tolkappiyam/review-manifest.json`
11. `research/audits/r15-premerge/tolkappiyam/dimension-crosswalk.json`
12. `scripts/validate_r15_premerge_matrix_audit.py`
13. `tests/test_r15_premerge_matrix_audit.py`
14. `docs/CLASSICAL_TAMIL_RESEARCH_MATRIX.md`
15. `PROJECT_GUIDELINES.md`
16. `PROJECT_HANDOVER.md` for historical continuity, while treating this prompt and the split pre-merge audit handover as the current status override.

Then inspect current branch head, PR #3 state, workflow runs and current `main`. Live repository state overrides stale historical prose.

## Source-terminology boundary

- preserve the exact Tamil social, ritual, learned, occupational, political, kinship, and community term printed by the relevant source;
- where the source uses forms such as `அந்தணர்`, `பார்ப்பார்`, `பார்ப்பனர்`, `அரசர்`, `வேளாளர்`, or `பாணர்`, retain the applicable printed form rather than replacing it with a later identity label;
- do not infer later caste, sectarian, modern-community, hierarchy, or external-influence identities from a source term alone;
- any such historical claim, if ever researched, belongs in a separately classified external-evidence or interpretive assertion with independent provenance;
- never alter the frozen source text to satisfy research terminology preferences.

## Exhaustive review boundary

### Puṟanāṉūṟu

- records 1–400 have been read sequentially from the frozen consolidated source;
- all 29 matrix dimensions were considered for every record;
- qualifying dimensions are stored sparsely in eight 50-record TSV parts;
- record 200 remains damaged/unreconstructed;
- records 267–268 remain source-lost/unreconstructed;
- empty cells mean only that qualifying evidence was not recorded, not historical absence.

### Tolkāppiyam

- all 1,602 நூற்பா across 27 இயல் have been read in context;
- all 29 matrix dimensions were considered for every நூற்பா;
- distinguish `GRAMMATICAL_CONCEPT_EVIDENCE`, `INCIDENTAL_EXAMPLE`, and `NO_QUALIFYING_EVIDENCE`;
- the 29-dimension crosswalk records representative formal support and differing depth;
- Tolkāppiyam evidence must never automatically classify a Sangam poem.

## Required next activity

Finish the **validation and audit closure only**:

1. run the exhaustive pre-merge matrix validator;
2. run the complete regression suite;
3. run repository audit and Corpus/Tolkāppiyam non-drift checks;
4. prove R1 primary histories remain unchanged;
5. correct any audit-data or validator defect without weakening source/evidence rules;
6. update the split handover and PR #3 body with the final results;
7. leave PR #3 **draft and unmerged** even if everything passes;
8. report the result to the user and await explicit merge authorization.

Do not create R2 branches, schemas, observations, baselines, prompts or extraction output in this phase.

The pre-audit R2 draft prompt is preserved only as history in `docs/history/NEXT_CHAT_PROMPT_R2_DRAFT_PRE_AUDIT.md`.
