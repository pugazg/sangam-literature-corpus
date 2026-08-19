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
- Tolkāppiyam `0001–0082` is the validated gap-free production prefix.
- **நூல் மரபு 0001–0033 and மொழி மரபு 0034–0082 are complete.**
- Current Tolkāppiyam state: **82 / 1,602 reviewed; 1,520 remaining; next `tolkappiyam-0083`; 87 formal grammatical/poetics observations; 7 incidental examples; 29 dimensions; 228 tests passed**.
- Tolkāppiyam evidence never auto-classifies a Sangam poem.

## Evidence roles

For every dimension of every நூற்பா, distinguish:

1. formal grammatical/poetics concept evidence;
2. incidental example evidence;
3. no qualifying evidence identified.

Only formal evidence becomes `GRAMMATICAL_CONCEPT_EVIDENCE` in `research/observations/tolkappiyam/r15-production.ndjson`, with classification basis `tolkappiyam_mapping`.

Incidental examples remain inside the per-record review and must not be promoted into historical, ecological, social, material, identity or lived-life claims.

The old crosswalk is representative/control evidence, not an exhaustive occurrence index and not a classifier.

## Durable lessons through 0082

Earlier நூல் மரபு boundaries remain binding: grammatical `உயிர்`/`மெய்`, `இசை`, `காலை`, etc. must not be promoted outside context; 0033 remains the special formal music/textual edge.

மொழி மரபு 0034–0082 was reviewed as **49 sequential source-first decisions and then published in one user-authorized full-இயல் spec**. The batch adds 52 formal observations and 2 incidental examples.

Important boundaries:

- 0043–0045 introduce formal `knowledge.grammar.word_structure`.
- 0050 carries both formal phonology and word-structure evidence.
- 0051 `செய்யுள் இறுதிப் போலும்` is formal `textual_intertextual_relationships` through `textual.poetic_form.formal_context`; it is not Akam/Puram `literary_domain` and not performance.
- 0053 keeps `இசைப்பினும்` phonological; `புலவர்` and `என்மனார் புலவர்` are incidental role/attribution evidence.
- 0067 `முறைப்பெயர்` remains an unresolved source grammatical class and is not mapped to kinship/relationships.
- 0068 `பொருள்` is grammatical/lexical meaning, not economy/material culture.
- 0082 uses both phonology and word structure; `அஃறிணை` remains grammatical, not a social/gender classification.

The stream-specific registry now also contains:

- `knowledge.grammar.word_structure`
- `textual.poetic_form.formal_context`

## Publication cadence

Semantic review is always sequential and source-first and never crosses an இயல் boundary in one spec.

Normal publication preference remains contiguous chunks of at most 25 records. **0034–0082 is a deliberate user-authorized exception that published the entire 49-record மொழி மரபு இயல் in one go.** Do not infer a >25 full-இயல் publication rule for later iyal unless the user explicitly requests it.

## Required next activity — 0083–0103

Review **0083 through 0103 sequentially and source-first**, completing எழுத்ததிகாரம் / பிறப்பியல்.

For every record:

1. read the complete frozen நூற்பா and its பிறப்பியல் context;
2. consider all 29 dimensions;
3. fix formal evidence, incidental examples and reviewed-empty decisions before moving to the next record;
4. preserve exact Tamil terms and source spans;
5. do not use the old crosswalk to manufacture a classification;
6. only after all fresh decisions are complete, compare with the old manifest/crosswalk as control context;
7. stage one contiguous `0083-0103.json` spec;
8. materialize records and the flattened formal stream deterministically;
9. validate the exact gap-free prefix through 0103;
10. finish on one clean user-authored/squashed checkpoint parented by the previous green checkpoint, with full exact-head PR CI green.

## Hard boundaries

- Frozen `corpus/tolkappiyam/` is immutable.
- Exact source Tamil wins over generalized labels.
- Grammatical examples are not automatic historical facts.
- Tolkāppiyam evidence never auto-classifies Puṟanāṉūṟu or another work.
- Empty means no qualifying evidence in that reviewed நூற்பா, not historical absence.
- Keep PR #4 draft/unmerged.
- Do not start R2.
