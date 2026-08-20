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
- Tolkāppiyam production: எழுத்ததிகாரம் and all nine சொல்லதிகாரம் இயல் complete; பொருளதிகாரம் / அகத்திணையியல் next
- R2: blocked / not started

R1.5A keeps schema `0.3.0` and the same exact 29 dimensions.

## Puṟanāṉūṟu completed state

Puṟanāṉūṟu `001–400` is complete and validated at 400 reviewed / 0 remaining / 7,169 observations / 29 dimensions.

Durable cadence history remains benchmark `001–002`, stabilization **003–010**, regular **25-record** batches from **011–035** through `361–385`, then final `386–400`.

## Tolkāppiyam production contract

Tolkāppiyam is a separate grammatical/poetics evidence stream over the frozen `3 அதிகாரம் / 27 இயல் / 1,602 நூற்பா` hierarchy.

Per-நூற்பா review distinguishes formal grammatical/poetics concept evidence, incidental examples, and no qualifying evidence identified. Only formal evidence enters `research/observations/tolkappiyam/r15-production.ndjson`; incidental examples stay in the record and are never automatic historical/lived-life claims.

The old Tolkāppiyam manifest/crosswalk remains representative control evidence only and never a classifier.

## Current Tolkāppiyam boundary through சொல்லதிகாரம்

`0001–0946` is the current materialized gap-free production prefix:

- reviewed: **946 / 1,602**;
- remaining: **656**;
- next: **tolkappiyam-0947**;
- next இயல்: **பொருளதிகாரம் / அகத்திணையியல் `0947–1004`**;
- formal grammatical/poetics concept evidence: **1,375**;
- incidental examples: **220**;
- dimensions per record: **29**;
- regression suite: **228 passed** at materialization.

Completed எழுத்ததிகாரம் இயல்:

- `0001–0033` — நூல் மரபு;
- `0034–0082` — மொழி மரபு;
- `0083–0103` — பிறப்பியல்;
- `0104–0143` — புணரியல்;
- `0144–0173` — தொகைமரபு;
- `0174–0203` — உருபியல்;
- `0204–0296` — உயிர்மயங்கியல்;
- `0297–0406` — புள்ளிமயங்கியல்;
- `0407–0483` — குற்றியலுகரப்புணரியல்.

Current reviewed specs include all boundaries through `research/production/tolkappiyam/review-specs/0482-0483.json`.

## Durable boundaries through 0483

Earlier நூல் மரபு, மொழி மரபு, பிறப்பியல், புணரியல், தொகைமரபு and உருபியல் guardrails remain binding, including contextual treatment of grammatical `உயிர்`, `மெய்`, `இசை`, `காலை`, `பொருள்`, `உயர்திணை`, `அஃறிணை`, `தொழில்`, articulation anatomy, measure vocabulary, learned-authority formulas, `மரப்பெயர்`, `திசைப் பெயர்`, and grammatical `இயற்கை` / `செயற்கை`.

### உயிர்மயங்கியல் 0204–0228

The first 25 உயிர்மயங்கியல் நூற்பா were reviewed sequentially/source-first across all 29 dimensions before control comparison. This boundary adds **33 formal observations** and **3 incidental examples**.

- The dominant formal layer is `knowledge.grammar.morphophonology`: doubling, addition, loss, lengthening, alternation and default boundary behavior are recorded only where source-explicit.
- `knowledge.grammar.morphology` is used where the source actually assigns or delimits grammatical form classes, சாரியை or உருபு behavior.
- `knowledge.grammar.word_structure` is used for explicit structural categories such as `தொடர்மொழி`, `தொடர் அல்`, `இரு பெயர்த் தொகைமொழி` and `ஓரெழுத்து மொழி`.
- 0208 grammatical `உயிர்` means vowel and is not body/health/life evidence.
- 0209 `செய்யுளுள்` and 0214 `செய்யுள் கண்ணிய` support the narrow formal `textual.poetic_form.formal_context`; neither identifies an external work nor establishes a historical performance event.
- 0218 `மரப்பெயர்` is retained as incidental tree-name/flora-language only.
- 0219 `மகப்பெயர்` is a grammatical lexical-class label, not historical family/gender/kinship evidence.
- 0223 `புலவர்` / `என்மனார் புலவர்` remain incidental learned-role/attribution evidence only.
- 0225 exact forms `ஆ` / `மா` are not silently resolved into fauna.
- 0228 `இரா` is the grammatical form governed by the rule and is not promoted into historical time/night evidence.

### உயிர்மயங்கியல் 0229–0253

The second 25 உயிர்மயங்கியல் நூற்பா were reviewed sequentially/source-first across all 29 dimensions before control comparison. This boundary adds **30 formal observations** and **7 incidental examples**.

