# Tolkāppiyam concept-evidence stream — R1.5

This directory reserves a **separate grammatical/poetics concept-evidence stream** for Tolkāppiyam.

R1.5 establishes the schema and methodological boundary only. It does **not** bulk-populate Tolkāppiyam observations and does not treat a நூற்பா as a poem-level source classification.

Future populated records must conform to `research/schemas/tolkappiyam-concept-evidence-r15.schema.json` and must preserve:

- the canonical Tolkāppiyam record ID;
- exact source-supported surface form/location;
- the canonical record SHA-256;
- `GRAMMATICAL_CONCEPT_EVIDENCE` as the evidence class;
- `tolkappiyam_mapping` as the classification basis;
- explicit confidence and review status;
- a stable controlled `concept_id` from the versioned registry.

A Tolkāppiyam concept assertion may later support comparison with poem evidence, but it must never silently rewrite or auto-classify a Sangam poem. Cross-text applications must remain separate, assertion-backed research claims.

No production Tolkāppiyam concept-evidence records are created in R1.5. Corpus-wide or cross-text population belongs to a later approved phase after the R1.5 acceptance gates pass.
