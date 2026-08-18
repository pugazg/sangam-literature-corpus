# Next Chat Prompt — R1.5A batched 29-dimension production review

Continue directly in `pugazg/sangam-literature-corpus`.

Active branch: `research/classical-tamil-concept-matrix-r1.5a`.

Treat live GitHub state as authoritative.

## Phase boundary

R1.5 was explicitly authorized for merge and was merged into `main` at merge commit `d82f9c78f27f9c9daf8fbb913d01ddfb29bddba1`.

R1.5A is the follow-on production-review phase. It does **not** change the concept schema version (`0.3.0`) and it is **not R2**. R2 remains blocked until R1.5A is completed and the user explicitly authorizes a later phase transition.

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
12. current `main`, active R1.5A branch, active PR metadata, and latest checks.

The old R1.5 pre-merge audit remains a control/provenance artifact. Its old merge-hold prose is historical and must not override this prompt.

## Accepted state

- Corpus 1.1.0 remains frozen: 28 works / 7,234 canonical records.
- R0 evidence schema `0.1.0` remains preserved: 2,867 assertions, 285 candidates, 43 pilot entities, 51 relationships.
- R1 workflow schema `0.2.0` remains preserved with 8 append-only review events and 3 conservative entity decisions.
- R1.5 concept/observation schema remains `0.3.0`.
- The production concept vocabulary/schema is aligned to the exact canonical 29 dimensions and machine-validated against regression/collapse.
- Puṟanāṉūṟu production records `001.json` through `010.json` form the current gap-free production prefix.
- R1.5A stabilization batch `003–010` is complete.
- The next record is **011** and the next planned batch is **011–035**.
- `research/production/purananuru/review-specs/003-010.json` is the source-first reviewed batch specification for the completed stabilization batch.
- `scripts/materialize_r15a_purananuru_batch.py` deterministically expands reviewed batch specs into the individual production record schema. It is a materializer, not an automatic classifier.
- The exhaustive 400-record Puṟanāṉūṟu audit and 1,602-நூற்பா Tolkāppiyam audit are controls only; they are not the production matrix.
- Tolkāppiyam must not auto-classify Sangam poems.

## Exact 29-dimension surface

Use the IDs in `research/audits/r15-premerge/dimensions.json` and `research/controlled-vocabularies/concept-dimensions-r15.json` exactly:

`literary_domain`, `tinai_turai`, `landscape_environment`, `season_weather_time`, `flora`, `fauna`, `people_social_roles`, `relationships`, `emotion_lived_experience`, `occupations_production`, `food_subsistence`, `clothing_ornaments_adornment`, `material_culture_everyday_objects`, `weapons_warfare`, `mobility_transport`, `settlements_built_environment`, `economy`, `trade_exchange`, `polity_political_life`, `communities_social_groups`, `family_gender_kinship`, `religion_ritual`, `death_mourning_memory`, `arts_music_performance`, `knowledge_technology`, `values_ethical_concepts`, `body_health`, `named_entities`, `textual_intertextual_relationships`.

Do not collapse dimensions for convenience.

## R1.5A working cadence

The scholarly review remains strictly record-by-record and sequential; repository publishing is batched.

For each poem:

1. read the complete frozen canonical record and source-explicit metadata;
2. consider all 29 dimensions;
3. complete that record's reviewed decision state before reading the next poem;
4. stage the reviewed evidence selectors/decisions in the active compact batch spec under `research/production/purananuru/review-specs/`;
5. retain exact Tamil evidence, source spans, provenance, uncertainty, reviewed-empty states, and real R0 assertion links where they actually exist;
6. use `direct_record_review` only when semantic evidence is source-supported but no suitable prior R0 assertion exists;
7. preserve exact source terminology under `docs/SOURCE_TERMINOLOGY_POLICY.md`;
8. only after the fresh review is complete, compare with the old sparse audit control and record discrepancies;
9. deterministically materialize the batch into separate `research/production/purananuru/records/NNN.json` files;
10. validate that the result extends the longest gap-free prefix with no skipped record.

### Repository checkpoint cadence

- completed stabilization batch: **003–010**;
- active next batch: **011–035**;
- subsequent 25-record batches: **036–060, 061–085, ...**;
- final batch may be shorter to end exactly at 400;
- publish one deterministic multi-file Git checkpoint per completed batch rather than one commit per poem;
- run focused production validation while preparing the batch;
- run the full repository CI/non-drift suite once per published batch, not once per poem;
- if a batch cannot be completed in the current work session, checkpoint the completed contiguous prefix rather than discarding reviewed records.

The materializer must never manufacture semantic classifications. It only expands the already-reviewed batch spec into the canonical per-record JSON schema, computes deterministic observation IDs/provenance fields, and exposes any mismatch to validation.

## Puṟanāṉūṟu sequence

Continue from record **011** and do not skip ahead. Preserve record 200 as damaged where the frozen source is damaged. Preserve 267 and 268 as source-lost/unreconstructed. Printed names remain source mentions unless separately resolved through permitted evidence.

Do not start the Tolkāppiyam production pass until Puṟanāṉūṟu 001–400 is complete and validated.

## Validation

At each published batch checkpoint require at minimum:

```bash
python3 scripts/validate_research_r15_dimensions.py --root .
python3 scripts/validate_r15_purananuru_production.py --root .
pytest -q
python3 scripts/audit_repository.py --root .
```

The GitHub workflow must also preserve R0/R1/R1.5 deterministic checks, Corpus 1.1.0/Tolkāppiyam non-drift, and R1 primary-history non-mutation.

## Required next activity

1. Confirm PR #4 remains open, draft, unmerged and inspect the live head/check state.
2. Confirm the production validator reports a gap-free prefix through `010` and next record `011`.
3. Review Puṟanāṉūṟu records **011–035 sequentially**, source-first and against all 29 dimensions.
4. Build the compact reviewed batch spec for 011–035 without copying the old audit.
5. Materialize the individual 011–035 production JSON records deterministically.
6. Publish the completed 25-record batch as the next R1.5A checkpoint.
7. Validate the batch through the full PR workflow.
8. If green, continue with 036–060.

Do not start R2.
