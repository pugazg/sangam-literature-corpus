# Patiṉeṇkīḻkkaṇakku corpus programme

This programme adds the eighteen Patiṉeṇkīḻkkaṇakku works as independently
provenanced, source-faithful corpus works. It does not treat the collection as
one homogeneous HTML grammar.

The reusable design is:

```text
shared preservation, schema, manifests, auditing and fidelity validation
+
an explicit source-object boundary and parser profile for each work
```

Every work was first onboarded with `corpus_schema_version: null` and
`version_status: unfrozen`. A formal `1.0.0` freeze was recorded only after
physical inventory, schema, source-output fidelity, source-note fidelity,
idempotence, tests and regression checks pass.

The authoritative source survey is
`sources/source-metadata/pathinenkilkanakku-source-survey.json`. Programme
progress is recorded in `manifests/pathinenkilkanakku-program.json`.

The programme is complete: all eighteen selected works are frozen at `1.0.0`.
The corpus follows the printed source even where a title-derived count differs:
Tiṇaimālai prints 153 numbered records; Paḻamoḻi prints 399 numbered records
plus two unnumbered opening texts; Ciṟupañcamūlam prints 98 numbered records;
and Kainnilai prints four tiṇai headings across 60 records. Missing printed
headings are represented as absences rather than silently supplied.

Canonical transformation remains limited to entity decoding, Unicode NFC, LF
line endings, conservative blank-line cleanup and documented layout-only
boundary restoration. Printed errors, gaps and uncertainty remain evidence.
