# test_integrity_snapshot.py – Eden Protocol Infra Diagnostic
# Validates DAO readiness and user progression state across payload, XP, and Tree layers

import json
from datetime import datetime
from os.path import dirname, join
import sys

# Import local mock payloads + merit ledger
sys.path.insert(0, join(dirname(__file__), '..', 'sim'))
sys.path.insert(0, join(dirname(__file__), '..', 'infra'))

from eden_payload_viewer import get_all_mock_payloads
from meritcoin_ledger import load_ledger

TREE_MINIMUM = 50
DAO_ENTRY_LEVEL = 7

def validate_tree_health(tree):
    return all(value >= TREE_MINIMUM for value in tree.values())

def find_merit_log_for_user(user_id, ledger):
    return [entry for entry in ledger if entry["user_id"] == user_id]

def snapshot_dao_readiness():
    payloads = get_all_mock_payloads()
    ledger = load_ledger()

    snapshot = []

    for user in payloads:
        user_id = user.get("user_id") or "unknown"
        level = user.get("xp_awarded", 0) // 100 + 1  # approximation
        tree = user.get("tree_traits", {})
        tree_ok = validate_tree_health(tree)

        merit_logs = find_merit_log_for_user(user_id, ledger)
        merit_synced = any(log["level"] >= DAO_ENTRY_LEVEL for log in merit_logs)

        snapshot.append({
            "user_id": user_id,
            "level_estimate": level,
            "tree_ok": tree_ok,
            "merit_synced": merit_synced,
            "eligible_for_dao": tree_ok and merit_synced and level >= DAO_ENTRY_LEVEL
        })

    print("\n=== DAO Readiness Snapshot –", datetime.utcnow().isoformat(), "UTC ===\n")
    print(json.dumps(snapshot, indent=2))

if __name__ == "__main__":
    snapshot_dao_readiness()
