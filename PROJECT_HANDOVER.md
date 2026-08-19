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

Durable cadence history must remain documented exactly:

- benchmark `001–002`;
- stabilization **003–010**;
- regular **25-record** batches beginning **011–035** through `361–385`;
- final batch `386–400`.

Definitive completion checkpoint: `491fa3107984b29f1dbb747bc7483e0cb694ab91`. It validates 400 reviewed / 0 remaining / 7,169 production observations / 29 dimensions. Existing source-terminology/source-loss guardrails remain binding, including record 176, damaged record 200 and source-lost records 267–268.

## Tolkāppiyam R1.5A production — நூல் மரபு + மொழி மரபு complete

Tolkāppiyam is a **separate grammatical/poetics evidence stream** over the frozen hierarchy:

`work → 3 அதிகாரம் → 27 இயல் → 1,602 நூற்பா`

Canonical production identity is source sequence: `tolkappiyam-0001` … `tolkappiyam-1602`.

Current validated gap-free boundary:

- `0001.json` through `0082.json`;
- reviewed: **82 / 1,602**;
- remaining: **1,520**;
- next record: **tolkappiyam-0083**;
- formal grammatical/poetics concept evidence: **87**;
- incidental examples: **7**;
- exact dimensions per record: **29**;
- regression suite: **228 passed**.

This completes **எழுத்ததிகாரம் / நூல் மரபு (0001–0033)** and **எழுத்ததிகாரம் / மொழி மரபு (0034–0082)**. Every production record was reviewed source-first; the old manifest/crosswalk was consulted only after fresh decisions.

## Tolkāppiyam evidence contract

Every நூற்பா is reviewed sequentially across all 29 dimensions. For every dimension distinguish:

1. formal grammatical/poetics concept evidence;
2. incidental example evidence;
3. no qualifying evidence identified.

Only formal evidence is flattened into `research/observations/tolkappiyam/r15-production.ndjson` as `GRAMMATICAL_CONCEPT_EVIDENCE` with classification basis `tolkappiyam_mapping`. Incidental examples remain inside the per-record review and must not become automatic historical, ecological, social, material, identity or lived-life claims.

The old `research/audits/r15-premerge/tolkappiyam/review-manifest.json` and `dimension-crosswalk.json` remain coverage/representative-control artifacts. They never manufacture classifications. The materializer is deterministic expansion only, never a classifier.

## Controlled concepts

Stream-specific Tolkāppiyam concepts are additive in `research/concepts/classical-tamil/tolkappiyam-production-concepts-r15a.json`.

Current concepts:

- `knowledge.grammar.phonology` → `knowledge_technology`;
- `arts.music.formal_context` → `arts_music_performance`;
- `textual.tradition.reference` → `textual_intertextual_relationships`;
- `knowledge.grammar.word_structure` → `knowledge_technology`;
- `textual.poetic_form.formal_context` → `textual_intertextual_relationships`.

The first three were established through நூல் மரபு. The latter two were required by fresh மொழி மரபு review: word-structure classification at 0043–0045/0050/0082 and explicit `செய்யுள்` text-form context at 0051. They do not broaden into historical technology, Akam/Puram classification, named external works, or performance events without source support.

## Durable lessons through 0082

Earlier நூல் மரபு guardrails remain binding, especially:

- `உயிர்` / `மெய்` as grammatical classes, not body/life/religion/truth claims;
- ordinary grammatical `இசை` wording is not automatically music/performance;
- 0033 is exceptional because its rule explicitly places sound-lengthening in an `இசை`-connected formal domain and separately refers to `நரம்பின் மறை`.

### மொழி மரபு 0034–0082

The user explicitly authorized **the entire 49-record இயல் in one publication/materialization batch**. Semantic review still proceeded strictly நூற்பா-by-நூற்பா, source-first across all 29 dimensions before the old control artifacts were opened.

The batch adds **52 formal observations + 2 incidental examples**, taking cumulative Tolkāppiyam totals to **87 formal / 7 incidental**.

Durable source-boundary lessons:

- **0034–0042:** formal phonology/morphophonology only. `சினை`, `நிலை`, `முன்னர்`, `ஊர்ந்தே`, `உயிர்`, `உரு`, `காலை`, and ordinary `இசை/இசைமை` remain grammatical wording where used that way. `குன்று இசை` in 0041 is deficient sound, not mountain/music evidence.
- **0043–0045:** formal word-structure classification (`ஓர் எழுத்து ஒருமொழி`, `ஈர் எழுத்து ஒருமொழி`, `தொடர்மொழி`) uses `knowledge.grammar.word_structure`.
- **0050:** legitimately carries two formal `knowledge_technology` concepts: phonology and word structure. `அளவு` is grammatical quantity, not calendrical time.
- **0051:** `செய்யுள் இறுதிப் போலும்` is formal textual/poetic-form context under `textual_intertextual_relationships`; it is not Akam/Puram `literary_domain` evidence and not a performance event.
- **0053:** `இசைப்பினும்` is pronunciation/sound, not music. `புலவர்` and `என்மனார் புலவர்` remain incidental role/attribution evidence only.
- **0057:** `தேரும் காலை` means when examined/considered; it is not chariot/mobility or time-of-day evidence.
- **0066:** `தம் பெயர்` refers to grammatical names of forms, not historical named entities.
- **0067–0068:** exact source term `முறைப்பெயர்` is preserved as an unresolved grammatical class; it is not mapped to relationships/kinship. `பொருள்` is grammatical/lexical meaning, not economy/material culture.
- **0082:** `மகரத் தொடர்மொழி` / `னகரத் தொடர்மொழி` support both phonology and word structure. `அஃறிணை` remains a grammatical class, not a social group or human gender category; `புகர் அற` is not promoted to an ethical-value claim.

## Tolkāppiyam publication cadence

The governing rule remains **இயல்-aware sequential review**:

- never cross an இயல் boundary in a production spec;
- semantic review is always strictly நூற்பா-by-நூற்பா and source-first;
- the previous normal publication preference was chunks of at most 25 records;
- **மொழி மரபு 0034–0082 is a user-authorized full-இயல் exception: all 49 reviewed records were published/materialized in one contiguous spec**;
- a future whole-இயல் batch larger than 25 requires the same explicit user direction rather than being inferred automatically.

Immediate next batch:

- **0083–0103** — 21 records, completes எழுத்ததிகாரம் / பிறப்பியல்.

## Source terminology rule

`docs/SOURCE_TERMINOLOGY_POLICY.md` is mandatory.

Retain exact source Tamil. Do not silently substitute later identity, hierarchy, caste/community, sectarian, deity, taxonomy, modern-community or external-influence labels. Formal grammatical categories, lexical examples and historical claims remain distinct.

A Tolkāppiyam rule never automatically classifies Puṟanāṉūṟu or another Sangam poem.

## Next permitted activity

Proceed with **Tolkāppiyam 0083–0103**, all 21 records of எழுத்ததிகாரம் / பிறப்பியல்.

For every நூற்பா:

1. read the complete frozen canonical record and current இயல் context;
2. consider all 29 dimensions;
3. fix formal evidence, incidental examples and reviewed-empty decisions before moving to the next record;
4. preserve exact source spans/Tamil terminology;
5. only after all fresh decisions are fixed, consult the old manifest/crosswalk as control;
6. stage one contiguous `0083-0103.json` spec;
7. materialize deterministically, validate the gap-free prefix, and finish on one clean user-authored/squashed checkpoint with full exact-head PR CI green.

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
