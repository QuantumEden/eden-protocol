# grant_dispenser.py – DAO Symbolic Grant Module
# Distributes XP, meritcoin, or transformation unlocks to verified users

import json
from datetime import datetime

GRANT_LOG = []

def grant_xp(user_id, amount, reason):
    entry = {
        "type": "xp",
        "user_id": user_id,
        "amount": amount,
        "reason": reason,
        "timestamp": datetime.utcnow().isoformat() + "Z"
    }
    GRANT_LOG.append(entry)
    return entry

def grant_meritcoin(user_id, meritcoin_id, level, soulform_id=None):
    entry = {
        "type": "meritcoin",
        "user_id": user_id,
        "meritcoin_id": meritcoin_id,
        "level": level,
        "soulform_id": soulform_id,
        "timestamp": datetime.utcnow().isoformat() + "Z"
    }
    GRANT_LOG.append(entry)
    return entry

def get_grant_log():
    return GRANT_LOG

# Example
if __name__ == "__main__":
    print("Granting XP...")
    print(json.dumps(grant_xp("user_alch_001", 75, "DAO proposal co-authorship"), indent=2))

    print("Granting MeritCoin...")
    print(json.dumps(grant_meritcoin("user_sage_002", "MERIT-DAO-01", 9, "dragon"), indent=2))

    print("Log:")
    print(json.dumps(get_grant_log(), indent=2))
