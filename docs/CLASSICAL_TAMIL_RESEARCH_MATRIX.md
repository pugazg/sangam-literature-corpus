# Classical Tamil Research Matrix

## 1. Purpose

This document defines the long-term conceptual research model for the derived Classical Tamil Research Layer.

It exists to prevent the project from becoming a loose collection of tags such as “flora”, “fauna”, “king”, or “place”. The research goal is broader: to build an evidence-backed, multidimensional representation of literary domains, landscapes, relationships, ecology, material culture, society, economy, polity, ritual, arts, and everyday life across the preserved Classical Tamil corpus.

The frozen corpus remains authoritative source evidence. The matrix is a derived research model.

The matrix must never be written back into frozen canonical poem or நூற்பா records merely because a classification is useful.

## 2. Governing architecture

The intended architecture is:

```text
Frozen canonical corpus
        ↓
Source-grounded evidence assertions
        ↓
Review events and ambiguity queues
        ↓
Concept classification and entity resolution
        ↓
Cross-record / cross-work relationships
        ↓
Research matrices and analytical datasets
        ↓
Maps, timelines, networks, search, visualisation, interpretation
```

A matrix cell is therefore a **view derived from assertions**. It is not an unsupported boolean fact attached to a poem.

Bad model:

```text
Poem 24 × Elephant = Yes
```

Preferred model:

```yaml
concept: fauna.elephant
work_id: <work>
record_id: <record>
surface_form: <exact printed form>
evidence_span: <exact source span>
evidence_class: SOURCE_EXPLICIT
confidence: <controlled value>
review_status: <controlled value>
assertion_id: <deterministic ID>
```

The matrix is generated from such records.

## 3. Claim-type separation

The same concept may be supported in different ways. These must never be collapsed.

Example:

```text
A poem literally contains “முல்லை”
→ SOURCE_EXPLICIT lexical evidence

A selected source prints the poem's திணை as முல்லை
→ SOURCE_EXPLICIT classification evidence

A poem contains features commonly associated with முல்லை but the source does not classify it
→ DERIVED_CLASSIFICATION / EDITORIAL_INFERENCE

A Tolkāppiyam நூற்பா defines or associates a முல்லை concept
→ GRAMMATICAL_CONCEPT_EVIDENCE

A modern scholar identifies an ancient place with a modern location
→ EXTERNAL_HISTORICAL
```

The research layer must retain the evidence basis for every claim.

At minimum, preserve and distinguish repository-appropriate equivalents of:

- `SOURCE_EXPLICIT`
- `MECHANICALLY_DERIVED`
- `CROSS_TEXT`
- `EDITORIAL_INFERENCE`
- `GRAMMATICAL_CONCEPT_EVIDENCE`
- `EXTERNAL_HISTORICAL`
- `INTERPRETATION`

Do not silently upgrade one class into another.

## 4. Akam / Puram as a first-class axis

Akam / Puram must become a top-level research dimension rather than an informal work label.

Recommended model:

```yaml
literary_domain:
  value:
    - akam
    - puram
    - uncertain
    - not_applicable
  evidence_basis:
    - source_explicit
    - work_level_classification
    - tolkappiyam_mapping
    - derived
  supporting_assertions: []
  review_status:
```

Do not store only:

```yaml
akam: true
```

because that conceals why the classification exists.

The model must permit source-explicit, work-level, grammatical, and derived classifications to coexist without being treated as equivalent.

## 5. Tiṇai and related Akam categories

The five major landscapes must be modeled explicitly:

- குறிஞ்சி / Kuṟiñci
- முல்லை / Mullai
- மருதம் / Marutam
- நெய்தல் / Neytal
- பாலை / Pālai

The system must also support exceptional or additional Akam categories where evidence requires them, including:

- கைக்கிளை / Kaikkilai
- பெருந்திணை / Peruntiṇai

Do not infer a tiṇai merely from conventional expectations when the selected source does not print it.

Keep separate:

- tiṇai printed by the canonical source;
- tiṇai printed in source notes or structural metadata;
- tiṇai asserted by Tolkāppiyam concept evidence;
- tiṇai inferred by later editorial/research analysis.

## 6. Five-landscape concept model

The project must not reduce a landscape to a single terrain label such as “Kuṟiñci = mountain”.

Each landscape should be able to participate in a multidimensional concept graph.

Conceptual template:

