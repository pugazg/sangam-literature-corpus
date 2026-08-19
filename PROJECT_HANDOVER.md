# Sangam Literature Corpus — Project Handover

## Authoritative current state

Repository: `pugazg/sangam-literature-corpus`

Default branch: `main`

Active research branch: `research/classical-tamil-concept-matrix-r1.5a`

R1.5 was explicitly authorized for merge and merged into `main` at:

`d82f9c78f27f9c9daf8fbb913d01ddfb29bddba1`

PR #3 is historical/merged. Draft PR #4 is the active R1.5A proposal.

R1.5A keeps concept/observation schema `0.3.0`; it is not R2. **R2 remains blocked and must not start without later explicit user authorization.**

Treat current GitHub state, current branch head, open PRs, and current checks as authoritative over older status prose.

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

Merged into `main` at `d82f9c78...`. It established the concept registry/evidence policies, exact 29-dimension production vocabulary/schema, separate Tolkāppiyam grammatical/poetics evidence contract, validators, exhaustive control audits, production-review schema/validator, and the first two Puṟanāṉūṟu production records.

The exhaustive pre-merge audit remains control evidence only:

- Puṟanāṉūṟu 400 / 400 × 29 dimensions;
- Tolkāppiyam 1,602 / 1,602 நூற்பா × 29 dimensions.

It must never be copied mechanically into production.

## R1.5A — active production review

R1.5A changes cadence, not scholarly standards.

Canonical progress is the longest gap-free prefix under:

`research/production/purananuru/records/`

Current materialized and validated production boundary:

- `001.json` through `260.json` form the gap-free production prefix;
- stabilization batch **003–010** is complete;
- regular 25-record batches **011–035**, **036–060**, **061–085**, **086–110**, **111–135**, **136–160**, **161–185**, **186–210**, **211–235**, and **236–260** are complete;
- next record: **261**;
- next planned checkpoint: **261–285**.

Current validated production figures:

- records reviewed: **260**;
- records remaining: **140**;
- production observations checked: **4,628**;
- canonical dimensions: **29**;
- regression suite: **224 passed**;
- R0/R1/R1.5 validation, deterministic R1/R1.5 regeneration, repository audit, Corpus 1.1.0/Tolkāppiyam non-drift, and R1 primary-history preservation: **pass**.

Every poem must still be read completely, sequentially, and considered against all 29 dimensions. Exact source evidence/provenance, reviewed-empty states, ambiguity, damaged/source-lost conditions, and source terminology must be retained.

The old sparse audit is consulted only after the fresh source review for a record is complete.

## R1.5A cadence and materialization

The active cadence is:

1. review poems strictly sequentially and source-first;
2. complete each poem's 29-dimension semantic decision state before reading the next poem;
3. stage compact reviewed decisions under `research/production/purananuru/review-specs/`;
4. deterministically expand them into separate `NNN.json` production records;
5. attach an existing R0 body assertion only when its assertion type belongs to the already-reviewed dimension and its exact source text occurs inside the selected evidence span;
6. never let R0 evidence create a semantic classification;
7. compare the completed fresh classification with the old audit only after fresh review;
8. publish one multi-file checkpoint per batch and run full PR CI/non-drift once per published batch.

`scripts/materialize_r15a_purananuru_batch.py` remains the semantic-schema materializer. `scripts/materialize_r15a_purananuru_batch_driver.py` is the range-aware orchestration/source-state compatibility layer: it selects the correct 50-record audit-control TSV, safely handles reviewed specs that cross audit-part boundaries, preserves records with no printed source-note block, preserves a blank canonical `thurai` without inventing a `TURAI_VALUE`, and preserves exact unknown poet attribution `பெயர் தெரிந்திலது` as metadata while preventing that unknown-attribution phrase from becoming a `named_entities` observation. These compatibility rules do not classify semantics.

The core materializer also records explicit post-review discrepancies when the fresh canonical code order and old audit order differ even if their code sets are identical. The historical control ledger is not silently normalized.

Completed cadence:

- benchmark: 001–002;
- stabilization: **003–010**;
- regular batches: **011–035**, **036–060**, **061–085**, **086–110**, **111–135**, **136–160**, **161–185**, **186–210**, **211–235**, **236–260**.

Next cadence:

- **261–285, 286–310, ...** through 400.

## Source terminology rule

`docs/SOURCE_TERMINOLOGY_POLICY.md` is mandatory.

Retain the exact Tamil term printed by the relevant source. Do not silently substitute later identity, hierarchy, sectarian, modern-community, deity, taxonomy, or external-influence labels. Any later equivalence claim requires a separately classified evidence layer with independent provenance.

