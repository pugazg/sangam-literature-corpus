# Sangam Literature Corpus — Project Working Guidelines

## 1. Authority and scope

The active repository is `pugazg/sangam-literature-corpus`.

Treat live GitHub state as authoritative. Historical chat summaries, local absolute paths, earlier repository names, and old prompt text are secondary evidence only.

This repository contains two conceptually different layers:

1. the frozen preservation corpus;
2. independently versioned derived research layers.

Never blur them.

## 2. Core preservation principle

The project preserves what the selected source prints, including uncertainty and irregularity.

Prefer:

- source-faithful;
- checksum-pinned;
- deterministic;
- provenance-rich;
- explicit about uncertainty;
- independently auditable.

Do not prefer:

- cosmetically clean output;
- conventional counts over physical source evidence;
- silently modernised spelling;
- inferred missing headings;
- merged editions;
- repaired punctuation;
- reconstructed historical identities;
- convenient parser assumptions.

## 3. Frozen corpus protection

All 28 currently frozen works are protected release objects.

Before changing shared infrastructure, capture or verify a baseline covering:

- source-object inventory;
- source bytes and SHA-256;
- canonical record inventory;
- canonical body hashes;
- source-note hashes;
- whole-record hashes;
- structure/navigation inventories;
- work metadata;
- schema/version state;
- protected anomaly records.

No frozen body, source note, raw source, source decision, or version field may drift without an explicit new corpus release process.

A research change is never sufficient reason to edit frozen corpus content.

## 4. Release discipline

Current release identities:

- Classical Tamil Corpus 1.0.0 — 27 works / 5,632 canonical numbered records;
- Classical Tamil Corpus 1.1.0 — 28 works / 7,234 canonical records, adding 1,602 Tolkāppiyam நூற்பா.

Do not move, delete, recreate, or retarget an existing release tag.

Do not amend historical release commits merely to improve documentation.

A new corpus release is required only when the frozen preservation layer itself intentionally changes or grows.

Derived research work has its own versioning and must not cause an unnecessary corpus release.

## 5. Git branch discipline

Use `main` for verified repository state and durable project documentation.

Use dedicated branches for active research or corpus-extension work.

Current important branches include:

- `main`;
- `research/sangam-evidence-r0`.

For the next research continuation, create a fresh branch from current `main` such as:

`research/sangam-evidence-r1`

Then port/reconcile R0 onto it after inspecting the exact diff.

Do not force-push shared branches.

Do not reset away unexplained changes.

Do not merge a stale research branch blindly when it is behind current release work.

## 6. Source acquisition rules

Whenever a new canonical source object is added:

1. preserve exact bytes;
2. record source URL / identifier;
3. record byte size;
4. record SHA-256;
5. record acquisition date and method;
6. preserve source header / attribution where required;
7. classify artifact type accurately;
8. distinguish source-only and commentary-bearing editions;
9. document non-selected competing editions;
10. never silently replace an already frozen source identity.

Rendered browser text is not raw HTML.

OCR is not authoritative when a reliable encoded source exists.

## 7. Edition-selection rules

When multiple editions exist:

- compare them explicitly;
- choose one coherent canonical source/edition or source set;
- document the rationale;
- isolate commentary, variants, and editorial prose;
- keep non-selected editions in apparatus/evidence space;
- do not create a synthetic critical text by mixing preferred readings.

Ease of parsing is not a valid edition-selection criterion by itself.

## 8. Source text versus derived fields

Keep these categories separate:

- canonical literary text;
- source-explicit metadata;
- mechanically derived fields;
- source notes;
- commentary;
- editorial prose;
- external evidence;
- interpretation.

Only the first two belong in the canonical preservation layer as source content/metadata.

Mechanically derived values must be labelled as such.

External evidence can never overwrite canonical text.

## 9. Printed identity versus repository identity

Keep distinct where necessary:

- canonical repository record ID;
- source order;
- printed number;
- division-local number;
- chapter-local number;
- traditional number;
- generated semantic ID;
- upstream alias.

Never silently correct repeated, missing, restarted, or malformed printed numbering.

Deterministic repository IDs are allowed, but the source's printed identity must remain recoverable.