```text
Tiṇai / landscape
│
├── literary domain
├── terrain / physical environment
├── season / climate
├── time / சிறுபொழுது / பெரும்பொழுது where evidence supports it
├── flora
├── fauna
├── water / land features
├── occupations
├── food and subsistence
├── settlements
├── mobility / transport
├── deities / ritual references
├── social actors
├── emotional / relational situation
├── characteristic activities
├── material objects
└── supporting textual evidence
```

The conventional association system must not be hard-coded as fact into poem records.

Tolkāppiyam and other explicit textual evidence should be represented as separate concept evidence streams so researchers can compare theory/prescription with poetic usage.

## 7. Core matrix dimensions

The research matrix should support at least the following dimensions. Additional concepts may be introduced later through versioned controlled vocabularies.

### 7.1 Literary and poetic structure

- Akam
- Puram
- uncertain / mixed / not applicable
- tiṇai
- tuṟai
- source-printed subdivisions
- exceptional Akam categories
- poem situation / context where source-explicit
- speaker / addressee where source-explicit
- poetic or rhetorical features when separately classified

### 7.2 Landscape and environment

- mountain
- hill
- forest
- pastoral tract
- cultivated plain
- field
- coast
- sea
- river
- stream
- pond / tank / water body
- waterfall
- dry / transformed landscape condition
- settlement-environment relationships
- other source-explicit geographic features

### 7.3 Season, weather, and time

- season
- rainfall
- drought
- heat
- cold
- monsoon-related evidence
- dawn
- day
- evening
- night
- other source-explicit temporal expressions
- சிறுபொழுது / பெரும்பொழுது mappings only with explicit evidence classification

### 7.4 Flora

- flowers
- trees
- shrubs
- grasses
- crops
- fruits
- medicinal plants
- material-use plants
- agricultural plants

Scientific or modern taxonomic identification must be a separate external evidence assertion, never silently substituted for the Tamil printed form.

### 7.5 Fauna

- mammals
- domestic animals
- wild animals
- birds
- fish
- marine animals
- reptiles
- insects
- other animal mentions

Modern zoological identification must remain separate from source-explicit mention evidence.

### 7.6 Human actors and social roles

Examples include:

- தலைவன்
- தலைவி
- தோழி
- செவிலி
- mother / father / child / kin
- poet
- bard / பாணர் and other performers
- king
- chief
- patron
- warrior
- cultivator
- pastoral worker
- fisher
- salt worker
- merchant
- artisan / craft worker
- messenger
- religious / ritual actor
- other source-explicit roles

Do not collapse role mentions into resolved historical persons.

### 7.7 Relationships

- lovers
- spouses
- parent / child
- siblings / kin
- friend / companion
- ruler / poet
- patron / bard
- ruler / subordinate ruler
- ally
- enemy
- warrior / ruler
- community / occupation
- person / place
- person / polity
- poem / poet
- poem / addressee

Relationship assertions must cite supporting assertion IDs.

### 7.8 Emotion and lived experience

Possible categories, when evidence and methodology support them:

- union
- separation
- waiting
- longing
- anxiety
- grief
- mourning
- courage
- fear
- shame
- honour
- generosity
- hospitality
- friendship
- loyalty
- fame

Do not derive psychological certainty from modern sentiment analysis.

### 7.9 Occupations and production

- agriculture
- pastoralism
- fishing
- salt production
- hunting
- gathering
- craft production
- metal work
- textile work
- maritime activity
- trade
- transport
- bardic / performance work
- warfare as profession/activity
- other economic activities

### 7.10 Food and subsistence

- grains
- rice / millet and other source-explicit crops
- meat
- fish
- fruits
- vegetables / plant foods
- dairy
- drinks
- intoxicants where source-explicit
- cooking / preparation
- feast
- hospitality food
- scarcity / hunger

Avoid modern nutritional interpretation in the source evidence layer.

### 7.11 Clothing, ornament, and adornment

- garments
- textiles
- jewellery
- metals used in ornament
- flowers worn
- garlands
- cosmetics / body adornment where source-explicit
- status-related adornment

### 7.12 Material culture and everyday objects

- pottery
- vessels
- household objects
- lamps
- furniture
- tools
- agricultural tools
- craft tools
- storage objects
- ritual objects
- musical instruments
- weapons
- transport objects

### 7.13 Weapons and warfare

