# Sangam Literature Corpus — Project Handover

## 1. Repository authority

This document is the continuity handover for the active repository:

- GitHub: `pugazg/sangam-literature-corpus`
- Default branch: `main`
- Repository visibility at the time of this handover: private
- Current `main` head inspected for this handover: `86704efea303f5a0d4b1fa6b5a5299a23b79e2f0`

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

At handover, GitHub exposes at least:

- `main`
- `research/sangam-evidence-r0`

The R0 research branch is important and is not yet integrated with current `main`.

Verified research branch commit recorded by the project:

`7087626347b56e0145ab69b2fb7ef355f6bc07d5d`

Branch relationship inspected at handover:

- merge base with current `main`: `272d9d5a79d55994e2c12efacc22be20b2c88030`
- R0 branch: one research commit ahead of that merge base
- R0 branch: three commits behind current `main`

Those three `main`-side commits include the Tolkāppiyam 1.1.0 corpus work, its release checkpoint, and the later publication-status documentation.

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

## 10. Planned research roadmap

The previously agreed research sequence is:

- R0 — research architecture + Puṟanāṉūṟu evidence pilot — implemented on the R0 branch
- R1 — review workflow + entity-resolution rules
- R2 — evidence extraction across all nine core Sangam works
- R3 — cross-work poets, rulers, places, and relationships
- R4 — economy, ecology, society, and political datasets
- R5 — maps, timelines, search, and visual research interface
- R6 — extend the derived research layer to Patiṉeṇkīḻkkaṇakku

Tolkāppiyam should later participate through a separate grammatical/concept evidence stream; do not force grammatical நூற்பா into poem-oriented research types.

## 11. Immediate next activity

The next chat should not restart corpus extraction.

The next activity is:

### R0 reconciliation → R1 foundation

1. inspect current `main` and `research/sangam-evidence-r0` from GitHub;
2. verify exact branch heads and compare them;
3. establish current corpus 1.1.0 as the working base without moving release checkpoints;
4. verify Puṟanāṉūṟu hashes are unchanged from R0's 1.0.0 source release;
5. create a new research continuation branch from current `main`, preferably `research/sangam-evidence-r1`;
6. port the single R0 research commit/diff onto that branch while preserving current 1.1.0 corpus documentation;
7. run the research validator and full frozen-corpus regressions;
8. confirm all R0 deterministic assertion IDs and counts remain unchanged;
9. document the compatibility result;
10. begin R1: review workflow and entity-resolution rules.

Do not merge R0 blindly into `main` if the README or release documentation conflicts. The current 1.1.0 corpus documentation wins; the R0 research additions must be reconciled around it.

## 12. R1 design intent

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

## 13. Rights / visibility note

`docs/source-rights-and-redistribution-review.md` contains unresolved questions. Do not make a visibility or redistribution-policy change merely because GitHub access now works.

Repository visibility changes require a separate explicit decision after the rights review is resolved.

## 14. Mandatory files to read in a new chat

Before making changes, read at minimum:

1. `PROJECT_HANDOVER.md`
2. `PROJECT_GUIDELINES.md`
3. `NEXT_CHAT_PROMPT.md`
4. `README.md`
5. `docs/classical-tamil-corpus-release-1.1.0.md`
6. `manifests/classical-tamil-corpus-release-1.1.0.json`
7. `manifests/repository-protected-conditions-1.1.0.json`
8. `docs/manifest-ordering-policy.md`
9. `docs/source-rights-and-redistribution-review.md`
10. `corpus/tolkappiyam/metadata.json`
11. on the R0 branch: `docs/classical-tamil-research-layer.md`
12. on the R0 branch: `manifests/classical-tamil-research-program.json`
13. on the R0 branch: `research/README.md`
14. on the R0 branch: `research/reports/purananuru-extraction-summary.json`
15. on the R0 branch: R0 decisions, baseline, idempotence, and frozen-regression logs

Then inspect the live branches and commits. Repository state is authoritative over this document if later commits intentionally supersede it.

## 15. Definition of safe continuation

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
- any new inference remains outside `SOURCE_EXPLICIT` canonical metadata.

## 16. End-state expected from the next research phase

The next phase should leave:

- current corpus 1.1.0 intact;
- Tolkāppiyam intact;
- R0 safely reconciled onto a current-main-derived research branch;
- a documented compatibility record between R0 source inputs and corpus 1.1.0;
- R1 review/entity-resolution architecture implemented and validated;
- no false promotion of candidate mentions to verified historical entities;
- updated handover, guidelines, and next-chat prompt before handing off again.
