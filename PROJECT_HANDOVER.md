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

## Tolkāppiyam R1.5A production — stabilization complete

Tolkāppiyam is a **separate grammatical/poetics evidence stream** over the frozen hierarchy:

`work → 3 அதிகாரம் → 27 இயல் → 1,602 நூற்பா`

Canonical production identity is source sequence: `tolkappiyam-0001` … `tolkappiyam-1602`.

Materialized gap-free boundary after benchmark + stabilization:

- `0001.json` through `0010.json`;
- reviewed: **10 / 1,602**;
- remaining: **1,592**;
- next record: **tolkappiyam-0011**;
- formal grammatical concept evidence: **10**;
- incidental examples: **4**;
- exact dimensions per record: **29**;
- regression suite remains **228 tests** at this stabilization implementation boundary.

Benchmark `0001–0002` and stabilization `0003–0010` were both reviewed source-first. The old Tolkāppiyam manifest/crosswalk was consulted only after fresh decisions.

## Tolkāppiyam evidence contract

Every நூற்பா is reviewed sequentially across all 29 dimensions. For every dimension distinguish:

1. formal grammatical/poetics concept evidence;
2. incidental example evidence;
3. no qualifying evidence identified.

Only formal evidence is flattened into `research/observations/tolkappiyam/r15-production.ndjson` as `GRAMMATICAL_CONCEPT_EVIDENCE` with classification basis `tolkappiyam_mapping`. Incidental examples remain inside the per-record review and must not become automatic historical, ecological, social, material, identity or lived-life claims.

The old `research/audits/r15-premerge/tolkappiyam/review-manifest.json` and `dimension-crosswalk.json` remain coverage/representative-control artifacts. They never manufacture classifications.

Primary production implementation:

- `research/production/tolkappiyam/review-specs/`
- `research/production/tolkappiyam/records/`
- `research/observations/tolkappiyam/r15-production.ndjson`
- `research/schemas/tolkappiyam-production-review-r15.schema.json`
- `research/schemas/tolkappiyam-concept-evidence-r15.schema.json`
- `research/concepts/classical-tamil/tolkappiyam-production-concepts-r15a.json`
- `scripts/materialize_r15a_tolkappiyam_batch.py`
- `scripts/validate_r15_tolkappiyam_production.py`
- `.github/workflows/materialize-r15a-tolkappiyam-batch.yml`

The materializer is deterministic expansion only, never a classifier.

## Stabilization 0003–0010 — durable lessons

All eight records have one formal `knowledge_technology` observation using controlled concept `knowledge.grammar.phonology`.

- **0003:** `அ இ உ / எ ஒ ... ஓர் அளபு ... குற்றெழுத்து` formally classifies the five short vowels and one-அளபு phonological duration. `அளபு` is grammatical sound duration, not general historical/calendar time.
- **0004:** `ஆ ஈ ஊ ஏ ஐ / ஓ ஔ ... ஈர் அளபு ... நெட்டெழுத்து` formally classifies the seven long vowels and two-அளபு duration.
- **0005:** `மூ அளபு இசைத்தல் ஓர் எழுத்து இன்றே` constrains a single letter from taking three அளபு; no separate time claim is created.
- **0006:** `நீட்டம் வேண்டின் ... கூட்டி எழூஉதல்` gives the grammatical procedure for extension. `புலவர்` is preserved as an incidental `people_social_roles` mention; `என்மனார் புலவர்` is also an incidental attribution under `textual_intertextual_relationships`. Neither is historical identity/community resolution.
- **0007:** `கண் இமை நொடி ... மாத்திரை` formally calibrates grammatical duration. The same source line is preserved incidentally under `season_weather_time` for `நொடி` and under `body_health` for `கண் இமை`; neither becomes chronology or a medical claim. `நுண்ணிதின் உணர்ந்தோர்` is not promoted to a social-role classification.
- **0008:** `பன்னீர் எழுத்தும் உயிர்` formally classifies the twelve vowels. `உயிர்` is the grammatical vowel label, not a body/life/religious claim.
- **0009:** `பதினெண் எழுத்தும் மெய்` formally classifies the eighteen consonants. `மெய்` is the grammatical consonant label, not body or truth/ethical evidence.
- **0010:** `மெய்யொடு இயையினும் உயிர் இயல் திரியா` states vowel-class behavior in consonant combination. The grammatical relation is not a human/social relationship, and `மெய்`/`உயிர்` are not body, ethical or ritual claims.

These records prove the formal/incidental split can preserve useful lexical evidence without contaminating the formal observation stream.

## Scaled Tolkāppiyam cadence after stabilization

Use **இயல்-aware sequential batching**:

- never cross an இயல் boundary in a production spec;
- if the remaining portion of an இயல் is **25 records or fewer**, review/publish it as one contiguous batch;
- if an இயல் is longer, split it into contiguous chunks of **at most 25 records**, each wholly inside that இயல்;
- semantic review remains strictly நூற்பா-by-நூற்பா and source-first; the batch size changes publication/CI granularity only.

Immediate cadence:

- **0011–0033** — 23 records, completes எழுத்ததிகாரம் / நூல் மரபு;
- **0034–0058** — first 25 records of மொழி மரபு;
- **0059–0082** — remaining 24 records of மொழி மரபு;
- **0083–0103** — 21 records, completes பிறப்பியல்.

This cadence preserves இயல் context while avoiding unnecessarily repeated materialization/CI cycles.

## Source terminology rule

`docs/SOURCE_TERMINOLOGY_POLICY.md` is mandatory.

Retain exact source Tamil. Do not silently substitute later identity, hierarchy, caste/community, sectarian, deity, taxonomy, modern-community or external-influence labels. Formal grammatical categories, lexical examples and historical claims remain distinct.

A Tolkāppiyam rule never automatically classifies Puṟanāṉūṟu or another Sangam poem.

## Next permitted activity

Proceed with **Tolkāppiyam 0011–0033**, completing நூல் மரபு.

For every நூற்பா:

1. read the complete frozen canonical record and current இயல் context;
2. consider all 29 dimensions;
3. fix formal evidence, incidental examples and reviewed-empty decisions before moving to the next record;
4. preserve exact source spans/Tamil terminology;
5. only after fresh decisions, consult the old manifest/crosswalk as control;
6. stage one contiguous `0011-0033.json` spec;
7. materialize deterministically, validate the new gap-free prefix, then finish on one clean user-authored/squashed checkpoint with full exact-head PR CI green.

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
