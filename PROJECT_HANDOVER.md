# Sangam Literature Corpus — Project Handover

## Authoritative current state

Repository: `pugazg/sangam-literature-corpus`

Default branch: `main`

Active research branch: `research/classical-tamil-concept-matrix-r1.5a`

R1.5 was explicitly authorized and merged into `main` at `d82f9c78f27f9c9daf8fbb913d01ddfb29bddba1`. PR #3 is historical/merged. Draft PR #4 is the active R1.5A proposal.

R1.5A keeps concept/observation schema `0.3.0`; it is not R2. **R2 remains blocked and must not start without later explicit user authorization.** Treat current GitHub state, branch head, open PRs and checks as authoritative over older prose.

## Frozen corpus and preserved layers

Classical Tamil Corpus 1.1.0 remains frozen: 28 works / 7,234 canonical records / 5,632 poems / 1,602 Tolkāppiyam நூற்பா. Tag: `classical-tamil-corpus-v1.1.0`.

R0 schema `0.1.0` remains preserved: 2,867 assertions / 285 literary-body candidates / 43 pilot surface-form entities / 51 relationships.

R1 schema `0.2.0` remains preserved: 8 append-only review events / 3 conservative entity-resolution decisions / 0 verified historical identities.

R1.5 schema `0.3.0` remains the exact 29-dimension concept/evidence foundation. The exhaustive pre-merge Puṟanāṉūṟu and Tolkāppiyam audit remains control evidence only and must never be copied mechanically into production.

## R1.5A — Puṟanāṉūṟu production review complete

Canonical progress is the longest gap-free prefix under `research/production/purananuru/records/`.

Current materialized and validated production boundary:

- `001.json` through `400.json` form the complete gap-free Puṟanāṉūṟu production corpus;
- benchmark **001–002** is complete;
- stabilization batch **003–010** is complete;
- regular 25-record semantic batches **011–035** through **361–385** are complete;
- final 15-record batch **386–400** is complete;
- records reviewed: **400**;
- records remaining: **0**;
- next Puṟanāṉūṟu record: **none**.

Authoritative completion figures from normal PR workflow `32265906972`:

- production observations checked: **7,169**;
- canonical dimensions: **29**;
- regression suite: **224 passed**;
- R0/R1/R1.5 validation: **pass**;
- deterministic R1/R1.5 regeneration: **pass**;
- repository audit: **pass**;
- Corpus 1.1.0 / Tolkāppiyam non-drift: **pass**;
- R1 primary-history preservation: **pass**;
- Tolkāppiyam production observation count: **0**.

All 400 production records were reviewed source-first. Exact evidence/provenance, reviewed-empty states, ambiguity, damaged/source-lost conditions, source terminology, and metadata/body/source-note boundaries remain part of the durable production record.

## Final 386–400 publication cadence

All 15 poems were reviewed completely and sequentially before the old 351–400 control ledger was opened. Durable publication uses three compact reviewed specs:

- `386-390.json`
- `391-395.json`
- `396-400.json`

The split changes Git/materialization granularity only. It does not permit batched semantic guessing, skipped poems, audit-first classification or weakened provenance review.

A construction-only malformed `391-395.json` serialization and temporary diagnostic workflow/log were used only to isolate one missing closing brace; the corrected spec materialized normally. The diagnostic workflow was restored and the debug log removed. None of those construction artifacts may survive the final squash.

`scripts/materialize_r15a_purananuru_batch.py` remains a deterministic materializer, not a classifier. `scripts/materialize_r15a_purananuru_batch_driver.py` remains the range-aware source-state compatibility layer; **no new driver rule was required for 386–400**.

Current exact unknown-poet/non-identification literals handled by the driver remain:

- `பெயர் தெரிந்திலது`
- `பெயர் புலனாகவில்லை`
- `பாடப்பட்டோர் : பெயர்கள் தெரிந்தில`
- `, பாடப்பட்டோர், திணை, துறை தெரிந்தில`

The driver also treats addressee `பெயர் தெரிந்திலது` as explicit non-identification during named-entity linking, then restores the exact printed metadata value. These rules preserve frozen source state; they do not classify records or resolve identities.

A pre-existing R0 body assertion may attach only when its type belongs to a dimension already selected by fresh review and its exact source text lies inside selected evidence.

## Source terminology rule

`docs/SOURCE_TERMINOLOGY_POLICY.md` is mandatory.

Retain the exact Tamil term printed by the source. Do not silently substitute later identity, hierarchy, caste/community, sectarian, deity, taxonomy, modern-community or external-influence labels. Source metadata, canonical body and printed source-note evidence remain distinct. Null/blank metadata stays null/blank. Printed names remain source mentions unless independently resolved.

## Important 386–400 fidelity/provenance lessons

