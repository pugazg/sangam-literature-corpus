# Tolkāppiyam R1.5A production review

## Status

This is the separate Tolkāppiyam grammatical/poetics production stream under R1.5A schema `0.3.0`.

Puṟanāṉūṟu 001–400 is complete and validated. Tolkāppiyam benchmark 0001–0002 is complete and validated. R2 remains blocked.

Current canonical source hierarchy:

`work → 3 அதிகாரம் → 27 இயல் → 1,602 நூற்பா`

Canonical record identity is source sequence:

- `corpus/tolkappiyam/nurpas/0001.md` … `1602.md`
- IDs `tolkappiyam-0001` … `tolkappiyam-1602`

## Current production boundary

Gap-free production prefix:

- `0001.json` through `0002.json`
- reviewed: **2 / 1,602**
- remaining: **1,600**
- next record: **tolkappiyam-0003**
- formal grammatical concept evidence: **2**
- incidental examples: **0**
- exact dimensions per record: **29**
- regression suite: **228 passed**
- benchmark verification workflow: `32270636581`, fully green

## Evidence model

Every நூற்பா is reviewed sequentially across the same exact 29 dimensions, but Tolkāppiyam evidence is not poem-world evidence.

For each dimension, the durable review distinguishes:

1. `grammatical_concept_evidence_recorded` — the நூற்பா itself formally defines, classifies, constrains, or systematizes the concept;
2. `incidental_example_recorded` — a lexical/example occurrence is useful to preserve but must not be promoted into a historical, ecological, social, material, identity or lived-life claim;
3. `no_qualifying_evidence_identified` — no qualifying evidence was found in that reviewed நூற்பா.

A dimension may contain both formal evidence and incidental examples; these remain separate.

Formal concept evidence conforms to `research/schemas/tolkappiyam-concept-evidence-r15.schema.json`:

- evidence class: `GRAMMATICAL_CONCEPT_EVIDENCE`
- classification basis: `tolkappiyam_mapping`
- exact source text/location
- canonical source hash
- controlled concept ID
- explicit confidence/review state

Incidental examples do not generate formal concept-evidence objects.

## Production paths

- reviewed specs: `research/production/tolkappiyam/review-specs/`
- canonical production records: `research/production/tolkappiyam/records/`
- flattened formal observation stream: `research/observations/tolkappiyam/r15-production.ndjson`
- production schema: `research/schemas/tolkappiyam-production-review-r15.schema.json`
- formal evidence schema: `research/schemas/tolkappiyam-concept-evidence-r15.schema.json`
- production concept extension: `research/concepts/classical-tamil/tolkappiyam-production-concepts-r15a.json`
- materializer: `scripts/materialize_r15a_tolkappiyam_batch.py`
- validator: `scripts/validate_r15_tolkappiyam_production.py`
- materializer workflow: `.github/workflows/materialize-r15a-tolkappiyam-batch.yml`

The materializer expands already-reviewed decisions. It is not a classifier.

## Source-first rule

For every நூற்பா:

1. read the complete frozen canonical record and its அதிகாரம்/இயல் context;
2. consider all 29 dimensions;
3. decide formal evidence, incidental examples, and reviewed-empty states before moving to the next record;
4. preserve exact Tamil terminology and exact body spans;
5. do not convert examples into historical claims;
6. only after fresh source decisions, use the old R1.5 Tolkāppiyam review manifest/crosswalk as coverage/control evidence;
7. materialize only a contiguous gap-free batch.

The old `dimension-crosswalk.json` is representative formal support, not an exhaustive occurrence index and never a classifier.

## Controlled concept rule

The base R1.5 registry remains unchanged for its bounded Puṟanāṉūṟu pilot. Stream-specific controlled concepts needed by Tolkāppiyam production are versioned additively in:

`research/concepts/classical-tamil/tolkappiyam-production-concepts-r15a.json`

The benchmark introduces:

- `knowledge.grammar.phonology` → `knowledge_technology`

This denotes formal grammatical phonology / letter-system knowledge. It does not make a historical technology claim.

## Accepted benchmark 0001–0002

### 0001

Formal source:

`எழுத்து எனப்படுப / அகரம் முதல் / னகர இறுவாய் முப்பஃது என்ப / சார்ந்து வரல் மரபின் மூன்று அலங்கடையே.`

Fresh review result:

- one formal observation in `knowledge_technology`;
- concept `knowledge.grammar.phonology`;
- no incidental examples;
- other 28 dimensions reviewed-empty;
- letter names/forms remain grammatical categories, not material objects or historical named entities.

### 0002

Formal source:

`அவைதாம், / குற்றியலிகரம் குற்றியலுகரம் / ஆய்தம் என்ற / முப்பாற்புள்ளியும் எழுத்து ஓரன்ன.`

Fresh review result:

- one formal observation in `knowledge_technology`;
- concept `knowledge.grammar.phonology`;
- no incidental examples;
- other 28 dimensions reviewed-empty;
- `குற்றியலிகரம்`, `குற்றியலுகரம்`, `ஆய்தம்`, `புள்ளி` remain formal categories rather than material/historical claims.

The generated flattened stream contains exactly these two formal evidence objects and no incidental examples.

## Acceptance/prerequisite boundary

The original R1.5 acceptance invariant that kept Tolkāppiyam unpopulated while Puṟanāṉūṟu production was incomplete is now prerequisite-gated:

- Tolkāppiyam production may populate only when all Puṟanāṉūṟu 001–400 production records exist;
- the bounded R1.5 pilot remains preserved;
- Tolkāppiyam production never auto-classifies a Sangam poem.

The R1.5 baseline counts actual Tolkāppiyam NDJSON rows, not NDJSON files.

## Stabilization cadence

Next batch is deliberately small:

- **0003–0010**: stabilization

Do not choose the scaled publication cadence until 0003–0010 proves:

- source-span fidelity;
- exact 29-dimension reviewed states;
- formal-vs-incidental separation;
- deterministic materialization;
- validator behavior;
- stable controlled concepts;
- no corpus drift;
- no automatic Sangam classification.

After stabilization, prefer இயல்-aware sequential batches; do not sacrifice இயல் context merely to hit an arbitrary Git batch size.

## Hard boundaries

- Frozen `corpus/tolkappiyam/` is immutable.
- Exact source Tamil wins over generalized labels.
- Grammatical examples are not automatic historical facts.
- A Tolkāppiyam rule never auto-classifies Puṟanāṉūṟu or another Sangam poem.
- `named_entities` is mention/formal-name evidence only; it is not historical identity resolution.
- Empty means no qualifying evidence in the reviewed நூற்பா, not historical absence.
- R2 remains blocked.
