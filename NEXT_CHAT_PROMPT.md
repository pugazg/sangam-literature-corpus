# Next Chat Prompt — Reconcile R0 and Begin R1 Research Review

Use this document as the startup prompt for a fresh ChatGPT/Codex window.

---

Continue the Classical Tamil Corpus / Research Layer project directly in:

`pugazg/sangam-literature-corpus`

Work from GitHub repository state, not from stale local paths or earlier chat assumptions.

## Mandatory startup

Before making any change, use the GitHub connector and read these files completely:

1. `PROJECT_HANDOVER.md`
2. `PROJECT_GUIDELINES.md`
3. `NEXT_CHAT_PROMPT.md`
4. `docs/CLASSICAL_TAMIL_RESEARCH_MATRIX.md`
5. `README.md`
6. `docs/classical-tamil-corpus-release-1.1.0.md`
7. `manifests/classical-tamil-corpus-release-1.1.0.json`
8. `manifests/repository-protected-conditions-1.1.0.json`
9. `docs/manifest-ordering-policy.md`
10. `docs/source-rights-and-redistribution-review.md`
11. `corpus/tolkappiyam/metadata.json`

Then inspect the live GitHub repository:

- default branch;
- current `main` head;
- branches;
- recent commits;
- release refs/tags where available;
- open PRs;
- repository visibility;
- current file tree.

Repository state is authoritative over SHA values or status paragraphs in this prompt if newer intentional work exists.

## Research branch startup

Inspect:

`research/sangam-evidence-r0`

Read completely from that branch:

1. `docs/classical-tamil-research-layer.md`
2. `manifests/classical-tamil-research-program.json`
3. `research/README.md`
4. `research/reports/purananuru-extraction-summary.json`
5. `logs/classical-tamil-research-program-decisions.md`
6. latest `logs/classical-tamil-research-layer-r0-baseline-*.json`
7. latest `logs/classical-tamil-research-layer-r0-idempotence-*.json`
8. latest `logs/classical-tamil-research-frozen-regression-*.json`
9. `scripts/generate_research_layer.py`
10. `scripts/validate_research_layer.py`
11. relevant research schemas and controlled vocabularies

Inspect the exact branch comparison with current `main` before modifying either branch.

The historically recorded R0 commit is:

`7087626347b56e0145ab69b2fb7ef355f6bc07d5d`

Do not assume this remains the branch head without checking.

## Current verified corpus baseline

The current frozen corpus release is Classical Tamil Corpus `1.1.0`.

Expected verified state:

- 28 frozen works;
- 7,234 canonical records;
- 5,632 poem records;
- 1,602 Tolkāppiyam நூற்பா records;
- Tolkāppiyam: 3 அதிகாரம் / 27 இயல் / 1,602 நூற்பா;
- release fingerprint: `4ca530d3a836341b5abaa395af97cf7307529ced04dd40dec17b1a010949abca`.

Tolkāppiyam source:

- Project Madurai `pmuni0100`;
- SHA-256 `16b2edf314763ef491bdc498c0017de33e7e190753587b230bbafcd03219f5da`;
- upstream reference `pugazg/tolkappiyam-arivagam`;
- pinned upstream commit `16123f742503283e46f0ed321802a46f99df6392`.

Do not re-onboard or refreeze Tolkāppiyam.

Do not alter any existing frozen canonical work.

## R0 pilot status that must be preserved

R0 is a derived Puṟanāṉūṟu research pilot, not part of the frozen corpus.

Expected R0 summary:

- research schema: `0.1.0`;
- records processed: 400;
- literary bodies processed: 398;
- source-lost: 267 and 268;
- assertions: 2,867;
- mention candidates: 285;
- pilot entity records: 43;
- pilot relationships: 51;
- machine-checked assertions: 2,582;
- human-review-required assertions: 285;
- external historical assertions: 0;
- interpretation assertions: 0.

All R0 assertions are evidence records. They are not resolved historical facts.

Do not change assertion IDs, evidence spans, or source hashes merely to update metadata.

## Critical provenance issue to resolve first

R0 was generated against corpus release `1.0.0` before Tolkāppiyam was added.

Current `main` is corpus release `1.1.0` plus later documentation.

Before porting or extending R0:

1. verify every Puṟanāṉūṟu canonical record/body/source-note hash relevant to R0 is unchanged between the R0 release baseline and current `main`;
2. verify the Puṟanāṉūṟu physical inventory remains 400 canonical records with lost records 267 and 268 unchanged;
3. verify R0 assertion source hashes still match the current Puṟanāṉūṟu inputs;
4. create a machine-readable compatibility record showing whether the R0 evidence remains valid against corpus 1.1.0;
5. preserve the original R0 source-release provenance even when current repository compatibility is proven.

