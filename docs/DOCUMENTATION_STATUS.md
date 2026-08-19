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
- Tolkāppiyam production: active; நூல் மரபு + மொழி மரபு complete through 0082
- R2: blocked / not started

R1.5A keeps schema `0.3.0` and the same exact 29 dimensions.

## Puṟanāṉūṟu completed state

Puṟanāṉūṟu `001–400` is complete and validated at 400 reviewed / 0 remaining / 7,169 observations / 29 dimensions.

Durable cadence history remains benchmark `001–002`, stabilization **003–010**, regular **25-record** batches from **011–035** through `361–385`, then final `386–400`.

## Tolkāppiyam production contract

Tolkāppiyam is a separate grammatical/poetics evidence stream over the frozen `3 அதிகாரம் / 27 இயல் / 1,602 நூற்பா` hierarchy.

Per-நூற்பா production review distinguishes formal grammatical/poetics concept evidence, incidental examples, and no qualifying evidence identified. Only formal evidence enters `research/observations/tolkappiyam/r15-production.ndjson` as `GRAMMATICAL_CONCEPT_EVIDENCE`; incidental examples remain in the record and are never automatic historical/lived-life claims.

The old Tolkāppiyam manifest/crosswalk remains representative coverage/control evidence only and never a classifier.

## Current Tolkāppiyam boundary

`0001–0082` is a validated gap-free production prefix:

- reviewed: **82 / 1,602**;
- remaining: **1,520**;
- next: **tolkappiyam-0083**;
- formal grammatical/poetics concept evidence: **87**;
- incidental examples: **7**;
- dimensions per record: **29**;
- regression suite: **228 passed**.

Completed இயல்:

- `0001–0033` — எழுத்ததிகாரம் / நூல் மரபு;
- `0034–0082` — எழுத்ததிகாரம் / மொழி மரபு.

The 0034–0082 batch was reviewed sequentially/source-first across all 29 dimensions and, by explicit user instruction, published/materialized as **one 49-record full-இயல் spec**. It adds **52 formal observations + 2 incidental examples**.

Durable boundaries include:

- 0043–0045/0050/0082 formal word structure via `knowledge.grammar.word_structure`;
- 0051 formal `செய்யுள்` text-form context via `textual.poetic_form.formal_context`, not Akam/Puram literary domain;
- 0053 `இசைப்பினும்` = pronunciation/sound; `புலவர்` and attribution remain incidental;
- 0067 `முறைப்பெயர்` remains unresolved and is not mapped to kinship/relationships;
- 0068 `பொருள்` remains grammatical/lexical meaning;
- 0082 `அஃறிணை` remains a grammatical class, not a social/gender category.

## Publication cadence

Semantic review is always one நூற்பா at a time, source-first, and a production spec never crosses an இயல் boundary.

The normal publication preference remains contiguous chunks of at most 25 records. **மொழி மரபு 0034–0082 is a user-authorized exception for one full 49-record இயல் publication.** Do not generalize that exception to a later >25-record இயல் without explicit direction.

Next batch:

- `0083–0103` — 21 records, completes எழுத்ததிகாரம் / பிறப்பியல்.

## Source terminology boundary

`docs/SOURCE_TERMINOLOGY_POLICY.md` remains mandatory.

Retain exact Tamil. Do not silently map source terms to later caste/community, hierarchy, sectarian, deity, taxonomy or modern identity categories. Tolkāppiyam formal categories and incidental examples are not automatic historical claims.

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

Proceed with **Tolkāppiyam 0083–0103**, all 21 records of பிறப்பியல். Review every நூற்பா sequentially across all 29 dimensions before consulting the old control crosswalk, stage one contiguous spec, materialize, validate, squash onto the previous green checkpoint and require full exact-head PR CI green.

**Do not start R2.**
