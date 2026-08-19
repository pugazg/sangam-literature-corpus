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

- `001.json` through `385.json` form the gap-free production prefix;
- stabilization batch **003–010** is complete;
- regular **25-record semantic batches** begin at **011–035** and are complete through **361–385**;
- records reviewed: **385**;
- records remaining: **15**;
- next record: **386**;
- final Puṟanāṉūṟu batch: **386–400**.

Current validated production figures from normal PR workflow `32261366327`:

- production observations checked: **6,819**;
- canonical dimensions: **29**;
- regression suite: **224 passed**;
- R0/R1/R1.5 validation: **pass**;
- deterministic R1/R1.5 regeneration: **pass**;
- repository audit: **pass**;
- Corpus 1.1.0 / Tolkāppiyam non-drift: **pass**;
- R1 primary-history preservation: **pass**;
- Tolkāppiyam production observation count: **0**.

Every poem must still be read completely and sequentially, with all 29 dimension decisions completed source-first before the old sparse audit is consulted. Exact evidence/provenance, reviewed-empty states, ambiguity, damaged/source-lost conditions and source terminology must be retained.

## Publication cadence

Semantic review remains one poem at a time. Repository publication may batch already-completed reviews.

The completed 361–385 review was source-first across all 25 poems before the 351–400 control ledger was opened. Durable publication uses five compact specs:

- `361-365.json`
- `366-370.json`
- `371-375.json`
- `376-380.json`
- `381-385.json`

The split is publication granularity only. It does not permit batched semantic guessing, skipped poems, audit-first classification or weakened provenance review. One contiguous 25-record spec remains preferred when practical; split specs remain valid for technical/source-state isolation.

`scripts/materialize_r15a_purananuru_batch.py` is a deterministic materializer, not a classifier. `scripts/materialize_r15a_purananuru_batch_driver.py` is the range-aware source-state compatibility layer.

Current exact unknown-poet/non-identification literals handled by the driver are:

- `பெயர் தெரிந்திலது`
- `பெயர் புலனாகவில்லை`
- `பாடப்பட்டோர் : பெயர்கள் தெரிந்தில`
- `, பாடப்பட்டோர், திணை, துறை தெரிந்தில`

The driver also treats addressee `பெயர் தெரிந்திலது` as explicit non-identification during named-entity linking, then restores the exact printed metadata value. These rules preserve frozen source state; they do not classify the poem or resolve identities.

A pre-existing R0 body assertion may attach only when its type belongs to a dimension already selected by fresh review and its exact source text lies inside selected evidence.

## Source terminology rule

`docs/SOURCE_TERMINOLOGY_POLICY.md` is mandatory.

Retain the exact Tamil term printed by the source. Do not silently substitute later identity, hierarchy, caste/community, sectarian, deity, taxonomy, modern-community or external-influence labels. Source metadata, canonical body and printed source-note evidence remain distinct. Null/blank metadata stays null/blank. Printed names remain source mentions unless independently resolved.

## Important 361–385 fidelity/provenance lessons

- 361 preserves null thinai/thurai/addressee and frozen poet field `, பாடப்பட்டோர், திணை, துறை தெரிந்தில`; the printed note `பாடியவர், பாடப்பட்டோர், திணை, துறை தெரிந்தில.` is unresolved attribution/classification TIR, not a person or TT classification.
- 362 preserves exact `அந்தணாளர்`, `நான்மறை`, `அறம்`, `பொருள்` and other-world/funerary wording without later identity or doctrinal expansion.
- 363 preserves exact `இழி பிறப்பினோன்` only as source social/funerary wording; no later hierarchy/community equivalence is imposed.
- 366 is incomplete/lacunose; printed addressee `தருமபுத்திரன்` remains unresolved and missing text is not reconstructed.
- 367 preserves exact `நோற்றோர்`, `பார்ப்பார்`, `நல்வினை`, `இருபிறப்பாளர்`, `முத்தீ`; its three-ruler `சிறப்பு` note is source-context/TIR, not independent historical verification.
- 368 retains the printed statement that the ruler had fallen in battle but life had not yet departed as source-reported battlefield loss, not an independently verified historical death.
- 369–371 preserve dense battlefield, corpse, blood and supernatural imagery source-first; damaged 370–371 are not reconstructed, and 371 `பறை` is retained as the printed instrument term.
- 372 preserves canonical `மறக்கள வேள்வி` with `மாமறி பிண்டம்`, `வாலுவன்`, `வதுவை விழவு`, `பூதநீர்` and related battle-ritual wording without later sectarian/doctrinal equivalence.
- 373 keeps canonical `வாகை / மறக்களவழி` and adds printed `ஏர்க்கள உருவகமும் ஆம்` as a third TT observation plus TIR; canonical metadata is not overwritten.
- 374 preserves `புலிப்பற் றாலி` as source adornment wording without later symbolic/identity mapping.
- 375 preserves exact `ஏரின் வாழ்நர்` and `குடிமுறை` as source agrarian/social language without later community substitution.
- 376 and 379 preserve `எந்தை` as father-like patron language rather than literal genealogy; 379 body `இலங்கை` remains an unresolved source place-name.
- 377 keeps mountain gem, sea gold and pearls as bestowed gifts; no transactional long-distance trade is inferred.
- 378 preserves exact `தென் பரதவர்`, `வட வடுகர்`; its Rama–Sita–`அரக்கன்`–monkey comparison is explicit intertextual narrative evidence, not historical verification.
- 380 preserves null thinai/thurai/poet/addressee, absent source note and the damaged body without reconstruction; body `நாஞ்சிற் பொருநன்` / `கந்தன்` do not reconstruct metadata.
- 381 distinguishes father-like `எந்தை` from separate explicit kinship `கரும்பன் ஊரன் காதல் மகனே`.
- 383 restores canonical addressee `பெயர் தெரிந்திலது`; body `அவியன்` remains a separate unresolved mention, while the source note's `கொள்ளலும் பொருந்தும்` is conjectural TIR and does not resolve the addressee.
- 383–385 preserve `வெள்ளி` only as source celestial/prognostic/time wording; no modern astronomical equivalence or causal weather theory is imposed.
- 384 preserves exact `உழவர்` and drought/agricultural evidence source-bound.
- 385 preserves `காவிரி அணையும் தாழ்நீர்ப் படப்பை` / rice cultivation as source water-management/agricultural evidence without expanding beyond the wording; `காவிரி`, `அம்பர்`, `அருவந்தை`, `வேங்கட` remain unresolved source names.

Earlier lessons remain binding, including record 176, damaged record 200, source-lost records 267–268, and all earlier terminology/source-state/provenance guardrails.

## Puṟanāṉūṟu boundary

Review **386–400** sequentially as the final Puṟanāṉūṟu production batch. Only after Puṟanāṉūṟu 001–400 is complete and validated may the equivalent Tolkāppiyam production pass begin.

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

Confirm the final/squashed 001–385 checkpoint and exact-head CI are green. Then review Puṟanāṉūṟu **386–400** sequentially/source-first as the final Puṟanāṉūṟu batch.

Do not start the Tolkāppiyam production pass before that final 001–400 checkpoint is fully validated. Do not start R2.
