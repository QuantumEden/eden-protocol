# grant_dispenser.py – DAO Symbolic Grant Module
# Distributes XP, meritcoin, or transformation unlocks to verified users

import json
from datetime import datetime
from uuid import uuid4

GRANT_LOG = []

def current_time():
    return datetime.utcnow().isoformat() + "Z"

def generate_meritcoin_id():
    return f"MERIT-GRANT-{uuid4().hex[:6].upper()}"

def grant_xp(user_id: str, amount: int, reason: str) -> dict:
    """Issues XP as a symbolic DAO grant."""
    entry = {
        "type": "xp",
        "user_id": user_id,
        "amount": amount,
        "reason": reason,
        "timestamp": current_time()
    }
    GRANT_LOG.append(entry)
    return entry

def grant_meritcoin(user_id: str, level: int, reason: str, soulform_id: str = None) -> dict:
    """Issues a symbolic MeritCoin as recognition for contribution."""
    entry = {
        "type": "meritcoin",
        "user_id": user_id,
        "meritcoin_id": generate_meritcoin_id(),
        "level": level,
        "soulform_id": soulform_id or "none",
        "reason": reason,
        "timestamp": current_time()
    }
    GRANT_LOG.append(entry)
    return entry

def grant_transformation(user_id: str, soulform_id: str, token: str = None) -> dict:
    """Records a soulform transformation grant from DAO."""
    entry = {
        "type": "transformation",
        "user_id": user_id,
        "soulform_id": soulform_id,
        "token": token or f"SOUL-{uuid4().hex[:6]}",
        "timestamp": current_time()
    }
    GRANT_LOG.append(entry)
    return entry

def get_grant_log():
    return GRANT_LOG

# Example CLI test
if __name__ == "__main__":
    print("Granting XP...")
    print(json.dumps(grant_xp("seer_alch_001", 75, "DAO proposal co-authorship"), indent=2))

    print("Granting MeritCoin...")
    print(json.dumps(grant_meritcoin("sage_dao_002", 10, "Led Group Ritual", "seraph"), indent=2))

    print("Granting Transformation...")
    print(json.dumps(grant_transformation("rogue_echo_003", "phoenix"), indent=2))

    print("Current Log:")
    print(json.dumps(get_grant_log(), indent=2))
