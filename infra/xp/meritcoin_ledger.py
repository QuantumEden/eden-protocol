# meritcoin_ledger.py – Eden Protocol Infra
# Logs soulbound XP commits and symbolic milestone events with zkXP compatibility

import os
import json
from datetime import datetime
from uuid import uuid4

# === Ledger Storage Path
LEDGER_PATH = os.path.join(os.path.dirname(__file__), 'meritcoin_commit_log.json')


def generate_commit_id() -> str:
    """
    Generates a unique MeritCoin commit ID.
    """
    return f"MERIT-{uuid4().hex[:12].upper()}"


def load_ledger() -> list:
    """
    Loads the current ledger from file.
    """
    if os.path.exists(LEDGER_PATH):
        with open(LEDGER_PATH, "r") as f:
            return json.load(f)
    return []


def save_ledger(ledger: list) -> None:
    """
    Saves the full ledger to file.
    """
    with open(LEDGER_PATH, "w") as f:
        json.dump(ledger, f, indent=2)


def log_commit(user_id: str, level: int, xp: int, reason: str, traits_snapshot: dict,
               soulform: dict = None, verified_by: str = "zkXP_stub_hash") -> dict:
    """
    Append a verified XP/MeritCoin event to the soulbound commit ledger.

    Args:
        user_id: ID of the user.
        level: Level of the user at time of commit.
        xp: XP awarded.
        reason: Description of the milestone.
        traits_snapshot: Tree of Life traits at the time of commit.
        soulform: Optional soulform data.
        verified_by: zkXP proof or signature string.

    Returns:
        The commit entry object.
    """
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


# === CLI Test Mode ===
if __name__ == "__main__":
    print("🪙 Simulating MeritCoin commit...\n")

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