- sword
- spear
- bow
- arrow
- shield
- armour where source-explicit
- elephant warfare
- cavalry
- chariot warfare
- fort
- siege
- battle
- raid
- victory / defeat
- battlefield death
- military mobilisation
- alliance / hostility

Evidence records do not equal unique historical battles.

### 7.14 Mobility and transport

- walking / journey
- cart
- chariot
- horse
- elephant
- boat
- ship
- maritime travel
- routes
- movement between ecological zones

### 7.15 Settlements and built environment

- ஊர்
- மூதூர்
- பட்டினம்
- village / settlement expressions
- port
- city
- palace
- fortification
- house / household
- market
- agricultural settlement
- coastal settlement
- other built features

Do not assign modern coordinates at extraction time.

### 7.16 Economy

- cultivation
- production
- exchange
- market activity
- gifts
- bardic reward
- wealth
- tribute
- taxation where source-explicit
- cattle wealth
- land-related wealth
- pearls
- salt
- metals
- craft goods
- scarcity
- redistribution

### 7.17 Trade and exchange

- merchant
- commodity
- port
- maritime exchange
- inland exchange
- gift exchange
- tribute
- imported/exported goods only where evidence supports the direction
- routes
- ships / boats

Do not infer a trade network merely from isolated commodity mentions.

### 7.18 Polity and political life

- king
- chief
- ruler title
- polity name
- sovereignty
- territory
- tribute
- alliance
- hostility
- diplomacy
- succession where source-explicit
- patronage
- rulership practice
- war leadership

Dynasty or chronology reconstruction belongs to later reviewed/external layers unless source-explicit.

### 7.19 Communities and social groups

- occupational communities
- performers
- warriors
- cultivators
- pastoral communities
- fishers
- salt workers
- merchants
- artisans
- other named communities

Do not map ancient community labels directly onto modern caste categories without separately cited evidence and methodological review.

### 7.20 Family, gender, and kinship

- lovers
- marriage
- spouse
- mother
- father
- child
- sibling
- extended kin
- widowhood
- motherhood
- gendered roles
- household relations

Interpretive claims about gender systems require later methodological treatment.

### 7.21 Religion and ritual

- deity mention
- sacred place
- worship
- offering
- sacrifice
- vow
- ritual practice
- divination where source-explicit
- funerary / memorial practice

Do not impose later sectarian categories automatically.

### 7.22 Death, mourning, and memory

- battlefield death
- death outside battle
- mourning
- lament
- widowhood
- memorialisation
- hero stone / நடுகல் where source-explicit
- fame after death
- remembrance

### 7.23 Arts, music, and performance

- poet
- bard
- musician
- dancer
- performer
- instrument
- song
- dance
- court performance
- itinerant performance
- patronage of arts

### 7.24 Knowledge and technology

When explicitly evidenced:

- medicine
- healing
- agriculture knowledge
- irrigation
- navigation
- astronomy / celestial observation
- calendrical/time expressions
- metallurgy
- craft techniques
- textile production
- ship/boat knowledge
- animal management

### 7.25 Values and ethical concepts

When source-explicit or separately classified:

- அறம்
- honour
- fame
- generosity
- hospitality
- friendship
- loyalty
- courage
- restraint
- justice
- duty

Do not merge later ethical-system interpretations into Sangam evidence automatically.

### 7.26 Body and health

- body descriptions
- wounds
- injury
- illness
- hunger
- fatigue
- beauty/body imagery
- medicine
- healing
- pregnancy / childbirth where source-explicit

### 7.27 Named entities

- poets
- rulers
- chiefs
- patrons
- addressees
- persons
- places
- polities
- communities
- deities

Mention inventory comes before historical identity resolution.

### 7.28 Textual and intertextual relationships

- repeated surface forms
- shared first lines
- repeated phrases
- explicit cross-references
- shared poet
- shared ruler
- shared place
- shared community
- shared object / commodity / species concept
- Tolkāppiyam concept correspondence

Textual similarity must not be converted automatically into dependence or chronology.

## 8. Record-centric research view

Every Sangam poem should eventually be queryable across a common multidimensional research frame:

