# Sangam Text Corpus

## Derived research layer

Development above the immutable corpus release now occurs on the separate
`research/sangam-evidence-r0` branch. The independently versioned Research Layer
R0 (`0.1.0`, pilot) is isolated under `research/` and currently contains only a
Puṟanāṉūṟu evidence pilot. It does not modify or reinterpret the frozen
transcription. See [`docs/classical-tamil-research-layer.md`](docs/classical-tamil-research-layer.md).

## Repository release checkpoint

The repository-wide **Classical Tamil Corpus 1.0.0** checkpoint contains 27
frozen works and 5,632 canonical numbered records: nine core Sangam works and
eighteen Patiṉeṇkīḻkkaṇakku works. The release inventories, protected-condition
register, deterministic content fingerprint, and Git checkpoint are described
in [`docs/classical-tamil-corpus-release-1.0.0.md`](docs/classical-tamil-corpus-release-1.0.0.md).

Before release, an overlapping write to the shared `poems.csv` manifest was
detected. Canonical corpus content was unaffected. The manifest was
semantically reconstructed from all frozen record files, given a documented
canonical ordering policy, and protected by atomic replacement and an advisory
lock. Two serial all-work regeneration passes then produced no path or byte
changes.

## Patiṉeṇkīḻkkaṇakku programme

The Patiṉeṇkīḻkkaṇakku programme is complete. All eighteen independently
reconnoitred works are formally frozen at corpus schema version `1.0.0`.
`முப்பால்` is an alias of Tirukkural, not a separate corpus work, and
`கைந்நிலை` is the selected eighteenth-work tradition; `இன்னிலை` is not a
canonical nineteenth work.

The frozen works are Tirukkural, Nālāṭiyār, Nāṉmaṇikkaṭigai, Iṉṉā Nāṟpatu,
Iṉiyavai Nāṟpatu, Kār Nāṟpatu, Kaḷavaḻi Nāṟpatu, Aintiṇai Aimpathu,
Aintiṇai Eḻupathu, Tiṇaimālai Nūṟṟaimpatu, Tiṇaimoḻi Aimpathu, Tirikaṭukam,
Ācārakkōvai, Paḻamoḻi Nāṉūṟu, Ciṟupañcamūlam, Mutumoḻik Kāñci, Ēlāti, and
Kainnilai.

Corpus schema version: **1.0.0**

## Project purpose

This repository builds reproducible, source-faithful Markdown transcriptions of classical Tamil works published by Project Madurai. It preserves provenance and exposes uncertainty without performing translation, literary interpretation, historical inference, spelling modernization, or silent textual correction. The core programme contains nine works, all formally frozen at corpus schema 1.0.0: Naṟṟiṇai, Aiṅkuṟunūṟu, Kuruntokai, Akanāṉūṟu, Puṟanāṉūṟu, Pattuppāṭṭu, Patiṟṟuppattu, Paripāṭal, and Kalittokai.

## Source and editorial hierarchy

1. **Raw source preservation** — unchanged downloaded bytes and SHA-256 provenance.
2. **Source-faithful canonical transcription** — literary lines after only permitted mechanical transformations.
3. **Source-explicit metadata** — only values printed in the selected Project Madurai source.
4. **Validation and anomaly reporting** — machine checks and review queues, never silent repair.
5. **External textual comparison** — evidence from TamilVU or other sources, isolated under `apparatus/`.
6. **Reviewed editorial interpretation** — not currently permitted.
7. **Literary and historical analysis** — not currently permitted.

Only layers 1–5 may be created in this phase. External evidence cannot overwrite layers 1–3.

## Python and installation

- Python: 3.11 or later
- Dependencies: Beautiful Soup (HTML parsing), lxml (deterministic HTML tree), PyYAML (front matter), certifi (verified HTTPS CA bundle)

```bash
python3 -m venv .venv
. .venv/bin/activate
python3 -m pip install -r requirements.txt
python3 -m unittest discover -s tests -v
```

Dependencies are pinned in `requirements.txt`. TLS verification is never disabled.

## Repository tree

```text
sangam-text-corpus/
├── README.md
├── requirements.txt
├── scripts/
│   ├── corpuslib.py
│   ├── fetch_source.py
│   ├── extract_text.py
│   ├── normalize_text.py
│   ├── split_poems.py
│   ├── build_manifest.py
│   ├── validate_output.py
│   ├── audit_repository.py
│   └── process_work.py
├── sources/
│   ├── raw-html/
│   ├── raw-txt/
│   └── source-metadata/
├── corpus/
│   ├── natrinai/
│   ├── aingurunuru/
│   ├── kuruntokai/
│   ├── akananuru/
│   ├── purananuru/
│   ├── pattuppattu/
│   ├── patirruppattu/
│   ├── paripatal/
│   └── kalittokai/
├── manifests/
├── issues/
├── apparatus/
│   ├── natrinai/
│   ├── aingurunuru/
│   ├── kuruntokai/
│   ├── akananuru/
│   ├── purananuru/
│   ├── pattuppattu/
│   ├── patirruppattu/
│   ├── paripatal/
│   └── kalittokai/
├── logs/
└── tests/
```

