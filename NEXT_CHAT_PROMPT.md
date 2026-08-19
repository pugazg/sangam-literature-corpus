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
- Puṟanāṉūṟu `001.json` through `160.json` form the current materialized gap-free production prefix.
- Stabilization batch **003–010** is complete.
- Regular 25-record batches **011–035**, **036–060**, **061–085**, **086–110**, **111–135**, and **136–160** are complete.
- The next record is **161** and the next planned batch is **161–185**.
- Current production validation: **160 reviewed / 240 remaining / 2,939 observations / next 161**.
- Current regression suite: **224 passed**.
- Reviewed specs for 136–160 are `136-140.json`, `141-145.json`, `146-150.json`, and single-record specs `151.json` through `160.json`; spec splitting is staging only.
- The core materializer expands already-reviewed semantic decisions; it is not a classifier.
- The range-aware driver selects the correct 50-record audit control and preserves frozen source anomalies without inventing evidence.
- Existing R0 evidence may be attached only when it supports an already-made semantic decision and exact source text falls inside the selected evidence span.
- The materialization workflow processes only review specs changed in its triggering commit, protecting completed historical batches from regeneration drift.
- The exhaustive Puṟanāṉūṟu and Tolkāppiyam audits remain controls only.
- Tolkāppiyam must not auto-classify Sangam poems.

## Exact 29-dimension surface

Use these IDs exactly:

`literary_domain`, `tinai_turai`, `landscape_environment`, `season_weather_time`, `flora`, `fauna`, `people_social_roles`, `relationships`, `emotion_lived_experience`, `occupations_production`, `food_subsistence`, `clothing_ornaments_adornment`, `material_culture_everyday_objects`, `weapons_warfare`, `mobility_transport`, `settlements_built_environment`, `economy`, `trade_exchange`, `polity_political_life`, `communities_social_groups`, `family_gender_kinship`, `religion_ritual`, `death_mourning_memory`, `arts_music_performance`, `knowledge_technology`, `values_ethical_concepts`, `body_health`, `named_entities`, `textual_intertextual_relationships`.

Do not collapse dimensions for convenience.

## R1.5A working cadence

For each poem:

1. read the complete frozen canonical record and source-explicit metadata;
2. consider all 29 dimensions;
3. complete that record's semantic decision state before reading the next poem;
4. preserve exact Tamil evidence, source spans, uncertainty, reviewed-empty states, and source terminology;
5. never let R0 assertions or the old audit manufacture a dimension classification;
6. only after fresh review, compare with the correct sparse audit control and record discrepancies;
7. stage the reviewed decision in a compact spec;
8. materialize separate canonical `NNN.json` records deterministically;
9. validate that the result extends the longest gap-free prefix with no skip.

Repository publication remains batched: one clean checkpoint and one full normal PR CI run per completed batch.

## Source-state lessons from 136–160

Preserve exact source states, including:

- 137 canonical `இயன் மொழி` remains separate from source-note `பரிசில் துறையும் ஆம்`;
- 141 canonical `பாணாற்று படை` remains separate from source-note `புலவராற்றுப் படையும் ஆம்`;
- 143 retains exact `குறவர் மாக்கள்`, `உயர்பலி`, `கடவுள்`, source-note `கண்ணகி`, and alternative `தாபதநிலையும் ஆம்` without later substitution;
- 145 keeps alternative authorship `பரணர் பாட்டு எனவும் கொள்வர்` only as source-note evidence;
- 150 keeps exact `வேட்டுவக் குடியினன்` and the printed source note's trailing comma;
- 151 keeps frozen malformed addressee `இளவிச்சிக்கோ. திணை: பாடாண்`; source-note `இளங் கண்டீரக்கோ` remains separate;
- 152 keeps exact `வேட்டுவர்` and source-note `வேட்டுவக் குடியினன்`;
- 157 keeps exact `குறவர் பெருமகன்` and source-note `குறவர் குடியினன்`;
- 158 keeps poet `; பெருஞ்சித்திரனார்`, addressee `குமணன். திணை; பாடாண்`, `மோசி பாடிய ஆயும்`, `எழுவர் மாய்ந்த பின்றை`, and source-note `எழுவர் வள்ளல்கள்` / `பரிசில் கடாநிலையும் ஆம்` exactly;
- 159–160 keep poet `; பெருஞ்சித்திரனார்`; 159 explicitly lacks salt and buttermilk; 160's `மறப்புலி` is imagined verbal imagery, not an actual tiger occurrence.

## Puṟanāṉūṟu sequence

Continue from record **161** and do not skip ahead. Preserve record 200 as damaged where the frozen source is damaged. Preserve 267 and 268 as source-lost/unreconstructed. Printed names remain source mentions unless separately resolved through permitted evidence.

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
2. Confirm the production validator reports a gap-free prefix through `160` and next record `161`.
3. Review Puṟanāṉūṟu **161–185 sequentially**, source-first and against all 29 dimensions.
4. Build compact contiguous reviewed specs without copying the old audit.
5. Materialize 161–185 into separate canonical production JSON records through the range-aware driver.
6. Publish the completed 25-record batch as one R1.5A checkpoint.
7. Run the full PR workflow on the final user-authored/squashed head.
8. If green, continue with 186–210.

Do not start R2.
