# Sangam Literature Corpus — Project Handover

## 1. Repository authority

This document is the continuity handover for the active repository:

- GitHub: `pugazg/sangam-literature-corpus`
- Default branch: `main`
- Repository visibility at the time of this handover: private
- Pre-update `main` state inspected before this handover revision included the completed 1.1.0 corpus release and the project continuity documents.

Treat the live GitHub repository, its current branches, commits, manifests, freeze records, and source artifacts as authoritative over stale local paths, earlier chat summaries, or historical prompt text.

Do not resume work from the former repository name `pugazg/classical-tamil`. The active project repository is `pugazg/sangam-literature-corpus`.

## 2. Project purpose

The repository is a source-preservation and provenance platform for classical Tamil texts. It is not a corrected critical edition.

The governing hierarchy is:

1. preserved source artifacts;
2. source-faithful canonical transcription;
3. source-explicit metadata;
4. deterministic validation and anomaly reporting;
5. isolated apparatus / external evidence;
6. independently versioned derived research layers.

Frozen canonical text must never be silently modernised, corrected, reconstructed, translated, interpreted, or overwritten by later research.

The long-term research goal is broader than keyword tagging. It is to construct an evidence-backed, multidimensional research model of the world represented in Classical Tamil literature: Akam/Puram, tiṇai and tuṟai, five landscapes, ecology, food, occupations, trade, material culture, family, relationships, society, polity, warfare, ritual, arts, mobility, settlements, values, and other aspects of lived experience.

The authoritative research-concept plan is documented in:

`docs/CLASSICAL_TAMIL_RESEARCH_MATRIX.md`

That document must be read before designing or extending R2 and later research extraction.

## 3. Frozen corpus status

The current repository release is Classical Tamil Corpus `1.1.0`.

Verified release manifest facts:

- frozen works: 28
- canonical records: 7,234
- poem records: 5,632
- Tolkāppiyam நூற்பா records: 1,602
- repository fingerprint: `4ca530d3a836341b5abaa395af97cf7307529ced04dd40dec17b1a010949abca`
- release content commit: `89e75678b4c35401801a0052ecb8a495d1805dd5`
- release checkpoint commit: `51c65b36d07ecf604c11d8cc6399ad40ab7e7086`
- release identity: `classical-tamil-corpus-v1.1.0`
- previous release identity: `classical-tamil-corpus-v1.0.0`

The earlier 1.0.0 checkpoint contains 27 works and 5,632 canonical numbered records. The 1.1.0 checkpoint adds Tolkāppiyam without changing the earlier frozen works.

Before relying on a remote Git tag, verify the live Git ref. The release identities above are authoritative release records; do not move or recreate an existing release tag.

## 4. Corpus programmes completed

### 4.1 Core Sangam corpus

Nine repository works are complete and frozen:

- Naṟṟiṇai
- Aiṅkuṟunūṟu
- Kuruntokai
- Akanāṉūṟu
- Puṟanāṉūṟu
- Pattuppāṭṭu
- Patiṟṟuppattu
- Paripāṭal
- Kalittokai

Programme total: 2,376 canonical records.

### 4.2 Patiṉeṇkīḻkkaṇakku

All eighteen selected works are complete and frozen:

- Tirukkural
- Nālāṭiyār
- Nāṉmaṇikkaṭigai
- Iṉṉā Nāṟpatu
- Iṉiyavai Nāṟpatu
- Kār Nāṟpatu
- Kaḷavaḻi Nāṟpatu
- Aintiṇai Aimpathu
- Aintiṇai Eḻupathu
- Tiṇaimālai Nūṟṟaimpatu
- Tiṇaimoḻi Aimpathu
- Tirikaṭukam
- Ācārakkōvai
- Paḻamoḻi Nāṉūṟu
- Ciṟupañcamūlam
- Mutumoḻik Kāñci
- Ēlāti
- Kainnilai

Programme total: 3,256 canonical numbered records.

`முப்பால்` is an alias of Tirukkural, not a separate nineteenth work. `கைந்நிலை` is the selected eighteenth-work tradition; `இன்னிலை` is not a canonical nineteenth work in this repository.

### 4.3 Tolkāppiyam

