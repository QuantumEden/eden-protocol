# /src/blockchain/xp_commit_encoder.py

"""
XP Commit Encoder — Eden Protocol

This module encodes XP events into cryptographic hashes using SHA-256.
Used to anchor XP gains, mod completions, and behavioral truths to the blockchain layer.
"""

import hashlib
import json
import datetime


def generate_xp_commit(user_id: str, xp_amount: int, trait: str, source: str, mod_id: str = None) -> str:
    """
    Generate a hashed XP commitment payload.
    
    Args:
        user_id (str): Unique user identifier
        xp_amount (int): Amount of XP earned
        trait (str): Trait being modified (e.g., discipline, empathy)
        source (str): Source of XP (e.g., core, mod, quest)
        mod_id (str, optional): Required if source is "mod"

    Returns:
        str: SHA-256 hash representing XP event
    """
    payload = {
        "user_id": user_id,
        "xp": xp_amount,
        "trait": trait,
        "source": source,
        "mod_id": mod_id,
        "timestamp": datetime.datetime.utcnow().isoformat()
    }
    encoded = json.dumps(payload, sort_keys=True)
    return hashlib.sha256(encoded.encode()).hexdigest()


# Example use case
if __name__ == "__main__":
    commit_hash = generate_xp_commit(
        user_id="user42",
        xp_amount=50,
        trait="discipline",
        source="mod",
        mod_id="tai_chi_001"
    )
    print("XP Commit Hash:", commit_hash)
