# Sangam Literature Corpus — Project Working Guidelines

## 1. Authority and scope

The active repository is `pugazg/sangam-literature-corpus`.

Treat live GitHub state as authoritative. Historical chat summaries, local absolute paths, earlier repository names, and old prompt text are secondary evidence only.

This repository contains two conceptually different layers:

1. the frozen preservation corpus;
2. independently versioned derived research layers.

Never blur them.

The authoritative concept-matrix design for later research is:

`docs/CLASSICAL_TAMIL_RESEARCH_MATRIX.md`

R1.5 is the accepted concept-matrix foundation. Read this specification before designing R2 or any later matrix/ontology extraction, and preserve the R1.5 evidence/provenance boundary unless a versioned change is explicitly approved.

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
- grammatical/concept evidence;
- external evidence;
- interpretation.

Only canonical literary text and source-explicit metadata belong in the canonical preservation layer as source content/metadata.

Mechanically derived values must be labelled as such.

External evidence can never overwrite canonical text.

Tolkāppiyam concept evidence can inform derived research but must not silently rewrite poem metadata.

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

For research, Tolkāppiyam must use a separate grammatical/poetics concept evidence stream. A நூற்பா-based concept assertion must not be treated as if it were a poem-level source classification.

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

`frozen corpus → evidence assertions → review events → concept classification / entity resolution → relationships → analytical datasets → visual research views`

Research outputs belong under `research/` or equivalent derived paths.

Never place inferred people, places, dynasties, modern geography, translations, themes, historical conclusions, or concept-matrix assignments inside frozen poem/nūṟpā YAML merely because they are useful for research.

## 15. Research evidence classes

Use controlled evidence classes and keep provenance separate from confidence.

R0 established classes including:

- `SOURCE_EXPLICIT`;
- `MECHANICALLY_DERIVED`;
- `CROSS_TEXT`;
- `EDITORIAL_INFERENCE`;
- reserved later classes for external history and interpretation.

The later matrix/ontology work should add a clearly separate repository-appropriate class such as `GRAMMATICAL_CONCEPT_EVIDENCE` for Tolkāppiyam-based conceptual evidence.

A source-explicit string occurrence does not prove a modern historical identification.

Example:

A printed name in a poem may be `SOURCE_EXPLICIT` as a mention. The claim that it denotes a specific historically reconstructed individual is a separate assertion and may require external evidence.

Similarly, a Tolkāppiyam statement about a tiṇai is not automatically a source-explicit classification of every poem associated with that tiṇai.

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

## 17. Concept versus entity rules

Concept identity and entity identity are different problems.

Examples:

- `முல்லை` as a printed lexical occurrence;
- Mullai as a source-printed tiṇai classification;
- Mullai as a controlled research concept;
- Mullai-related terrain/flora/fauna associations;
- a place or plant entity whose surface form happens to overlap with a concept label.

Do not collapse these merely because labels match.

Every controlled concept must have a stable concept ID and every application of that concept must cite assertions.

## 18. Review rules

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

## 19. Akam / Puram rules

Akam/Puram must be a first-class research dimension with explicit evidence basis.

Do not store only `akam: true` or `puram: true` in derived data without indicating why.

Distinguish at minimum:

- source-explicit classification;
- work-level classification;
- Tolkāppiyam concept mapping;
- derived/editorial classification;
- uncertain / not applicable.

A matrix view may combine these for analysis only when the contributing evidence classes remain inspectable.

## 20. Tiṇai / Tuṟai and five-landscape rules

The research layer must support:

- குறிஞ்சி / Kuṟiñci;
- முல்லை / Mullai;
- மருதம் / Marutam;
- நெய்தல் / Neytal;
- பாலை / Pālai;
- கைக்கிளை / Kaikkilai and பெருந்திணை / Peruntiṇai where evidence requires them.

Do not infer tiṇai or tuṟai from conventional expectations when the selected source does not print it.

Do not reduce landscape concepts to one-word terrain definitions.

