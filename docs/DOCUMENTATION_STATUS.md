# Documentation status — R1.5 pre-merge audit and production review

## Purpose

This file records which documents are current operational authority and which files are intentionally historical/frozen snapshots.

It exists because older continuity prose survived after R0/R1 completion and branch deletion, creating contradictory current-branch and next-activity instructions.

## Live repository state at audit

- repository: `pugazg/sangam-literature-corpus`
- default branch: `main`
- active research branch: `research/classical-tamil-concept-matrix-r1.5`
- PR #3: open, draft, unmerged
- R2: not started / blocked

Only `main` and the R1.5 research branch were returned by the live branch inspection during the documentation audit.

## Current R1.5 activity

The exhaustive pre-merge audit is complete as a coverage/control artifact.

The user has approved a stronger R1.5 production-review continuation before any merge decision:

1. make the exact 29-dimension registry the canonical production matrix surface;
2. align the older coarse 22-dimension production vocabulary/schema to that exact 29-dimension surface;
3. validate the schema alignment;
4. review Puṟanāṉūṟu records 1–400 sequentially and write each poem's durable matrix/review state before moving to the next;
5. only after Puṟanāṉūṟu is complete and validated, review all 1,602 Tolkāppiyam நூற்பா across 27 இயல் using the same all-29-dimensions discipline while keeping grammatical/poetics evidence separate from Sangam literary-world observations.

This remains R1.5. PR #3 must stay draft/unmerged and R2 stays blocked.

## Current operational documents

The following must describe current R1.5 pre-merge state and must not contain executable instructions for deleted R0/R1 branches:

- `README.md`
- `PROJECT_GUIDELINES.md`
- `PROJECT_HANDOVER.md`
- `NEXT_CHAT_PROMPT.md`
- `docs/CLASSICAL_TAMIL_RESEARCH_MATRIX.md`
- `docs/classical-tamil-research-layer.md`
- `docs/SOURCE_TERMINOLOGY_POLICY.md`
- `docs/tolkappiyam-arivagam-integration-plan.md`
- `docs/handover/r15-premerge-audit/README.md`
- `docs/handover/r15-premerge-audit/01-PURANANURU.md`
- `docs/handover/r15-premerge-audit/02-TOLKAPPIYAM.md`
- `docs/handover/r15-premerge-audit/03-VALIDATION-AND-MERGE-GATE.md`
- `docs/handover/r15-premerge-audit/04-29-DIMENSION-PRODUCTION-REVIEW.md`
- `research/audits/r15-premerge/dimensions.json`
- `research/controlled-vocabularies/concept-dimensions-r15.json`
- `research/README.md`
- `research/audits/r15-premerge/README.md`
- `logs/classical-tamil-research-program-decisions.md`

## Historical / immutable-document classes

These are not expected to be rewritten merely because project status advances:

1. `docs/history/` — superseded prompts retained for provenance; never execute as current instructions.
2. release documents such as `docs/classical-tamil-corpus-release-1.0.0.md` and `docs/classical-tamil-corpus-release-1.1.0.md` — release snapshots.
3. durable machine logs under `logs/` — records of the run/head they actually describe; old workflow IDs remain historically correct.
4. corpus/work README and metadata files — preservation documentation tied to frozen source/release state unless a real preservation change occurs.
5. static policies such as manifest ordering and rights review — update only when their policy/facts change.

## Documentation defects already corrected

- removed deleted R0/R1 branches from active current-branch instructions;
- removed instructions to restart completed R0 reconciliation/R1 work;
- changed R1/R1.5 roadmap status to completed/current pre-merge state;
- made PR #3 merge hold explicit across active continuity files;
- kept R2 blocked and unstarted;
- synchronized exhaustive Puṟanāṉūṟu/Tolkāppiyam audit status;
- synchronized source-terminology policy across research/continuity docs;
- corrected the Tolkāppiyam Arivagam integration plan to the active repository name;
- removed stale fixed workflow/test counts from general active docs where they would quickly become outdated;
- retired the one-shot R1.5 continuity finalizer so it cannot overwrite current docs with older phase prose;
- added a split continuation file for the 29-dimension production review instead of enlarging one monolithic handover.

## Source-terminology boundary

`docs/SOURCE_TERMINOLOGY_POLICY.md` is current authority.

Classical Tamil social, ritual, learned, occupational, political, kinship and community terms remain in the exact source-supported Tamil form in source-level research descriptions. Later identity/equivalence claims are separate evidence classes.

## Validation policy

`tests/test_documentation_status.py` protects the active-document boundary against reintroducing deleted-branch instructions, the former repository name in the integration plan, or disallowed later identity terminology.

Documentation and production-review changes must pass the same PR workflow as the rest of R1.5, including full regression, repository audit, corpus/Tolkāppiyam non-drift and R1 primary-history preservation.

The strengthened production review must additionally make the 29-dimension surface machine-enforced and prove record-level completion rather than relying only on aggregate coverage statements.

## Merge hold

A green audit or production review is **not** merge authorization.

Keep PR #3 open, draft and unmerged until the user explicitly authorizes merge. Do not start R2 before an authorized merge and fresh inspection of merged `main`.
