#!/usr/bin/env python3
"""APEX Daily Gap Governor v0.1

Safe evidence runner.
This script reads gaps/active_gaps.json, selects one gap, performs safe file checks,
and writes a minimal receipt. It does not modify production systems.
"""

from __future__ import annotations

import json
from datetime import date, datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
GAPS_FILE = ROOT / "gaps" / "active_gaps.json"
RECEIPTS_DIR = ROOT / "daily_receipts"
TESTS_DIR = ROOT / "tests"
DECISIONS_DIR = ROOT / "decisions"
LOGS_DIR = ROOT / "logs"


def load_registry() -> dict:
    if not GAPS_FILE.exists():
        raise FileNotFoundError("Missing gaps/active_gaps.json")
    return json.loads(GAPS_FILE.read_text(encoding="utf-8"))


def select_gap(registry: dict) -> dict:
    gaps = registry.get("active_gaps", [])
    if not gaps:
        raise ValueError("No active gaps found")
    return sorted(gaps, key=lambda g: g.get("priority_score", 0), reverse=True)[0]


def safe_checks(gap: dict) -> dict:
    checks = {
        "active_gap_registry_exists": GAPS_FILE.exists(),
        "test_plan_exists": (TESTS_DIR / "daily_gap_governor_test_plan.md").exists(),
        "next_action_exists": (DECISIONS_DIR / "latest_next_smallest_action.md").exists(),
        "receipt_folder_exists": RECEIPTS_DIR.exists(),
    }
    return checks


def truth_status_from_checks(checks: dict) -> str:
    if all(checks.values()):
        return "TESTED_IN_SCOPE"
    return "NEEDS_EVIDENCE"


def write_receipt(gap: dict, checks: dict) -> Path:
    RECEIPTS_DIR.mkdir(parents=True, exist_ok=True)
    today = date.today().isoformat()
    path = RECEIPTS_DIR / f"{today}_{gap['gap_id']}_receipt.json"
    receipt = {
        "receipt_id": f"APEX-DGG-{today}-{gap['gap_id']}",
        "created_utc": datetime.now(timezone.utc).isoformat(),
        "gap_id": gap["gap_id"],
        "baseline_yesterday": gap.get("current_state"),
        "current_state_today": "Safe repository checks completed by Daily Gap Governor runner.",
        "what_changed": "A receipt was generated from safe file-existence checks.",
        "evidence_link_or_file": [
            "gaps/active_gaps.json",
            "tests/daily_gap_governor_test_plan.md",
            "decisions/latest_next_smallest_action.md",
            str(path.relative_to(ROOT)),
        ],
        "safe_checks": checks,
        "confidence_change": "+0.00 until human review or CI evidence confirms movement",
        "next_smallest_action": gap.get("next_smallest_action"),
        "truth_status": truth_status_from_checks(checks),
        "scale_state": "LOCKED",
        "limitations": [
            "This receipt proves only that the runner performed safe repository checks.",
            "It does not prove the OCODE runtime parser-renderer loop.",
            "It does not unlock scale mode."
        ]
    }
    path.write_text(json.dumps(receipt, indent=2), encoding="utf-8")
    return path


def append_log(gap: dict, receipt_path: Path, checks: dict) -> None:
    LOGS_DIR.mkdir(parents=True, exist_ok=True)
    log_path = LOGS_DIR / "daily_gap_governor_log.md"
    lines = [
        "\n## Daily Gap Governor run",
        f"Date: {date.today().isoformat()}",
        f"Selected gap: {gap['gap_id']}",
        f"Receipt: {receipt_path.relative_to(ROOT)}",
        f"Truth status: {truth_status_from_checks(checks)}",
        "Scale state: LOCKED",
    ]
    log_path.write_text((log_path.read_text(encoding="utf-8") if log_path.exists() else "# APEX Daily Gap Governor Log\n") + "\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    registry = load_registry()
    gap = select_gap(registry)
    checks = safe_checks(gap)
    receipt_path = write_receipt(gap, checks)
    append_log(gap, receipt_path, checks)
    print(f"Selected gap: {gap['gap_id']}")
    print(f"Receipt: {receipt_path.relative_to(ROOT)}")
    print(f"Truth status: {truth_status_from_checks(checks)}")
    print("Scale state: LOCKED")


if __name__ == "__main__":
    main()
