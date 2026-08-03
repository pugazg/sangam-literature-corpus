# Akanāṉūṟu architecture review

## Shared architecture generalisations

- Add an explicit fourth work profile; unknown work slugs continue to fail.
- Allow a source-printed macro-division section strategy alongside mechanical ranges and பத்து groups.
- Add generic manifest provenance for `poem_number_as_printed`, `source_order`, `major_division_as_printed`, and `source_object_id`.
- Extend recursive physical auditing without changing the frozen inventories of the first three works.
- Keep work manifests open-ended rather than assuming exactly three records.

## Akanāṉūṟu source-specific parser

- Parse the repeated table-cell record grammar in `pmuni0229`.
- Anchor records on number/body cells because malformed HTML makes record 174 a row inside the preceding table.
- Treat source order 1–400 as canonical record identity while retaining the duplicated printed labels at source-order records 131 and 319.
- Remove only numeric line-end layout cells and three embedded line-marker suffixes; preserve all literary strings otherwise.

## Akanāṉūṟu structural-output strategy

- Preserve the three printed macro-divisions as `001-120.md`, `121-300.md`, and `301-400.md`.
- Preserve printed record 0 in the work full text without fabricating `000.md`.
- Do not infer poem-level tiṇai, speaker/context, poet, or number-derived classifications.

## Source-set handling

`pmuni0229` is a single complete source-only object, so no multi-object implementation is required. The metadata nevertheless records a one-entry `source_objects` list using reusable provenance fields. Separate Project Madurai commentary editions are apparatus evidence only.

## Frozen-work protection

No frozen poem, source note, raw source, work metadata, section, or README is regenerated for this onboarding. Their hashes are compared with `logs/pre-akananuru-baseline-20260713T163825.json` after implementation.
