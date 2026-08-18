# Puṟanāṉūṟu R1.5 production review ledger

This directory is the durable record-by-record production layer for the strengthened **R1.5** 29-dimension review.

## Hard boundaries

- This is R1.5 work. It is not R2.
- PR #3 remains open, draft, and unmerged until explicit user authorization.
- `corpus/purananuru/` is frozen source material and is never edited by this review.
- The earlier sparse audit under `research/audits/r15-premerge/purananuru/` is a coverage/control artifact, not the production observation dataset.
- The Tolkāppiyam production pass must not begin until all 400 Puṟanāṉūṟu records are complete and validated.

## Canonical ledger

Each reviewed poem is stored as one file under:

`research/production/purananuru/records/NNN.json`

The files themselves are the canonical record-level ledger. Progress is the longest gap-free prefix beginning at `001`; do not use prose status as the authoritative progress counter.

Before record `NNN+1` is read, record `NNN.json` must already contain a durable completed review state.

Every record must:

1. identify the exact frozen canonical record and R0 assertion snapshot;
2. consider the exact 29 canonical dimensions in registry order;
3. distinguish qualifying evidence from reviewed-empty dimensions;
4. retain exact source Tamil and body-relative line/character spans for body evidence;
5. retain real R0 assertion IDs where an existing assertion supports the production observation;
6. mark genuinely new semantic evidence as `direct_r15_source_review_no_prior_assertion` rather than inventing an R0 assertion;
7. preserve source metadata/body provenance distinctions;
8. keep printed names as source mentions unless separately resolved through permitted external evidence;
9. preserve damaged/source-lost states without reconstruction;
10. compare against the old sparse audit only **after** the fresh source review is complete.

## Evidence spans

For `canonical_body` evidence, `evidence_span.start_line` and `end_line` are **1-based poem-body line numbers**, not whole-file line numbers. Character offsets are 0-based Python/Unicode string positions within the first/last cited body line. `source_text` must reproduce the cited frozen source slice exactly.

Metadata evidence uses its exact YAML field/source location and may have a null body span.

## Empty-cell semantics

`no_qualifying_evidence_identified` means only that the completed review found no qualifying evidence for that dimension in that source record. It never asserts historical absence.

## Source terminology

`docs/SOURCE_TERMINOLOGY_POLICY.md` governs this ledger. Exact printed Tamil terms are preserved. They are not silently replaced with later caste, sectarian, hierarchical, modern-community, geographic, or external-influence identities.

## Validation

Run:

```bash
python3 scripts/validate_r15_purananuru_production.py --root .
pytest -q
```

The validator checks sequential prefix completion, the exact ordered 29-dimension surface, canonical source hashes, source-span fidelity, real R0 assertion linkage, deterministic production observation IDs, concept/dimension compatibility where a stable concept exists, and post-review audit-control consistency.