Source metadata, canonical body, and printed source-note evidence remain distinct. Null/blank canonical metadata stays null/blank. Printed names remain source mentions unless independently resolved.

Important 236–260 fidelity/provenance lessons:

- record 236 preserves `கேண்மை`, `நட்பு`, `குறவர்`, and body/source-note `பாரி` evidence without later identity expansion;
- record 237 keeps deceased `வெளிமான்` distinct from addressee `இளவெளிமான்` and retains `கூற்றம்` / `ஊழ்` in source context;
- record 238 preserves the source-note quotation/comment on `கண்ணில் ஊமன் கடற் பட்டாங்கு` as textual evidence separate from the body;
- record 241 preserves `வச்சிரத் தடக்கை நெடியோன் கோயிலுள்` without later named-deity identification;
- record 242 preserves source-note alternate attribution `கடவாயில் நல்லாதனார் பாடியது என்பதும் பாடம்` as textual-variant evidence without replacing canonical poet metadata;
- record 243 treats `நடுக்குற்று` / `சிலசொல்` as explicit aging/body evidence and does not manufacture death evidence from the `கையறுநிலை` label alone;
- record 244 is an incomplete fragment with null thinai/thurai/poet/addressee metadata; only surviving evidence (`பாணர்`, `விறலியர்`, `இரவல் மாக்கள்`, `வண்டு`, `தொடி`) is classified and no death is reconstructed from title/tradition;
- records 246–247 preserve exact `உயவற் பெண்டிரேம்`, `கணவன்`, `கானவர்`, `அணங்குடை முன்றில்`, `கொழுநன்`, and `இன்னுயிர் நடுங்கும்` without importing later named practices, legal status, or sectarian identity;
- record 249 preserves its lacuna, alternate poet attribution, and explicit Nacciṉārkkiṉiyar/Tolkāppiyam source-note citation as textual/intertextual evidence only; the Tolkāppiyam reference does not auto-classify the poem;
- records 251–252 preserve source signs of `தாபத வாகை`, including `புரிசடை` / `சடை`, fire, plant gathering, and exact `வேட்டுவன்`, without mapping them to a later religious order;
- record 254 preserves exact `என் மகன்`, `அன்னை`, `கிளை`, and `மள்ள`;
- record 255 preserves `அறனில் கூற்றே` without later deity mapping;
- records 256–257 preserve literal poet metadata `பெயர் தெரிந்திலது` while `named_entities` remains reviewed-empty; the phrase denotes unknown attribution and is not a person/entity;
- record 259 preserves `மறவர்` and comparison-term `புலைத்தி` exactly without later caste/community substitution;
- record 260 preserves canonical `கரந்தை (பாடாண் திணையுமாம்) / கையறுநிலை செருவிடை வீழ்தல்` and source-note alternatives `கையறு நிலையுமாம்`, `பாண்பாட்டுமாம்`, and `பாடாண் பாட்டுமாம்` as explicit TT/TIR variants rather than normalizing them.

Earlier lessons remain binding, including record 176 and all 186–235 terminology/source-state/provenance guardrails.

## Puṟanāṉūṟu boundary

Review **261 onward** sequentially until all 400 records are complete.

Special source conditions remain binding:

- record 200 is canonically reviewed without reconstruction from its damaged `???` body;
- **records 267–268 are source-lost and must remain unreconstructed in the next batch**;
- empty dimension state means only no qualifying evidence identified in that reviewed source record;
- printed names remain source mentions, not automatically verified historical identities.

Only after Puṟanāṉūṟu 001–400 is complete and validated may the equivalent Tolkāppiyam production pass begin.

## Validation

R1.5A batch checkpoints must include:

- exact 29-dimension schema/vocabulary validation;
- Puṟanāṉūṟu production-prefix validation;
- full regression tests;
- R0/R1/R1.5 validation;
- deterministic R1/R1.5 regeneration checks;
- repository audit;
- Corpus 1.1.0/Tolkāppiyam non-drift;
- R1 primary-history non-mutation;
- documentation-status checks.

A bot-authored materialization commit may not itself launch the normal PR workflow. The authoritative batch checkpoint must therefore end on a user-authored/squashed branch head with the full normal PR workflow green on that exact SHA.

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

Files under `docs/history/` and `docs/handover/r15-premerge-audit/` remain historical/control records where they conflict with this handover.

## Next permitted activity

First confirm the current final/squashed 001–260 checkpoint and its exact-head CI remain green. Then continue Puṟanāṉūṟu at record **261** and complete batch **261–285** sequentially using the source-first reviewed-spec → deterministic-materialization cadence. Preserve source-lost records 267–268 without reconstruction.

Do not start the Tolkāppiyam production pass. Do not start R2.
