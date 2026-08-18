# Next Chat Prompt — R1.5 29-dimension production review

Continue directly in:

`pugazg/sangam-literature-corpus`

Active branch:

`research/classical-tamil-concept-matrix-r1.5`

Active pull request:

**PR #3**

Treat live GitHub state as authoritative.

## HARD HOLD

**Do not merge PR #3. Keep it open, draft, and unmerged. Do not start R2.**

This work is a strengthening of R1.5, not R2.

## Mandatory startup

Before changing the repository, read these files completely:

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
16. current PR #3 metadata and latest checks.

Then inspect live branches and `main`. Current GitHub state overrides stale historical prose.

## Accepted preservation/research boundaries

- Corpus 1.1.0 remains frozen: 28 works / 7,234 canonical records.
- R0 evidence schema `0.1.0` remains intact: 2,867 assertions, 285 candidates, 43 pilot entities, 51 relationships.
- R1 workflow schema `0.2.0` remains intact with 8 append-only review events and 3 conservative entity decisions.
- R1.5 concept schema `0.3.0` is the current pre-merge foundation.
- Puṟanāṉūṟu exhaustive audit already visited 400 / 400 records against 29 dimensions.
- Tolkāppiyam exhaustive audit already visited 1,602 / 1,602 நூற்பா across 27 இயல் against 29 dimensions.
- The prior exhaustive audit is a coverage/control artifact, not the final production matrix.
- Tolkāppiyam evidence must not auto-classify Sangam poems.
- R2 is blocked and has not started.

## Canonical production matrix surface

The production matrix must support these exact 29 dimensions:

1. literary domain: Akam/Puram
2. tiṇai / tuṟai
3. landscape/environment
4. season/weather/time
5. flora
6. fauna
7. people and social roles
8. relationships
9. emotion/lived experience
10. occupations and production
11. food and subsistence
12. clothing, ornaments, adornment
13. material culture and everyday objects
14. weapons and warfare
15. mobility and transport
16. settlements and built environment
17. economy
18. trade and exchange
19. polity and political life
20. communities/social groups
21. family/gender/kinship
22. religion/ritual
23. death/mourning/memory
24. arts/music/performance
25. knowledge/technology
26. values/ethical concepts
27. body/health
28. named entities
29. textual/intertextual relationships

`research/audits/r15-premerge/dimensions.json` already contains this exact 29-dimension registry.

The older production vocabulary `research/controlled-vocabularies/concept-dimensions-r15.json` is coarser and currently has 22 dimensions. **The first activity is to align the production vocabulary/schema to the exact 29-dimension frame.** Do not collapse separate dimensions for convenience.

## Record-by-record review rule

For every poem or நூற்பா:

1. Read the complete canonical record and its source-explicit metadata/context.
2. Consider **all 29 dimensions**, even when most are empty.
3. Record every qualifying observation with exact source-supported Tamil evidence and provenance.
4. Preserve ambiguity; do not guess.
5. Update/write that record's durable matrix/ledger state **before moving to the next record**.
6. Empty means only: no qualifying evidence identified in this reviewed source record. It never means historical absence.
7. Keyword/token searches may assist navigation but are not sufficient semantic evidence.
8. Git commits may be made in deterministic batches; the durable ledger must nevertheless prove individual record completion.

## Puṟanāṉūṟu sequence

After the 29-dimension production vocabulary/schema is aligned and validated:

- review Puṟanāṉūṟu records 1 through 400 sequentially;
- update the production matrix/ledger after each poem before reading the next;
- consider all 29 dimensions for every poem;
- keep source metadata and body-derived observations provenance-distinct;
- preserve damaged/lacuna text;
- record 200 conservatively as damaged where applicable;
- keep 267 and 268 source-lost and unreconstructed;
- do not turn printed names into verified historical identities without separate evidence.

Do not merely copy the old sparse audit ledger into production. Use it as a coverage/control artifact and retain exact evidence spans/assertion provenance in production observations.

## Tolkāppiyam sequence

Only after the Puṟanāṉūṟu production pass is complete and validated, review Tolkāppiyam sequentially across all 27 இயல் / 1,602 நூற்பா.

For each நூற்பா:

- consider all 29 dimensions;
- update the durable review/matrix state before moving to the next நூற்பா;
- distinguish at minimum:
  - `GRAMMATICAL_CONCEPT_EVIDENCE`
  - `INCIDENTAL_EXAMPLE`
  - `NO_QUALIFYING_EVIDENCE`
- keep grammatical/poetics evidence separate from Sangam literary-world observations;
- never auto-classify a Sangam poem from a Tolkāppiyam rule.

A lexical example in a grammatical rule is not automatically a historical/social/ecological/material-culture assertion.

## Source terminology boundary

Follow `docs/SOURCE_TERMINOLOGY_POLICY.md` exactly.

Preserve the exact Tamil social, ritual, learned, occupational, political, kinship, and community term printed by the relevant source. Do not silently replace source terms with later identity, hierarchy, sectarian, modern-community, or external-influence labels.

The frozen source text is never edited to satisfy research terminology preferences.

## Validation and continuity

Before any future claim that strengthened R1.5 is merge-ready:

- verify exact 29-dimension schema/vocabulary support;
- prove 400/400 Puṟanāṉūṟu record-level production review states;
- prove 1,602/1,602 Tolkāppiyam நூற்பா-level production review states;
- retain exact populated evidence provenance;
- retain source-lost/damaged states;
- preserve empty-cell semantics;
- pass terminology policy tests;
- pass generators/idempotence/full regression/repository audit;
- prove Corpus 1.1.0 and Tolkāppiyam canonical non-drift;
- prove R1 primary histories remain preserved except explicitly permitted append-only changes;
- keep PR #3 draft/unmerged until explicit user authorization.

If continuity becomes large, add another numbered file under `docs/handover/r15-premerge-audit/` and update its index. Do not grow one monolithic handover file.

## Required next activity

1. Inspect current PR #3 and live branch state.
2. Confirm PR #3 is open, draft, and unmerged; do not merge it.
3. Align the production concept-dimension vocabulary/schema from the current coarse 22-dimension model to the exact canonical 29-dimension matrix.
4. Add/update tests and validators so the 29 dimensions cannot regress or be silently collapsed.
5. Run full CI/non-drift validation.
6. Once the schema alignment is green, begin Puṟanāṉūṟu record 001 and proceed sequentially, updating the durable matrix state after each poem.

Do not start R2.