Each `corpus/<work>/` directory contains `README.md`, `metadata.json`, `full-text.md`, `poems/`, and work-appropriate navigation or structural files. Shared manifests, issues, apparatus, logs, scripts, and sources remain repository-level directories rather than being nested beneath one work.

## Commands

Complete orchestration:

```bash
python3 scripts/process_work.py \
  --url "https://www.projectmadurai.org/pm_etexts/utf8/pmuni0296.html" \
  --work natrinai --verbose
```

Verification/regeneration from the already-preserved raw HTML, without network access or raw-source replacement:

```bash
python3 scripts/process_work.py natrinai
python3 scripts/process_work.py aingurunuru
python3 scripts/process_work.py kuruntokai
python3 scripts/process_work.py akananuru
python3 scripts/process_work.py purananuru
python3 scripts/process_work.py pattuppattu
python3 scripts/process_work.py patirruppattu
python3 scripts/process_work.py paripatal
python3 scripts/process_work.py kalittokai
python3 scripts/process_work.py tirukkural
python3 scripts/process_work.py naladiyar
# The remaining Patiṉeṇkīḻkkaṇakku slugs are listed in
# manifests/pathinenkilkanakku-program.json and are processed identically.
```

Individual stages:

```bash
python3 scripts/fetch_source.py --url "<PROJECT_MADURAI_URL>" --work natrinai
python3 scripts/extract_text.py --work natrinai
python3 scripts/normalize_text.py --work natrinai
python3 scripts/split_poems.py --work natrinai
python3 scripts/build_manifest.py --work natrinai
python3 scripts/validate_output.py --work natrinai
python3 scripts/validate_output.py --work aingurunuru
python3 scripts/validate_output.py --work kuruntokai
python3 scripts/validate_output.py --work akananuru
python3 scripts/validate_output.py --work purananuru
python3 scripts/validate_output.py --work pattuppattu
python3 scripts/validate_output.py --work patirruppattu
python3 scripts/validate_output.py --work paripatal
python3 scripts/validate_output.py --work kalittokai
python3 scripts/audit_repository.py --root .
pytest -q
```

`--dry-run` previews supported operations, `--verbose` reports progress, and `--force` explicitly permits replacement. Without `--force`, raw HTML and first-pass text are never overwritten. Regeneration from an already-preserved raw source begins at `extract_text.py`.

## Raw-source preservation and checksums

The HTTP response is stored byte-for-byte under `sources/raw-html/`. The fetch metadata records URL, access date, identifier, byte length, SHA-256, and the fact that the raw source was not modified. `sources/raw-txt/` is the first entity-decoded/tag-stripped extraction before canonical normalization. Checksums always describe the raw bytes, not later transcriptions. A changed upstream response therefore produces a changed checksum and requires review.

## Unicode normalization and transformation policy

Permitted automatic operations are HTML entity decoding, Unicode NFC, CRLF/CR to LF conversion, duplicate blank-line removal, removal of webpage boilerplate, and layout-only line-wrap cleanup explicitly supported by the source parser.

Prohibited operations include spelling modernization, typo correction, word splitting/merging, sandhi changes, inferred tiṇai/speaker/poet, deletion of apparent repetition, unreported renumbering, supplementation from external editions, translation, and interpretation. Printed punctuation, unusual characters, lacuna marks, and dash placeholders remain unchanged. Suspected errors belong in `issues/` or `apparatus/`, never in canonical lines.

## Poem splitting and work-specific structure

Naṟṟiṇai poem headings provide the printed number, tiṇai, and poet. Each numbered record becomes `poems/NNN.md`. The unnumbered invocation remains in `full-text.md`. Mechanical 50-poem ranges generate eight `sections/` files; these ranges are navigation aids, not inferred literary divisions.

Aiṅkuṟunūṟu uses the same canonical-file, provenance, fidelity, and physical-inventory guarantees but not Naṟṟiṇai's mechanical sections. Its 500 numbered records are organized into 50 ten-poem source-order groups. Forty-eight groups have printed பத்து headings; the first two do not. Its `sections/` files therefore correspond to exact ten-poem ranges, while `pattu-inventory.json` preserves printed headings, printed ordinals, source order, membership, and anomalies. The five hundred-poem blocks are mechanical navigation divisions with null printed names; the source does not print major-division headings, so conventional tiṇai names are not silently supplied.

