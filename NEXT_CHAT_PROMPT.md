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
- Puṟanāṉūṟu `001.json` through `210.json` form the current materialized gap-free production prefix.
- Stabilization batch **003–010** is complete.
- Regular 25-record batches **011–035**, **036–060**, **061–085**, **086–110**, **111–135**, **136–160**, **161–185**, and **186–210** are complete.
- The next record is **211** and the next planned batch is **211–235**.
- Current production validation: **210 reviewed / 190 remaining / 3,736 observations / next 211**.
- Current canonical dimension count: **29**.
- Current regression suite: **224 passed**.
- Reviewed specs for 186–210 are `186-190.json`, `191-195.json`, `196-200.json`, `201-205.json`, and `206-210.json`.
- The core materializer expands already-reviewed semantic decisions; it is not a classifier.
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
7. stage the reviewed decision in a compact spec;
8. materialize separate canonical `NNN.json` records deterministically;
9. validate that the result extends the longest gap-free prefix with no skip.

Repository publication remains batched: one clean checkpoint and one full normal PR CI run per completed batch.

## Durable lessons from 186–210

- Record 194: null thinai/thurai/poet metadata and no source-note block remain null/absent; invent nothing.
- Record 195: retain `கணிச்சிக் கூர்ம்படைக் கடுந்திறல் ஒருவன்` as source imagery; do not identify it with a later named deity.
- Record 200: frozen body is only `???` / `???`; only work-level `literary_domain` qualifies and the other 28 dimensions remain explicitly reviewed-empty. Do not reconstruct from the title.
- Record 201: preserve `அந்தணன்`, `புலவன்`, `வேளிருள் வேளே`, `பாண்கடன்`; body-level `பறம்பு` / `பாரி` / `துவரை` remain direct source-review evidence with only genuinely matching body R0 support, separate from metadata identity evidence.
- Record 202: preserve `வேட்டுவர்`, `தொல்குடி`; tiger-striped comparison is imagery, not an asserted tiger occurrence; `புகழ்ந்த செய்யுள்` is explicit textual/intertextual evidence.
- Records 205–206: preserve `வேட்டுவ`, `பரிசிலர்`, `மரங்கொல் தச்சன்` exactly.
- Record 207: preserve `ஆளி` as source creature imagery without later taxonomy or mythic equivalence.
- Record 208: `வாணிகப் பரிசிலன் அல்லேன்` is direct `trade_exchange` evidence, not permission to infer a market system.
- Record 210: retain `கூற்றம்` as source death-agent/religious imagery without later deity/doctrine mapping.

Earlier source-terminology and provenance guardrails, including record 176, remain binding.

## Puṟanāṉūṟu sequence

Continue from record **211** and do not skip ahead. Preserve records 267 and 268 as source-lost/unreconstructed. Printed names remain source mentions unless separately resolved through permitted evidence.

Do not start the Tolkāppiyam production pass until Puṟanāṉūṟu 001–400 is complete and validated.

## Validation

At each published batch checkpoint require at minimum:

```bash
python3 scripts/validate_research_r15_dimensions.py --root .
python3 scripts/validate_r15_purananuru_production.py --root .
pytest -q
python3 scripts/audit_repository.py --root .
```

The GitHub workflow must also preserve R0/R1/R1.5 validation, deterministic R1 and R1.5 regeneration, Corpus 1.1.0/Tolkāppiyam non-drift, R1 primary-history non-mutation, and documentation continuity.

## Required next activity

1. Confirm PR #4 remains open, draft and unmerged; inspect live head and checks.
2. Confirm the final/squashed production checkpoint is exactly **210 reviewed / 190 remaining / 3,736 observations / next 211**, with 29 canonical dimensions and 224 tests.
3. Confirm the record-200 non-reconstruction, record-208 `trade_exchange`, and record-210 `கூற்றம்` provenance guardrails remain intact.
4. Review Puṟanāṉūṟu **211–235 sequentially**, source-first and against all 29 dimensions.
5. Build compact contiguous reviewed specs without copying the old audit.
6. Materialize 211–235 into separate canonical production JSON records through the repository's deterministic materializer/driver.
7. Publish the completed 25-record batch as one clean user-authored checkpoint.
8. Run the full normal PR workflow on the exact final squashed head.
9. If green, the next permitted batch is 236–260.

Do not start the Tolkāppiyam production pass. Do not start R2.
