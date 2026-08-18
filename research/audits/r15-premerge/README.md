# R1.5 pre-merge exhaustive matrix audit

## Why this exists

The bounded R1.5 production pilot proved the concept/observation model but did not prove that every Puṟanāṉūṟu poem had been semantically reviewed against every research dimension.

The exhaustive audit therefore reviewed two source streams against the same controlled 29-dimension frame.

## Scope

### Puṟanāṉūṟu

- records reviewed: 400 / 400;
- dimensions considered per record: 29;
- sparse results stored in eight 50-record TSV parts;
- omitted codes mean only that qualifying evidence was not recorded in that pass;
- record 200 remains damaged/unreconstructed;
- records 267–268 remain source-lost/unreconstructed.

### Tolkāppiyam

- இயல் reviewed: 27 / 27;
- நூற்பா reviewed: 1,602 / 1,602;
- dimensions considered: 29;
- formal crosswalk dimensions: 29;
- automatic Tolkāppiyam → Sangam poem classification: disabled.

The crosswalk records representative formal support and support depth. It is not an exhaustive concordance of every incidental lexical example.

## Evidence boundaries

- No frozen corpus/source file is edited by this audit.
- Puṟanāṉūṟu dimension codes are reviewed audit observations, not external historical facts.
- Tolkāppiyam grammatical concept evidence is a separate stream.
- A lexical example inside a grammatical rule is not automatically a cultural/historical claim.
- Names are not resolved into historical identities without separate evidence.
- Exact source Tamil social/ritual/community terminology is preserved under `docs/SOURCE_TERMINOLOGY_POLICY.md`.
- Empty cells never prove historical absence.
- Audit ledger codes do not automatically become production R1.5 observations.

## Files

- `dimensions.json` — 29-dimension registry.
- `purananuru/parts/001-050.tsv` … `351-400.tsv` — record-by-record audit ledger.
- `purananuru/dimension-summary.json` — deterministic dimension coverage counts.
- `tolkappiyam/review-manifest.json` — exact 27-இயல் / 1,602-நூற்பா coverage map.
- `tolkappiyam/dimension-crosswalk.json` — representative formal/structural support.

## Current merge boundary

The exhaustive audit gates have passed. A subsequent documentation audit synchronizes active continuity files and is CI-validated on the current PR head.

PR #3 must remain open, draft and unmerged until explicit user authorization. R2 remains blocked.
