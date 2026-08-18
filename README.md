# Sangam Literature Corpus

## Current repository state

This repository preserves a frozen Classical Tamil corpus and maintains independently versioned derived research layers above it.

Current preservation release: **Classical Tamil Corpus 1.1.0**.

- frozen works: 28
- canonical records: 7,234
- poem records: 5,632
- Tolkāppiyam நூற்பா: 1,602
- release identity: `classical-tamil-corpus-v1.1.0`

R1.5 — the exact 29-dimension Classical Tamil concept-matrix foundation — was explicitly authorized for merge and merged into `main` at `d82f9c78f27f9c9daf8fbb913d01ddfb29bddba1`.

**PR #3 is historical/merged.**

Current research work is **R1.5A — batched 29-dimension production review** on branch `research/classical-tamil-concept-matrix-r1.5a`.

R1.5A keeps concept/observation schema `0.3.0`; it changes production-review cadence, not the evidence standard. **R2 remains blocked and must not start without later explicit user authorization.**

Treat live GitHub branch/PR/check state as authoritative. Historical prompts, pre-merge handovers and old workflow logs remain provenance rather than current execution instructions.

## Research version boundary

- R0 evidence schema: `0.1.0`
- R1 review/entity-resolution workflow schema: `0.2.0`
- R1.5 / R1.5A concept-observation schema: `0.3.0`

Preserved R0 baseline:

- 2,867 source-grounded assertions
- 285 literary-body candidates
- 43 pilot surface-form entities
- 51 assertion-supported relationships

Preserved R1 baseline:

- 8 append-only review events
- 3 conservative entity-resolution decisions
- verified historical identities: 0

R1.5 established the versioned concept registry/evidence policies, exact 29-dimension vocabulary/schema, separate Tolkāppiyam grammatical/poetics evidence contract, exhaustive control audits, production-review schema/validator, and the first two validated Puṟanāṉūṟu production records.

## R1.5A production review

Canonical Puṟanāṉūṟu production records live at:

`research/production/purananuru/records/NNN.json`

At R1.5A start:

- 001 complete
- 002 complete
- 003 next

Every poem is still read sequentially and considered against all 29 dimensions. Each poem must have a complete individual production JSON in the working tree before the next poem is read.

Git publication is batched:

- stabilization batch: **003–010**
- then 25-record batches beginning **011–035**, **036–060**, **061–085**, and onward through 400
- full PR CI/non-drift runs once per published batch, not once per poem
- if interrupted, checkpoint the completed contiguous prefix

The older exhaustive audit is a post-review control artifact; it is never copied mechanically into production.

## Frozen preservation boundary

Corpus 1.1.0 is frozen. Research work does not alter canonical source text, source notes, source objects, apparatus evidence, release tags, or release fingerprints.

Raw/source evidence and derived research remain separate layers.

## Source and editorial hierarchy

1. raw source preservation;
2. source-faithful canonical transcription;
3. source-explicit metadata;
4. validation/anomaly reporting;
5. external textual comparison in separate apparatus;
6. derived research evidence;
7. separately classified external historical or interpretive claims.

Do not silently modernise, repair, reconstruct, infer missing text, merge editions, or turn a printed name into a verified historical identity.

## Tolkāppiyam boundary

Tolkāppiyam uses `work → அதிகாரம் → இயல் → நூற்பா` and canonical records under `corpus/tolkappiyam/nurpas/`.

Its grammatical/poetics evidence stream remains separate from Sangam literary-world observations. Tolkāppiyam must never auto-classify a Sangam poem.

Do not begin the Tolkāppiyam production pass until Puṟanāṉūṟu 001–400 is complete and validated.

## Commands

Core research validation includes:

```bash
python3 scripts/generate_research_layer.py --root .
python3 scripts/generate_research_r1.py --root .
python3 scripts/generate_research_r15.py --root .
python3 scripts/validate_research_layer.py --root .
python3 scripts/validate_research_r1.py --root .
python3 scripts/validate_research_r15.py --root .
python3 scripts/validate_research_r15_acceptance.py --root .
python3 scripts/validate_research_r15_dimensions.py --root .
python3 scripts/validate_r15_premerge_matrix_audit.py --root .
python3 scripts/validate_r15_purananuru_production.py --root .
pytest -q
python3 scripts/audit_repository.py --root .
```

The GitHub workflow additionally verifies deterministic regeneration, Corpus 1.1.0/Tolkāppiyam non-drift, and R1 primary-history preservation.

## Evidence-first matrix rule

Every populated production matrix value must have an evidence chain from the matrix state to the exact source field/span and frozen source provenance.

Reviewed-empty means only that no qualifying evidence was identified in that completed source record. It is not a historical absence claim.

## Source terminology

Read [`docs/SOURCE_TERMINOLOGY_POLICY.md`](docs/SOURCE_TERMINOLOGY_POLICY.md) before social, ritual, learned, occupational, political, kinship, or community classification.

Use the exact Tamil term printed by the relevant source. Do not silently replace a Classical Tamil source term with a later identity, hierarchy, sectarian, modern-community, or external-influence label.

## Key current documents

- [`PROJECT_HANDOVER.md`](PROJECT_HANDOVER.md) — authoritative continuity state.
- [`PROJECT_GUIDELINES.md`](PROJECT_GUIDELINES.md) — working rules.
- [`NEXT_CHAT_PROMPT.md`](NEXT_CHAT_PROMPT.md) — continuation contract.
- [`docs/DOCUMENTATION_STATUS.md`](docs/DOCUMENTATION_STATUS.md) — active/historical documentation boundary.
- [`docs/handover/r15a-production-review/README.md`](docs/handover/r15a-production-review/README.md) — R1.5A cadence contract.
- [`research/production/purananuru/README.md`](research/production/purananuru/README.md) — record ledger contract.
- [`docs/CLASSICAL_TAMIL_RESEARCH_MATRIX.md`](docs/CLASSICAL_TAMIL_RESEARCH_MATRIX.md) — matrix architecture.
- [`docs/classical-tamil-research-layer.md`](docs/classical-tamil-research-layer.md) — research evidence/version model.
- [`docs/SOURCE_TERMINOLOGY_POLICY.md`](docs/SOURCE_TERMINOLOGY_POLICY.md) — source-term rule.

`docs/handover/r15-premerge-audit/` remains historical/control methodology and evidence. Its old PR #3 merge-hold prose is not current operational authority.

## Rights / visibility

The repository remains private. `docs/source-rights-and-redistribution-review.md` retains unresolved redistribution questions. Do not change repository visibility without separate explicit user authorization.
