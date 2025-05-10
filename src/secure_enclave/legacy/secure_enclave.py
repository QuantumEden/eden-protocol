# Secure Enclave Engine – Local Validation Module for Eden Protocol

from typing import Dict, Any
import hashlib

# Step 1: Simulate local signature generator
def generate_signature(user_id: str, raw_trait: str, secret_key: str) -> str:
    base_string = user_id + raw_trait + secret_key
    return hashlib.sha256(base_string.encode()).hexdigest()

# Step 2: Validate signature using known key
def validate_signature(user_id: str, raw_trait: str, provided_sig: str, secret_key: str) -> bool:
    expected_sig = generate_signature(user_id, raw_trait, secret_key)
    return expected_sig == provided_sig

# Step 3: Produce zero-knowledge compatible token stub
def issue_verification_token(user_id: str, trait: str, verified: bool) -> Dict[str, Any]:
    return {
        "user": user_id,
        "trait": trait,
        "verified": verified,
        "token": hashlib.md5((user_id + trait).encode()).hexdigest()
    }

# Optional local test
if __name__ == "__main__":
    USER_ID = "user007"
    TRAIT = "INTJ"
    SECRET_KEY = "enclave_secret"

    print("\n=== Secure Enclave Simulation ===")
    sig = generate_signature(USER_ID, TRAIT, SECRET_KEY)
    print(f"Generated Signature: {sig}")

    result = validate_signature(USER_ID, TRAIT, sig, SECRET_KEY)
    print(f"Validation Successful: {result}")

    token = issue_verification_token(USER_ID, TRAIT, result)
    print("Verification Token:")
    for k, v in token.items():
        print(f"{k}: {v}")