Suggested record:

`logs/classical-tamil-research-r0-to-corpus-1.1.0-compatibility-<timestamp>.json`

Do not rewrite all R0 assertions from `source_release_tag: classical-tamil-corpus-v1.0.0` to `v1.1.0` if their original derivation provenance is correct.

## Branch strategy

Do not directly continue R1 on the stale R0 branch.

Preferred strategy:

1. create a fresh branch from current `main`:

   `research/sangam-evidence-r1`

2. port the verified R0 research commit/diff onto that branch;
3. preserve all current 1.1.0 corpus/Tolkāppiyam changes from `main`;
4. resolve README/documentation conflicts in favour of the current corpus release text while retaining valid R0 research documentation;
5. do not modify either immutable corpus release identity;
6. do not force-push.

Use the safest available GitHub/git workflow. If cherry-picking or merging would introduce ambiguous changes, inspect the diff file-by-file before proceeding.

Do not merge the stale R0 branch blindly into `main`.

## Gate A — R0 reconciliation verification

After R0 is ported onto the current-main-derived research branch, verify:

- 2,867 assertions unchanged;
- 285 mention candidates unchanged;
- 43 pilot entity records unchanged;
- 51 pilot relationships unchanged;
- assertion IDs unchanged;
- evidence spans unchanged;
- research controlled vocabularies unchanged unless a documented compatibility edit is required;
- no corpus canonical file changed;
- no raw source changed;
- no source-note changed;
- no Tolkāppiyam file changed;
- no shared manifest regression;
- research generation remains deterministic;
- research validator passes;
- full repository tests pass;
- frozen corpus audit passes.

Create a reconciliation report.

Suggested path:

`logs/classical-tamil-research-r0-reconciliation-<timestamp>.json`

Only after Gate A passes should R1 begin.

# R1 Goal — Review Workflow and Entity-Resolution Rules

R1 must improve reviewability and identity resolution without inventing history.

Proposed research schema version:

`0.2.0`

Do not mark the research layer final or frozen.

## R1 objectives

Implement reusable support for:

1. reviewer identity/type;
2. append-only review events;
3. ambiguity queues;
4. entity-resolution decision records;
5. merge / split / reject / supersede operations;
6. variant-form tracking;
7. evidence requirements for identity decisions;
8. deterministic reviewed exports;
9. audit reports;
10. safe transition rules between review statuses.

## Review status rules

Preserve the existing controlled review model unless repository evidence justifies a versioned change.

Important rules:

- `machine_checked` is not human verification;
- `human_review_required` means a person/editor must inspect the evidence;
- assistant-assisted review must identify itself accurately;
- `reviewed` may be used only after an explicit recorded review event;
- `verified` must require an explicit stronger verification decision;
- rejected and superseded records must remain auditable;
- no review step silently deletes historical evidence.

## Entity resolution rules

Do not automatically merge two mentions because they share:

- the same printed form;
- a normalised form;
- a likely epithet;
- a conventional scholarly identity;
- a nearby geographic context.

Create explicit identity states such as repository-appropriate equivalents of:

- unresolved;
- candidate entity;
- possible match;
- reviewed match;
- verified match;
- rejected match;
- split required;
- superseded.

Keep `POSSIBLY_SAME_AS` distinct from a verified identity relation.

Every entity-resolution decision must cite supporting assertion IDs.

## R1 pilot scope

Do not attempt to resolve all 285 human-review-required mentions automatically.

Use a deterministic pilot subset sufficient to validate the workflow.

Preferred review set:

- the existing records 1–25 entity sample;
- the deterministic R0 review sample;
- repeated poet/ruler/place surface forms directly connected to those records.

If a larger sample is safe and evidence-backed, document why.

Do not use external historical sources in R1 unless a separately classified external-evidence subtask is explicitly introduced and cited.

## R1 source-grounded review

For each reviewed mention/entity decision retain:

- exact work/record;
- assertion ID;
- printed form;
- exact evidence span;
- source field/body location;
- current confidence;
- current review status;
- proposed entity identity or unresolved status;
- reviewer type;
- decision rationale;
- supporting assertion IDs;
- ambiguity note;
- timestamp in the review event only.

Do not mutate deterministic source assertions to store reviewer prose.

## Required R1 outputs

Create or evolve repository-appropriate equivalents of:

