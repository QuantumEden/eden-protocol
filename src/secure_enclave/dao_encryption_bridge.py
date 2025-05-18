# dao_encryption_bridge.py – Eden Protocol DAO Encryption Layer
# Simulates encrypted DAO communications using symbolic passphrases and consensus proofs

import hashlib
import hmac
import time
from typing import Dict

SECRET_DAO_KEY = "eden_dao_secret_sigil"

def encrypt_dao_message(message: str, sender_id: str) -> Dict[str, str]:
    """
    Encrypts a DAO-bound message using HMAC symbolic signature.
    """
    timestamp = str(int(time.time()))
    payload = f"{sender_id}|{message}|{timestamp}"

    signature = hmac.new(
        SECRET_DAO_KEY.encode(),
        payload.encode(),
        hashlib.sha256
    ).hexdigest()

    return {
        "message": message,
        "sender": sender_id,
        "timestamp": timestamp,
        "signature": signature
    }

def verify_dao_message(payload: Dict[str, str]) -> bool:
    """
    Verifies a symbolic DAO message HMAC signature.
    """
    reconstructed = f"{payload['sender']}|{payload['message']}|{payload['timestamp']}"
    expected_sig = hmac.new(
        SECRET_DAO_KEY.encode(),
        reconstructed.encode(),
        hashlib.sha256
    ).hexdigest()

    return expected_sig == payload.get("signature")

# Optional test
if __name__ == "__main__":
    encrypted = encrypt_dao_message("Activate Eden AI Archive", "seer_omega_9")
    verified = verify_dao_message(encrypted)

    print("🔐 Encrypted DAO Message:")
    for k, v in encrypted.items():
        print(f"{k}: {v}")
    print("\n✅ Verified:", verified)
