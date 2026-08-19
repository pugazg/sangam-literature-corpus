# Sangam Literature Corpus — Project Handover

## Authoritative current state

Repository: `pugazg/sangam-literature-corpus`

Default branch: `main`

Active research branch: `research/classical-tamil-concept-matrix-r1.5a`

R1.5 was explicitly authorized for merge and merged into `main` at:

`d82f9c78f27f9c9daf8fbb913d01ddfb29bddba1`

PR #3 is historical/merged. Draft PR #4 is the active R1.5A proposal.

R1.5A keeps concept/observation schema `0.3.0`; it is not R2. **R2 remains blocked and must not start without later explicit user authorization.**

Treat current GitHub state, branch head, open PRs and current checks as authoritative over older status prose.

## Frozen corpus

Current preservation release: **Classical Tamil Corpus 1.1.0**.

- 28 frozen works
- 7,234 canonical records
- 5,632 poem records
- 1,602 Tolkāppiyam நூற்பா
- fingerprint: `4ca530d3a836341b5abaa395af97cf7307529ced04dd40dec17b1a010949abca`
- tag: `classical-tamil-corpus-v1.1.0`

R1.5A must not alter frozen canonical corpus/source/apparatus release evidence.

## Preserved research layers

### R0 — schema `0.1.0`

- 2,867 assertions
- 285 literary-body candidates
- 43 pilot surface-form entities
- 51 relationships

R0 assertion identity/provenance remains preserved.

### R1 — schema `0.2.0`

- 8 append-only review events
- 3 conservative entity-resolution decisions
- verified historical identities: 0

R1 primary histories remain append-only.

### R1.5 — schema `0.3.0`

Merged into `main` at `d82f9c78...`. It established the concept registry/evidence policies, exact 29-dimension production vocabulary/schema, separate Tolkāppiyam grammatical/poetics evidence contract, validators, exhaustive control audits, production-review schema/validator, and initial Puṟanāṉūṟu production records.

The exhaustive pre-merge audit remains control evidence only:

- Puṟanāṉūṟu 400 / 400 × 29 dimensions;
- Tolkāppiyam 1,602 / 1,602 நூற்பா × 29 dimensions.

It must never be copied mechanically into production.

## R1.5A — active production review

Canonical progress is the longest gap-free prefix under:

`research/production/purananuru/records/`

Current materialized and validated production boundary:

- `001.json` through `285.json` form the gap-free production prefix;
- stabilization batch **003–010** is complete;
- regular 25-record batches **011–035**, **036–060**, **061–085**, **086–110**, **111–135**, **136–160**, **161–185**, **186–210**, **211–235**, **236–260**, and **261–285** are complete;
- next record: **286**;
- next planned checkpoint: **286–310**.

Current validated production figures:

- records reviewed: **285**;
- records remaining: **115**;
- production observations checked: **5,024**;
- canonical dimensions: **29**;
- regression suite: **224 passed**;
- R0/R1/R1.5 validation, deterministic R1/R1.5 regeneration, repository audit, Corpus 1.1.0/Tolkāppiyam non-drift, and R1 primary-history preservation: **pass**;
- Tolkāppiyam production observation count: **0**.

Every poem must still be read completely, sequentially and considered against all 29 dimensions. Exact source evidence/provenance, reviewed-empty states, ambiguity, damaged/source-lost conditions and source terminology must be retained. The old sparse audit is consulted only after fresh source review is complete.

## Faster production cadence without reduced scholarship

The 261–285 batch demonstrated a lower-latency publication path and this should be the default when a whole 25-record batch can be completed in one working session:

1. review all 25 poems **strictly sequentially and source-first**, completing each poem's 29-dimension decision state before the next poem;
2. do not consult the old audit until fresh decisions are complete;
3. stage the whole completed contiguous batch in **one reviewed spec** (261–285 used `research/production/purananuru/review-specs/261-285.json`);
4. let the range-aware driver deterministically materialize the full contiguous range in one workflow run;
5. perform targeted generated-record checks for source-loss, lacunae, metadata/body boundaries and important discrepancies;
6. run the authoritative normal PR verifier to obtain the actual production observation count;
7. update operational docs once, squash to one user-authored checkpoint parented by the previous green checkpoint, and run final exact-head CI once.

This optimization removes repeated five-record materializer/install/regression/poll cycles. It changes **publication granularity only**; it does not permit batched semantic guessing, skipped poems, audit-first classification, or reduced provenance review. Split specs remain allowed when a session cannot finish the whole batch or a specific source-state problem genuinely requires isolation.