```text
Record
│
├── Akam / Puram
├── Tiṇai
├── Tuṟai
│
├── People
├── Roles
├── Relationships
│
├── Places
├── Landscape
├── Flora
├── Fauna
├── Season / Time
│
├── Food
├── Clothing
├── Ornament
├── Weapons
├── Objects
├── Transport
│
├── Occupations
├── Production
├── Trade
├── Gifts
├── Wealth
│
├── Kingship
├── Warfare
├── Diplomacy
│
├── Family
├── Gender
├── Social practice
├── Religion / ritual
│
├── Music
├── Dance
├── Performance
│
└── exact evidence assertions
```

Empty cells mean “no qualifying assertion currently exists”, not “the concept was absent from ancient Tamil life”.

Source silence must never be interpreted automatically as historical absence.

## 9. Tolkāppiyam as a separate conceptual evidence stream

Tolkāppiyam should become a conceptual spine for later research, but its நூற்பா must not be forced into poem-oriented research types.

Recommended direction:

```text
Tolkāppiyam
   ↓
அதிகாரம் / இயல் / நூற்பா
   ↓
grammatical / poetic concept assertions
   ↓
controlled concept registry
   ↓
comparison with Sangam poem evidence
```

Example conceptual relationship:

```text
Tolkāppiyam
Poruḷatikāram
   ↓
Akattiṇaiyiyal
   ↓
concept: குறிஞ்சி
   ↓
source-supported conceptual associations
   ↓
Sangam evidence occurrences
```

The relationship is comparative, not automatically prescriptive.

A Tolkāppiyam rule must not silently rewrite a poem's classification.

The research layer should allow questions such as:

> How closely does surviving Sangam poetic usage correspond to, differ from, or exceed the conceptual model represented in Tolkāppiyam?

That question requires separate evidence streams for grammar/poetics and poem usage.

## 10. Concept registries and controlled vocabularies

R1.5 should establish a versioned concept registry before R2 bulk extraction.

Each concept should support repository-appropriate equivalents of:

```yaml
concept_id:
preferred_label_tamil:
preferred_label_english:
transliteration:
concept_family:
parent_concept:
source_status:
definition_status:
introduced_in_version:
notes:
```

Do not create modern English definitions that imply scholarly consensus unless sourced/reviewed.

Tamil printed forms remain primary evidence.

## 11. Evidence-first matrix rule

Every populated research matrix cell must be traceable to one or more assertion IDs.

Required chain:

```text
matrix cell
→ assertion
→ exact record
→ exact source span or source-explicit field
→ canonical record hash
→ frozen source provenance
```

For derived or external claims, continue the chain to the relevant review event or external citation.

No manually entered matrix value may bypass this chain.

## 12. Recommended research roadmap

The research roadmap is now formalised as:

### R0 — Research architecture + Puṟanāṉūṟu pilot

Status: implemented on `research/sangam-evidence-r0`.

Purpose:

- assertion architecture;
- exact evidence spans;
- source-explicit metadata;
- conservative mention candidates;
- deterministic generation;
- first entity/relationship sample.

### R1 — Review workflow + entity-resolution rules

Immediate next phase after R0 reconciliation.

Purpose:

- append-only review events;
- reviewer model;
- ambiguity queues;
- possible / reviewed / verified identity states;
- merge/split/reject/supersede rules;
- deterministic reviewed exports.

R1 must not attempt mass historical resolution.

### R1.5 — Classical Tamil Concept Matrix and Ontology Foundation

Mandatory before R2 bulk extraction.

Purpose:

- formalise Akam / Puram as first-class research dimensions;
- formalise tiṇai and tuṟai evidence models;
- formalise five-landscape concept structure;
- define cross-corpus concept IDs;
- define matrix dimensions for ecology, material culture, economy, society, polity, ritual, arts, daily life, and relationships;
- define concept hierarchy and controlled vocabulary policy;
- define evidence requirements for each concept family;
- define how source-explicit, derived, Tolkāppiyam, external, and interpretive claims coexist;
- create deterministic matrix views from assertions;
- pilot the matrix against Puṟanāṉūṟu evidence before corpus-wide use.

R2 must not begin until R1.5 is validated.

### R2 — Apply the matrix across all nine core Sangam works

Purpose:

- extract comparable evidence across the nine frozen core Sangam works;
- retain work-specific source metadata differences;
- populate common concept families only through evidence assertions;
- preserve Akam/Puram/tiṇai/tuṟai provenance;
- produce work-level and cross-work coverage reports.

Do not resolve historical entities simply because the same name appears across works.

