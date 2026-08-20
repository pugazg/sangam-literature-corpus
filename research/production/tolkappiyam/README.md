# Tolkāppiyam R1.5A production review

## Status

This is the separate Tolkāppiyam grammatical/poetics production stream under R1.5A schema `0.3.0`.

Puṟanāṉūṟu 001–400 is complete and validated; its historical cadence remains benchmark 001–002, stabilization **003–010**, regular **25-record** batches beginning **011–035**, and final 386–400. Tolkāppiyam `0001–0203` is now materialized as a gap-free prefix. R2 remains blocked.

Canonical source hierarchy:

`work → 3 அதிகாரம் → 27 இயல் → 1,602 நூற்பா`

Canonical record identity is source sequence: `tolkappiyam-0001` … `tolkappiyam-1602`.

## Current production boundary

Gap-free production prefix:

- `0001.json` through `0203.json`
- reviewed: **203 / 1,602**
- remaining: **1,399**
- next record: **tolkappiyam-0204**
- next இயல்: **எழுத்ததிகாரம் / உயிர்மயங்கியல்**
- formal grammatical/poetics concept evidence: **259**
- incidental examples: **23**
- exact dimensions per record: **29**
- regression suite: **228 passed** at materialization

Completed இயல்:

- `0001–0033` — எழுத்ததிகாரம் / நூல் மரபு
- `0034–0082` — எழுத்ததிகாரம் / மொழி மரபு
- `0083–0103` — எழுத்ததிகாரம் / பிறப்பியல்
- `0104–0143` — எழுத்ததிகாரம் / புணரியல்
- `0144–0173` — எழுத்ததிகாரம் / தொகைமரபு
- `0174–0203` — எழுத்ததிகாரம் / உருபியல், published as `0174–0198` then `0199–0203`

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
7. materialize only a contiguous gap-free batch that does not cross an இயல் boundary.

The old `dimension-crosswalk.json` is representative formal support, not an exhaustive occurrence index and never a classifier.

## Controlled concept rule

The base R1.5 registry remains unchanged for its bounded Puṟanāṉūṟu pilot. Stream-specific controlled concepts are additive in `research/concepts/classical-tamil/tolkappiyam-production-concepts-r15a.json`.

Current production concepts:

- `knowledge.grammar.phonology` → `knowledge_technology`;
- `knowledge.grammar.word_structure` → `knowledge_technology`;
- `knowledge.grammar.morphology` → `knowledge_technology`;
- `knowledge.grammar.morphophonology` → `knowledge_technology`;
- `knowledge.grammar.quantification` → `knowledge_technology`;
- `body.articulation.anatomy` → `body_health`;
- `arts.music.formal_context` → `arts_music_performance`;
- `textual.tradition.reference` → `textual_intertextual_relationships`;
- `textual.poetic_form.formal_context` → `textual_intertextual_relationships`.

Each is scoped to formal Tolkāppiyam evidence. None by itself establishes a historical event, medicine, historical technology, market system, external work identity or social identity. No new controlled concept was required for உருபியல் `0174–0203`.

## Durable completed-இயல் boundaries through 0173

Earlier durable boundaries remain binding: source-context treatment of `உயிர்`, `மெய்`, ordinary grammatical `இசை`, `காலை`, `பொருள்`, `உயர்திணை`, `அஃறிணை`, `தொழில்`; articulatory anatomy is grammatical rather than medical; learned-authority formulas remain unresolved/incidental; and quantity/measure vocabulary is not automatically historical economy or metrology.

## உருபியல் — complete 0174–0203

All 30 நூற்பா were reviewed sequentially/source-first across all 29 dimensions before control comparison, using normal publication boundaries `0174–0198` and `0199–0203`.

Reviewed specs:

- `0174-0198.json`
- `0199-0203.json`

Full உருபியல் adds **41 formal grammatical observations** and **3 incidental examples**: 31 + 3 in the first boundary, followed by 10 + 0 in the closing boundary.

Durable boundaries:

- `சாரியை`, `வேற்றுமை உருபு`, inflection/end-form selection and grammatical noun/pronoun classes use `knowledge.grammar.morphology` where source-explicit;
- joining, loss, shortening, consonant/vowel change and other boundary-form behavior use `knowledge.grammar.morphophonology`; a நூற்பா may support both when it genuinely treats both layers;
- 0179 `புலவர்` / `என்மனார் புலவர்` remain incidental learned-role/attribution evidence, not a resolved historical group, author or external text;
- 0182 `மரப்பெயர்` is incidental tree-name/flora-language inside a grammatical lexical class, not a specific plant occurrence or historical ecology claim;
- 0191 `உயர்திணை` remains a grammatical noun-class condition, not social hierarchy, caste/community, status, human-gender or kinship evidence;
- 0198 `இயற்கை` / `செயற்கை` are grammatical/formal terms in context, not environmental evidence or a separate historical technology claim;
- 0199 `எண்` is formal grammatical quantification plus morphology, not historical numeracy/economy;
- 0200 `ஒன்று`–`பத்து` are formal grammatical quantification; `ஆன்` is morphology and explicit loss/retention is morphophonology. This does not establish accounting, trade or standardized metrology, and `காலை` is not time evidence;
- 0201 combines morphology with explicit ஆய்தம் loss as morphophonology;
- 0202 `திசைப் பெயர்` is a grammatical lexical class under seventh-case/சாரியை morphology, not geographic evidence; its final-consonant loss is morphophonology and grammatical `இயற்கை` is not environmental evidence;
- 0203 generalizes case-marker/சாரியை morphology; grammatical `உயிர்` is not life/body/health evidence and `தேரும் காலை` is analytic rather than temporal evidence.

## Publication cadence

Semantic review is always strictly one நூற்பா at a time, source-first, and a spec never crosses an இயல் boundary.

Normal publication preference remains contiguous chunks of at most 25 records. A >25 full-இயல் batch requires explicit user direction. உருபியல் correctly used `0174–0198` followed by `0199–0203`.

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

Proceed from **tolkappiyam-0204**, first நூற்பா of **எழுத்ததிகாரம் / உயிர்மயங்கியல்**. Resolve the full frozen உயிர்மயங்கியல் boundary before choosing publication chunks, then apply sequential/source-first 29-dimension review and the normal at-most-25 cadence unless the user explicitly authorizes another >25 full-இயல் exception.
