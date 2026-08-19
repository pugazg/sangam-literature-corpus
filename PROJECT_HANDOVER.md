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

- `001.json` through `235.json` form the gap-free production prefix;
- stabilization batch **003–010** is complete;
- regular 25-record batches **011–035**, **036–060**, **061–085**, **086–110**, **111–135**, **136–160**, **161–185**, **186–210**, and **211–235** are complete;
- next record: **236**;
- next planned checkpoint: **236–260**.

Current validated production figures:

- records reviewed: **235**;
- records remaining: **165**;
- production observations checked: **4,182**;
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

`scripts/materialize_r15a_purananuru_batch.py` remains the semantic-schema materializer. `scripts/materialize_r15a_purananuru_batch_driver.py` is the range-aware orchestration/source-state compatibility layer: it selects the correct 50-record audit-control TSV, safely handles reviewed specs that cross audit-part boundaries, preserves records with no printed source-note block, and preserves a blank canonical `thurai` without inventing a `TURAI_VALUE`. Neither script is an automatic classifier.

The core materializer also records explicit post-review discrepancies when the fresh canonical code order and old audit order differ even if their code sets are identical. The historical control ledger is not silently normalized.

Completed cadence:

- benchmark: 001–002;
- stabilization: **003–010**;
- regular batches: **011–035**, **036–060**, **061–085**, **086–110**, **111–135**, **136–160**, **161–185**, **186–210**, **211–235**.

Next cadence:

- **236–260, 261–285, ...** through 400.

## Source terminology rule

`docs/SOURCE_TERMINOLOGY_POLICY.md` is mandatory.

Retain the exact Tamil term printed by the relevant source. Do not silently substitute later identity, hierarchy, sectarian, modern-community, or external-influence labels. Any later equivalence claim requires a separately classified evidence layer with independent provenance.

Source metadata, canonical body, and printed source-note evidence remain distinct. Null/blank canonical metadata stays null/blank. Printed names remain source mentions unless independently resolved.

Important 211–235 fidelity/provenance lessons:

- record 213 keeps the printed source note's `தன் மக்கள்மேற் போருக்கு` as source-note kinship/war/relationship evidence rather than reconstructing it from the body;
- record 214 preserves `நல்வினை`, `மாறிப் பிறப்பு`, and `தவம்` as the poem's own religious/moral language without importing a later doctrinal system;
- records 215–217 preserve body/source-note/name-form distinctions around `பிசிரோன்`, `பிசிராந்தையார்`, the friend's coming, and prior utterances without collapsing them into externally reconstructed history;
- record 218 preserves the literal attribution `கண்ணகனார் நத்தத்தனார் எனவும் பாடம்` and records `எனவும் பாடம்` as a textual-variant signal rather than normalizing the poet attribution;
- record 219 preserves exact `மள்ள` and does not over-resolve `வள்ளுரம்` or map the social term to a later identity;
- records 221–223 preserve `கூற்றம்`, `நடுகல்`, quoted prior speech, `உடம்பு`, `இன்னுயிர்`, and `தொன்னட்பு` in their source contexts without later deity/doctrine or genealogy expansion;
- record 224 preserves exact `யூப நெடுந்தூண்`, `வேத வேள்வித் தொழில்`, `இரும்பாண் ஒக்கல்`, and `கோவலர்`; the ritual evidence is not expanded into sectarian, hierarchy, or external-influence claims;
- record 225 preserves `தலையோர்`, `இடையோர்`, and `கடையோர்` as source sequence/group labels without mapping them to a later hierarchy system;
- records 226–227 retain `கூற்றே` / `நயனில் கூற்றம்` as source death-agent imagery; record 227's `பசி` belongs to personified `கூற்றம்`, not to human subsistence evidence;
- record 228 preserves potter/kiln/funerary-vessel technology and `தேவர் உலகம்` as source funerary/other-world language;
- record 229 preserves `பங்குனி`, half-night, named star positions, a falling celestial sign, and the seven-day interval as source calendrical/astronomical knowledge and omen language without modern astronomical identification;
- record 232 keeps canonical YAML `பொதுவியல் / கையறுநிலை` unchanged while separately preserving the printed source-note alternate classification `தும்பை / பாண்பாட்டும் ஆம்` as source-note TT/TIR evidence;
- record 233 keeps body `அகுதை` / `எவ்வி` named-entity evidence separate from metadata identity evidence and treats the dawn voice as a source-reported wound/loss claim, not independently verified history;
- record 234 preserves `பிண்டம்` as funerary food/offering evidence and `தன்அமர் காதலி` without inferring a narrower legal status;
- record 235 preserves `இரும்பாணர்`, `இரப்போர்`, `புலவர்`, `பாடுநர்`, and father-like `எந்தை`; the latter is not treated as literal genealogy.

Earlier lessons remain binding, including the record-176 body/metadata provenance distinction and all 186–210 terminology/source-state guardrails.

## Puṟanāṉūṟu boundary

Review **236 onward** sequentially until all 400 records are complete.

Special source conditions remain binding:

- record 200 is canonically reviewed without reconstruction from its damaged `???` body;
- records 267–268 must preserve source-lost/unreconstructed state;
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

First confirm the current final/squashed 001–235 checkpoint and its exact-head CI remain green. Then continue Puṟanāṉūṟu at record **236** and complete batch **236–260** sequentially using the source-first reviewed-spec → deterministic-materialization cadence.

Do not start the Tolkāppiyam production pass. Do not start R2.
