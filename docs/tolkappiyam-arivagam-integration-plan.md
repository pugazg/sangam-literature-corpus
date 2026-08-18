# Tolkāppiyam Arivagam integration plan

The preservation dependency direction is one-way:

```text
pugazg/sangam-literature-corpus
    ↓ exports a versioned, checksum-pinned canonical Tolkāppiyam dataset
pugazg/tolkappiyam-arivagam
    ↓ consumes or synchronizes that dataset for its website
```

The corpus repository owns raw-source provenance, canonical நூற்பா bodies, structure, stable corpus identities, validation, and release fingerprints.

Tolkāppiyam Arivagam may add teaching material, translations, explanations, search, transliteration, māttirai tools, commentary, and UI metadata, but those remain outside the canonical source layer.

A future integration should consume an immutable release asset containing repository metadata, structure inventory, canonical record export, and SHA-256 inventory. The website should pin the corpus release identity and verify checksums.

No corpus regeneration path may depend on website runtime code, live website state, or application-only metadata.

For research, the corpus also owns the separately versioned Tolkāppiyam grammatical/poetics concept-evidence contract. That derived evidence may be consumed by research applications only with its schema/provenance intact; it must never be converted into automatic poem classification.

This plan does not modify the Arivagam repository.
