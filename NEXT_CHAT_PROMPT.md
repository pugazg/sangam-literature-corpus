# Next Chat Prompt — R1.5 documentation-audit / merge hold

Treat live GitHub state as authoritative.

**Do not merge PR #3. Keep it open, draft, and unmerged. Do not start R2 unless the user explicitly authorizes the R1.5 merge and the merged `main` has then been re-inspected.**

## Mandatory startup

Read completely before changing the repository:

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
13. current PR #3 metadata and checks.

Then inspect live branches and `main`. Current GitHub state overrides any stale historical prose.

## Accepted boundaries

- Corpus 1.1.0 remains frozen: 28 works / 7,234 canonical records.
- R0 evidence schema `0.1.0` remains intact: 2,867 assertions, 285 candidates, 43 pilot entities, 51 relationships.
- R1 workflow schema `0.2.0` remains intact with 8 append-only review events and 3 conservative entity decisions.
- R1.5 concept schema `0.3.0` remains the current pre-merge foundation.
- Puṟanāṉūṟu exhaustive audit: 400 / 400 records × 29 dimensions.
- Tolkāppiyam exhaustive audit: 1,602 / 1,602 நூற்பா across 27 இயல் × 29 dimensions.
- Tolkāppiyam evidence does not auto-classify Sangam poems.
- R2 is blocked and has not started.

## Source terminology boundary

Follow `docs/SOURCE_TERMINOLOGY_POLICY.md`.

Preserve the exact Tamil social, ritual, learned, occupational, political, kinship, and community term printed by the relevant source. Do not silently replace a source term with a later caste, sectarian, modern-community, hierarchy, or external-influence identity.

The frozen source text is never edited to satisfy research terminology preferences.

## Documentation rule

Active status/guidance documents must describe the live R1.5 branch/PR state. Historical prompts belong under `docs/history/` and are non-executable provenance.

Do not reintroduce deleted R0/R1 branches into active “current branch” or “next activity” instructions.

## Required next activity

Only complete the current documentation/validation hold:

1. inspect the current PR #3 head and latest workflow result;
2. if a documentation-only change was made, require fresh CI;
3. confirm exhaustive matrix validation, complete tests, determinism, repository audit, corpus/Tolkāppiyam non-drift, and R1 primary-history preservation still pass;
4. correct documentation defects without changing frozen corpus evidence or weakening evidence rules;
5. keep PR #3 draft and unmerged;
6. report the result and wait for explicit user instruction.

Do not create R2 branches, schemas, observations, prompts, baselines, or extraction output in this phase.
