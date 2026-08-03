# நற்றிணை (Naṟṟiṇai)

Corpus schema version: **1.0.0**

Version status: **frozen**.

## Naṟṟiṇai source

This directory is the source-faithful canonical transcription of Naṟṟiṇai selected from Project Madurai. It contains no translation, literary interpretation, reconstructed completion, or inferred speaker classification.

## Project Madurai identifier and source URL

- Project Madurai identifier: `pmuni0296`
- Source URL: https://www.projectmadurai.org/pm_etexts/utf8/pmuni0296.html
- Raw HTML: `sources/raw-html/natrinai.html`
- Raw checksum and access date: `metadata.json` and `sources/source-metadata/natrinai.json`

## Poem count

- Printed numbered records: 400
- Markdown poem files: 400 (`001.md` through `400.md`)
- Canonical literary text available: 399
- Source-lost canonical text: poem 234
- Textually incomplete canonical text: poem 385

The unnumbered `கடவுள் வாழ்த்து` is retained in `full-text.md` rather than assigned poem number zero.

## Known textual conditions

Known source conditions are represented in YAML, manifests, validation issues, and the separate editorial apparatus. They are never silently repaired.

## Poem 234

Project Madurai states that the accepted original text is lost and prints two conjectural candidates. Therefore poem 234 has `textual_status: lost`, no canonical body, successful extraction status, and both candidates retained exclusively under `Source note (as printed)`. TamilVU's selection of one candidate and its `குறிஞ்சி` classification exist only in `apparatus/natrinai/`.

## Poem 385

Project Madurai prints an incomplete poem ending in dash placeholders. It has `textual_status: incomplete`, an ending lacuna, and successful extraction. All printed lines and dashes remain unchanged; no completion is reconstructed.

## Shared first lines

The distinct pairs 7/268, 15/203, 153/346, and 205/399 share their opening line but have different normalized full bodies. TamilVU independently confirms these as separate numbered poems. Validation records them as informational `shared_first_line` findings, never duplicate-body warnings.

## Parser assumptions

- Only observed headings numbered 1–400 open poem records.
- Both `125.குறிஞ்சி` and the normal spaced form are recognized without renumbering.
- Tiṇai and poet are copied from Project Madurai headings.
- `(?)` is retained through `poet_as_printed`, while canonical `poet` is null.
- Printed prose notes are preserved but are not mapped to controlled speaker labels.
- Candidate material following poem 234 is source-note material, not canonical poem text.
- HTML entities, line endings, blank-line noise, and Unicode NFC are handled only under the repository's permitted transformation policy.

## Section generation

Eight navigation files cover mechanical ranges of 50 poem numbers: 001–050 through 351–400. They are organizational aids and do not claim source-defined literary divisions.

## Metadata provenance

Every poem carries field-level provenance for tiṇai, poet, speaker, and source note. Null values are meaningful. External evidence cannot replace Project Madurai metadata or canonical lines.

## Validation status

Acceptance requires 400 exact filenames, hardened-schema coverage for all files, source-body and source-note fidelity for all 400 records, no duplicate full bodies, no integrity errors, and review of the known poem-234 warning and informational findings.

## External evidence policy

TamilVU comparisons are layer 5 evidence stored under `apparatus/natrinai/`. They cannot modify `corpus/natrinai/`. Reviewed speaker mapping and literary/historical analysis remain disabled layers 6 and 7.
