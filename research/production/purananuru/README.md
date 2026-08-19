# Puṟanāṉūṟu R1.5A production review ledger

This directory is the durable record-by-record production layer built on the merged R1.5 exact 29-dimension foundation.

## Hard boundaries

- Current phase: R1.5A. It is not R2.
- R1.5 merged into `main` at `d82f9c78f27f9c9daf8fbb913d01ddfb29bddba1`.
- `corpus/purananuru/` is frozen source material and is never edited by this review.
- The earlier sparse audit under `research/audits/r15-premerge/purananuru/` is a coverage/control artifact, not the production observation dataset.
- The Tolkāppiyam production pass must not begin until all 400 Puṟanāṉūṟu records are complete and validated.
- `docs/SOURCE_TERMINOLOGY_POLICY.md` is mandatory.

## Canonical ledger

Each reviewed poem is stored as one file under:

`research/production/purananuru/records/NNN.json`

Progress is the longest gap-free prefix beginning at `001`; prose status is not the authoritative progress counter.

Current materialized gap-free prefix: **001–285**.

- benchmark: 001–002;
- stabilization batch: **003–010** complete;
- regular 25-record batches: **011–035**, **036–060**, **061–085**, **086–110**, **111–135**, **136–160**, **161–185**, **186–210**, **211–235**, **236–260**, **261–285** complete;
- next record: **286**;
- next batch: **286–310**.

Current validated figures: **285 reviewed / 115 remaining / 5,024 production observations / 29 canonical dimensions / 224 tests passed**.

Before record `NNN+1` is read, that record's complete semantic decision state must already be complete. Git publication/materialization may batch already-completed records.

Every record must:

1. identify the exact frozen canonical record and R0 assertion snapshot;
2. consider the exact 29 canonical dimensions in registry order;
3. distinguish qualifying evidence from reviewed-empty dimensions;
4. retain exact source Tamil and body-relative line/character spans for body evidence;
5. retain real R0 assertion IDs where an existing assertion genuinely supports the already-reviewed production observation;
6. mark genuinely new semantic evidence as `direct_r15_source_review_no_prior_assertion` rather than inventing an R0 assertion;
7. preserve source metadata/body/source-note provenance distinctions;
8. keep printed names as source mentions unless separately resolved through permitted external evidence;
9. preserve damaged/source-lost states without reconstruction;
10. compare against the old sparse audit only after fresh source review is complete.

## Reviewed batch specs and materialization

Compact source-first reviewed batch specs live under:

`research/production/purananuru/review-specs/`

Completed 261–285 spec:

- `261-285.json`

The 261–285 batch proved that one complete contiguous 25-record reviewed spec can be materialized safely in a single workflow cycle. This is the preferred low-latency method when the full batch can be completed in one session.

**This does not batch semantic review.** Each poem is still read strictly sequentially and source-first, with its complete 29-dimension decision state finished before moving to the next poem. The old audit remains post-review control only. Split specs remain valid if a session cannot finish the whole batch or a specific source-state problem requires isolation.

`scripts/materialize_r15a_purananuru_batch.py` deterministically expands already-reviewed semantic decisions into canonical production records. It computes evidence spans, source/R0 blob identities, deterministic observation IDs, dimension-review rows, and post-review audit discrepancies.

`scripts/materialize_r15a_purananuru_batch_driver.py` is the range-aware orchestration/source-state compatibility layer. It selects the correct 50-record audit-control TSV per record, safely handles specs crossing audit-part boundaries, accepts genuinely absent source-note blocks, preserves blank canonical `thurai`, and preserves exact `பெயர் தெரிந்திலது` unknown-poet metadata while excluding that non-identity phrase from named-entity linking. These rules represent frozen source states; they do not classify semantics.

Neither script is an automatic semantic classifier. A pre-existing R0 body assertion may be auto-attached only when its assertion type belongs to the dimension already selected by fresh review and its exact source text occurs inside the already-selected source evidence.

After one-pass materialization, perform targeted checks for source-loss, lacunae, metadata/body boundaries and important audit discrepancies; obtain the actual observation count from the normal verifier; update docs once; squash to one user-authored checkpoint parented by the prior green checkpoint; then run final exact-head CI once.

