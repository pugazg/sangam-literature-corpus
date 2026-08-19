# Next Chat Prompt — R1.5A batched 29-dimension production review

Continue directly in `pugazg/sangam-literature-corpus`.

Active branch: `research/classical-tamil-concept-matrix-r1.5a`.

Treat live GitHub state as authoritative.

## Phase boundary

R1.5 was explicitly authorized for merge and merged into `main` at `d82f9c78f27f9c9daf8fbb913d01ddfb29bddba1`.

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

The old R1.5 pre-merge audit remains a control/provenance artifact and is consulted only after fresh source review.

## Accepted state

- Corpus 1.1.0 remains frozen: 28 works / 7,234 canonical records.
- R0 schema `0.1.0` remains preserved: 2,867 assertions, 285 candidates, 43 pilot entities, 51 relationships.
- R1 schema `0.2.0` remains preserved with 8 append-only review events and 3 conservative entity decisions.
- R1.5 concept/observation schema remains `0.3.0`.
- Exact 29-dimension production vocabulary/schema remains machine-validated.
- Puṟanāṉūṟu `001.json` through `310.json` form the materialized gap-free production prefix.
- Stabilization batch **003–010** is complete.
- Regular 25-record batches **011–035**, **036–060**, **061–085**, **086–110**, **111–135**, **136–160**, **161–185**, **186–210**, **211–235**, **236–260**, **261–285**, and **286–310** are complete.
- The next record is **311** and the next planned batch is **311–335**.
- Current production validation: **310 reviewed / 90 remaining / 5,430 observations / next 311**.
- Current canonical dimension count: **29**.
- Current regression suite: **224 passed**.
- The completed 286–310 review is staged as one contiguous reviewed spec: `research/production/purananuru/review-specs/286-310.json`.
- The materializer expands already-reviewed semantic decisions; it is not a classifier.
- Existing R0 evidence may be attached only when it supports an already-made semantic decision and exact source text falls inside selected evidence.
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
7. stage the completed contiguous batch in a reviewed spec;
8. materialize separate canonical `NNN.json` records deterministically;
9. validate that the result extends the longest gap-free prefix with no skip.

### Low-latency publication rule

When the full 25-record batch can be completed in the same session, prefer **one contiguous 25-record reviewed spec and one materialization cycle**. This has been proven on 261–285 and 286–310.

This is only a publication/materialization optimization. Semantic review remains strictly poem-by-poem and source-first. Do not batch-guess classifications, skip poems, consult the old audit early or reduce provenance checks.

After materialization, perform targeted checks for source-loss, lacunae, metadata/body/source-note boundaries and important audit discrepancies. Obtain the real observation total from the normal verifier, update docs once, squash to one clean user-authored checkpoint parented by the prior green checkpoint, then run final exact-head CI once.

## Source-state compatibility rule

The range-aware driver preserves exact unknown-poet metadata without allowing non-identification phrases to become named entities. Current exact literals are:

- `பெயர் தெரிந்திலது`
- `பெயர் புலனாகவில்லை`

These literals are restored verbatim to `source_metadata_reviewed.poet_as_printed` after core materialization and remain excluded from named-entity linking. This is a compatibility rule, not semantic classification.

## Durable lessons from 286–310

- Record 287: preserve exact `புலைய` and `இழிசின` without later caste/community substitution.
- Record 288: incomplete/lacunose; classify only surviving spear/chest/blood/vulture battlefield evidence and do not reconstruct the lacuna.
- Record 289: thinai/thurai remain null; printed `திணை, துறை. தெரிந்தில.` is classification-uncertainty TIR. Preserve `உழவன்`, `தொல்குடி`, `பாண`, `இழிசினன்` exactly.
- Record 294: preserve `கூற்றுவினை` as source death-agent imagery without later deity/doctrine mapping.
- Record 296: preserve `வேம்பு`, `காஞ்சி`, நெய் and `ஐயவி` smoke without later ritual/medical-system mapping.
- Record 297: `பாடினோர் பாடப்பட்டோன் : பெயர்கள் தெரிந்தில.` is unresolved attribution TIR; `named_entities` remains reviewed-empty.
- Record 298: no source-note block and null thinai/thurai/poet/addressee; preserve those states and keep `named_entities` reviewed-empty.
- Record 299: preserve TT `நொச்சி / குதிரை மறம்` and literal `அணங்குஉடை முருகன் கோட்டத்துக் / கலம்தொடா மகளிர்`; body `முருகன்` is only a source-explicit named sacred referent, not a later doctrinal/temple/caste classification.
- Record 302: preserve `வெறிபாடிய காமக் கண்ணியார் (காமக் கணியார் எனவும் பாடம்)` and retain the alternate attribution as TIR.
- Record 305: preserve exact `பார்ப்பான்` / `பார்ப்பன வாகை` without later caste/doctrinal substitution.
- Record 306: incomplete/lacunose; `நடுகல் கைதொழுது பரவும்` is explicit memorial-stone honoring/worship and death-memory evidence without later ritual-system mapping.
- Record 307: preserve exact unknown poet metadata `பெயர் புலனாகவில்லை`; `named_entities` stays reviewed-empty and the printed unknown-attribution note is TIR.

Earlier source-terminology and provenance guardrails remain binding, including record 176, record 200, source-lost 267–268 and all prior batches.

## Puṟanāṉūṟu sequence

Continue from record **311** and do not skip ahead. Printed names remain source mentions unless separately resolved through permitted evidence.

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
2. Confirm the final/squashed production checkpoint is exactly **310 reviewed / 90 remaining / 5,430 observations / next 311**, with 29 canonical dimensions and 224 tests.
3. Confirm record 297/307 unknown-attribution handling, record 298 absent source-state, record 299 sacred-reference boundary, record 305 terminology boundary and record 306 lacuna/memorial handling remain intact.
4. Review Puṟanāṉūṟu **311–335 sequentially**, source-first and against all 29 dimensions.
5. Prefer one contiguous `311-335.json` reviewed spec if the entire batch is completed in-session.
6. Materialize once through the deterministic materializer/driver and perform targeted generated-record checks.
7. Publish one clean user-authored checkpoint parented by the previous green checkpoint.
8. Run the full normal PR workflow on that exact final squashed head.
9. If green, the next permitted batch is **336–360**.

Do not start the Tolkāppiyam production pass. Do not start R2.
