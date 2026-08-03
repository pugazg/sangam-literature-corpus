# Paripāṭal / பரிபாடல்

Status: formally frozen. Corpus schema version: **1.0.0**.

## Canonical source

The canonical transcription source is Project Madurai `pmuni0087`,
`https://www.projectmadurai.org/pm_etexts/utf8/pmuni0087.html`. The exact HTTP
HTML response is preserved as `sources/raw-html/paripatal.html` with SHA-256
`07497b27fa06415c89e0023530d7599595521f400cc088cbaeaee9f2ea8e4fc9`.

## Source structure

The page prints two divisions: `பரிபாடல்` with 22 numbered records, followed by
`பரிபாடல்-திரட்டு` with 13 fragment records. The திரட்டு restarts numbering at
1. Corpus filenames use a unique source-order sequence 001–035; each record
retains its printed number independently in `poem_number_as_printed`.

Styled topical headings are recorded in `structure-inventory.json` and are not
treated as verse. Printed attribution fields and recovery/editorial statements
are retained in source notes. Five-line layout counters are excluded. Printed
dot lacunae and anomalous Unicode strings remain unchanged.

## Navigation and provenance

The two files in `sections/` correspond to the two source-printed divisions.
They are navigation aggregations, not additional canonical records. Tiṇai and
speaker values remain null because the selected source does not print them as
controlled poem metadata. Poet, music composer, and paṇ are populated only
where explicitly printed.

## Editorial policy

No external edition has been merged into the canonical transcription.
Comparison evidence belongs only under `apparatus/paripatal/`. Version 1.0.0
freezes the selected source identity and checksum, the 22 main records plus 13
திரட்டு fragment records, canonical bodies, source-note separation,
source-explicit metadata, printed divisions, and validation expectations. It
does not assert that Project Madurai is a critical edition.