## Source-state lessons from 261–285

- Record 261 preserves `நடுகல்`, memorial naming/adornment, cattle recovery, lament, shorn hair and loss of ornaments as source-explicit memorial/mourning evidence.
- Record 262 preserves `உண்டாட்டு (தலை தோற்றமுமாம்)` as alternate-thurai/classification evidence rather than normalizing it.
- Record 263 preserves `தொழாதனை கழிதல் ஓம்புமதி` as explicit memorial-stone honoring/worship; bare `பாடியவர் / பாடப்பாட்டோர்` labels remain unresolved source-state/TIR evidence.
- Records 264–265 preserve memorial installation/adornment/name inscription and exact `கோவலர்` / `பரிசிலர்` without later identity expansion.
- Records **267–268 are source-lost**. No canonical body or thinai/thurai/poet/addressee metadata survives. Production retains only work-level `literary_domain`; all other 28 dimensions are reviewed-empty with explicit no-reconstruction notes. Do not infer missing content from title, audit, commentary or external tradition.
- Record 270 preserves exact `மறவர்` as source martial/social terminology.
- Record 272 leaves `death_mourning_memory` reviewed-empty because the body does not explicitly state death; metadata `செருவிடை வீழ்தல்` remains TT evidence and does not manufacture a body-level death claim.
- Records 277–280 preserve mother/son, father/husband/son, battlefield death, mourning and widow-like observances while keeping family, ritual, emotion, body and death evidence distinct.
- Record 281 preserves `வேம்பு`, யாழ், ஐயவி, ஆம்பல், `காஞ்சி` song, bells/smoke and wound-protection practices without later ritual/medical-system mapping.
- Record 282 remains incomplete/lacunose with null thinai/thurai; printed `திணையும் துறையும் தெரிந்தில.` is explicit classification-uncertainty TIR, not reconstructed TT.
- Record 283 remains incomplete/lacunose and preserves exact `கோசர்` plus `பாண்பாட்டு (பாடாண் பாட்டும் ஆம்)` as an alternate-thurai signal without later identity/classification normalization.
- Record 285 remains incomplete/lacunose; camp, performance, warfare, wound, city/village, public honor and village-grant evidence is retained without inventing a completed death claim.

Earlier provenance and terminology guardrails remain binding, including record 176, record 200 and all 236–260 lessons.

## R1.5A cadence

The review is sequential; repository publication is batched.

- benchmark: 001–002;
- completed stabilization batch: **003–010**;
- completed regular batches: **011–035**, **036–060**, **061–085**, **086–110**, **111–135**, **136–160**, **161–185**, **186–210**, **211–235**, **236–260**, **261–285**;
- next batch: **286–310**;
- subsequent cadence: **311–335, 336–360, ...**;
- final batch ends exactly at 400;
- prefer one contiguous 25-record spec + one materialization cycle when the whole batch is complete in-session;
- one clean user-authored/squashed Git checkpoint per completed batch;
- full final PR CI/non-drift on the exact squashed head;
- if the session cannot complete the planned batch, checkpoint only the completed contiguous prefix.

This cadence must never be used to skip sequential semantic review or copy the control ledger into production.

## Evidence spans

For `canonical_body` evidence, `evidence_span.start_line` and `end_line` are 1-based poem-body line numbers. Character offsets are 0-based Unicode string positions within the cited body lines. `source_text` must reproduce the frozen source slice exactly.

Metadata evidence uses its exact YAML field/source location and may have a null body span.

## Empty-cell semantics

`no_qualifying_evidence_identified` means only that the completed review found no qualifying evidence for that dimension in that source record. It never asserts historical absence.

## Validation

At each final batch checkpoint run at minimum:

```bash
python3 scripts/validate_research_r15_dimensions.py --root .
python3 scripts/validate_r15_purananuru_production.py --root .
pytest -q
```

The full PR workflow additionally covers R0/R1/R1.5 validation, deterministic R1 and R1.5 regeneration, repository audit, Corpus 1.1.0/Tolkāppiyam non-drift, R1 history preservation, and documentation continuity.
