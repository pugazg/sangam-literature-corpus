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
- Puṟanāṉūṟu `001.json` through `385.json` form the materialized gap-free production prefix.
- Stabilization batch **003–010** is complete.
- Regular **25-record** semantic batches begin at **011–035** and are complete through **361–385**.
- The next record is **386** and the final Puṟanāṉūṟu batch is **386–400**.
- Current production validation: **385 reviewed / 15 remaining / 6,819 observations / next 386**.
- Current canonical dimension count: **29**.
- Current regression suite: **224 passed**.
- 361–385 was fully reviewed sequentially/source-first before the 351–400 control ledger was opened, then published in five specs: `361-365.json`, `366-370.json`, `371-375.json`, `376-380.json`, `381-385.json`.
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

For the final 386–400 batch, semantic review is still poem-by-poem even though the checkpoint contains only 15 records. Split specs are valid if source-state or connector-size isolation is useful.

After materialization, perform targeted checks for source loss, lacunae, metadata/body/source-note boundaries and substantive audit discrepancies. Obtain the real observation total from the normal verifier, update docs once, squash to one clean user-authored checkpoint parented by the prior green checkpoint, then run final exact-head CI.

## Source-state compatibility rule

The range-aware driver preserves explicit non-identification metadata without allowing it to become named-entity evidence. Current unknown-poet literals are:

- `பெயர் தெரிந்திலது`
- `பெயர் புலனாகவில்லை`
- `பாடப்பட்டோர் : பெயர்கள் தெரிந்தில`
- `, பாடப்பட்டோர், திணை, துறை தெரிந்தில`

It also temporarily suppresses and then restores addressee `பெயர் தெரிந்திலது` during named-entity linking. This is source-state compatibility, not semantic classification or identity resolution.

## Durable lessons from 361–385

- 361: thinai/thurai/addressee remain null; frozen poet field `, பாடப்பட்டோர், திணை, துறை தெரிந்தில` and printed note are non-identification/TIR, not a named entity or TT classification.
- 362: preserve exact `அந்தணாளர்`, `நான்மறை`, `அறம்`, `பொருள்` without later identity/doctrinal import.
- 363: preserve exact `இழி பிறப்பினோன்` only as source social/funerary wording without later hierarchy/community equivalence.
- 366: incomplete/lacunose; `தருமபுத்திரன்` remains unresolved printed addressee; do not reconstruct.
- 367: preserve `நோற்றோர்`, `பார்ப்பார்`, `நல்வினை`, `இருபிறப்பாளர்`, `முத்தீ`; three-ruler `சிறப்பு` is source-context/TIR, not external historical verification.
- 368: source note says the ruler had fallen but life had not yet departed; retain as source-reported battlefield loss, not independently verified death.
- 370–371: incomplete/lacunose battlefield records; no reconstruction. 371 `பறை` is the printed instrument term.
- 372: preserve canonical `மறக்கள வேள்வி` and `மாமறி பிண்டம்`, `வாலுவன்`, `வதுவை விழவு`, `பூதநீர்` as source battle-ritual vocabulary without later doctrine.
- 373: canonical `வாகை / மறக்களவழி` remains; printed `ஏர்க்கள உருவகமும் ஆம்` is additional TT/TIR, not a metadata overwrite.
- 374: preserve `புலிப்பற் றாலி` as source adornment wording.
- 375: preserve `ஏரின் வாழ்நர்`, `குடிமுறை` without later community substitution.
- 376 and 379: `எந்தை` is father-like patron language, not literal genealogy; 379 `இலங்கை` stays an unresolved source place-name.
- 377: gem, gold and pearl are bestowed gifts; do not infer transactional long-distance trade.
- 378: preserve exact `தென் பரதவர்`, `வட வடுகர்`; Rama–Sita–`அரக்கன்`–monkey comparison is narrative intertext, not historical verification.
- 380: null thinai/thurai/poet/addressee and absent source note remain absent; damaged body does not reconstruct them.
- 381: `எந்தை` is relational; `கரும்பன் ஊரன் காதல் மகனே` separately supplies explicit kinship evidence.
- 383: addressee remains `பெயர் தெரிந்திலது`; body `அவியன்` is separately unresolved; source-note `கொள்ளலும் பொருந்தும்` remains conjectural TIR and does not resolve the addressee.
- 383–385: preserve `வெள்ளி` as source celestial/prognostic/time language without modern astronomical equivalence or validated causal weather theory.
- 384: preserve exact `உழவர்` source-bound.
- 385: `காவிரி அணையும் தாழ்நீர்ப் படப்பை` / rice cultivation supports source water-management/agricultural evidence only; printed names remain unresolved.

Earlier source-terminology and provenance guardrails remain binding, including record 176, damaged record 200, and source-lost records 267–268.

## Puṟanāṉūṟu sequence

Continue with records **386–400** and do not skip ahead. This is the final Puṟanāṉūṟu production batch.

Do not start the Tolkāppiyam production pass until Puṟanāṉūṟu 001–400 is complete and the full final checkpoint is validated.

## Validation

At the final Puṟanāṉūṟu checkpoint require at minimum:

```bash
python3 scripts/validate_research_r15_dimensions.py --root .
python3 scripts/validate_r15_purananuru_production.py --root .
pytest -q
python3 scripts/audit_repository.py --root .
```

The GitHub workflow must also preserve R0/R1/R1.5 validation, deterministic R1/R1.5 regeneration, Corpus 1.1.0/Tolkāppiyam non-drift, R1 primary-history non-mutation and documentation continuity.

## Required next activity

1. Confirm PR #4 remains open, draft and unmerged; inspect live head and checks.
2. Confirm the final/squashed production checkpoint is exactly **385 reviewed / 15 remaining / 6,819 observations / next 386**, with 29 canonical dimensions and 224 tests.
3. Confirm 361 unresolved classification, 367 ritual terminology/source-note boundary, 373 alternate classification, 378 narrative intertext, 380 absent metadata, 383 unknown addressee/body Aviyan distinction, and 383–385 `வெள்ளி` handling remain intact.
4. Review Puṟanāṉūṟu **386–400 sequentially**, source-first and against all 29 dimensions.
5. Materialize deterministically and perform targeted generated-record checks.
6. Publish one clean user-authored checkpoint parented by the previous green checkpoint.
7. Run the full normal PR workflow on that exact final squashed head.
8. Only after 001–400 is complete and fully validated may planning for the Tolkāppiyam production pass begin. R2 remains separately blocked.

Do not start R2.