- 386 records direct salt-pricing/exchange from `சிறுவெள் உப்பின் கொள்ளை சாற்றி` / `உமண்`; maritime vessels remain transport evidence; `வெள்ளி` stays source celestial/prognostic wording; `எந்தை` is father-like patron language, not genealogy.
- 387 preserves tribute `பணிதிறை`, gifts, fortification, animals and cultivation; exact `பூழியர்` and body `பொருநை` remain source-level/unresolved; tribute is not converted into trade.
- 388 preserves drought/`வெள்ளி`, cultivation and body `மருகன்` as source kinship/relational wording. Poet-name `மகனார்` is not independently expanded into historical genealogy; `எந்தை` is not genealogy.
- 389 preserves summer/drought, hunger relief, elephants/calves, `வேங்கடம்`, old-age and women’s source wording without market or identity expansion.
- 390 is incomplete/lacunose and is not reconstructed; exact `ஆயர்`, fortified urban space, clothing replacement, food/paddy gifts, elephants and performance remain source-bounded.
- 391 preserves rainfall/yield, hunger/migration, wetland/fish ecology and `நெஞ்சமர் காதல் நின்வெய் யோளடு` as source intimate/gender relationship wording without narrower legal-status inference; `வேங்கட` remains unresolved.
- 392 preserves exact `அணங்குடை மரபு` as source sacred/ritual-power wording without later deity/sectarian/doctrinal identification; war wounds, donkey-ploughing and millet seed remain direct evidence. Printed addressee `மகன்` is metadata kinship only; `கரும்பு இவண் தந்தோன்` is not expanded into a diffusion/external-influence claim.
- 393 remains incomplete/lacunose; exact `குடிமுறை`, `ஒக்கல்`, poverty/hunger, relief, `காவிரி`, summer and performance remain source-bounded without reconstruction.
- 394 records elephant gifts and performance as patronage, not market exchange; `தந்தை` in the ruler/song phrase is not treated as literal genealogy.
- 395 preserves exact `உழவர்`, rich cultivation/food/bird/fish/performance evidence, printed addressee `மகன்`, and body household-woman wording without external genealogy or narrower legal-status projection.
- 396 remains incomplete/lacunose; exact `கோசர்`, `வேள்`, `ஒக்கல்`, food/drink and performance remain source-bound. Its moon/star-like comparison is praise imagery and is not treated as an actual astronomical occurrence; `எந்தை` is not genealogy.
- 397 keeps canonical `பாடாண் / பரிசில் விடை`; printed `கடைநிலை விடையும் ஆம்` is additional TT/TIR and does not overwrite metadata. Exact `அறுதொழில் அந்தணர்` / ritual-fire wording stays source-level without later caste, sectarian or deity mapping; `வெள்ளி` remains source time/celestial wording.
- 398 remains incomplete/lacunose; rooster is direct fauna, while tiger/serpent comparisons remain imagery rather than animal-occurrence claims. Exact `பாணர்`, `பரிசிலர்`, `ஒக்கல்` remain source terminology.
- 399 remains incomplete/lacunose; frozen combined `thinai_as_printed` `பாடாண் துறை: பரிசில் விடை` is preserved exactly. Exact `அறவர்`, `மறவர்`, `மள்ளர்`, `தொல்லோர்` remain source terms; `கடவுட்கும் தொடேன்` stays source religious/ethical wording without deity identification. `விடுமீன் நொடுத்துக்` is narrow fish-transaction evidence only; no wider market system is inferred. Body `காவிரி` / `கிள்ளி வளவன்` remain separate unresolved mentions from metadata addressee `தாமான் தோன்றிக்கோன்`.
- 400 remains incomplete/lacunose; `வெண் திங்கள்`, `மூ வைந்தான் முறை முற்றக்` remain source lunar/calendrical wording without modern astronomical equivalence. Exact `வேள்வித் தூண்` and `மறவர்` remain source-level. Ships, river channels and ports support transport/infrastructure/practical knowledge but **not trade** absent printed goods/exchange; `எந்தை` is not genealogy.

Earlier lessons remain binding, including record 176, damaged record 200, source-lost records 267–268, and all earlier terminology/source-state/provenance guardrails.

## Puṟanāṉūṟu completion boundary

The R1.5A Puṟanāṉūṟu production pass is complete at **001–400** and has passed the full validation boundary. Do not reopen or mechanically rewrite completed records merely to align them with the older sparse audit.

The prerequisite that blocked Tolkāppiyam production has therefore been satisfied. The **next permitted activity is a separate Tolkāppiyam R1.5A production pass**, using Tolkāppiyam as its own evidence stream and the same exact 29-dimension/source-first/provenance discipline. Before the first Tolkāppiyam production mutation, inspect the current Tolkāppiyam source structure, existing R1.5 crosswalk/control artifacts, schema/validator readiness, and define the deterministic record/cadence contract from current repository state.

This permission to begin Tolkāppiyam production does **not** authorize R2. R2 remains blocked.

## Validation requirement

The final Puṟanāṉūṟu checkpoint must finish on one user-authored/squashed branch head parented directly by the previous green checkpoint `bf7e0e168fd05476a99b0ee8615ddc324694924d`, with the full normal PR workflow green on that exact SHA.

The final checkpoint must preserve exact 29-dimension validation, complete Puṟanāṉūṟu production validation, full regression, R0/R1/R1.5 validation, deterministic R1/R1.5 regeneration, repository audit, Corpus/Tolkāppiyam non-drift, R1 primary-history non-mutation, and documentation continuity.

## Current documentation authority

Read in this order:

1. `docs/DOCUMENTATION_STATUS.md`
2. `docs/SOURCE_TERMINOLOGY_POLICY.md`
3. `PROJECT_HANDOVER.md`
4. `PROJECT_GUIDELINES.md`
5. `NEXT_CHAT_PROMPT.md`
6. `docs/handover/r15a-production-review/README.md`
7. `research/production/purananuru/README.md`
8. `docs/CLASSICAL_TAMIL_RESEARCH_MATRIX.md`
9. `docs/classical-tamil-research-layer.md`
10. `docs/handover/r15-premerge-audit/04-29-DIMENSION-PRODUCTION-REVIEW.md` as historical/control methodology.

## Next permitted activity

First confirm the final/squashed Puṟanāṉūṟu 001–400 checkpoint and exact-head CI are green. Then begin the **Tolkāppiyam R1.5A production-pass startup/review design** as a separate evidence stream.

Do not start R2.
