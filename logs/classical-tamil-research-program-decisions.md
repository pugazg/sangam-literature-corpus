# Classical Tamil Research Layer R0 decisions

## Programme boundary

The research layer is derived from the immutable `classical-tamil-corpus-v1.0.0`
tag and is independently versioned at research schema `0.1.0`. Research data
must never be written into `corpus/`, `sources/`, or `apparatus/`.

## Evidence hierarchy

Frozen canonical corpus → evidence extraction → reviewed assertions → resolved
entities/concepts → relationships/datasets → interpretation/visualisation.
Phase R0 implements the first four structures, but only source-explicit evidence
and reviewable candidates are populated. No external historical or interpretive
assertions are created.

## Identity and review

Assertion IDs hash stable canonical fields and never include timestamps. Exact
printed forms are retained beside separate NFC/punctuation-stripped lookup
forms. Initial metadata copies are `machine_checked`; literary-body candidates
are `human_review_required`. Surface-form entities in records 1–25 are not
claims of historical identity, and variant forms are not automatically merged.

## Mention policy

The pilot uses exact-token matches from a small, versioned Tamil candidate
lexicon plus exact poet/addressee forms printed by the frozen source. Matches
retain exact line and character spans. Their classification is deliberately a
review candidate, not a historical conclusion. No stemming, suffix splitting,
modern geography, translation, taxonomy, biography, dating, or dynastic
assignment is applied.

## Deterministic writing

Work-local record files are written first and one authoritative aggregator
writes NDJSON and CSV. Files use UTF-8/LF, same-directory temporary files,
`fsync`, atomic replacement, and an advisory lock. Timestamps are excluded from
deterministic research content and confined to execution logs/baselines.

## Frozen-release protection

Every assertion pins its canonical whole-record, body, and source-note SHA-256.
Generation and validation fail if the frozen input inventory or release tag
does not match the approved baseline. The pre-existing uncommitted post-tag
verification log remains external audit evidence and is not altered.

The first baseline file (`20260803T193822`) treated the Markdown heading as
part of the derived body-hash projection when a blank line preceded it. Tests
caught that research-only boundary error before acceptance. It was not used for
freeze comparison. The corrected, independently created baseline
`pre-research-layer-frozen-baseline-20260803T194532.json` supersedes it and uses
the same canonical-body boundary as the corpus fidelity model. Neither baseline
operation modified frozen files.

<!-- R1_REVIEW_WORKFLOW_COMPLETE_20260818 -->
## R1 reconciliation and review-workflow decisions — 2026-08-18

R1 was created from current `main` (`05bc2ae328a7f9cc94129b295f6c59d7457491ec`)
rather than by advancing the stale R0 branch. The attempted direct R0→R1 merge
conflicted and was not merged. The accepted reconciliation overlays the exact R0
research subtree and research-support blobs onto the current Corpus 1.1.0 base;
it does not write canonical corpus paths.

R0 evidence remains schema `0.1.0`. R1 workflow records are versioned separately
at `0.2.0`; upgrading the workflow does not rewrite assertion IDs, spans, source
hashes, or evidence text.

`review-events.ndjson` is append-only. The R0 generator entry point now delegates
to the preserved R0 implementation while protecting existing review history.
Assistant-assisted review is recorded explicitly and creates no verified
historical identity.

Entity equality by printed/normalized form is never an automatic merge. R1
records only assertion-provenanced conservative candidate/possible-match
decisions in the production pilot. Merge, split, reject, and supersede remain
supported audited operations.

No external historical or interpretive assertion is introduced in R1. R1.5
Classical Tamil Concept Matrix is the next permitted phase; R2 must not begin
directly.
