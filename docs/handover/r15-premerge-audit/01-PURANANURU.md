# Part 1 — Puṟanāṉūṟu exhaustive matrix review

## Why this audit was necessary

R0 processed all 400 canonical records, but its literary-body candidate extraction used a bounded exact-token seed list. R1 reviewed eight selected candidates and R1.5 mapped those eight reviewed observations into the concept model. That was **not equivalent** to reading all 400 poems semantically against all 29 dimensions.

## New review performed

The frozen `corpus/purananuru/full-text.md` was read sequentially from record 1 through record 400. For every record, all 29 controlled dimensions in `research/audits/r15-premerge/dimensions.json` were considered.

The audit is stored sparsely in eight 50-record TSV files. A listed code means qualifying evidence was observed in the reviewed source record. An omitted code means only that qualifying evidence was not recorded in this pass; it does not prove historical absence.

Special conditions are preserved:

- record 200 retains its damaged/unreadable body condition; no missing semantics are invented;
- records 267 and 268 are explicitly reviewed as source-lost and remain unreconstructed.

## Coverage result

- records reviewed: **400 / 400**
- dimensions considered per record: **29 / 29**
- source-lost records: **267, 268**
- damaged/unreadable special record: **200**

Dimension-level record counts are recorded in `research/audits/r15-premerge/purananuru/dimension-summary.json`. These counts are audit observations, not counts of historical facts.

## What the full read added beyond the old seed scan

The semantic read repeatedly surfaced material that a small token list could not safely model: famine and hunger, poverty, widowhood and mourning practices, cremation and hero-stones, kinship and parent/child relations, hospitality, bardic livelihood, agriculture and irrigation, salt/ship movement, craft and wound-care practices, household objects, clothing and ornaments, women’s roles, social communities, political ethics, ritual, astronomy/omens, and explicit textual/allusive relationships.

Examples of why separate dimensions matter include:

- poverty joining food scarcity, clothing, body, family and patronage rather than being only an `economy` tag;
- battlefield poems joining warfare with medicine, ritual, mourning, fauna, food and performance;
- poem 335 joining flora/food, named communities, warfare, death and hero-stone ritual;
- poem 378 containing a source-visible Rāvaṇa/Sītā/monkey ornament analogy suitable for the textual/intertextual dimension without external reconstruction.

## Interpretation boundaries

- `literary_domain` uses the work-level Puram classification unless a narrower source basis is recorded.
- tiṇai/tuṟai are not invented where source classification is absent or damaged.
- names remain source-printed candidates, not resolved historical identities.
- intertextual evidence is recorded only when the source visibly supplies the relation/allusion.