Tolkāppiyam is independently frozen at work schema `1.0.0`.

Canonical source and provenance:

- Project Madurai ID: `pmuni0100`
- source path: `sources/raw-html/tolkappiyam-pmuni0100.html`
- source bytes: 384,080
- source SHA-256: `16b2edf314763ef491bdc498c0017de33e7e190753587b230bbafcd03219f5da`
- upstream reference repository: `pugazg/tolkappiyam-arivagam`
- pinned upstream commit: `16123f742503283e46f0ed321802a46f99df6392`

Verified structure:

- 3 அதிகாரம்
- 27 இயல்
- 1,602 நூற்பா
- 1,597 high-confidence
- 5 medium-confidence
- 0 low-confidence
- 12 independently reviewed parser/source warnings

Canonical records live in `corpus/tolkappiyam/nurpas/`. Repository IDs are kept distinct from upstream semantic-ID aliases. The Tolkāppiyam Arivagam web application remains a separate specialised application; its UI code, explanations, glossaries, teaching tools, and analysis fields are not canonical corpus data.

## 5. Important source conditions that must remain protected

The repository intentionally preserves irregular source evidence rather than making titles and counts look conventional. Examples include:

- Naṟṟiṇai source-loss/lacuna conditions;
- Aiṅkuṟunūṟu source-lost records and பத்து inventory;
- Kuruntokai attribution/layout irregularities;
- Akanāṉūṟu printed numbering anomalies and three printed macro-divisions;
- Puṟanāṉūṟu source-lost records 267–268, bare heading 99, printed dot-sequence conditions, and its explicitly approved text-export provenance;
- Pattuppāṭṭu multi-source provenance, Mullai commentary isolation, Tirumurukāṟṟuppaṭai internal structure, and three declared/extracted line-count discrepancies;
- Patiṟṟuppattu surviving records 11–90 and explicit first/tenth பத்து losses;
- Paripāṭal main-poem / திரட்டு distinction and restarted printed numbering;
- Kalittokai printed lacunae in records 114 and 131;
- Aintiṇai Eḻupathu source-lost records 25, 26, 69, 70;
- Tiṇaimālai Nūṟṟaimpatu 153 printed records despite the nominal 150 title;
- Tirikaṭukam absent printed headings 43 and 57;
- Ācārakkōvai missing heading 47 and anomalous punctuation;
- Paḻamoḻi Nāṉūṟu 399 numbered records, two unnumbered opening texts, and absent chapter ordinal 12;
- Kainnilai only four source-printed tiṇai headings;
- Tolkāppiyam source/editorial heading separation and all 12 confirmed warning conditions.

Always consult the work-specific metadata, validation report, apparatus, protected-condition manifest, and freeze log before changing shared infrastructure.

## 6. Deterministic manifest protection

A prior overlapping write corrupted `manifests/poems.csv` during release preparation. No canonical corpus content was damaged.

The repository now has a deterministic combined-manifest policy:

- authoritative work order;
- canonical record order inside each work;
- deterministic tie-breaks;
- UTF-8 deterministic serialisation;
- atomic replacement;
- filesystem synchronisation where implemented;
- advisory locking for shared aggregation;
- no parallel append/write to shared combined manifests.

The approved deterministic `poems.csv` SHA-256 for release 1.1.0 remains inherited from the verified corpus state: `4c287ee9901d028f97659b3a099bd521efc7d43819424b32184c975de9bf4cb7`.

Do not reintroduce concurrent shared-manifest writers.

## 7. Current Git branches

GitHub exposes at least:

- `main`
- `research/sangam-evidence-r0`

The R0 research branch is important and is not yet integrated with current `main`.

Verified research branch commit recorded by the project:

`7087626347b56e0145ab69b2fb7ef355f6bc07d5d`

The previously inspected branch relationship was:

- merge base with then-current `main`: `272d9d5a79d55994e2c12efacc22be20b2c88030`
- R0 branch: one research commit ahead of that merge base
- R0 branch: three corpus/release commits behind the then-current `main`

Since durable documentation commits have been added after that comparison, always re-run the live branch comparison before acting.

Do not overwrite either side of this divergence.