The concept matrix may connect a landscape to terrain, season/time, flora, fauna, occupations, food/subsistence, settlement, social actors, emotional/relational situations, mobility, ritual references, and characteristic objects **only through explicitly classified evidence**.

Conventional textbook associations are not source facts unless supported by an appropriate evidence stream.

## 21. Research matrix dimensions

The planned matrix must support, at minimum:

- literary domain: Akam/Puram;
- tiṇai / tuṟai;
- landscape/environment;
- season/weather/time;
- flora;
- fauna;
- people and social roles;
- relationships;
- emotion/lived experience;
- occupations and production;
- food and subsistence;
- clothing, ornaments, adornment;
- material culture and everyday objects;
- weapons and warfare;
- mobility and transport;
- settlements and built environment;
- economy;
- trade and exchange;
- polity and political life;
- communities/social groups;
- family/gender/kinship;
- religion/ritual;
- death/mourning/memory;
- arts/music/performance;
- knowledge/technology;
- values/ethical concepts;
- body/health;
- named entities;
- textual/intertextual relationships.

The detailed specification lives in `docs/CLASSICAL_TAMIL_RESEARCH_MATRIX.md`.

## 22. Evidence-first matrix rule

A matrix is a derived view over assertions.

Never manually populate a matrix cell without an evidence chain.

Required chain:

`matrix cell → assertion ID → exact record → exact evidence span/source field → canonical record hash → frozen source provenance`

For derived/external claims, continue the chain to review events and external citations.

Empty matrix cells mean no qualifying assertion currently exists. They do **not** prove historical absence.

## 23. R0 preservation rules

The existing R0 pilot contains deterministic research outputs derived from Puṟanāṉūṟu.

Do not regenerate it merely to change release labels.

Before porting R0 onto current `main`:

1. verify the Puṟanāṉūṟu canonical hashes used by R0 are unchanged between corpus 1.0.0 and 1.1.0;
2. preserve R0 assertion IDs;
3. preserve evidence spans;
4. preserve original source-release provenance;
5. create a compatibility record for the newer repository base;
6. rerun research validation and idempotence checks.

## 24. R1 review/entity-resolution design rules

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

R1 must leave the R0 evidence assertions stable and create an architecture onto which R1.5 concept classification can be added without rewriting those assertions.

## 25. R1.5 concept-matrix rules

R1.5 is mandatory before R2.

It must establish:

- a versioned concept registry;
- Akam/Puram evidence rules;
- tiṇai/tuṟai evidence rules;
- five-landscape concept families;
- concept hierarchy and IDs;
- explicit evidence requirements for each concept family;
- a separate Tolkāppiyam grammatical/poetics concept stream;
- assertion-backed matrix generation;
- deterministic matrix exports;
- validation for orphan concepts/assertions/relationships;
- a Puṟanāṉūṟu matrix pilot.

Do not begin R2 until R1.5 is validated.

## 26. Revised research roadmap

The formal roadmap is:

- R0 — research architecture + Puṟanāṉūṟu pilot — implemented;
- R1 — review workflow + entity-resolution rules — immediate next phase;
- R1.5 — Classical Tamil Concept Matrix / ontology foundation — mandatory before R2;
- R2 — apply the concept matrix across all nine core Sangam works;
- R3 — cross-corpus poets, rulers, chiefs, places, communities, and relationships;
- R4 — civilisation datasets: ecology, food, economy, trade, material culture, society, gender/kinship, polity, warfare, ritual, arts, knowledge, values, daily life;
- R5 — matrix explorer, maps, timelines, networks, search, tiṇai atlas, evidence drill-down;
- R6 — extend compatible derived research to Patiṉeṇkīḻkkaṇakku;
- R7 — Tolkāppiyam ↔ Sangam grammatical/concept mapping;
- R8 — external scholarship / modern historical-identification layer.

Do not skip phases merely because extraction can be automated.

## 27. External research rules

Do not use web or secondary scholarship to fill canonical gaps silently.

When external evidence is intentionally introduced later:

- cite the external source;
- record edition/publication details where possible;
- classify the assertion as external evidence;
- preserve the original corpus evidence separately;
- do not overwrite source-explicit fields;
- distinguish scholarly disagreement.

