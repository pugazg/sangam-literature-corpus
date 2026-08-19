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
- Puṟanāṉūṟu production: complete
- Tolkāppiyam production: permitted next, not yet started
- R2: blocked / not started

R1.5A keeps concept/observation schema `0.3.0`. It changes production-review cadence, not the evidence standard or phase schema.

## Current production state

The exact 29-dimension production vocabulary/schema remains aligned and validated.

Puṟanāṉūṟu production progress is the longest gap-free prefix under `research/production/purananuru/records/`.

Current materialized and validated state:

- records **001–400** form the complete gap-free Puṟanāṉūṟu production corpus;
- benchmark 001–002 and stabilization batch 003–010 are complete;
- regular 25-record semantic batches through 361–385 are complete;
- final 15-record batch **386–400** is complete;
- current validation: **400 reviewed / 0 remaining / 7,169 production observations / next record null / 224 tests passed**;
- canonical dimension count: **29**;
- Tolkāppiyam production observation count: **0**.

Normal PR verification workflow `32265906972` is green for the complete 001–400 production tree, including R0/R1/R1.5 validators, exact 29-dimension and production-prefix gates, deterministic regeneration, repository audit, Corpus/Tolkāppiyam non-drift and R1 primary-history preservation.

## Final Puṟanāṉūṟu publication method

Semantic review remained strictly poem-by-poem, sequential and source-first. The old sparse audit remained post-review control only.

The final 386–400 batch was fully reviewed across all 15 poems before the 351–400 control ledger was opened. Durable publication uses three compact specs:

- `386-390.json`
- `391-395.json`
- `396-400.json`

This changes only Git/materialization granularity. Split specs do not permit batch semantic guessing, skipped poems, audit-first classification or reduced provenance checking.

A construction-only malformed 391–395 serialization and temporary diagnostic workflow/log identified one missing closing brace. The corrected spec materialized normally; the workflow was restored and the log removed. Construction-only artifacts must not survive the final squash.

The core materializer expands already-reviewed decisions deterministically; it must not manufacture classifications. Existing R0 evidence may attach only to a dimension already selected by fresh review with exact source-text support inside selected evidence.

No new source-state driver rule was required for 386–400. Current unknown-poet literals remain:

- `பெயர் தெரிந்திலது`
- `பெயர் புலனாகவில்லை`
- `பாடப்பட்டோர் : பெயர்கள் தெரிந்தில`
- `, பாடப்பட்டோர், திணை, துறை தெரிந்தில`

The driver also suppresses and restores addressee `பெயர் தெரிந்திலது` during named-entity linking. These are source-state compatibility rules, not semantic classification or identity resolution.

## Important fidelity/provenance checks from 386–400

- 386 records narrow salt-pricing/exchange from `சிறுவெள் உப்பின் கொள்ளை சாற்றி` / `உமண்`; `வெள்ளி` remains source celestial/prognostic wording; `எந்தை` is not genealogy.
- 387 preserves tribute `பணிதிறை`, exact `பூழியர்`, unresolved `பொருநை`; tribute is not trade.
- 388 preserves drought/`வெள்ளி`, body `மருகன்` kinship wording and avoids deriving genealogy from poet-name `மகனார்`; `எந்தை` is not genealogy.
- 390 and 393 remain incomplete/lacunose and are not reconstructed.
- 391 preserves intimate/gender relationship wording without narrower legal-status inference.
- 392 preserves exact `அணங்குடை மரபு` without deity/sectarian/doctrinal mapping; printed addressee `மகன்` remains metadata kinship only.
- 394 treats elephant gifts as patronage, not market exchange; `தந்தை` is not genealogy.
- 395 preserves exact `உழவர்` and source-only `மகன்` / household-woman relation.
- 396 remains incomplete; exact `கோசர்`, `வேள்`, `ஒக்கல்`; moon/star comparison is praise imagery rather than an actual astronomical occurrence.
- 397 keeps canonical `பாடாண் / பரிசில் விடை`; source-note `கடைநிலை விடையும் ஆம்` is additional TT/TIR, not overwrite; exact `அறுதொழில் அந்தணர்` remains source-level without later caste/sectarian equivalence.
- 398 remains incomplete; tiger/serpent comparisons are imagery, not actual fauna occurrences.
- 399 preserves combined frozen thinai field `பாடாண் துறை: பரிசில் விடை`, exact `அறவர்`, `மறவர்`, `மள்ளர்`, `தொல்லோர்`, and `கடவுட்கும் தொடேன்` without deity identification; `விடுமீன் நொடுத்துக்` is narrow fish transaction only.
- 400 remains incomplete; lunar/calendrical wording is source-level; exact `வேள்வித் தூண்`, `மறவர்`; ships/river channels/ports are transport/infrastructure but not trade absent printed exchange.

Earlier source-terminology and provenance guardrails remain binding, including record 176, damaged record 200 and source-lost records 267–268.

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

Historical handovers, release snapshots, durable machine logs and the R1.5 pre-merge audit remain truthful records of their own boundaries and must not be rewritten merely to imitate current state. The old sparse ledgers are post-review control evidence, not the production matrix.

## Source terminology boundary

`docs/SOURCE_TERMINOLOGY_POLICY.md` remains mandatory.

Classical Tamil social, ritual, learned, occupational, political, kinship and community terms remain in the exact source-supported Tamil form. Do not silently map them to later caste, community, sectarian, hierarchy, deity, taxonomy or modern identity categories. Source metadata, body evidence and printed source-note evidence remain distinct. Null/blank canonical metadata remains null/blank. Printed names remain source mentions unless independently resolved. An explicit unknown-attribution phrase is metadata about non-identification, not itself an identity.

## Validation policy

The final Puṟanāṉūṟu R1.5A checkpoint must pass exact 29-dimension surface validation, complete Puṟanāṉūṟu production validation, R0/R1/R1.5 validators, full regression, deterministic R1/R1.5 regeneration, repository audit, Corpus/Tolkāppiyam non-drift, R1 primary-history preservation and documentation continuity.

A generated bot commit is not the final checkpoint. Finish on one user-authored/squashed head parented directly by the previous green checkpoint `bf7e0e168fd05476a99b0ee8615ddc324694924d` and validate that exact head.

## Phase hold / next stream

The Puṟanāṉūṟu production prerequisite is complete and validated. The next permitted R1.5A activity is to inspect and design the **separate Tolkāppiyam production pass** from the frozen 3 அதிகாரம் / 27 இயல் / 1,602 நூற்பா source and existing R1.5 crosswalk/control artifacts before producing the first benchmark records.

Tolkāppiyam evidence must never auto-classify Puṟanāṉūṟu or other Sangam poems. **Do not start R2.**
