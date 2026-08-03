# தொல்காப்பியம் / Tolkāppiyam

Status: **frozen**  
Corpus schema version: **1.0.0**

## Canonical source

The canonical artifact is the exact 384,080-byte Project Madurai `pmuni0100`
HTML object copied byte-for-byte from `pugazg/tolkappiyam-arivagam` commit
`16123f742503283e46f0ed321802a46f99df6392`. Its SHA-256 is
`16b2edf314763ef491bdc498c0017de33e7e190753587b230bbafcd03219f5da`.
Regeneration uses this preserved local object and never requires live GitHub or
Project Madurai access.

## Structure and identity

The independently parsed hierarchy is work → 3 அதிகாரம் → 27 இயல் → 1,602
நூற்பா. Canonical records use `nurpas/0001.md` through `nurpas/1602.md` and
repository IDs `tolkappiyam-0001` through `tolkappiyam-1602`. Source sequence,
traditional இயல்-local number, display number, and the verified upstream
semantic ID are retained separately. The upstream semantic ID is an alias, not
the sole preservation identity.

`adhikarams/` and `iyals/` are deterministic source-structure aggregations, not
additional canonical records. The source-printed சிறப்புப் பாயிரம் is preserved
as structural prefatory material and is not counted as a numbered நூற்பா.

## Source and editorial separation

Canonical bodies contain only source-extracted literary/grammatical lines.
Upstream English headings, transliteration, glosses, concepts, keywords,
explanations, related aphorisms, commentary placeholders, audio fields, and
application labels are excluded. Seven source/editorial heading differences
remain separately represented. Five attached-number cases receive only a
layout-boundary restoration.

## Freeze validation

Independent results: 1,597 high-confidence records, five medium-confidence
attached-number records, zero low-confidence records, and twelve confirmed
warning conditions. Source-output and source-note fidelity are 1,602/1,602.
The independent work-level freeze completed after two byte-stable regenerations,
full physical inventory and fidelity validation, and regression validation of
all 27 previously frozen works. Version `1.0.0` certifies this exact
source-faithful representation; it does not treat the upstream web application
or its editorial fields as canonical source authority.