## 10. Structure versus navigation

Source-printed structure and generated navigation are different concepts.

Examples of valid source structure:

- பத்து groups;
- printed macro-divisions;
- tiṇai divisions;
- pāl / chapter hierarchy;
- அதிகாரம் / இயல் hierarchy;
- internal long-poem headings.

Mechanical navigation may be generated for usability but must never be described as ancient or source-printed structure.

## 11. Tolkāppiyam-specific rules

Tolkāppiyam is a grammatical work with hierarchy:

`work → அதிகாரம் → இயல் → நூற்பா`

Canonical records use `corpus/tolkappiyam/nurpas/`.

Do not force Tolkāppiyam into poem-oriented record terminology.

Keep separate:

- repository canonical ID;
- upstream semantic ID alias;
- source sequence;
- traditional/local numbering;
- source heading;
- editorial display heading.

Do not import Tolkāppiyam Arivagam web application code, explanations, glossary definitions, teaching tools, translations, modern linguistic equivalents, or UI metadata into the canonical corpus.

The website may consume future corpus exports; it is not the canonical preservation authority.

## 12. Combined manifest safety

The project previously encountered an invalid UTF-8 `poems.csv` caused by overlapping writers.

Never let parallel work generators append/write directly to a shared combined manifest.

Required shared-manifest model:

1. work-local generation;
2. one authoritative aggregator;
3. deterministic work/record order;
4. UTF-8 explicit encoding;
5. atomic temporary-file replacement;
6. lock/advisory concurrency protection;
7. validation before replacement;
8. byte-stable repeated generation.

Any concurrency change must preserve these guarantees.

## 13. Validation requirements for corpus work

At minimum run the established repository equivalents of:

```bash
python3 scripts/audit_repository.py --root .
pytest -q
python3 scripts/validate_output.py --work <work>
```

For corpus-wide/shared changes, validate every frozen work.

Required success conditions:

- physical audit passes;
- tests pass;
- validator errors = 0;
- source-output fidelity complete;
- source-note fidelity complete;
- canonical body drift = none for previously frozen works;
- raw-source drift = none;
- inventory drift = none;
- repeated generation is deterministic.

Warnings are acceptable only when they represent documented source conditions rather than parser failure.

## 14. Research-layer separation

All research outputs must remain derived and replaceable.

Preferred architecture:

`frozen corpus → evidence assertions → review events → entity resolution → relationships → analytical datasets`

Research outputs belong under `research/` or equivalent derived paths.

Never place inferred people, places, dynasties, modern geography, translations, themes, or historical conclusions inside frozen poem/nūṟpā YAML merely because they are useful for research.

## 15. Research evidence classes

Use controlled evidence classes and keep provenance separate from confidence.

R0 established classes including:

- `SOURCE_EXPLICIT`;
- `MECHANICALLY_DERIVED`;
- `CROSS_TEXT`;
- `EDITORIAL_INFERENCE`;
- reserved later classes for external history and interpretation.

A source-explicit string occurrence does not prove a modern historical identification.

Example:

A printed name in a poem may be `SOURCE_EXPLICIT` as a mention. The claim that it denotes a specific historically reconstructed individual is a separate assertion and may require external evidence.

## 16. Mention versus entity rules

A mention is a surface occurrence in a record.

An entity is a resolved research identity.

Do not automatically merge mentions because:

- they share the same printed form;
- they have similar normalised spelling;
- an epithet resembles another name;
- modern scholarship commonly equates them.

Entity resolution must be explicit, reviewable, reversible, and supported by assertion IDs.

Use uncertainty-friendly relations such as `POSSIBLY_SAME_AS` before asserting identity.

## 17. Review rules

Review history must be append-only.

Do not silently mutate an assertion to hide an earlier decision.

Use review events with:

- previous status;
- new status;
- reviewer identity/type;
- decision;
- timestamp;
- notes;
- supersession/rejection references where applicable.

Reserve `verified` for an explicit review decision.

Machine-assisted or assistant-assisted review must identify itself accurately; it must not pretend to be independent human verification.

## 18. R0 preservation rules

