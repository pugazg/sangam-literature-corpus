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

Validated completion: **400 reviewed / 0 remaining / 7,169 production observations / 29 dimensions**. Existing source-terminology/source-loss guardrails remain binding.

## Tolkāppiyam R1.5A production — உயிர்மயங்கியல் active

Tolkāppiyam is a separate grammatical/poetics evidence stream over the frozen hierarchy:

`work → 3 அதிகாரம் → 27 இயல் → 1,602 நூற்பா`

Canonical production identity is source sequence: `tolkappiyam-0001` … `tolkappiyam-1602`.

Current materialized gap-free boundary:

- `0001.json` through `0228.json`;
- reviewed: **228 / 1,602**;
- remaining: **1,374**;
- next record: **tolkappiyam-0229**;
- current இயல்: **எழுத்ததிகாரம் / உயிர்மயங்கியல்**;
- formal grammatical/poetics concept evidence: **292**;
- incidental examples: **26**;
- exact dimensions per record: **29**;
- regression suite: **228 passed** at materialization.

Completed எழுத்ததிகாரம் இயல்:

1. `0001–0033` — நூல் மரபு;
2. `0034–0082` — மொழி மரபு;
3. `0083–0103` — பிறப்பியல்;
4. `0104–0143` — புணரியல்;
5. `0144–0173` — தொகைமரபு;
6. `0174–0203` — உருபியல்.

Current partial இயல் is **உயிர்மயங்கியல் `0204–0296` (93 records)**. The first publication boundary `0204–0228` is complete. Remaining normal boundaries are `0229–0253`, `0254–0278`, and `0279–0296`.

Every production record is reviewed source-first; the old manifest/crosswalk is consulted only after fresh decisions.

## Tolkāppiyam evidence contract

Every நூற்பா is reviewed sequentially across all 29 dimensions. For every dimension distinguish:

1. formal grammatical/poetics concept evidence;
2. incidental example evidence;
3. no qualifying evidence identified.

Only formal evidence is flattened into `research/observations/tolkappiyam/r15-production.ndjson` as `GRAMMATICAL_CONCEPT_EVIDENCE` with classification basis `tolkappiyam_mapping`. Incidental examples remain inside per-record review and must not become automatic historical, ecological, social, material, identity or lived-life claims.

The old `review-manifest.json` and `dimension-crosswalk.json` remain coverage/representative-control artifacts. They never manufacture classifications. The materializer is deterministic expansion only, never a classifier.

## Controlled concepts

Stream-specific Tolkāppiyam concepts are additive in `research/concepts/classical-tamil/tolkappiyam-production-concepts-r15a.json`.

Current concepts:

- `knowledge.grammar.phonology` → `knowledge_technology`;
- `knowledge.grammar.word_structure` → `knowledge_technology`;
- `knowledge.grammar.morphology` → `knowledge_technology`;
- `knowledge.grammar.morphophonology` → `knowledge_technology`;
- `knowledge.grammar.quantification` → `knowledge_technology`;
- `body.articulation.anatomy` → `body_health`;
- `arts.music.formal_context` → `arts_music_performance`;
- `textual.tradition.reference` → `textual_intertextual_relationships`;
- `textual.poetic_form.formal_context` → `textual_intertextual_relationships`.

These are intentionally narrow formal concepts. They do not establish historical technology, medicine, social identity, market systems, external-text identity, or performance events without source support.

## Durable lexical/source lessons

All earlier guardrails remain binding. In particular:

- grammatical `உயிர்`, `மெய்`, ordinary `இசை`, `காலை`, `பொருள்`, `உயர்திணை`, `அஃறிணை`, `தொழில்` remain contextual rather than being promoted by surface resemblance;
- பிறப்பியல் articulation anatomy is formal grammar, not medicine;
- 0102 `அளபின் கோடல் அந்தணர் மறைத்தே` keeps exact wording; `அந்தணர்` is incidental learned-role evidence, not a silently substituted later caste/community/sectarian identity;
- `புலவர்` / `என்மனார் புலவர்` attribution formulas remain unresolved/incidental unless the source itself establishes more;
- தொகைமரபு `அளவு` / `நிறை` / `எண்` formal quantification and measure vocabulary do not reconstruct markets or standardized metrology;
- `மரப்பெயர்` can be retained as incidental flora-language while remaining a grammatical lexical class;
- `திசைப் பெயர்` does not automatically become geography;
- grammatical `இயற்கை` / `செயற்கை` do not automatically become environmental or historical-technology claims.

