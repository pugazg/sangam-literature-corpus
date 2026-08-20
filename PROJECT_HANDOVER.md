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

Puṟanāṉūṟu `001.json` through `400.json` form the complete gap-free production corpus.

Durable cadence history remains:

- benchmark `001–002`;
- stabilization **003–010**;
- regular **25-record** batches beginning **011–035** through `361–385`;
- final batch `386–400`.

The validated completion state is 400 reviewed / 0 remaining / 7,169 production observations / 29 dimensions. Existing source-terminology/source-loss guardrails remain binding, including record 176, damaged record 200 and source-lost records 267–268.

## Tolkāppiyam R1.5A production — six எழுத்ததிகாரம் இயல் complete

Tolkāppiyam is a **separate grammatical/poetics evidence stream** over the frozen hierarchy:

`work → 3 அதிகாரம் → 27 இயல் → 1,602 நூற்பா`

Canonical production identity is source sequence: `tolkappiyam-0001` … `tolkappiyam-1602`.

Current materialized gap-free boundary:

- `0001.json` through `0203.json`;
- reviewed: **203 / 1,602**;
- remaining: **1,399**;
- next record: **tolkappiyam-0204**;
- next இயல்: **எழுத்ததிகாரம் / உயிர்மயங்கியல்**;
- formal grammatical/poetics concept evidence: **259**;
- incidental examples: **23**;
- exact dimensions per record: **29**;
- regression suite: **228 passed** at materialization.

Completed இயல்:

1. `0001–0033` — எழுத்ததிகாரம் / நூல் மரபு;
2. `0034–0082` — எழுத்ததிகாரம் / மொழி மரபு;
3. `0083–0103` — எழுத்ததிகாரம் / பிறப்பியல்;
4. `0104–0143` — எழுத்ததிகாரம் / புணரியல்;
5. `0144–0173` — எழுத்ததிகாரம் / தொகைமரபு;
6. `0174–0203` — எழுத்ததிகாரம் / உருபியல், published under normal boundaries `0174–0198` and `0199–0203`.

Every production record is reviewed source-first; the old manifest/crosswalk is consulted only after fresh decisions.

## Tolkāppiyam evidence contract

Every நூற்பா is reviewed sequentially across all 29 dimensions. For every dimension distinguish:

1. formal grammatical/poetics concept evidence;
2. incidental example evidence;
3. no qualifying evidence identified.

Only formal evidence is flattened into `research/observations/tolkappiyam/r15-production.ndjson` as `GRAMMATICAL_CONCEPT_EVIDENCE` with classification basis `tolkappiyam_mapping`. Incidental examples remain inside per-record review and must not become automatic historical, ecological, social, material, identity or lived-life claims.

The old `research/audits/r15-premerge/tolkappiyam/review-manifest.json` and `dimension-crosswalk.json` remain coverage/representative-control artifacts. They never manufacture classifications. The materializer is deterministic expansion only, never a classifier.

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

These are intentionally narrow formal concepts. They do not establish historical technology, medicine, social identity, market systems, external text identity, or performance events without source support. No new concept was needed for உருபியல் `0174–0203`.

## Durable lessons before உருபியல்

Earlier நூல் மரபு and மொழி மரபு guardrails remain binding, especially contextual treatment of `உயிர்`, `மெய்`, ordinary grammatical `இசை`, `காலை`, `பொருள்`, `உயர்திணை` and `அஃறிணை`.

### பிறப்பியல் 0083–0103

- Formal grammar explicitly uses articulatory body structures and airflow to explain sound production. `body.articulation.anatomy` captures this source-explicit formal anatomy without turning it into diagnosis, medicine or a reconstructed physiological system.
- 0102 `அளபின் கோடல் அந்தணர் மறைத்தே` is preserved exactly. It supports an unresolved formal tradition/authority reference; `அந்தணர்` remains an incidental learned-role term. Do not substitute later caste/community/sectarian identities.

### புணரியல் 0104–0143

- Fresh review requires distinct morphology and morphophonology concepts. `வேற்றுமை உருபு`, `சாரியை`, noun classes, பெயர்/தொழில் and boundary sound/form changes are formal grammar.
- `உயர்திணை` / `அஃறிணை` remain grammatical classes, not social hierarchy or human-gender claims.
- 0125 `நாள்` is an incidental lexical time example inside a form rule, not a dated event.
- 0131 `புலவர்` and `என்மனார் புலவர்` are incidental learned-role/attribution evidence only.
- `தொழில்`, `உடம்படுமெய்`, and `பொருள்` stay grammatical where the rule uses them that way; they do not create occupation/body/economy evidence by lexical resemblance.

