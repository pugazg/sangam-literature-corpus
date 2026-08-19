# Next Chat Prompt — R1.5A Tolkāppiyam stabilization

Continue directly in `pugazg/sangam-literature-corpus`.

Active branch: `research/classical-tamil-concept-matrix-r1.5a`.

Treat live GitHub state as authoritative.

## Phase boundary

R1.5 was explicitly authorized and merged into `main` at `d82f9c78f27f9c9daf8fbb913d01ddfb29bddba1`.

R1.5A keeps concept/observation schema `0.3.0` and is **not R2**. R2 remains blocked until explicit user authorization.

## Mandatory startup

Before changing the repository, read completely:

1. `docs/DOCUMENTATION_STATUS.md`
2. `docs/SOURCE_TERMINOLOGY_POLICY.md`
3. `PROJECT_HANDOVER.md`
4. `PROJECT_GUIDELINES.md`
5. `NEXT_CHAT_PROMPT.md`
6. `docs/handover/r15a-production-review/README.md`
7. `research/production/purananuru/README.md`
8. `research/production/tolkappiyam/README.md`
9. `research/observations/tolkappiyam/README.md`
10. `research/schemas/tolkappiyam-production-review-r15.schema.json`
11. `research/schemas/tolkappiyam-concept-evidence-r15.schema.json`
12. `research/concepts/classical-tamil/tolkappiyam-production-concepts-r15a.json`
13. `research/audits/r15-premerge/tolkappiyam/review-manifest.json`
14. `research/audits/r15-premerge/tolkappiyam/dimension-crosswalk.json`
15. `scripts/materialize_r15a_tolkappiyam_batch.py`
16. `scripts/validate_r15_tolkappiyam_production.py`
17. current PR #4 metadata and exact-head checks.

## Accepted state

- Corpus 1.1.0 remains frozen: 28 works / 7,234 canonical records / 5,632 poems / 1,602 Tolkāppiyam நூற்பா.
- R0, R1 and the bounded R1.5 pilot remain preserved.
- Exact 29-dimension surface remains unchanged.
- Puṟanāṉūṟu production is complete: 400/400, 7,169 observations.
- Puṟanāṉūṟu cadence history remains: benchmark `001–002`, stabilization **003–010**, regular **25-record** batches beginning **011–035**, final `386–400`.
- Tolkāppiyam benchmark `0001–0002` is materialized and validated.
- Tolkāppiyam state: **2 / 1,602 reviewed; 1,600 remaining; next `tolkappiyam-0003`; 2 formal grammatical observations; 0 incidental examples; 29 dimensions; 228 tests passed**.
- Benchmark workflow `32270636581` is fully green on the benchmark tree.
- Tolkāppiyam evidence never auto-classifies a Sangam poem.

## Tolkāppiyam production evidence roles

For every dimension of every நூற்பா, distinguish:

1. formal grammatical/poetics concept evidence;
2. incidental example evidence;
3. no qualifying evidence identified.

Only formal evidence becomes `GRAMMATICAL_CONCEPT_EVIDENCE` in `research/observations/tolkappiyam/r15-production.ndjson`, with classification basis `tolkappiyam_mapping`.

Incidental examples remain inside the per-record review and must not be promoted into historical, ecological, social, material, identity or lived-life claims.

The old crosswalk is representative/control evidence, not an exhaustive occurrence index and not a classifier.

## Benchmark lessons

### 0001

`எழுத்து எனப்படுப / அகரம் முதல் / னகர இறுவாய் முப்பஃது என்ப / சார்ந்து வரல் மரபின் மூன்று அலங்கடையே.`

- formal evidence only in `knowledge_technology`;
- concept `knowledge.grammar.phonology`;
- `எழுத்து`/letter names are grammatical categories, not material objects or named historical entities;
- no Akam/Puram or tiṇai/tuṟai classification is inferred.

### 0002

`அவைதாம், / குற்றியலிகரம் குற்றியலுகரம் / ஆய்தம் என்ற / முப்பாற்புள்ளியும் எழுத்து ஓரன்ன.`

- formal evidence only in `knowledge_technology`;
- same controlled concept;
- `குற்றியலிகரம்`, `குற்றியலுகரம்`, `ஆய்தம்`, `புள்ளி` remain formal grammatical categories;
- no material-object or historical-entity claim is manufactured.

## Required next activity — stabilization 0003–0010

Review **0003 through 0010 sequentially and source-first**.

For each record:

1. read the complete frozen நூற்பா and its எழுத்ததிகாரம் / நூல் மரபு context;
2. consider all 29 dimensions;
3. fix formal evidence, incidental examples and reviewed-empty decisions before moving to the next record;
4. preserve exact Tamil terms and source spans;
5. do not use the old crosswalk to manufacture a classification;
6. only after all eight fresh decisions are complete, compare with the old manifest/crosswalk as control context;
7. stage one contiguous `0003-0010.json` stabilization spec;
8. materialize records 0003–0010 and the flattened formal stream deterministically;
9. validate the exact gap-free prefix through 0010;
10. run full PR CI and capture actual formal-evidence count, incidental-example count and test count.

Do not choose the scaled long-run cadence until stabilization is green. Afterward prefer இயல்-aware sequential batches rather than mechanically copying the Puṟanāṉūṟu 25-record cadence.

## Hard boundaries

- Frozen `corpus/tolkappiyam/` is immutable.
- Exact source Tamil wins over generalized labels.
- Grammatical examples are not automatic historical facts.
- Tolkāppiyam evidence never auto-classifies Puṟanāṉūṟu or another work.
- Empty means no qualifying evidence in that reviewed நூற்பா, not historical absence.
- Keep PR #4 draft/unmerged.
- Do not start R2.
