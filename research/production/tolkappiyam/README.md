# Tolkāppiyam R1.5A production review

## Status

This is the separate Tolkāppiyam grammatical/poetics production stream under R1.5A schema `0.3.0`.

Puṟanāṉūṟu 001–400 is complete and validated; its historical cadence remains benchmark 001–002, stabilization **003–010**, regular **25-record** batches beginning **011–035**, and final 386–400. Tolkāppiyam `0001–0082` is complete/materialized as a gap-free prefix, completing நூல் மரபு and மொழி மரபு. R2 remains blocked.

Canonical source hierarchy:

`work → 3 அதிகாரம் → 27 இயல் → 1,602 நூற்பா`

Canonical record identity is source sequence: `tolkappiyam-0001` … `tolkappiyam-1602`.

## Current production boundary

Gap-free production prefix:

- `0001.json` through `0082.json`
- reviewed: **82 / 1,602**
- remaining: **1,520**
- next record: **tolkappiyam-0083**
- formal grammatical/poetics concept evidence: **87**
- incidental examples: **7**
- exact dimensions per record: **29**
- regression suite: **228 passed**

Completed இயல்:

- `0001–0033` — எழுத்ததிகாரம் / நூல் மரபு
- `0034–0082` — எழுத்ததிகாரம் / மொழி மரபு

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
- `arts.music.formal_context` → `arts_music_performance`;
- `textual.tradition.reference` → `textual_intertextual_relationships`;
- `knowledge.grammar.word_structure` → `knowledge_technology`;
- `textual.poetic_form.formal_context` → `textual_intertextual_relationships`.

Each is scoped to formal Tolkāppiyam evidence. None establishes a historical performance event, historical technology, external work identity, or social category without source support.

## Completed நூல் மரபு — 0001–0033

Benchmark 0001–0002 and stabilization 0003–0010 established the formal/incidental contract. 0011–0032 each contain one formal `knowledge.grammar.phonology` observation with no incidental examples.

0033 is the first formal multi-dimension edge: phonology + explicit formal music context + unresolved textual/tradition reference, with `புலவர்` only incidental. `நரம்பின் மறை` is not mapped to anatomy, religion, or a named historical work.

Cumulative state through 0033: **35 formal / 5 incidental**.

## Completed மொழி மரபு — 0034–0082

All **49 நூற்பா were reviewed sequentially and source-first before control comparison**. At explicit user direction, the entire இயல் was then published/materialized as one contiguous `0034-0082.json` spec rather than two ≤25-record publication chunks.

Batch result: **52 formal observations + 2 incidental examples**, producing cumulative totals of **87 formal / 7 incidental** through 0082.

### Durable source boundaries

- **0034–0042:** phonology/morphophonology. Polysemous `சினை`, `நிலை`, `முன்னர்`, `ஊர்ந்தே`, `உயிர்`, `உரு`, `காலை`, `இசை/இசைமை` remain grammatical in context. `குன்று இசை` is deficient sound, not mountain/music.
- **0043–0045:** formal word structure; `ஓர் எழுத்து ஒருமொழி`, `ஈர் எழுத்து ஒருமொழி`, `தொடர்மொழி`.
- **0050:** two formal concepts under `knowledge_technology`: phonology + word structure.
- **0051:** `செய்யுள் இறுதிப் போலும்` gives formal poetic/text-form context under `textual_intertextual_relationships`; it is not Akam/Puram `literary_domain` and not a performance event.
- **0053:** `இசைப்பினும்` is pronunciation/sound. `புலவர்` and `என்மனார் புலவர்` are incidental role/attribution examples only.
- **0057:** `தேரும் காலை` means when examined/considered, not chariot/time-of-day.
- **0066:** `தம் பெயர்` means grammatical form names, not historical named entities.
- **0067:** exact `முறைப்பெயர்` is preserved as an unresolved grammatical class; no kinship/relationship mapping is manufactured.
- **0068/0080:** `பொருள்` is grammatical/lexical meaning, not economy/material culture.
- **0082:** phonology + word structure; `அஃறிணை` is grammatical, not social/gender classification; `புகர் அற` is not promoted to ethics.

## Publication cadence

Semantic review is always strictly one நூற்பா at a time, source-first, and a spec never crosses an இயல் boundary.

Normal publication preference remains contiguous chunks of at most 25 records. **0034–0082 is a user-authorized one-time full-இயல் publication exception for the 49-record மொழி மரபு.** A later >25-record full-இயல் batch requires explicit user direction.

Immediate sequence:

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

Proceed with **0083–0103**, all 21 records of பிறப்பியல். Review sequentially/source-first across all 29 dimensions, consult the old crosswalk only after all fresh decisions, stage one contiguous spec, materialize, validate, squash onto the previous green checkpoint, and require full exact-head PR CI green.
