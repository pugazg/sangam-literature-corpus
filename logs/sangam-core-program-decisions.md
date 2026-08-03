# Core Sangam corpus programme decisions

Date: 2026-07-29

## Programme boundary

The completed core comprises the eight Ettuttokai anthologies plus Pattuppāṭṭu:
Naṟṟiṇai, Aiṅkuṟunūṟu, Kuruntokai, Akanāṉūṟu, Puṟanāṉūṟu,
Patiṟṟuppattu, Paripāṭal, Kalittokai, and Pattuppāṭṭu. All nine are frozen at
corpus schema version 1.0.0.

## Architecture decision

The reusable architecture is:

```text
shared preservation, schema, manifests, audit, fidelity, and validation
+
explicit source-specific parser and structural strategy
```

No parser is a default fallback. Unknown work slugs fail. Work profiles declare
physical inventories and section strategies without weakening another work.

## Source-structure decisions

- Mechanical ranges are used only where no source divisions are printed and
  are labelled as navigation.
- Source-printed divisions and groups are preserved when present.
- Pattuppāṭṭu uses ten independently checksum-pinned source objects and ten
  long-poem records.
- Patiṟṟuppattu preserves only surviving numbered records 11–90; unavailable
  first and tenth groups are structural loss evidence, not manufactured poems.
- Paripāṭal preserves 22 main poems plus 13 Tirattu fragments as 35 unique
  source-order records, retaining restarted printed numbering separately.
- Kalittokai uses 150 table-row records and six printed structural sections
  including the invocation.

## Editorial decisions

Canonical text records what the selected Project Madurai source prints after
only documented mechanical normalization. Lost text, lacunae, malformed labels,
uncertain attributions, and source anomalies remain explicit. External
comparisons are isolated in apparatus directories and never overwrite canonical
bodies or provenance.

## Completion evidence

The final recursive physical audit passed. Seventy-three tests passed. Each work
validated with zero errors. Sequential regeneration of all nine works produced
no path additions, removals, or corpus-file hash changes. `manifests/poems.csv`
contains 2,376 records and `manifests/works.json` contains exactly nine frozen
work records.
