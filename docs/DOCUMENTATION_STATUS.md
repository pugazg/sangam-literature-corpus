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
- Tolkāppiyam production: active; நூல் மரபு complete through 0033
- R2: blocked / not started

R1.5A keeps schema `0.3.0` and the same exact 29 dimensions.

## Puṟanāṉūṟu completed state

Puṟanāṉūṟu `001–400` is complete and validated at 400 reviewed / 0 remaining / 7,169 observations / 29 dimensions.

Durable cadence history remains benchmark `001–002`, stabilization `003–010`, regular **25-record** batches from `011–035` through `361–385`, then final `386–400`.

## Tolkāppiyam production contract

Tolkāppiyam is a separate grammatical/poetics evidence stream over the frozen `3 அதிகாரம் / 27 இயல் / 1,602 நூற்பா` hierarchy.

Per-நூற்பா production review distinguishes formal grammatical/poetics concept evidence, incidental examples, and no qualifying evidence identified. Only formal evidence enters `research/observations/tolkappiyam/r15-production.ndjson` as `GRAMMATICAL_CONCEPT_EVIDENCE`; incidental examples remain in the record and are never automatic historical/lived-life claims.

The old Tolkāppiyam manifest/crosswalk remains representative coverage/control evidence only and never a classifier.

## Current Tolkāppiyam boundary

`0001–0033` is a validated gap-free production prefix and completes **எழுத்ததிகாரம் / நூல் மரபு**:

- reviewed: **33 / 1,602**;
- remaining: **1,569**;
- next: **tolkappiyam-0034**;
- formal grammatical/poetics concept evidence: **35**;
- incidental examples: **5**;
- dimensions per record: **29**;
- regression suite: **228 passed**.

The 0011–0033 batch adds 25 formal observations and 1 incidental example. Records 0011–0032 each carry one formal `knowledge.grammar.phonology` observation with no incidental examples.

Record 0033 is the first formal multi-dimension edge in this production stream:

- `knowledge.grammar.phonology` under `knowledge_technology`;
- `arts.music.formal_context` under `arts_music_performance`;
- `textual.tradition.reference` under `textual_intertextual_relationships`;
- incidental `people_social_roles` for `புலவர்`.

`நரம்பின் மறை` remains exact unresolved source wording for a scholarly/textual tradition: it is not promoted to body/health, religion/sectarian identity, or a resolved named historical work. `இசையிடன்` in 0013 and `இசைகள்` in 0025 remain phonological sound wording and are not classified as music/performance.

## Scaled cadence

Use **இயல்-aware sequential batches**:

- never cross an இயல் boundary;
- one batch when the remaining portion of an இயல் is ≤25 records;
- otherwise split inside that இயல் into contiguous chunks of at most 25 records;
- source-first semantic review remains one நூற்பா at a time.

Next planned batches:

- `0034–0058` — first 25 records of மொழி மரபு;
- `0059–0082` — remaining 24 records of மொழி மரபு;
- `0083–0103` — completes பிறப்பியல்.

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

Proceed with **Tolkāppiyam 0034–0058**, the first 25 records of மொழி மரபு. Review every நூற்பா sequentially across all 29 dimensions before consulting the old control crosswalk, stage one contiguous spec, materialize, validate, squash onto the previous green checkpoint and require full exact-head PR CI green.

**Do not start R2.**
