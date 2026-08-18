# Sangam Literature Corpus — Project Working Guidelines

## 1. Authority

Active repository: `pugazg/sangam-literature-corpus`.

Treat live GitHub state as authoritative over chat summaries, stale SHAs, deleted branches, local paths, old repository names, and historical prompts.

Current live branch model at this documentation audit:

- `main`
- `research/classical-tamil-concept-matrix-r1.5`

R0 and R1 research branches were deleted after their work was preserved/reconciled. Do not recreate them merely because historical documents mention them.

PR #3 is the active R1.5 proposal. **Keep it open, draft, and unmerged until the user explicitly authorizes merge. Do not start R2 before that authorization and a fresh post-merge inspection of `main`.**

## 2. Two-layer rule

The repository contains:

1. a frozen preservation corpus;
2. independently versioned derived research layers.

Never blur them.

A research change is never sufficient reason to alter frozen canonical text, source notes, raw sources, apparatus evidence, release tags, or release fingerprints.

## 3. Frozen release discipline

Current release identities:

- Corpus 1.0.0 — 27 works / 5,632 canonical numbered records;
- Corpus 1.1.0 — 28 works / 7,234 canonical records, adding 1,602 Tolkāppiyam நூற்பா.

Do not move, retarget, recreate, amend, or overwrite an existing release tag or release commit to improve documentation.

A new corpus release is required only for an intentional preservation-layer change.

## 4. Source fidelity

Preserve what the selected source prints, including uncertainty, loss, irregular numbering, unusual spelling, punctuation, headings, and layout-supported distinctions.

Do not silently:

- modernise spelling;
- repair punctuation;
- invent missing text;
- merge editions;
- infer missing headings;
- convert commentary into canonical text;
- reconstruct historical identities.

OCR and rendered browser text are secondary aids when reliable encoded source bytes exist.

## 5. Source terminology policy

`docs/SOURCE_TERMINOLOGY_POLICY.md` is mandatory for research prose and classification.

When a source prints a Tamil social, ritual, learned, occupational, political, kinship, or community term, retain that exact source form. Examples may include `அந்தணர்`, `பார்ப்பார்`, `பார்ப்பனர்`, `அரசர்`, `வேளாளர்`, `பாணர்`, and other source-supported forms.

Do not substitute one Tamil term for another merely because they may appear related. Do not convert a source term automatically into a later caste, sectarian, modern-community, hierarchy, or external-influence identity.

Any later historical equivalence claim belongs in a separately classified external-evidence or interpretive layer with independent provenance.

## 6. Tolkāppiyam rules

Tolkāppiyam hierarchy is:

`work → அதிகாரம் → இயல் → நூற்பா`

Canonical records live under `corpus/tolkappiyam/nurpas/`.

Keep repository ID, upstream alias, source sequence, local/traditional numbering, source heading, and editorial display heading distinct where required.

Tolkāppiyam Arivagam is a consumer/reference application, not canonical authority.

For research, Tolkāppiyam uses a separate grammatical/poetics concept-evidence stream. A நூற்பா may support later comparison but must never auto-classify or rewrite a Sangam poem.

## 7. Shared-manifest safety

Never permit parallel writers to append to a shared combined manifest.

Required pattern:

1. work-local generation;
2. one authoritative aggregator;
3. deterministic ordering;
4. explicit UTF-8 serialisation;
5. atomic replacement;
6. advisory locking;
7. validation before replacement;
8. repeated byte stability.

## 8. Research evidence model

Keep these independent:

- evidence class;
- confidence;
- review status;
- entity-resolution state;
- concept classification.

Controlled claim classes include:

- `SOURCE_EXPLICIT`
- `MECHANICALLY_DERIVED`
- `CROSS_TEXT`
- `EDITORIAL_INFERENCE`
- `GRAMMATICAL_CONCEPT_EVIDENCE`
- `EXTERNAL_HISTORICAL`
- `INTERPRETATION`

Never silently upgrade one claim class into another.

## 9. Mention, entity, concept

A mention is a printed/source occurrence. An entity is a resolved research identity. A concept is a controlled analytical category.

Do not merge or resolve identities because of matching strings, normalized forms, epithets, conventional scholarship, or modern expectations.

`possible_match` is weaker than verified identity. Every identity decision must be reviewable, reversible, and assertion-provenanced.

Concept membership also does not establish historical identity.

## 10. Review history

R1 review events and entity-resolution decisions are primary histories. They are append-only and must not be regenerated from scratch or silently truncated.

