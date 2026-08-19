# Next Chat Prompt — R1.5A Tolkāppiyam production

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
- Tolkāppiyam benchmark `0001–0002` and stabilization **0003–0010** are materialized.
- Current Tolkāppiyam state: **10 / 1,602 reviewed; 1,592 remaining; next `tolkappiyam-0011`; 10 formal grammatical observations; 4 incidental examples; 29 dimensions; 228 tests at the stabilization implementation boundary**.
- Tolkāppiyam evidence never auto-classifies a Sangam poem.

## Tolkāppiyam evidence roles

For every dimension of every நூற்பா, distinguish:

1. formal grammatical/poetics concept evidence;
2. incidental example evidence;
3. no qualifying evidence identified.

Only formal evidence becomes `GRAMMATICAL_CONCEPT_EVIDENCE` in `research/observations/tolkappiyam/r15-production.ndjson`, with classification basis `tolkappiyam_mapping`.

Incidental examples remain inside the per-record review and must not be promoted into historical, ecological, social, material, identity or lived-life claims.

The old crosswalk is representative/control evidence, not an exhaustive occurrence index and not a classifier.

## Stabilization lessons 0003–0010

All eight records carry one formal `knowledge_technology` observation using `knowledge.grammar.phonology`.

- **0003:** five short vowels; one `அளபு`; phonological duration only.
- **0004:** seven long vowels; two `அளபு`; phonological duration only.
- **0005:** no single letter takes three `அளபு`; no calendar/time claim.
- **0006:** extension procedure is formal phonology. `புலவர்` is incidental `people_social_roles`; `என்மனார் புலவர்` is incidental `textual_intertextual_relationships`. No historical identity/community inference.
- **0007:** `கண் இமை நொடி` calibrates `மாத்திரை`. `நொடி` is incidental `season_weather_time`; `கண் இமை` is incidental `body_health`. Neither becomes chronology or medicine. `நுண்ணிதின் உணர்ந்தோர்` is not promoted to a social role.
- **0008:** `உயிர்` is the grammatical vowel-class label, not body/life/religious evidence.
- **0009:** `மெய்` is the grammatical consonant-class label, not body or truth/ethical evidence.
- **0010:** vowel/consonant combination is a grammatical relation, not a human/social relationship; `மெய்`/`உயிர்` remain grammatical labels.

Total after stabilization: **10 formal observations / 4 incidental examples**.

## Scaled cadence

Use **இயல்-aware sequential batching** after stabilization:

- never cross an இயல் boundary in one production spec;
- if the remaining portion of an இயல் is 25 records or fewer, use one contiguous batch;
- if an இயல் is longer, split it into contiguous chunks of at most 25 records, all within that இயல்;
- semantic review remains strictly நூற்பா-by-நூற்பா and source-first; batch size only controls publication/CI granularity.

Immediate planned batches:

- **0011–0033** — 23 records; completes நூல் மரபு;
- **0034–0058** — first 25 records of மொழி மரபு;
- **0059–0082** — remaining 24 records of மொழி மரபு;
- **0083–0103** — 21 records; completes பிறப்பியல்.

## Required next activity — 0011–0033

Review **0011 through 0033 sequentially and source-first**, completing எழுத்ததிகாரம் / நூல் மரபு.

For every record:

1. read the complete frozen நூற்பா and its நூல் மரபு context;
2. consider all 29 dimensions;
3. fix formal evidence, incidental examples and reviewed-empty decisions before moving to the next record;
4. preserve exact Tamil terms and source spans;
5. do not use the old crosswalk to manufacture a classification;
6. only after fresh decisions are complete, compare with the old manifest/crosswalk as control context;
7. stage one contiguous `0011-0033.json` spec;
8. materialize the records and flattened formal stream deterministically;
9. validate the exact gap-free prefix through 0033;
10. finish the batch on one clean user-authored/squashed checkpoint parented by the previous green stabilization checkpoint, with full exact-head PR CI green.

## Hard boundaries

- Frozen `corpus/tolkappiyam/` is immutable.
- Exact source Tamil wins over generalized labels.
- Grammatical examples are not automatic historical facts.
- Tolkāppiyam evidence never auto-classifies Puṟanāṉūṟu or another work.
- Empty means no qualifying evidence in that reviewed நூற்பா, not historical absence.
- Keep PR #4 draft/unmerged.
- Do not start R2.
