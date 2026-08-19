# Sangam Literature Corpus — Project Handover

## Authoritative current state

Repository: `pugazg/sangam-literature-corpus`

Default branch: `main`

Active research branch: `research/classical-tamil-concept-matrix-r1.5a`

R1.5 was explicitly authorized and merged into `main` at `d82f9c78f27f9c9daf8fbb913d01ddfb29bddba1`. PR #3 is historical/merged. Draft PR #4 is the active R1.5A proposal.

R1.5A keeps concept/observation schema `0.3.0`; it is not R2. **R2 remains blocked and must not start without explicit user authorization.** Treat live GitHub state as authoritative over older prose.

## Frozen corpus and preserved layers

Classical Tamil Corpus 1.1.0 remains frozen: 28 works / 7,234 canonical records / 5,632 poems / 1,602 Tolkāppiyam நூற்பா. Tag: `classical-tamil-corpus-v1.1.0`.

R0 schema `0.1.0`, R1 schema `0.2.0`, and the bounded R1.5 pilot remain preserved. R1.5 schema `0.3.0` remains the exact 29-dimension concept/evidence foundation. Old Puṟanāṉūṟu/Tolkāppiyam audits are post-review control evidence only and never classifiers.

## Puṟanāṉūṟu R1.5A production — complete

Puṟanāṉūṟu `001.json` through `400.json` form the complete gap-free production corpus.

Durable cadence history must remain documented exactly:

- benchmark `001–002`;
- stabilization **003–010**;
- regular **25-record** batches beginning **011–035** through `361–385`;
- final batch `386–400`.

Definitive completion checkpoint: `491fa3107984b29f1dbb747bc7483e0cb694ab91`. It validates 400 reviewed / 0 remaining / 7,169 production observations / 29 dimensions. Existing source-terminology/source-loss guardrails remain binding, including record 176, damaged record 200 and source-lost records 267–268.

## Tolkāppiyam R1.5A production — நூல் மரபு complete

Tolkāppiyam is a **separate grammatical/poetics evidence stream** over the frozen hierarchy:

`work → 3 அதிகாரம் → 27 இயல் → 1,602 நூற்பா`

Canonical production identity is source sequence: `tolkappiyam-0001` … `tolkappiyam-1602`.

Current validated gap-free boundary:

- `0001.json` through `0033.json`;
- reviewed: **33 / 1,602**;
- remaining: **1,569**;
- next record: **tolkappiyam-0034**;
- formal grammatical/poetics concept evidence: **35**;
- incidental examples: **5**;
- exact dimensions per record: **29**;
- regression suite: **228 passed**;
- pre-squash full verification workflow `32275760766`: fully green.

This completes **எழுத்ததிகாரம் / நூல் மரபு**. Every record 0001–0033 was reviewed source-first; the old manifest/crosswalk was consulted only after fresh decisions.

## Tolkāppiyam evidence contract

Every நூற்பா is reviewed sequentially across all 29 dimensions. For every dimension distinguish:

1. formal grammatical/poetics concept evidence;
2. incidental example evidence;
3. no qualifying evidence identified.

Only formal evidence is flattened into `research/observations/tolkappiyam/r15-production.ndjson` as `GRAMMATICAL_CONCEPT_EVIDENCE` with classification basis `tolkappiyam_mapping`. Incidental examples remain inside the per-record review and must not become automatic historical, ecological, social, material, identity or lived-life claims.

The old `research/audits/r15-premerge/tolkappiyam/review-manifest.json` and `dimension-crosswalk.json` remain coverage/representative-control artifacts. They never manufacture classifications. The materializer is deterministic expansion only, never a classifier.

## Controlled concepts

Stream-specific Tolkāppiyam concepts remain additive in `research/concepts/classical-tamil/tolkappiyam-production-concepts-r15a.json`.

Current concepts:

- `knowledge.grammar.phonology` → `knowledge_technology`;
- `arts.music.formal_context` → `arts_music_performance`;
- `textual.tradition.reference` → `textual_intertextual_relationships`.

The latter two were introduced by fresh review of நூற்பா 0033. They are deliberately narrow: music-context evidence does not establish a historical performance event, and a textual/tradition reference does not resolve a particular external work without source support.

## Durable lessons through 0033

Stabilization 0003–0010 proved the formal/incidental split. In particular:

