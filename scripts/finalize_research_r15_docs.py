#!/usr/bin/env python3
"""Finalize R1.5 continuity sections without rewriting historical handover text."""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

HANDOVER_MARKER = "<!-- R1_REVIEW_WORKFLOW_COMPLETE_20260818 -->"
HANDOVER_NEXT = "## 1. Repository authority"
README_MARKER = "<!-- R1_REVIEW_WORKFLOW_COMPLETE_20260818 -->"
README_NEXT = "## Repository release checkpoint"

HANDOVER_SECTION = """<!-- R15_ACCEPTANCE_COMPLETE_20260818 -->
## Active handover — R1.5 acceptance complete, merge gate next

R1.5 Classical Tamil Concept Matrix foundation is complete on
`research/classical-tamil-concept-matrix-r1.5` and is proposed to `main` in
PR #3. Do **not** begin R2 until that validated PR is merged and live `main`
is re-inspected.

Accepted R1.5 boundary:

- R0 evidence schema `0.1.0` remains intact: 2,867 assertions, 285 body
  candidates, 43 pilot entities, and 51 relationships.
- R1 workflow schema `0.2.0` remains intact with 8 append-only review events,
  3 conservative entity-resolution decisions, and 0 verified historical
  identities.
- R1.5 concept/observation schema is `0.3.0`.
- The concept registry contains 36 definitions, including Akam/Puram, seven
  tiṇai categories, first-class tuṟai states, five landscape concept families,
  named-entity families, and lived-life dimensions.
- The bounded Puṟanāṉūṟu pilot contains 8 provenance-bearing observations across
  6 records, 7 populated concepts, and 7 populated dimensions.
- All 8 pilot observations are `SOURCE_EXPLICIT` and `reviewed`; there are 0
  external-historical observations, 0 interpretive observations, and 0 verified
  historical identities.
- `இறைவன்` and `ஆய்` remain generic ruler-role observations with unresolved
  historical identity.
- Matrix cells are deterministic evidence views, not unsupported booleans;
  empty cells mean only that qualifying evidence is not currently recorded.
- Tolkāppiyam has a separate `GRAMMATICAL_CONCEPT_EVIDENCE` /
  `tolkappiyam_mapping` stream contract and 0 production R1.5 observations.

Recorded acceptance evidence:

- PR #3 acceptance workflow run `32131938420` passed at research head
  `b93e021d8c83717d78cf0c796045f07cccdf47a1` before continuity-only finalization.
- R0, R1, R1.5 pilot, and R1.5 acceptance validators all passed with zero
  errors/warnings.
- Complete regression suite: **203 passed**.
- R1 and R1.5 deterministic regeneration passed; R1.5 outputs were byte-stable
  and all declared primary inputs remained unchanged.
- R1.5 acceptance validator found 27/27 required foundation concepts, 0 orphan
  observation assertions, 0 orphan observation concepts, 0 orphan relationship
  assertions/entities, and 0 invalid relationship subjects.
- Full repository audit passed across 8,768 files.
- Corpus 1.1.0 and Tolkāppiyam non-drift checks passed.
- R1 primary evidence/history/relationship files remained unchanged by
  generation.

Durable acceptance records:

- `logs/classical-tamil-research-r15-validation-20260818T164600.json`
- `logs/classical-tamil-research-r15-acceptance-20260818T164600.json`
- `logs/classical-tamil-research-r15-idempotence-20260818T164600.json`
- `logs/classical-tamil-research-r15-baseline-20260818T164600.json`

The R1.5 continuation prompt is archived at
`docs/history/NEXT_CHAT_PROMPT_R15.md`. `NEXT_CHAT_PROMPT.md` now contains the
R2 startup contract, but that prompt itself forbids R2 work until PR #3 has
been merged into `main`.

The historical R0/R1 handover material below is retained as provenance. This
active section overrides stale branch/status paragraphs in that historical
material.

"""

README_SECTION = """<!-- R15_ACCEPTANCE_COMPLETE_20260818 -->
## Derived research layer — R1.5 acceptance complete

R0 Puṟanāṉūṟu evidence remains at schema `0.1.0`; R1 review/entity-resolution
workflow remains at `0.2.0`; R1.5 adds the independently versioned Classical
Tamil concept/observation model at `0.3.0`. The research layer does not edit the
frozen Corpus 1.1.0 evidence.

The validated R1.5 branch is `research/classical-tamil-concept-matrix-r1.5`
(PR #3). Its bounded Puṟanāṉūṟu pilot has 8 evidence-backed observations across
6 records. The concept foundation covers Akam/Puram, tiṇai, tuṟai, five
landscape families, named entities, and lived-life dimensions while keeping
classification provenance explicit. Tolkāppiyam has a separate grammatical
concept-evidence contract and no production R1.5 observations.

The acceptance workflow passed 203 tests, deterministic regeneration, the full
repository audit, Corpus/Tolkāppiyam non-drift, and primary-history
non-mutation. R2 remains blocked until PR #3 is merged into `main`. See
[`research/README.md`](research/README.md),
[`docs/CLASSICAL_TAMIL_RESEARCH_MATRIX.md`](docs/CLASSICAL_TAMIL_RESEARCH_MATRIX.md),
and [`PROJECT_HANDOVER.md`](PROJECT_HANDOVER.md).

"""


def replace_section(text: str, marker: str, next_heading: str, replacement: str) -> str:
    start = text.find(marker)
    if start < 0:
        # Allow reruns after the marker has already been upgraded.
        upgraded = "<!-- R15_ACCEPTANCE_COMPLETE_20260818 -->"
        start = text.find(upgraded)
        if start < 0:
            raise RuntimeError(f"continuity marker not found before {next_heading}")
    end = text.find(next_heading, start)
    if end < 0:
        raise RuntimeError(f"continuity boundary heading not found: {next_heading}")
    return text[:start] + replacement + text[end:]


def write_if_changed(path: Path, content: str) -> bool:
    old = path.read_text(encoding="utf-8")
    if old == content:
        return False
    path.write_text(content, encoding="utf-8")
    return True


def main() -> None:
    handover_path = ROOT / "PROJECT_HANDOVER.md"
    handover = handover_path.read_text(encoding="utf-8")
    handover = replace_section(handover, HANDOVER_MARKER, HANDOVER_NEXT, HANDOVER_SECTION)
    handover_changed = write_if_changed(handover_path, handover)

    readme_path = ROOT / "README.md"
    readme = readme_path.read_text(encoding="utf-8")
    readme = replace_section(readme, README_MARKER, README_NEXT, README_SECTION)
    readme_changed = write_if_changed(readme_path, readme)

    guidelines_path = ROOT / "PROJECT_GUIDELINES.md"
    guidelines = guidelines_path.read_text(encoding="utf-8")
    old = "Read it before designing R1.5, R2, or any matrix/ontology extraction."
    new = (
        "R1.5 is the accepted concept-matrix foundation. Read this specification before "
        "designing R2 or any later matrix/ontology extraction, and preserve the R1.5 "
        "evidence/provenance boundary unless a versioned change is explicitly approved."
    )
    if old in guidelines:
        guidelines = guidelines.replace(old, new, 1)
    elif new not in guidelines:
        raise RuntimeError("expected PROJECT_GUIDELINES R1.5 sentence not found")
    guidelines_changed = write_if_changed(guidelines_path, guidelines)

    print(
        {
            "PROJECT_HANDOVER.md": handover_changed,
            "README.md": readme_changed,
            "PROJECT_GUIDELINES.md": guidelines_changed,
        }
    )


if __name__ == "__main__":
    main()
