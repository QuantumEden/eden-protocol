# infra/test_integrity_snapshot.py – Eden Protocol Infra Diagnostic
# Validates DAO readiness and user progression state across payload, XP, and Tree layers

import json
import sys
import os
from datetime import datetime

# === Patch Import Paths ===
base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, os.path.join(base_path, 'sim'))
sys.path.insert(0, os.path.join(base_path, 'infra'))

# === Imports ===
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
        user_id = user.get("user_id", "unknown")
        level = user.get("xp_awarded", 0) // 100 + 1  # approximate level
        tree = user.get("tree_traits", {})
        tree_ok = validate_tree_health(tree) if tree else False

        merit_logs = find_merit_log_for_user(user_id, ledger)
        merit_synced = any(log.get("level", 0) >= DAO_ENTRY_LEVEL for log in merit_logs)

        snapshot.append({
            "user_id": user_id,
            "level_estimate": level,
            "tree_ok": tree_ok,
            "merit_synced": merit_synced,
            "eligible_for_dao": tree_ok and merit_synced and level >= DAO_ENTRY_LEVEL
        })

    print("\n=== 🧬 DAO Readiness Snapshot –", datetime.utcnow().isoformat(), "UTC ===\n")
    print(json.dumps(snapshot, indent=2))

if __name__ == "__main__":
    snapshot_dao_readiness()
