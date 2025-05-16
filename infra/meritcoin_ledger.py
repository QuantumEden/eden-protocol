# meritcoin_ledger.py – Eden Protocol Infra
# Logs soulbound XP commits and symbolic milestone events

import os
import json
from datetime import datetime

LEDGER_PATH = os.path.join(os.path.dirname(__file__), 'meritcoin_commit_log.json')

def load_ledger():
    if os.path.exists(LEDGER_PATH):
        with open(LEDGER_PATH, 'r') as f:
            return json.load(f)
    return []

def save_ledger(log):
    with open(LEDGER_PATH, 'w') as f:
        json.dump(log, f, indent=2)

def log_commit(user_id, level, xp, reason, soulform=None):
    entry = {
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "user_id": user_id,
        "level": level,
        "xp": xp,
        "reason": reason,
    }

    if soulform:
        entry["soulform"] = {
            "id": soulform.get("id"),
            "name": soulform.get("name"),
            "element": soulform.get("elemental_affinity")
        }

    log = load_ledger()
    log.append(entry)
    save_ledger(log)
    return entry

# Example usage
if __name__ == "__main__":
    print("Simulating merit commit...")
    commit = log_commit(
        user_id="user_alch_001",
        level=7,
        xp=1200,
        reason="Completed Legacy Trial",
        soulform={"id": "phoenix", "name": "Ashborn Phoenix", "elemental_affinity": "Fire"}
    )
    print(json.dumps(commit, indent=2))
