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
10. Tolkāppiyam production schemas, concept extension, old controls, materializer and validator
11. current PR #4 metadata, exact branch head, and exact-head checks.

## Accepted state

- Corpus 1.1.0 remains frozen: 28 works / 7,234 canonical records / 5,632 poems / 1,602 Tolkāppiyam நூற்பா.
- Puṟanāṉūṟu production is complete: 400/400, 7,169 observations.
- Puṟanāṉūṟu cadence remains benchmark `001–002`, stabilization `003–010`, regular 25-record batches beginning `011–035`, and final `386–400`.
- Tolkāppiyam production is complete and gap-free through `0001–1602`.
- Reviewed: **1,602 / 1,602**.
- Remaining: **0**.
- Next: **none**.
- Formal grammatical/poetics observations: **3,505**.
- Incidental examples: **348**.
- Exact dimensions: **29**.
- All 27 இயல் across all three அதிகாரம் are complete.

## Completed சொல்லதிகாரம்

சொல்லதிகாரம் `0484–0946` is complete:

- கிளவியாக்கம் `0484–0545`: 65 formal + 18 incidental;
- வேற்றுமையியல் `0546–0567`: 44 formal + 22 incidental;
- வேற்றுமைமயங்கியல் `0568–0602`: 36 formal + 8 incidental;
- விளிமரபு `0603–0639`: 74 formal + 4 incidental;
- பெயரியல் `0640–0682`: 83 formal + 16 incidental;
- வினையியல் `0683–0733`: 81 formal + 8 incidental;
- இடையியல் `0734–0781`: 96 formal + 7 incidental;
- உரியியல் `0782–0879`: 99 formal + 42 incidental;
- எச்சவியல் `0880–0946`: 135 formal + 12 incidental.

Total: **713 formal observations + 137 incidental examples**.

Three narrow controlled concepts were added because சொல்லதிகாரம் formally requires distinctions not represented by morphology alone:

- `knowledge.grammar.syntax`;
- `knowledge.grammar.lexical_semantics`;
- `knowledge.grammar.discourse_pragmatics`.

Lexical meanings, gender/kinship forms, social-role language, emotion, body, wealth/poverty, deity/mantra, region/direction, tense, music/sound, and poetic examples remain source-contextual. They are not automatically historical facts.

## Evidence contract

Review every நூற்பா sequentially/source-first across all 29 dimensions. Distinguish formal grammatical/poetics evidence, incidental examples, and reviewed-empty decisions. Only formal evidence enters the flattened stream with `tolkappiyam_mapping`.

Exact source Tamil wins. The old manifest/crosswalk is post-review control evidence only and never a classifier. Tolkāppiyam evidence never auto-classifies another work.

## Next canonical activity

Tolkāppiyam R1.5A production has no next canonical record. Verify and review the completed draft PR #4; do not merge without explicit user authorization.

Keep PR #4 draft/unmerged. Do not start R2.
