# Sangam Literature Corpus — Project Handover

## Authoritative current state

Repository: `pugazg/sangam-literature-corpus`

Default branch: `main`

Active research branch: `research/classical-tamil-concept-matrix-r1.5a`

R1.5 was explicitly authorized for merge and merged into `main` at:

`d82f9c78f27f9c9daf8fbb913d01ddfb29bddba1`

PR #3 is therefore historical/merged, not an active merge hold.

R1.5A is the current follow-on production-review phase. It keeps concept/observation schema `0.3.0`; it is not R2. **R2 remains blocked and must not start without a later explicit user authorization.**

Treat current GitHub state, current branch head, open PRs, and current checks as authoritative over older R1.5 pre-merge prose.

## Frozen corpus

Current preservation release: **Classical Tamil Corpus 1.1.0**.

- 28 frozen works
- 7,234 canonical records
- 5,632 poem records
- 1,602 Tolkāppiyam நூற்பா
- fingerprint: `4ca530d3a836341b5abaa395af97cf7307529ced04dd40dec17b1a010949abca`
- tag: `classical-tamil-corpus-v1.1.0`

R1.5A must not alter frozen canonical corpus/source/apparatus release evidence.

## Research layers

### R0 — schema `0.1.0`

Preserved baseline:

- 2,867 assertions
- 285 literary-body candidates
- 43 pilot surface-form entities
- 51 relationships

R0 assertion identity/provenance remains preserved.

### R1 — schema `0.2.0`

Completed and merged before R1.5:

- 8 append-only review events
- 3 conservative entity-resolution decisions
- verified historical identities: 0

R1 primary histories remain append-only.

### R1.5 — schema `0.3.0`

Merged into `main` at `d82f9c78...` after validation.

It established:

- concept registry and evidence policies;
- classification-basis vocabulary;
- Akam/Puram and tiṇai/tuṟai foundations;
- separate Tolkāppiyam grammatical/poetics evidence contract;
- exact 29-dimension production vocabulary/schema;
- validators preventing dimension collapse;
- production-review schema/validator;
- completed Puṟanāṉūṟu production records 001 and 002.

The exhaustive pre-merge audit remains a coverage/control artifact:

- Puṟanāṉūṟu 400 / 400 × 29 dimensions;
- Tolkāppiyam 1,602 / 1,602 நூற்பா × 29 dimensions.

It must not be copied mechanically into production.

## R1.5A — active production review

R1.5A changes cadence, not scholarly standards.

Current production progress is the longest gap-free prefix under:

`research/production/purananuru/records/`

Current validated production boundary:

- `001.json` through `010.json` are complete as the gap-free production prefix;
- first R1.5A stabilization batch `003–010` is complete;
- next record: **011**;
- next planned checkpoint: **011–035**.

Every poem must still be read completely and reviewed against all 29 dimensions. Exact source evidence/provenance, reviewed-empty states, ambiguity, damaged/source-lost conditions, and source terminology must be retained.

The old sparse audit is consulted only after the fresh source review for a record is complete.

## R1.5A cadence

The active cadence is:

1. review poems strictly sequentially;
2. write each completed record JSON into the working tree before reading the next poem;
3. keep each poem as its own `NNN.json` production record;
4. stage reviewed decisions in a compact batch review spec under `research/production/purananuru/review-specs/`;
5. materialize the individual production JSON files deterministically with `scripts/materialize_r15a_purananuru_batch.py`;
6. publish records in deterministic multi-file batches rather than one Git commit per poem;
7. stabilization batch **003–010** is complete;
8. regular 25-record batches begin **011–035, 036–060, 061–085, ...** through 400;
9. if interrupted, checkpoint the completed contiguous prefix rather than losing reviewed records;
10. run the full PR CI/non-drift suite once per published batch rather than once per poem.

The materializer is not an automatic classifier. Its review spec records already-made source-first semantic decisions; it only expands those decisions into the canonical per-record schema and computes deterministic provenance fields/observation IDs.

This preserves individual scholarly completion while removing the previous commit/CI bottleneck.

## Source terminology rule

`docs/SOURCE_TERMINOLOGY_POLICY.md` is mandatory.

Retain the exact Tamil term printed by the relevant source. Do not silently substitute later identity, hierarchy, sectarian, modern-community, or external-influence labels. Any later equivalence claim requires a separately classified evidence layer with independent provenance.

## Puṟanāṉūṟu boundary

Review 011 onward sequentially until all 400 records are complete.

Special source conditions remain binding:

- record 200: preserve damage/lacuna conservatively;
- records 267–268: preserve source-lost/unreconstructed state;
- empty dimension state means only no qualifying evidence identified in that reviewed source record;
- printed names are source mentions, not automatically verified historical identities.

Only after Puṟanāṉūṟu 001–400 is complete and validated may the equivalent Tolkāppiyam production pass begin.

## Validation

R1.5A batch checkpoints must include:

- exact 29-dimension schema/vocabulary validation;
- Puṟanāṉūṟu production-prefix validation;
- full regression tests;
- deterministic R0/R1/R1.5 regeneration checks;
- repository audit;
- Corpus 1.1.0/Tolkāppiyam non-drift;
- R1 primary-history non-mutation;
- documentation-status checks.

The live PR/check state is authoritative for readiness.

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

Files under `docs/history/` and `docs/handover/r15-premerge-audit/` may describe earlier branch/merge boundaries and must be interpreted as historical/control records where they conflict with this post-merge handover.

## Next permitted activity

Continue Puṟanāṉūṟu at record **011** and complete the next R1.5A batch **011–035** sequentially using the reviewed-spec → deterministic-materialization cadence. Publish the completed batch, validate the PR, and continue only if green.

Do not start R2.
