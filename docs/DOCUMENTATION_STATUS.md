# Documentation status — R1.5A production review

## Live phase state

- repository: `pugazg/sangam-literature-corpus`
- default branch: `main`
- R1.5 merge commit on `main`: `d82f9c78f27f9c9daf8fbb913d01ddfb29bddba1`
- PR #3: merged / historical
- active branch: `research/classical-tamil-concept-matrix-r1.5a`
- active PR: #4, draft/unmerged
- current phase: R1.5A production review
- Puṟanāṉūṟu production: complete
- Tolkāppiyam production: six எழுத்ததிகாரம் இயல் complete; உயிர்மயங்கியல் active
- R2: blocked / not started

R1.5A keeps schema `0.3.0` and the same exact 29 dimensions.

## Puṟanāṉūṟu completed state

Puṟanāṉūṟu `001–400` is complete and validated at 400 reviewed / 0 remaining / 7,169 observations / 29 dimensions.

Durable cadence history remains benchmark `001–002`, stabilization **003–010**, regular **25-record** batches from **011–035** through `361–385`, then final `386–400`.

## Tolkāppiyam production contract

Tolkāppiyam is a separate grammatical/poetics evidence stream over the frozen `3 அதிகாரம் / 27 இயல் / 1,602 நூற்பா` hierarchy.

Per-நூற்பா review distinguishes formal grammatical/poetics concept evidence, incidental examples, and no qualifying evidence identified. Only formal evidence enters `research/observations/tolkappiyam/r15-production.ndjson`; incidental examples stay in the record and are never automatic historical/lived-life claims.

The old Tolkāppiyam manifest/crosswalk remains representative control evidence only and never a classifier.

## Current Tolkāppiyam boundary

`0001–0228` is the current materialized gap-free production prefix:

- reviewed: **228 / 1,602**;
- remaining: **1,374**;
- next: **tolkappiyam-0229**;
- current இயல்: **எழுத்ததிகாரம் / உயிர்மயங்கியல்**;
- formal grammatical/poetics concept evidence: **292**;
- incidental examples: **26**;
- dimensions per record: **29**;
- regression suite: **228 passed** at materialization.

Completed இயல்:

- `0001–0033` — எழுத்ததிகாரம் / நூல் மரபு;
- `0034–0082` — எழுத்ததிகாரம் / மொழி மரபு;
- `0083–0103` — எழுத்ததிகாரம் / பிறப்பியல்;
- `0104–0143` — எழுத்ததிகாரம் / புணரியல்;
- `0144–0173` — எழுத்ததிகாரம் / தொகைமரபு;
- `0174–0203` — எழுத்ததிகாரம் / உருபியல்.

Current partial இயல்:

- **உயிர்மயங்கியல் = `0204–0296` (93 records)**;
- first publication boundary `0204–0228` is complete;
- remaining normal boundaries: `0229–0253`, `0254–0278`, `0279–0296`.

Current reviewed spec: `research/production/tolkappiyam/review-specs/0204-0228.json`.

## Durable boundaries through 0228

Earlier நூல் மரபு, மொழி மரபு, பிறப்பியல், புணரியல், தொகைமரபு and உருபியல் guardrails remain binding, including contextual treatment of grammatical `உயிர்`, `மெய்`, `இசை`, `காலை`, `பொருள்`, `உயர்திணை`, `அஃறிணை`, `தொழில்`, articulation anatomy, measure vocabulary, learned-authority formulas, `மரப்பெயர்`, `திசைப் பெயர்`, and grammatical `இயற்கை` / `செயற்கை`.

### உயிர்மயங்கியல் 0204–0228

The first 25 உயிர்மயங்கியல் நூற்பா were reviewed sequentially/source-first across all 29 dimensions before control comparison. This boundary adds **33 formal observations** and **3 incidental examples**.