- `research/reviews/purananuru/review-events.ndjson`
- `research/reviews/purananuru/review-queue.ndjson`
- `research/entities/pilot/entity-resolution-decisions.ndjson`
- `research/reports/purananuru-r1-review-summary.json`
- `research/reports/purananuru-r1-review-summary.md`
- `research/reports/purananuru-r1-ambiguity-register.md`
- `research/reports/purananuru-r1-unresolved-entities.csv`

Add schemas and vocabulary entries only where needed and version them explicitly.

Do not create speculative resolved entities just to populate output files.

## Determinism

Review-derived deterministic exports must have stable ordering.

Execution timestamps belong in event/audit records where semantically required, not in deterministic aggregate content that should be byte-stable.

Use atomic writing and existing concurrency-safe aggregation patterns.

Do not reintroduce overlapping shared writers.

## R1 validation

Extend `scripts/validate_research_layer.py` or equivalent to validate:

- review-event schema;
- reviewer identity/type;
- valid status transitions;
- append-only history;
- entity decision provenance;
- assertion-ID references;
- no orphan relationships;
- no orphan entity decisions;
- deterministic IDs;
- exact source hash/evidence-span preservation;
- no forbidden external/interpretive assertions;
- stable ordering;
- frozen corpus non-drift.

## R1 tests

Retain every existing test and add tests for at least:

1. R0 compatibility with current corpus 1.1.0;
2. R0 assertion-ID stability after reconciliation;
3. review-event schema;
4. reviewer-type validation;
5. legal status transitions;
6. illegal status transitions;
7. append-only review history;
8. entity merge decision provenance;
9. entity split decision provenance;
10. rejected identity candidates;
11. `POSSIBLY_SAME_AS` versus verified identity distinction;
12. unresolved mention preservation;
13. deterministic review queue;
14. deterministic entity-resolution export;
15. exact assertion references;
16. no corpus write from research generation;
17. idempotent research regeneration;
18. full 28-work frozen corpus regression;
19. Tolkāppiyam non-regression;
20. shared manifest concurrency safety.

# Mandatory future phase — R1.5 Classical Tamil Concept Matrix

Do **not** begin R2 immediately after R1.

The next phase after R1 must be R1.5, defined by:

`docs/CLASSICAL_TAMIL_RESEARCH_MATRIX.md`

R1.5 must formalise the observation model before corpus-wide extraction.

At minimum it must make these first-class, evidence-backed dimensions:

- Akam / Puram;
- tiṇai / tuṟai;
- five landscapes: Kuṟiñci, Mullai, Marutam, Neytal, Pālai;
- exceptional Akam categories such as Kaikkilai and Peruntiṇai where evidence supports them;
- landscape/environment, season, time, water;
- flora and fauna;
- human actors and social roles;
- family, gender, kinship, relationships;
- emotion/lived experience;
- occupations, production, food, subsistence;
- clothing, ornament, material culture, everyday objects;
- weapons, warfare, transport;
- settlements and built environment;
- economy, trade, exchange, gifts, wealth;
- kingship, polity, diplomacy;
- communities/social groups;
- religion, ritual, death, mourning, memorialisation;
- arts, music, dance, performance;
- knowledge, technology, body, health, values;
- named entities and textual/intertextual relationships.

Every populated matrix cell must be traceable to assertion IDs and exact evidence.

Do not create boolean tags without evidence provenance.

Empty matrix cells mean only that qualifying evidence is not currently recorded; they do not prove historical absence.

## Akam / Puram rule for R1.5

Do not store only `akam: true` or `puram: true`.

Akam/Puram classification must retain its basis, for example:

- source-explicit;
- work-level classification;
- Tolkāppiyam concept mapping;
- derived/editorial classification;
- uncertain / not applicable.

The same provenance rule applies to tiṇai and tuṟai.

## Five-landscape rule for R1.5

Do not reduce a landscape to a single terrain equivalence such as “Kuṟiñci = mountain”.

The matrix should be able to relate a tiṇai, where evidence supports it, to:

- terrain/environment;
- season/time;
- flora/fauna;
- occupations;
- food/subsistence;
- settlements;
- mobility;
- social actors;
- emotional/relational situations;
- ritual/deity references;
- objects/activities.

Conventional textbook associations must not be inserted into poem records as source facts.

## Tolkāppiyam research rule

Tolkāppiyam is a separate grammatical/poetics evidence stream.

Later research should support:

```text
Tolkāppiyam நூற்பா
      ↓
grammatical / poetic concept assertion
      ↓
controlled concept registry
      ↓
comparison with Sangam poem evidence
```

