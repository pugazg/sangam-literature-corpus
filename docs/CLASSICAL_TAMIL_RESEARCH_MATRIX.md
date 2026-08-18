# Classical Tamil Research Matrix

## 1. Purpose

This document defines the evidence-backed conceptual model for the derived Classical Tamil Research Layer.

The frozen corpus remains authoritative source evidence. The matrix is derived research output and must never be written back into canonical poem or நூற்பா records merely because a classification is useful.

Current implementation boundary: **R1.5 concept schema `0.3.0` on PR #3, open/draft/unmerged. R2 has not started.**

## 2. Architecture

```text
Frozen canonical corpus
        ↓
Source-grounded evidence assertions
        ↓
Review events and ambiguity queues
        ↓
Concept classification / entity resolution
        ↓
Cross-record and cross-work relationships
        ↓
Research matrices and analytical datasets
        ↓
Later maps, timelines, networks, search, visualisation, interpretation
```

A matrix cell is a view over evidence-backed observations, not an unsupported boolean historical fact.

Preferred observation shape:

```yaml
concept_id: <stable controlled concept>
work_id: <work>
record_id: <record>
surface_form: <exact printed form>
evidence_span: <exact span>
evidence_class: <controlled class>
classification_basis: <controlled basis>
confidence: <controlled value>
review_status: <controlled value>
supporting_assertion_ids: []
```

Empty cells mean only that qualifying evidence is not currently recorded. Source silence is never automatic historical absence.

## 3. Claim classes

Keep claim type separate from confidence, review state, and identity state.

Controlled classes include:

- `SOURCE_EXPLICIT`
- `MECHANICALLY_DERIVED`
- `CROSS_TEXT`
- `EDITORIAL_INFERENCE`
- `GRAMMATICAL_CONCEPT_EVIDENCE`
- `EXTERNAL_HISTORICAL`
- `INTERPRETATION`

Do not silently upgrade one class into another.

Examples:

- a poem literally contains `முல்லை` → source-explicit lexical evidence;
- source metadata classifies a record → source-explicit classification evidence;
- features resemble a conventional tiṇai pattern without source classification → explicit editorial/derived claim only;
- a Tolkāppiyam நூற்பா defines a concept → grammatical/poetics concept evidence;
- modern place or identity reconstruction → external evidence, never source-explicit by default.

## 4. Source terminology

`docs/SOURCE_TERMINOLOGY_POLICY.md` governs social, ritual, learned, occupational, political, kinship, and community terminology.

Use the exact Tamil form printed by the relevant source. Do not replace it silently with a later identity label. A historical equivalence claim, if researched later, must be separate from the source-level concept observation.

## 5. Literary domain

Akam/Puram is a first-class dimension and must retain classification basis.

Supported conceptual states include:

- `akam`
- `puram`
- `uncertain`
- `not_applicable`

Possible bases include source-explicit metadata, documented work-level classification, separately represented Tolkāppiyam concept evidence, or explicit editorial inference. These are not interchangeable.

## 6. Tiṇai and tuṟai

The concept model supports:

- குறிஞ்சி
- முல்லை
- மருதம்
- நெய்தல்
- பாலை
- கைக்கிளை
- பெருந்திணை

Tiṇai and tuṟai must retain provenance. Do not infer them from conventional expectations when the selected source does not support the assignment.

Keep separate:

- source-printed classification;
- source-note/structural metadata classification;
- Tolkāppiyam grammatical concept evidence;
- later editorial/research classification.

Specific tuṟai values require stable versioned concept IDs before production assignment.

## 7. Five-landscape concept families

Landscape families are not one-word terrain definitions and are not automatic tiṇai assignments.

Where evidence supports it, a landscape may be linked separately to:

- terrain and water features;
- season/weather/time;
- flora;
- fauna;
- occupation/production;
- food/subsistence;
- settlements;
- mobility/transport;
- social actors;
- emotional/relational situations;
- ritual references;
- material objects and characteristic activities.

Every link requires its own evidence/provenance. Conventional association tables are not source facts by themselves.

## 8. Controlled 29-dimension audit frame

R1.5 uses the following exhaustive review dimensions:

1. literary domain — Akam/Puram;
2. tiṇai / tuṟai;
3. landscape/environment;
4. season/weather/time;
5. flora;
6. fauna;
7. people and social roles;
8. relationships;
9. emotion/lived experience;
10. occupations and production;
11. food and subsistence;
12. clothing, ornaments, adornment;
13. material culture and everyday objects;
14. weapons and warfare;
15. mobility and transport;
16. settlements and built environment;
17. economy;
18. trade and exchange;
19. polity and political life;
20. communities/social groups;
21. family/gender/kinship;
22. religion/ritual;
23. death/mourning/memory;
24. arts/music/performance;
25. knowledge/technology;
26. values/ethical concepts;
27. body/health;
28. named entities;
29. textual/intertextual relationships.

The machine-readable audit registry is `research/audits/r15-premerge/dimensions.json`.

## 9. Dimension evidence boundaries

### Environment, flora and fauna

Preserve Tamil printed forms. Modern scientific taxonomy or modern geographic identification is a separate external claim.

### People, communities and roles

