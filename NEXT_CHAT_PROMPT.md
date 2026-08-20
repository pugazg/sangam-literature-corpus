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
- Puṟanāṉūṟu cadence remains benchmark `001–002`, stabilization **003–010**, regular **25-record** batches beginning **011–035**, final `386–400`.
- Tolkāppiyam `0001–0228` is the current gap-free production prefix.
- Completed எழுத்ததிகாரம் இயல்: நூல் மரபு, மொழி மரபு, பிறப்பியல், புணரியல், தொகைமரபு, உருபியல்.
- Current partial இயல்: **உயிர்மயங்கியல் `0204–0296` (93 records)**.
- உயிர்மயங்கியல் `0204–0228` is complete as the first 25-record publication boundary.
- Remaining normal உயிர்மயங்கியல் boundaries: `0229–0253`, `0254–0278`, `0279–0296`.
- Current Tolkāppiyam state: **228 / 1,602 reviewed; 1,374 remaining; next `tolkappiyam-0229`; 292 formal grammatical/poetics observations; 26 incidental examples; 29 dimensions; 228 tests passed at materialization**.
- Tolkāppiyam evidence never auto-classifies a Sangam poem.

## Evidence roles

For every dimension of every நூற்பா, distinguish:

1. formal grammatical/poetics concept evidence;
2. incidental example evidence;
3. no qualifying evidence identified.

Only formal evidence becomes `GRAMMATICAL_CONCEPT_EVIDENCE` in `research/observations/tolkappiyam/r15-production.ndjson`, with classification basis `tolkappiyam_mapping`.

Incidental examples remain inside per-record review and must not be promoted into historical, ecological, social, material, identity or lived-life claims.

The old crosswalk is representative/control evidence, not an exhaustive occurrence index and not a classifier.

## Durable lessons through 0228

Earlier lexical guardrails remain binding: grammatical `உயிர்`, `மெய்`, ordinary `இசை`, `காலை`, `பொருள்`, `உயர்திணை`, `அஃறிணை`, `தொழில்` and related terms remain contextual rather than being promoted by surface resemblance. Articulation anatomy is grammatical rather than medical; measure vocabulary is not automatically historical economy/metrology; `புலவர்` attribution formulas remain unresolved/incidental; `மரப்பெயர்`, `திசைப் பெயர்`, `இயற்கை`, `செயற்கை` remain source-contextual.

### உயிர்மயங்கியல் 0204–0228

Reviewed spec: `research/production/tolkappiyam/review-specs/0204-0228.json`.

This boundary adds **33 formal observations** and **3 incidental examples**.

- The dominant formal layer is `knowledge.grammar.morphophonology` for source-explicit doubling, addition, loss, lengthening, alternation and boundary behavior.
- Morphology is used only where grammatical form classes, சாரியை or உருபு behavior are actually assigned.
- `knowledge.grammar.word_structure` is used where structural categories such as `தொடர்மொழி`, `தொடர் அல்`, `இரு பெயர்த் தொகைமொழி`, `ஓரெழுத்து மொழி` are explicit.
- 0208 `உயிர்` means vowel; no body/health/life promotion.
- 0209 `செய்யுளுள்` and 0214 `செய்யுள் கண்ணிய` support narrow `textual.poetic_form.formal_context`, not external-work identity or historical performance.
- 0211 grammatical `தொழில்` / `உரைப்பொருட் கிளவி` do not become occupation/economy evidence.
- 0216 `இயற்கை` remains grammatical, not environmental.
- 0218 `மரப்பெயர்` is incidental flora-language only, not a specific plant occurrence/ecology claim.
- 0219 `மகப்பெயர்` is a grammatical lexical-class label, not historical family/gender/kinship evidence.
- 0220 `அவண்` is grammatical positional/deictic wording, not geography.
- 0223 `புலவர்` / `என்மனார் புலவர்` remain incidental learned-role/attribution evidence only.
- 0224 `இரு பெயர்த் தொகைமொழி` is formal word structure; `மெய்ம்மையாக` is not body evidence.
- 0225 grammatical `தொழில்` does not become occupation evidence; `ஆ` / `மா` are not silently resolved into fauna.
- 0228 `இரா` is the exact grammatical form, not historical time/night evidence.
- No new controlled concept was required.

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

## Publication cadence

Semantic review is always sequential/source-first and one production spec never crosses an இயல் boundary.

Normal publication preference remains contiguous chunks of at most 25 records. A >25 full-இயல் publication requires explicit user direction. உயிர்மயங்கியல் follows `0204–0228`, `0229–0253`, `0254–0278`, `0279–0296`.

## Required next activity — உயிர்மயங்கியல் 0229–0253

Review **எழுத்ததிகாரம் / உயிர்மயங்கியல் `0229–0253` (25 records)**.

For every record:

1. read the complete frozen நூற்பா and current இயல் context;
2. consider all 29 dimensions;
3. fix formal evidence, incidental examples and reviewed-empty decisions before moving to the next record;
4. preserve exact Tamil terms and source spans;
5. do not use the old crosswalk to manufacture a classification;
6. only after all fresh decisions for the semantic batch are complete, compare with the old manifest/crosswalk as control;
7. materialize only the contiguous gap-free `0229–0253` boundary;
8. validate exact counts from the production validator;
9. update current handover/status documentation;
10. finish on one clean user-authored/squashed checkpoint with full exact-head PR CI green.

Do not begin `0254–0278` until `0229–0253` is green.

## Hard boundaries

- Frozen `corpus/tolkappiyam/` is immutable.
- Exact source Tamil wins over generalized labels.
- Grammatical examples are not automatic historical facts.
- Tolkāppiyam evidence never auto-classifies Puṟanāṉūṟu or another work.
- Empty means no qualifying evidence in that reviewed நூற்பா, not historical absence.
- Keep PR #4 draft/unmerged.
- Do not start R2.
