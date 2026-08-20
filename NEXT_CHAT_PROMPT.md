# Next Chat Prompt — R1.5A Tolkāppiyam production

Continue directly in `pugazg/sangam-literature-corpus`.

Active branch: `research/classical-tamil-concept-matrix-r1.5a`. Active PR: #4, draft/unmerged.

Treat live GitHub state as authoritative.

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
- Tolkāppiyam production is gap-free through `0001–0406`.
- Reviewed: **406 / 1,602**.
- Remaining: **1,196**.
- Next: **tolkappiyam-0407**.
- Formal grammatical/poetics observations: **511**.
- Incidental examples: **67**.
- Exact dimensions: **29**.
- Completed எழுத்ததிகாரம் இயல்: நூல் மரபு, மொழி மரபு, பிறப்பியல், புணரியல், தொகைமரபு, உருபியல், உயிர்மயங்கியல், புள்ளிமயங்கியல்.
- Next இயல்: **குற்றியலுகரப்புணரியல் `0407–0483` / 77 records**.

## Completed recent இயல்

### உயிர்மயங்கியல் `0204–0296`

Four publication boundaries are complete: `0204–0228`, `0229–0253`, `0254–0278`, `0279–0296`.

Total contribution: **116 formal observations + 23 incidental examples**.

### புள்ளிமயங்கியல் `0297–0406`

Five publication boundaries are complete:

- `0297–0321`: 32 formal + 4 incidental;
- `0322–0346`: 31 formal + 6 incidental;
- `0347–0371`: 29 formal + 3 incidental;
- `0372–0396`: 32 formal + 6 incidental;
- `0397–0406`: 12 formal + 2 incidental.

Total contribution: **136 formal observations + 21 incidental examples**.

No new controlled concept was required.

## Evidence contract

Review every நூற்பா sequentially/source-first across all 29 dimensions. Distinguish formal grammatical/poetics evidence, incidental examples, and reviewed-empty decisions.

Only formal evidence enters `research/observations/tolkappiyam/r15-production.ndjson` as `GRAMMATICAL_CONCEPT_EVIDENCE` with `tolkappiyam_mapping`.

Incidental lexical examples never become automatic historical, ecological, social, material, identity, medical, economic, or lived-life claims. Exact source Tamil wins. The old manifest/crosswalk is control evidence only and never a classifier. Tolkāppiyam evidence never auto-classifies another work.

## Iteration rule

The user requires **one complete இயல் per iteration**. An iteration may contain multiple contiguous publication checkpoints of at most 25 records, but must not cross into the next இயல்.

Each checkpoint must be materialized and green before the next checkpoint begins.

## Required next iteration — குற்றியலுகரப்புணரியல்

Complete **எழுத்ததிகாரம் / குற்றியலுகரப்புணரியல் `0407–0483` (77 records)**.

Use publication boundaries:

- `0407–0431`;
- `0432–0456`;
- `0457–0481`;
- `0482–0483`.

For every record:

1. read the complete frozen நூற்பா and current இயல் context;
2. consider all 29 dimensions;
3. fix formal evidence, incidental examples and reviewed-empty decisions before moving on;
4. preserve exact Tamil terms and source spans;
5. compare with old controls only after fresh semantic decisions;
6. materialize only the contiguous boundary;
7. validate exact counts;
8. update current documentation and PR #4;
9. require full exact-head CI green before the next boundary.

Stop after `tolkappiyam-0483`; next must be `tolkappiyam-0484`. Keep PR #4 draft/unmerged. Do not start R2.
