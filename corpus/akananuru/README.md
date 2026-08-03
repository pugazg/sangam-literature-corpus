# அகநானுறு (Akanāṉūṟu)

Version status: **frozen**  
Corpus schema version: **1.0.0**

## Canonical source

- Project Madurai identifier: `pmuni0229`
- URL: <https://www.projectmadurai.org/pm_etexts/utf8/pmuni0229.html>
- Printed title: `அகநானுறு / akanAnURu`
- Preserved raw size: 794,903 bytes
- SHA-256: `0f2484a5b1b2df77fd43ab89a206f8f101bfa2d0161e6905f9822b08a04279cb`

This is Project Madurai's complete source-only release. Separate Project Madurai commentary editions were not merged into the canonical transcription.

## Source structure

The HTML uses table records: a bare number cell, BR-delimited literary lines, and separate numeric line-end cells. It contains one unnumbered invocation printed as record `0`, followed by 400 numbered source-order records. Record `0` is retained in `full-text.md`; no `000.md` is fabricated.

The source explicitly prints three macro-divisions:

1. `1.  களிற்றியாணை நிரை` — records 1–120
2. `2.  மணிமிடை பவளம்` — records 121–300
3. `3.  நித்திலக்கோவை` — records 301–400

The three section files reproduce those divisions. They are not mechanical navigation ranges.

## Printed metadata and provenance

The source prints no poem-level tiṇai, speaker/context, or poet attribution. Those structured fields remain null. It is prohibited to derive tiṇai from poem number or to import metadata from commentary editions.

Source-order records 131 and 319 are printed with duplicated labels `130` and `318`. Their canonical filenames follow continuous source order, while `poem_number_as_printed`, source order, source metadata, and validation issues preserve the discrepancy explicitly. Record 174 begins inside malformed table markup and is recovered only from the repeated source record grammar.

Numeric line-end cells are layout markers, not literary lines. Three markers attached to final verse cells (`.129-18`, `.246-10`, `.399-18`) receive the same layout-only treatment. No Tamil spelling or punctuation is corrected.

## Textual conditions

All 400 numbered records contain literary text. The source does not explicitly mark a lost poem, incomplete poem, or candidate text. ASCII ellipses in poems 143 and 354 remain exactly printed; because the source gives no loss statement, their textual force remains unresolved rather than being silently classified or repaired.

Poems 121 and 122 share a first line but have different normalized full bodies. This is informational, not a duplicate-body finding.

## Validation status

The onboarding validator reports 400 canonical poem files, three exact source-division files, complete hardened-schema coverage, 400/400 source-body matches, 400/400 source-note matches, and no identical normalized full bodies. The two duplicated printed number labels remain warnings requiring review.

See `sources/source-metadata/akananuru-reconnaissance.json`, `structure-inventory.json`, and `apparatus/akananuru/` for the source audit and editorial separation policy.

## Corpus schema version 1.0.0 freeze

Version `1.0.0` freezes the canonical `pmuni0229` source identity and checksum; its one-source-object provenance; the 400 deterministic source-order record identities; exact `poem_number_as_printed` values; all canonical literary bodies and source-note representations; record `0` invocation handling; the three printed divisions; numeric layout-marker exclusion; record 174 recovery; the duplicated printed labels at source-order records 131 and 319; the unresolved printed ellipses in poems 143 and 354; and deterministic validation/regeneration expectations.

Canonical `poem_number` is the deterministic corpus/source-order identity for the 400 printed literary records. `poem_number_as_printed` preserves the exact Project Madurai numeric label. For source-order records 131 and 319, these fields intentionally differ because the source duplicates printed labels 130 and 318.

The freeze does not assert that Project Madurai is a critical edition, that the duplicated labels are philologically wrong, that the source-order identities establish critical-edition numbering, that the ASCII ellipses prove textual loss, or that poems possess any tiṇai, speaker/context, or poet metadata not printed by the selected canonical source.
