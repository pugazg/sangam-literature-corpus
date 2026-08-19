# Sangam Literature Corpus — Project Handover

## Authoritative current state

Repository: `pugazg/sangam-literature-corpus`

Default branch: `main`

Active research branch: `research/classical-tamil-concept-matrix-r1.5a`

R1.5 was explicitly authorized for merge and merged into `main` at:

`d82f9c78f27f9c9daf8fbb913d01ddfb29bddba1`

PR #3 is historical/merged. Draft PR #4 is the active R1.5A proposal.

R1.5A keeps concept/observation schema `0.3.0`; it is not R2. **R2 remains blocked and must not start without later explicit user authorization.**

Treat current GitHub state, branch head, open PRs and checks as authoritative over older prose.

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

### R1 — schema `0.2.0`

- 8 append-only review events
- 3 conservative entity-resolution decisions
- verified historical identities: 0

### R1.5 — schema `0.3.0`

Merged into `main` at `d82f9c78...`. It established the concept registry/evidence policies, exact 29-dimension production vocabulary/schema, separate Tolkāppiyam evidence contract, validators, exhaustive control audits, production-review schema/validator, and initial Puṟanāṉūṟu production records.

The exhaustive pre-merge audit remains control evidence only:

- Puṟanāṉūṟu 400 / 400 × 29 dimensions;
- Tolkāppiyam 1,602 / 1,602 நூற்பா × 29 dimensions.

It must never be copied mechanically into production.

## R1.5A — active production review

Canonical progress is the longest gap-free prefix under:

`research/production/purananuru/records/`

Current materialized and validated production boundary:

- `001.json` through `310.json` form the gap-free production prefix;
- stabilization batch **003–010** is complete;
- regular 25-record batches **011–035**, **036–060**, **061–085**, **086–110**, **111–135**, **136–160**, **161–185**, **186–210**, **211–235**, **236–260**, **261–285**, and **286–310** are complete;
- next record: **311**;
- next planned checkpoint: **311–335**.

Current validated production figures:

- records reviewed: **310**;
- records remaining: **90**;
- production observations checked: **5,430**;
- canonical dimensions: **29**;
- regression suite: **224 passed**;
- R0/R1/R1.5 validation, deterministic R1/R1.5 regeneration, repository audit, Corpus 1.1.0/Tolkāppiyam non-drift, and R1 primary-history preservation: **pass**;
- Tolkāppiyam production observation count: **0**.

Every poem must still be read completely and sequentially, and all 29 dimension decisions must be completed source-first before the old sparse audit is consulted. Exact evidence/provenance, reviewed-empty states, ambiguity, damaged/source-lost conditions and source terminology must be retained.

## Faster production cadence without reduced scholarship

The 261–285 and 286–310 batches demonstrate the preferred lower-latency publication path when a complete 25-record batch can be finished in one session:

1. review all 25 poems strictly sequentially and source-first, completing each poem's 29-dimension decision state before the next;
2. consult the old audit only after fresh review;
3. stage the completed contiguous range in one reviewed spec;
4. materialize the full range in one workflow cycle through the range-aware driver;
5. perform targeted checks for source loss, lacunae, metadata/body/source-note boundaries and substantive audit discrepancies;
6. obtain the actual observation total from the normal PR verifier;
7. update operational docs once;
8. squash all construction/materializer/doc commits into one user-authored checkpoint parented by the previous green checkpoint;
9. run final exact-head PR CI once.

This changes publication granularity only. It does not permit batched semantic guessing, skipped poems, audit-first classification or weakened provenance review. Split specs remain valid if a full batch cannot be completed or a source-state issue genuinely needs isolation.

`scripts/materialize_r15a_purananuru_batch.py` remains a deterministic semantic-schema materializer, not a classifier. `scripts/materialize_r15a_purananuru_batch_driver.py` remains the range-aware source-state compatibility layer. It handles audit-part boundaries, absent source-note blocks, blank `thurai`, and exact unknown-attribution literals without turning those non-identification phrases into named entities.

