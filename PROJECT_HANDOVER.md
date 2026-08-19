# Sangam Literature Corpus — Project Handover

## Authoritative current state

Repository: `pugazg/sangam-literature-corpus`

Default branch: `main`

Active research branch: `research/classical-tamil-concept-matrix-r1.5a`

R1.5 was explicitly authorized and merged into `main` at `d82f9c78f27f9c9daf8fbb913d01ddfb29bddba1`. PR #3 is historical/merged. Draft PR #4 is the active R1.5A proposal.

R1.5A keeps concept/observation schema `0.3.0`; it is not R2. **R2 remains blocked and must not start without explicit user authorization.** Treat current GitHub state, branch head, open PRs and checks as authoritative over older prose.

## Frozen corpus and preserved layers

Classical Tamil Corpus 1.1.0 remains frozen: 28 works / 7,234 canonical records / 5,632 poems / 1,602 Tolkāppiyam நூற்பா. Tag: `classical-tamil-corpus-v1.1.0`.

R0 schema `0.1.0` remains preserved: 2,867 assertions / 285 literary-body candidates / 43 pilot surface-form entities / 51 relationships.

R1 schema `0.2.0` remains preserved: 8 append-only review events / 3 conservative entity-resolution decisions / 0 verified historical identities.

R1.5 schema `0.3.0` remains the exact 29-dimension concept/evidence foundation. The old Puṟanāṉūṟu and Tolkāppiyam audits remain control evidence only and must never be copied mechanically into production.

## Puṟanāṉūṟu R1.5A production — complete

Puṟanāṉūṟu `001.json` through `400.json` form the complete gap-free production corpus.

Durable cadence history must remain documented exactly:

- benchmark `001–002`;
- stabilization **003–010**;
- regular **25-record** batches beginning **011–035** through `361–385`;
- final batch `386–400`.

Definitive completion checkpoint:

- SHA `491fa3107984b29f1dbb747bc7483e0cb694ab91`;
- parent `bf7e0e168fd05476a99b0ee8615ddc324694924d`;
- 400 reviewed / 0 remaining / next record null;
- 7,169 production observations;
- 29 canonical dimensions;
- 224 tests at the Puṟanāṉūṟu-only completion boundary;
- workflow `32267324444` green on that exact checkpoint;
- deterministic regeneration, repository audit, Corpus/Tolkāppiyam non-drift and R1 history preservation all passed.

Do not reopen completed Puṟanāṉūṟu records merely to match the older sparse audit. Existing source-terminology/source-loss guardrails remain binding, including record 176, damaged record 200 and source-lost records 267–268.

## Tolkāppiyam R1.5A production — benchmark accepted

The prerequisite that blocked Tolkāppiyam production is satisfied. Tolkāppiyam production is now active as a **separate grammatical/poetics evidence stream**.

Frozen source hierarchy:

`work → 3 அதிகாரம் → 27 இயல் → 1,602 நூற்பா`

Canonical production identity is source sequence:

- `corpus/tolkappiyam/nurpas/0001.md` … `1602.md`;
- record IDs `tolkappiyam-0001` … `tolkappiyam-1602`.

The initial benchmark **0001–0002** is materialized and validated:

- records reviewed: **2 / 1,602**;
- records remaining: **1,600**;
- next record: **tolkappiyam-0003**;
- grammatical concept evidence: **2**;
- incidental examples: **0**;
- exact dimension count: **29**;
- expanded regression suite: **228 passed**;
- verification workflow `32270636581`: fully green;
- R0/R1/R1.5 validation, Puṟanāṉūṟu production validation, Tolkāppiyam production validation, deterministic regeneration, repository audit, frozen-corpus non-drift and R1 history preservation all passed.

The two benchmark observations are both `knowledge_technology` formal evidence using controlled concept `knowledge.grammar.phonology`:

- 0001 formally defines the letter-system scope/count and dependent forms;
- 0002 formally classifies `குற்றியலிகரம்`, `குற்றியலுகரம்`, `ஆய்தம்` and related dependent-sign structure.

The benchmark deliberately records **no incidental examples** and does not turn `எழுத்து`, `புள்ளி`, letter/sign labels or grammatical categories into material, historical or named-entity claims.

