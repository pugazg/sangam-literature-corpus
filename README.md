# Sangam Literature Corpus

## Current repository state

This repository preserves a frozen Classical Tamil corpus and maintains independently versioned derived research layers above it.

Current preservation release: **Classical Tamil Corpus 1.1.0**.

- frozen works: 28
- canonical records: 7,234
- poem records: 5,632
- Tolkāppiyam நூற்பா: 1,602
- release identity: `classical-tamil-corpus-v1.1.0`

Current research work is **R1.5 — Classical Tamil Concept Matrix Foundation** on branch `research/classical-tamil-concept-matrix-r1.5`, proposed to `main` through PR #3.

**PR #3 must remain open, draft, and unmerged until the user explicitly authorizes a merge. R2 is blocked; do not start R2 before that authorization and a fresh inspection of the merged `main`.**

The live PR and branch state are authoritative for current workflow/check status. Historical prompts, release snapshots, and older workflow logs remain provenance rather than current execution instructions.

## Repository release checkpoint

The immutable **Classical Tamil Corpus 1.0.0** checkpoint contains 27 frozen works and 5,632 canonical numbered poem records. The succeeding **Classical Tamil Corpus 1.1.0** checkpoint adds independently parsed Tolkāppiyam as the twenty-eighth work, bringing the repository to 7,234 canonical records: 5,632 poems plus 1,602 நூற்பா.

Existing release tags and frozen source/corpus content are not retargeted merely because the derived research layer advances.

## Research version boundary

- R0 evidence schema: `0.1.0`
- R1 review/entity-resolution workflow schema: `0.2.0`
- R1.5 concept/observation schema: `0.3.0`

R0 remains 2,867 source-grounded assertions, 285 literary-body candidates, 43 pilot surface-form entities, and 51 assertion-supported relationships. R1 adds 8 append-only review events and 3 conservative entity-resolution decisions, with no verified historical identity. R1.5 adds the versioned concept registry/evidence policies, a bounded 8-observation Puṟanāṉūṟu production pilot, and the exhaustive pre-merge matrix audit.

The exhaustive R1.5 audit reviewed:

- Puṟanāṉūṟu: 400 / 400 records × 29 research dimensions;
- Tolkāppiyam: 1,602 / 1,602 நூற்பா across 27 இயல் × the same 29 dimensions;
- automatic Tolkāppiyam → Sangam poem classification: disabled.

Audit ledgers are review evidence; they do not automatically become production observations.

## Patiṉeṇkīḻkkaṇakku programme

The Patiṉeṇkīḻkkaṇakku preservation programme is complete. All eighteen selected works are frozen at corpus schema version `1.0.0`. `முப்பால்` is treated as an alias of Tirukkural rather than a separate corpus work, and `கைந்நிலை` is the selected eighteenth-work tradition.

## Project purpose

The preservation layer builds reproducible, source-faithful Markdown transcriptions of Classical Tamil works from selected, checksum-pinned source objects. It preserves provenance and uncertainty without silent spelling modernization, textual repair, translation, or historical reconstruction.

The derived research layer is separate. It may create evidence assertions, review events, concept observations, relationships, matrices, and later analytical views, but it cannot overwrite frozen canonical evidence.

## Source and editorial hierarchy

1. **Raw source preservation** — exact acquired bytes and provenance.
2. **Source-faithful canonical transcription** — only permitted mechanical transformations.
3. **Source-explicit metadata** — values supported by the selected source.
4. **Validation and anomaly reporting** — machine checks and review queues, never silent repair.
5. **External textual comparison** — isolated under `apparatus/` or another clearly separate evidence layer.
6. **Derived research evidence** — independently versioned assertions/reviews/concepts/relationships.
7. **External historical or interpretive claims** — separately classified and cited; never silently collapsed into source evidence.

## Python and installation

- Python: 3.11 or later
- core dependencies: Beautiful Soup, lxml, PyYAML, certifi

```bash
python3 -m venv .venv
. .venv/bin/activate
python3 -m pip install -r requirements.txt
python3 -m pip install pytest
pytest -q
```

Dependencies are pinned in `requirements.txt`. TLS verification is not disabled for source acquisition.

## Repository tree

