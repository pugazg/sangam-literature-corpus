# Classical Tamil Research Layer

## Purpose

The research layer is a derived, reproducible programme above the immutable Classical Tamil Corpus. It never edits canonical transcription, raw-source preservation, or frozen apparatus merely to improve research output.

## Version boundary

- R0 evidence schema: `0.1.0`
- R1 review/entity-resolution workflow schema: `0.2.0`
- R1.5 concept/observation schema: `0.3.0`
- compatible frozen corpus: Classical Tamil Corpus `1.1.0`

R0 evidence was originally generated against Corpus 1.0.0 and reconciled onto 1.1.0 without changing assertion identity or Puṟanāṉūṟu source evidence.

## Current phase state

R0 and R1 are complete. R1 is merged into `main`.

R1.5 is current on `research/classical-tamil-concept-matrix-r1.5` in PR #3. The PR remains **open, draft, and unmerged**. R2 is blocked and has not started.

## Architecture

```text
frozen corpus
→ deterministic source assertions
→ append-only review events
→ concept classification / entity resolution
→ assertion-supported relationships
→ deterministic matrices/reports
→ later interpretation and visualisation
```

## Evidence, review and identity

Evidence class, confidence, review status, identity status, and concept membership are independent.

`SOURCE_EXPLICIT` states what a source supports. It does not by itself prove a modern historical identification.

`machine_checked` is not human verification. `reviewed` requires an explicit review event. `verified` requires a stronger explicit decision.

Assistant-assisted review is recorded as `assistant_assisted` and does not independently establish biography, dynasty, modern geography, chronology, taxonomy, or historical co-reference.

`possible_match` remains weaker than verified identity. Exact or normalized string equality never causes an automatic merge.

## R0 preserved evidence

Puṟanāṉūṟu R0 remains:

- 400 canonical records processed;
- 398 available literary bodies;
- source-lost records 267–268;
- 2,867 assertions;
- 285 literary-body candidates;
- 43 pilot surface-form entities;
- 51 relationships;
- 0 external-historical assertions;
- 0 interpretive assertions.

## R1 primary histories

Primary append-only histories:

- `research/reviews/purananuru/review-events.ndjson`
- `research/entities/pilot/entity-resolution-decisions.ndjson`

R1 contains 8 review events and 3 conservative entity decisions. No verified historical identity is created.

Deterministic derived R1 views include the review queue, reviewed export, summaries, ambiguity register, and unresolved-entity report.

## R1.5 concept layer

R1.5 adds:

- versioned concept registry;
- classification-basis vocabulary;
- evidence-policy vocabulary;
- concept-observation schema;
- separate Tolkāppiyam grammatical/poetics concept-evidence schema;
- bounded Puṟanāṉūṟu mapping/generator;
- deterministic matrix and summary views;
- acceptance and orphan-reference validation.

The bounded production pilot contains 8 source-explicit reviewed observations across 6 Puṟanāṉūṟu records and 7 concepts/dimensions. No external-historical or interpretive production observation is populated.

## Exhaustive R1.5 audit

The pre-merge audit extends semantic review coverage beyond the bounded production pilot:

- Puṟanāṉūṟu: 400 / 400 records × 29 dimensions;
- Tolkāppiyam: 1,602 / 1,602 நூற்பா across 27 இயல் × 29 dimensions.

Puṟanāṉūṟu audit data is sparse: omitted dimensions mean only that qualifying evidence was not recorded in that review pass.

Tolkāppiyam audit distinguishes grammatical concept evidence from incidental examples and no qualifying evidence. The 29-dimension crosswalk is not an automatic poem classifier.

Audit ledgers are review evidence and do not automatically become production concept observations.

## Source terminology

Research text follows `docs/SOURCE_TERMINOLOGY_POLICY.md`.

Use the exact Tamil source form for social, ritual, learned, occupational, political, kinship, and community terms. Later identity/equivalence claims must remain separate external-evidence or interpretive assertions.

## Matrix semantics

A production matrix row is a deterministic view over provenance-bearing observations, not a yes/no historical fact flag.

Every populated production value must retain concept, work/record, exact source form/span, evidence class, classification basis, confidence/review state, and supporting assertion IDs.

Empty cells are not historical absence claims.

## Generation and validation

```bash
python3 scripts/generate_research_layer.py --root .
python3 scripts/generate_research_r1.py --root .
python3 scripts/generate_research_r15.py --root .
python3 scripts/validate_research_layer.py --root .
python3 scripts/validate_research_r1.py --root .
python3 scripts/validate_research_r15.py --root .
python3 scripts/validate_research_r15_acceptance.py --root .
python3 scripts/validate_r15_premerge_matrix_audit.py --root .
python3 scripts/verify_research_r1_idempotence.py --root .
python3 scripts/verify_research_r15_idempotence.py --root .
pytest -q
python3 scripts/audit_repository.py --root .
```

CI also proves Corpus 1.1.0/Tolkāppiyam non-drift and R1 primary-history non-mutation.

## Next phase gate

R2 may be considered only after the user explicitly authorizes merge of PR #3, the merge succeeds, and live `main` is freshly inspected.

Green CI alone is not merge authorization.
