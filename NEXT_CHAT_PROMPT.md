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
- Puṟanāṉūṟu cadence history remains benchmark `001–002`, stabilization **003–010**, regular **25-record** batches beginning **011–035**, final `386–400`.
- Tolkāppiyam `0001–0203` is the current gap-free production prefix.
- Completed எழுத்ததிகாரம் இயல்: நூல் மரபு, மொழி மரபு, பிறப்பியல், புணரியல், தொகைமரபு, உருபியல்.
- உருபியல் `0174–0203` is complete under normal publication boundaries `0174–0198` and `0199–0203`.
- Current Tolkāppiyam state: **203 / 1,602 reviewed; 1,399 remaining; next `tolkappiyam-0204`; 259 formal grammatical/poetics observations; 23 incidental examples; 29 dimensions; 228 tests passed at materialization**.
- `tolkappiyam-0204` is confirmed as **எழுத்ததிகாரம் / உயிர்மயங்கியல்**, traditional நூற்பா 1.
- Tolkāppiyam evidence never auto-classifies a Sangam poem.

## Evidence roles

For every dimension of every நூற்பா, distinguish:

1. formal grammatical/poetics concept evidence;
2. incidental example evidence;
3. no qualifying evidence identified.

Only formal evidence becomes `GRAMMATICAL_CONCEPT_EVIDENCE` in `research/observations/tolkappiyam/r15-production.ndjson`, with classification basis `tolkappiyam_mapping`.

Incidental examples remain inside per-record review and must not be promoted into historical, ecological, social, material, identity or lived-life claims.

The old crosswalk is representative/control evidence, not an exhaustive occurrence index and not a classifier.

## Durable lessons through 0203

Earlier lexical guardrails remain binding: grammatical `உயிர்`, `மெய்`, ordinary `இசை`, `காலை`, `பொருள்`, `உயர்திணை`, `அஃறிணை`, `தொழில்` and related terms must remain contextual rather than being promoted by surface resemblance.

### பிறப்பியல் 0083–0103

- Formal `body.articulation.anatomy` records source-explicit articulation sites/breath pathways only; it does not create medical claims.
- 0102 exact `அளபின் கோடல் அந்தணர் மறைத்தே` is a formal unresolved tradition reference with incidental `அந்தணர்` learned-role evidence. Do not substitute later caste/community/sectarian identity.

### புணரியல் 0104–0143

- Distinguish formal `knowledge.grammar.morphology` from `knowledge.grammar.morphophonology`.
- `உயர்திணை` / `அஃறிணை` remain grammatical noun classes, not social hierarchy or human-gender claims.
- 0125 `நாள்` is incidental lexical time inside a form rule.
- 0131 `புலவர்` / `என்மனார் புலவர்` are incidental learned-role/attribution evidence.
- `உடம்படுமெய்`, grammatical `தொழில்`, and grammatical `பொருள்` do not become body, occupation or economy evidence.

### தொகைமரபு 0144–0173

- Use formal `knowledge.grammar.quantification` for grammatical `அளவு`, `நிறை`, `எண்` and related measure/quantity classes, separate from morphology/morphophonology.
- Measure expressions `அரை`, `கலம்`, `பனை`, `கா`, `அளவு`, `நிறை` may be retained as incidental economy/measurement vocabulary but do not establish markets, transactions or standardized metrology.
- 0170 `பனை` is a measure-expression name in context, not flora.
- 0147/0159 `புலவர்` and attribution formulas remain incidental.

### உருபியல் 0174–0203

- Full உருபியல் adds **41 formal observations** and **3 incidental examples** across the two reviewed specs `0174-0198.json` and `0199-0203.json`.
- `சாரியை`, `வேற்றுமை உருபு`, inflection/end-form selection and grammatical noun/pronoun classes are morphology; explicit joining, loss, shortening and boundary-form/letter changes are morphophonology; some rules support both.
- 0179 `புலவர்` / `என்மனார் புலவர்` remain incidental learned-role/attribution evidence only.
- 0182 `மரப்பெயர்` is incidental tree-name/flora-language inside a grammatical lexical class, not a specific plant occurrence or historical ecology claim.
- 0191 `உயர்திணை` remains a grammatical noun-class condition, not hierarchy, caste/community, status, gender or kinship evidence.
- 0198 `இயற்கை` / `செயற்கை` remain grammatical/formal terminology, not environmental evidence or a separate historical technology claim.
- 0199 `எண்` is formal grammatical quantification plus morphology, not historical numeracy/economy.
- 0200 `ஒன்று`–`பத்து` are formal grammatical quantification; intermediary `ஆன்` is morphology and explicit loss/retention is morphophonology. This does not establish accounting, trade, prices or standardized metrology; `காலை` is not time evidence.
- 0201 combines morphology with explicit ஆய்தம் loss as morphophonology.
- 0202 `திசைப் பெயர்` is a grammatical lexical class under seventh-case/சாரியை morphology, not geography; final-consonant loss is morphophonology and grammatical `இயற்கை` is not environmental evidence.
- 0203 generalizes case-marker/சாரியை morphology; grammatical `உயிர்` is not life/body/health evidence and `தேரும் காலை` is analytic rather than temporal evidence.

## Current stream-specific concepts

The Tolkāppiyam extension registry includes:

- `knowledge.grammar.phonology`
- `knowledge.grammar.word_structure`
- `knowledge.grammar.morphology`
- `knowledge.grammar.morphophonology`
- `knowledge.grammar.quantification`
- `body.articulation.anatomy`
- `arts.music.formal_context`
- `textual.tradition.reference`
- `textual.poetic_form.formal_context`

No new concept was required for உருபியல் `0174–0203`.

## Publication cadence

Semantic review is always sequential/source-first and one production spec never crosses an இயல் boundary.

Normal publication preference remains contiguous chunks of at most 25 records. A >25 full-இயல் publication requires explicit user direction. உருபியல் followed the normal two-boundary cadence and is complete.

## Required next activity — உயிர்மயங்கியல் from 0204

Start from **tolkappiyam-0204**, the confirmed first நூற்பா of **எழுத்ததிகாரம் / உயிர்மயங்கியல்**.

Before creating a review spec:

1. resolve the full frozen உயிர்மயங்கியல் start/end boundary from canonical source structure;
2. derive normal contiguous publication chunks of at most 25 records without crossing the இயல் boundary;
3. review each நூற்பா sequentially/source-first across all 29 dimensions;
4. fix formal evidence, incidental examples and reviewed-empty decisions before moving to the next record;
5. preserve exact Tamil terms and source spans;
6. do not use the old crosswalk to manufacture a classification;
7. only after fresh decisions for the semantic batch are complete, compare with the old manifest/crosswalk as control;
8. materialize only a contiguous gap-free production boundary;
9. validate exact counts from the production validator;
10. update current handover/status documentation;
11. finish each publication boundary on one clean user-authored/squashed checkpoint with full exact-head PR CI green.

## Hard boundaries

- Frozen `corpus/tolkappiyam/` is immutable.
- Exact source Tamil wins over generalized labels.
- Grammatical examples are not automatic historical facts.
- Tolkāppiyam evidence never auto-classifies Puṟanāṉūṟu or another work.
- Empty means no qualifying evidence in that reviewed நூற்பா, not historical absence.
- Keep PR #4 draft/unmerged.
- Do not start R2.