### R3 — Cross-corpus entity resolution and relationships

Purpose:

- poets;
- rulers;
- chiefs;
- patrons;
- addressees;
- places;
- polities;
- communities;
- cross-work relationships;
- variant names and epithets;
- evidence-backed identity decisions.

### R4 — Civilisation datasets

Purpose:

Build evidence-backed analytical datasets for:

- ecology;
- landscapes;
- flora/fauna;
- food and subsistence;
- occupations;
- production;
- economy;
- trade;
- material culture;
- settlements;
- transport;
- society;
- kinship and gender;
- polity;
- warfare;
- religion and ritual;
- death and memorialisation;
- arts and performance;
- knowledge/technology;
- values and lived experience.

R4 outputs must distinguish evidence counts from historical event/fact counts.

### R5 — Research experience

Purpose:

- matrix explorer;
- cross-text search;
- maps;
- timelines;
- network views;
- entity pages;
- tiṇai atlas;
- landscape explorer;
- evidence drill-down;
- reproducible exports.

Visualisations must allow users to reach the underlying assertion and canonical text.

### R6 — Extend the derived layer to Patiṉeṇkīḻkkaṇakku

Purpose:

- apply compatible research concepts to the eighteen frozen Patiṉeṇkīḻkkaṇakku works;
- introduce didactic/ethical concept families where appropriate;
- do not force Sangam poem categories onto structurally different works.

### R7 — Tolkāppiyam ↔ Sangam conceptual mapping

Purpose:

- build a separate grammatical / poetics concept stream from Tolkāppiyam;
- connect relevant நூற்பா to controlled concepts;
- compare Tolkāppiyam concept evidence with poem evidence;
- examine correspondences and differences without rewriting canonical classification;
- support concept-level citation in both directions.

### R8 — External scholarship and historical-identification layer

Purpose:

- modern place identifications;
- chronology proposals;
- historical person resolution using scholarship;
- archaeological evidence;
- botanical/zoological modern identifications;
- broader historical interpretation.

Every R8 claim must carry explicit external citations, confidence, review status, and disagreement handling.

R8 must remain separable from the source-derived research layer.

## 13. Immediate sequencing rule

Current sequence:

```text
R0 reconciliation
      ↓
R1 review/entity-resolution foundation
      ↓
R1.5 concept matrix and ontology foundation
      ↓
R2 nine-work Sangam extraction
```

Do not skip R1.5.

The reason is methodological: bulk extraction should not begin until the project knows exactly which dimensions it intends to observe, how those dimensions are defined, and what evidence is sufficient to populate them.

## 14. Long-term research objective

The project is not merely building a keyword index.

The long-term goal is an auditable textual evidence base from which researchers can investigate the world represented in Classical Tamil literature, including:

- landscapes and ecology;
- love and relationships;
- family and social organisation;
- food and subsistence;
- occupations and production;
- trade and exchange;
- material culture;
- political life and warfare;
- ritual and belief;
- music, performance, and poetry;
- mobility and settlements;
- human relationships with plants, animals, water, and land;
- correspondence between literary usage and Tolkāppiyam's conceptual models.

Every such investigation must remain traceable to source evidence and explicit about uncertainty.

## 15. Non-goals of the matrix foundation

The matrix foundation must not:

- rewrite canonical texts;
- silently classify every poem;
- treat absence of evidence as evidence of absence;
- turn conventional textbook associations into source facts;
- infer modern caste identities;
- geocode ancient places automatically;
- invent chronology;
- merge names automatically;
- treat evidence mentions as unique historical events;
- treat Tolkāppiyam as automatically descriptive of every surviving poem;
- generate historical conclusions before review methodology exists.

## 16. Success condition for R1.5

R1.5 is ready for R2 only when:

- the concept registry is versioned;
- Akam/Puram evidence rules are explicit;
- tiṇai/tuṟai evidence rules are explicit;
- five-landscape concept families are represented without hard-coded unsupported assignments;
- matrix dimensions are documented and machine-readable;
- every matrix value is assertion-backed;
- Tolkāppiyam concept evidence has a separate type/stream;
- entity and concept identity are not conflated;
- validation covers orphan concepts/assertions/relationships;
- deterministic generation passes twice;
- Puṟanāṉūṟu pilot compatibility is demonstrated;
- all frozen corpus works remain unchanged;
- the project can explain why each populated matrix cell exists.
