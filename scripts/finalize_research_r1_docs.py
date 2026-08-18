#!/usr/bin/env python3
"""Finalize R1 continuity docs after all validation gates have passed."""
from __future__ import annotations

import os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MARKER = "R1_REVIEW_WORKFLOW_COMPLETE_20260818"


def insert_after_title(path: Path, block: str) -> None:
    text = path.read_text(encoding="utf-8")
    if MARKER in text:
        return
    lines = text.splitlines(keepends=True)
    if lines and lines[0].startswith("# "):
        text = lines[0] + "\n" + block.rstrip() + "\n\n" + "".join(lines[1:]).lstrip("\n")
    else:
        text = block.rstrip() + "\n\n" + text
    path.write_text(text, encoding="utf-8")


def append_once(path: Path, block: str) -> None:
    text = path.read_text(encoding="utf-8")
    if MARKER in text:
        return
    path.write_text(text.rstrip() + "\n\n" + block.rstrip() + "\n", encoding="utf-8")


def main() -> None:
    validated_sha = os.environ.get("GITHUB_SHA", "validated-r1-branch-state")

    readme_block = f"""<!-- {MARKER} -->
## Derived research layer — R1

The active research branch is `research/sangam-evidence-r1`. R0 Puṟanāṉūṟu
evidence remains at schema `0.1.0`; R1 adds independently versioned review and
entity-resolution workflow schema `0.2.0`. The research layer does not edit the
frozen Corpus 1.1.0 evidence. See
[`docs/classical-tamil-research-layer.md`](docs/classical-tamil-research-layer.md).
"""

    handover_block = f"""<!-- {MARKER} -->
## Active handover — R1 complete, R1.5 next

R1 review workflow and entity-resolution foundation completed on
`research/sangam-evidence-r1` after validation of `{validated_sha}`.

- R0 evidence identity is preserved: 2,867 assertions, 285 body candidates,
  43 pilot entities, and 51 relationships.
- Corpus 1.1.0 and Tolkāppiyam remain unchanged.
- Review history is append-only and hash-chained.
- R1 records assistant-assisted source review explicitly and creates no
  verified historical identities.
- Entity resolution supports merge/split/reject/supersede operations but
  production decisions remain conservative and assertion-provenanced.
- Required R1 deterministic queues/reports and baseline/idempotence reports are
  present under `research/` and `logs/`.
- R2 must not begin. The next active phase is **R1.5 Classical Tamil Concept
  Matrix**, controlled by `docs/CLASSICAL_TAMIL_RESEARCH_MATRIX.md`.

The earlier R0/R1 handover material below is retained as historical provenance;
this section is authoritative for the next activity.
"""

    guideline_block = f"""<!-- {MARKER} -->
## R1 review and identity-resolution rules

- R0 assertions remain immutable evidence records at schema `0.1.0`; workflow
  evolution must not rewrite their IDs, spans, source hashes, or evidence text.
- `review-events.ndjson` is append-only. `reviewed` requires an explicit event;
  `verified` requires a stronger explicit verification decision.
- Reviewer identity and type must be recorded accurately. `machine_checked` and
  `assistant_assisted` are not independent human verification.
- Entity-resolution decisions must cite supporting assertion IDs. Exact printed
  or normalized form equality may support `possible_match` but never an
  automatic merge or verified historical identity.
- Rejected, split, merged, and superseded decisions remain auditable; history is
  never silently deleted.
- Deterministic derived exports exclude execution timestamps. Primary event
  timestamps remain only where semantically required.
"""

    decision_block = f"""<!-- {MARKER} -->
## R1 reconciliation and review-workflow decisions — 2026-08-18

R1 was created from current `main` (`05bc2ae328a7f9cc94129b295f6c59d7457491ec`)
rather than by advancing the stale R0 branch. The attempted direct R0→R1 merge
conflicted and was not merged. The accepted reconciliation overlays the exact R0
research subtree and research-support blobs onto the current Corpus 1.1.0 base;
it does not write canonical corpus paths.

R0 evidence remains schema `0.1.0`. R1 workflow records are versioned separately
at `0.2.0`; upgrading the workflow does not rewrite assertion IDs, spans, source
hashes, or evidence text.

`review-events.ndjson` is append-only. The R0 generator entry point now delegates
to the preserved R0 implementation while protecting existing review history.
Assistant-assisted review is recorded explicitly and creates no verified
historical identity.

Entity equality by printed/normalized form is never an automatic merge. R1
records only assertion-provenanced conservative candidate/possible-match
decisions in the production pilot. Merge, split, reject, and supersede remain
supported audited operations.

No external historical or interpretive assertion is introduced in R1. R1.5
Classical Tamil Concept Matrix is the next permitted phase; R2 must not begin
directly.
"""

    old_next = ROOT / "NEXT_CHAT_PROMPT.md"
    archive = ROOT / "docs/history/NEXT_CHAT_PROMPT_R1.md"
    if not archive.exists():
        archive.parent.mkdir(parents=True, exist_ok=True)
        archive.write_text(old_next.read_text(encoding="utf-8"), encoding="utf-8")

    next_prompt = f"""# Next Chat Prompt — R1.5 Classical Tamil Concept Matrix

<!-- {MARKER} -->

Treat current GitHub state as authoritative. Do **not** repeat R0 reconciliation
or R1 review-workflow implementation, and do **not** begin R2.

## Mandatory startup

Read these files completely before making any repository change:

1. `PROJECT_HANDOVER.md`
2. `PROJECT_GUIDELINES.md`
3. `NEXT_CHAT_PROMPT.md`
4. `docs/CLASSICAL_TAMIL_RESEARCH_MATRIX.md`
5. `docs/classical-tamil-research-layer.md`
6. `manifests/classical-tamil-research-program.json`
7. `research/reports/purananuru-r1-review-summary.json`
8. `research/reports/purananuru-r1-review-summary.md`
9. `research/reports/purananuru-r1-ambiguity-register.md`
10. `logs/classical-tamil-research-r0-to-corpus-1.1.0-compatibility-20260818T145500.json`
11. `logs/classical-tamil-research-r1-baseline-20260818T145500.json`
12. `logs/classical-tamil-research-r1-idempotence-20260818T145500.json`
13. `logs/classical-tamil-research-program-decisions.md`

Then inspect current `main`, `research/sangam-evidence-r1`, open PRs, recent
commits, tags, and the live repository tree. Current GitHub state overrides
stale SHAs in historical prose.

## R1 accepted boundary

R1 preserves R0 evidence identity at schema `0.1.0` and adds workflow schema
`0.2.0`. It contains no external-historical or interpretive assertions and no
verified historical identity. Do not weaken these constraints.

## Active work — R1.5

Proceed exactly from `docs/CLASSICAL_TAMIL_RESEARCH_MATRIX.md`.

R1.5 must formalise the observation model before corpus-wide extraction. Every
populated cell must remain traceable to assertion IDs and exact evidence.
Akam/Puram, tiṇai, tuṟai, landscapes, material/lived-life dimensions, and named
entities must retain classification basis/provenance rather than becoming
unsupported boolean tags.

Empty cells mean only “qualifying evidence is not currently recorded”; they do
not prove historical absence.

Start with a bounded, deterministic pilot and explicit schemas/vocabularies.
Do not expand to corpus-wide R2 extraction until the R1.5 model, validation,
tests, audit, and handover are complete.

The historical prompt that led through R0 reconciliation and R1 is archived at
`docs/history/NEXT_CHAT_PROMPT_R1.md`.
"""
    old_next.write_text(next_prompt, encoding="utf-8")

    insert_after_title(ROOT / "README.md", readme_block)
    insert_after_title(ROOT / "PROJECT_HANDOVER.md", handover_block)
    append_once(ROOT / "PROJECT_GUIDELINES.md", guideline_block)
    append_once(ROOT / "logs/classical-tamil-research-program-decisions.md", decision_block)


if __name__ == "__main__":
    main()
