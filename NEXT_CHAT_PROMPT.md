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
- Puṟanāṉūṟu `001.json` through `335.json` form the materialized gap-free production prefix.
- Stabilization batch **003–010** is complete.
- Regular **25-record** batches **011–035**, **036–060**, **061–085**, **086–110**, **111–135**, **136–160**, **161–185**, **186–210**, **211–235**, **236–260**, **261–285**, **286–310**, and **311–335** are complete.
- The next record is **336** and the next planned batch is **336–360**.
- Current production validation: **335 reviewed / 65 remaining / 5,866 observations / next 336**.
- Current canonical dimension count: **29**.
- Current regression suite: **224 passed**.
- 311–335 was semantically reviewed as one complete sequential source-first 25-poem batch, then published in five 5-record specs (`311-315.json` through `331-335.json`) for manageable connector writes and source-state isolation around record 323.
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

### Publication rule

Prefer one contiguous 25-record spec and one materialization cycle when practical; this was proven on 261–285 and 286–310. Split specs are allowed when connector/write size or a source-state case benefits from staged validation. The 311–335 batch used five 5-record specs only after all 25 semantic reviews were already completed source-first.

This changes publication granularity only. Do not batch-guess classifications, skip poems, consult the audit early, or reduce provenance checks.

After materialization, perform targeted checks for source loss, lacunae, metadata/body/source-note boundaries and substantive audit discrepancies. Obtain the real observation total from the normal verifier, update docs once, squash to one clean user-authored checkpoint parented by the prior green checkpoint, then run final exact-head CI.

## Source-state compatibility rule

The range-aware driver preserves exact unknown-poet/non-identification metadata without allowing those literals to become named entities. Current exact literals are:

- `பெயர் தெரிந்திலது`
- `பெயர் புலனாகவில்லை`
- `பாடப்பட்டோர் : பெயர்கள் தெரிந்தில`

These are restored verbatim to `source_metadata_reviewed.poet_as_printed` after core materialization and remain excluded from named-entity linking. This is compatibility handling, not semantic classification.

## Durable lessons from 311–335

- Record 311: preserve exact `புலைத்தி` as source occupational/social terminology without later identity substitution.
- Record 312: thinai/thurai/poet/addressee remain null and no printed source note survives; do not let the clear body duty sequence reconstruct metadata.
- Record 313: preserve exact `இரவன் மாக்கள்`, `உமணர்` and `உப்பொய் சாகாட்டு`; the salt-cart wording is trade evidence only, not a wider inferred market system.
- Record 315: keep printed poet/`பாடப்பட்டோன்` attribution distinct from body `நெடுமான் அஞ்சி`; source relation is TIR.
- Record 317: incomplete/lacunose; do not reconstruct missing text.
- Record 319: preserve exact canonical `யாம் க·டு உண்டென`; do not silently repair it.
- Record 321: incomplete/lacunose; surviving sword-scar / `செருவெங் குருசில்` evidence supports warfare without reconstructing the lacuna.
- Record 322: preserve `கரும்பின் எந்திரம்` as source-explicit processing/mechanical evidence and `கண்படை ஈயா` as a body-state signal.
- Record 323: incomplete/lacunose; preserve `பாடப்பட்டோர் : பெயர்கள் தெரிந்தில` and source-note `பாடியவர் பாடப்பட்டோர் : பெயர்கள் தெரிந்தில.` as unresolved attribution; `named_entities` remains reviewed-empty.
- Record 324: preserve exact `வேட்டுவர்`, `இடையன்`, `பாணர்` without later identity substitution.
- Records 327–328: preserve exact `பெயர் தெரிந்திலது`; 328 remains lacunose and neither record manufactures an entity.
- Record 329: `நடுகல்`, `நாட்பலி`, water, ghee/fragrance and smoke form an explicit memorial-stone ritual sequence; do not import a later doctrinal system.
- Record 331: preserve `உறையூர் முது கூற்றனார் எனவும் பாடம்` as alternate poet reading/TIR; `போகுபலி வெண்சோறு` is source offering language only.
- Record 332: preserve exact `மறவன்` as source martial/social terminology.
- Record 333: incomplete/lacunose with `பெயர் தெரிந்திலது`; `named_entities` remains reviewed-empty and damaged text is not reconstructed.
- Record 334: incomplete/lacunose; retain only surviving adornment wording.
- Record 335: incomplete/lacunose; retain only surviving plant names (`குருந்து`, `முல்லை`, `வரகு`, `தினை`, `கொள்ளு`, `அவரை`); preserve exact `துடியன், பாணன், பறையன், கடம்பன்`; treat `கல்லே பரவின் ... நெல்உகுத்துப் பரவும் கடவுளும் இலவே` as this poem's memorial-worship/deity language, not a generalized historical absence claim.

Earlier source-terminology and provenance guardrails remain binding, including record 176, damaged record 200, and source-lost records 267–268.

## Puṟanāṉūṟu sequence

Continue from record **336** and do not skip ahead. Printed names remain source mentions unless separately resolved through permitted evidence.

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
2. Confirm the final/squashed production checkpoint is exactly **335 reviewed / 65 remaining / 5,866 observations / next 336**, with 29 canonical dimensions and 224 tests.
3. Confirm record 312 absent metadata/source-note handling, record 323 unknown-attribution handling, record 329 memorial ritual, record 331 alternate attribution, record 333 lacuna/unknown poet, and record 335 terminology/ritual/lacuna boundaries remain intact.
4. Review Puṟanāṉūṟu **336–360 sequentially**, source-first and against all 29 dimensions.
5. Materialize through the deterministic materializer/driver and perform targeted generated-record checks.
6. Publish one clean user-authored checkpoint parented by the previous green checkpoint.
7. Run the full normal PR workflow on that exact final squashed head.
8. If green, the next permitted batch is **361–385**.

Do not start the Tolkāppiyam production pass. Do not start R2.