R8 is the intended major phase for systematic external historical identification, though smaller explicitly classified external-evidence tasks may be approved earlier when methodologically necessary.

## 28. Modern geography

Do not assign modern latitude/longitude, districts, states, countries, archaeological sites, or modern spellings to ancient place mentions during source extraction.

Modern identification belongs in a separate research assertion with evidence and confidence.

## 29. Interpretation boundary

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

Likewise, absence of an assertion is not evidence that a social practice, species, object, or institution was absent historically.

## 30. Rights and repository visibility

Consult `docs/source-rights-and-redistribution-review.md` before any visibility, redistribution, release-package, or public-download change.

Unresolved rights questions must not be bypassed because the technical repository is ready.

Do not make the repository public without an explicit separately authorised decision.

## 31. Documentation discipline

At the end of a substantial phase, update:

- `PROJECT_HANDOVER.md`;
- `PROJECT_GUIDELINES.md` only when rules changed;
- `NEXT_CHAT_PROMPT.md`;
- `docs/CLASSICAL_TAMIL_RESEARCH_MATRIX.md` when the concept model changes;
- phase-specific manifest/status records;
- relevant README/docs;
- completion or blocker logs.

The handover must describe actual GitHub state, not intended state.

The next-chat prompt must instruct the next assistant to inspect live repository state before changing anything.

## 32. Commit discipline

Keep commits logically scoped.

Good boundaries include:

- source/provenance acquisition;
- parser/schema architecture;
- generated corpus outputs;
- validation/freeze;
- research schema;
- research data generation;
- review workflow;
- concept-matrix/ontology changes;
- handover/documentation.

Do not mix unrelated corpus corrections with research-layer changes.

Do not commit caches, temporary files, editor backups, secrets, or local machine artefacts.

## 33. Blocker policy

Stop rather than guess when facing:

- uncertain canonical source identity;
- checksum mismatch;
- unexplained frozen drift;
- commentary/body boundary ambiguity;
- record-count ambiguity that changes canonical identity;
- conflicting editions with no documented selection basis;
- release-tag conflict;
- rights uncertainty requiring a policy decision;
- research entity merge unsupported by evidence;
- concept classification whose evidence basis cannot be stated;
- landscape association that would require silently converting convention into source fact.

When blocked, record:

- exact blocker;
- evidence inspected;
- files changed/not changed;
- safe resumption steps.

Then leave the repository in a stable auditable state.

## 34. Mandatory startup for future chats

Before changing the repository:

1. read `PROJECT_HANDOVER.md` completely;
2. read `PROJECT_GUIDELINES.md` completely;
3. read `NEXT_CHAT_PROMPT.md` completely;
4. read `docs/CLASSICAL_TAMIL_RESEARCH_MATRIX.md` completely;
5. inspect `main` and active research branches;
6. read release / protected-condition manifests relevant to the task;
7. compare repository state to the handover;
8. treat newer intentional commits as authoritative;
9. run or inspect baseline validations before writing.

Never restart completed source ingestion from scratch unless the live repository proves it is incomplete or corrupted.

<!-- R1_REVIEW_WORKFLOW_COMPLETE_20260818 -->
## R1 review and identity-resolution rules

- R0 assertions remain immutable evidence records at schema `0.1.0`; workflow
  evolution must not rewrite their IDs, spans, source hashes, or evidence text.
- `review-events.ndjson` is append-only. `reviewed` requires an explicit event;
  `verified` requires a stronger explicit verification decision.
- Reviewer identity and type must be recorded accurately. `machine_checked` and
  `assistant_assisted` are not independent human verification.
- Entity-resolution decisions must cite supporting assertion IDs. Exact printed
  or normalized form equality may support `possible_match` but never an
  automatic merge or verified historical identity.
- Rejected, split, merged, and superseded decisions remain auditable; history is
  never silently deleted.
- Deterministic derived exports exclude execution timestamps. Primary event
  timestamps remain only where semantically required.