## 8. Classical Tamil Research Layer — R0 status

The derived research programme is intentionally separate from the frozen corpus.

Programme identity on `research/sangam-evidence-r0`:

- programme: `classical-tamil-research-layer`
- phase: R0
- phase name: Research Architecture and Puṟanāṉūṟu Evidence Pilot
- research schema: `0.1.0`
- status: `pilot`
- pilot work: Puṟanāṉūṟu
- records processed: 400
- literary bodies processed: 398
- source-lost records: 267 and 268

R0 output summary:

- assertions: 2,867
- mention candidates: 285
- pilot entity records: 43
- pilot relationships: 51
- evidence class in R0 assertions: 2,867 `SOURCE_EXPLICIT`
- machine-checked assertions: 2,582
- human-review-required assertions: 285
- external historical assertions: 0
- interpretation assertions: 0

Important source-explicit assertion counts include:

- poet attribution: 386
- patron/addressee: 233
- tiṇai: 386
- tuṟai: 386
- source-context note: 791
- textual condition: 400
- warfare mention: 34
- gift mention: 32
- fauna mention: 79
- flora mention: 21

These are evidence-record counts, not resolved historical fact counts.

R0 correctly keeps mentions separate from resolved entities and keeps append-only review events separate from assertion generation.

## 9. R0 provenance caveat after corpus 1.1.0

R0 was built against the immutable Classical Tamil Corpus `1.0.0` release before Tolkāppiyam was added.

Do not rewrite R0 assertion provenance merely because current `main` is release 1.1.0.

The correct next integration procedure is:

1. verify that every Puṟanāṉūṟu canonical input hash used by R0 is unchanged between the 1.0.0 and 1.1.0 corpus checkpoints;
2. preserve each R0 assertion ID and its original canonical hashes;
3. record a compatibility / non-drift result showing that the R0 pilot remains valid against current `main`;
4. integrate the research work onto a branch based on current `main` without modifying frozen corpus files;
5. only then begin R1.

Do not globally change the R0 `source_release_tag` field and regenerate assertion IDs just to make metadata look current.

## 10. Research concept matrix — mandatory methodological layer

The project now has an explicit concept-matrix specification:

`docs/CLASSICAL_TAMIL_RESEARCH_MATRIX.md`

This is not optional background reading. It defines the intended observation model before bulk R2 extraction.

The matrix makes the following first-class research dimensions:

- Akam / Puram literary domain;
- tiṇai and tuṟai;
- five landscapes: Kuṟiñci, Mullai, Marutam, Neytal, Pālai;
- exceptional Akam categories such as Kaikkilai and Peruntiṇai when evidence supports them;
- terrain, water, season, time, flora, fauna;
- people, social roles, family, gender, kinship, relationships;
- occupations, production, food, subsistence, trade, economy, gifts, wealth;
- clothing, ornament, material culture, weapons, transport, settlements;
- kingship, polity, diplomacy, warfare;
- religion, ritual, death, mourning, memorialisation;
- music, dance, performance, arts;
- knowledge, technology, body, health, values;
- named entities and cross-text relationships.

The matrix is assertion-backed. A populated matrix cell must trace to exact evidence, not to an unsupported boolean tag.

For example, do not reduce a poem to `elephant = true`. Preserve exact printed form, record, evidence span, evidence class, confidence, review status, and assertion ID; derive matrix views from those records.

Source silence is not historical absence.

## 11. Akam / Puram and landscape evidence rules

Akam/Puram must be represented with evidence basis, not just a boolean.

Repository-appropriate values should distinguish:

- source-explicit classification;
- work-level classification;
- Tolkāppiyam concept mapping;
- derived/editorial classification;
- uncertain / not applicable.

The same rule applies to tiṇai and tuṟai.

The five landscapes must not be reduced to one-word terrain mappings. The research concept model should be able to connect each landscape, where evidence supports it, to:

- terrain/environment;
- season and time;
- flora and fauna;
- occupations;
- food/subsistence;
- settlements;
- mobility;
- social actors;
- emotional/relational situations;
- ritual/deity references;
- characteristic objects and activities.

Conventional textbook associations must not be written into poem records as source facts.