```text
sangam-literature-corpus/
├── README.md
├── PROJECT_GUIDELINES.md
├── PROJECT_HANDOVER.md
├── NEXT_CHAT_PROMPT.md
├── requirements.txt
├── corpus/
├── sources/
├── apparatus/
├── manifests/
├── research/
├── docs/
├── issues/
├── logs/
├── scripts/
└── tests/
```

Each `corpus/<work>/` directory uses the structure appropriate to that work. Anthology/didactic works generally retain poem-oriented records; Tolkāppiyam uses the hierarchy `work → அதிகாரம் → இயல் → நூற்பா` and canonical records under `corpus/tolkappiyam/nurpas/`.

## Commands

Corpus regeneration/validation examples:

```bash
python3 scripts/process_work.py natrinai
python3 scripts/process_work.py purananuru
python3 scripts/process_work.py tolkappiyam
python3 scripts/audit_repository.py --root .
pytest -q
```

Research-layer regeneration/validation:

```bash
python3 scripts/generate_research_layer.py --root .
python3 scripts/generate_research_r1.py --root .
python3 scripts/generate_research_r15.py --root .
python3 scripts/validate_research_layer.py --root .
python3 scripts/validate_research_r1.py --root .
python3 scripts/validate_research_r15.py --root .
python3 scripts/validate_research_r15_acceptance.py --root .
python3 scripts/validate_r15_premerge_matrix_audit.py --root .
python3 scripts/verify_research_r1_idempotence.py --root .
python3 scripts/verify_research_r15_idempotence.py --root .
pytest -q
python3 scripts/audit_repository.py --root .
```

## Raw-source preservation and checksums

Raw source objects are preserved without silent replacement. Acquisition/source metadata records the source identity, access information where applicable, byte length, checksum, and selected-edition decision. A changed upstream response is a new evidence condition and must not silently replace a frozen source identity.

Puṟanāṉūṟu retains its documented source-artifact decision. Tolkāppiyam retains its independently frozen Project Madurai source identity. Research work does not modify either source object.

## Unicode normalization and transformation policy

Permitted automatic transformations are narrowly mechanical and documented, such as Unicode NFC and line-ending normalization where the source-processing policy permits them.

Prohibited silent transformations include spelling modernization, typo correction, word splitting/merging, inferred metadata, deletion of repetition, unreported renumbering, supplementation from another edition, translation, and interpretation.

Printed punctuation, unusual characters, lacuna markers, numbering anomalies, and source loss are preserved or explicitly documented.

## Poem splitting and work-specific structure

Splitting logic is source-specific rather than one universal parser assumption. Source-printed structure is kept separate from mechanically generated navigation.

Examples include source-printed பத்து groupings, macro-divisions, long-poem structure, or flat numbered sequences. Tolkāppiyam is not forced into poem-oriented terminology: it uses `அதிகாரம் / இயல் / நூற்பா` structure.

No research concept or conventional literary classification may be used to manufacture missing preservation-layer structure.

## Poem metadata and provenance

Canonical metadata includes only source-supported values plus clearly labeled repository/mechanical provenance fields. Printed identity, source order, repository identity, and generated navigation identity remain distinct where necessary.

A source-explicit poet, addressee, tiṇai, tuṟai, heading, or other field is not silently converted into a historical identity claim.

## Manifests and deterministic ordering

Shared manifests use deterministic aggregation and must not be written concurrently by multiple work generators. The required model is work-local generation followed by one authoritative aggregator, explicit UTF-8 encoding, stable order, validation, and atomic replacement.

The repository previously detected an overlapping writer problem in a shared manifest; canonical corpus content was unaffected, and the shared-manifest path is now protected by deterministic/atomic generation rules.

## Validation rules

A preservation or research change is acceptable only when the applicable validators pass and previously frozen evidence does not drift unexpectedly.

For the current R1.5 PR, CI must prove:

- R0 compatibility validation;
- R1 workflow validation;
- R1.5 pilot validation;
- R1.5 acceptance/orphan-reference validation;
- exhaustive R1.5 matrix-audit validation;
- complete regression tests;
- R1 and R1.5 deterministic regeneration;
- repository physical audit;
- Corpus 1.1.0/Tolkāppiyam non-drift;
- R1 primary-history non-mutation;
- documentation-status regression checks.

