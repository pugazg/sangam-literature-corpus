# Puṟanāṉūṟu R1.5A production review ledger

This directory is the durable record-by-record production layer built on the merged R1.5 exact 29-dimension foundation.

## Hard boundaries

- Current phase: R1.5A. It is not R2.
- R1.5 merged into `main` at `d82f9c78f27f9c9daf8fbb913d01ddfb29bddba1`.
- `corpus/purananuru/` is frozen source material and is never edited by this review.
- The earlier sparse audit under `research/audits/r15-premerge/purananuru/` is post-review control evidence, not the production dataset.
- `docs/SOURCE_TERMINOLOGY_POLICY.md` is mandatory.
- Puṟanāṉūṟu production is now complete; do not reopen records merely to mirror the old audit.

## Canonical ledger

Each reviewed poem is stored as one file under `research/production/purananuru/records/NNN.json`.

Progress is the longest gap-free prefix beginning at `001`; prose status is not the authoritative progress counter.

Current materialized and validated gap-free prefix: **001–400 — complete**.

- benchmark: 001–002 complete;
- stabilization batch: 003–010 complete;
- regular 25-record semantic batches: 011–035 through 361–385 complete;
- final 15-record batch: **386–400 complete**;
- records reviewed: **400**;
- records remaining: **0**;
- next record: **null / none**.

Current validated figures: **400 reviewed / 0 remaining / 7,169 production observations / 29 canonical dimensions / 224 tests passed**.

Every completed record identifies the exact frozen source and R0 snapshot, considers all 29 dimensions, distinguishes qualifying evidence from reviewed-empty states, retains exact source Tamil/spans, preserves metadata/body/source-note distinctions, keeps printed names unresolved unless separately resolved, preserves damaged/source-lost states without reconstruction, and uses the old audit only after fresh source review.

## Final reviewed specs and materialization

The final 386–400 publication uses:

- `386-390.json`
- `391-395.json`
- `396-400.json`

All 15 poems were semantically reviewed sequentially/source-first before the old 351–400 control ledger was opened. The three-spec publication only isolates technical/source-state boundaries; **this never batches semantic review**.

A construction-only malformed 391–395 serialization contained one missing final brace. A temporary diagnostic workflow/log isolated that JSON error; the spec was corrected, materialized normally, the workflow was restored, and the log was deleted. Those construction artifacts are not durable production state and must not survive the final squash.

`scripts/materialize_r15a_purananuru_batch.py` deterministically expands already-reviewed decisions into canonical records. It is not a classifier.

`scripts/materialize_r15a_purananuru_batch_driver.py` remains the range-aware source-state compatibility layer. **No new driver rule was required for 386–400.**

Current unknown-poet literals handled by the driver remain:

- `பெயர் தெரிந்திலது`
- `பெயர் புலனாகவில்லை`
- `பாடப்பட்டோர் : பெயர்கள் தெரிந்தில`
- `, பாடப்பட்டோர், திணை, துறை தெரிந்தில`

The driver also suppresses and restores addressee `பெயர் தெரிந்திலது` during core named-entity linking. These are source-state compatibility rules only.

A pre-existing R0 body assertion may attach only when its type belongs to a dimension already selected by fresh review and its exact source text occurs inside selected evidence.

## Source-state lessons from 386–400

