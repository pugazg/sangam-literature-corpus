# Next Chat Prompt — R1.5A batched 29-dimension production review

Continue directly in `pugazg/sangam-literature-corpus`.

Active branch: `research/classical-tamil-concept-matrix-r1.5a`.

Treat live GitHub state as authoritative.

## Phase boundary

R1.5 was explicitly authorized for merge and merged into `main` at `d82f9c78f27f9c9daf8fbb913d01ddfb29bddba1`.

R1.5A is the follow-on production-review phase. It keeps concept/observation schema `0.3.0` and is **not R2**. R2 remains blocked until R1.5A is completed and the user explicitly authorizes a later transition.

## Mandatory startup

Before changing the repository, read completely:

1. `docs/DOCUMENTATION_STATUS.md`
2. `docs/SOURCE_TERMINOLOGY_POLICY.md`
3. `PROJECT_HANDOVER.md`
4. `PROJECT_GUIDELINES.md`
5. `NEXT_CHAT_PROMPT.md`
6. `docs/handover/r15a-production-review/README.md`
7. `research/production/purananuru/README.md`
8. `docs/handover/r15-premerge-audit/04-29-DIMENSION-PRODUCTION-REVIEW.md`
9. `research/audits/r15-premerge/dimensions.json`
10. `research/controlled-vocabularies/concept-dimensions-r15.json`
11. `scripts/materialize_r15a_purananuru_batch.py`
12. `scripts/materialize_r15a_purananuru_batch_driver.py`
13. `.github/workflows/materialize-r15a-purananuru-batch.yml`
14. current `main`, active R1.5A branch, PR #4 metadata, and latest checks.

The old R1.5 pre-merge audit remains a control/provenance artifact. Its old merge-hold prose is historical.

## Accepted state

- Corpus 1.1.0 remains frozen: 28 works / 7,234 canonical records.
- R0 schema `0.1.0` remains preserved: 2,867 assertions, 285 candidates, 43 pilot entities, 51 relationships.
- R1 schema `0.2.0` remains preserved with 8 append-only review events and 3 conservative entity decisions.
- R1.5 concept/observation schema remains `0.3.0`.
- Exact 29-dimension production vocabulary/schema remains machine-validated.
- Puṟanāṉūṟu `001.json` through `060.json` form the current materialized gap-free production prefix.
- Stabilization batch **003–010** is complete.
- Regular 25-record batches **011–035** and **036–060** are complete.
- The next record is **061** and the next planned batch is **061–085**.
- Compact reviewed specs exist under `research/production/purananuru/review-specs/` for completed R1.5A batches.
- The core materializer expands already-reviewed semantic decisions; it is not a classifier.
- The range-aware driver selects the correct 50-record audit control and handles specs that cross audit-part boundaries.
- Existing R0 evidence may be attached only when it supports an already-made semantic decision and its exact source text falls inside the selected evidence span.
- The materialization workflow processes only review-spec files changed in its triggering commit, protecting completed historical batches from regeneration drift.
- The exhaustive Puṟanāṉūṟu and Tolkāppiyam audits remain controls only.
- Tolkāppiyam must not auto-classify Sangam poems.

## Exact 29-dimension surface

Use these IDs exactly:

`literary_domain`, `tinai_turai`, `landscape_environment`, `season_weather_time`, `flora`, `fauna`, `people_social_roles`, `relationships`, `emotion_lived_experience`, `occupations_production`, `food_subsistence`, `clothing_ornaments_adornment`, `material_culture_everyday_objects`, `weapons_warfare`, `mobility_transport`, `settlements_built_environment`, `economy`, `trade_exchange`, `polity_political_life`, `communities_social_groups`, `family_gender_kinship`, `religion_ritual`, `death_mourning_memory`, `arts_music_performance`, `knowledge_technology`, `values_ethical_concepts`, `body_health`, `named_entities`, `textual_intertextual_relationships`.

Do not collapse dimensions for convenience.

## R1.5A working cadence

The scholarly review remains strictly record-by-record and sequential; repository publishing is batched.

For each poem:

1. read the complete frozen canonical record and source-explicit metadata;
2. consider all 29 dimensions;
3. complete that record's semantic decision state before reading the next poem;
4. stage exact evidence selectors/decisions in the active compact review spec;
5. preserve exact Tamil evidence, source spans, uncertainty, reviewed-empty states, and source terminology;
6. attach real R0 assertion IDs only where they actually support the already-reviewed observation;
7. never let R0 assertions or the old audit manufacture a dimension classification;
8. only after fresh review, compare with the correct 50-record sparse audit control and record discrepancies;
9. materialize separate `research/production/purananuru/records/NNN.json` records deterministically;
10. validate that the result extends the longest gap-free prefix with no skip.

### Repository checkpoint cadence

- completed stabilization batch: **003–010**;
- completed regular batches: **011–035**, **036–060**;
- active next batch: **061–085**;
- subsequent 25-record batches: **086–110, 111–135, ...**;
- final batch may be shorter to end exactly at 400;
- publish one deterministic multi-file checkpoint per completed batch;
- run full repository CI/non-drift once per published batch, not once per poem;
- if interrupted, checkpoint the completed contiguous prefix.

A generated bot commit may not itself run the normal PR workflow. Finish each activity on a user-authored/squashed branch head and require that exact head's full PR workflow to be green.

## Puṟanāṉūṟu sequence

Continue from record **061** and do not skip ahead. Preserve record 200 as damaged where the frozen source is damaged. Preserve 267 and 268 as source-lost/unreconstructed. Printed names remain source mentions unless separately resolved through permitted evidence.

Do not start the Tolkāppiyam production pass until Puṟanāṉūṟu 001–400 is complete and validated.

## Validation

At each published batch checkpoint require at minimum:

```bash
python3 scripts/validate_research_r15_dimensions.py --root .
python3 scripts/validate_r15_purananuru_production.py --root .
pytest -q
python3 scripts/audit_repository.py --root .
```

The GitHub workflow must also preserve R0/R1/R1.5 deterministic checks, Corpus 1.1.0/Tolkāppiyam non-drift, R1 primary-history non-mutation, and documentation continuity.

## Required next activity

1. Confirm PR #4 remains open, draft and unmerged; inspect the live head/check state.
2. Confirm the production validator reports a gap-free prefix through `060` and next record `061`.
3. Review Puṟanāṉūṟu **061–085 sequentially**, source-first and against all 29 dimensions.
4. Build the compact reviewed batch spec without copying the old audit.
5. Materialize 061–085 into separate canonical production JSON records through the range-aware driver.
6. Publish the completed 25-record batch as one R1.5A checkpoint.
7. Run the full PR workflow on the final user-authored/squashed head.
8. If green, continue with 086–110.

Do not start R2.
