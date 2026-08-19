# Tolkāppiyam R1.5A production review

## Status

This is the separate Tolkāppiyam grammatical/poetics production stream under R1.5A schema `0.3.0`.

Puṟanāṉūṟu 001–400 is complete and validated. Tolkāppiyam `0001–0033` is complete/materialized as a gap-free prefix and completes நூல் மரபு. R2 remains blocked.

Canonical source hierarchy:

`work → 3 அதிகாரம் → 27 இயல் → 1,602 நூற்பா`

Canonical record identity is source sequence: `tolkappiyam-0001` … `tolkappiyam-1602`.

## Current production boundary

Gap-free production prefix:

- `0001.json` through `0033.json`
- reviewed: **33 / 1,602**
- remaining: **1,569**
- next record: **tolkappiyam-0034**
- formal grammatical/poetics concept evidence: **35**
- incidental examples: **5**
- exact dimensions per record: **29**
- regression suite: **228 passed**

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

Current production concepts:

- `knowledge.grammar.phonology` → `knowledge_technology`;
- `arts.music.formal_context` → `arts_music_performance`;
- `textual.tradition.reference` → `textual_intertextual_relationships`.

The latter two arise from fresh source review of 0033. They are scoped to formal Tolkāppiyam evidence and do not establish historical performance events or identify an external text without source support.

## Completed நூல் மரபு — 0001–0033

Benchmark 0001–0002 and stabilization 0003–0010 established the formal/incidental contract. Through 0010 the cumulative state was 10 formal / 4 incidental.

### 0011–0032

Each record contains one formal `knowledge.grammar.phonology` observation and no incidental examples. Important lexical boundaries include:

- 0013 `இசையிடன்` = phonological sound environment, not music/performance;
- 0025 `இசைகள்` = phonological sound correspondence, not music/performance;
- `காலை` in grammatical rules is conditional phrasing, not historical/calendar time;
- `உயிர்`, `மெய்`, `உரு`, `புள்ளி`, `இயற்கை`, `நிலை` remain grammar/form terminology when used that way by the rule.

### 0033 — formal multi-dimension edge

Source:

`அளபு இறந்து உயிர்த்தலும் ஒற்று இசை நீடலும் / உள என மொழிப இசையொடு சிவணிய / நரம்பின் மறைய என்மனார் புலவர்.`

Production result:

- formal `knowledge_technology` → `knowledge.grammar.phonology`;
- formal `arts_music_performance` → `arts.music.formal_context`;
- formal `textual_intertextual_relationships` → `textual.tradition.reference`;
- incidental `people_social_roles` for `புலவர்`.

Guardrails: `அளபு` is phonological duration; `நரம்பு` is not promoted to anatomy/health; `மறை` is not mapped to religion/sectarian identity; `நரம்பின் மறை` remains an unresolved textual/disciplinary reference rather than a resolved named historical work.

Batch 0011–0033 adds **25 formal observations + 1 incidental example**, producing cumulative totals of **35 formal / 5 incidental**.

## Scaled cadence

Use **இயல்-aware sequential batching**:

- never cross an இயல் boundary in one production spec;
- if the remaining portion of an இயல் is **25 records or fewer**, publish it as one contiguous batch;
- if an இயல் is longer, split it into contiguous chunks of **at most 25 records**, all inside that இயல்;
- semantic review remains strictly one நூற்பா at a time, source-first; chunk size controls materialization/CI granularity only.

Immediate sequence:

- **0034–0058** — first 25 records of மொழி மரபு;
- **0059–0082** — remaining 24 records of மொழி மரபு;
- **0083–0103** — 21 records, completes பிறப்பியல்.

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

Proceed with **0034–0058**, the first 25 records of மொழி மரபு. Review sequentially/source-first across all 29 dimensions, consult the old crosswalk only after all fresh decisions, stage one contiguous spec, materialize, validate, squash onto the previous green checkpoint, and require full exact-head PR CI green.
