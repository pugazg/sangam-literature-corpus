# Classical Tamil Corpus release 1.1.0

## Scope

Release `1.1.0` is an additive checkpoint containing 28 works and 7,234
canonical records. It preserves all 27 works and 5,632 poem records certified
by `classical-tamil-corpus-v1.0.0` and adds Tolkāppiyam as 1,602 independently
verified நூற்பா records.

The Tolkāppiyam hierarchy is work → 3 அதிகாரம் → 27 இயல் → 1,602 நூற்பா.
Its canonical source is the exact Project Madurai `pmuni0100` HTML blob imported
byte-for-byte from `pugazg/tolkappiyam-arivagam` commit
`16123f742503283e46f0ed321802a46f99df6392`. The source SHA-256 is
`16b2edf314763ef491bdc498c0017de33e7e190753587b230bbafcd03219f5da`.

## Independence from the web application

The corpus parser independently verifies the preserved HTML. Upstream generated
files are comparison evidence only. Application pages, components, styles,
search, teaching content, explanations, glossaries, analysis, and deployment
configuration are not corpus dependencies and do not enter canonical bodies or
source-explicit metadata.

## Verification

The work-level freeze requires 1,602/1,602 source-output matches,
1,602/1,602 source-note matches, exact physical inventories, 12 independently
reviewed source conditions, two byte-stable regenerations, and regression checks
for the previous 27 frozen works. The repository release uses neutral
`records.csv` for all record types while retaining the approved 5,632-row
`poems.csv` unchanged.

The `1.1.0` source, work, record, and protected-condition inventories and the
deterministic content fingerprint under `manifests/` define the checkpoint.
The prior `classical-tamil-corpus-v1.0.0` tag is immutable and is not moved.

## Rights and publication

The source-rights review is maintained at
`docs/source-rights-and-redistribution-review.md`. The GitHub repository remains
private unless a later, separately authorized visibility decision follows a
complete rights review. A release tag certifies preservation and reproducible
source representation; it does not assert that Project Madurai is a critical
edition.