## 12. Tolkāppiyam's future research role

Tolkāppiyam is not merely a twenty-eighth frozen text. It should later provide a separate grammatical / poetics concept evidence stream.

The intended relationship is:

```text
Tolkāppiyam நூற்பா
      ↓
grammatical / poetic concept assertion
      ↓
controlled concept registry
      ↓
comparison with Sangam poem evidence
```

A Tolkāppiyam rule must not automatically rewrite a poem's classification.

The project should eventually support evidence-backed questions such as:

> How closely does surviving Sangam poetic usage correspond to, differ from, or exceed the conceptual system represented in Tolkāppiyam?

This is why Tolkāppiyam ↔ Sangam mapping is now planned as a distinct later phase rather than being mixed casually into R2.

## 13. Revised research roadmap

The formal roadmap is now:

### R0 — Research architecture + Puṟanāṉūṟu evidence pilot

Status: implemented on the R0 branch.

### R1 — Review workflow + entity-resolution rules

Immediate next phase after R0 reconciliation.

Establish append-only review events, reviewer identity/type, ambiguity queues, variant-form handling, possible/reviewed/verified identity states, and reversible merge/split/reject/supersede decisions.

Do not attempt mass historical resolution.

### R1.5 — Classical Tamil Concept Matrix and Ontology Foundation

Mandatory before R2.

Formalise:

- Akam/Puram evidence rules;
- tiṇai/tuṟai evidence rules;
- five-landscape concept families;
- concept registry and IDs;
- ecology, material culture, economy, society, polity, ritual, arts, everyday-life dimensions;
- claim/evidence classes including a separate Tolkāppiyam grammatical-concept stream;
- deterministic assertion-backed matrix views;
- Puṟanāṉūṟu matrix pilot.

R2 must not begin until R1.5 passes validation.

### R2 — Apply the concept matrix across all nine core Sangam works

Perform comparable evidence extraction across the nine frozen core Sangam works while retaining work-specific metadata differences and exact provenance.

### R3 — Cross-corpus entity resolution and relationships

Resolve poets, rulers, chiefs, patrons, addressees, places, polities, communities, variant names, epithets, and cross-work relationships through reviewed evidence.

### R4 — Civilisation datasets

Build evidence-backed datasets for landscapes/ecology, food/subsistence, occupations, production, economy, trade, material culture, settlements, mobility, society, kinship/gender, polity, warfare, religion/ritual, death/memory, arts/performance, knowledge/technology, values, and lived experience.

Evidence-record counts must remain distinct from historical event/fact counts.

### R5 — Research experience

Build matrix exploration, cross-text search, maps, timelines, networks, entity pages, tiṇai atlas, landscape explorer, evidence drill-down, and reproducible exports.

Every visualisation must be traceable to source assertions.

### R6 — Extend the derived layer to Patiṉeṇkīḻkkaṇakku

Apply compatible research concepts to the eighteen frozen works while allowing didactic/ethical models appropriate to those texts. Do not force Sangam poem categories onto structurally different works.

### R7 — Tolkāppiyam ↔ Sangam conceptual mapping

Build a separate grammatical/poetics concept stream from Tolkāppiyam and compare it with poem evidence without rewriting canonical classifications.

### R8 — External scholarship and historical-identification layer

Add modern place identifications, chronology proposals, historical person resolution, archaeology, botanical/zoological identifications, and broader interpretation only with explicit external citations, confidence, review status, and disagreement handling.

## 14. Immediate next activity

The next chat should not restart corpus extraction and should not begin R2.

The next activity is:

### R0 reconciliation → R1 foundation

1. inspect current `main` and `research/sangam-evidence-r0` from GitHub;
2. verify exact branch heads and compare them;
3. establish current corpus 1.1.0 as the working base without moving release checkpoints;
4. verify Puṟanāṉūṟu hashes are unchanged from R0's 1.0.0 source release;
5. create a new research continuation branch from current `main`, preferably `research/sangam-evidence-r1`;
6. port the R0 research diff onto that branch while preserving current 1.1.0 corpus documentation;
7. run the research validator and full frozen-corpus regressions;
8. confirm all R0 deterministic assertion IDs and counts remain unchanged;
9. document the compatibility result;
10. begin R1: review workflow and entity-resolution rules.