Green validation is technical readiness only; it does not authorize merging PR #3.

## Severity levels

Use repository validators/issues to distinguish blocking errors from documented source conditions.

- **error / fail** — broken provenance, missing/duplicate canonical records, hash drift, invalid schema, invalid evidence reference, non-determinism, or another invariant breach;
- **warning / review condition** — a documented source ambiguity or anomaly requiring inspection but not silent repair;
- **pass** — required invariants hold.

Do not turn a genuine source condition into a false clean pass by modifying canonical text.

## Manual review process

When a validator or audit surfaces ambiguity:

1. inspect the controlling source;
2. preserve exact printed evidence;
3. distinguish source text, commentary, damage, source loss, and editorial inference;
4. record the decision in the appropriate issue/apparatus/review history;
5. rerun deterministic validation;
6. never hide an earlier research decision by rewriting append-only history.

Assistant-assisted review must identify itself accurately and does not constitute independent historical verification.

## External comparison sources

External editions, scholarship, modern geography, biography, chronology, taxonomy, or historical equivalence are separate evidence. They may support apparatus or later externally cited research assertions but cannot overwrite canonical source evidence.

Tolkāppiyam grammatical/poetics evidence is likewise a separate evidence stream and does not automatically classify Sangam poems.

## Canonical transcription versus editorial apparatus

`corpus/` answers what the selected source supports after permitted mechanical processing. `apparatus/` and derived research layers answer separate comparison/research questions.

An apparatus observation, concept classification, external identification, or interpretation cannot mutate canonical transcription.

## Source terminology

Read [`docs/SOURCE_TERMINOLOGY_POLICY.md`](docs/SOURCE_TERMINOLOGY_POLICY.md) before social, ritual, learned, occupational, political, kinship, or community classification.

Use the exact Tamil term printed by the relevant source, such as `அந்தணர்`, `அரசர்`, `பாணர்`, or another source-supported form. Do not silently replace a Classical Tamil source term with a later caste, sectarian, modern-community, hierarchy, or external-influence identity.

## Adding the next Project Madurai work

Do not generalize an existing parser blindly. For any future preservation-layer addition:

1. preserve the new source bytes and checksum;
2. perform complete source reconnaissance;
3. document source grammar, printed structure, anomalies, and edition selection;
4. add an explicit work/source parser profile where required;
5. keep source structure separate from mechanical navigation;
6. run complete physical, fidelity, regression, deterministic, and non-drift checks;
7. use a separate formal freeze/release step.

R2 research extraction is **not** a new corpus-work onboarding activity and must not begin while PR #3 is held unmerged.

## Key current documents

- [`PROJECT_HANDOVER.md`](PROJECT_HANDOVER.md) — authoritative current continuity state.
- [`PROJECT_GUIDELINES.md`](PROJECT_GUIDELINES.md) — working rules.
- [`NEXT_CHAT_PROMPT.md`](NEXT_CHAT_PROMPT.md) — safe continuation contract.
- [`docs/DOCUMENTATION_STATUS.md`](docs/DOCUMENTATION_STATUS.md) — active/historical documentation classification.
- [`docs/CLASSICAL_TAMIL_RESEARCH_MATRIX.md`](docs/CLASSICAL_TAMIL_RESEARCH_MATRIX.md) — matrix architecture and phase roadmap.
- [`docs/classical-tamil-research-layer.md`](docs/classical-tamil-research-layer.md) — research-layer evidence/version model.
- [`docs/SOURCE_TERMINOLOGY_POLICY.md`](docs/SOURCE_TERMINOLOGY_POLICY.md) — source-term rule.
- [`docs/handover/r15-premerge-audit/README.md`](docs/handover/r15-premerge-audit/README.md) — exhaustive-audit continuity.

Files under `docs/history/` are historical snapshots and must not be executed as current instructions. Release documents and durable machine logs remain truthful records of the state/run they actually describe.

## Rights / visibility

The repository remains private. `docs/source-rights-and-redistribution-review.md` retains unresolved redistribution questions. Do not change repository visibility without a separate explicit user decision after that review.
