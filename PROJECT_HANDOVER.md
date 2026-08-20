# Sangam Literature Corpus — Project Handover

## Authoritative current state

Repository: `pugazg/sangam-literature-corpus`

Default branch: `main`

Active research branch: `research/classical-tamil-concept-matrix-r1.5a`

R1.5 was explicitly authorized and merged into `main` at `d82f9c78f27f9c9daf8fbb913d01ddfb29bddba1`. PR #3 is historical/merged. Draft PR #4 is the active R1.5A proposal.

R1.5A keeps concept/observation schema `0.3.0`; it is not R2. **R2 remains blocked and must not start without explicit user authorization.** Treat live GitHub state as authoritative over older prose.

## Frozen corpus and preserved layers

Classical Tamil Corpus 1.1.0 remains frozen: 28 works / 7,234 canonical records / 5,632 poems / 1,602 Tolkāppiyam நூற்பா. Tag: `classical-tamil-corpus-v1.1.0`.

R0 schema `0.1.0`, R1 schema `0.2.0`, and the bounded R1.5 pilot remain preserved. R1.5 schema `0.3.0` remains the exact 29-dimension concept/evidence foundation. Old Puṟanāṉūṟu/Tolkāppiyam audits are post-review control evidence only and never classifiers.

## Puṟanāṉūṟu R1.5A production — complete

Puṟanāṉūṟu `001.json` through `400.json` form the complete gap-free production corpus. Durable cadence remains benchmark `001–002`, stabilization **003–010**, regular **25-record** batches beginning **011–035** through `361–385`, and final `386–400`.

Validated completion: **400 reviewed / 0 remaining / 7,169 production observations / 29 dimensions**.

## Tolkāppiyam R1.5A production — உயிர்மயங்கியல் active

Tolkāppiyam is a separate grammatical/poetics evidence stream over the frozen hierarchy:

`work → 3 அதிகாரம் → 27 இயல் → 1,602 நூற்பா`

Canonical production identity is source sequence: `tolkappiyam-0001` … `tolkappiyam-1602`.

Current materialized gap-free boundary:

- `0001.json` through `0406.json`;
- reviewed: **406 / 1,602**;
- remaining: **1,196**;
- next record: **tolkappiyam-0407**;
- next இயல்: **எழுத்ததிகாரம் / குற்றியலுகரப்புணரியல்**;
- formal grammatical/poetics concept evidence: **511**;
- incidental examples: **67**;
- exact dimensions per record: **29**;
- regression suite: **228 passed** at materialization.

Completed எழுத்ததிகாரம் இயல்:

1. `0001–0033` — நூல் மரபு;
2. `0034–0082` — மொழி மரபு;
3. `0083–0103` — பிறப்பியல்;
4. `0104–0143` — புணரியல்;
5. `0144–0173` — தொகைமரபு;
6. `0174–0203` — உருபியல்.

உயிர்மயங்கியல் `0204–0296` is complete across publication boundaries `0204–0228`, `0229–0253`, `0254–0278`, and `0279–0296`.

Every production record is reviewed source-first; the old manifest/crosswalk is consulted only after fresh decisions.

## Tolkāppiyam evidence contract

Every நூற்பா is reviewed sequentially across all 29 dimensions. For every dimension distinguish:

1. formal grammatical/poetics concept evidence;
2. incidental example evidence;
3. no qualifying evidence identified.

Only formal evidence is flattened into `research/observations/tolkappiyam/r15-production.ndjson` as `GRAMMATICAL_CONCEPT_EVIDENCE` with classification basis `tolkappiyam_mapping`. Incidental examples remain inside per-record review and must not become automatic historical, ecological, social, material, identity or lived-life claims.

The old `review-manifest.json` and `dimension-crosswalk.json` remain coverage/representative-control artifacts. They never manufacture classifications. The materializer is deterministic expansion only, never a classifier.

## Controlled concepts

Current Tolkāppiyam extension concepts:

- `knowledge.grammar.phonology`;
- `knowledge.grammar.word_structure`;
- `knowledge.grammar.morphology`;
- `knowledge.grammar.morphophonology`;
- `knowledge.grammar.quantification`;
- `body.articulation.anatomy`;
- `arts.music.formal_context`;
- `textual.tradition.reference`;
- `textual.poetic_form.formal_context`.