### தொகைமரபு 0144–0173

- `knowledge.grammar.quantification` captures formal `அளவு` / `நிறை` / `எண்` classification, alongside morphology/morphophonology.
- Measure expressions such as `அரை`, `கலம்`, `பனை`, `கா`, `அளவு`, `நிறை` are retained as incidental economy/measurement vocabulary where source-explicit, but do not establish a market, transaction system or standardized metrology.
- 0170 `பனை` is the name of a measure expression in its grammatical context and is not flora evidence.
- 0147 and 0159 preserve `புலவர்` / `என்மனார் புலவர்` only as incidental role/attribution evidence.

## உருபியல் 0174–0203 — complete

All 30 உருபியல் நூற்பா were reviewed sequentially/source-first across all 29 dimensions before control comparison, using the normal publication cadence:

- `research/production/tolkappiyam/review-specs/0174-0198.json` — first 25 records;
- `research/production/tolkappiyam/review-specs/0199-0203.json` — remaining 5 records.

Full உருபியல் adds **41 formal observations** and **3 incidental examples**: 31 + 3 in the first publication boundary, then 10 + 0 in the closing boundary.

Durable decisions:

- `சாரியை`, `வேற்றுமை உருபு`, inflection/end-form selection and grammatical noun/pronoun classes are formal `knowledge.grammar.morphology` where source-explicit.
- Explicit joining, loss, shortening and letter/form change at grammatical boundaries are `knowledge.grammar.morphophonology`; some rules support both morphology and morphophonology.
- 0179 `புலவர்` / `என்மனார் புலவர்` remain incidental learned-role/attribution evidence only, not a resolved historical group, author or external text.
- 0182 `மரப்பெயர்` remains incidental tree-name/flora-language inside a grammatical lexical class; it does not establish a specific plant occurrence or historical ecology.
- 0191 `உயர்திணை` is a grammatical noun-class condition, not historical hierarchy, caste/community, status, gender or kinship evidence.
- 0198 `இயற்கை` / `செயற்கை` are grammatical/formal terminology in context, not environmental evidence or a separate historical technology claim.
- 0199 `எண்` is a form-governing grammatical category: formal quantification plus morphology, not historical numeracy or economy.
- 0200 `ஒன்று`–`பத்து` are formal grammatical quantification; intermediary `ஆன்` is morphology and explicit loss/retention is morphophonology. The numeral range does not establish accounting, trade, prices or standardized metrology. `காலை` is analytic/grammatical, not historical time.
- 0201 combines morphology with explicit ஆய்தம் loss as morphophonology.
- 0202 `திசைப் பெயர்` is a grammatical lexical class under seventh-case/சாரியை morphology; final-consonant loss is morphophonology. `திசைப் பெயர்` and grammatical `இயற்கை` do not establish geography, routes, landscape or environmental conditions.
- 0203 closes உருபியல் with generalized case-marker/சாரியை morphology. `உயிர்` in `உயிர் இறு கிளவி` is the grammatical vowel category, not life/body/health evidence; `தேரும் காலை` is analytic phrasing, not time evidence.

## Tolkāppiyam publication cadence

The governing rule remains இயல்-aware sequential review:

- never cross an இயல் boundary in a production spec;
- semantic review is always strictly நூற்பா-by-நூற்பா and source-first;
- normal publication preference is chunks of at most 25 records;
- a >25 full-இயல் publication requires explicit user direction, as previously done for மொழி மரபு 0034–0082.

உருபியல் followed the normal cadence and is now complete.

## Source terminology rule

`docs/SOURCE_TERMINOLOGY_POLICY.md` is mandatory.

Retain exact source Tamil. Do not silently substitute later identity, hierarchy, caste/community, sectarian, deity, taxonomy, modern-community or external-influence labels. Formal grammatical categories, lexical examples and historical claims remain distinct.

A Tolkāppiyam rule never automatically classifies Puṟanāṉūṟu or another Sangam poem.

## Next permitted activity

Proceed from **tolkappiyam-0204**, confirmed as the first நூற்பா of **எழுத்ததிகாரம் / உயிர்மயங்கியல்**. Before publishing a review spec, resolve the full frozen உயிர்மயங்கியல் boundary from the canonical hierarchy. Then review sequentially/source-first across all 29 dimensions and use normal contiguous chunks of at most 25 unless the user explicitly authorizes another >25 full-இயல் exception.

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