- 0006 preserves `புலவர்` as incidental `people_social_roles` and `என்மனார் புலவர்` as incidental attribution;
- 0007 preserves `நொடி` as incidental time-language and `கண் இமை` as incidental body-language without chronology or medicine;
- `உயிர்` / `மெய்` remain grammatical class labels, not body/life/religion/truth claims.

For 0011–0032, each record contributes one formal `knowledge.grammar.phonology` observation and no incidental example. Polysemous grammatical wording is not promoted across dimensions: `இசையிடன்` in 0013 and `இசைகள்` in 0025 remain phonological sound language rather than music/performance evidence; `காலை` remains conditional grammatical phrasing rather than chronology.

### 0033 — formal multi-dimension edge

Source:

`அளபு இறந்து உயிர்த்தலும் ஒற்று இசை நீடலும் / உள என மொழிப இசையொடு சிவணிய / நரம்பின் மறைய என்மனார் புலவர்.`

Fresh source-first result:

- formal `knowledge_technology` via `knowledge.grammar.phonology`;
- formal `arts_music_performance` via `arts.music.formal_context` because the rule explicitly places exceptional sound-lengthening in an `இசை`-connected domain;
- formal `textual_intertextual_relationships` via `textual.tradition.reference` for `நரம்பின் மறைய`, preserved without identifying a particular external work;
- incidental `people_social_roles` for `புலவர்` in the attribution formula.

Guardrails: `அளபு` is not calendar time; `நரம்பு` is not promoted to anatomy/health; `மறை` is not mapped to religion/sectarian identity; `நரம்பின் மறை` is not resolved as a named historical work.

The 0011–0033 batch adds **25 formal observations** (23 phonology + the two additional formal 0033 dimensions) and **1 incidental example**, taking the cumulative totals to **35 formal / 5 incidental**.

## Scaled Tolkāppiyam cadence

Use **இயல்-aware sequential batching**:

- never cross an இயல் boundary in a production spec;
- if the remaining portion of an இயல் is **25 records or fewer**, review/publish it as one contiguous batch;
- if an இயல் is longer, split it into contiguous chunks of **at most 25 records**, each wholly inside that இயல்;
- semantic review remains strictly நூற்பா-by-நூற்பா and source-first; batch size changes publication/CI granularity only.

Immediate cadence:

- **0034–0058** — first 25 records of மொழி மரபு;
- **0059–0082** — remaining 24 records of மொழி மரபு;
- **0083–0103** — 21 records, completes பிறப்பியல்.

## Source terminology rule

`docs/SOURCE_TERMINOLOGY_POLICY.md` is mandatory.

Retain exact source Tamil. Do not silently substitute later identity, hierarchy, caste/community, sectarian, deity, taxonomy, modern-community or external-influence labels. Formal grammatical categories, lexical examples and historical claims remain distinct.

A Tolkāppiyam rule never automatically classifies Puṟanāṉūṟu or another Sangam poem.

## Next permitted activity

Proceed with **Tolkāppiyam 0034–0058**, the first 25 records of எழுத்ததிகாரம் / மொழி மரபு.

For every நூற்பா:

1. read the complete frozen canonical record and current இயல் context;
2. consider all 29 dimensions;
3. fix formal evidence, incidental examples and reviewed-empty decisions before moving to the next record;
4. preserve exact source spans/Tamil terminology;
5. only after all fresh decisions are fixed, consult the old manifest/crosswalk as control;
6. stage one contiguous `0034-0058.json` spec;
7. materialize deterministically, validate the gap-free prefix, and finish on one clean user-authored/squashed checkpoint with full exact-head PR CI green.

Do not start R2.

## Current documentation authority

Read in this order:

1. `docs/DOCUMENTATION_STATUS.md`
2. `docs/SOURCE_TERMINOLOGY_POLICY.md`
3. `PROJECT_HANDOVER.md`
4. `PROJECT_GUIDELINES.md`
5. `NEXT_CHAT_PROMPT.md`
6. `docs/handover/r15a-production-review/README.md`
7. `research/production/purananuru/README.md`
8. `research/production/tolkappiyam/README.md`
9. `research/observations/tolkappiyam/README.md`
10. `docs/CLASSICAL_TAMIL_RESEARCH_MATRIX.md`
11. `docs/classical-tamil-research-layer.md`
12. `research/audits/r15-premerge/tolkappiyam/review-manifest.json`
13. `research/audits/r15-premerge/tolkappiyam/dimension-crosswalk.json`

PR #4 remains draft/unmerged until a later user-authorized merge boundary.
