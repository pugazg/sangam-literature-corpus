# Sangam Literature Corpus — Project Working Guidelines

## 1. Authority

Active repository: `pugazg/sangam-literature-corpus`.

Treat live GitHub state as authoritative over chat summaries, stale SHAs, deleted branches, local paths, old repository names, and historical prompts.

Current phase: **R1.5A** on `research/classical-tamil-concept-matrix-r1.5a`.

R1.5 was merged into `main` at `d82f9c78f27f9c9daf8fbb913d01ddfb29bddba1`. PR #3 is historical/merged. R2 is blocked and must not start without later explicit user authorization.

## 2. Two-layer rule

The repository contains:

1. a frozen preservation corpus;
2. independently versioned derived research layers.

A research change is never sufficient reason to alter frozen canonical text, source notes, raw sources, apparatus evidence, release tags, or release fingerprints.

## 3. Frozen release discipline

- Corpus 1.0.0 — 27 works / 5,632 canonical numbered records.
- Corpus 1.1.0 — 28 works / 7,234 canonical records, including 1,602 Tolkāppiyam நூற்பா.

Do not move, retarget, recreate, amend, or overwrite an existing release tag or release commit to improve research documentation.

## 4. Source fidelity

Preserve what the selected source prints, including uncertainty, loss, irregular numbering, unusual spelling, punctuation, headings, and layout-supported distinctions.

Do not silently modernise, repair, reconstruct, merge editions, infer missing headings, convert commentary into canonical text, or manufacture historical identities.

## 5. Source terminology policy

`docs/SOURCE_TERMINOLOGY_POLICY.md` is mandatory for research prose and classification.

When a source prints a Tamil social, ritual, learned, occupational, political, kinship, or community term, retain that exact source form. Do not substitute one Tamil term for another merely because they appear related. Do not automatically convert a source term into a later caste, sectarian, modern-community, hierarchy, or external-influence identity.

Any later historical equivalence claim belongs in a separately classified external-evidence or interpretive layer with independent provenance.

## 6. Tolkāppiyam rule

Tolkāppiyam hierarchy is `work → அதிகாரம் → இயல் → நூற்பா`.

Tolkāppiyam uses a separate grammatical/poetics concept-evidence stream. A நூற்பா may support later comparison but must never auto-classify or rewrite a Sangam poem.

Do not start the Tolkāppiyam production pass until Puṟanāṉūṟu production records 001–400 are complete and validated.

## 7. Research evidence model

Keep evidence class, confidence, review status, entity-resolution state, and concept classification independent.

A mention is a printed/source occurrence. An entity is a resolved research identity. A concept is a controlled analytical category. Matching strings, epithets, conventional scholarship, or modern expectations do not by themselves resolve identity.

R1 review events and entity-resolution decisions are primary append-only histories. Do not regenerate or silently truncate them.

## 8. Exact 29-dimension production surface

R1.5/R1.5A uses exactly:

1. `literary_domain`
2. `tinai_turai`
3. `landscape_environment`
4. `season_weather_time`
5. `flora`
6. `fauna`
7. `people_social_roles`
8. `relationships`
9. `emotion_lived_experience`
10. `occupations_production`
11. `food_subsistence`
12. `clothing_ornaments_adornment`
13. `material_culture_everyday_objects`
14. `weapons_warfare`
15. `mobility_transport`
16. `settlements_built_environment`
17. `economy`
18. `trade_exchange`
19. `polity_political_life`
20. `communities_social_groups`
21. `family_gender_kinship`
22. `religion_ritual`
23. `death_mourning_memory`
24. `arts_music_performance`
25. `knowledge_technology`
26. `values_ethical_concepts`
27. `body_health`
28. `named_entities`
29. `textual_intertextual_relationships`

Do not collapse distinct dimensions for convenience.

## 9. Evidence-first matrix rule

Every populated production matrix value must have an evidence chain:

`matrix state → observation/assertion → exact record → exact span/source field → canonical hash → frozen source provenance`.

Empty means only `no_qualifying_evidence_identified` in that completed source review. It never means historical absence.

The exhaustive audit ledgers are controls, not production observations.

## 10. R1.5A record-review rule

For every Puṟanāṉūṟu poem:

1. read the complete canonical record and source-explicit metadata;
2. consider all 29 dimensions;
3. write the complete individual `research/production/purananuru/records/NNN.json` in the working tree before reading the next record;
4. retain exact source Tamil, provenance and body-relative spans;
5. link a real R0 assertion only when it genuinely supports the observation;
6. use `direct_record_review` when source-supported semantic evidence has no suitable earlier R0 assertion;
7. preserve ambiguity rather than guessing;
8. compare with the old sparse audit only after the fresh review is complete.

## 11. R1.5A batching cadence

Scholarly review is sequential; Git publishing is batched.

- existing benchmark: 001–002 complete;
- first stabilization batch: 003–010;
- then 25-record batches: 011–035, 036–060, 061–085, and so on;
- final batch ends exactly at 400;
- keep separate per-record JSON files;
- publish one deterministic multi-file commit per completed batch;
- if interrupted, checkpoint the completed contiguous prefix rather than losing reviewed work;
- run full PR CI/non-drift once per published batch, not once per poem.

Do not skip record order merely to fill a batch.

## 12. Special Puṟanāṉūṟu source conditions

- record 200 remains damaged/unreconstructed where the source is damaged;
- records 267–268 remain source-lost/unreconstructed;
- printed names are source mentions unless separately resolved through permitted evidence.

## 13. Branch and PR discipline

Do not force-push shared branches. Do not reset unexplained changes. Do not recreate deleted historical branches merely because old documents mention them.

R1.5A should remain a reviewable branch/PR until the user explicitly authorizes its eventual merge or next phase transition.

## 14. Validation

At each R1.5A batch checkpoint run the established full CI-equivalent gates, including:

```bash
python3 scripts/generate_research_layer.py --root .
python3 scripts/generate_research_r1.py --root .
python3 scripts/generate_research_r15.py --root .
python3 scripts/validate_research_layer.py --root .
python3 scripts/validate_research_r1.py --root .
python3 scripts/validate_research_r15.py --root .
python3 scripts/validate_research_r15_acceptance.py --root .
python3 scripts/validate_research_r15_dimensions.py --root .
python3 scripts/validate_r15_premerge_matrix_audit.py --root .
python3 scripts/validate_r15_purananuru_production.py --root .
pytest -q
python3 scripts/audit_repository.py --root .
```

Also prove Corpus 1.1.0/Tolkāppiyam non-drift and R1 primary-history non-mutation.

## 15. Documentation discipline

Current instructions belong in active documents. Historical prompts, pre-merge hold documents, release snapshots, and older machine logs remain provenance and must not override current post-merge instructions.

`docs/DOCUMENTATION_STATUS.md` defines the active/historical boundary.

## 16. Rights / visibility

The repository remains private. Do not change visibility without separate explicit user authorization after rights review.

## 17. Roadmap

- R1.5A — current: full production review using the merged R1.5 29-dimension foundation.
- R2 — blocked pending explicit user authorization after R1.5A completion/readiness.
- later phases remain evidence/provenance gated.

Never skip source fidelity, review, provenance, and non-drift gates between phases.
