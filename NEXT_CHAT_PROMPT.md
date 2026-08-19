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

The old R1.5 pre-merge audit remains a control/provenance artifact and is consulted only after fresh source review.

## Accepted state

- Corpus 1.1.0 remains frozen: 28 works / 7,234 canonical records.
- R0 schema `0.1.0` remains preserved: 2,867 assertions, 285 candidates, 43 pilot entities, 51 relationships.
- R1 schema `0.2.0` remains preserved with 8 append-only review events and 3 conservative entity decisions.
- R1.5 concept/observation schema remains `0.3.0`.
- Exact 29-dimension production vocabulary/schema remains machine-validated.
- Puṟanāṉūṟu `001.json` through `285.json` form the materialized gap-free production prefix.
- Stabilization batch **003–010** is complete.
- Regular 25-record batches **011–035**, **036–060**, **061–085**, **086–110**, **111–135**, **136–160**, **161–185**, **186–210**, **211–235**, **236–260**, and **261–285** are complete.
- The next record is **286** and the next planned batch is **286–310**.
- Current production validation: **285 reviewed / 115 remaining / 5,024 observations / next 286**.
- Current canonical dimension count: **29**.
- Current regression suite: **224 passed**.
- The completed 261–285 review is staged as one contiguous reviewed spec: `research/production/purananuru/review-specs/261-285.json`.
- The materializer expands already-reviewed semantic decisions; it is not a classifier.
- Existing R0 evidence may be attached only when it supports an already-made semantic decision and exact source text falls inside the selected evidence span.
- Tolkāppiyam remains a separate evidence stream and must not auto-classify Sangam poems.

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
7. stage the completed contiguous batch in a reviewed spec;
8. materialize separate canonical `NNN.json` records deterministically;
9. validate that the result extends the longest gap-free prefix with no skip.

### Low-latency publication rule

When the full 25-record batch can be completed in the same session, prefer **one contiguous 25-record reviewed spec and one materialization cycle** rather than five 5-record specs/runs. This was successfully proven on 261–285.

This is only a publication/materialization optimization. Semantic review remains strictly poem-by-poem and source-first. Do not batch-guess classifications, skip poems, consult the old audit early, or reduce provenance checks. Split specs remain acceptable when a session cannot finish the full batch or a source-state issue requires isolation.

After materialization, perform targeted checks for source-loss, lacunae, metadata/body boundaries and important audit discrepancies. Obtain the real observation total from the normal verifier, update docs once, squash to one clean user-authored checkpoint parented by the prior green checkpoint, then run final exact-head CI once.

## Durable lessons from 261–285

- Record 261: preserve `நடுகல்`, memorial naming/adornment, cattle recovery, lament, shorn hair and loss of ornaments as source-explicit memorial/mourning evidence.
- Record 262: preserve `உண்டாட்டு (தலை தோற்றமுமாம்)` as an alternate thurai/classification signal rather than normalizing it.
- Record 263: `தொழாதனை கழிதல் ஓம்புமதி` is explicit honoring/worship of the memorial stone; bare source-note `பாடியவர் / பாடப்பாட்டோர்` labels remain unresolved source-state/TIR evidence, not reconstructed identities.
- Records 264–265: preserve memorial-stone installation/adornment/name inscription and exact `கோவலர்` / `பரிசிலர்` without later identity expansion.
- Records **267–268 are source-lost**. No canonical body or thinai/thurai/poet/addressee metadata survives. Keep only work-level `literary_domain`; all other 28 dimensions remain reviewed-empty with explicit no-reconstruction notes. Do not infer missing content from title, audit, commentary or external tradition.
- Record 270: preserve exact `மறவர்` as source social/martial terminology.
- Record 272: keep `death_mourning_memory` reviewed-empty because the body does not explicitly state death; `செருவிடை வீழ்தல்` is metadata TT evidence and must not manufacture a body-level death claim.
- Records 277–280: preserve mother/son, father/husband/son, battlefield death, mourning, widow-like observances and body evidence while keeping kinship, ritual, emotion and death dimensions distinct.
- Record 281: preserve `வேம்பு`, யாழ், ஐயவி, ஆம்பல், `காஞ்சி` song, bells/smoke and wound-protection practices without mapping them to a later ritual or medical system.
- Record 282: incomplete/lacunose with null thinai/thurai; printed `திணையும் துறையும் தெரிந்தில.` is explicit classification-uncertainty TIR, not a basis for reconstruction.
- Record 283: incomplete/lacunose; preserve exact `கோசர்` and `பாண்பாட்டு (பாடாண் பாட்டும் ஆம்)` as an alternate thurai signal without later community/classification normalization.
- Record 285: incomplete/lacunose; retain camp, performance, warfare, wound, city/village, public honor and village-grant evidence without inventing a completed death claim.

Earlier source-terminology and provenance guardrails remain binding, including record 176, record 200, and 236–260.

## Puṟanāṉūṟu sequence

Continue from record **286** and do not skip ahead. Records 267–268 remain permanently source-lost/unreconstructed in this production edition. Printed names remain source mentions unless separately resolved through permitted evidence.

Do not start the Tolkāppiyam production pass until Puṟanāṉūṟu 001–400 is complete and validated.

## Validation

At each final published batch checkpoint require at minimum:

```bash
python3 scripts/validate_research_r15_dimensions.py --root .
python3 scripts/validate_r15_purananuru_production.py --root .
pytest -q
python3 scripts/audit_repository.py --root .
```

The GitHub workflow must also preserve R0/R1/R1.5 validation, deterministic R1 and R1.5 regeneration, Corpus 1.1.0/Tolkāppiyam non-drift, R1 primary-history non-mutation, and documentation continuity.

## Required next activity

1. Confirm PR #4 remains open, draft and unmerged; inspect live head and checks.
2. Confirm the final/squashed production checkpoint is exactly **285 reviewed / 115 remaining / 5,024 observations / next 286**, with 29 canonical dimensions and 224 tests.
3. Confirm records 267–268 source-lost handling, record 272 death-boundary, record 282 classification uncertainty, and record 283 alternate-thurai/lacuna provenance remain intact.
4. Review Puṟanāṉūṟu **286–310 sequentially**, source-first and against all 29 dimensions.
5. Prefer one contiguous `286-310.json` reviewed spec if the entire batch is completed in the session; do not weaken poem-by-poem scholarly review.
6. Materialize 286–310 once through the deterministic materializer/driver, then perform targeted generated-record checks.
7. Publish the completed batch as one clean user-authored checkpoint parented by the previous green checkpoint.
8. Run the full normal PR workflow on that exact final squashed head.
9. If green, the next permitted batch is **311–335**.

Do not start the Tolkāppiyam production pass. Do not start R2.
