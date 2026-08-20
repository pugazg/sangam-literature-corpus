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
- Tolkāppiyam `0001–0406` is the current gap-free production prefix.
- Completed எழுத்ததிகாரம் இயல்: நூல் மரபு, மொழி மரபு, பிறப்பியல், புணரியல், தொகைமரபு, உருபியல்.
- Current partial இயல்: **உயிர்மயங்கியல் `0204–0296` (93 records)**.
- Completed உயிர்மயங்கியல் publication boundaries: `0204–0228`, `0229–0253`.
- Remaining normal உயிர்மயங்கியல் boundaries: `0254–0278`, `0279–0296`.
- Current Tolkāppiyam state: **253 / 1,602 reviewed; 1,349 remaining; next `tolkappiyam-0254`; 322 formal grammatical/poetics observations; 33 incidental examples; 29 dimensions; 228 tests passed at materialization**.
- Tolkāppiyam evidence never auto-classifies a Sangam poem.

## Evidence roles

For every dimension of every நூற்பா, distinguish:

1. formal grammatical/poetics concept evidence;
2. incidental example evidence;
3. no qualifying evidence identified.

Only formal evidence becomes `GRAMMATICAL_CONCEPT_EVIDENCE` in `research/observations/tolkappiyam/r15-production.ndjson`, with classification basis `tolkappiyam_mapping`.

Incidental examples remain inside per-record review and must not be promoted into historical, ecological, social, material, identity or lived-life claims.

The old crosswalk is representative/control evidence, not an exhaustive occurrence index and not a classifier.

## Durable lessons through 0253

Earlier lexical guardrails remain binding: grammatical `உயிர்`, `மெய்`, ordinary `இசை`, `காலை`, `பொருள்`, `உயர்திணை`, `அஃறிணை`, `தொழில்` and related terms remain contextual rather than being promoted by surface resemblance. Articulation anatomy is grammatical rather than medical; measure vocabulary is not automatically historical economy/metrology; `புலவர்` attribution formulas remain unresolved/incidental; `மரப்பெயர்`, `திசைப் பெயர்`, `இயற்கை`, `செயற்கை` remain source-contextual.

### உயிர்மயங்கியல் 0204–0228

Reviewed spec: `research/production/tolkappiyam/review-specs/0204-0228.json`.

This boundary adds **33 formal observations** and **3 incidental examples**.

Key guardrails include grammatical `உயிர்`, `தொழில்`, `இயற்கை`, `மகப்பெயர்`, `அவண்`, `மெய்ம்மையாக`, exact `ஆ` / `மா`, and `இரா`; `மரப்பெயர்` and `புலவர்` formulas remain incidental where appropriate; explicit `செய்யுளுள்` / `செய்யுள் கண்ணிய` support narrow poetic-text-form context only.

### உயிர்மயங்கியல் 0229–0253

Reviewed spec: `research/production/tolkappiyam/review-specs/0229-0253.json`.

This boundary adds **30 formal observations** and **7 incidental examples**.

- 0229 `நிலா` remains exact grammatical lexical evidence, not a historical calendrical/environmental assertion.
- 0230 `யாமரம்`, `பிடா`, `தளா` and 0232 `மாமரக் கிளவி` are incidental flora-language only.
- 0232 exact `ஆ` / `மா` remain unresolved grammatical forms, not automatic fauna evidence.
- 0235/0238 `செய்யுளுள்` support narrow `textual.poetic_form.formal_context` only.
- 0237 `காலை` / `இடம்` remain grammatical wording rather than historical time/geography.
- 0240 `பதக்கு` / `தூணி` are not promoted into historical economy/metrology.
- 0242 `பனி` is incidental weather-language; 0243 `வளி` is incidental environmental language.
- 0244 `உதிமரம்`, 0245 `புளிமரம்`, 0246 `புளிப் பெயர்` remain incidental flora-language only.
- 0248 `தொழில்நிலைக் கிளவி` is grammatical rather than occupation evidence; `நாள்` is not a historical date/event assertion.
- 0249 `திங்கள்` remains the grammatical lexical form, not a historical calendrical assertion.
- 0251–0252 `இடம் வரை கிளவி` is grammatical, not geography; 0252 `உடன் நிலை மொழி` supports formal word-structure evidence.
- No new controlled concept was required.

