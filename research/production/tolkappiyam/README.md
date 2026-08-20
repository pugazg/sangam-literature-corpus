# Tolkāppiyam R1.5A production review

## Status

This is the separate Tolkāppiyam grammatical/poetics production stream under R1.5A schema `0.3.0`.

Puṟanāṉūṟu 001–400 is complete and validated; its historical cadence remains benchmark 001–002, stabilization **003–010**, regular **25-record** batches beginning **011–035**, and final 386–400. Tolkāppiyam `0001–0173` is complete/materialized as a gap-free prefix. R2 remains blocked.

Canonical source hierarchy:

`work → 3 அதிகாரம் → 27 இயல் → 1,602 நூற்பா`

Canonical record identity is source sequence: `tolkappiyam-0001` … `tolkappiyam-1602`.

## Current production boundary

Gap-free production prefix:

- `0001.json` through `0173.json`
- reviewed: **173 / 1,602**
- remaining: **1,429**
- next record: **tolkappiyam-0174**
- formal grammatical/poetics concept evidence: **218**
- incidental examples: **20**
- exact dimensions per record: **29**
- regression suite: **228 passed**

Completed இயல்:

- `0001–0033` — எழுத்ததிகாரம் / நூல் மரபு
- `0034–0082` — எழுத்ததிகாரம் / மொழி மரபு
- `0083–0103` — எழுத்ததிகாரம் / பிறப்பியல்
- `0104–0143` — எழுத்ததிகாரம் / புணரியல்
- `0144–0173` — எழுத்ததிகாரம் / தொகைமரபு

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

Each is scoped to formal Tolkāppiyam evidence. None by itself establishes a historical event, medicine, historical technology, market system, external work identity or social identity.

## Completed நூல் மரபு and மொழி மரபு — 0001–0082

Earlier durable boundaries remain binding: `உயிர்` / `மெய்`, ordinary grammatical `இசை`, `காலை`, `பொருள்`, `உயர்திணை` and `அஃறிணை` are classified by source context, not lexical resemblance. 0033 remains the early explicit formal music/tradition edge; 0043–0045 establish word structure; 0051 establishes explicit செய்யுள் text-form context; 0067 `முறைப்பெயர்` remains unresolved.

## Completed பிறப்பியல் — 0083–0103

All 21 நூற்பா were reviewed sequentially/source-first before control comparison.

Durable boundaries:

- formal `body.articulation.anatomy` captures source-explicit articulation sites and breath pathways used to explain speech-sound production;
- this is not medical diagnosis or a general physiology reconstruction;
- 0102 exact `அளபின் கோடல் அந்தணர் மறைத்தே` remains an unresolved formal tradition/authority reference;
- `அந்தணர்` is preserved exactly as incidental learned-role wording without later caste/community/sectarian substitution.

## Completed புணரியல் — 0104–0143

All 40 நூற்பா were reviewed sequentially/source-first before control comparison.

Durable boundaries:

- formal `knowledge.grammar.morphology` is distinct from `knowledge.grammar.morphophonology`;
- `வேற்றுமை உருபு`, `சாரியை`, noun classes, பெயர்/தொழில் and boundary alternations remain grammatical-system evidence;
- `உயர்திணை` / `அஃறிணை` do not become historical social hierarchy or human-gender evidence;
- 0125 `நாள்` is incidental lexical time only;
- 0131 `புலவர்` / `என்மனார் புலவர்` remain incidental learned-role/attribution evidence;
- `தொழில்`, `உடம்படுமெய்`, and grammatical `பொருள்` are not promoted by surface resemblance to occupation, body or economy.

## Completed தொகைமரபு — 0144–0173

All 30 நூற்பா were reviewed sequentially/source-first before control comparison.

Durable boundaries:

- formal `knowledge.grammar.quantification` captures grammatical treatment of `அளவு`, `நிறை`, `எண்` and related measure/quantity expressions;
- morphophonology/morphology remain separately represented where the rule warrants them;
- `அரை`, `கலம்`, `பனை`, `கா`, `அளவு`, `நிறை` may be incidental economy/measurement vocabulary but do not establish a historical market or standardized metrology;
- 0170 `பனை` is a measure-expression name and is not flora evidence;
- 0147/0159 learned-authority formulas remain incidental role/attribution evidence.

The three current specs are:

- `0083-0103.json`
- `0104-0143.json`
- `0144-0173.json`

They complete the user-requested three-இயல் activity while keeping each spec wholly inside one இயல்.

## Publication cadence

Semantic review is always strictly one நூற்பா at a time, source-first, and a spec never crosses an இயல் boundary.

Normal publication preference remains contiguous chunks of at most 25 records. A >25 full-இயல் batch requires explicit user direction; the earlier 49-record மொழி மரபு batch was such an exception.

Next இயல்: **உருபியல் 0174–0203 (30 records)**. Normal publication boundaries are `0174–0198` and `0199–0203` unless the user explicitly authorizes another full-இயல் >25 exception.

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

Proceed with **உருபியல் beginning at 0174**, keeping review sequential/source-first across all 29 dimensions, old crosswalk control-only, deterministic materialization and full exact-head PR validation.