The currently recognized exact unknown-poet literals are:

- `பெயர் தெரிந்திலது`
- `பெயர் புலனாகவில்லை`

They are temporarily suppressed only for named-entity linking and then restored verbatim into `source_metadata_reviewed.poet_as_printed`. This is a source-state compatibility rule, not semantic classification.

A pre-existing R0 body assertion may be attached only when its assertion type belongs to a dimension already selected by fresh review and its exact source text occurs inside selected evidence.

## Source terminology rule

`docs/SOURCE_TERMINOLOGY_POLICY.md` is mandatory.

Retain the exact Tamil term printed by the relevant source. Do not silently substitute later identity, hierarchy, caste/community, sectarian, deity, taxonomy, modern-community or external-influence labels. Any later equivalence claim requires a separately classified evidence layer with independent provenance.

Source metadata, canonical body and printed source-note evidence remain distinct. Null/blank canonical metadata stays null/blank. Printed names remain source mentions unless independently resolved.

## Important 286–310 fidelity/provenance lessons

- record 287 preserves exact `புலைய` and `இழிசின` as source social labels without later caste/community substitution;
- record 288 remains incomplete/lacunose; only surviving spear/chest/blood/vulture battlefield evidence is classified and no missing text is reconstructed;
- record 289 keeps canonical thinai/thurai null while printed `திணை, துறை. தெரிந்தில.` is classification-uncertainty TIR; exact `உழவன்`, `தொல்குடி`, `பாண`, `இழிசினன்` are preserved;
- record 294 preserves `கூற்றுவினை` as source death-agent imagery without mapping it to a later named deity/doctrine;
- record 296 preserves `வேம்பு`, `காஞ்சி`, நெய் and `ஐயவி` smoke as explicit protective practice without later ritual/medical-system mapping;
- record 297 preserves printed `பாடினோர் பாடப்பட்டோன் : பெயர்கள் தெரிந்தில.` as unresolved attribution TIR; `named_entities` remains reviewed-empty and no identities are reconstructed;
- record 298 has no source-note block and null thinai/thurai/poet/addressee metadata; these states remain absent/null and `named_entities` stays reviewed-empty;
- record 299 preserves canonical `நொச்சி / குதிரை மறம்` TT metadata and literal `அணங்குஉடை முருகன் கோட்டத்துக் / கலம்தொடா மகளிர்`; body `முருகன்` is retained only as a source-explicit named sacred referent, without external doctrinal, temple, caste or priesthood expansion;
- record 302 preserves `வெறிபாடிய காமக் கண்ணியார் (காமக் கணியார் எனவும் பாடம்)` with the parenthetical alternate attribution as TIR rather than normalization;
- record 305 preserves exact `பார்ப்பான்` and `பார்ப்பன வாகை` without later caste/doctrinal substitution;
- record 306 remains incomplete/lacunose and preserves `நடுகல் கைதொழுது பரவும்` as explicit memorial-stone honoring/worship plus death-memory evidence, without importing a later ritual system;
- record 307 preserves exact unknown poet metadata `பெயர் புலனாகவில்லை`; `named_entities` is reviewed-empty, while the unknown-attribution source note is TIR. The driver now handles this exact literal alongside `பெயர் தெரிந்திலது`;
- records 308–310 preserve exact martial, kinship, wound and performance evidence without external identity expansion.

Earlier lessons remain binding, including record 176, record 200 damaged-body handling, source-lost 267–268, and all earlier terminology/source-state/provenance guardrails.

## Puṟanāṉūṟu boundary

Review **311 onward** sequentially until all 400 records are complete.

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
- documentation continuity.

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

Confirm the final/squashed 001–310 checkpoint and exact-head CI are green. Then review Puṟanāṉūṟu **311–335** sequentially/source-first, preferably using one contiguous 25-record reviewed spec and one materialization cycle when the whole batch can be completed in-session.

Do not start the Tolkāppiyam production pass. Do not start R2.
