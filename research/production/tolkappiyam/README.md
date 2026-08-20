# Tolkāppiyam R1.5A production review

## Status

This is the separate Tolkāppiyam grammatical/poetics production stream under R1.5A schema `0.3.0`.

Puṟanāṉūṟu `001–400` is complete and validated. Tolkāppiyam `0001–0228` is the current materialized gap-free prefix. R2 remains blocked.

Canonical source hierarchy:

`work → 3 அதிகாரம் → 27 இயல் → 1,602 நூற்பா`

Canonical record identity is source sequence: `tolkappiyam-0001` … `tolkappiyam-1602`.

## Current production boundary

- `0001.json` through `0228.json`
- reviewed: **228 / 1,602**
- remaining: **1,374**
- next record: **tolkappiyam-0229**
- current இயல்: **எழுத்ததிகாரம் / உயிர்மயங்கியல்**
- formal grammatical/poetics concept evidence: **292**
- incidental examples: **26**
- exact dimensions per record: **29**
- regression suite: **228 passed** at materialization

Completed இயல்:

- `0001–0033` — எழுத்ததிகாரம் / நூல் மரபு
- `0034–0082` — எழுத்ததிகாரம் / மொழி மரபு
- `0083–0103` — எழுத்ததிகாரம் / பிறப்பியல்
- `0104–0143` — எழுத்ததிகாரம் / புணரியல்
- `0144–0173` — எழுத்ததிகாரம் / தொகைமரபு
- `0174–0203` — எழுத்ததிகாரம் / உருபியல்

Current partial இயல்:

- உயிர்மயங்கியல் is frozen at **`0204–0296` / 93 records**;
- `0204–0228` is complete as the first 25-record publication boundary;
- next `0229–0253`, then `0254–0278`, final `0279–0296`.

## Evidence model

Every நூற்பா is reviewed sequentially across the same exact 29 dimensions, but Tolkāppiyam evidence is not poem-world evidence.

For each dimension distinguish:

1. `grammatical_concept_evidence_recorded` — formal grammar/poetics evidence;
2. `incidental_example_recorded` — source lexical/example evidence retained without historical promotion;
3. `no_qualifying_evidence_identified` — no qualifying evidence in that reviewed நூற்பா.

A dimension may contain both formal and incidental evidence; they remain separate. Only formal evidence is flattened to `research/observations/tolkappiyam/r15-production.ndjson` as `GRAMMATICAL_CONCEPT_EVIDENCE` with classification basis `tolkappiyam_mapping`.

## Production paths

- reviewed specs: `research/production/tolkappiyam/review-specs/`
- canonical production records: `research/production/tolkappiyam/records/`
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

## Controlled concepts

Current production concepts are:

- `knowledge.grammar.phonology` → `knowledge_technology`;
- `knowledge.grammar.word_structure` → `knowledge_technology`;
- `knowledge.grammar.morphology` → `knowledge_technology`;
- `knowledge.grammar.morphophonology` → `knowledge_technology`;
- `knowledge.grammar.quantification` → `knowledge_technology`;
- `body.articulation.anatomy` → `body_health`;
- `arts.music.formal_context` → `arts_music_performance`;
- `textual.tradition.reference` → `textual_intertextual_relationships`;
- `textual.poetic_form.formal_context` → `textual_intertextual_relationships`.

Each is scoped to formal Tolkāppiyam evidence. None by itself establishes a historical event, medicine, technology, market system, external work identity or social identity.

## Durable boundaries inherited from 0001–0203

Earlier guardrails remain binding: grammatical `உயிர்`, `மெய்`, `இசை`, `காலை`, `பொருள்`, `உயர்திணை`, `அஃறிணை`, `தொழில்` remain contextual; articulation anatomy is grammatical rather than medical; `புலவர்` attribution formulas remain unresolved/incidental; measure vocabulary is not automatically historical economy/metrology; `மரப்பெயர்` does not itself establish flora occurrence; `திசைப் பெயர்` does not itself establish geography; grammatical `இயற்கை` / `செயற்கை` are not environmental/technology claims.

## உயிர்மயங்கியல் — first publication boundary 0204–0228

All 25 நூற்பா were reviewed sequentially/source-first across all 29 dimensions before control comparison. Reviewed spec: `0204-0228.json`.

This boundary adds **33 formal grammatical/poetics observations** and **3 incidental examples**.

Durable boundaries:

- boundary doubling, addition, loss, lengthening and alternation are `knowledge.grammar.morphophonology` only where source-explicit;
- morphology is used where grammatical form classes, சாரியை or உருபு behavior are actually assigned;
- `தொடர்மொழி`, `தொடர் அல்`, `இரு பெயர்த் தொகைமொழி`, `ஓரெழுத்து மொழி` support formal `knowledge.grammar.word_structure` where explicit;
- 0208 `உயிர்` is vowel, not body/health/life evidence;
- 0209 `செய்யுளுள்` and 0214 `செய்யுள் கண்ணிய` support `textual.poetic_form.formal_context`, not external-work identity or historical performance;
- 0211 grammatical `தொழில்` / `உரைப்பொருட் கிளவி` do not establish occupation/economy;
- 0216 `இயற்கை` remains grammatical, not environmental;
- 0218 `மரப்பெயர்` is incidental flora-language only;
- 0219 `மகப்பெயர்` is a grammatical lexical-class label, not a historical kinship claim;
- 0220 `அவண்` is grammatical positional/deictic wording, not geographic evidence;
- 0223 `புலவர்` / `என்மனார் புலவர்` remain incidental learned-role/attribution evidence;
- 0224 `இரு பெயர்த் தொகைமொழி` is formal word structure; `மெய்ம்மையாக` is not body evidence;
- 0225 grammatical `தொழில்` is not occupation evidence, and `ஆ` / `மா` are not silently resolved into fauna;
- 0228 `இரா` is the exact grammatical form, not historical night/time evidence.

No new controlled concept was required for `0204–0228`.

## Publication cadence

Semantic review is strictly one நூற்பா at a time, source-first, and a spec never crosses an இயல் boundary.

Normal publication preference remains contiguous chunks of at most 25 records. A >25 full-இயல் batch requires explicit user direction. உயிர்மயங்கியல் therefore uses `0204–0228`, `0229–0253`, `0254–0278`, `0279–0296`.

## Acceptance and hard boundaries

- Frozen `corpus/tolkappiyam/` is immutable.
- Exact source Tamil wins over generalized labels.
- `docs/SOURCE_TERMINOLOGY_POLICY.md` is mandatory.
- Grammatical examples are not automatic historical facts.
- `named_entities` is mention/formal-name evidence only, never automatic historical identity resolution.
- Empty means no qualifying evidence in the reviewed நூற்பா, not historical absence.
- Tolkāppiyam production never auto-classifies a Sangam poem.
- R2 remains blocked.

## Next activity

Proceed with **உயிர்மயங்கியல் `0229–0253`**, keeping review sequential/source-first across all 29 dimensions, old crosswalk control-only, deterministic materialization and full exact-head PR validation.
