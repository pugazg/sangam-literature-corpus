# Next Chat Prompt — R1.5 Classical Tamil Concept Matrix

<!-- R1_REVIEW_WORKFLOW_COMPLETE_20260818 -->

Treat current GitHub state as authoritative. Do **not** repeat R0 reconciliation
or R1 review-workflow implementation, and do **not** begin R2.

## Mandatory startup

Read these files completely before making any repository change:

1. `PROJECT_HANDOVER.md`
2. `PROJECT_GUIDELINES.md`
3. `NEXT_CHAT_PROMPT.md`
4. `docs/CLASSICAL_TAMIL_RESEARCH_MATRIX.md`
5. `docs/classical-tamil-research-layer.md`
6. `manifests/classical-tamil-research-program.json`
7. `research/reports/purananuru-r1-review-summary.json`
8. `research/reports/purananuru-r1-review-summary.md`
9. `research/reports/purananuru-r1-ambiguity-register.md`
10. `logs/classical-tamil-research-r0-to-corpus-1.1.0-compatibility-20260818T145500.json`
11. `logs/classical-tamil-research-r1-baseline-20260818T145500.json`
12. `logs/classical-tamil-research-r1-idempotence-20260818T145500.json`
13. `logs/classical-tamil-research-program-decisions.md`

Then inspect current `main`, `research/sangam-evidence-r1`, open PRs, recent
commits, tags, and the live repository tree. Current GitHub state overrides
stale SHAs in historical prose.

## R1 accepted boundary

R1 preserves R0 evidence identity at schema `0.1.0` and adds workflow schema
`0.2.0`. It contains no external-historical or interpretive assertions and no
verified historical identity. Do not weaken these constraints.

## Active work — R1.5

Proceed exactly from `docs/CLASSICAL_TAMIL_RESEARCH_MATRIX.md`.

R1.5 must formalise the observation model before corpus-wide extraction. Every
populated cell must remain traceable to assertion IDs and exact evidence.
Akam/Puram, tiṇai, tuṟai, landscapes, material/lived-life dimensions, and named
entities must retain classification basis/provenance rather than becoming
unsupported boolean tags.

Empty cells mean only “qualifying evidence is not currently recorded”; they do
not prove historical absence.

Start with a bounded, deterministic pilot and explicit schemas/vocabularies.
Do not expand to corpus-wide R2 extraction until the R1.5 model, validation,
tests, audit, and handover are complete.

The historical prompt that led through R0 reconciliation and R1 is archived at
`docs/history/NEXT_CHAT_PROMPT_R1.md`.
