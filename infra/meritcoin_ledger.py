# meritcoin_ledger.py – Eden Protocol Infra
# Logs soulbound XP commits and symbolic milestone events

import os
import json
from datetime import datetime
from uuid import uuid4

LEDGER_PATH = os.path.join(os.path.dirname(__file__), 'meritcoin_commit_log.json')

def load_ledger():
    """Load the existing MeritCoin ledger from file."""
    if os.path.exists(LEDGER_PATH):
        with open(LEDGER_PATH, 'r') as f:
            return json.load(f)
    return []

def save_ledger(log):
    """Write the current log state to disk."""
    with open(LEDGER_PATH, 'w') as f:
        json.dump(log, f, indent=2)

def generate_commit_id():
    return f"MERIT-{uuid4().hex[:8].upper()}"

def log_commit(user_id, level, xp, reason, traits_snapshot, soulform=None, verified_by="zkXP_stub_hash"):
    """Appends a validated MeritCoin commit to the ledger."""
    entry = {
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "user_id": user_id,
        "meritcoin_id": generate_commit_id(),
        "level": level,
        "xp": xp,
        "reason": reason,
        "verified_by": verified_by,
        "traits_snapshot": traits_snapshot,
        "soulform": soulform or {
            "id": "none",
            "name": "Untransformed",
            "element": "Neutral"
        }
    }

    log = load_ledger()
    log.append(entry)
    save_ledger(log)

    return entry

# CLI test
if __name__ == "__main__":
    print("Simulating MeritCoin commit...")

    traits = {
        "discipline": 72,
        "resilience": 85,
        "mindfulness": 78,
        "expression": 66,
        "physical_care": 70,
        "emotional_regulation": 74
    }

    soulform = {
        "id": "seraph",
        "name": "Wings of Conviction",
        "element": "Air",
        "transformed_at": "2025-05-14T17:00:00Z"
    }

    commit = log_commit(
        user_id="seer_alch_011",
        level=10,
        xp=950,
        reason="Completed DAO proposal and Shadow Quest",
        traits_snapshot=traits,
        soulform=soulform
    )

    print(json.dumps(commit, indent=2))