- 0229 `நிலா` is preserved as the exact lexical form of the grammatical rule; it is not promoted into a historical calendrical/environmental observation.
- 0230 `யாமரம்`, `பிடா`, `தளா` and 0232 `மாமரக் கிளவி` remain incidental flora-language inside grammatical example sets; they do not establish historical ecology/cultivation.
- 0232 exact `ஆ` / `மா` remain unresolved grammatical forms rather than automatic fauna evidence.
- 0235 and 0238 explicit `செய்யுளுள்` support narrow `textual.poetic_form.formal_context`, not external-work identity or historical performance.
- 0237 `காலை` and `இடம்` remain grammatical wording, not historical time/geography.
- 0240 `பதக்கு` / `தூணி` remain exact lexical forms inside a grammatical comparison and are not promoted into historical economy/metrology.
- 0242 `பனி` is incidental weather/season-language inside a morphology rule; 0243 `வளி` is incidental environmental language inside a grammatical rule.
- 0244 `உதிமரம்`, 0245 `புளிமரம்`, and 0246 `புளிப் பெயர்` remain incidental flora-language only.
- 0248 `தொழில்நிலைக் கிளவி` is grammatical rather than occupation evidence; `நாள்` is not promoted into a historical date/event.
- 0249 `திங்கள்` remains the lexical form governed by the morphology rule, not a historical calendrical assertion.
- 0251–0252 `இடம் வரை கிளவி` is a grammatical class, not geography; 0252 `உடன் நிலை மொழி` supports formal `knowledge.grammar.word_structure`.
- No new controlled concept was required for `0229–0253`.

Across உயிர்மயங்கியல் `0204–0253`, the two completed publication boundaries add **63 formal observations** and **10 incidental examples**.

### உயிர்மயங்கியல் 0254–0278

Reviewed spec: `research/production/tolkappiyam/review-specs/0254-0278.json`.

This boundary adds **31 formal grammatical/poetics observations** and **3 incidental examples**. `காலை`, `இடன்`, grammatical `மெய்`, `இயற்கை`, and `எண்` remain contextual; `எரு` / `செரு` are not promoted into historical landscape, agriculture, or warfare claims; `ஒடுமரம்` / `உதி மரம்` and `பூ` remain incidental flora-language; `ஆடூஉ` / `மகடூஉ` remain grammatical பெயர் forms rather than historical kinship/gender claims; `என்மனார் புலவர்` remains an incidental learned-authority formula; `செய்யுள் மருங்கின்` supports only narrow formal poetic-text context. No new controlled concept was required.

### உயிர்மயங்கியல் 0279–0296 — complete

Reviewed spec: `research/production/tolkappiyam/review-specs/0279-0296.json`.

This final boundary adds **22 formal grammatical/poetics observations** and **10 incidental examples**. Across உயிர்மயங்கியல் `0204–0296`, the four boundaries contribute **116 formal observations** and **23 incidental examples**. Durable guards preserve tree/plant names, `பெற்றம்`, calendrical/weather terms, emotional lexical forms, grammatical `மெய்` / `உயிர்` / `இயற்கை`, and learned-authority formulas without unsupported historical promotion. No new controlled concept was required.

### புள்ளிமயங்கியல் 0397–0406 — complete

Reviewed spec: `research/production/tolkappiyam/review-specs/0397-0406.json`.

This final boundary adds **12 formal grammatical/poetics observations** and **2 incidental examples**. Across புள்ளிமயங்கியல் `0297–0406`, five publication boundaries contribute **136 formal observations** and **21 incidental examples**. Durable guards preserve grammatical class labels, kinship/name formulas, learned-authority and inherited-tradition wording, quantification, environmental/material/fauna/flora lexical examples, and ambiguous forms without unsupported historical promotion. No new controlled concept was required.

## Current stream-specific concepts

The Tolkāppiyam extension registry includes:

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

Normal publication preference remains contiguous chunks of at most 25 records. உயிர்மயங்கியல் uses `0204–0228`, `0229–0253`, `0254–0278`, `0279–0296`.

After உயிர்மயங்கியல், canonical order requires **புள்ளிமயங்கியல் `0297–0406`** before **குற்றியலுகரப்புணரியல் `0407–0483`**. Do not skip புள்ளிமயங்கியல் to reach குற்றியலுகரப்புணரியல்.

## Source terminology boundary

`docs/SOURCE_TERMINOLOGY_POLICY.md` remains mandatory. Retain exact Tamil and do not silently map source terms to later caste/community, hierarchy, sectarian, deity, taxonomy or modern identity categories. Tolkāppiyam formal categories and incidental examples are not automatic historical claims.

Tolkāppiyam evidence must never auto-classify Puṟanāṉūṟu or another Sangam poem.

## Current operational documents

The current authority set includes `PROJECT_GUIDELINES.md`, `PROJECT_HANDOVER.md`, `NEXT_CHAT_PROMPT.md`, this file, `docs/SOURCE_TERMINOLOGY_POLICY.md`, the R1.5A production handover, the Puṟanāṉūṟu/Tolkāppiyam production READMEs, the Tolkāppiyam observation README, schemas, concept extension, old manifest/crosswalk controls, materializer and validator.

Historical handovers/audits remain truthful records of their own boundaries.

## குற்றியலுகரப்புணரியல் — complete

The four boundaries `0407–0431`, `0432–0456`, `0457–0481`, and `0482–0483` contribute **151 formal observations** and **16 incidental examples**. Formal morphophonology, morphology, word structure, quantification, and narrow poetic/tradition contexts remain distinct from incidental tree, fauna, gender, directional, measure, and learned-authority language. No new controlled concept was required.

## சொல்லதிகாரம் — complete

All nine சொல்லதிகாரம் இயல் are complete through `0946`: கிளவியாக்கம், வேற்றுமையியல், வேற்றுமைமயங்கியல், விளிமரபு, பெயரியல், வினையியல், இடையியல், உரியியல், and எச்சவியல். Together they add **713 formal observations** and **137 incidental examples**.

## Next activity

Next canonical record is `tolkappiyam-0947`, beginning **பொருளதிகாரம் / அகத்திணையியல் `0947–1004`**. Do not enter பொருளதிகாரம் without a new user-directed iteration.

**Do not start R2.**