## உருபியல் 0174–0203 — complete

உருபியல் used normal publication boundaries `0174–0198` and `0199–0203`, adding **41 formal observations** and **3 incidental examples**. Morphology and morphophonology remain distinct; `உயர்திணை`, measure/number vocabulary, `மரப்பெயர்`, `திசைப் பெயர்`, `புலவர்`, `உயிர்`, `காலை`, `இயற்கை` and `செயற்கை` retain the contextual safeguards recorded in the production specs and continuity documents.

## உயிர்மயங்கியல் 0204–0228 — first publication boundary complete

The full frozen உயிர்மயங்கியல் boundary was resolved first as **0204–0296 / 93 records**. The first 25 records were then reviewed sequentially/source-first across all 29 dimensions before the old controls were consulted.

Reviewed spec: `research/production/tolkappiyam/review-specs/0204-0228.json`.

This boundary adds **33 formal observations** and **3 incidental examples**.

Durable decisions:

- the dominant layer is `knowledge.grammar.morphophonology` for source-explicit doubling, addition, loss, lengthening, alternation and boundary behavior;
- morphology is used only where grammatical form classes, சாரியை or உருபு behavior are explicitly assigned;
- formal word-structure evidence is used for explicit `தொடர்மொழி`, `தொடர் அல்`, `இரு பெயர்த் தொகைமொழி`, `ஓரெழுத்து மொழி` conditions;
- 0208 grammatical `உயிர்` is vowel only, not life/body/health;
- 0209 `செய்யுளுள்` and 0214 `செய்யுள் கண்ணிய` support narrow `textual.poetic_form.formal_context`, not an external work identity or historical performance event;
- 0211 grammatical `தொழில்` / `உரைப்பொருட் கிளவி` do not establish occupation/economy;
- 0216 `இயற்கை` stays grammatical rather than environmental;
- 0218 `மரப்பெயர்` is incidental tree-name/flora-language only, not a plant occurrence/ecology claim;
- 0219 `மகப்பெயர்` is a grammatical lexical-class label and is not promoted into family/gender/kinship history;
- 0220 `அவண்` is positional/deictic in the grammatical rule, not geographic evidence;
- 0223 `புலவர்` / `என்மனார் புலவர்` remain incidental learned-role/attribution evidence only;
- 0224 `இரு பெயர்த் தொகைமொழி` is formal word structure; `மெய்ம்மையாக` is not body/health evidence;
- 0225 grammatical `தொழில்` is not occupation evidence; exact `ஆ` / `மா` are not silently resolved into fauna;
- 0228 `இரா` is the exact grammatical form governed by the rule and is not promoted into historical time/night evidence.

No new controlled concept was required for `0204–0228`.

## Tolkāppiyam publication cadence

The governing rule remains இயல்-aware sequential review:

- never cross an இயல் boundary in a production spec;
- semantic review is always strictly நூற்பா-by-நூற்பா and source-first;
- normal publication preference is chunks of at most 25 records;
- a >25 full-இயல் publication requires explicit user direction.

உயிர்மயங்கியல் therefore follows `0204–0228`, `0229–0253`, `0254–0278`, `0279–0296`.

## Source terminology rule

`docs/SOURCE_TERMINOLOGY_POLICY.md` is mandatory. Retain exact source Tamil. Do not silently substitute later identity, hierarchy, caste/community, sectarian, deity, taxonomy, modern-community or external-influence labels. Formal grammatical categories, lexical examples and historical claims remain distinct.

A Tolkāppiyam rule never automatically classifies Puṟanāṉūṟu or another Sangam poem.

## Next permitted activity

Proceed with **Tolkāppiyam எழுத்ததிகாரம் / உயிர்மயங்கியல் `0229–0253`**. Review sequentially/source-first across all 29 dimensions; only after fresh decisions may the old manifest/crosswalk be used as control. Preserve exact source spans and terminology, materialize deterministically, and require full exact-head PR CI at the publication boundary.

Do not start R2.

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
