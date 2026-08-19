# Documentation status — R1.5A production review

## Purpose

This file defines current operational documentation after the authorized R1.5 merge and distinguishes it from historical/control material.

## Live phase state

- repository: `pugazg/sangam-literature-corpus`
- default branch: `main`
- R1.5 merge commit on `main`: `d82f9c78f27f9c9daf8fbb913d01ddfb29bddba1`
- PR #3: merged; historical R1.5 proposal
- active research branch: `research/classical-tamil-concept-matrix-r1.5a`
- active PR: #4, draft/unmerged R1.5A proposal
- current phase: R1.5A production review
- R2: blocked / not started

R1.5A keeps concept/observation schema `0.3.0`. It changes production-review cadence, not the evidence standard or phase schema.

## Current production state

The exact 29-dimension production vocabulary/schema remains aligned and validated.

Puṟanāṉūṟu production progress is the longest gap-free prefix under `research/production/purananuru/records/`.

Current materialized and validated state:

- records **001–310** form the gap-free production prefix;
- stabilization batch **003–010** is complete;
- regular 25-record batches through **286–310** are complete;
- next record: **311**;
- next planned batch: **311–335**;
- current validation: **310 reviewed / 90 remaining / 5,430 production observations / 224 tests passed**;
- canonical dimension count: **29**;
- Tolkāppiyam production observation count: **0**.

Records remain separate per-poem JSON files. The completed 286–310 review is staged in one contiguous spec: `research/production/purananuru/review-specs/286-310.json`.

## Low-latency publication method

The 261–285 and 286–310 batches prove that a complete 25-record batch can be staged as one contiguous reviewed spec and materialized in one workflow cycle. This is the preferred default when the entire batch can be completed in one session.

This optimization changes only Git/materialization granularity. Every poem must still be read sequentially and source-first, all 29 dimension decisions must be complete before moving to the next poem, and the old sparse audit remains post-review control only. Split specs remain valid when a session cannot finish a full batch or a source-state issue genuinely requires isolation.

After one-pass materialization, use targeted generated-record checks for source-loss, lacunae, metadata/body/source-note boundaries and substantive audit differences. Obtain the actual observation count from normal PR verification, update docs once, squash to one clean user-authored checkpoint and run exact-head final CI once.

Compact reviewed specs are source-first staging artifacts. The core materializer expands them deterministically but must not manufacture semantic classifications. Existing R0 evidence may only be attached to a dimension already selected by fresh review, with exact source-text support inside selected evidence.

The range-aware driver selects the proper 50-record audit-control part per record, including batches crossing an audit boundary. It preserves absent source-note states, blank canonical `thurai`, and exact unknown poet attribution literals while preventing those non-identification phrases from being treated as person/entity evidence.

Currently recognized exact unknown-poet literals:

- `பெயர் தெரிந்திலது`
- `பெயர் புலனாகவில்லை`

They are restored verbatim into `source_metadata_reviewed.poet_as_printed` after materialization. This is a source-state compatibility rule, not semantic classification.

## Important fidelity/provenance checks from 286–310

- record 287 preserves exact `புலைய` and `இழிசின` without later caste/community substitution;
- record 288 remains incomplete/lacunose and is not reconstructed;
- record 289 preserves null thinai/thurai while `திணை, துறை. தெரிந்தில.` is classification-uncertainty TIR;
- record 294 preserves `கூற்றுவினை` without later named-deity/doctrinal mapping;
- record 296 preserves `வேம்பு`, `காஞ்சி`, நெய் and `ஐயவி` smoke without later ritual/medical-system mapping;
- record 297 preserves `பாடினோர் பாடப்பட்டோன் : பெயர்கள் தெரிந்தில.` as unresolved attribution TIR and keeps `named_entities` reviewed-empty;
- record 298 has no source-note block and null thinai/thurai/poet/addressee metadata; these source states remain unchanged;
- record 299 preserves `அணங்குஉடை முருகன் கோட்டத்துக் / கலம்தொடா மகளிர்` literally and treats body `முருகன்` only as a source-explicit named sacred referent, without later doctrinal/temple/caste expansion;
- record 302 preserves alternate poet reading `காமக் கணியார் எனவும் பாடம்` as TIR;
- record 305 preserves exact `பார்ப்பான்` / `பார்ப்பன வாகை` without later caste/doctrinal substitution;
- record 306 remains incomplete/lacunose and preserves `நடுகல் கைதொழுது பரவும்` as memorial-stone honoring/worship and death-memory evidence;
- record 307 preserves exact `பெயர் புலனாகவில்லை`, keeps `named_entities` reviewed-empty, and records the unknown attribution as TIR.

Earlier source-terminology and provenance guardrails remain binding.

## Current operational documents

The current authority set is:

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
- `research/audits/r15-premerge/dimensions.json`
- `research/controlled-vocabularies/concept-dimensions-r15.json`
- `research/README.md`

## Historical / control documents

These remain truthful records and must not be rewritten merely to imitate current state:

1. `docs/history/` — superseded prompts and phase snapshots.
2. `docs/handover/r15-premerge-audit/` — R1.5 pre-merge audit/coverage/control methodology and results.
3. release documents — immutable release snapshots.
4. durable machine logs — records of the run/head they actually describe.
5. frozen corpus/work metadata and source notes — preservation evidence.

The R1.5 pre-merge sparse ledgers remain useful only as post-review control evidence. They are not the production matrix and must not be copied mechanically.

## Source terminology boundary

`docs/SOURCE_TERMINOLOGY_POLICY.md` remains mandatory.

Classical Tamil social, ritual, learned, occupational, political, kinship and community terms remain in the exact source-supported Tamil form. Do not silently map them to later caste, community, sectarian, hierarchy, deity, taxonomy or modern identity categories. Later equivalence claims require a separate evidence class and independent provenance.

Source metadata, poem-body evidence and printed source-note evidence remain distinct. Null/blank canonical metadata remains null/blank. Printed names remain source mentions unless independently resolved. An explicit unknown-attribution phrase is metadata about non-identification, not itself an identity.

## Validation policy

R1.5A final batch checkpoints must pass:

- exact 29-dimension surface validation;
- Puṟanāṉūṟu production-prefix validation;
- R0/R1/R1.5 validators;
- full regression;
- deterministic R1 and R1.5 regeneration checks;
- repository audit;
- Corpus 1.1.0/Tolkāppiyam non-drift;
- R1 primary-history preservation;
- documentation continuity.

A generated bot commit is not the final checkpoint. Finish on one user-authored/squashed head parented by the previous green checkpoint and validate that exact head.

## Phase hold

R1.5A remains active. Continue Puṟanāṉūṟu sequentially from **311**; the next permitted batch is **311–335**. Prefer one contiguous 25-record reviewed spec and one materialization cycle when the whole batch can be completed in-session. Do not start the Tolkāppiyam production pass until Puṟanāṉūṟu 001–400 is complete and validated. **Do not start R2.**
