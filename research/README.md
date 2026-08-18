# Classical Tamil derived research layer

This directory contains independently versioned, reproducible derivatives of the frozen corpus.

## Version boundary

- R0 Puṟanāṉūṟu evidence schema: `0.1.0`.
- R1 review/entity-resolution workflow schema: `0.2.0`.
- R1.5 concept/observation schema: `0.3.0`.
- compatible frozen corpus: `classical-tamil-corpus-v1.1.0`.

R0 assertion IDs, spans, printed forms and source hashes remain the compatibility baseline. R1/R1.5 do not rewrite them.

## Current phase

R0 and R1 are complete. R1 is integrated into `main`.

R1.5 is current on PR #3. The PR remains open, draft and unmerged. R2 is blocked.

## Directory roles

- `schemas/` — evidence/workflow/concept schemas.
- `controlled-vocabularies/` — review, identity, classification-basis, dimension and evidence-policy vocabularies.
- `evidence/purananuru/` — authoritative deterministic R0 assertions.
- `mentions/purananuru/` — unresolved R0 literary-body candidates.
- `entities/pilot/` — surface-form entities plus append-only R1 decisions.
- `relationships/pilot/` — assertion-supported relationships.
- `reviews/purananuru/` — append-only review events plus deterministic queues/exports.
- `concepts/classical-tamil/` — R1.5 concept registry.
- `pilots/purananuru/` — bounded assertion-to-concept mapping contract.
- `observations/purananuru/` — deterministic R1.5 production pilot observations.
- `observations/tolkappiyam/` — separate grammatical/poetics concept-evidence contract; no production NDJSON in R1.5.
- `matrices/purananuru/` — deterministic production matrix views.
- `audits/r15-premerge/` — exhaustive semantic/matrix review ledgers and Tolkāppiyam crosswalk.
- `reports/` — deterministic coverage/review/pilot reports.

## Primary histories versus generated views

`reviews/purananuru/review-events.ndjson` and `entities/pilot/entity-resolution-decisions.ndjson` are primary append-only histories.

Generated R1 queues/reports and R1.5 pilot observations/matrices/summaries are deterministic views over declared primary inputs.

The exhaustive pre-merge audit ledgers are reviewed audit records, not automatic production concept observations.

## Review / identity semantics

`machine_checked` is not human verification. `reviewed` requires an explicit event. `verified` is a stronger explicit decision.

Assistant-assisted review does not establish a verified historical identity.

Printed-form or normalized-form equality never causes automatic merge. Concept membership is also separate from historical identity.

## Matrix semantics

A production matrix row retains evidence/provenance, classification basis, confidence and review state. It is not a yes/no historical fact flag.

Empty cells mean only that qualifying evidence is not currently recorded.

Conventional tiṇai/landscape associations are not hard-coded as source facts.

## Source terminology

Follow `docs/SOURCE_TERMINOLOGY_POLICY.md`. Preserve the exact Tamil term printed by the relevant source and keep later identity/equivalence claims in a separately classified evidence layer.

## Tolkāppiyam stream

Tolkāppiyam uses `GRAMMATICAL_CONCEPT_EVIDENCE` with `tolkappiyam_mapping` in a separate contract.

The exhaustive Tolkāppiyam audit covers all 1,602 நூற்பா and all 29 dimensions, but it does not bulk-populate production concept observations and never auto-classifies Sangam poems.

## Regeneration and validation

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

R2 may begin only after explicit user authorization to merge PR #3, successful merge, and fresh inspection of live `main`.
