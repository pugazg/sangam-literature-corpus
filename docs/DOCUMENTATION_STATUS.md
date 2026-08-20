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
- Tolkāppiyam production: active in எழுத்ததிகாரம் / உருபியல்
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

`0001–0198` is the current materialized gap-free production prefix:

- reviewed: **198 / 1,602**;
- remaining: **1,404**;
- next: **tolkappiyam-0199**;
- formal grammatical/poetics concept evidence: **249**;
- incidental examples: **23**;
- dimensions per record: **29**;
- regression suite: **228 passed** at materialization.

Completed இயல்:

- `0001–0033` — எழுத்ததிகாரம் / நூல் மரபு;
- `0034–0082` — எழுத்ததிகாரம் / மொழி மரபு;
- `0083–0103` — எழுத்ததிகாரம் / பிறப்பியல்;
- `0104–0143` — எழுத்ததிகாரம் / புணரியல்;
- `0144–0173` — எழுத்ததிகாரம் / தொகைமரபு.

Current partial இயல்:

- `0174–0198` — எழுத்ததிகாரம் / உருபியல், first 25 of 30 records;
- remaining உருபியல் publication boundary: `0199–0203`.

The current review spec is `research/production/tolkappiyam/review-specs/0174-0198.json`.

## Durable boundaries through 0198

Earlier நூல் மரபு, மொழி மரபு, பிறப்பியல், புணரியல் and தொகைமரபு guardrails remain binding, including contextual treatment of grammatical `உயிர்`, `மெய்`, `இசை`, `காலை`, `பொருள்`, `உயர்திணை`, `அஃறிணை`, `தொழில்`, articulation anatomy, measure vocabulary, and unresolved learned-authority formulas.

### உருபியல் 0174–0198

- `சாரியை`, `வேற்றுமை உருபு`, inflectional/end-form selection and noun/pronoun classes are formal `knowledge.grammar.morphology` where the rule classifies or constrains grammatical form.
- Explicit joining, loss, shortening, consonant/vowel change and comparable boundary behavior are formal `knowledge.grammar.morphophonology`; some நூற்பா legitimately support both morphology and morphophonology.
- 0179 `புலவர்` / `என்மனார் புலவர்` are incidental learned-role/attribution evidence only. They do not resolve a historical group, author or external text.
- 0182 `மரப்பெயர்` is a grammatical lexical class referring to tree-name words. It is retained as incidental flora-language only and does not establish a specific plant occurrence or historical ecology.
- 0191 `உயர்திணை` is a grammatical noun-class condition, not historical social hierarchy, caste/community, status, gender or kinship evidence.
- 0198 `இயற்கை` / `செயற்கை` describe grammatical/formal behavior in context. They are not promoted to environmental evidence or a separate historical technology claim.

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

No new controlled concept was required for `0174–0198`.

## Publication cadence

Semantic review is always one நூற்பா at a time, source-first, and a production spec never crosses an இயல் boundary.

Normal publication preference remains contiguous chunks of at most 25 records. A >25 full-இயல் publication requires explicit user direction. உருபியல் therefore uses normal boundaries `0174–0198` and `0199–0203`.

## Source terminology boundary

`docs/SOURCE_TERMINOLOGY_POLICY.md` remains mandatory. Retain exact Tamil and do not silently map source terms to later caste/community, hierarchy, sectarian, deity, taxonomy or modern identity categories. Tolkāppiyam formal categories and incidental examples are not automatic historical claims.

Tolkāppiyam evidence must never auto-classify Puṟanāṉūṟu or another Sangam poem.

## Current operational documents

The current authority set includes:

- `README.md`
- `PROJECT_GUIDELINES.md`
- `PROJECT_HANDOVER.md`
- `NEXT_CHAT_PROMPT.md`
- `docs/DOCUMENTATION_STATUS.md`
- `docs/SOURCE_TERMINOLOGY_POLICY.md`
- `docs/CLASSICAL_TAMIL_RESEARCH_MATRIX.md`
- `docs/classical-tamil-research-layer.md`
- `docs/handover/r15a-production-review/README.md`
- `research/production/purananuru/README.md`
- `research/production/tolkappiyam/README.md`
- `research/observations/tolkappiyam/README.md`
- `research/audits/r15-premerge/tolkappiyam/review-manifest.json`
- `research/audits/r15-premerge/tolkappiyam/dimension-crosswalk.json`

Historical handovers/audits remain truthful records of their own boundaries.

## Next activity

Proceed with **Tolkāppiyam எழுத்ததிகாரம் / உருபியல் `0199–0203`**, sequentially/source-first across all 29 dimensions. Only after fresh decisions may the old control artifacts be consulted. Preserve exact source terminology, materialize the contiguous gap-free boundary, validate exact totals, and finish on a clean exact-head PR checkpoint.

**Do not start R2.**
