# tests/integration/test_integrity_snapshot.py – Eden Protocol DAO Integrity Test
# Validates DAO readiness and user progression across payloads and ledger history

import os
import sys
import json
from datetime import datetime

# Patch paths to source modules
base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.insert(0, os.path.join(base_path, 'sim'))
sys.path.insert(0, os.path.join(base_path, 'infra'))

# Imports
from eden_payload_viewer import get_all_mock_payloads
from xp.meritcoin_ledger import load_ledger

# DAO Thresholds
TREE_MINIMUM = 50
DAO_ENTRY_LEVEL = 7

def validate_tree(tree: dict) -> bool:
    """
    Ensures all core traits meet symbolic thresholds.
    """
    return all(score >= TREE_MINIMUM for score in tree.values())

def find_ledger_entries(user_id: str, ledger: list) -> list:
    """
    Filters meritcoin ledger for a given user.
    """
    return [entry for entry in ledger if entry["user_id"] == user_id]

def test_integrity_snapshot():
    """
    Cross-validates mock payloads against DAO trait and XP thresholds.
    Prints results for DAO onboarding status.
    """
    payloads = get_all_mock_payloads()
    ledger = load_ledger()
    results = []

    print(f"\n📊 DAO Readiness Integrity Snapshot — {datetime.utcnow().isoformat()} UTC\n")

    for payload in payloads:
        user_id = payload.get("user_id", "unknown")
        level = payload.get("xp_awarded", 0) // 100 + 1
        tree = payload.get("tree_traits", {})
        eligible_tree = validate_tree(tree)
        merit_logs = find_ledger_entries(user_id, ledger)
        merit_synced = any(log["level"] >= DAO_ENTRY_LEVEL for log in merit_logs)

        eligible = level >= DAO_ENTRY_LEVEL and eligible_tree and merit_synced

        user_result = {
            "user_id": user_id,
            "level_estimate": level,
            "tree_ok": eligible_tree,
            "merit_synced": merit_synced,
            "eligible_for_dao": eligible
        }

        print(json.dumps(user_result, indent=2))
        results.append(user_result)

        assert isinstance(tree, dict), f"❌ Invalid tree for {user_id}"
        assert "xp_awarded" in payload, f"❌ Missing XP for {user_id}"
        assert isinstance(merit_logs, list), f"❌ Ledger lookup failed for {user_id}"

    print("\n✅ DAO eligibility audit completed.\n")
    return results


# === CLI Diagnostic Run ===
if __name__ == "__main__":
    test_integrity_snapshot()