Across உயிர்மயங்கியல் `0204–0253`, the two completed boundaries contribute **63 formal observations** and **10 incidental examples**.

### உயிர்மயங்கியல் 0254–0278

Reviewed spec: `research/production/tolkappiyam/review-specs/0254-0278.json`.

This boundary adds **31 formal grammatical/poetics observations** and **3 incidental examples**. `காலை`, `இடன்`, grammatical `மெய்`, `இயற்கை`, and `எண்` remain contextual; `எரு` / `செரு` are not promoted into historical landscape, agriculture, or warfare claims; `ஒடுமரம்` / `உதி மரம்` and `பூ` remain incidental flora-language; `ஆடூஉ` / `மகடூஉ` remain grammatical பெயர் forms rather than historical kinship/gender claims; `என்மனார் புலவர்` remains an incidental learned-authority formula; `செய்யுள் மருங்கின்` supports only narrow formal poetic-text context. No new controlled concept was required.

### உயிர்மயங்கியல் 0279–0296 — complete

Reviewed spec: `research/production/tolkappiyam/review-specs/0279-0296.json`.

This final boundary adds **22 formal grammatical/poetics observations** and **10 incidental examples**. Across உயிர்மயங்கியல் `0204–0296`, the four boundaries contribute **116 formal observations** and **23 incidental examples**. Durable guards preserve tree/plant names, `பெற்றம்`, calendrical/weather terms, emotional lexical forms, grammatical `மெய்` / `உயிர்` / `இயற்கை`, and learned-authority formulas without unsupported historical promotion. No new controlled concept was required.

### புள்ளிமயங்கியல் 0397–0406 — complete

Reviewed spec: `research/production/tolkappiyam/review-specs/0397-0406.json`.

This final boundary adds **12 formal grammatical/poetics observations** and **2 incidental examples**. Across புள்ளிமயங்கியல் `0297–0406`, five publication boundaries contribute **136 formal observations** and **21 incidental examples**. Durable guards preserve grammatical class labels, kinship/name formulas, learned-authority and inherited-tradition wording, quantification, environmental/material/fauna/flora lexical examples, and ambiguous forms without unsupported historical promotion. No new controlled concept was required.

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

## Publication cadence and long-range path

Semantic review is always sequential/source-first and one production spec never crosses an இயல் boundary.

Normal publication preference remains contiguous chunks of at most 25 records. உயிர்மயங்கியல் follows `0204–0228`, `0229–0253`, `0254–0278`, `0279–0296`.

After உயிர்மயங்கியல், frozen canonical order is:

- **புள்ளிமயங்கியல் `0297–0406` / 110 records**;
- **குற்றியலுகரப்புணரியல் `0407–0483` / 77 records**.

The user has asked to work toward உயிர்மயங்கியல் and குற்றியலுகரப்புணரியல். Preserve the gap-free prefix: finish உயிர்மயங்கியல், then complete புள்ளிமயங்கியல், then proceed through குற்றியலுகரப்புணரியல். Do not skip `0297–0406`.

## Required next activity — உயிர்மயங்கியல் 0254–0278

Review **எழுத்ததிகாரம் / உயிர்மயங்கியல் `0254–0278` (25 records)**.

For every record:

1. read the complete frozen நூற்பா and current இயல் context;
2. consider all 29 dimensions;
3. fix formal evidence, incidental examples and reviewed-empty decisions before moving to the next record;
4. preserve exact Tamil terms and source spans;
5. do not use the old crosswalk to manufacture a classification;
6. only after all fresh decisions for the semantic batch are complete, compare with the old manifest/crosswalk as control;
7. materialize only the contiguous gap-free `0254–0278` boundary;
8. validate exact counts from the production validator;
9. update current handover/status documentation;
10. finish on one clean user-authored/squashed checkpoint with full exact-head PR CI green.

Do not begin `0279–0296` until `0254–0278` is green.

## Hard boundaries

- Frozen `corpus/tolkappiyam/` is immutable.
- Exact source Tamil wins over generalized labels.
- Grammatical examples are not automatic historical facts.
- Tolkāppiyam evidence never auto-classifies Puṟanāṉūṟu or another work.
- Empty means no qualifying evidence in that reviewed நூற்பா, not historical absence.
- Keep PR #4 draft/unmerged.
- Do not start R2.
