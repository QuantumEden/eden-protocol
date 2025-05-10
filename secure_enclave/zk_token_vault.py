# /secure_enclave/zk_token_vault.py

import hashlib
import json
import os

# Simulated ZK token vault for XP and behavior commitments
vault = {}

# Helper: Generate a ZK-style commitment hash
def _commit(user_id: str, data: dict) -> str:
    payload = json.dumps(data, sort_keys=True) + user_id
    return hashlib.sha3_512(payload.encode()).hexdigest()

# Commit an XP gain (or other behavior) securely
def commit_xp(user_id: str, xp_amount: int) -> str:
    commitment = _commit(user_id, {"xp": xp_amount})
    vault[user_id] = vault.get(user_id, []) + [commitment]
    return commitment

# Validate a claimed XP gain against the vault
def validate_commit(user_id: str, xp_amount: int, commitment: str) -> bool:
    expected = _commit(user_id, {"xp": xp_amount})
    return expected == commitment and commitment in vault.get(user_id, [])

# Export the vault to a JSON file for blockchain simulation
def export_commitments(filepath="data/zk_commitments.json"):
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, "w") as f:
        json.dump(vault, f, indent=2)

# Example usage for test
def simulate():
    user_id = "user-eden-001"
    xp = 540
    token = commit_xp(user_id, xp)
    print("ZK Commitment:", token)
    print("Valid?", validate_commit(user_id, xp, token))
    export_commitments()

if __name__ == "__main__":
    simulate()
