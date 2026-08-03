# Research layer

This directory contains independently versioned, reproducible derivatives of
the immutable Classical Tamil Corpus 1.0.0 release. It must not be used to edit
or supersede canonical transcription.

- `schemas/`: reusable JSON models.
- `controlled-vocabularies/`: small versioned R0 vocabularies.
- `evidence/purananuru/`: authoritative assertions and reporting CSV.
- `mentions/purananuru/`: unresolved literary-body mention candidates.
- `entities/pilot/`: records 1–25 surface-form resolution sample.
- `relationships/pilot/`: assertion-supported pilot relationships.
- `reviews/purananuru/`: append-only events and deterministic review sample.
- `reports/`: coverage, ambiguity, and review reports.

All generated deterministic content excludes execution timestamps. Human review
must append review events rather than silently mutate assertion history.
