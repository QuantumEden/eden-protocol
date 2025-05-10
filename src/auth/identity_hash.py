# /src/auth/identity_hash.py

"""
Identity Hash Engine for Eden Protocol

This module generates deterministic, anonymized user IDs based on:
- Core psychometric traits (e.g., MBTI, moral foundation, aptitude profile)
- Device-specific biometric signature (optional hash)

These hashes are used for Zero-Knowledge (ZK)-style anchoring and DAO access
without exposing raw user data.
"""

import hashlib
import json

def generate_identity_hash(psychometric_profile: dict, device_id: str = "") -> str:
    """
    Generate a stable SHA-256 hash from psychometric traits + device salt.
    This serves as a pseudonymous user ID.
    """
    stable_payload = {
        "mbti": psychometric_profile.get("mbti"),
        "moral": sorted(psychometric_profile.get("morality", [])),
        "aptitude": sorted(psychometric_profile.get("aptitude", [])),
        "interests": sorted(psychometric_profile.get("interests", []))
    }
    payload_str = json.dumps(stable_payload, sort_keys=True) + device_id
    return hashlib.sha256(payload_str.encode("utf-8")).hexdigest()

# Simulated profile test
if __name__ == "__main__":
    profile = {
        "mbti": "INFJ",
        "morality": ["Care", "Fairness", "Liberty"],
        "aptitude": ["Verbal", "Creative"],
        "interests": ["Artistic", "Investigative"]
    }
    device_salt = "OuraRingSerial123"

    user_hash = generate_identity_hash(profile, device_salt)
    print("\n[IDENTITY HASH RESULT]")
    print(f"Hash: {user_hash}")
