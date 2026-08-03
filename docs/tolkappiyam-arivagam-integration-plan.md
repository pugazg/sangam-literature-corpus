# Tolkāppiyam Arivagam integration plan

The preservation dependency direction is one-way:

```text
classical-tamil
    ↓ exports a versioned, checksum-pinned canonical Tolkāppiyam dataset
tolkappiyam-arivagam
    ↓ consumes or synchronizes that dataset for its website
```

The corpus repository owns raw-source provenance, canonical நூற்பா bodies,
structure, stable corpus identities, validation, and release fingerprints. The
website may add teaching material, translations, explanations, search,
transliteration, māttirai tools, commentary, and UI metadata, but those fields
remain outside the canonical source layer.

A future integration should consume an immutable release asset containing
`metadata.json`, `structure-inventory.json`, canonical record NDJSON/JSON and
SHA-256 inventory. The website must pin the corpus release tag and verify its
checksum. No corpus regeneration path may depend on website runtime code or
live GitHub access. This goal does not modify the Arivagam repository.
