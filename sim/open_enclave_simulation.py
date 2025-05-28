# /sim/open_enclave_simulation.py
# Eden Protocol – Secure Enclave Token Simulation

from secure_enclave.open_enclave_handler import (
    sign_payload,
    validate_token,
    generate_user_id
)
from datetime import datetime

# Simulated payload for testing
test_payload = {
    "discipline": 72,
    "resilience": 53,
    "empathy": 94,
    "level": 6,
    "xp": 540
}

def run_enclave_test():
    print("\n🔐 OPEN ENCLAVE SIMULATION – Secure Payload Signing\n")

    # Generate user ID
    user_id = generate_user_id()

    # Sign the payload
    token = sign_payload(test_payload, user_id)

    # Validate the token
    is_valid = validate_token(test_payload, token, user_id)

    # Output results
    print(f"Timestamp    : {datetime.utcnow().isoformat()}Z")
    print(f"User ID      : {user_id}")
    print(f"Payload      : {test_payload}")
    print(f"Signature    : {token}")
    print(f"Validation   : {'✅ Valid' if is_valid else '❌ Invalid'}\n")

    if not is_valid:
        raise ValueError("Open Enclave validation failed – token mismatch.")

if __name__ == "__main__":
    run_enclave_test()
