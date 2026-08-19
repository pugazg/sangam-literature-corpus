# Puṟanāṉūṟu R1.5A production review ledger

This directory is the durable record-by-record production layer built on the merged R1.5 exact 29-dimension foundation.

## Hard boundaries

- Current phase: R1.5A. It is not R2.
- R1.5 merged into `main` at `d82f9c78f27f9c9daf8fbb913d01ddfb29bddba1`.
- `corpus/purananuru/` is frozen source material and is never edited by this review.
- The earlier sparse audit under `research/audits/r15-premerge/purananuru/` is control evidence, not the production observation dataset.
- The Tolkāppiyam production pass must not begin until all 400 Puṟanāṉūṟu records are complete and validated.
- `docs/SOURCE_TERMINOLOGY_POLICY.md` is mandatory.

## Canonical ledger

Each reviewed poem is stored as one file under:

`research/production/purananuru/records/NNN.json`

Progress is the longest gap-free prefix beginning at `001`; prose status is not the authoritative progress counter.

Current materialized gap-free prefix: **001–310**.

- benchmark: 001–002;
- stabilization batch: **003–010** complete;
- regular 25-record batches: **011–035**, **036–060**, **061–085**, **086–110**, **111–135**, **136–160**, **161–185**, **186–210**, **211–235**, **236–260**, **261–285**, **286–310** complete;
- next record: **311**;
- next batch: **311–335**.

Current validated figures: **310 reviewed / 90 remaining / 5,430 production observations / 29 canonical dimensions / 224 tests passed**.

Before record `NNN+1` is read, that record's complete semantic decision state must already be complete. Git publication/materialization may batch already-completed records.

Every record must:

1. identify the exact frozen canonical record and R0 assertion snapshot;
2. consider the exact 29 canonical dimensions in registry order;
3. distinguish qualifying evidence from reviewed-empty dimensions;
4. retain exact source Tamil and body-relative line/character spans for body evidence;
5. retain real R0 assertion IDs where an existing assertion genuinely supports an already-reviewed observation;
6. mark genuinely new evidence as `direct_r15_source_review_no_prior_assertion` rather than inventing an R0 assertion;
7. preserve metadata/body/source-note provenance distinctions;
8. keep printed names as source mentions unless separately resolved;
9. preserve damaged/source-lost states without reconstruction;
10. compare against the old sparse audit only after fresh source review is complete.

## Reviewed batch specs and materialization

Compact source-first reviewed batch specs live under:

`research/production/purananuru/review-specs/`

Completed current spec:

- `286-310.json`

The 261–285 and 286–310 batches prove that one complete contiguous 25-record reviewed spec can be materialized safely in a single workflow cycle. This is the preferred low-latency method when the full batch can be completed in one session.

**This does not batch semantic review.** Each poem is still read strictly sequentially and source-first, with its complete 29-dimension decision state finished before moving to the next poem. The old audit remains post-review control only. Split specs remain valid if a session cannot finish the whole batch or a source-state problem requires isolation.

`scripts/materialize_r15a_purananuru_batch.py` deterministically expands already-reviewed semantic decisions into canonical records. It computes evidence spans, source/R0 blob identities, deterministic observation IDs, dimension-review rows and post-review audit discrepancies.

`scripts/materialize_r15a_purananuru_batch_driver.py` is the range-aware source-state compatibility layer. It selects the correct 50-record audit-control TSV per record, handles specs crossing audit-part boundaries, accepts absent source-note blocks, preserves blank canonical `thurai`, and preserves exact unknown poet metadata while excluding explicit non-identification phrases from named-entity linking.

Current exact unknown-poet literals handled by the driver:

- `பெயர் தெரிந்திலது`
- `பெயர் புலனாகவில்லை`

The driver stores the literal, temporarily exposes null to core named-entity linking, then restores the exact printed value in `source_metadata_reviewed.poet_as_printed`. This is source-state compatibility only; it does not classify semantics.