A role/community mention does not resolve a historical individual or modern community identity.

### Relationships

Relationship observations require evidence pointers. Shared names or shared concepts do not automatically prove co-reference, dependency, alliance, chronology, or kinship.

### Emotion and lived experience

Source-visible emotion/lived state may be classified cautiously. Do not convert modern sentiment scoring into source certainty.

### Economy and trade

Commodity or gift evidence does not by itself prove a reconstructed trade network, tax system, or direction of exchange.

### Polity and warfare

Ruler/title/weapon/battle evidence does not automatically establish a unique historical person, dynasty, date, or battle event.

### Religion and ritual

Record only source-supported deity/ritual/sacred-practice evidence. Do not impose later sectarian identities automatically.

### Named entities

Mention inventory precedes historical identity resolution. Modern geography, biography, chronology, dynasty, or co-reference requires separately classified evidence.

### Textual/intertextual relationships

A source-visible allusion or explicit relation may be recorded. Similarity alone does not prove textual dependence or chronology.

## 10. Tolkāppiyam as separate concept evidence

Tolkāppiyam is a grammatical/poetics work with its own evidence stream:

```text
Tolkāppiyam
  → அதிகாரம் / இயல் / நூற்பா
  → GRAMMATICAL_CONCEPT_EVIDENCE
  → controlled concept
  → later reviewed comparison with poem evidence
```

R1.5 defines this stream but creates zero production Tolkāppiyam concept-observation NDJSON records.

The exhaustive audit read all 1,602 நூற்பா in இயல் context and built a 29-dimension formal crosswalk. That crosswalk is review/coverage evidence, not an automatic classifier.

A Tolkāppiyam rule must never silently rewrite a Sangam poem's source classification.

## 11. R1.5 implementation

Current R1.5 foundation contains:

- concept schema `0.3.0`;
- 36 concept definitions;
- classification-basis vocabulary;
- concept-evidence policy vocabulary;
- Akam/Puram states;
- seven tiṇai categories;
- first-class tuṟai family/states;
- five landscape families;
- named-entity families;
- lived-life dimensions;
- separate Tolkāppiyam concept-evidence schema;
- 8 provenance-bearing Puṟanāṉūṟu pilot observations across 6 records;
- deterministic matrix/report generation;
- acceptance/orphan-reference validation;
- exhaustive Puṟanāṉūṟu and Tolkāppiyam pre-merge audit.

The 8 production pilot observations remain source-explicit and reviewed. There are no external-historical or interpretive pilot observations and no verified historical identities.

## 12. Exhaustive pre-merge review boundary

### Puṟanāṉūṟu

- 400 / 400 records read sequentially;
- all 29 dimensions considered for every record;
- sparse ledger stored in eight 50-record TSV parts;
- record 200 remains damaged/unreconstructed;
- records 267–268 remain source-lost/unreconstructed.

### Tolkāppiyam

- 27 / 27 இயல் reviewed;
- 1,602 / 1,602 நூற்பா read in context;
- all 29 dimensions considered;
- crosswalk covers 29 / 29 dimensions at unequal depth;
- automatic poem classification disabled.

These audits prove review coverage; they do not claim that every qualifying ledger code is already a production concept observation.

## 13. Evidence-first production rule

Required chain:

```text
matrix value
→ concept observation / assertion
→ exact record
→ exact source span or source-explicit field
→ canonical record hash
→ frozen source provenance
→ review/external citation where applicable
```

No manually entered production matrix value may bypass this chain.

## 14. Phase roadmap and status

### R0 — complete

Research architecture and Puṟanāṉūṟu evidence pilot. Evidence schema `0.1.0` preserved.

### R1 — complete and merged

Append-only review workflow and entity-resolution rules. Workflow schema `0.2.0` preserved.

### R1.5 — current pre-merge phase

Concept/observation foundation, bounded pilot, exhaustive matrix audit, validation, documentation audit. PR #3 remains draft and unmerged by explicit user instruction.

### R2 — blocked / not started

After explicit R1.5 merge authorization and fresh inspection of merged `main`, apply the concept model across the nine core Sangam works with record-level evidence provenance.

### R3

Cross-corpus entity resolution and reviewed relationships.

### R4

Evidence-backed civilisation/lived-life datasets.

### R5

Matrix explorer, search, maps, timelines, networks and evidence drill-down.

### R6

Compatible extension to Patiṉeṇkīḻkkaṇakku without forcing Sangam-specific structure onto different works.

### R7

Tolkāppiyam ↔ Sangam conceptual comparison through separately represented evidence.

### R8

External scholarship/historical-identification layer with explicit citations, confidence, review and disagreement handling.

## 15. R1.5 merge gate

R1.5 may be considered technically ready only when:

- schemas/vocabularies validate;
- production observations remain assertion-provenanced;
- exhaustive audit validator passes;
- full tests pass;
- R1 and R1.5 deterministic regeneration passes;
- repository audit passes;
- Corpus 1.1.0 and Tolkāppiyam remain unchanged;
- R1 primary histories remain unchanged;
- current continuity documents are synchronized;
- source terminology policy is preserved.

Technical readiness does **not** authorize merge. PR #3 remains open/draft/unmerged until the user explicitly authorizes it.
