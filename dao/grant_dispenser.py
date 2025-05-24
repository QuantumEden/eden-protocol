# grant_dispenser.py – DAO Symbolic Grant Module
# Distributes XP, MeritCoin, or transformation unlocks to verified users
# Integrates zkXP tracking and Ritual Safeguard encoding

import json
from datetime import datetime
from uuid import uuid4
from typing import Optional

GRANT_LOG = []

def current_time() -> str:
    return datetime.utcnow().isoformat() + "Z"

def generate_meritcoin_id() -> str:
    return f"MERIT-GRANT-{uuid4().hex[:6].upper()}"

def generate_soul_token() -> str:
    return f"SOUL-{uuid4().hex[:6].upper()}"

def grant_xp(user_id: str, amount: int, reason: str, zkxp_hash: Optional[str] = None) -> dict:
    """Issues XP as a symbolic DAO grant."""
    entry = {
        "type": "xp",
        "user_id": user_id,
        "amount": amount,
        "reason": reason,
        "zkxp_hash": zkxp_hash or "none",
        "timestamp": current_time()
    }
    GRANT_LOG.append(entry)
    return entry

def grant_meritcoin(user_id: str, level: int, reason: str, soulform_id: Optional[str] = None, zkxp_hash: Optional[str] = None) -> dict:
    """Issues a symbolic MeritCoin as recognition for contribution."""
    entry = {
        "type": "meritcoin",
        "user_id": user_id,
        "meritcoin_id": generate_meritcoin_id(),
        "level": level,
        "soulform_id": soulform_id or "none",
        "reason": reason,
        "zkxp_hash": zkxp_hash or "none",
        "timestamp": current_time()
    }
    GRANT_LOG.append(entry)
    return entry

def grant_transformation(user_id: str, soulform_id: str, token: Optional[str] = None, zkxp_hash: Optional[str] = None) -> dict:
    """Records a soulform transformation grant from DAO."""
    entry = {
        "type": "transformation",
        "user_id": user_id,
        "soulform_id": soulform_id,
        "token": token or generate_soul_token(),
        "zkxp_hash": zkxp_hash or "none",
        "timestamp": current_time()
    }
    GRANT_LOG.append(entry)
    return entry

def get_grant_log() -> list:
    return GRANT_LOG

# Example CLI test
if __name__ == "__main__":
    print("Granting XP...")
    print(json.dumps(grant_xp("seer_alch_001", 75, "DAO proposal co-authorship", "zkxp001"), indent=2))

    print("Granting MeritCoin...")
    print(json.dumps(grant_meritcoin("sage_dao_002", 10, "Led Group Ritual", "seraph", "zkxp002"), indent=2))

    print("Granting Transformation...")
    print(json.dumps(grant_transformation("rogue_echo_003", "phoenix", None, "zkxp003"), indent=2))

    print("Current Log:")
    print(json.dumps(get_grant_log(), indent=2))
