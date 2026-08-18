# R1.5A Production Review — Handover and Cadence Contract

## Why R1.5A exists

R1.5 established and validated the exact 29-dimension research foundation, then was explicitly authorized for merge and merged into `main` at `d82f9c78f27f9c9daf8fbb913d01ddfb29bddba1`.

The first two Puṟanāṉūṟu production records demonstrated that a one-poem → one-commit → full-CI cadence is unnecessarily slow. R1.5A preserves the same scholarly/evidence standard while changing only the working and publication cadence.

R1.5A is not R2 and does not change schema version `0.3.0`.

## Production state at phase start

- exact 29-dimension production vocabulary/schema: aligned and validated;
- production validator: present;
- production record schema: present;
- Puṟanāṉūṟu 001: complete/validated;
- Puṟanāṉūṟu 002: complete/validated;
- Puṟanāṉūṟu 003: next record;
- old exhaustive 400-record sparse audit: control artifact only;
- Tolkāppiyam production review: not started and blocked until Puṟanāṉūṟu completion.

## Non-negotiable record rule

Records are still reviewed one at a time in canonical order.

Before reading the next poem, the current poem must have a complete individual production JSON in the working tree that records all 29 dimension-review states and all qualifying evidence observations.

A later batch commit is only a Git publication boundary; it is not a semantic-review boundary.

## Cadence

### Stabilization batch

Review and publish **003–010** together.

Purpose: prove the faster batching mechanism and confirm that the schema/validator remains comfortable across several consecutive records.

### Regular batches

After 003–010 is green, use 25-record batches:

- 011–035
- 036–060
- 061–085
- 086–110
- 111–135
- 136–160
- 161–185
- 186–210
- 211–235
- 236–260
- 261–285
- 286–310
- 311–335
- 336–360
- 361–385
- 386–400

Do not skip order to make a batch convenient.

If work is interrupted before the planned boundary, publish/checkpoint the completed contiguous prefix rather than losing reviewed records.

## Per-record sequence

For record `NNN`:

1. read the full canonical poem file and all source-explicit metadata;
2. inspect its R0 assertion snapshot;
3. perform a fresh semantic review against all exact 29 dimensions;
4. preserve ambiguity and distinguish metadata evidence from body evidence;
5. use exact Tamil evidence and exact source spans;
6. link only genuine existing R0 assertions;
7. use `direct_record_review` where source-supported evidence has no appropriate prior assertion;
8. create the complete `NNN.json` in the working tree;
9. only then inspect the old sparse audit row and record control agreement/discrepancy;
10. validate the completed record sufficiently to catch schema/span/provenance errors before reading `NNN+1`.

## Batch publication sequence

At a completed batch boundary:

1. validate the contiguous production prefix;
2. publish all newly completed per-record JSON files in one deterministic multi-file commit;
3. update only genuinely current progress/continuity metadata if needed;
4. run the full PR workflow once for the batch;
5. do not begin the next batch if the published batch has a substantive validation failure.

This removes repeated commit/CI overhead while preserving source-by-source scholarly accountability.

## Control-audit rule

The old sparse audit is never the starting point for a production record.

Fresh source review comes first. The audit is opened only after fresh review completion and may be used to identify:

- agreement;
- production additions supported by exact source evidence;
- control-only dimensions not accepted into production;
- changed confidence/interpretive boundary.

Every discrepancy must remain explainable from the source, not from a desire to match the old ledger.

## Source terminology

`docs/SOURCE_TERMINOLOGY_POLICY.md` remains binding. Preserve the exact Tamil source term and do not silently substitute later identities or equivalences.

## Special source conditions

- Puṟanāṉūṟu 200: preserve damage/lacuna without reconstruction.
- Puṟanāṉūṟu 267–268: preserve source-lost/unreconstructed condition.
- source-printed names are mentions, not automatically verified historical identities.

## Validation checkpoint

Each batch must pass the current workflow, including the explicit exact-29-dimension and Puṟanāṉūṟu production-prefix validators, full regression, deterministic checks, repository audit, frozen-corpus/Tolkāppiyam non-drift, and R1 history preservation.

## Next action

Continue record 003, then 004 through 010 sequentially. Publish 003–010 as the first R1.5A production batch and validate it before starting 011–035.

R2 remains blocked.
