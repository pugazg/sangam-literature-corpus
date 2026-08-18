# Puṟanāṉūṟu R1.5A production review ledger

This directory is the durable record-by-record production layer built on the merged R1.5 exact 29-dimension foundation.

## Hard boundaries

- Current phase: R1.5A. It is not R2.
- R1.5 merged into `main` at `d82f9c78f27f9c9daf8fbb913d01ddfb29bddba1`.
- `corpus/purananuru/` is frozen source material and is never edited by this review.
- The earlier sparse audit under `research/audits/r15-premerge/purananuru/` is a coverage/control artifact, not the production observation dataset.
- The Tolkāppiyam production pass must not begin until all 400 Puṟanāṉūṟu records are complete and validated.
- `docs/SOURCE_TERMINOLOGY_POLICY.md` is mandatory.

## Canonical ledger

Each reviewed poem is stored as one file under:

`research/production/purananuru/records/NNN.json`

The files are the canonical record-level ledger. Progress is the longest gap-free prefix beginning at `001`; prose status is not the authoritative progress counter.

Before record `NNN+1` is read, the complete `NNN.json` must already exist in the working tree with its completed 29-dimension review state. Git commits may batch several already-completed record files.

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
10. compare against the old sparse audit only after the fresh source review is complete.

## R1.5A cadence

The review is sequential; repository publication is batched.

- benchmark already complete: 001–002;
- stabilization batch: 003–010;
- regular cadence: 25-record batches beginning 011–035, then 036–060, 061–085, and so on;
- final batch ends exactly at 400;
- one deterministic multi-file Git commit per completed batch;
- full PR CI/non-drift once per published batch, not once per poem;
- if the active work session cannot complete a planned batch, checkpoint the completed contiguous prefix.

This cadence must never be used to skip sequential semantic review or to copy the control ledger into production.

## Evidence spans

For `canonical_body` evidence, `evidence_span.start_line` and `end_line` are 1-based poem-body line numbers. Character offsets are 0-based Unicode string positions within the cited body lines. `source_text` must reproduce the frozen source slice exactly.

Metadata evidence uses its exact YAML field/source location and may have a null body span.

## Empty-cell semantics

`no_qualifying_evidence_identified` means only that the completed review found no qualifying evidence for that dimension in that source record. It never asserts historical absence.

## Validation

At each batch checkpoint run:

```bash
python3 scripts/validate_research_r15_dimensions.py --root .
python3 scripts/validate_r15_purananuru_production.py --root .
pytest -q
```

The full PR workflow additionally covers deterministic regeneration, repository audit, Corpus 1.1.0/Tolkāppiyam non-drift, R1 history preservation, and documentation continuity.
