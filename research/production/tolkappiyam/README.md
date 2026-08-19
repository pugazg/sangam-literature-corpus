# Tolkāppiyam R1.5A production review

## Status

This is the separate Tolkāppiyam grammatical/poetics production stream under R1.5A schema `0.3.0`.

Puṟanāṉūṟu 001–400 is complete and validated. Tolkāppiyam benchmark 0001–0002 and stabilization 0003–0010 are complete/materialized. R2 remains blocked.

Canonical source hierarchy:

`work → 3 அதிகாரம் → 27 இயல் → 1,602 நூற்பா`

Canonical record identity is source sequence: `tolkappiyam-0001` … `tolkappiyam-1602`.

## Current production boundary

Gap-free production prefix:

- `0001.json` through `0010.json`
- reviewed: **10 / 1,602**
- remaining: **1,592**
- next record: **tolkappiyam-0011**
- formal grammatical concept evidence: **10**
- incidental examples: **4**
- exact dimensions per record: **29**
- regression suite: **228 tests** at the stabilization implementation boundary

## Evidence model

Every நூற்பா is reviewed sequentially across the same exact 29 dimensions, but Tolkāppiyam evidence is not poem-world evidence.

For each dimension, distinguish:

1. `grammatical_concept_evidence_recorded` — the நூற்பா formally defines, classifies, constrains, or systematizes the concept;
2. `incidental_example_recorded` — a useful lexical/example occurrence preserved without promoting it into a historical, ecological, social, material, identity or lived-life claim;
3. `no_qualifying_evidence_identified` — no qualifying evidence found in that reviewed நூற்பா.

A dimension may contain both formal and incidental evidence; they remain separate. Only formal evidence is flattened to `research/observations/tolkappiyam/r15-production.ndjson` as `GRAMMATICAL_CONCEPT_EVIDENCE` with classification basis `tolkappiyam_mapping`.

## Production paths

- reviewed specs: `research/production/tolkappiyam/review-specs/`
- canonical records: `research/production/tolkappiyam/records/`
- flattened formal stream: `research/observations/tolkappiyam/r15-production.ndjson`
- production schema: `research/schemas/tolkappiyam-production-review-r15.schema.json`
- formal evidence schema: `research/schemas/tolkappiyam-concept-evidence-r15.schema.json`
- controlled concept extension: `research/concepts/classical-tamil/tolkappiyam-production-concepts-r15a.json`
- materializer: `scripts/materialize_r15a_tolkappiyam_batch.py`
- validator: `scripts/validate_r15_tolkappiyam_production.py`
- workflow: `.github/workflows/materialize-r15a-tolkappiyam-batch.yml`

The materializer expands already-reviewed decisions. It is not a classifier.

## Source-first rule

For every நூற்பா:

1. read the complete frozen canonical record and its அதிகாரம்/இயல் context;
2. consider all 29 dimensions;
3. decide formal evidence, incidental examples and reviewed-empty states before moving to the next record;
4. preserve exact Tamil terminology and source spans;
5. do not convert grammatical examples into historical claims;
6. only after fresh decisions, use the old R1.5 Tolkāppiyam manifest/crosswalk as coverage/control evidence;
7. materialize only a contiguous gap-free batch.

The old `dimension-crosswalk.json` is representative formal support, not an exhaustive occurrence index and never a classifier.

## Controlled concept rule

The base R1.5 registry remains unchanged for its bounded Puṟanāṉūṟu pilot. Stream-specific controlled concepts are additive in `research/concepts/classical-tamil/tolkappiyam-production-concepts-r15a.json`.

Current production concept:

- `knowledge.grammar.phonology` → `knowledge_technology`

This denotes formal grammatical phonology / letter-system knowledge and does not make a historical technology claim.

## Accepted benchmark 0001–0002

- 0001: formal letter-system scope/count; `knowledge_technology`; no incidental examples.
- 0002: formal `குற்றியலிகரம்` / `குற்றியலுகரம்` / `ஆய்தம்` classification; `knowledge_technology`; no incidental examples.

Letter/sign labels remain grammatical categories, not material or historical named-entity claims.

## Stabilization 0003–0010

All eight records contain one formal `knowledge.grammar.phonology` observation.

- **0003:** five `குற்றெழுத்து`; one `அளபு`. Phonological duration only.
- **0004:** seven `நெட்டெழுத்து`; two `அளபு`.
- **0005:** no single letter takes three `அளபு`.
- **0006:** extension procedure is formal phonology. `புலவர்` is incidental `people_social_roles`; `என்மனார் புலவர்` is incidental `textual_intertextual_relationships`. No identity/community resolution.
- **0007:** `கண் இமை நொடி` calibrates `மாத்திரை`. `நொடி` is incidental `season_weather_time`; `கண் இமை` is incidental `body_health`. Neither becomes chronology or medicine.
- **0008:** `உயிர்` is the vowel-class label, not body/life/religious evidence.
- **0009:** `மெய்` is the consonant-class label, not body/truth evidence.
- **0010:** vowel/consonant combination is a grammatical relation, not a human/social relationship; `மெய்`/`உயிர்` remain grammatical labels.

Stabilization totals: **8 new formal observations + 4 incidental examples**, producing cumulative totals of **10 formal / 4 incidental** through 0010.

## Scaled cadence after stabilization

Use **இயல்-aware sequential batching**:

- never cross an இயல் boundary in one production spec;
- if the remaining portion of an இயல் is **25 records or fewer**, publish it as one contiguous batch;
- if an இயல் is longer, split it into contiguous chunks of **at most 25 records**, all inside that இயல்;
- semantic review remains strictly one நூற்பா at a time, source-first; the chunk size only controls materialization/CI granularity.

Immediate sequence:

- **0011–0033** — 23 records, completes நூல் மரபு;
- **0034–0058** — first 25 records of மொழி மரபு;
- **0059–0082** — remaining 24 records of மொழி மரபு;
- **0083–0103** — 21 records, completes பிறப்பியல்.

This preserves இயல் context while avoiding needless repeated CI cycles.

## Acceptance/prerequisite boundary

Tolkāppiyam production may populate only after complete Puṟanāṉūṟu 001–400 production. The bounded original R1.5 pilot remains preserved. Tolkāppiyam production never auto-classifies a Sangam poem. The R1.5 baseline counts actual Tolkāppiyam observation rows, not NDJSON files.

## Hard boundaries

- Frozen `corpus/tolkappiyam/` is immutable.
- Exact source Tamil wins over generalized labels.
- `docs/SOURCE_TERMINOLOGY_POLICY.md` is mandatory.
- Grammatical examples are not automatic historical facts.
- `named_entities` is mention/formal-name evidence only, never automatic historical identity resolution.
- Empty means no qualifying evidence in the reviewed நூற்பா, not historical absence.
- R2 remains blocked.

## Next activity

Proceed with **0011–0033**, completing நூல் மரபு. Review sequentially/source-first across all 29 dimensions, consult the old crosswalk only after fresh decisions, stage one contiguous spec, materialize, validate, squash onto the previous green checkpoint, and require full exact-head PR CI green.
