# Next Chat Prompt — R1.5A after Puṟanāṉūṟu production completion

Continue directly in `pugazg/sangam-literature-corpus`.

Active branch: `research/classical-tamil-concept-matrix-r1.5a`.

Treat live GitHub state as authoritative.

## Phase boundary

R1.5 was explicitly authorized and merged into `main` at `d82f9c78f27f9c9daf8fbb913d01ddfb29bddba1`.

R1.5A keeps concept/observation schema `0.3.0` and is **not R2**. R2 remains blocked until the user explicitly authorizes a later transition.

## Mandatory startup

Before changing the repository, read completely:

1. `docs/DOCUMENTATION_STATUS.md`
2. `docs/SOURCE_TERMINOLOGY_POLICY.md`
3. `PROJECT_HANDOVER.md`
4. `PROJECT_GUIDELINES.md`
5. `NEXT_CHAT_PROMPT.md`
6. `docs/handover/r15a-production-review/README.md`
7. `research/production/purananuru/README.md`
8. `docs/CLASSICAL_TAMIL_RESEARCH_MATRIX.md`
9. `docs/classical-tamil-research-layer.md`
10. `docs/handover/r15-premerge-audit/04-29-DIMENSION-PRODUCTION-REVIEW.md`
11. `research/audits/r15-premerge/dimensions.json`
12. `research/controlled-vocabularies/concept-dimensions-r15.json`
13. current `main`, active R1.5A branch, PR #4 metadata, and exact-head checks.

For the Tolkāppiyam startup, additionally inspect the complete frozen Tolkāppiyam source structure under `corpus/tolkappiyam/`, all existing Tolkāppiyam R1.5 crosswalk/audit artifacts, and any current schemas/scripts/tests that mention Tolkāppiyam production. Do not assume the Puṟanāṉūṟu record/materializer contract transfers unchanged.

## Accepted state

- Corpus 1.1.0 remains frozen: 28 works / 7,234 canonical records / 5,632 poems / 1,602 Tolkāppiyam நூற்பா.
- R0 schema `0.1.0` remains preserved: 2,867 assertions, 285 candidates, 43 pilot entities, 51 relationships.
- R1 schema `0.2.0` remains preserved with 8 append-only review events and 3 conservative entity decisions.
- R1.5 concept/observation schema remains `0.3.0`.
- Exact 29-dimension production vocabulary/schema remains machine-validated.
- R1.5A publication cadence is durably documented: benchmark `001–002`, stabilization **003–010**, then regular **25-record** batches from **011–035** through `361–385`, followed by final `386–400`.
- Puṟanāṉūṟu `001.json` through `400.json` form the complete materialized and validated gap-free production corpus.
- Puṟanāṉūṟu production validation: **400 reviewed / 0 remaining / 7,169 observations / next record null**.
- Canonical dimension count: **29**.
- Regression suite: **224 passed**.
- Completion verification workflow: `32265906972`, fully green on the complete 001–400 tree.
- Tolkāppiyam production observation count remains **0**.
- The prerequisite blocking Tolkāppiyam production has now been satisfied.
- The old R1.5 exhaustive audit remains post-review control evidence only; it must never manufacture production classifications.

## Exact 29-dimension surface

Use these IDs exactly:

`literary_domain`, `tinai_turai`, `landscape_environment`, `season_weather_time`, `flora`, `fauna`, `people_social_roles`, `relationships`, `emotion_lived_experience`, `occupations_production`, `food_subsistence`, `clothing_ornaments_adornment`, `material_culture_everyday_objects`, `weapons_warfare`, `mobility_transport`, `settlements_built_environment`, `economy`, `trade_exchange`, `polity_political_life`, `communities_social_groups`, `family_gender_kinship`, `religion_ritual`, `death_mourning_memory`, `arts_music_performance`, `knowledge_technology`, `values_ethical_concepts`, `body_health`, `named_entities`, `textual_intertextual_relationships`.

Do not collapse dimensions for convenience.

## Puṟanāṉūṟu completion guardrails

The completed 386–400 final batch was reviewed sequentially/source-first before the old 351–400 control ledger was consulted and was published through:

- `386-390.json`
- `391-395.json`
- `396-400.json`

Durable final-batch lessons include:

