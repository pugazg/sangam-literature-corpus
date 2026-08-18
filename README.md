# Sangam Literature Corpus

## Current repository state

This repository preserves a frozen Classical Tamil corpus and maintains independently versioned derived research layers above it.

Current preservation release: **Classical Tamil Corpus 1.1.0**.

- frozen works: 28
- canonical records: 7,234
- poem records: 5,632
- Tolkāppiyam நூற்பா: 1,602
- release identity: `classical-tamil-corpus-v1.1.0`

Current research work is **R1.5 — Classical Tamil Concept Matrix Foundation** on branch `research/classical-tamil-concept-matrix-r1.5`, proposed to `main` through PR #3.

**PR #3 must remain open, draft, and unmerged until the user explicitly authorizes a merge. R2 has not started and must not start before that authorization and a fresh inspection of live `main`.**

The live PR and branch state are authoritative for current workflow/check status. Do not copy old workflow IDs into new continuity prose and treat them as permanent status.

## Research version boundary

- R0 evidence schema: `0.1.0`
- R1 review/entity-resolution workflow schema: `0.2.0`
- R1.5 concept/observation schema: `0.3.0`

R0 remains 2,867 source-grounded assertions, 285 literary-body candidates, 43 pilot surface-form entities, and 51 assertion-supported relationships. R1 adds 8 append-only review events and 3 conservative entity-resolution decisions, with no verified historical identity. R1.5 adds a versioned concept registry, evidence policies, a bounded 8-observation Puṟanāṉūṟu pilot, and the exhaustive pre-merge matrix audit.

The exhaustive R1.5 audit reviewed:

- Puṟanāṉūṟu: 400 / 400 records × 29 research dimensions;
- Tolkāppiyam: 1,602 / 1,602 நூற்பா across 27 இயல் × the same 29 dimensions;
- automatic Tolkāppiyam → Sangam poem classification: disabled.

The audit ledger is review evidence, not a corpus rewrite and not an automatic production observation set.

## Preservation and research separation

The governing architecture is:

```text
frozen source corpus
    ↓
source-grounded assertions
    ↓
review events / ambiguity handling
    ↓
concept classification and entity resolution
    ↓
relationships and analytical datasets
    ↓
research matrices / later visualisation
```

Frozen `corpus/`, `sources/`, and source apparatus must not be edited merely to make research output easier or cleaner.

A matrix cell is a derived evidence view, never an unsupported historical boolean. Empty cells mean only that qualifying evidence is not currently recorded.

## Source terminology

Read [`docs/SOURCE_TERMINOLOGY_POLICY.md`](docs/SOURCE_TERMINOLOGY_POLICY.md) before social, ritual, learned, occupational, political, kinship, or community classification.

Use the exact Tamil term printed by the relevant source, for example `அந்தணர்`, `அரசர்`, `பாணர்`, or another source-supported form. Do not silently replace a Classical Tamil source term with a later caste, sectarian, modern-community, hierarchy, or external-influence identity.

## Key current documents

- [`PROJECT_HANDOVER.md`](PROJECT_HANDOVER.md) — authoritative current continuity state.
- [`PROJECT_GUIDELINES.md`](PROJECT_GUIDELINES.md) — working rules.
- [`NEXT_CHAT_PROMPT.md`](NEXT_CHAT_PROMPT.md) — safe continuation contract.
- [`docs/DOCUMENTATION_STATUS.md`](docs/DOCUMENTATION_STATUS.md) — documentation audit classification.
- [`docs/CLASSICAL_TAMIL_RESEARCH_MATRIX.md`](docs/CLASSICAL_TAMIL_RESEARCH_MATRIX.md) — matrix architecture and roadmap.
- [`docs/classical-tamil-research-layer.md`](docs/classical-tamil-research-layer.md) — research-layer version/evidence model.
- [`docs/SOURCE_TERMINOLOGY_POLICY.md`](docs/SOURCE_TERMINOLOGY_POLICY.md) — source-term rule.
- [`docs/handover/r15-premerge-audit/README.md`](docs/handover/r15-premerge-audit/README.md) — R1.5 exhaustive-audit continuity.

Files under `docs/history/` are historical snapshots and must not be used as current instructions. Release documents for 1.0.0 and 1.1.0 are immutable release records, not phase-status documents.

## Validation

The research PR workflow runs the R0/R1/R1.5 generators and validators, the exhaustive matrix validator, complete regression tests, deterministic-regeneration checks, repository audit, Corpus 1.1.0/Tolkāppiyam non-drift checks, and R1 primary-history non-mutation checks.

Core local equivalents include:

```bash
python3 scripts/generate_research_layer.py --root .
python3 scripts/generate_research_r1.py --root .
python3 scripts/generate_research_r15.py --root .
python3 scripts/validate_research_layer.py --root .
python3 scripts/validate_research_r1.py --root .
python3 scripts/validate_research_r15.py --root .
python3 scripts/validate_research_r15_acceptance.py --root .
python3 scripts/validate_r15_premerge_matrix_audit.py --root .
pytest -q
python3 scripts/audit_repository.py --root .
```

## Rights / visibility

The repository is private. `docs/source-rights-and-redistribution-review.md` retains unresolved redistribution questions. Do not change repository visibility without a separate explicit user decision after that review.
