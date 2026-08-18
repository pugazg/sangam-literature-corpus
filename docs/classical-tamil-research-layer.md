# Classical Tamil Research Layer

## Purpose and version boundary

The Classical Tamil Research Layer is a derived, replaceable research programme above the immutable Classical Tamil Corpus. It never edits canonical transcription, raw source preservation, or editorial apparatus.

Puṟanāṉūṟu R0 evidence remains at research evidence schema `0.1.0`. R1 introduces independently versioned review and entity-resolution workflow schema `0.2.0`. The workflow version does not rewrite assertion IDs, evidence spans, canonical hashes, printed forms, or R0 evidence files.

R0 was originally derived from `classical-tamil-corpus-v1.0.0`. Before R1 began, the exact R0 research layer was reconciled onto the current Corpus 1.1.0 base. Corpus 1.1.0 adds the independently frozen Tolkāppiyam work; the reconciliation does not modify Puṟanāṉūṟu or any other canonical corpus path.

## Architecture

The immutable corpus supplies source-faithful records. Assertions retain exact provenance and spans. Reviews qualify assertions through append-only review events. Resolved or candidate entities remain separate from mentions. Relationships and entity-resolution decisions cite assertion IDs. Interpretation and external historical claims remain later layers and are not populated in R1.

The evidence hierarchy is:

frozen canonical corpus → deterministic source assertions → explicit review events → candidate/resolved entities → assertion-supported relationships/datasets → later interpretation/visualisation.

## Evidence, confidence, review, and identity

Evidence class, extraction confidence, review status, and identity-resolution state are independent dimensions.

- `SOURCE_EXPLICIT` states what the frozen source supports; it does not make a historical claim by itself.
- `machine_checked` is not human verification.
- `human_review_required` requires an editor/person to inspect the evidence before review advancement.
- `reviewed` requires an explicit recorded review event.
- `verified` requires a stronger explicit verification decision and cannot be reached directly from `machine_checked` or `human_review_required`.
- `rejected` and `superseded` records remain auditable.
- `possible_match` / `POSSIBLY_SAME_AS` is explicitly weaker than verified identity.

Assistant-assisted review must identify itself as `assistant_assisted`. In R1 it may confirm an exact source occurrence, evidence span, and bounded candidate category when the canonical source supports that decision. It does not by itself establish biography, dynasty, modern geography, dating, taxonomy, or historical co-reference.

## Append-only review history

`research/reviews/purananuru/review-events.ndjson` is a primary history, not a generator scratch file. Events are sequenced and hash-chained. Deterministic generators read this history but never truncate or rewrite it.

Each reviewed source candidate retains its work/record, assertion ID, printed form, exact evidence span, source field/location, prior and new review status, reviewer identity/type, rationale, supporting assertion IDs, ambiguity note, verification scope, and event timestamp.

Reviewer prose is never written back into deterministic source assertions.

## Entity resolution

`research/entities/pilot/entity-resolution-decisions.ndjson` records explicit identity decisions separately from the R0 surface-form entities.

Supported operations are `retain`, `possible_match`, `merge`, `split`, `reject`, and `supersede`. Supported identity states include unresolved/candidate, possible match, reviewed match, verified match, rejected match, split required, and superseded.

No operation is inferred merely because two strings share a printed form, lookup-normalised form, epithet, or geographic context. Every populated decision cites supporting assertion IDs. R1 production decisions remain deliberately conservative: possible variant-form groupings may be recorded as `possible_match`, while exact-surface groupings may be retained as candidate entities. No verified historical identity is manufactured to populate a report.

## Deterministic R1 exports

Primary histories are converted into stable derived views:

- `research/reviews/purananuru/review-queue.ndjson`
- `research/reviews/purananuru/reviewed-export.ndjson`
- `research/reports/purananuru-r1-review-summary.json`
- `research/reports/purananuru-r1-review-summary.md`
- `research/reports/purananuru-r1-ambiguity-register.md`
- `research/reports/purananuru-r1-unresolved-entities.csv`

Execution timestamps are excluded from these deterministic aggregate outputs. Timestamps occur only in event/audit records where time is semantically part of the record.

## Tamil text and normalisation policy

Canonical Tamil is never changed. Derived lookup normalisation remains Unicode NFC plus punctuation-to-space and whitespace collapse. Printed forms, canonical source text, and exact zero-based character offsets are authoritative. No silent stemming, morphology, translation, modern identification, spelling regularisation, or historical reconstruction is performed.

## Generation and validation

R0 evidence generation remains available through a compatibility wrapper that delegates to the preserved R0 implementation while protecting an existing append-only review history:

```bash
python3 scripts/generate_research_layer.py --root .
```

R1 deterministic review exports are generated separately:

```bash
python3 scripts/generate_research_r1.py --root .
python3 scripts/validate_research_layer.py --root .
python3 scripts/validate_research_r1.py --root .
pytest -q
python3 scripts/audit_repository.py --root .
```

Generation uses the repository advisory lock and atomic replacement for derived outputs. The R1 validator checks review-event integrity, reviewer type, legal transitions, exact assertion/source references, entity-decision provenance, deterministic queue ordering, R0 identity invariants, relationship integrity, and the recorded Corpus 1.1.0 compatibility gate.

## Puṟanāṉūṟu R1 pilot scope

The deterministic pilot is bounded to the existing records 1–25 entity sample, the R0 deterministic review sample, and entities directly represented by that pilot. R1 does not attempt to resolve all 285 body mention candidates automatically.

The original R0 extraction remains 400 canonical records / 398 literary bodies with records 267 and 268 source-lost. R1 does not reconstruct those losses.

## Limits and next phase

R1 does not provide translations, summaries, sentiment, reconstructed historical identities, modern geography, embeddings, a public website, or a final knowledge graph. It introduces no `EXTERNAL_HISTORICAL` or `INTERPRETATION` assertions.

After R1 validation and audit are complete, the mandatory next phase is **R1.5 Classical Tamil Concept Matrix**, governed by `docs/CLASSICAL_TAMIL_RESEARCH_MATRIX.md`. R2 corpus-wide extraction must not begin before R1.5 formalises the observation model and passes its own validation gates.
