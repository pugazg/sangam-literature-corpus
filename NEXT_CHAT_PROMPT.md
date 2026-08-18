# Next Chat Prompt — R2 Core Sangam Concept-Matrix Extraction

<!-- R15_ACCEPTANCE_COMPLETE_20260818 -->

Treat current GitHub state as authoritative. R0, R1, and R1.5 are completed
foundations and must not be restarted or reimplemented.

**Do not begin R2 unless the validated R1.5 PR has been merged into `main`.** If
R1.5 remains open/unmerged, stop at repository-state verification and preserve
the merge gate.

## Mandatory startup

Before making any repository change, read these files completely:

1. `PROJECT_HANDOVER.md`
2. `PROJECT_GUIDELINES.md`
3. `NEXT_CHAT_PROMPT.md`
4. `docs/CLASSICAL_TAMIL_RESEARCH_MATRIX.md`
5. `docs/classical-tamil-research-layer.md`
6. `research/README.md`
7. `manifests/classical-tamil-research-program.json`
8. `research/concepts/classical-tamil/concept-registry-r15.json`
9. `research/controlled-vocabularies/classification-bases-r15.json`
10. `research/controlled-vocabularies/concept-dimensions-r15.json`
11. `research/controlled-vocabularies/concept-evidence-policies-r15.json`
12. `research/schemas/concept-observation-r15.schema.json`
13. `research/schemas/tolkappiyam-concept-evidence-r15.schema.json`
14. `research/reports/purananuru-r15-pilot-summary.json`
15. `logs/classical-tamil-research-r15-validation-20260818T164600.json`
16. `logs/classical-tamil-research-r15-acceptance-20260818T164600.json`
17. `logs/classical-tamil-research-r15-idempotence-20260818T164600.json`
18. `logs/classical-tamil-research-r15-baseline-20260818T164600.json`
19. `logs/classical-tamil-research-program-decisions.md`
20. `docs/history/NEXT_CHAT_PROMPT_R15.md`

Then inspect live `main`, all current branches, open PRs, recent commits, tags,
workflow status, and the relevant repository tree. Current GitHub state overrides
historical SHAs or stale branch names in older prose.

## Accepted boundary inherited from R1.5

Preserve all of these invariants:

- R0 source evidence remains schema `0.1.0` and retains its original source-release provenance.
- R1 review/entity workflow remains schema `0.2.0` with append-only primary histories.
- R1.5 concept/observation infrastructure remains schema `0.3.0` unless R2 introduces an explicitly documented compatible version change.
- Matrix cells are deterministic views over provenance-bearing observations, never unsupported booleans.
- Empty cells mean only “qualifying evidence is not currently recorded”; they do not establish historical absence.
- Source-explicit, mechanically derived, cross-text, grammatical, editorial, external-historical, and interpretive claims remain distinct evidence classes/bases.
- Named-entity mention classification never by itself establishes historical identity.
- Conventional textbook landscape/tiṇai associations are not source facts unless separately evidenced.
- Tolkāppiyam remains a separate grammatical/poetics evidence stream and must not silently auto-classify poem records.
- Frozen canonical corpus, sources, apparatus, and release manifests must not be modified by research extraction.

## R2 goal

Apply the validated concept-matrix architecture across the **nine frozen core
Sangam works**:

1. Naṟṟiṇai
2. Aiṅkuṟunūṟu
3. Kuruntokai
4. Akanāṉūṟu
5. Puṟanāṉūṟu
6. Pattuppāṭṭu
7. Patiṟṟuppattu
8. Paripāṭal
9. Kalittokai

R2 is not permission for one-shot bulk tagging. Use staged, deterministic,
reviewable extraction with explicit gates.

## Required R2 startup activity

Before corpus-wide generation:

1. verify all nine frozen work inventories and protected conditions against Corpus 1.1.0;
2. define the R2 schema/version boundary and compatibility with R1.5 `0.3.0`;
3. define deterministic work order and record order;
4. define assertion/observation generation rules per evidence class and concept family;
5. define source-metadata versus literary-body extraction rules separately;
6. define how source-printed Akam/Puram, tiṇai, and tuṟai values are represented without inventing absent classifications;
7. define review queues for uncertain, inferred, entity-like, and cross-text cases;
8. define named-entity mention extraction separately from historical resolution;
9. define validation for orphan concepts, assertions, observations, relationships, duplicate IDs, invalid evidence spans, source-hash drift, and unsupported classification bases;
10. define deterministic matrix/report exports and idempotence checks;
11. create an R2 baseline before large-scale population.

## Bounded rollout rule

Start with a small representative batch spanning both Akam- and Puram-oriented
works and multiple metadata/source conditions. Validate the entire pipeline and
its evidence semantics before expanding to all nine works.

Do not infer that a feature is absent because no observation was generated.
Do not create external historical identities or interpretations merely to fill
matrix cells.

## Acceptance gates before R2 expansion

At every expansion gate require:

- generation succeeds deterministically;
- validators report zero errors;
- review/ambiguity states remain explicit;
- all observations trace to valid evidence/provenance;
- primary histories remain append-only;
- full repository tests pass;
- repository audit passes;
- Corpus 1.1.0 and Tolkāppiyam non-drift checks pass;
- outputs regenerate byte-for-byte;
- programme decisions, handover, and next prompt are updated before moving to a materially broader extraction stage.

Do not modify the canonical text to make research extraction easier.
