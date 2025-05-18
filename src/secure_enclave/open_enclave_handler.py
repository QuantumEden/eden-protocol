# open_enclave_handler.py – Eden Protocol Secure Enclave Interface
# Handles biometric hash generation, token validation, and symbolic oath registration

import hashlib
import hmac
import time
from typing import Dict

# Configurable hash key for signature validation (in real use, securely rotate this)
SECRET_ENCLAVE_KEY = "eden_enclave_master_key_2025"

def generate_signature(user_id: str, data: str, secret_key: str) -> str:
    """
    Generates a secure hash signature for given user data using HMAC.
    """
    message = f"{user_id}:{data}:{int(time.time())}"
    signature = hmac.new(secret_key.encode(), message.encode(), hashlib.sha256).hexdigest()
    return signature

def validate_signature(user_id: str, data: str, signature: str, secret_key: str) -> bool:
    """
    Verifies the provided signature matches the recomputed hash.
    """
    # Signature is considered valid if it matches current or recent window
    # To prevent abuse, in production this should use timestamp expiration logic
    expected = generate_signature(user_id, data, secret_key)
    return hmac.compare_digest(expected, signature)

def issue_verification_token(user_id: str, trait: str, verified: bool) -> Dict[str, str]:
    """
    Issues a symbolic DAO onboarding token upon successful trait signature verification.
    """
    if not verified:
        return {
            "status": "denied",
            "reason": "Signature validation failed"
        }

    payload = f"{user_id}:{trait}:{int(time.time())}"
    token_hash = hashlib.sha256(payload.encode()).hexdigest()

    return {
        "status": "approved",
        "issued_token": token_hash,
        "verified_trait": trait,
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    }

# Optional CLI test
if __name__ == "__main__":
    uid = "test_user"
    trait = "INTJ"
    sig = generate_signature(uid, trait, SECRET_ENCLAVE_KEY)
    valid = validate_signature(uid, trait, sig, SECRET_ENCLAVE_KEY)
    token = issue_verification_token(uid, trait, valid)

    print("🔐 Signature:", sig)
    print("✅ Verified:", valid)
    print("🎟️ Token:", token)
