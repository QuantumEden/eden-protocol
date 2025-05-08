# Secure Enclave Simulation – Signature & Token Validation Test

from src.secure_enclave.secure_enclave import (
    generate_signature,
    validate_signature,
    issue_verification_token
)

print("\n=== Secure Enclave Simulation: Validation & Token Generation ===\n")

# Test data
user_id = "user_alpha"
trait = "INFP"
secret_key = "quantumeden_enclave"

# Step 1: Generate secure signature
signature = generate_signature(user_id, trait, secret_key)
print(f"Generated Signature: {signature}")

# Step 2: Validate signature (should succeed)
validation_pass = validate_signature(user_id, trait, signature, secret_key)
print(f"Signature Valid: {validation_pass}")

# Step 3: Issue verification token
token = issue_verification_token(user_id, trait, validation_pass)
print("\nIssued Verification Token:")
for key, value in token.items():
    print(f"{key}: {value}")
