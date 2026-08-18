# R1.5 pre-merge exhaustive matrix audit

This audit was opened after the bounded R1.5 pilot had already passed its original acceptance gates. It exists because `400 records processed` in R0 did **not** mean that every Puṟanāṉūṟu poem had been semantically reviewed against every research-matrix dimension.

## Scope

The controlled dimension list is `dimensions.json` and contains exactly 29 dimensions.

Two different source reads are recorded:

1. **Puṟanāṉūṟu** — every record 1–400 was read sequentially from the frozen consolidated source and all 29 dimensions were considered. The eight TSV parts store only qualifying dimensions; omitted dimensions mean only that no qualifying evidence was recorded in that reviewed source record.
2. **Tolkāppiyam** — every one of the 1,602 நூற்பா was read in its இயல் context and checked for whether the 29 dimensions are formally or structurally represented. `review-manifest.json` proves complete range coverage. `dimension-crosswalk.json` records representative formal support and the depth of support.

## Evidence boundaries

- No frozen corpus/source file is edited by this audit.
- Puṟanāṉūṟu matrix labels are source-review observations, not external historical facts.
- Tolkāppiyam `GRAMMATICAL_CONCEPT_EVIDENCE` is a separate grammatical/poetics stream and never auto-classifies a Sangam poem.
- A lexical example inside a grammatical rule is not automatically a cultural or historical claim.
- Named forms are not resolved into historical identities without separate evidence.
- Empty cells never prove historical absence.

## Special Puṟanāṉūṟu conditions

- record 200: damaged/unreadable body condition retained; only the work-level literary-domain review is recorded.
- records 267–268: source-lost; both were explicitly visited and no lost text is reconstructed.

## Files

- `dimensions.json` — controlled 29-dimension registry.
- `purananuru/parts/001-050.tsv` … `351-400.tsv` — exhaustive poem-by-poem semantic review.
- `purananuru/dimension-summary.json` — dimension coverage counts and interpretation constraints.
- `tolkappiyam/review-manifest.json` — 27 இயல் coverage map expanding exactly to 1,602 நூற்பா.
- `tolkappiyam/dimension-crosswalk.json` — formal/structural Tolkāppiyam support for the 29 dimensions.

This audit reopens the R1.5 merge gate. PR #3 must remain unmerged until the audit validator, regression suite, repository audit and non-drift checks pass on the final audit head.
