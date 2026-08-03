# குறுந்தொகை (Kuruntokai)

Corpus schema version: **1.0.0**

Version status: **formally frozen** after physical, schema, fidelity, regeneration-stability, and frozen-work regression verification.

The freeze fixes the Project Madurai source identity and checksum, numbered inventory, canonical bodies, provenance and textual-status representation, printed tiṇai/context/poet strings and anomalies, mechanical navigation strategy, and validation expectations. It does not claim that Project Madurai is a critical edition or that its printed anomalies are philologically correct.

## Canonical source

Project Madurai `pmuni0110`, https://www.projectmadurai.org/pm_etexts/utf8/pmuni0110.html. The unchanged raw response is preserved under `sources/raw-html/kuruntokai.html`; provenance and checksum are recorded in `metadata.json`.

## Printed structure

The source contains an unnumbered `கடவுள் வாழ்த்து` followed by 401 consecutively numbered poems. Each heading prints poem number, tiṇai, and speaker/context. A poet attribution follows each poem. No anthology section divisions are printed.

## Navigation sections

Nine generated files cover mechanical fifty-poem ranges, ending with `401-401.md`. They are navigation aids only and are not represented as source-printed or ancient divisions.

## Source anomalies

- Poem 29 prints `தலைன் கூற்று`.
- Poem 396 prints `பாால`.
- Ten poet attributions are printed only as dot placeholders and remain null structured values with their printed forms preserved.
- Poems 105 and 180 place the attribution on the same HTML line as the final verse; the parser restores only that layout boundary.
- Two pairs share first lines: 104/287 and 246/313. Their full bodies differ.

No source-lost poem, literary lacuna, conjectural candidate text, missing number, duplicate number, or identical normalized full body was detected.

## Editorial policy

Printed tiṇai and context strings are preserved without correction. They are not inferred from external scholarship. External comparisons belong only under `apparatus/kuruntokai/` and cannot alter this canonical transcription.
