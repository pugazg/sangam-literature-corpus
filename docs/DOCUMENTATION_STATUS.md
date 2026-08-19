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
- Tolkāppiyam production: active; benchmark accepted
- R2: blocked / not started

R1.5A keeps schema `0.3.0` and the same exact 29 dimensions.

## Puṟanāṉūṟu completed state

Puṟanāṉūṟu `001–400` is the complete, validated, gap-free production corpus.

Durable cadence history remains:

- benchmark `001–002`;
- stabilization `003–010`;
- regular 25-record batches from `011–035` through `361–385`;
- final `386–400`.

Definitive Puṟanāṉūṟu completion checkpoint:

- SHA `491fa3107984b29f1dbb747bc7483e0cb694ab91`;
- 400 reviewed / 0 remaining;
- 7,169 production observations;
- 29 dimensions;
- 224 tests at that completion boundary;
- exact-head workflow `32267324444` green.

## Tolkāppiyam production contract

Tolkāppiyam is a separate grammatical/poetics evidence stream over the frozen hierarchy:

`3 அதிகாரம் / 27 இயல் / 1,602 நூற்பா`

Canonical IDs are `tolkappiyam-0001` through `tolkappiyam-1602`, ordered by source sequence.

Per-நூற்பா production review distinguishes:

- formal grammatical/poetics concept evidence;
- incidental examples;
- no qualifying evidence identified.

Only formal evidence enters `research/observations/tolkappiyam/r15-production.ndjson` as `GRAMMATICAL_CONCEPT_EVIDENCE` with classification basis `tolkappiyam_mapping`. Incidental examples remain inside the record and never become automatic historical/lived-life claims.

Primary durable implementation:

- `research/production/tolkappiyam/README.md`
- `research/production/tolkappiyam/review-specs/`
- `research/production/tolkappiyam/records/`
- `research/observations/tolkappiyam/r15-production.ndjson`
- `research/schemas/tolkappiyam-production-review-r15.schema.json`
- `research/concepts/classical-tamil/tolkappiyam-production-concepts-r15a.json`
- `scripts/materialize_r15a_tolkappiyam_batch.py`
- `scripts/validate_r15_tolkappiyam_production.py`
- `.github/workflows/materialize-r15a-tolkappiyam-batch.yml`

The old Tolkāppiyam review manifest/crosswalk remains coverage/control evidence only. It is representative formal support, not an exhaustive occurrence index and not a classifier.

## Accepted Tolkāppiyam benchmark

Benchmark `0001–0002` is materialized and validated.

Authoritative benchmark state from workflow `32270636581`:

- records reviewed: **2 / 1,602**;
- records remaining: **1,600**;
- next record: **tolkappiyam-0003**;
- grammatical concept evidence: **2**;
- incidental examples: **0**;
- canonical dimensions: **29**;
- regression suite: **228 passed**;
- Puṟanāṉūṟu production validator: pass;
- Tolkāppiyam production validator: pass;
- R0/R1/R1.5 validators: pass;
- deterministic R1/R1.5 regeneration: pass;
- repository audit: pass;
- Corpus/Tolkāppiyam non-drift: pass;
- R1 primary histories preserved.

Both benchmark records have formal evidence only in `knowledge_technology`, using stream-specific controlled concept `knowledge.grammar.phonology`. No incidental examples are recorded.

The R1.5 acceptance invariant now permits Tolkāppiyam production only when Puṟanāṉūṟu 001–400 production is complete. The original bounded R1.5 pilot remains preserved.

The R1.5 baseline metric counts actual Tolkāppiyam observation rows, not NDJSON files.

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

Historical handovers/audits remain truthful records of their own boundaries and should not be rewritten merely to imitate current state.

## Next activity

Proceed with **Tolkāppiyam 0003–0010 stabilization** using the accepted formal/incidental/empty evidence contract.

Review each நூற்பா sequentially across all 29 dimensions before using the old crosswalk as control context. Stage one contiguous stabilization spec after all eight source-first decisions are fixed, then materialize, validate and run full PR CI.

Do not choose the long-run batch cadence until stabilization is green. Prefer இயல்-aware batches after stabilization.

**Do not start R2.**
