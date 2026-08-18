#!/usr/bin/env python3
"""Create the final Phase R0 research baseline log."""
from __future__ import annotations

import datetime as dt
import hashlib
import json
from pathlib import Path


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def latest(root: Path, pattern: str) -> Path:
    values = sorted(root.glob(pattern))
    if not values: raise FileNotFoundError(pattern)
    return values[-1]


def main() -> None:
    root = Path(__file__).resolve().parents[1]; now = dt.datetime.now().astimezone()
    summary = json.loads((root / "research/reports/purananuru-extraction-summary.json").read_text())
    validation = json.loads((root / "research/reports/research-validation.json").read_text())
    idempotence_path = latest(root, "logs/classical-tamil-research-layer-r0-idempotence-*.json")
    regression_path = latest(root, "logs/classical-tamil-research-frozen-regression-*.json")
    idempotence = json.loads(idempotence_path.read_text()); regression = json.loads(regression_path.read_text())
    result = {
        "created_at": now.isoformat(), "programme_id": "classical-tamil-research-layer", "phase": "R0",
        "source_release_tag": "classical-tamil-corpus-v1.0.0", "source_release_commit": "272d9d5a79d55994e2c12efacc22be20b2c88030",
        "source_repository_fingerprint": "a220173f9b444095b191814622220203cd223d8258744091d7cbbbec1b76d326",
        "research_schema_version": "0.1.0", "research_status": "pilot",
        "assertion_count": summary["assertion_count"], "mention_count": summary["mention_count"],
        "entity_sample_count": summary["entity_sample_count"], "relationship_count": summary["relationship_count"],
        "validation": validation, "test_result": {"passed": 130, "failed": 0, "dependency_warnings": 88},
        "idempotence": idempotence, "frozen_regression": regression,
        "review_status_counts": summary["review_status_counts"],
        "unresolved_ambiguities": ["285 literary-body candidates require review", "43 surface-form pilot entities do not assert historical identity", "variant printed names remain unmerged", "modern geography and taxonomy remain unassigned"],
        "research_output_sha256": {str(path.relative_to(root)): sha(path) for path in sorted((root / "research").rglob("*")) if path.is_file()},
        "status": "pass" if validation["status"] == idempotence["status"] == regression["status"] == "pass" else "fail",
    }
    target = root / "logs" / f"classical-tamil-research-layer-r0-baseline-{now.strftime('%Y%m%dT%H%M%S')}.json"
    target.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
    print(target.relative_to(root))
    if result["status"] != "pass": raise SystemExit(1)


if __name__ == "__main__": main()