Do not merge R0 blindly into `main` if README or release documentation conflicts. Current corpus documentation wins; R0 research additions must be reconciled around it.

After R1 is complete, the next mandatory phase is R1.5, not R2.

## 15. R1 design intent

R1 should improve reviewability without converting machine extraction into false historical certainty.

Required principles:

- mentions are not entities;
- same printed form does not prove same historical person/place;
- variant spellings are not automatically merged;
- `SOURCE_EXPLICIT` describes the occurrence/evidence, not the truth of an inferred historical identity;
- review events are append-only;
- rejected/superseded assertions remain auditable;
- `verified` requires an explicit review decision;
- machine-assisted review must identify itself as such;
- no modern geography, chronology, biography, dynasty assignment, or external historical claim enters R1 without a separately cited evidence class;
- canonical corpus files remain untouched.

R1 must be designed so that R1.5 can attach reviewed concept classifications without mutating the original R0 evidence assertions.

## 16. R1.5 design intent

R1.5 should answer, before bulk extraction:

- What exactly are we observing?
- What evidence is sufficient to populate each concept family?
- Which concepts are source-explicit, mechanically derived, Tolkāppiyam-based, editorial/derived, external, or interpretive?
- How are Akam/Puram and tiṇai/tuṟai represented without hiding provenance?
- How are five-landscape associations represented without hard-coding conventional assumptions?
- How are people/entities kept distinct from roles and concepts?
- How does every matrix cell point back to assertions and exact source spans?

The complete design is in `docs/CLASSICAL_TAMIL_RESEARCH_MATRIX.md`.

## 17. Rights / visibility note

`docs/source-rights-and-redistribution-review.md` contains unresolved questions. Do not make a visibility or redistribution-policy change merely because GitHub access works.

Repository visibility changes require a separate explicit decision after the rights review is resolved.

## 18. Mandatory files to read in a new chat

Before making changes, read at minimum:

1. `PROJECT_HANDOVER.md`
2. `PROJECT_GUIDELINES.md`
3. `NEXT_CHAT_PROMPT.md`
4. `docs/CLASSICAL_TAMIL_RESEARCH_MATRIX.md`
5. `README.md`
6. `docs/classical-tamil-corpus-release-1.1.0.md`
7. `manifests/classical-tamil-corpus-release-1.1.0.json`
8. `manifests/repository-protected-conditions-1.1.0.json`
9. `docs/manifest-ordering-policy.md`
10. `docs/source-rights-and-redistribution-review.md`
11. `corpus/tolkappiyam/metadata.json`
12. on the R0 branch: `docs/classical-tamil-research-layer.md`
13. on the R0 branch: `manifests/classical-tamil-research-program.json`
14. on the R0 branch: `research/README.md`
15. on the R0 branch: `research/reports/purananuru-extraction-summary.json`
16. on the R0 branch: R0 decisions, baseline, idempotence, and frozen-regression logs

Then inspect live branches and commits. Repository state is authoritative over this document if later commits intentionally supersede it.

## 19. Definition of safe continuation

A continuation is safe only if:

- no existing frozen canonical body changes;
- no source-note changes;
- no raw-source changes;
- no release tag/ref is moved;
- R0 assertion IDs and evidence spans remain reproducible;
- all current tests pass;
- all current validators pass;
- research validation passes;
- deterministic regeneration is byte-stable;
- shared manifests remain concurrency-safe;
- any new inference remains outside source-explicit canonical metadata;
- concept/matrix outputs remain derived and assertion-backed.

## 20. End-state expected from the next research phase

The next phase should leave:

- current corpus 1.1.0 intact;
- Tolkāppiyam intact;
- R0 safely reconciled onto a current-main-derived research branch;
- a documented compatibility record between R0 source inputs and corpus 1.1.0;
- R1 review/entity-resolution architecture implemented and validated;
- no false promotion of candidate mentions to verified historical entities;
- the R1.5 concept-matrix phase explicitly queued as the next mandatory research phase;
- updated handover, guidelines, research manifest/decision log, and next-chat prompt before handing off again.
