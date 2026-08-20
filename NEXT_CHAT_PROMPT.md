# Next Chat Prompt — R2 Core Sangam production

Continue directly in `pugazg/sangam-literature-corpus`.

Active branch: `research/classical-tamil-concept-matrix-r2`. Treat live GitHub state as authoritative.

## Phase boundary

R1.5A merged into `main` at `1e6684b09a5e41fc675ea3e07ba8b6a646d35830`. R2 was explicitly authorized afterward.

R2 uses multi-work production-review schema `0.4.0` while preserving the exact 29 dimensions and all R0/R1/R1.5 histories. It covers the frozen nine-work Core Sangam Corpus. The programme direction through R8 is authorized, but phases remain sequentially gated. Only the current R2 boundary is active.

## Mandatory startup

Before changing the repository, read completely:

1. `docs/DOCUMENTATION_STATUS.md`
2. `docs/SOURCE_TERMINOLOGY_POLICY.md`
3. `PROJECT_HANDOVER.md`
4. `PROJECT_GUIDELINES.md`
5. `docs/r2/ROADMAP.md`
6. `research/production/r2-scope.json`
7. `manifests/sangam-core-program.json`
8. Kuṟuntokai README, metadata and active canonical records
9. R2 schemas, materializer, validator and tests once present
10. current R2 branch/PR metadata and exact-head checks.

## Fixed scope

The nine works contain 2,376 frozen records. Puṟanāṉūṟu 400/400 is a completed carried-forward foundation and must not be re-reviewed. New R2 review scope is 1,976 records.

Kuṟuntokai is complete: `001–401`, 4,540 observations, exact 29-dimension reviews, no next record. Naṟṟiṇai benchmark `001–002` is complete with 26 observations. Next boundary: `003–010` stabilization.

Production architecture: 8 independent Eṭṭuttokai work folders; 10 independent Pattuppāṭṭu long-work folders; 18 independent Patiṉeṇkīḻkkaṇakku folders planned but not activated.

## Evidence contract

Review each poem sequentially/source-first across all 29 dimensions. Preserve exact Tamil, exact body spans, source-explicit heading/attribution fields, canonical hashes, ambiguity, and reviewed-empty semantics. Write the complete durable record before moving to the next.

Printed tiṇai, speaker/context and poet metadata remain provenance-distinct. Tolkāppiyam evidence never auto-classifies a poem. Printed names never become verified historical identities automatically. The frozen corpus is immutable.

## Immediate next activity

Review and materialize Naṟṟiṇai `003–010` sequentially/source-first as its stabilization boundary. Run full CI/non-drift on the exact head. Keep PR #5 draft/unmerged.

Do not start R3.
