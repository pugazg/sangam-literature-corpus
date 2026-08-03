# Classical Tamil Research Layer

## Purpose and status

The Classical Tamil Research Layer is a derived, replaceable research programme
above the frozen 27-work corpus. Phase R0, “Research Architecture and
Puṟanāṉūṟu Evidence Pilot,” uses research schema version `0.1.0` and status
`pilot`. It is not part of corpus release 1.0.0.

## Architecture

The immutable corpus supplies source-faithful records. Assertions retain exact
provenance and spans; append-only reviews qualify them; resolved entities remain
separate from mentions; relationships cite assertion IDs. Interpretation and
external historical claims are later layers and are empty in R0.

## Evidence, confidence, and review

Evidence class describes provenance; confidence describes extraction or
boundary confidence. They are never interchangeable. Exact frozen metadata is
initially `SOURCE_EXPLICIT`, high confidence, and `machine_checked`.
Literary-body candidates retain printed spans as `SOURCE_EXPLICIT`, medium
confidence, and `human_review_required`; this records that the string occurs in
the source without asserting that its category or historical identity is
verified. Only an explicit review event may advance a status to `verified`.

## Tamil text policy

Canonical Tamil is never changed. Derived lookup normalization applies NFC,
replaces punctuation with spaces, and collapses whitespace. The printed form,
canonical source text, and zero-based character offsets remain authoritative.
No silent stemming, morphology, translation, modern identification, or spelling
regularisation is performed.

## Generation and validation

```bash
python3 scripts/generate_research_layer.py --root .
python3 scripts/validate_research_layer.py --root .
pytest -q
```

Generation is serialized by an advisory lock and uses atomic replacement. The
validator checks schemas/vocabularies, deterministic IDs, canonical hashes,
exact evidence spans, relationship provenance, review transitions, stable
inventory, and release-tag identity.

## Puṟanāṉūṟu pilot

All 400 canonical records receive a metadata/textual-condition pass. The 398
available literary bodies receive conservative exact-token candidate scanning.
Records 267 and 268 remain source-lost and yield no literary-body mentions. A
surface-form-only entity and relationship sample is limited to records 1–25.
The deterministic review sample is not automatically human-verified.

## Limits

Counts are evidence-record counts, not historical fact counts. Phase R0 does
not provide translations, summaries, sentiment, reconstructed identities,
modern geography, embeddings, a public website, or a final knowledge graph.