These are intentionally narrow formal concepts and do not establish historical technology, medicine, social identity, market systems, external-text identity or performance events without source support.

## Durable lexical/source lessons

All earlier guardrails remain binding. In particular:

- grammatical `உயிர்`, `மெய்`, ordinary `இசை`, `காலை`, `பொருள்`, `உயர்திணை`, `அஃறிணை`, `தொழில்` remain contextual rather than being promoted by surface resemblance;
- பிறப்பியல் articulation anatomy is formal grammar, not medicine;
- 0102 exact `அளபின் கோடல் அந்தணர் மறைத்தே` keeps source terminology; `அந்தணர்` is incidental learned-role evidence, not a silently substituted later identity;
- `புலவர்` / `என்மனார் புலவர்` attribution formulas remain unresolved/incidental unless the source itself establishes more;
- தொகைமரபு `அளவு` / `நிறை` / `எண்` and measure vocabulary do not reconstruct markets or standardized metrology;
- `மரப்பெயர்` can be retained as incidental flora-language while remaining a grammatical lexical class;
- `திசைப் பெயர்` does not automatically become geography;
- grammatical `இயற்கை` / `செயற்கை` do not automatically become environmental or historical-technology claims.

## உருபியல் 0174–0203 — complete

உருபியல் used normal publication boundaries `0174–0198` and `0199–0203`, adding **41 formal observations** and **3 incidental examples**. Morphology and morphophonology remain distinct; its lexical safeguards remain binding.

## உயிர்மயங்கியல் — production through 0253

The full frozen boundary is **0204–0296 / 93 records**.

### 0204–0228

Reviewed spec: `research/production/tolkappiyam/review-specs/0204-0228.json`.

Adds **33 formal observations** and **3 incidental examples**.

Key guardrails: grammatical `உயிர்`, `தொழில்`, `இயற்கை`, `மகப்பெயர்`, `அவண்`, `மெய்ம்மையாக`, `ஆ` / `மா`, and `இரா` remain contextual; `மரப்பெயர்` and `புலவர்` formulas are incidental where appropriate; explicit `செய்யுளுள்` / `செய்யுள் கண்ணிய` support narrow `textual.poetic_form.formal_context` only.

### 0229–0253

Reviewed spec: `research/production/tolkappiyam/review-specs/0229-0253.json`.

Adds **30 formal observations** and **7 incidental examples**.

Durable decisions:

- 0229 `நிலா` is exact grammatical lexical evidence, not a historical calendrical/environmental claim;
- 0230 `யாமரம்`, `பிடா`, `தளா` and 0232 `மாமரக் கிளவி` are incidental flora-language only;
- 0232 exact `ஆ` / `மா` remain unresolved grammatical forms and are not automatic fauna evidence;
- 0235/0238 `செய்யுளுள்` support narrow formal poetic-text context only;
- 0237 `காலை` / `இடம்` remain grammatical wording rather than historical time/geography;
- 0240 `பதக்கு` / `தூணி` are not promoted into historical economy/metrology;
- 0242 `பனி` is incidental weather-language; 0243 `வளி` is incidental environmental language;
- 0244 `உதிமரம்`, 0245 `புளிமரம்`, 0246 `புளிப் பெயர்` remain incidental flora-language only;
- 0248 `தொழில்நிலைக் கிளவி` is grammatical, while `நாள்` is not a historical date/event assertion;
- 0249 `திங்கள்` remains the grammatical lexical form, not a historical calendrical assertion;
- 0251–0252 `இடம் வரை கிளவி` is grammatical rather than geographic; 0252 `உடன் நிலை மொழி` supports formal word-structure evidence.

No new controlled concept was required.

Across completed உயிர்மயங்கியல் `0204–0253`, totals added are **63 formal observations** and **10 incidental examples**.

### உயிர்மயங்கியல் 0254–0278

Reviewed spec: `research/production/tolkappiyam/review-specs/0254-0278.json`.

This boundary adds **31 formal grammatical/poetics observations** and **3 incidental examples**. `காலை`, `இடன்`, grammatical `மெய்`, `இயற்கை`, and `எண்` remain contextual; `எரு` / `செரு` are not promoted into historical landscape, agriculture, or warfare claims; `ஒடுமரம்` / `உதி மரம்` and `பூ` remain incidental flora-language; `ஆடூஉ` / `மகடூஉ` remain grammatical பெயர் forms rather than historical kinship/gender claims; `என்மனார் புலவர்` remains an incidental learned-authority formula; `செய்யுள் மருங்கின்` supports only narrow formal poetic-text context. No new controlled concept was required.

