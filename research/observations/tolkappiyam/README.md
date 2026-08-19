# Tolkāppiyam concept-evidence stream — R1.5 / R1.5A

This directory is the **separate grammatical/poetics concept-evidence stream** for Tolkāppiyam.

R1.5 established the schema and methodological boundary. R1.5A may populate reviewed production evidence only after the Puṟanāṉūṟu 001–400 production prerequisite is complete and validated.

Formal production observations must conform to `research/schemas/tolkappiyam-concept-evidence-r15.schema.json` and preserve:

- canonical Tolkāppiyam record ID;
- exact source-supported surface form/location;
- canonical record SHA-256;
- `GRAMMATICAL_CONCEPT_EVIDENCE`;
- `tolkappiyam_mapping`;
- explicit confidence and review status;
- a stable controlled `concept_id` from a versioned registry.

`r15-production.ndjson` is a deterministic flattened view of formal concept evidence embedded in the per-நூற்பா production records. It is generated; the per-record review files are the durable 29-dimension review ledger.

A lexical item used only as an example remains an **incidental example** in the production record and is not emitted into the formal concept-evidence stream.

A Tolkāppiyam concept assertion may later support comparison with poem evidence, but it must never silently rewrite or auto-classify a Sangam poem. Cross-text applications remain separate, evidence-backed research claims.

R2 remains blocked.
