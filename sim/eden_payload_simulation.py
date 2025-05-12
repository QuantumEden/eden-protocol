import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import json
from src.eden_payload_generator.eden_payload_generator import generate_eden_payload

# Test profile for symbolic payload validation
profile = {
    "mbti": "INTJ",
    "iq": 140,
    "eq": 120,
    "moral": "truth",
    "sacred_path": "Hermeticism",
    "group_opt_in": False
}

# Simulated user credentials
user_id = "observer_000"
secret_key = "vault_key_123"

# Generate full Eden payload
payload = generate_eden_payload(user_id, profile, secret_key)

# Output formatted for clarity
print("\n=== Eden Protocol Payload Diagnostic ===\n")
print(json.dumps(payload, indent=2))