`scripts/materialize_r15a_purananuru_batch.py` remains the semantic-schema materializer. `scripts/materialize_r15a_purananuru_batch_driver.py` remains the range-aware source-state compatibility layer: it selects the correct 50-record audit control, handles specs that cross audit boundaries, preserves absent source notes, blank `thurai`, and exact unknown attribution `பெயர் தெரிந்திலது` without turning that phrase into a named entity. Neither script is a semantic classifier.

A pre-existing R0 body assertion may be attached only when its assertion type belongs to a dimension already selected by fresh review and the exact source text occurs inside the selected evidence.

## Source terminology rule

`docs/SOURCE_TERMINOLOGY_POLICY.md` is mandatory.

Retain the exact Tamil term printed by the relevant source. Do not silently substitute later identity, hierarchy, caste/community, sectarian, deity, taxonomy, modern-community or external-influence labels. Any later equivalence claim requires a separately classified evidence layer with independent provenance.

Source metadata, canonical body and printed source-note evidence remain distinct. Null/blank canonical metadata stays null/blank. Printed names remain source mentions unless independently resolved.

## Important 261–285 fidelity/provenance lessons

- record 261 preserves `நடுகல்`, memorial naming/adornment, cattle recovery, lament, shorn hair and loss of ornaments as source-explicit memorial/mourning evidence;
- record 262 preserves printed `உண்டாட்டு (தலை தோற்றமுமாம்)` as an alternate thurai/classification signal rather than normalizing it;
- record 263 preserves `தொழாதனை கழிதல் ஓம்புமதி` as explicit honoring/worship of the memorial stone, while bare source-note `பாடியவர் / பாடப்பாட்டோர்` labels remain unresolved source-state/TIR evidence rather than reconstructed identities;
- records 264–265 preserve memorial-stone installation/adornment/name inscription and exact `கோவலர்` / `பரிசிலர்` without later identity expansion;
- records **267–268 are source-lost**: no canonical body and no thinai/thurai/poet/addressee metadata survive. Production records contain only work-level `literary_domain`; all other 28 dimensions are reviewed-empty with an explicit no-reconstruction note. Do not infer missing content from title, audit, commentary or external tradition;
- record 270 preserves exact `மறவர்` as source social/martial terminology;
- record 272 keeps `death_mourning_memory` reviewed-empty because the body does not explicitly state death; metadata `செருவிடை வீழ்தல்` remains TT evidence and does not independently manufacture a body-level death claim;
- records 277–280 preserve mother/son, father/husband/son, battlefield death, mourning, widow-like observances and body evidence with kinship, ritual, emotion and death dimensions kept distinct;
- record 281 preserves `வேம்பு`, யாழ், ஐயவி, ஆம்பல், `காஞ்சி` song, bells/smoke and wound-protection practices without mapping them to a later ritual or medical system;
- record 282 remains incomplete/lacunose with null thinai/thurai; printed `திணையும் துறையும் தெரிந்தில.` is explicit classification-uncertainty TIR, not a basis for reconstruction;
- record 283 remains incomplete/lacunose and preserves exact `கோசர்` plus `பாண்பாட்டு (பாடாண் பாட்டும் ஆம்)` as an alternate thurai signal without later community or classification normalization;
- record 285 remains incomplete/lacunose; camp, performance, warfare, wound, city/village, public honor and village grant evidence are retained without inventing a completed death claim.

Earlier lessons remain binding, including record 176, record 200 damaged-body handling, records 236–260, and all earlier terminology/source-state/provenance guardrails.

## Puṟanāṉūṟu boundary

Review **286 onward** sequentially until all 400 records are complete.

Special source conditions remain binding:

- record 200 remains reviewed without reconstruction from its damaged `???` body;
- records 267–268 remain source-lost/unreconstructed;
- empty dimension state means only no qualifying evidence identified in that reviewed source record;
- printed names remain source mentions, not automatically verified historical identities.

Only after Puṟanāṉūṟu 001–400 is complete and validated may the equivalent Tolkāppiyam production pass begin.

## Validation

Each final R1.5A batch checkpoint must include:

- exact 29-dimension schema/vocabulary validation;
- Puṟanāṉūṟu production-prefix validation;
- full regression tests;
- R0/R1/R1.5 validation;
- deterministic R1/R1.5 regeneration checks;
- repository audit;
- Corpus 1.1.0/Tolkāppiyam non-drift;
- R1 primary-history non-mutation;
- documentation-status continuity.

A bot-authored materialization commit is not the authoritative checkpoint. Finish on one user-authored/squashed branch head with the full normal PR workflow green on that exact SHA.

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

Confirm the final/squashed 001–285 checkpoint and its exact-head CI are green. Then review Puṟanāṉūṟu **286–310** sequentially/source-first. Prefer one contiguous 25-record reviewed spec and one materialization cycle when the entire batch can be completed in the session.

Do not start the Tolkāppiyam production pass. Do not start R2.
