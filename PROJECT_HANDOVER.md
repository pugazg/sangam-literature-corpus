# Sangam Literature Corpus — Project Handover

## Authoritative current state

Repository: `pugazg/sangam-literature-corpus`

Default branch: `main`

Active research branch: `research/classical-tamil-concept-matrix-r1.5a`

R1.5 was explicitly authorized and merged into `main` at `d82f9c78f27f9c9daf8fbb913d01ddfb29bddba1`. PR #3 is historical/merged. Draft PR #4 is the active R1.5A proposal.

R1.5A keeps concept/observation schema `0.3.0`; it is not R2. **R2 remains blocked and must not start without later explicit user authorization.** Treat current GitHub state, branch head, open PRs and checks as authoritative over older prose.

## Frozen corpus and preserved layers

Classical Tamil Corpus 1.1.0 remains frozen: 28 works / 7,234 canonical records / 5,632 poems / 1,602 Tolkāppiyam நூற்பா. Tag: `classical-tamil-corpus-v1.1.0`.

R0 schema `0.1.0` remains preserved: 2,867 assertions / 285 literary-body candidates / 43 pilot surface-form entities / 51 relationships.

R1 schema `0.2.0` remains preserved: 8 append-only review events / 3 conservative entity-resolution decisions / 0 verified historical identities.

R1.5 schema `0.3.0` remains the exact 29-dimension concept/evidence foundation. The exhaustive pre-merge Puṟanāṉūṟu and Tolkāppiyam audit remains post-review control evidence only and must never be copied mechanically into production.

## R1.5A — active production review

Canonical progress is the longest gap-free prefix under `research/production/purananuru/records/`.

Current materialized and validated production boundary:

- `001.json` through `360.json` form the gap-free production prefix;
- stabilization batch **003–010** is complete;
- regular **25-record semantic batches** **011–035**, **036–060**, **061–085**, **086–110**, **111–135**, **136–160**, **161–185**, **186–210**, **211–235**, **236–260**, **261–285**, **286–310**, **311–335**, and **336–360** are complete;
- next record: **361**;
- next planned checkpoint: **361–385**.

Current validated production figures from normal PR workflow `32254779147`:

- records reviewed: **360**;
- records remaining: **40**;
- production observations checked: **6,304**;
- canonical dimensions: **29**;
- regression suite: **224 passed**;
- R0/R1/R1.5 validation: **pass**;
- deterministic R1/R1.5 regeneration: **pass**;
- repository audit: **pass**;
- Corpus 1.1.0 / Tolkāppiyam non-drift: **pass**;
- R1 primary-history preservation: **pass**;
- Tolkāppiyam production observation count: **0**.

Every poem must be read completely and sequentially, and all 29 dimension decisions must be completed source-first before the old sparse audit is consulted. Exact evidence/provenance, reviewed-empty states, ambiguity, damaged/source-lost conditions and source terminology must be retained.

## Publication cadence

Semantic review remains one poem at a time. Repository publication may batch already-completed reviews.

For 336–360, all 25 poems were reviewed completely and sequentially before either old control ledger was opened. Publication used six compact specs:

- `336-340.json`
- `341-343.json`
- `344-345.json`
- `346-350.json`
- `351-355.json`
- `356-360.json`

The split around 344–345 isolates its composite printed attribution and alternate thinai/thurai source note. A construction-only malformed oversized staging spec and temporary workflow debug path were removed; they are not part of the durable production state and must not survive the final batch squash.

This split changes Git/materialization granularity only. It does not permit batched semantic guessing, skipped poems, audit-first classification or weakened provenance review. One contiguous 25-record spec remains preferred when practical; split specs remain valid when technical/source-state isolation is useful.

`scripts/materialize_r15a_purananuru_batch.py` is a deterministic materializer, not a classifier. `scripts/materialize_r15a_purananuru_batch_driver.py` is the range-aware source-state compatibility layer.

Current exact unknown-poet/non-identification literals handled by the driver remain:

- `பெயர் தெரிந்திலது`
- `பெயர் புலனாகவில்லை`
- `பாடப்பட்டோர் : பெயர்கள் தெரிந்தில`

No new driver literal was required for 344–345. Their frozen attribution is preserved as printed and semantically scoped in the reviewed observation note: `அடைநெடுங் கல்வியார்` is the named poet, while `பாடப்பட்டோன்: பெயர் தெரிந்திலது` explicitly leaves the sung person unidentified.

A pre-existing R0 body assertion may attach only when its type belongs to a dimension already selected by fresh review and its exact source text lies inside selected evidence.

## Source terminology rule

`docs/SOURCE_TERMINOLOGY_POLICY.md` is mandatory.

Retain the exact Tamil term printed by the source. Do not silently substitute later identity, hierarchy, caste/community, sectarian, deity, taxonomy, modern-community or external-influence labels. Source metadata, canonical body and printed source-note evidence remain distinct. Null/blank metadata stays null/blank. Printed names remain source mentions unless independently resolved.

