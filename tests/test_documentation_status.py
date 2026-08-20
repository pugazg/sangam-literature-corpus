from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

ACTIVE_DOCS = [
    "README.md",
    "PROJECT_GUIDELINES.md",
    "PROJECT_HANDOVER.md",
    "NEXT_CHAT_PROMPT.md",
    "docs/CLASSICAL_TAMIL_RESEARCH_MATRIX.md",
    "docs/classical-tamil-research-layer.md",
    "docs/SOURCE_TERMINOLOGY_POLICY.md",
    "docs/tolkappiyam-arivagam-integration-plan.md",
    "docs/DOCUMENTATION_STATUS.md",
    "docs/handover/r15a-production-review/README.md",
    "research/production/purananuru/README.md",
    "research/README.md",
    "logs/classical-tamil-research-program-decisions.md",
]

DELETED_BRANCHES = [
    "research/sangam-evidence-r0",
    "research/sangam-evidence-r1",
]


def read(path):
    return (ROOT / path).read_text(encoding="utf-8")


def test_active_document_inventory_exists():
    assert all((ROOT / path).is_file() for path in ACTIVE_DOCS)


def test_deleted_branches_are_not_current_operational_instructions():
    for path in ACTIVE_DOCS:
        if path == "docs/DOCUMENTATION_STATUS.md":
            continue
        text = read(path)
        for branch in DELETED_BRANCHES:
            assert branch not in text, f"stale deleted branch in {path}: {branch}"


def test_post_merge_continuity_is_r15a_and_r2_is_blocked():
    for path in ("README.md", "PROJECT_HANDOVER.md", "NEXT_CHAT_PROMPT.md"):
        text = read(path).lower()
        assert "r1.5a" in text
        assert "r2" in text and ("blocked" in text or "do not start" in text)
        assert "pr #3 must remain open" not in text

    for path in ("README.md", "PROJECT_HANDOVER.md"):
        text = read(path).lower()
        assert "pr #3" in text and "merged" in text


def test_r15a_cadence_is_documented():
    for path in (
        "PROJECT_GUIDELINES.md",
        "PROJECT_HANDOVER.md",
        "NEXT_CHAT_PROMPT.md",
        "docs/handover/r15a-production-review/README.md",
        "research/production/purananuru/README.md",
    ):
        text = read(path)
        assert "003–010" in text
        assert "011–035" in text
        assert "25-record" in text


def test_source_terminology_policy_is_linked_from_core_docs():
    for path in (
        "README.md",
        "PROJECT_GUIDELINES.md",
        "PROJECT_HANDOVER.md",
        "NEXT_CHAT_PROMPT.md",
        "docs/CLASSICAL_TAMIL_RESEARCH_MATRIX.md",
        "docs/classical-tamil-research-layer.md",
        "research/README.md",
    ):
        assert "SOURCE_TERMINOLOGY_POLICY.md" in read(path)


def test_disallowed_later_identity_terms_are_absent_from_active_docs():
    prohibited = [("brah" + "min").lower(), ("ve" + "dic").lower()]
    for path in ACTIVE_DOCS:
        text = read(path).lower()
        for term in prohibited:
            assert term not in text, f"disallowed later identity terminology in {path}"


def test_arivagam_plan_uses_active_repository_name():
    text = read("docs/tolkappiyam-arivagam-integration-plan.md")
    assert "pugazg/sangam-literature-corpus" in text


def test_retired_continuity_finalizer_cannot_rewrite_docs():
    text = read("scripts/finalize_research_r15_docs.py")
    assert "is retired" in text
    assert "raise SystemExit" in text
