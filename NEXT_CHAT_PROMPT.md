# Next Chat Prompt — R1.5A Tolkāppiyam production

Continue directly in `pugazg/sangam-literature-corpus`.

Active branch: `research/classical-tamil-concept-matrix-r1.5a`. Active PR: #4, draft/unmerged. Treat live GitHub state as authoritative.

## Phase boundary

R1.5 was explicitly authorized and merged into `main` at `d82f9c78f27f9c9daf8fbb913d01ddfb29bddba1`.

R1.5A keeps concept/observation schema `0.3.0` and the exact 29 dimensions. It is not R2. R2 remains blocked.

## Mandatory startup

Before changing the repository, read completely:

1. `docs/DOCUMENTATION_STATUS.md`
2. `docs/SOURCE_TERMINOLOGY_POLICY.md`
3. `PROJECT_HANDOVER.md`
4. `PROJECT_GUIDELINES.md`
5. `NEXT_CHAT_PROMPT.md`
6. `docs/handover/r15a-production-review/README.md`
7. `research/production/purananuru/README.md`
8. `research/production/tolkappiyam/README.md`
9. `research/observations/tolkappiyam/README.md`
10. both Tolkāppiyam production schemas
11. the Tolkāppiyam production concept extension
12. old Tolkāppiyam manifest/crosswalk controls
13. Tolkāppiyam materializer and production validator
14. current PR #4 metadata, exact branch head, and exact-head checks.

## Accepted state

- Corpus 1.1.0 remains frozen: 28 works / 7,234 canonical records / 5,632 poems / 1,602 Tolkāppiyam நூற்பா.
- Puṟanāṉūṟu production is complete: 400/400, 7,169 observations.
- Puṟanāṉūṟu cadence remains benchmark `001–002`, stabilization `003–010`, and regular 25-record batches beginning `011–035`, with final `386–400`.
- Tolkāppiyam production is gap-free through `0001–0483`.
- Reviewed: **483 / 1,602**.
- Remaining: **1,119**.
- Next: **tolkappiyam-0484**.
- Formal grammatical/poetics observations: **662**.
- Incidental examples: **83**.
- Exact dimensions: **29**.
- All nine எழுத்ததிகாரம் இயல் are complete.
- Next இயல்: **சொல்லதிகாரம் / கிளவியாக்கம் `0484–0545` / 62 records**.

## Completed குற்றியலுகரப்புணரியல்

குற்றியலுகரப்புணரியல் `0407–0483` is complete across:

- `0407–0431`: 40 formal + 7 incidental;
- `0432–0456`: 51 formal + 4 incidental;
- `0457–0481`: 54 formal + 4 incidental;
- `0482–0483`: 6 formal + 1 incidental.

Total contribution: **151 formal observations + 16 incidental examples**. No new controlled concept was required.

Formal boundary transformations, morphology, word structure, number/measure expressions, and narrow poetic/tradition contexts remain grammatical. `மரப்பெயர்`, `வண்டு`, `பெண்டு`, directional forms, learned-authority formulas, measure vocabulary, `உயர்திணை`, `அஃறிணை`, `இசை`, and `தொழில்` remain contextual and are not promoted into unsupported historical claims.

## Evidence contract

Review every நூற்பா sequentially/source-first across all 29 dimensions. Distinguish formal grammatical/poetics evidence, incidental examples, and reviewed-empty decisions.

Only formal evidence enters `research/observations/tolkappiyam/r15-production.ndjson` as `GRAMMATICAL_CONCEPT_EVIDENCE` with `tolkappiyam_mapping`.

Incidental examples never become automatic historical, ecological, social, material, identity, medical, economic, or lived-life claims. Exact source Tamil wins. The old manifest/crosswalk is control evidence only and never a classifier. Tolkāppiyam evidence never auto-classifies another work.

## Iteration rule

The user requires **one complete இயல் per iteration**. An iteration may contain multiple contiguous publication checkpoints of at most 25 records, but must not cross into the next இயல். Each checkpoint must be materialized and green before the next begins.

## Required next iteration — கிளவியாக்கம்

Complete **சொல்லதிகாரம் / கிளவியாக்கம் `0484–0545` (62 records)**.

Use publication boundaries:

- `0484–0508`;
- `0509–0533`;
- `0534–0545`.

For every record, read the complete frozen நூற்பா and current இயல் context, consider all 29 dimensions, settle formal/incidental/empty decisions before moving on, preserve exact Tamil and source spans, consult controls only after fresh decisions, materialize only the contiguous boundary, and require full exact-head CI green before advancing.

Stop after `tolkappiyam-0545`; next must be `tolkappiyam-0546`. Keep PR #4 draft/unmerged. Do not start R2.
