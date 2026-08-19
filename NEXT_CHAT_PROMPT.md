# Next Chat Prompt — R1.5A batched 29-dimension production review

Continue directly in `pugazg/sangam-literature-corpus`.

Active branch: `research/classical-tamil-concept-matrix-r1.5a`.

Treat live GitHub state as authoritative.

## Phase boundary

R1.5 was explicitly authorized and merged into `main` at `d82f9c78f27f9c9daf8fbb913d01ddfb29bddba1`.

R1.5A keeps concept/observation schema `0.3.0` and is **not R2**. R2 remains blocked until R1.5A is completed and the user explicitly authorizes a later transition.

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

The old R1.5 pre-merge audit remains a post-review control/provenance artifact. Do not consult it before fresh source decisions are complete.

## Accepted state

- Corpus 1.1.0 remains frozen: 28 works / 7,234 canonical records.
- R0 schema `0.1.0` remains preserved: 2,867 assertions, 285 candidates, 43 pilot entities, 51 relationships.
- R1 schema `0.2.0` remains preserved with 8 append-only review events and 3 conservative entity decisions.
- R1.5 concept/observation schema remains `0.3.0`.
- Exact 29-dimension production vocabulary/schema remains machine-validated.
- Puṟanāṉūṟu `001.json` through `360.json` form the materialized gap-free production prefix.
- Stabilization batch **003–010** is complete.
- Regular **25-record** semantic batches begin at **011–035** and continue through **336–360**.
- The next record is **361** and the next planned batch is **361–385**.
- Current production validation: **360 reviewed / 40 remaining / 6,304 observations / next 361**.
- Current canonical dimension count: **29**.
- Current regression suite: **224 passed**.
- 336–360 was semantically reviewed as one complete sequential source-first 25-poem batch before either old control ledger was opened, then published in six compact specs: `336-340.json`, `341-343.json`, `344-345.json`, `346-350.json`, `351-355.json`, `356-360.json`.
- The materializer expands already-reviewed semantic decisions; it is not a classifier.
- Existing R0 evidence may attach only when it supports an already-made semantic decision and exact source text falls inside selected evidence.
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
4. preserve exact Tamil evidence, spans, uncertainty, reviewed-empty states and source terminology;
5. never let R0 assertions or the old audit manufacture a classification;
6. only after fresh review, compare with the correct sparse audit and record discrepancies;
7. stage the completed contiguous batch in reviewed specs;
8. materialize separate canonical `NNN.json` records deterministically;
9. validate that the result extends the longest gap-free prefix with no skip.

Prefer one contiguous 25-record spec when practical. Split specs are valid when connector/write size or source-state isolation benefits from staged validation. Publication granularity never changes the poem-by-poem semantic-review rule.

After materialization, perform targeted checks for source loss, lacunae, metadata/body/source-note boundaries and substantive audit discrepancies. Obtain the real observation total from the normal verifier, update docs once, squash to one clean user-authored checkpoint parented by the prior green checkpoint, then run final exact-head CI.

## Source-state compatibility rule

The range-aware driver preserves exact unknown-poet/non-identification metadata without allowing those literals to become named entities. Current exact literals remain:

- `பெயர் தெரிந்திலது`
- `பெயர் புலனாகவில்லை`
- `பாடப்பட்டோர் : பெயர்கள் தெரிந்தில`

No new driver literal was added for 344–345. Their full frozen attribution remains printed in `source_metadata_reviewed.poet_as_printed`, while the reviewed named-entity note distinguishes named poet `அடைநெடுங் கல்வியார்` from explicitly unknown `பாடப்பட்டோன்`.

## Durable lessons from 336–360

