# sacred_token_vault.py – Eden Protocol Token Vault
# Issues and verifies symbolic sacred tokens for ritual progression and soulform unlocks

import uuid
import hashlib
from datetime import datetime
from typing import Dict

# Simulated Vault Database (in-memory only for testing)
VAULT_DB = {}

def issue_verification_token(user_id: str, trait: str, verified: bool) -> Dict[str, str]:
    """
    Issues a symbolic verification token bound to user ID and trait signature.
    """
    if not verified:
        return {
            "status": "denied",
            "reason": "Verification failed. Ritual signature mismatch."
        }

    token_id = f"vault_token_{uuid.uuid4().hex[:8]}"
    timestamp = datetime.utcnow().isoformat() + "Z"
    hash_source = f"{user_id}-{trait}-{timestamp}"

    token_hash = hashlib.sha256(hash_source.encode()).hexdigest()

    VAULT_DB[token_id] = {
        "user_id": user_id,
        "trait": trait,
        "issued_at": timestamp,
        "token_hash": token_hash,
        "valid": True
    }

    return {
        "status": "issued",
        "token_id": token_id,
        "token_hash": token_hash,
        "issued_at": timestamp
    }

def revoke_token(token_id: str) -> bool:
    """
    Revokes an active sacred token.
    """
    if token_id in VAULT_DB:
        VAULT_DB[token_id]["valid"] = False
        return True
    return False

def validate_token(token_id: str, token_hash: str) -> bool:
    """
    Validates a token by ID and matching hash.
    """
    token = VAULT_DB.get(token_id)
    return token is not None and token["valid"] and token["token_hash"] == token_hash

# Optional CLI test
if __name__ == "__main__":
    print("\n🔐 Token Vault Test\n")
    token = issue_verification_token("user_xyz", "discipline", verified=True)
    print("Token Issued:", token)

    is_valid = validate_token(token["token_id"], token["token_hash"])
    print("Token Validated:", is_valid)

    revoked = revoke_token(token["token_id"])
    print("Token Revoked:", revoked)

    is_still_valid = validate_token(token["token_id"], token["token_hash"])
    print("Token Recheck:", is_still_valid)