- The dominant formal layer is `knowledge.grammar.morphophonology`: doubling, addition, loss, lengthening, alternation and default boundary behavior are recorded only where source-explicit.
- `knowledge.grammar.morphology` is used where the source actually assigns or delimits grammatical form classes, சாரியை or உருபு behavior.
- `knowledge.grammar.word_structure` is used for explicit structural categories such as `தொடர்மொழி`, `தொடர் அல்`, `இரு பெயர்த் தொகைமொழி` and `ஓரெழுத்து மொழி`.
- 0208 grammatical `உயிர்` means vowel and is not body/health/life evidence.
- 0209 `செய்யுளுள்` and 0214 `செய்யுள் கண்ணிய` support the narrow formal `textual.poetic_form.formal_context`; neither identifies an external work nor establishes a historical performance event.
- 0211 grammatical `தொழில்` / `உரைப்பொருட் கிளவி` do not become occupation/economy evidence.
- 0216 `இயற்கை` is grammatical/formal terminology, not environmental evidence.
- 0218 `மரப்பெயர்` is retained as incidental tree-name/flora-language only; it does not establish a specific plant occurrence or historical ecology.
- 0219 `மகப்பெயர்` is the exact source label of a grammatical lexical class and is not promoted into a historical family, gender or kinship claim.
- 0220 `அவண்` is positional/deictic inside the grammatical rule and does not establish geography, route or landscape.
- 0223 `புலவர்` / `என்மனார் புலவர்` remain incidental learned-role/attribution evidence only.
- 0224 `இரு பெயர்த் தொகைமொழி` is formal word-structure evidence; `மெய்ம்மையாக` is not body/health evidence.
- 0225 grammatical `தொழில்` does not become occupation evidence; exact forms `ஆ` / `மா` are not silently resolved into fauna.
- 0228 `இரா` is preserved as the grammatical form governed by the rule and is not promoted into historical time/night evidence.
- No new controlled concept was required for `0204–0228`.

## Current stream-specific concepts

The Tolkāppiyam extension registry includes:

- `knowledge.grammar.phonology`;
- `knowledge.grammar.word_structure`;
- `knowledge.grammar.morphology`;
- `knowledge.grammar.morphophonology`;
- `knowledge.grammar.quantification`;
- `body.articulation.anatomy`;
- `arts.music.formal_context`;
- `textual.tradition.reference`;
- `textual.poetic_form.formal_context`.

## Publication cadence

Semantic review is always one நூற்பா at a time, source-first, and a production spec never crosses an இயல் boundary.

Normal publication preference remains contiguous chunks of at most 25 records. A >25 full-இயல் publication requires explicit user direction. உயிர்மயங்கியல் therefore follows `0204–0228`, `0229–0253`, `0254–0278`, `0279–0296`.

## Source terminology boundary

`docs/SOURCE_TERMINOLOGY_POLICY.md` remains mandatory. Retain exact Tamil and do not silently map source terms to later caste/community, hierarchy, sectarian, deity, taxonomy or modern identity categories. Tolkāppiyam formal categories and incidental examples are not automatic historical claims.

Tolkāppiyam evidence must never auto-classify Puṟanāṉūṟu or another Sangam poem.

## Current operational documents

The current authority set includes `PROJECT_GUIDELINES.md`, `PROJECT_HANDOVER.md`, `NEXT_CHAT_PROMPT.md`, this file, `docs/SOURCE_TERMINOLOGY_POLICY.md`, the R1.5A production handover, the Puṟanāṉūṟu/Tolkāppiyam production READMEs, the Tolkāppiyam observation README, schemas, concept extension, old manifest/crosswalk controls, materializer and validator.

Historical handovers/audits remain truthful records of their own boundaries.

## Next activity

Proceed with **Tolkāppiyam எழுத்ததிகாரம் / உயிர்மயங்கியல் `0229–0253`**, sequentially/source-first across all 29 dimensions. Only after fresh decisions may the old control artifacts be consulted. Preserve exact source terminology, materialize the contiguous gap-free boundary, validate exact totals, and finish on a clean exact-head PR checkpoint.

**Do not start R2.**
