# பத்துப்பாட்டு (Pattuppāṭṭu)

Status: **frozen**  
Corpus schema version: **1.0.0**

## Canonical source model

Pattuppāṭṭu is represented as ten source-ordered long-poem records. Each record is derived from its own checksum-pinned Project Madurai HTML object and retains that object's identifier, URL, filename, byte size and SHA-256. There is deliberately no substitute aggregate source checksum.

The canonical record order is the adopted Pattuppāṭṭu anthology order corroborated by the ordinal descriptions printed on the individual Project Madurai pages. Project Madurai does not supply these ten selected texts as one anthology-level HTML object, so the corpus does not claim that the complete ordering is printed by a single source object.

## Record and navigation structure

`poems/001.md` through `poems/010.md` are the ten canonical records. The ten files under `sections/` are generated source-order navigation mirrors, one per long poem; they are not additional ancient divisions. Printed internal headings remain subordinate entries in `structure-inventory.json`.

திருமுருகாற்றுப்படை has six numbered internal headings and thirteen additional printed internal labels. They do not become separate anthology records.

## முல்லைப்பாட்டு

The selected object is Project Madurai `pmuni0488`, a commentary-bearing edition of முல்லைப்பாட்டு with நச்சினார்க்கினியர்'s notes, edited by உ.வே. சாமிநாத அய்யர். Its contiguous 103-line literary block is independently extracted. Commentary and editorial prose remain preserved in the raw object and documented in the apparatus, but never enter the canonical literary body.

See `sources/source-metadata/mullaippattu-canonical-source-decision.md`.

## Normalization and fidelity

Allowed transformations are HTML entity decoding, Unicode NFC, LF line endings, blank-layout cleanup and removal of line-end numeric layout markers. Tamil spelling, punctuation, names, uncertainty and literary wording are not corrected. Every record is checked against its extracted source block and its source-note representation.

## Regeneration

```bash
python3 scripts/process_work.py pattuppattu
python3 scripts/validate_output.py --work pattuppattu
```

Regeneration refuses unexpected poem or section files.

## Corpus schema version 1.0.0 freeze

Pattuppāṭṭu 1.0.0 freezes:

- the ten selected Project Madurai source-object identities, raw files and individual SHA-256 checksums;
- their source order and exact record-to-source mapping;
- canonical long-poem records `001`–`010`, their literary bodies, source-note representation and per-record provenance;
- the `pmuni0488` Mullai decision, its 103-line literary boundary, commentary exclusion, and isolation from non-selected `pmuni0053`;
- திருமுருகாற்றுப்படை's six numbered headings and thirteen additional labels as nineteen subordinate structural records, separate from its 317 literary lines;
- the ten navigation mirrors as generated aids rather than ancient divisions;
- the declared/extracted line-count pairs, including `pmuni0069` 500/501, `pmuni0073` 261/262 and `pmuni0077` 301/302;
- physical inventory, fidelity, validation and deterministic-regeneration expectations.

The Project Madurai pages print declared line counts that differ by one from the independently extracted BR-delimited literary lines in three records. The corpus preserves all printed literary lines and records the discrepancies without speculative line merging.

The freeze does not assert that these objects constitute a critical edition, that they originated as one anthology HTML object, that `pmuni0488` is source-only or preferable to `pmuni0053`, or that commentary and variant readings are canonical literary text. It makes no literary, historical or geographic interpretation.