- 386 records direct salt-pricing/exchange from `சிறுவெள் உப்பின் கொள்ளை சாற்றி` / `உமண்`; `வெள்ளி` remains source-level; `எந்தை` is not genealogy.
- 387 preserves tribute `பணிதிறை`, exact `பூழியர்`, unresolved `பொருநை`; tribute is not trade.
- 388 preserves drought/`வெள்ளி`; body `மருகன்` is source kinship wording; poet-name `மகனார்` does not establish independent genealogy; `எந்தை` is not genealogy.
- 389 preserves summer/drought, hunger relief, elephants/calves, `வேங்கடம்`, old-age and women’s source wording without market/identity expansion.
- 390 remains incomplete/lacunose and unreconstructed; exact `ஆயர்` and surviving urban/gift/performance evidence remain source-bounded.
- 391 preserves rainfall/yield, migration/hunger and intimate/gender relationship wording without narrower legal-status inference; `வேங்கட` remains unresolved.
- 392 preserves exact `அணங்குடை மரபு` without later deity/sectarian/doctrinal mapping; printed `மகன்` is metadata kinship only and `கரும்பு இவண் தந்தோன்` does not create a diffusion/external-influence claim.
- 393 remains incomplete/lacunose and unreconstructed; exact `குடிமுறை`, `ஒக்கல்`, relief, `காவிரி`, summer and performance remain source-bound.
- 394 records elephant gifts as patronage, not market exchange; `தந்தை` is not literal genealogy.
- 395 preserves exact `உழவர்`, cultivation/food/bird/fish/performance evidence, printed addressee `மகன்`, and household-woman wording without external genealogy/legal-status projection.
- 396 remains incomplete/lacunose; exact `கோசர்`, `வேள்`, `ஒக்கல்`; the moon/star comparison is praise imagery, not an actual astronomical occurrence; `எந்தை` is not genealogy.
- 397 keeps canonical `பாடாண் / பரிசில் விடை`; source-note `கடைநிலை விடையும் ஆம்` is additional TT/TIR and does not overwrite metadata. Exact `அறுதொழில் அந்தணர்` / ritual-fire wording remains source-level without later caste/sectarian/deity mapping.
- 398 remains incomplete/lacunose; rooster is direct fauna while tiger/serpent comparisons are imagery, not animal-occurrence claims; exact `பாணர்`, `பரிசிலர்`, `ஒக்கல்` remain source terms.
- 399 remains incomplete/lacunose; frozen combined `thinai_as_printed` `பாடாண் துறை: பரிசில் விடை` remains exact. Exact `அறவர்`, `மறவர்`, `மள்ளர்`, `தொல்லோர்` stay source-level; `கடவுட்கும் தொடேன்` does not identify a deity; `விடுமீன் நொடுத்துக்` is narrow fish-transaction evidence only; body and metadata names remain distinct/unresolved.
- 400 remains incomplete/lacunose; lunar/calendrical wording stays source-level without modern astronomical equivalence; exact `வேள்வித் தூண்`, `மறவர்`; ships, river channels and ports support transport/infrastructure/practical knowledge but not trade absent printed exchange; `எந்தை` is not genealogy.

Earlier provenance and terminology guardrails remain binding, including record 176, damaged record 200 and source-lost records 267–268.

## Completed R1.5A Puṟanāṉūṟu cadence

The review was sequential; repository publication was batched.

- benchmark: 001–002;
- stabilization: 003–010;
- 25-record batches: 011–035 through 361–385;
- final batch: 386–400;
- final production corpus: **001–400 complete**;
- one clean user-authored/squashed Git checkpoint is required for the final batch;
- full final PR CI/non-drift must pass on that exact squashed head.

This cadence never permits skipped sequential semantic review or copying the control ledger into production.

## Evidence and empty-cell semantics

For `canonical_body` evidence, spans are 1-based poem-body line numbers with 0-based Unicode character offsets. `source_text` reproduces the frozen source slice exactly. Metadata evidence uses its exact source field/location.

`no_qualifying_evidence_identified` means only that completed review found no qualifying evidence for that dimension in that source record. It never asserts historical absence.

## Validation

The complete Puṟanāṉūṟu production tree passed normal PR workflow `32265906972` with:

- 400 reviewed / 0 remaining / next record null;
- 7,169 production observations;
- 29 canonical dimensions;
- 224 tests passed;
- R0/R1/R1.5 validators green;
- deterministic R1/R1.5 regeneration green;
- repository audit green;
- Corpus 1.1.0/Tolkāppiyam non-drift green;
- R1 primary histories preserved;
- Tolkāppiyam production observation count 0.

The final authoritative batch checkpoint must be one user-authored/squashed commit parented directly by previous green checkpoint `bf7e0e168fd05476a99b0ee8615ddc324694924d`, followed by the full normal PR workflow on that exact SHA.

## Next stream

The former Tolkāppiyam block is satisfied because Puṟanāṉūṟu 001–400 is complete and validated. The next permitted R1.5A work is a **separate Tolkāppiyam production-pass startup/design**, beginning with the frozen 3 அதிகாரம் / 27 இயல் / 1,602 நூற்பா structure and existing R1.5 Tolkāppiyam crosswalk/control artifacts.

Do not mechanically copy crosswalk classifications into production, and do not use Tolkāppiyam to retroactively auto-classify Puṟanāṉūṟu. **R2 remains blocked.**