Assistant-assisted review must identify itself accurately. `reviewed` is not the same as independently verified historical identity.

Rejected and superseded decisions remain auditable.

## 11. Akam / Puram, tiṇai, tuṟai

Akam/Puram is a first-class research dimension with explicit classification basis.

Tiṇai and tuṟai assignments must retain provenance. Do not infer them merely from conventional associations.

Five-landscape families may be connected to terrain, season/time, flora, fauna, occupation, food, settlement, social actors, relationship situations, mobility, ritual references, or objects only through separately classified evidence.

## 12. Research matrix dimensions

The exhaustive R1.5 audit uses 29 controlled dimensions:

1. literary domain;
2. tiṇai/tuṟai;
3. landscape/environment;
4. season/weather/time;
5. flora;
6. fauna;
7. people/social roles;
8. relationships;
9. emotion/lived experience;
10. occupations/production;
11. food/subsistence;
12. clothing/ornaments/adornment;
13. material culture/everyday objects;
14. weapons/warfare;
15. mobility/transport;
16. settlements/built environment;
17. economy;
18. trade/exchange;
19. polity/political life;
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

Detailed methodology: `docs/CLASSICAL_TAMIL_RESEARCH_MATRIX.md`.

## 13. Evidence-first matrix rule

Every production matrix value must have an evidence chain:

`matrix row/cell → observation/assertion → exact record → exact span/source field → canonical hash → frozen source provenance`

Empty cells mean only that qualifying evidence is not currently recorded. They are not historical absence claims.

The exhaustive audit ledgers are semantic review records. They do not automatically become production observations.

## 14. Phase status

- R0 — completed; evidence schema `0.1.0` preserved.
- R1 — completed and merged to `main`; workflow schema `0.2.0` preserved.
- R1.5 — current validated pre-merge foundation on PR #3; concept schema `0.3.0`.
- R2 — blocked and not started.

R1.5 includes:

- versioned concept registry;
- evidence policies;
- Akam/Puram, tiṇai, tuṟai and landscape foundations;
- separate Tolkāppiyam concept-evidence contract;
- bounded Puṟanāṉūṟu production pilot;
- exhaustive 400-record Puṟanāṉūṟu × 29-dimension audit;
- exhaustive 1,602-நூற்பா Tolkāppiyam × 29-dimension audit;
- validators, deterministic regeneration, tests and non-drift gates.

## 15. Branch and PR discipline

Do not force-push shared branches.

Do not reset unexplained changes.

Do not recreate deleted historical branches unless a future explicit recovery task requires it.

Do not merge PR #3 simply because CI is green. Merge requires explicit user authorization.

After an authorized merge, inspect live `main` before creating or starting any R2 work.

## 16. Validation

For R1.5 changes, run the established CI-equivalent gates:

```bash
python3 scripts/generate_research_layer.py --root .
python3 scripts/generate_research_r1.py --root .
python3 scripts/generate_research_r15.py --root .
python3 scripts/validate_research_layer.py --root .
python3 scripts/validate_research_r1.py --root .
python3 scripts/validate_research_r15.py --root .
python3 scripts/validate_research_r15_acceptance.py --root .
python3 scripts/validate_r15_premerge_matrix_audit.py --root .
pytest -q
python3 scripts/audit_repository.py --root .
```

Also prove Corpus 1.1.0 and Tolkāppiyam non-drift and R1 primary-history non-mutation.

## 17. Documentation discipline

Current instructions belong in active documents. Historical prompts and superseded continuity text belong under `docs/history/` and must be clearly treated as non-executable provenance.

Do not retain a section titled “current branches” or “next activity” when its contents describe a deleted branch or completed phase.

`docs/DOCUMENTATION_STATUS.md` records the documentation audit boundary.

## 18. Rights / visibility

The repository remains private. `docs/source-rights-and-redistribution-review.md` retains unresolved questions. Do not change visibility without separate explicit user authorization after rights review.

## 19. Roadmap

- R2 — core Sangam concept-matrix extraction after authorized R1.5 merge;
- R3 — cross-corpus entity resolution and relationships;
- R4 — civilisation/lived-life analytical datasets;
- R5 — research explorer and visualisation;
- R6 — compatible extension to Patiṉeṇkīḻkkaṇakku;
- R7 — Tolkāppiyam ↔ Sangam conceptual comparison;
- R8 — separately cited external scholarship/historical-identification layer.

Never skip the evidence, review, provenance, and non-drift gates between phases.