A Tolkāppiyam rule must not silently rewrite a poem's source classification.

The project should ultimately be able to investigate how surviving Sangam poetic usage corresponds to, differs from, or exceeds Tolkāppiyam's conceptual system.

Systematic Tolkāppiyam ↔ Sangam mapping is planned as R7.

# Revised research roadmap

The authoritative roadmap is now:

- **R0** — research architecture + Puṟanāṉūṟu pilot — implemented;
- **R1** — review workflow + entity-resolution rules — current next phase;
- **R1.5** — Classical Tamil Concept Matrix / ontology foundation — mandatory before R2;
- **R2** — apply the concept matrix across all nine core Sangam works;
- **R3** — cross-corpus poets, rulers, chiefs, patrons, places, communities, and relationships;
- **R4** — civilisation datasets: ecology, food, occupations, economy, trade, material culture, society, kinship/gender, polity, warfare, ritual, death/memory, arts, technology, values, daily life;
- **R5** — matrix explorer, maps, timelines, networks, cross-text search, tiṇai atlas, evidence drill-down;
- **R6** — extend compatible derived research to Patiṉeṇkīḻkkaṇakku;
- **R7** — Tolkāppiyam ↔ Sangam grammatical/concept mapping;
- **R8** — external scholarship and modern historical-identification layer.

Do not skip R1.5 merely because R2 extraction can be automated.

## Required verification before declaring R1 complete

Run repository-appropriate equivalents of:

```bash
python3 scripts/generate_research_layer.py --root .
python3 scripts/validate_research_layer.py --root .
python3 scripts/audit_repository.py --root .
pytest -q
```

Validate all 28 frozen works.

Run the research generator twice and compare complete deterministic output hashes.

Required:

- path additions after second run: none;
- path removals after second run: none;
- R0 assertion changes: none unless explicitly versioned and justified;
- canonical body changes: none;
- source-note changes: none;
- raw-source changes: none;
- Tolkāppiyam changes: none;
- validation errors: zero;
- tests: pass;
- research validation: pass;
- physical audit: pass.

## Main branch policy

Do not merge the research branch to `main` automatically just because R1 tests pass.

First provide a concise review of:

- branch diff;
- corpus non-drift evidence;
- research output counts;
- review decisions made;
- unresolved ambiguities;
- schema changes;
- test/validation results.

If repository workflow and user instruction clearly permit direct integration, use a non-destructive merge/PR workflow. Never force-update `main`.

## Final documentation requirement

Before ending the work, update on the appropriate authoritative branch:

- `PROJECT_HANDOVER.md`;
- `PROJECT_GUIDELINES.md` only if operating rules changed;
- `NEXT_CHAT_PROMPT.md`;
- `docs/CLASSICAL_TAMIL_RESEARCH_MATRIX.md` only if R1 changed requirements relevant to the matrix;
- `manifests/classical-tamil-research-program.json`;
- research programme decision log;
- R1 completion/baseline/idempotence reports.

The next handover must record actual GitHub commit/branch state.

The updated `NEXT_CHAT_PROMPT.md` at the end of R1 should point to **R1.5**, not R2.

## Final report

Report:

1. repository;
2. starting `main` commit;
3. starting R0 commit;
4. branch comparison;
5. new R1 branch;
6. R0 compatibility result against corpus 1.1.0;
7. R0 reconciliation method;
8. R0 assertion count before/after;
9. mention count before/after;
10. entity sample count before/after;
11. relationship count before/after;
12. assertion-ID drift;
13. evidence-span drift;
14. frozen corpus drift;
15. Tolkāppiyam drift;
16. research schema version;
17. review workflow changes;
18. reviewer model;
19. review events created;
20. mentions reviewed;
21. unresolved mentions;
22. entity-resolution decisions;
23. possible matches;
24. verified matches, if any;
25. rejected matches;
26. ambiguity register;
27. validator result;
28. test result;
29. physical audit;
30. first generation result;
31. second idempotence result;
32. files changed;
33. branch/PR/merge state;
34. updated handover path;
35. updated guidelines path;
36. updated next-chat prompt path;
37. confirmation that R1.5 is the next phase;
38. any R1 findings that require amendments to the concept matrix before R1.5.

Explicitly answer:

`Was R0 safely reconciled with the current 1.1.0 corpus without changing its evidence identity?`

Then answer:

`Is the R1 review and entity-resolution foundation complete and ready for R1.5, the Classical Tamil Concept Matrix phase?`

Do not begin R1.5 or R2 in the same pass unless explicitly instructed.

---

End of next-chat startup prompt.