- 336: preserve exact `மறவர்`, family conflict and `அறன்இலன்` without later identity-system mapping.
- 337: incomplete/lacunose; do not reconstruct; `சோணாட்டு`, `பாரி`, `பறம்பு` remain unresolved source mentions.
- 338: preserve the printed `சிறப்பு` note about `நெடுவேள் ஆதன்` / `போந்தை` as source-context/TIR evidence distinct from the body.
- 339–340: incomplete/lacunose with exact `பெயர் தெரிந்திலது`; `named_entities` remains reviewed-empty; preserve exact `கோவலர்` in 339.
- 341: preserve `வாரா உலகம்` as source other-world/death language within the marriage-versus-battle alternative, without later doctrine.
- 343: fish-for-rice exchange, ship-borne gold and mountain/sea goods are direct exchange evidence only; do not infer a wider market system. `குட்டுவன்` / `முசிறி` remain unresolved.
- 344–345: frozen `அடைநெடுங் கல்வியார் பாடப்பட்டோன்: பெயர் தெரிந்திலது` means named poet plus explicitly unidentified sung person, not one composite identity. Alternate source-note `வாகை / மூதின் முல்லை` is additional TT/TIR and does not replace canonical `காஞ்சி / மகட்பாற் காஞ்சி`.
- 346–347: incomplete/lacunose; no reconstruction. 347 keeps `அகுதை`, `கூடல்` unresolved and `நறுங் கள்ளின்` source-bound.
- 348: preserve `பாண் சேரி`, `தண்ணுமை`, `தழும்பன்`, `ஊணூர்` without later community expansion.
- 349: preserve exact `அணங்கு` only as the poem's destructive/sacred-power wording without later deity/doctrine identification.
- 352: preserve `இடையிடை சிதைவுற்ற செய்யுள் இது` and `சிறப்பு: தித்தன் காலத்து உறந்தையின் நெல் வளம்.` as damage/source-context evidence; do not reconstruct damaged lines.
- 353: preserve exact `தொல்குடி`; `பஞ்சியும் களையாப் புண்ணர்` is source body/care evidence, not a modern diagnosis or medical-system mapping.
- 355: strict source-loss boundary; poet unknown, thurai literally `பெயர் தெரிந்திலது`, and `தோற்றக் கிடையாத போயின செய்யுள் இது.` is TIR/source-loss evidence; do not reconstruct.
- 356: `ஈம விளக்கு`, `சுடலை`, ash/bones, ghost-women imagery and tears are source funerary/death evidence without later doctrinal expansion.
- 358: preserve `தவம்` and canonical `மனையறம், துறவறம்` as source ethical/ascetic vocabulary without later doctrinal import.
- 360: preserve exact `புலையன்` without later caste/community equivalence; keep cremation/funerary-food context source-bound.

Earlier source-terminology and provenance guardrails remain binding, including record 176, damaged record 200, and source-lost records 267–268.

## Puṟanāṉūṟu sequence

Continue from record **361** and do not skip ahead. Printed names remain source mentions unless separately resolved through permitted evidence.

Do not start the Tolkāppiyam production pass until Puṟanāṉūṟu 001–400 is complete and validated.

## Validation

At each final published batch checkpoint require at minimum:

```bash
python3 scripts/validate_research_r15_dimensions.py --root .
python3 scripts/validate_r15_purananuru_production.py --root .
pytest -q
python3 scripts/audit_repository.py --root .
```

The GitHub workflow must also preserve R0/R1/R1.5 validation, deterministic R1/R1.5 regeneration, Corpus 1.1.0/Tolkāppiyam non-drift, R1 primary-history non-mutation and documentation continuity.

## Required next activity

1. Confirm PR #4 remains open, draft and unmerged; inspect live head and checks.
2. Confirm the final/squashed production checkpoint is exactly **360 reviewed / 40 remaining / 6,304 observations / next 361**, with 29 canonical dimensions and 224 tests.
3. Confirm 344–345 composite attribution/alternate classification, 352 damage/`சிறப்பு`, 355 source-loss/unknown thurai, 356 funerary evidence, 358 ascetic terminology and 360 exact `புலையன்` handling remain intact.
4. Review Puṟanāṉūṟu **361–385 sequentially**, source-first and against all 29 dimensions.
5. Materialize through the deterministic materializer/driver and perform targeted generated-record checks.
6. Publish one clean user-authored checkpoint parented by the previous green checkpoint.
7. Run the full normal PR workflow on that exact final squashed head.
8. If green, the final Puṟanāṉūṟu batch is **386–400**.

Do not start the Tolkāppiyam production pass. Do not start R2.
