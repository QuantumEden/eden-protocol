# zk_verification_test.py – Eden Protocol Integration Test
# Validates zk-readiness of payload and mock zero-knowledge proof structure

import sys, os, json
import hashlib
from datetime import datetime

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'src')))

from eden_payload_generator.eden_payload_generator import generate_eden_payload
from biometrics.biometric_integrity_check import log_biometric_event, verify_biometric_signature

def simulate_zk_proof(payload: dict, secret_key: str) -> dict:
    """
    Generates a mock zero-knowledge-compatible structure from payload.
    In production, this would interface with ZK-SNARK/STARK circuits.
    """
    core_fields = {
        "user_id": payload["user_id"],
        "xp_awarded": payload["xp_awarded"],
        "eligible_for_dao": payload["eligible_for_dao"],
        "soulform_id": payload.get("soulform_id", None)
    }

    combined = json.dumps(core_fields, sort_keys=True) + secret_key
    zk_commitment = hashlib.sha256(combined.encode()).hexdigest()

    return {
        "zk_commitment": zk_commitment,
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "proof_type": "mock-ZK-SHA256"
    }

# === Test Profile
user_id = "zk_user_888"
secret_key = "zk_secret_888"

profile = {
    "mbti": "ISTJ",
    "iq": 130,
    "eq": 110,
    "moral": "liberty",
    "sacred_path": "Hermeticism",
    "group_opt_in": True,
    "current_soulform": {
        "id": "wyrm",
        "name": "Twilight Serpent",
        "elemental_affinity": "Air",
        "activated_at": datetime.utcnow().isoformat() + "Z"
    }
}

# === Step 1: Generate payload
payload = generate_eden_payload(user_id, profile, secret_key)

print("\n🌱 Payload Snapshot:")
print(json.dumps(payload, indent=2))

# === Step 2: Simulate zk-proof commitment
zk_result = simulate_zk_proof(payload, secret_key)
print("\n🔐 Simulated zk-Proof:")
print(json.dumps(zk_result, indent=2))

# === Step 3: Biometric phrase and signature
bio_log = log_biometric_event(user_id, "My true self was never lost", context="zk unlock")
verified = verify_biometric_signature("My true self was never lost", bio_log["signature_hash"])

print("\n🧬 Biometric Signature Check:")
print(json.dumps(bio_log, indent=2))
print("✅ Signature Verified:", verified)

# === Final assertions
assert payload["zk_ready"] == True, "❌ Payload not marked as ZK-ready"
assert isinstance(zk_result["zk_commitment"], str), "❌ Invalid ZK commitment"
assert verified == True, "❌ Biometric signature verification failed"

print("\n✅ ZK integration test passed.\n")
