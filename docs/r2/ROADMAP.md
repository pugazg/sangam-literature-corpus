# R2 Core Sangam Production Roadmap

## Authorization and foundation

R2 was explicitly authorized by the user after R1.5A merged into `main` at `1e6684b09a5e41fc675ea3e07ba8b6a646d35830`.

R2 extends the exact 29-dimension, evidence-first production model across the frozen nine-work Core Sangam Corpus. It does not modify Corpus 1.1.0, restart completed Puṟanāṉūṟu review, perform cross-corpus historical entity resolution, create civilisation-level syntheses, build explorer interfaces, auto-classify poems from Tolkāppiyam, or introduce uncited external historical claims.

## Exact scope

The controlling scope is `manifests/sangam-core-program.json`:

| Work | Work ID | Frozen records | R2 state |
|---|---|---:|---|
| நற்றிணை | `natrinai` | 400 | pending |
| ஐங்குறுநூறு | `aingurunuru` | 500 | pending |
| குறுந்தொகை | `kuruntokai` | 401 | production active; complete through 010 |
| அகநானூறு | `akananuru` | 400 | pending |
| புறநானூறு | `purananuru` | 400 | completed foundation; carry forward |
| பத்துப்பாட்டு | `pattuppattu` | 10 | pending; long-work adapter required |
| பதிற்றுப்பத்து | `patirruppattu` | 80 | pending |
| பரிபாடல் | `paripatal` | 35 | pending; music/deity metadata adapter required |
| கலித்தொகை | `kalittokai` | 150 | pending |

Total frozen records: **2,376**. Completed Puṟanāṉūṟu foundation: **400**. New R2 review scope: **1,976** records.

The manifest order is the canonical scope order. Production order is evidence-engineering order and begins with Kuṟuntokai so Akam-specific metadata can be validated before scaling.

## Version contract

- R2 multi-work production-review schema: **0.4.0**.
- Exact concept dimensions: **29**, unchanged.
- Existing R0/R1/R1.5 identities and append-only histories remain preserved.
- Existing R1.5A Puṟanāṉūṟu and Tolkāppiyam records remain immutable inputs.
- A version increase represents the new multi-work record/metadata adapter contract; it does not authorize dimension drift.

## Evidence contract

For every newly reviewed record:

1. read the complete frozen canonical record before classification;
2. consider all exact 29 dimensions in canonical order;
3. preserve exact source Tamil and source-explicit metadata;
4. distinguish body, heading, attribution, source note and mechanical navigation fields;
5. retain exact evidence spans and canonical hashes;
6. record ambiguity rather than resolve it silently;
7. write a complete durable per-record ledger before moving to the next record;
8. treat empty as no qualifying evidence identified, never historical absence;
9. never use Tolkāppiyam as an automatic poem classifier;
10. never convert printed names into verified historical identities without separately permitted evidence.

## Gates

### Gate A — startup and contract

- close post-R1.5A continuity;
- freeze exact nine-work scope;
- introduce schema 0.4.0 multi-work adapter contract;
- add validators and tests;
- preserve frozen-corpus and prior-history non-drift.

### Gate B — Kuṟuntokai benchmark

Review Kuṟuntokai 001–002 sequentially and source-first. The benchmark must prove:

- Akam work context without unsupported inference;
- printed `thinai_as_printed`;
- printed `speaker_as_printed`;
- printed `poet_as_printed`;
- exact body spans;
- all 29 dimension decisions;
- deterministic record and observation identities;
- no Tolkāppiyam auto-classification.

### Gate C — stabilization — complete

Kuṟuntokai 003–010 was reviewed sequentially after the green benchmark. The resulting prefix is 001–010 with 114 observations and exact 29-dimension reviews. The regular batch size is frozen at 25 records.

### Gate D — Kuṟuntokai production

Continue in contiguous 25-record batches that never skip record order or cross a work boundary. The first regular batch is `011–035`. Complete all 401 records and run the per-work completion gate.

### Gate E — remaining works

Begin each work with its own two-record benchmark and adapter review. Provisional production order after Kuṟuntokai:

1. Naṟṟiṇai;
2. Aiṅkuṟunūṟu;
3. Akanāṉūṟu;
4. Kalittokai;
5. Paripāṭal;
6. Patiṟṟuppattu;
7. Pattuppāṭṭu.

The order may change only through a documented R2 decision; the nine-work scope may not drift silently.

### Gate F — unified R2 integration

- prove all 2,376 core records are represented, including carried-forward Puṟanāṉūṟu;
- generate unified work/record/dimension views from provenance-bearing ledgers;
- run deterministic regeneration, full regression, repository audit and Corpus 1.1.0 non-drift;
- update continuity and keep the R2 PR draft/unmerged until explicit merge authorization.

## Later-phase exclusions

R3 and all later phases remain blocked during R2.

- R3: cross-corpus entity resolution and reviewed relationships.
- R4: civilisation/lived-life synthesis.
- R5: explorer, maps, timelines, networks and UI.
- R7: separately represented Tolkāppiyam ↔ Sangam comparison.
- R8: external scholarship/historical-identification layer.

These exclusions remain binding throughout R2.