- 386: direct salt-pricing/exchange from `சிறுவெள் உப்பின் கொள்ளை சாற்றி` / `உமண்`; no broad market inference; `வெள்ளி` source-level; `எந்தை` not genealogy.
- 387: `பணிதிறை` is tribute/polity/economic evidence, not trade; exact `பூழியர்`; `பொருநை` unresolved.
- 388: drought/`வெள்ளி`; body `மருகன்` is source kinship wording; poet-name `மகனார்` does not create external genealogy.
- 390 and 393: incomplete/lacunose and unreconstructed.
- 391: beloved-woman wording remains intimate/gender relation without narrower legal status.
- 392: exact `அணங்குடை மரபு` remains source sacred/ritual-power wording; no deity/sectarian mapping; addressee `மகன்` remains source metadata kinship only.
- 394: elephant gifts are patronage, not market exchange; `தந்தை` is not genealogy.
- 395: exact `உழவர்`; printed `மகன்` and household-woman wording remain source-bounded.
- 396: incomplete; exact `கோசர்`, `வேள்`, `ஒக்கல்`; celestial comparison is praise imagery, not an actual astronomical observation.
- 397: canonical `பாடாண் / பரிசில் விடை`; source-note `கடைநிலை விடையும் ஆம்` is additional TT/TIR, not metadata overwrite; exact `அறுதொழில் அந்தணர்` retained without later caste/sectarian equivalence.
- 398: incomplete; tiger/serpent comparisons are imagery, not actual fauna occurrences.
- 399: combined frozen thinai field `பாடாண் துறை: பரிசில் விடை` remains exact; exact `அறவர்`, `மறவர்`, `மள்ளர்`, `தொல்லோர்`; `கடவுட்கும் தொடேன்` does not identify a deity; `விடுமீன் நொடுத்துக்` supports narrow fish transaction only.
- 400: incomplete; lunar/calendrical wording remains source-level; exact `வேள்வித் தூண்`, `மறவர்`; ships/river channels/ports are transport/infrastructure, not trade absent printed exchange.

Earlier source-terminology, source-loss, ambiguity and provenance guardrails remain binding, including record 176, damaged record 200, and source-lost records 267–268.

## Tolkāppiyam production boundary

Tolkāppiyam is a **separate evidence stream**. It must not be used to retroactively auto-classify Puṟanāṉūṟu or other Sangam poems.

Before producing the first Tolkāppiyam observation/record:

1. inspect the actual frozen Tolkāppiyam corpus structure: 3 அதிகாரம் / 27 இயல் / 1,602 நூற்பா;
2. identify the canonical ordering and stable record IDs used by the frozen corpus;
3. read the existing Tolkāppiyam R1.5 crosswalk/control evidence completely;
4. determine which current production schema can be reused and which record-level fields require Tolkāppiyam-specific representation;
5. define a deterministic production ledger path, review-spec format, validator and publication cadence;
6. preserve the exact 29-dimension surface and reviewed-empty semantics;
7. preserve source terminology exactly and distinguish grammatical/formal evidence from historical claims;
8. ensure Tolkāppiyam evidence never auto-classifies another work;
9. validate a very small initial benchmark before scaling cadence;
10. keep R2 blocked.

Do not copy the old Tolkāppiyam crosswalk mechanically into production. Fresh source review must precede control comparison just as it did for Puṟanāṉūṟu.

## Validation

The final Puṟanāṉūṟu checkpoint must be one clean user-authored/squashed commit parented by the previous green checkpoint `bf7e0e168fd05476a99b0ee8615ddc324694924d`, with full exact-head PR CI green.

Before beginning Tolkāppiyam production, confirm that final checkpoint still reports:

- 400 Puṟanāṉūṟu records reviewed;
- 0 remaining;
- 7,169 production observations;
- 29 canonical dimensions;
- 224 tests passed;
- repository audit green;
- Corpus/Tolkāppiyam non-drift green;
- R1 histories preserved;
- Tolkāppiyam production observation count 0.

## Required next activity

1. Confirm PR #4 remains open, draft and unmerged and that the final/squashed Puṟanāṉūṟu 001–400 checkpoint is exact-head green.
2. Confirm the final 386–400 source/provenance guardrails above remain intact.
3. Inspect the complete Tolkāppiyam source structure and all existing Tolkāppiyam R1.5 audit/crosswalk/schema artifacts.
4. Design the Tolkāppiyam R1.5A production record, validator/materialization contract and cautious initial benchmark cadence from current repository state.
5. Only then begin the first source-first Tolkāppiyam production reviews.

Do not start R2.
