# R1.5 — 29-dimension production review continuation

## Merge and phase hold

PR #3 must remain **open, draft, and unmerged** throughout this work.

R2 is blocked. Do not start R2, create R2 branches, or relabel this work as R2.

This is a continuation and strengthening of R1.5.

## Objective

Convert the exhaustive 29-dimension semantic audit into the canonical R1.5 production matrix through a record-by-record source review.

The 29-dimension audit registry at `research/audits/r15-premerge/dimensions.json` is the canonical target surface for this work.

The older production vocabulary at `research/controlled-vocabularies/concept-dimensions-r15.json` currently exposes a coarser 22-dimension model. The first implementation activity is therefore to align the production vocabulary/schema to the exact 29-dimension frame without changing frozen corpus/source text.

## Canonical 29 dimensions

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

Do not collapse dimensions merely for convenience. Economy and trade remain separate; emotion/lived experience and values/ethical concepts remain separate; body/health remains separate from clothing/adornment; people/social roles remains distinct from communities/social groups and family/gender/kinship.

## Record-by-record update rule

For every source record:

1. Read the complete canonical record and its source-explicit metadata/context.
2. Consider all 29 dimensions, not only dimensions suggested by keyword search.
3. Record every qualifying dimension with exact source-supported Tamil evidence and provenance.
4. Record ambiguity explicitly; do not guess.
5. Write/update that record's durable matrix/ledger result **before reading the next record**.
6. An empty dimension means only: no qualifying evidence was identified in that reviewed source record. It never means historical absence.
7. Commit record-level updates in deterministic review batches rather than creating one Git commit per record. The ledger itself must nevertheless show that each record was completed individually.

Keyword/token scans may assist navigation but are never sufficient evidence of semantic review.

## Puṟanāṉūṟu production review

Review records 1 through 400 sequentially from the frozen canonical source.

For each poem:

- consider all 29 dimensions;
- retain source-printed tiṇai/tuṟai and metadata provenance separately from body-derived observations;
- preserve damaged/lacuna text without reconstruction;
- record 200 conservatively as damaged where applicable;
- keep 267 and 268 source-lost and unreconstructed;
- do not convert names into verified historical identities without separately classified evidence;
- preserve exact Tamil source terminology under `docs/SOURCE_TERMINOLOGY_POLICY.md`.

The prior eight-part exhaustive audit ledger is evidence that all 400 records were visited, but it is not by itself the final production observation dataset. Production observations must retain exact evidence spans/assertion provenance and review state.

## Tolkāppiyam production review

After the Puṟanāṉūṟu production pass is complete and validated, review all 1,602 Tolkāppiyam நூற்பா sequentially across the 27 இயல்.

For each நூற்பா:

- consider all 29 dimensions;
- write its reviewed result before moving to the next நூற்பா;
- distinguish at minimum:
  - `GRAMMATICAL_CONCEPT_EVIDENCE`
  - `INCIDENTAL_EXAMPLE`
  - `NO_QUALIFYING_EVIDENCE`
- preserve the grammatical/poetics evidence stream separately from Sangam literary-world observations;
- never auto-classify a Sangam poem from a Tolkāppiyam rule;
- preserve exact source Tamil terms rather than replacing them with later social/religious/hierarchical identities.

A lexical item used only as an example inside a grammatical rule is not automatically a historical, social, ecological, or material-culture assertion.

## Evidence boundary

The frozen corpus remains authoritative and unchanged.

Allowed production evidence classes and review states must remain explicit and versioned. Do not silently upgrade a source observation into external history, historical identity, modern taxonomy, modern geography, translation, or interpretation.

The R1 append-only review histories and R0 evidence identities remain preserved.

## Validation expectations

Before any claim that this strengthened R1.5 is merge-ready:

- production vocabulary/schema exactly supports all 29 dimensions;
- every Puṟanāṉūṟu record has a deterministic record-level review state for all 29 dimensions;
- every Tolkāppiyam நூற்பா has a deterministic record-level review state for all 29 dimensions;
- source-lost/damaged states remain explicit;
- exact evidence provenance is retained for populated observations;
- empty-cell semantics are preserved;
- source-terminology policy passes;
- generators are deterministic;
- full tests pass;
- repository audit passes;
- Corpus 1.1.0 and Tolkāppiyam canonical preservation layers show no drift;
- R1 primary histories remain unchanged except through explicitly permitted append-only review events;
- PR #3 remains draft/unmerged until explicit user authorization.

## Continuation discipline

Do not restart the earlier R0 token scan, R1 review workflow, or the completed exhaustive audit.

Use the completed audit as a coverage/control artifact, then build the stronger production matrix record by record.

If a continuity document becomes large, add another numbered file in this handover directory and update the index instead of turning `PROJECT_HANDOVER.md` or `NEXT_CHAT_PROMPT.md` into a monolith.
