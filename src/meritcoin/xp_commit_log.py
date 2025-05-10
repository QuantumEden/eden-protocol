# /src/meritcoin/xp_commit_log.py

"""
XP Commit Log — Simulated Eden Ledger

Stores SHA-256 hashed XP commitments as a local proof-of-truth chain.
Future versions can write to smart contracts or zkRollup-compatible nodes.
"""

import json
import os
from datetime import datetime
from src.blockchain.xp_commit_encoder import generate_xp_commit

LEDGER_PATH = "infra/ledger/meritcoin_xp_log.json"


def record_xp_commit(user_id: str, xp_amount: int, trait: str, source: str, mod_id: str = None):
    commit_hash = generate_xp_commit(user_id, xp_amount, trait, source, mod_id)
    entry = {
        "timestamp": datetime.utcnow().isoformat(),
        "user_id": user_id,
        "xp": xp_amount,
        "trait": trait,
        "source": source,
        "mod_id": mod_id,
        "commit_hash": commit_hash
    }

    ledger = []
    if os.path.exists(LEDGER_PATH):
        with open(LEDGER_PATH, 'r') as f:
            ledger = json.load(f)

    ledger.append(entry)

    with open(LEDGER_PATH, 'w') as f:
        json.dump(ledger, f, indent=2)

    print(f"✅ XP commit recorded: {commit_hash}")
    return commit_hash


# Example use
if __name__ == "__main__":
    record_xp_commit("user123", 60, "resilience", "mod", mod_id="tai_chi_001")
