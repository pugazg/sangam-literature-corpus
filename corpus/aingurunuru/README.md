# ஐங்குறு நூறு (Aiṅkuṟunūṟu)

Corpus schema version: **1.0.0**

Freeze status: **formally frozen** after complete physical, fidelity, structural, and Naṟṟiṇai regression verification.

## Source

The canonical transcription source is Project Madurai `pmuni0028`: https://www.projectmadurai.org/pm_etexts/utf8/pmuni0028.html. The response bytes are preserved at `sources/raw-html/aingurunuru.html`; SHA-256 is `b1bbdbe90472ef28b617d32a7b8893b1f894f49afd9b4574e11501bd13e75ac9`.

## Attribution statements

The source prints `aingurunUru`, describes the work as one of the `eTTutokai`, and states “500 short poems (two are missing).” It attributes compilation to கூடலூர் கிழார், at the instance of Chera king யானைக்கட்சேய் மாந்தரஞ்சேரல் இரும்பொறை, and separately credits the electronic text compilation to வித்துவான் எம். நாராயண வேலுப்பிள்ளை. Ancient and electronic-text roles are distinct metadata fields, with printed forms retained.

## Poem inventory and textual conditions

There are exactly 500 canonical records and files, numbered 001–500. Project Madurai explicitly prints poems 129 and 130 as `கிடைக்காத பாடல்`; both are successful `lost` records with empty canonical bodies and the printed statement retained as a source note. Thus 498 records have canonical literary text.

The source prints poem 470's number without a full stop. The parser recognizes that exact heading form without altering the literary lines or printed source. No other source-lost poem was found.

## Structural hierarchy and named பத்து groups

Each poem belongs mechanically to exactly one source-order ten-poem group. Forty-eight of the 50 groups have printed பத்து headings. The source prints no heading before poems 1 or 11. It repeats ordinal `11` before poem 111 and prints ordinal `12` before poem 121; source order and printed ordinals are stored separately, and the discrepancies remain informational issues. The complete ordered inventory, ranges, counts, lost members, and printed forms are in `pattu-inventory.json`.

The source does not print major-division or tiṇai headings. The corpus therefore uses five neutral hundred-poem navigation blocks (`001-100` through `401-500`) and does not assign conventional tiṇai names. `major_division_as_printed` and poem `thinai` remain null.

## Parser assumptions

- A numbered line opens a poem; poem 470's bare numeric line is an observed exception.
- A short line ending in `பத்து`, optionally preceded by a printed ordinal, applies to the following ten-poem group.
- Group membership follows poem number and is checked against ten records; it is never repaired to fit a heading.
- Printed heading whitespace, punctuation, spellings, and ordinal errors are preserved in `pattu_as_printed`.
- Only entity decoding, NFC, LF normalization, blank-line cleanup, and Markdown structure affect derived output.
- Poet and speaker are null because the source does not print poem-level attributions for them.

## Metadata provenance

Structural provenance distinguishes printed headings from mechanical navigation. Work metadata separates ancient compiler, royal instance, and modern electronic-text compiler. Null values are deliberate and are preferable to external inference.

## Validation status

Acceptance requires 500 exact poem filenames, 50 exact ten-poem section files, 500/500 body and source-note fidelity, no missing or duplicate numbers, no duplicate normalized full bodies, exactly one group membership per poem, and zero errors. The two source-lost poems are warnings; shared openings and printed heading anomalies are informational.

## External evidence policy

External comparisons belong only under `apparatus/aingurunuru/`. They cannot add readings, tiṇai names, speakers, poets, or reconstructed text to this canonical Project Madurai corpus.