## Tolkāppiyam production contract

Durable paths:

- `research/production/tolkappiyam/review-specs/`
- `research/production/tolkappiyam/records/`
- `research/observations/tolkappiyam/r15-production.ndjson`
- `research/schemas/tolkappiyam-production-review-r15.schema.json`
- `research/schemas/tolkappiyam-concept-evidence-r15.schema.json`
- `research/concepts/classical-tamil/tolkappiyam-production-concepts-r15a.json`
- `scripts/materialize_r15a_tolkappiyam_batch.py`
- `scripts/validate_r15_tolkappiyam_production.py`
- `.github/workflows/materialize-r15a-tolkappiyam-batch.yml`

Every நூற்பா is reviewed sequentially across the same exact 29 dimensions, but Tolkāppiyam requires a different evidence-role distinction from poem production:

1. formal grammatical/poetics concept evidence;
2. incidental example evidence;
3. no qualifying evidence identified.

Only formal evidence is flattened into `research/observations/tolkappiyam/r15-production.ndjson` as `GRAMMATICAL_CONCEPT_EVIDENCE` with classification basis `tolkappiyam_mapping`. Incidental examples stay inside the per-record review and must not become historical, ecological, social, material or lived-life claims.

The old Tolkāppiyam `review-manifest.json` and `dimension-crosswalk.json` are coverage/control artifacts. The crosswalk is representative formal support, not an exhaustive occurrence index and not a classifier. Fresh source review must come first.

The R1.5 acceptance boundary has been updated so Tolkāppiyam production observations are permitted only when the complete Puṟanāṉūṟu 001–400 production corpus exists. The original bounded R1.5 pilot remains preserved.

The R1.5 baseline now counts actual Tolkāppiyam NDJSON observation rows rather than NDJSON files.

## Source terminology rule

`docs/SOURCE_TERMINOLOGY_POLICY.md` is mandatory.

Retain exact source Tamil. Do not silently substitute later identity, hierarchy, caste/community, sectarian, deity, taxonomy, modern-community or external-influence labels. Formal grammatical categories, lexical examples and historical claims must remain distinct.

A Tolkāppiyam rule never automatically classifies Puṟanāṉūṟu or another Sangam poem.

## Next permitted activity

Proceed with the **Tolkāppiyam 0003–0010 stabilization batch**.

For each நூற்பா 0003 through 0010, sequentially:

1. read the complete frozen canonical record and its நூல் மரபு context;
2. consider all 29 dimensions;
3. distinguish formal grammatical evidence from incidental examples and reviewed-empty dimensions;
4. preserve exact source spans and Tamil terminology;
5. do not let the old crosswalk create classifications;
6. after fresh decisions are complete, use the old manifest/crosswalk only as control context;
7. stage one contiguous stabilization spec only after all eight fresh reviews are fixed;
8. materialize deterministically and validate the gap-free prefix through 0010;
9. inspect the resulting formal observation stream and incidental-example counts;
10. run the complete PR workflow before choosing the scaled cadence.

Do **not** decide the long-run batch size until 0003–0010 has validated. Prefer இயல்-aware cadence after stabilization rather than mechanically copying Puṟanāṉūṟu’s 25-record cadence.

Do not start R2.

## Current documentation authority

Read in this order:

1. `docs/DOCUMENTATION_STATUS.md`
2. `docs/SOURCE_TERMINOLOGY_POLICY.md`
3. `PROJECT_HANDOVER.md`
4. `PROJECT_GUIDELINES.md`
5. `NEXT_CHAT_PROMPT.md`
6. `docs/handover/r15a-production-review/README.md`
7. `research/production/purananuru/README.md`
8. `research/production/tolkappiyam/README.md`
9. `research/observations/tolkappiyam/README.md`
10. `docs/CLASSICAL_TAMIL_RESEARCH_MATRIX.md`
11. `docs/classical-tamil-research-layer.md`
12. `research/audits/r15-premerge/tolkappiyam/review-manifest.json`
13. `research/audits/r15-premerge/tolkappiyam/dimension-crosswalk.json`

PR #4 remains draft/unmerged until a later user-authorized merge boundary.