Kuruntokai uses Project Madurai `pmuni0110`. Its flat HTML `<br>` grammar contains an unnumbered `கடவுள் வாழ்த்து` followed by 401 continuously numbered records. Each heading prints poem number, tiṇai, and speaker/context; a poet attribution follows each poem. Poems 105 and 180 print the attribution on the same HTML line as the final verse, so the source-specific parser restores only that layout boundary while preserving both strings. The source prints no anthology divisions. Nine generated fifty-poem navigation ranges, ending with `401-401.md`, are explicitly mechanical aids and are not source-printed, ancient, or canonical Kuruntokai divisions.

Akanāṉūṟu uses the complete source-only Project Madurai `pmuni0229` edition. Its table grammar prints an unnumbered invocation as record `0`, 400 numbered literary records, separate numeric line-end layout cells, and three explicit macro-divisions: `களிற்றியாணை நிரை` (1–120), `மணிமிடை பவளம்` (121–300), and `நித்திலக்கோவை` (301–400). Those three divisions, rather than mechanical fifty-poem ranges, generate the section files. The source prints no poem-level tiṇai, speaker/context, or poet attribution. Source-order records 131 and 319 repeat the printed labels 130 and 318; canonical record identity follows continuous source order while the exact printed labels remain in provenance and validation issues. Akanāṉūṟu is formally frozen at corpus schema version `1.0.0`.

Puṟanāṉūṟu uses Project Madurai `pmuni0057` through the exact checksum-pinned user-supplied text export `sources/purananuru.md`, formally approved as the canonical artifact under the documented Option B provenance decision. It has 400 canonical records; the printed combined statement `267- 268 கிடைத்தில` establishes two source-lost records. Printed poet, addressee, tiṇai, and tuṟai are provenance-qualified while speaker remains null. Printed dot lacunae are preserved. No source divisions were detected, so eight fifty-poem files are explicitly mechanical navigation aids. Puṟanāṉūṟu is formally frozen at corpus schema version `1.0.0`; this does not claim raw-HTML preservation.

Pattuppāṭṭu uses ten exact, independently checksum-pinned Project Madurai HTML objects and produces ten ordered long-poem records. Each record retains its own source-object provenance; there is no substitute aggregate checksum. Ten generated source-order navigation mirrors are not ancient divisions. திருமுருகாற்றுப்படை's internal headings remain subordinate structure. The selected முல்லைப்பாட்டு object, `pmuni0488`, is commentary-bearing: its independently extractable literary block is canonical while commentary is isolated in the apparatus. The Project Madurai pages for `pmuni0069`, `pmuni0073`, and `pmuni0077` declare 500, 261, and 301 lines respectively while their BR-delimited literary blocks yield 501, 262, and 302; all printed literary lines are retained without speculative joining. Pattuppāṭṭu is formally frozen at corpus schema version `1.0.0`.

Patiṟṟuppattu uses Project Madurai `pmuni0038`. It preserves the 80 surviving numbered records 11–90 in the eight source-printed பத்து groups numbered 2–9. The source explicitly marks the first and tenth groups unavailable; the pipeline does not manufacture their missing records. Group-level patron and poet statements and poem-level துறை, வண்ணம், தூக்கு, and பெயர் metadata are source notes with provenance. Printed பதிகம் blocks and recovered fragments remain structural evidence outside canonical numbered bodies. Eight section files correspond to the surviving source groups.

Paripāṭal uses Project Madurai `pmuni0087`, whose printed title includes both `பரிபாடல்` and `பரிபாடல்-திரட்டு`. The source has 22 main numbered poems followed by 13 separately printed திரட்டு fragment records whose numbering restarts at 1. Canonical filenames use unique source order 001–035 while `poem_number_as_printed` retains each printed label. Styled topical headings remain subordinate structure; printed attribution and recovery statements remain source notes. Two section files correspond to the two source-printed divisions.

Kalittokai uses Project Madurai `pmuni0221`. Exactly 150 table rows encode poems 1–150; poem 1 is the printed invocation and the remaining poems occupy five named source divisions. Six section files preserve that hierarchy. Division-level author attributions are copied only where printed. Dot lacunae in poems 114 and 131 remain unchanged, and no poem-level speaker or tiṇai is inferred.

## Poem metadata

YAML records identity, numbering, work-appropriate navigation or structure, source-supported tiṇai, speaker/context and poet values, first line, line count, source URL/file/identifier, language/script, extraction status, editorial-change flag, textual status, canonical/candidate availability, lacuna state/location, source-note availability, and field-level provenance. Fields are populated or null according to explicit source support. Allowed `textual_status` values are `complete`, `incomplete`, `lost`, and `uncertain`.

