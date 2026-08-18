# Classical Tamil Research Layer programme decisions

## R0 boundary

The research layer is derived from immutable corpus evidence and independently versioned. Research data must never be written into frozen corpus/source paths merely to support analysis.

R0 established deterministic source-grounded Puṟanāṉūṟu assertions, conservative mention candidates, surface-form entities and relationships. It introduced no external-historical or interpretive assertion population.

Assertion IDs exclude timestamps. Printed forms and exact evidence spans remain authoritative. No stemming, suffix splitting, modern geography, taxonomy, biography, dating, dynasty assignment or automatic historical identity resolution is applied.

## R1 reconciliation / review decisions — 2026-08-18

R1 was reconciled onto the then-current Corpus 1.1.0 base while preserving exact R0 research identity. R0 evidence remains schema `0.1.0`; R1 workflow is independently versioned at `0.2.0`.

`review-events.ndjson` and entity-resolution decisions are append-only primary histories. Assistant-assisted review is recorded explicitly and creates no verified historical identity.

Printed/normalized equality never causes automatic merge. Production decisions remain conservative and assertion-provenanced.

R1 is complete and merged into `main`. Historical R0/R1 branches were later deleted after their work was preserved.

## R1.5 concept-matrix decisions — 2026-08-18

R1.5 introduces concept/observation schema `0.3.0` without changing R0 evidence or R1 workflow identity.

A concept observation is a derived classification view over evidence; it is not a new canonical transcription and does not rewrite its assertion.

Matrix cells are evidence-bearing views, never unsupported booleans. Every populated production row retains stable observation ID, work/record identity, exact printed form/span, evidence class, classification basis, confidence/review state and supporting assertion IDs.

The bounded production pilot contains eight R1-reviewed source candidates. All remain source-explicit. No external-historical or interpretive observation and no verified historical identity are created.

The concept foundation includes Akam/Puram states, seven tiṇai categories, first-class tuṟai, five landscape families, named-entity families and lived-life dimensions. Conventional associations are not hard-coded into one another.

Tolkāppiyam has a separate grammatical/poetics concept-evidence contract. R1.5 creates zero production Tolkāppiyam concept-observation records and forbids automatic poem classification.

## Exhaustive R1.5 pre-merge audit decision — 2026-08-18

The bounded pilot was not treated as proof that all Puṟanāṉūṟu records had been semantically reviewed against every matrix dimension.

The merge boundary was reopened and the project completed:

- Puṟanāṉūṟu 400 / 400 records × 29 dimensions;
- Tolkāppiyam 1,602 / 1,602 நூற்பா across 27 இயல் × 29 dimensions;
- sparse audit ledgers and deterministic dimension summary;
- 29-dimension Tolkāppiyam formal crosswalk;
- explicit ban on automatic Tolkāppiyam → Sangam classification.

Audit ledgers are review evidence and do not automatically become production observations.

## Source-terminology decision — 2026-08-18

Classical Tamil source terms for social, ritual, learned, occupational, political, kinship and community roles must remain in the exact Tamil form printed by the relevant source in source-level research prose.

For example, மரபியல் நூற்பா 71 uses `அந்தணர்` and நூற்பா 72 uses `அரசர்`; those source terms are retained.

Do not silently replace such forms with later caste, sectarian, modern-community, hierarchy or external-influence identities. Any later equivalence claim belongs to a separately classified external-evidence or interpretive assertion with independent provenance.

## Documentation-audit decision — 2026-08-18

Active current-state documents must not preserve deleted branch instructions or completed-phase “next activity” guidance as executable prose.

Historical prompts remain under `docs/history/`; release documents and durable machine logs retain the historical state they actually record.

`docs/DOCUMENTATION_STATUS.md` defines the active/historical boundary, and a documentation regression test prevents the old R0/R1 branch instructions from returning to active operational docs.

PR #3 remains open, draft and unmerged. R2 remains blocked until explicit user merge authorization and fresh inspection of merged `main`.