### உயிர்மயங்கியல் 0279–0296 — complete

Reviewed spec: `research/production/tolkappiyam/review-specs/0279-0296.json`.

This final boundary adds **22 formal grammatical/poetics observations** and **10 incidental examples**. Across உயிர்மயங்கியல் `0204–0296`, the four boundaries contribute **116 formal observations** and **23 incidental examples**. Durable guards preserve tree/plant names, `பெற்றம்`, calendrical/weather terms, emotional lexical forms, grammatical `மெய்` / `உயிர்` / `இயற்கை`, and learned-authority formulas without unsupported historical promotion. No new controlled concept was required.

### புள்ளிமயங்கியல் 0397–0406 — complete

Reviewed spec: `research/production/tolkappiyam/review-specs/0397-0406.json`.

This final boundary adds **12 formal grammatical/poetics observations** and **2 incidental examples**. Across புள்ளிமயங்கியல் `0297–0406`, five publication boundaries contribute **136 formal observations** and **21 incidental examples**. Durable guards preserve grammatical class labels, kinship/name formulas, learned-authority and inherited-tradition wording, quantification, environmental/material/fauna/flora lexical examples, and ambiguous forms without unsupported historical promotion. No new controlled concept was required.

## Tolkāppiyam publication cadence and requested long-range path

The governing rule remains இயல்-aware sequential review:

- never cross an இயல் boundary in a production spec;
- semantic review is always strictly நூற்பா-by-நூற்பா and source-first;
- normal publication preference is chunks of at most 25 records.

உயிர்மயங்கியல் follows `0204–0228`, `0229–0253`, `0254–0278`, `0279–0296`.

After உயிர்மயங்கியல் the frozen canonical order is:

- **புள்ளிமயங்கியல் `0297–0406` / 110 records**;
- **குற்றியலுகரப்புணரியல் `0407–0483` / 77 records**.

The user has asked to work toward both உயிர்மயங்கியல் and குற்றியலுகரப்புணரியல். Preserve the gap-free contract: finish உயிர்மயங்கியல், then process புள்ளிமயங்கியல் in canonical order, then proceed through குற்றியலுகரப்புணரியல். Do not skip `0297–0406`.

## Source terminology rule

`docs/SOURCE_TERMINOLOGY_POLICY.md` is mandatory. Retain exact source Tamil. Do not silently substitute later identity, hierarchy, caste/community, sectarian, deity, taxonomy, modern-community or external-influence labels. Formal grammatical categories, lexical examples and historical claims remain distinct.

A Tolkāppiyam rule never automatically classifies Puṟanāṉūṟu or another Sangam poem.

## Next permitted activity

Proceed with **Tolkāppiyam எழுத்ததிகாரம் / குற்றியலுகரப்புணரியல் `0407–0483`**. Review sequentially/source-first across all 29 dimensions; only after fresh decisions may the old manifest/crosswalk be used as control. Preserve exact source spans and terminology, materialize deterministically, and require full exact-head PR CI at the publication boundary.

Do not begin `0279–0296` until `0254–0278` is green. Do not start R2.

## Current documentation authority

Read in this order:

1. `docs/DOCUMENTATION_STATUS.md`
2. `docs/SOURCE_TERMINOLOGY_POLICY.md`
3. `PROJECT_HANDOVER.md`
4. `PROJECT_GUIDELINES.md`
5. `NEXT_CHAT_PROMPT.md`
6. `docs/handover/r15a-production-review/README.md`
7. `research/production/purananuru/README.md`
8. `research/production/tolkappiyam/README.md`
9. `research/observations/tolkappiyam/README.md`
10. `docs/CLASSICAL_TAMIL_RESEARCH_MATRIX.md`
11. `docs/classical-tamil-research-layer.md`
12. `research/audits/r15-premerge/tolkappiyam/review-manifest.json`
13. `research/audits/r15-premerge/tolkappiyam/dimension-crosswalk.json`

PR #4 remains draft/unmerged until a later user-authorized merge boundary.
