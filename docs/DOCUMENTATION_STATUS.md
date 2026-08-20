# Documentation status — R1.5A production review

## Live phase state

- repository: `pugazg/sangam-literature-corpus`
- default branch: `main`
- R1.5 merge commit on `main`: `d82f9c78f27f9c9daf8fbb913d01ddfb29bddba1`
- PR #3: merged / historical
- active branch: `research/classical-tamil-concept-matrix-r1.5a`
- active PR: #4, draft/unmerged
- current phase: R1.5A production review
- Puṟanāṉūṟu production: complete
- Tolkāppiyam production: active through எழுத்ததிகாரம் / தொகைமரபு
- R2: blocked / not started

R1.5A keeps schema `0.3.0` and the same exact 29 dimensions.

## Puṟanāṉūṟu completed state

Puṟanāṉūṟu `001–400` is complete and validated at 400 reviewed / 0 remaining / 7,169 observations / 29 dimensions.

Durable cadence history remains benchmark `001–002`, stabilization **003–010**, regular **25-record** batches from **011–035** through `361–385`, then final `386–400`.

## Tolkāppiyam production contract

Tolkāppiyam is a separate grammatical/poetics evidence stream over the frozen `3 அதிகாரம் / 27 இயல் / 1,602 நூற்பா` hierarchy.

Per-நூற்பா review distinguishes formal grammatical/poetics concept evidence, incidental examples, and no qualifying evidence identified. Only formal evidence enters `research/observations/tolkappiyam/r15-production.ndjson`; incidental examples stay in the record and are never automatic historical/lived-life claims.

The old Tolkāppiyam manifest/crosswalk remains representative control evidence only and never a classifier.

## Current Tolkāppiyam boundary

`0001–0173` is the validated gap-free production prefix:

- reviewed: **173 / 1,602**;
- remaining: **1,429**;
- next: **tolkappiyam-0174**;
- formal grammatical/poetics concept evidence: **218**;
- incidental examples: **20**;
- dimensions per record: **29**;
- regression suite: **228 passed**.

Completed இயல்:

- `0001–0033` — எழுத்ததிகாரம் / நூல் மரபு;
- `0034–0082` — எழுத்ததிகாரம் / மொழி மரபு;
- `0083–0103` — எழுத்ததிகாரம் / பிறப்பியல்;
- `0104–0143` — எழுத்ததிகாரம் / புணரியல்;
- `0144–0173` — எழுத்ததிகாரம் / தொகைமரபு.

The latest activity reviewed **91 நூற்பா sequentially/source-first** across the three requested இயல். Publication remained as three separate contiguous specs, one per இயல்: `0083-0103.json`, `0104-0143.json`, and `0144-0173.json`.

## Durable 0083–0173 boundaries

### பிறப்பியல் 0083–0103

- Tolkāppiyam formally systematizes articulatory anatomy and breath pathways (`மிடறு`, `நெஞ்சு`, `பல்`, `இதழ்`, `நா`, `மூக்கு`, `அண்ணம்`, etc.) under `body.articulation.anatomy`. This is grammatical articulatory evidence, not medicine or diagnosis.
- 0102 preserves exact `அளபின் கோடல் அந்தணர் மறைத்தே`: `அந்தணர்` is an incidental learned/authority role and the phrase is a formal unresolved tradition reference. No later caste, community, sectarian or doctrinal identity is substituted.

### புணரியல் 0104–0143

- Formal grammar now distinguishes `knowledge.grammar.morphology` from `knowledge.grammar.morphophonology`.
- `வேற்றுமை உருபு`, `சாரியை`, grammatical பெயர்/தொழில் and boundary alternations remain grammatical system evidence.
- `உயர்திணை` / `அஃறிணை` are grammatical noun classes, not historical social hierarchy or gender claims.
- 0125 `நாள்` is only incidental time-language inside a form rule; 0131 `புலவர்` / `என்மனார் புலவர்` remain incidental learned-role/attribution evidence.
- `உடம்படுமெய்`, grammatical `தொழில்`, and grammatical `பொருள்` are not promoted into body, occupation, economy or lived-world evidence.

### தொகைமரபு 0144–0173

- Formal quantity grammar uses `knowledge.grammar.quantification` for `அளவு`, `நிறை`, `எண்` and related expressions while retaining morphophonology/morphology separately.
- Measure vocabulary such as `அரை`, `கலம்`, `பனை`, `கா`, `அளவு`, `நிறை` is preserved as incidental economy/measurement language only; it does not establish a historical market or standardized metrology.
- In 0170, `பனை` names a measure expression in the rule and is not promoted to flora.
- Learned-authority formulas such as `புலவர்` / `என்மனார் புலவர்` remain incidental rather than resolved historical identities or texts.

## Current stream-specific concepts

The Tolkāppiyam extension registry now includes:

- `knowledge.grammar.phonology`;
- `knowledge.grammar.word_structure`;
- `knowledge.grammar.morphology`;
- `knowledge.grammar.morphophonology`;
- `knowledge.grammar.quantification`;
- `body.articulation.anatomy`;
- `arts.music.formal_context`;
- `textual.tradition.reference`;
- `textual.poetic_form.formal_context`.

## Publication cadence

Semantic review is always one நூற்பா at a time, source-first, and a production spec never crosses an இயல் boundary.

Normal publication preference remains contiguous chunks of at most 25 records. The earlier full 49-record மொழி மரபு spec was an explicit user-authorized exception. In the current activity, the user authorized completing three இயல் together, but each இயல் remains its own production spec.

Next இயல் is **உருபியல் 0174–0203 (30 records)**. Under normal cadence it should be split inside the இயல் into `0174–0198` and `0199–0203` unless the user explicitly requests another full-இயல் >25 publication exception.

## Source terminology boundary

`docs/SOURCE_TERMINOLOGY_POLICY.md` remains mandatory. Retain exact Tamil and do not silently map source terms to later caste/community, hierarchy, sectarian, deity, taxonomy or modern identity categories. Tolkāppiyam formal categories and incidental examples are not automatic historical claims.

Tolkāppiyam evidence must never auto-classify Puṟanāṉūṟu or another Sangam poem.

## Current operational documents

The current authority set includes:

- `README.md`
- `PROJECT_GUIDELINES.md`
- `PROJECT_HANDOVER.md`
- `NEXT_CHAT_PROMPT.md`
- `docs/DOCUMENTATION_STATUS.md`
- `docs/SOURCE_TERMINOLOGY_POLICY.md`
- `docs/CLASSICAL_TAMIL_RESEARCH_MATRIX.md`
- `docs/classical-tamil-research-layer.md`
- `docs/handover/r15a-production-review/README.md`
- `research/production/purananuru/README.md`
- `research/production/tolkappiyam/README.md`
- `research/observations/tolkappiyam/README.md`
- `research/audits/r15-premerge/tolkappiyam/review-manifest.json`
- `research/audits/r15-premerge/tolkappiyam/dimension-crosswalk.json`

Historical handovers/audits remain truthful records of their own boundaries.

## Next activity

Proceed with **Tolkāppiyam உருபியல் beginning at 0174**. Keep semantic review sequential/source-first across all 29 dimensions, consult the old control artifacts only after fresh decisions, preserve exact source terminology, and finish each publication boundary with deterministic materialization and full exact-head PR CI.

**Do not start R2.**