## Important 336–360 fidelity/provenance lessons

- 336 preserves exact `மறவர்`, the father/mother/daughter conflict and `அறன்இலன்` as source social/ethical language without later identity-system mapping;
- 337 is incomplete/lacunose and is not reconstructed; body `சோணாட்டு`, `பாரி`, `பறம்பு` remain unresolved source mentions;
- 338 keeps the printed `சிறப்பு` note about `நெடுவேள் ஆதன்` / `போந்தை` as source-context/TIR evidence distinct from poem-body claims;
- 339–340 are lacunose with exact unknown poet `பெயர் தெரிந்திலது`; `named_entities` remains reviewed-empty; 339 preserves exact `கோவலர்`;
- 341 preserves the poem's marriage-versus-battle/death alternative and `வாரா உலகம்` as source other-world language without later doctrinal expansion;
- 343 records direct fish-for-rice exchange, ship-borne gold, and mountain/sea goods without inferring a wider market system; `குட்டுவன்` / `முசிறி` remain unresolved body mentions;
- 344–345 preserve frozen `அடைநெடுங் கல்வியார் பாடப்பட்டோன்: பெயர் தெரிந்திலது` as a named poet plus explicitly unidentified sung person, not one composite identity; their source-note alternate `வாகை / மூதின் முல்லை` classification is additional TT/TIR evidence and does not overwrite canonical `காஞ்சி / மகட்பாற் காஞ்சி`;
- 346–347 remain incomplete/lacunose and are not reconstructed; 347 keeps `அகுதை` / `கூடல்` unresolved and `நறுங் கள்ளின்` source-bound;
- 348 preserves `பாண் சேரி`, `தண்ணுமை`, `தழும்பன்`, `ஊணூர்` and food/transport evidence without later community expansion;
- 349 preserves exact `அணங்கு` only as the poem's own destructive/sacred-power wording without later deity/doctrine identification;
- 352 preserves explicit `இடையிடை சிதைவுற்ற செய்யுள் இது` plus `சிறப்பு: தித்தன் காலத்து உறந்தையின் நெல் வளம்.` as damage/source-context evidence without reconstruction;
- 353 preserves exact `தொல்குடி`, craft and `பஞ்சியும் களையாப் புண்ணர்` as source social/body/care evidence without later community or modern medical-system mapping;
- 355 is a strict source-loss boundary: poet unknown, thurai literally `பெயர் தெரிந்திலது`, only surviving lines classified, and `தோற்றக் கிடையாத போயின செய்யுள் இது.` retained as TIR/source-loss evidence without reconstruction;
- 356 preserves `ஈம விளக்கு`, `சுடலை`, ash/bones, ghost-women imagery and mourners' tears as source funerary/death evidence without later doctrinal expansion;
- 358 preserves `தவம்` and canonical `மனையறம், துறவறம்` as source ethical/ascetic vocabulary without importing a later doctrinal system;
- 360 preserves exact `புலையன்` without later caste/community equivalence and keeps its cremation/funerary-food setting source-bound.

Earlier lessons remain binding, including record 176, damaged record 200, source-lost records 267–268, and all earlier terminology/source-state/provenance guardrails.

## Puṟanāṉūṟu boundary

Review **361 onward** sequentially until all 400 records are complete. Only after Puṟanāṉūṟu 001–400 is complete and validated may the equivalent Tolkāppiyam production pass begin.

## Validation requirement

Each final R1.5A batch checkpoint must include exact 29-dimension validation, Puṟanāṉūṟu production-prefix validation, full regression, R0/R1/R1.5 validation, deterministic R1/R1.5 regeneration, repository audit, Corpus/Tolkāppiyam non-drift, R1 primary-history non-mutation and documentation continuity.

A bot-authored materialization commit is not the authoritative checkpoint. Finish on one user-authored/squashed branch head parented by the previous green checkpoint with the full normal PR workflow green on that exact SHA.

## Current documentation authority

Read in this order:

1. `docs/DOCUMENTATION_STATUS.md`
2. `docs/SOURCE_TERMINOLOGY_POLICY.md`
3. `PROJECT_HANDOVER.md`
4. `PROJECT_GUIDELINES.md`
5. `NEXT_CHAT_PROMPT.md`
6. `docs/handover/r15a-production-review/README.md`
7. `research/production/purananuru/README.md`
8. `docs/CLASSICAL_TAMIL_RESEARCH_MATRIX.md`
9. `docs/classical-tamil-research-layer.md`
10. `docs/handover/r15-premerge-audit/04-29-DIMENSION-PRODUCTION-REVIEW.md` as historical/control methodology.

## Next permitted activity

Confirm the final/squashed 001–360 checkpoint and exact-head CI are green. Then review Puṟanāṉūṟu **361–385** sequentially/source-first.

Do not start the Tolkāppiyam production pass. Do not start R2.