Neither script is an automatic semantic classifier. A pre-existing R0 body assertion may be auto-attached only when its assertion type belongs to a dimension already selected by fresh review and its exact source text occurs inside selected evidence.

After one-pass materialization, perform targeted checks for source-loss, lacunae, metadata/body/source-note boundaries and important audit discrepancies; obtain the actual observation count from the normal verifier; update docs once; squash to one user-authored checkpoint parented by the prior green checkpoint; then run final exact-head CI once.

## Source-state lessons from 286–310

- Record 287 preserves exact `புலைய` and `இழிசின` without later caste/community substitution.
- Record 288 remains incomplete/lacunose and only surviving source evidence is classified.
- Record 289 keeps null thinai/thurai; `திணை, துறை. தெரிந்தில.` is explicit classification-uncertainty TIR, with `உழவன்`, `தொல்குடி`, `பாண`, `இழிசினன்` retained literally.
- Record 294 preserves `கூற்றுவினை` as source death-agent imagery without later deity/doctrine mapping.
- Record 296 preserves `வேம்பு`, `காஞ்சி`, நெய் and `ஐயவி` smoke without later ritual/medical-system mapping.
- Record 297 preserves `பாடினோர் பாடப்பட்டோன் : பெயர்கள் தெரிந்தில.` as unresolved attribution TIR; `named_entities` remains reviewed-empty.
- Record 298 has no source-note block and null thinai/thurai/poet/addressee; these source states remain unchanged and `named_entities` is reviewed-empty.
- Record 299 preserves canonical `நொச்சி / குதிரை மறம்` TT and literal `அணங்குஉடை முருகன் கோட்டத்துக் / கலம்தொடா மகளிர்`; body `முருகன்` is a source-explicit named sacred referent only, without later doctrinal/temple/caste expansion.
- Record 302 preserves `வெறிபாடிய காமக் கண்ணியார் (காமக் கணியார் எனவும் பாடம்)` and the alternate attribution as TIR.
- Record 305 preserves exact `பார்ப்பான்` / `பார்ப்பன வாகை` without later caste/doctrinal substitution.
- Record 306 remains incomplete/lacunose and preserves `நடுகல் கைதொழுது பரவும்` as explicit memorial-stone honoring/worship and death-memory evidence.
- Record 307 preserves exact `பெயர் புலனாகவில்லை`; `named_entities` remains reviewed-empty and the unknown-attribution source note is TIR.

Earlier provenance and terminology guardrails remain binding, including record 176, record 200, source-lost records 267–268 and all prior source-state lessons.

## R1.5A cadence

The review is sequential; repository publication is batched.

- benchmark: 001–002;
- completed stabilization batch: **003–010**;
- completed regular 25-record batches: **011–035**, **036–060**, **061–085**, **086–110**, **111–135**, **136–160**, **161–185**, **186–210**, **211–235**, **236–260**, **261–285**, **286–310**;
- next batch: **311–335**;
- subsequent cadence: **336–360, 361–385, 386–400**;
- final batch ends exactly at 400;
- prefer one contiguous 25-record spec + one materialization cycle when the whole batch is complete in-session;
- one clean user-authored/squashed Git checkpoint per completed batch;
- full final PR CI/non-drift on the exact squashed head;
- if a session cannot complete the planned batch, checkpoint only the completed contiguous prefix.

This cadence must never be used to skip sequential semantic review or copy the control ledger into production.

## Evidence spans

For `canonical_body` evidence, `evidence_span.start_line` and `end_line` are 1-based poem-body line numbers. Character offsets are 0-based Unicode string positions within cited body lines. `source_text` must reproduce the frozen source slice exactly.

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

The full PR workflow additionally covers R0/R1/R1.5 validation, deterministic R1/R1.5 regeneration, repository audit, Corpus 1.1.0/Tolkāppiyam non-drift, R1 history preservation and documentation continuity.