`thinai_source`, `poet_source`, `speaker_source`, and `source_note_source` state where each value came from. Printed uncertainty remains a null structured value with its exact printed form and provenance. Naṟṟiṇai does not map prose descriptions to controlled speaker values; Kuruntokai copies printed speaker/context strings from poem headings. Null is meaningful and must not be replaced by inference.

## Manifests

`works.json` contains one record for every onboarded work. `poems.csv` is the combined poem manifest for all onboarded corpora and has identity and printed metadata; optional work-specific structure; textual/extraction status; body, source, and Markdown SHA-256 values; full-body duplicate and shared-first-line flags; source-output match; source-object paths; validation status; issue count; and notes. Null structural fields are retained where a source does not print them. The current repository inventory is 5,632 canonical numbered records across 27 frozen works; this is a current count, not an architectural maximum. The eighteen-work Patiṉeṇkīḻkkaṇakku programme contributes 3,256 numbered records. Source-explicit unnumbered invocations and prefatory texts remain outside those numbered totals.

`sangam-core-program.json` is the programme-level inventory and completion
record. It pins the nine-work scope, source identities, record counts, freeze
states, and final audit/idempotence results.

`pathinenkilkanakku-program.json` is the corresponding eighteen-work programme
inventory. Its source survey, programme decisions, individual validation
reports, freeze records, and final completion record preserve the decisions
behind counts that differ from title-derived expectations.

The deterministic combined-manifest order and its stable canonical row key are
documented in [`docs/manifest-ordering-policy.md`](docs/manifest-ordering-policy.md).
The aggregator uses atomic replacement and a repository-local advisory lock;
individual printed numbering never determines repository identity.

## Validation rules

Validation checks missing/duplicate numbers, sequence breaks, empty/heading-only poems, unexpected lengths, YAML, required metadata, filenames, section ranges, NFC, replacement characters, possible orphan Tamil combining marks, unidentified fragments, source/output counts, source-note fidelity, source-body versus Markdown-body hashes, shared first lines, and identical normalized full bodies.

A shared first line is informational only. Only identical non-empty normalized full bodies produce `duplicate_poem_body`. Any unexpected source-to-output mismatch is an error.

## Severity levels

- **error** — integrity failure; validation fails and output must not be accepted.
- **warning** — known source/editorial condition requiring human review but not an extraction failure.
- **info** — verified textual condition retained for visibility, such as a legitimate shared opening.

## Manual review process

1. Run tests and validation.
2. Resolve every error before acceptance.
3. Read warning records against the preserved raw source.
4. Confirm informational findings or cite external evidence in `apparatus/`.
5. Record observations without editing canonical poem bodies.
6. Rebuild manifests and compare body hashes after any parser change.

Work-level metadata may be corrected only when the selected source explicitly supports it. Proposed editorial changes must be stored separately and reviewed; raw files and canonical literary lines must remain untouched.

## External comparison sources

External evidence belongs only in `apparatus/<work>/`. Each record must identify source, URL, access date, evidence type, editorial status, affected poem numbers, and a concise comparison. Do not copy an external preferred reading into `corpus/`, replace Project Madurai metadata, or create uncontrolled speaker mappings. If external source files are downloaded later, preserve them in a clearly named apparatus source directory with their own checksums and rights metadata.

## Adding the next Project Madurai work

Do not generalize an existing parser blindly. Preserve the raw source; perform complete source reconnaissance; document its grammar, printed structure, and anomalies; review shared code for hidden work assumptions; and add an explicit parser profile or source-specific parser where required. Preserve source structure separately from mechanical navigation. Then run recursive physical auditing, source/body and source-note fidelity validation, complete regression tests, and hash comparisons for every frozen work. Successful onboarding establishes eligibility; use a separate formal freeze pass. The reusable principle is shared corpus infrastructure plus an explicit source-specific parsing and structural strategy—not a fallback to any existing work parser. Curated work README files are never generator outputs and regeneration must not overwrite them.

## Canonical transcription versus editorial apparatus

`corpus/` answers “what does the selected Project Madurai source print after permitted mechanical normalization?” `apparatus/` answers “what do external sources report or prefer?” An apparatus observation cannot mutate canonical transcription. Layers 6 and 7 remain out of scope.

## Testing

Run the complete regression suite with `pytest -q`. Tests cover heading recognition, Tamil preservation, Unicode NFC, metadata/front matter, lost and incomplete texts, candidate containment, dash preservation, shared openings, full-body distinctions, source-to-output fidelity, field provenance, apparatus isolation, manifests, and required documentation.
