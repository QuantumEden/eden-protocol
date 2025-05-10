# /sim/open_enclave_simulation.py

from secure_enclave.open_enclave_handler import sign_payload, validate_token, generate_user_id

# Simulated payload for testing
test_payload = {
    "discipline": 72,
    "resilience": 53,
    "empathy": 94,
    "level": 6,
    "xp": 540
}

# Generate a simulated user ID
user_id = generate_user_id()

# Sign the payload using simulated Kyber/Dilithium process
token = sign_payload(test_payload, user_id)

# Validate the signed token
is_valid = validate_token(test_payload, token, user_id)

# Display results
print("\n--- OPEN ENCLAVE SIMULATION ---")
print(f"User ID     : {user_id}")
print(f"Payload     : {test_payload}")
print(f"Signature   : {token}")
print(f"Is Valid?   : {is_valid}")
