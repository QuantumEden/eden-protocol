# src/biometrics/biometric_integrity_check.py
# Symbolic integrity checker for biometric inputs, voice signatures, and voluntary disclosures

import hashlib
from datetime import datetime
from typing import Dict, Any

# Simulated biometric input log for test/demo use
BIOMETRIC_LOG = []

def hash_biometric_signature(signature: str) -> str:
    """
    Hashes a biometric signature (e.g., voice print, input pattern) using SHA-256.
    """
    return hashlib.sha256(signature.encode("utf-8")).hexdigest()

def verify_biometric_signature(provided_signature: str, stored_hash: str) -> bool:
    """
    Compares a provided signature against a stored hash.
    """
    return hash_biometric_signature(provided_signature) == stored_hash

def log_biometric_event(user_id: str, signature: str, context: str) -> Dict[str, Any]:
    """
    Logs a hashed biometric event with timestamp and symbolic context.
    """
    entry = {
        "user_id": user_id,
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "signature_hash": hash_biometric_signature(signature),
        "context": context
    }
    BIOMETRIC_LOG.append(entry)
    return entry

def get_biometric_log() -> list:
    return BIOMETRIC_LOG

# Optional test block
if __name__ == "__main__":
    print("\n🔐 Biometric Integrity Test\n")

    user = "user_sentinel_001"
    raw_signature = "My sacred phrase for DAO initiation"
    context = "DAO onboarding"

    # Log event
    record = log_biometric_event(user, raw_signature, context)
    print("Logged Event:")
    print(record)

    # Attempt verification
    test_input = "My sacred phrase for DAO initiation"
    result = verify_biometric_signature(test_input, record["signature_hash"])
    print("\nVerification Passed?" , result)
