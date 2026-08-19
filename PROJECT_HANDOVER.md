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

- `001.json` through `335.json` form the gap-free production prefix;
- stabilization batch **003–010** is complete;
- regular **25-record** batches **011–035**, **036–060**, **061–085**, **086–110**, **111–135**, **136–160**, **161–185**, **186–210**, **211–235**, **236–260**, **261–285**, **286–310**, and **311–335** are complete;
- next record: **336**;
- next planned checkpoint: **336–360**.

Current validated production figures from normal PR workflow `32248997542`:

- records reviewed: **335**;
- records remaining: **65**;
- production observations checked: **5,866**;
- canonical dimensions: **29**;
- regression suite: **224 passed**;
- R0/R1/R1.5 validation: **pass**;
- deterministic R1/R1.5 regeneration: **pass**;
- repository audit: **pass**;
- Corpus 1.1.0 / Tolkāppiyam non-drift: **pass**;
- R1 primary-history preservation: **pass**;
- Tolkāppiyam production observation count: **0**.

Every poem must still be read completely and sequentially, and all 29 dimension decisions must be completed source-first before the old sparse audit is consulted. Exact evidence/provenance, reviewed-empty states, ambiguity, damaged/source-lost conditions and source terminology must be retained.

## Publication cadence

The semantic review remains one poem at a time. Repository publication may batch already-completed reviews.

The 261–285 and 286–310 batches proved the lower-latency one-spec/one-materialization path. For 311–335, all 25 poems were still reviewed completely and sequentially before the audit was opened, but publication used five 5-record specs (`311-315.json` through `331-335.json`) so connector writes stayed manageable and record 323's new source-state compatibility case could be validated in sequence.

This split changes Git/materialization granularity only. It does not permit batched semantic guessing, skipped poems, audit-first classification or weakened provenance review. One contiguous 25-record spec remains preferred when practical; split specs remain valid when technical/source-state isolation is useful.

`scripts/materialize_r15a_purananuru_batch.py` is a deterministic materializer, not a classifier. `scripts/materialize_r15a_purananuru_batch_driver.py` is the range-aware source-state compatibility layer.

Current exact unknown-poet/non-identification literals handled by the driver are:

- `பெயர் தெரிந்திலது`
- `பெயர் புலனாகவில்லை`
- `பாடப்பட்டோர் : பெயர்கள் தெரிந்தில`

They are temporarily suppressed only for core named-entity linking and then restored verbatim into `source_metadata_reviewed.poet_as_printed`. This is source-state compatibility, not semantic classification.

A pre-existing R0 body assertion may attach only when its type belongs to a dimension already selected by fresh review and its exact source text lies inside selected evidence.

## Source terminology rule

`docs/SOURCE_TERMINOLOGY_POLICY.md` is mandatory.

Retain the exact Tamil term printed by the source. Do not silently substitute later identity, hierarchy, caste/community, sectarian, deity, taxonomy, modern-community or external-influence labels. Source metadata, canonical body and printed source-note evidence remain distinct. Null/blank metadata stays null/blank. Printed names remain source mentions unless independently resolved.

## Important 311–335 fidelity/provenance lessons

- record 311 preserves exact `புலைத்தி` as source occupational/social terminology without later identity substitution;
- record 312 has null thinai/thurai/poet/addressee and no printed source note; those states remain absent while the body independently records the `கடன்` duty sequence, smithing, kingship and warfare;
- record 313 preserves exact `இரவன் மாக்கள்`, `உமணர்`, and `உப்பொய் சாகாட்டு` as source social/trade evidence without inventing a wider market system;
- record 315 keeps the printed poet/`பாடப்பட்டோன்` attribution distinct from body `நெடுமான் அஞ்சி` and records the source relationship as TIR;
- record 317 remains incomplete/lacunose and is not reconstructed;
- record 319 preserves the canonical odd form `யாம் க·டு உண்டென` exactly and does not silently repair it;
- record 321 remains incomplete/lacunose; surviving sword-scar / `செருவெங் குருசில்` evidence supports warfare without reconstructing missing text;
- record 322 preserves `கரும்பின் எந்திரம்` as source-explicit processing/mechanical evidence and `கண்படை ஈயா` as sleepless body-state evidence;
- record 323 remains incomplete/lacunose and preserves `பாடப்பட்டோர் : பெயர்கள் தெரிந்தில` / `பாடியவர் பாடப்பட்டோர் : பெயர்கள் தெரிந்தில.` as unresolved-attribution metadata/TIR; `named_entities` remains reviewed-empty;
- record 324 preserves exact `வேட்டுவர்`, `இடையன்`, `பாணர்` without later identity substitution;
- records 327–328 preserve exact `பெயர் தெரிந்திலது`; 328 remains lacunose and neither record manufactures a named entity;
- record 329 preserves `நடுகல்`, `நாட்பலி`, water, ghee/fragrance and smoke as an explicit memorial-stone ritual sequence without later doctrinal expansion;
- record 331 preserves `உறையூர் முது கூற்றனார் எனவும் பாடம்` as an alternate poet reading/TIR; `போகுபலி வெண்சோறு` is retained only as source offering language;
- record 332 preserves exact `மறவன்` as source martial/social terminology;
- record 333 remains incomplete/lacunose with `பெயர் தெரிந்திலது`; `named_entities` stays reviewed-empty and the damaged passage is not reconstructed;
- record 334 remains incomplete/lacunose and only surviving adornment wording is retained;
- record 335 remains incomplete/lacunose; only surviving plant names (`குருந்து`, `முல்லை`, `வரகு`, `தினை`, `கொள்ளு`, `அவரை`) are retained; exact `துடியன், பாணன், பறையன், கடம்பன்` is preserved without later identity equivalence; `கல்லே பரவின் ... நெல்உகுத்துப் பரவும் கடவுளும் இலவே` is classified as this poem's memorial-worship/deity language, not generalized into a historical claim that other gods or religions were absent.

Earlier lessons remain binding, including record 176, damaged record 200, source-lost records 267–268, and all earlier terminology/source-state/provenance guardrails.

## Puṟanāṉūṟu boundary

Review **336 onward** sequentially until all 400 records are complete. Only after Puṟanāṉūṟu 001–400 is complete and validated may the equivalent Tolkāppiyam production pass begin.

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

Confirm the final/squashed 001–335 checkpoint and exact-head CI are green. Then review Puṟanāṉūṟu **336–360** sequentially/source-first.

Do not start the Tolkāppiyam production pass. Do not start R2.
