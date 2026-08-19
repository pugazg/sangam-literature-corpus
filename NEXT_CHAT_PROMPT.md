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
- Puṟanāṉūṟu `001.json` through `260.json` form the current materialized gap-free production prefix.
- Stabilization batch **003–010** is complete.
- Regular 25-record batches **011–035**, **036–060**, **061–085**, **086–110**, **111–135**, **136–160**, **161–185**, **186–210**, **211–235**, and **236–260** are complete.
- The next record is **261** and the next planned batch is **261–285**.
- Current production validation: **260 reviewed / 140 remaining / 4,628 observations / next 261**.
- Current canonical dimension count: **29**.
- Current regression suite: **224 passed**.
- Reviewed specs for 236–260 are `236-240.json`, `241-245.json`, `246-250.json`, `251-255.json`, and `256-260.json`.
- The core materializer expands already-reviewed semantic decisions; it is not a classifier.
- The range/source-state driver preserves blank metadata, absent source notes, audit-part boundaries, and exact `பெயர் தெரிந்திலது` unknown-poet attribution without turning that phrase into a named entity.
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

## Durable lessons from 236–260

- Record 236: preserve `கேண்மை`, `நட்பு`, `குறவர்` and body/source-note `பாரி` provenance without later identity expansion.
- Record 237: distinguish deceased `வெளிமான்` from addressee `இளவெளிமான்`; retain `கூற்றம்` / `ஊழ்` in source context.
- Record 238: the source-note quotation/comment on `கண்ணில் ஊமன் கடற் பட்டாங்கு` is explicit TIR and remains separate from body evidence.
- Record 241: preserve `வச்சிரத் தடக்கை நெடியோன் கோயிலுள்` without later named-deity identification.
- Record 242: preserve `கடவாயில் நல்லாதனார் பாடியது என்பதும் பாடம்` as alternate-attribution TIR; do not overwrite canonical poet metadata.
- Record 243: `நடுக்குற்று` / `சிலசொல்` are aging/body evidence; do not manufacture death evidence from `கையறுநிலை` alone.
- Record 244: incomplete fragment, lacuna present, all thinai/thurai/poet/addressee metadata null. Classify only surviving `பாணர்`, `விறலியர்`, `இரவல் மாக்கள்`, `வண்டு`, `தொடி`; do not reconstruct death from title/tradition.
- Records 246–247: preserve `உயவற் பெண்டிரேம்`, `கணவன்`, `கானவர்`, `அணங்குடை முன்றில்`, `கொழுநன்`, `இன்னுயிர் நடுங்கும்` without later named-practice, legal-status or sectarian inference.
- Record 249: preserve incomplete/lacuna state, alternate poet attribution, and printed Nacciṉārkkiṉiyar/Tolkāppiyam citation as TIR only. The Tolkāppiyam citation must not auto-classify the poem.
- Records 251–252: preserve `தாபத வாகை` source signs (`புரிசடை` / `சடை`, fire, plant gathering, `வேட்டுவன்`) without mapping to a later religious order.
- Record 254: preserve exact `என் மகன்`, `அன்னை`, `கிளை`, `மள்ள`.
- Record 255: preserve `அறனில் கூற்றே` without later deity mapping.
- Records 256–257: literal `பெயர் தெரிந்திலது` is unknown-attribution metadata, not a named entity. Preserve the literal metadata while keeping `named_entities` reviewed-empty unless body/source-note evidence independently qualifies.
- Record 259: preserve exact `மறவர்` and comparison-term `புலைத்தி` without later caste/community substitution.
- Record 260: preserve canonical `கரந்தை (பாடாண் திணையுமாம்) / கையறுநிலை செருவிடை வீழ்தல்` plus source-note `கையறு நிலையுமாம்`, `பாண்பாட்டுமாம்`, `பாடாண் பாட்டுமாம்` as separate TT/TIR variants without normalization.

Earlier source-terminology and provenance guardrails, including record 176 and 186–235, remain binding.

## Puṟanāṉūṟu sequence

Continue from record **261** and do not skip ahead. **Records 267 and 268 are source-lost and must remain unreconstructed.** Printed names remain source mentions unless separately resolved through permitted evidence.

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
2. Confirm the final/squashed production checkpoint is exactly **260 reviewed / 140 remaining / 4,628 observations / next 261**, with 29 canonical dimensions and 224 tests.
3. Confirm record 244 fragment-only handling, record 249 Tolkāppiyam citation boundary, records 256–257 unknown-attribution provenance, and record 260 alternate TT/TIR readings remain intact.
4. Review Puṟanāṉūṟu **261–285 sequentially**, source-first and against all 29 dimensions.
5. Preserve records **267–268** as source-lost/unreconstructed; do not infer missing poem content from title, metadata, audit, commentary, or external tradition.
6. Build compact contiguous reviewed specs without copying the old audit.
7. Materialize 261–285 into separate canonical production JSON records through the deterministic materializer/driver.
8. Publish the completed batch as one clean user-authored checkpoint and run the full normal PR workflow on that exact final squashed head.
9. If green, the next permitted batch is 286–310.

Do not start the Tolkāppiyam production pass. Do not start R2.
