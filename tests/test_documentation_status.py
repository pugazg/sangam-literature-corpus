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


def test_post_r15a_merge_continuity_activates_r2():
    for path in (
        "PROJECT_GUIDELINES.md",
        "PROJECT_HANDOVER.md",
        "NEXT_CHAT_PROMPT.md",
        "docs/DOCUMENTATION_STATUS.md",
        "docs/CLASSICAL_TAMIL_RESEARCH_MATRIX.md",
    ):
        text = read(path)
        assert "R2" in text
        assert "research/classical-tamil-concept-matrix-r2" in text or path == "docs/CLASSICAL_TAMIL_RESEARCH_MATRIX.md"
        assert "R2 remains blocked" not in text
        assert "Do not start R2" not in text

    handover = read("PROJECT_HANDOVER.md")
    assert "1e6684b09a5e41fc675ea3e07ba8b6a646d35830" in handover
    assert "explicitly authorized" in handover
    assert "R3" in handover and "blocked" in handover


def test_r15a_cadence_is_preserved_in_r15a_documents():
    for path in (
        "PROJECT_GUIDELINES.md",
        "PROJECT_HANDOVER.md",
        "docs/handover/r15a-production-review/README.md",
        "research/production/purananuru/README.md",
    ):
        text = read(path)
        assert "003–010" in text
        assert "011–035" in text
        assert "25-record" in text


def test_r2_scope_and_benchmark_are_documented():
    for path in (
        "PROJECT_HANDOVER.md",
        "PROJECT_GUIDELINES.md",
        "NEXT_CHAT_PROMPT.md",
        "docs/DOCUMENTATION_STATUS.md",
        "docs/r2/ROADMAP.md",
    ):
        text = read(path)
        assert "Kuṟuntokai" in text
        assert "001–002" in text
        assert "29" in text

    roadmap = read("docs/r2/ROADMAP.md")
    assert "2,376" in roadmap
    assert "1,976" in roadmap
    assert "0.4.0" in roadmap
    assert "R3" in roadmap and "blocked" in roadmap


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