The existing R0 pilot contains deterministic research outputs derived from Puṟanāṉūṟu.

Do not regenerate it merely to change release labels.

Before porting R0 onto current `main`:

1. verify the Puṟanāṉūṟu canonical hashes used by R0 are unchanged between corpus 1.0.0 and 1.1.0;
2. preserve R0 assertion IDs;
3. preserve evidence spans;
4. preserve original source-release provenance;
5. create a compatibility record for the newer repository base;
6. rerun research validation and idempotence checks.

## 19. R1 review/entity-resolution design rules

R1 should focus on reviewability, not on producing large speculative historical graphs.

R1 should establish:

- reviewer model;
- append-only review event workflow;
- ambiguity queues;
- variant-form handling;
- entity-resolution states;
- merge/split/supersede rules;
- evidence requirements per decision type;
- deterministic exports;
- audit reports;
- clear boundary between reviewed and verified.

A small rigorously reviewed sample is better than mass automatic resolution.

## 20. External research rules

Do not use web or secondary scholarship to fill canonical gaps silently.

When external evidence is intentionally introduced later:

- cite the external source;
- record edition/publication details where possible;
- classify the assertion as external evidence;
- preserve the original corpus evidence separately;
- do not overwrite source-explicit fields;
- distinguish scholarly disagreement.

## 21. Modern geography

Do not assign modern latitude/longitude, districts, states, countries, archaeological sites, or modern spellings to ancient place mentions during source extraction.

Modern identification belongs in a separate research assertion with evidence and confidence.

## 22. Interpretation boundary

Counts of evidence assertions are not historical fact counts.

For example, 34 warfare-related evidence records do not establish 34 wars.

Do not turn extracted textual signals directly into conclusions about:

- state formation;
- caste;
- economy;
- religion;
- chronology;
- gender systems;
- polity;
- trade networks;
- ecology.

Those require later analytical methodology and evidence aggregation.

## 23. Rights and repository visibility

Consult `docs/source-rights-and-redistribution-review.md` before any visibility, redistribution, release-package, or public-download change.

Unresolved rights questions must not be bypassed because the technical repository is ready.

Do not make the repository public without an explicit separately authorised decision.

## 24. Documentation discipline

At the end of a substantial phase, update:

- `PROJECT_HANDOVER.md`;
- `PROJECT_GUIDELINES.md` only when rules changed;
- `NEXT_CHAT_PROMPT.md`;
- phase-specific manifest/status records;
- relevant README/docs;
- completion or blocker logs.

The handover must describe actual GitHub state, not intended state.

The next-chat prompt must instruct the next assistant to inspect live repository state before changing anything.

## 25. Commit discipline

Keep commits logically scoped.

Good boundaries include:

- source/provenance acquisition;
- parser/schema architecture;
- generated corpus outputs;
- validation/freeze;
- research schema;
- research data generation;
- review workflow;
- handover/documentation.

Do not mix unrelated corpus corrections with research-layer changes.

Do not commit caches, temporary files, editor backups, secrets, or local machine artefacts.

## 26. Blocker policy

Stop rather than guess when facing:

- uncertain canonical source identity;
- checksum mismatch;
- unexplained frozen drift;
- commentary/body boundary ambiguity;
- record-count ambiguity that changes canonical identity;
- conflicting editions with no documented selection basis;
- release-tag conflict;
- rights uncertainty requiring a policy decision;
- research entity merge unsupported by evidence.

When blocked, record:

- exact blocker;
- evidence inspected;
- files changed/not changed;
- safe resumption steps.

Then leave the repository in a stable auditable state.

## 27. Mandatory startup for future chats

Before changing the repository:

1. read `PROJECT_HANDOVER.md` completely;
2. read `PROJECT_GUIDELINES.md` completely;
3. read `NEXT_CHAT_PROMPT.md` completely;
4. inspect `main` and active research branches;
5. read release / protected-condition manifests relevant to the task;
6. compare repository state to the handover;
7. treat newer intentional commits as authoritative;
8. run or inspect baseline validations before writing.

Never restart completed source ingestion from scratch unless the live repository proves it is incomplete or corrupted.
