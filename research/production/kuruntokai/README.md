# Kuṟuntokai R2 production

Active phase: R2 under schema `0.4.0`.

Frozen source: `corpus/kuruntokai/poems/`. Never modify the canonical poems for research classification.

Benchmark: `001–002` — materialized as 2 gap-free records with 22 observations (001: 12; 002: 10), 29 dimension decisions per record, and next record `kuruntokai-003`. Stabilization after a green exact-head validation: `003–010`.

Every poem is reviewed sequentially/source-first across the exact 29 dimensions. Printed `thinai_as_printed`, `speaker_as_printed`, and `poet_as_printed` are separate metadata evidence. Mechanical section ranges are provenance/navigation only. Conventional tiṇai associations and Tolkāppiyam rules never auto-populate poem dimensions.

The reviewed spec is the durable human/assistant decision layer. Materialization must be deterministic and must reproduce exact canonical body spans and hashes.
