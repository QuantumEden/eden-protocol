import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

import json
from eden_payload_generator.eden_payload_generator import generate_eden_payload

# Minimal profile for viewing payload structure
profile = {
    "mbti": "INTJ",
    "iq": 140,
    "eq": 120,
    "moral": "truth",
    "sacred_path": "Hermeticism",
    "group_opt_in": True
}

user_id = "seer_011"
secret_key = "vault_key_456"

payload = generate_eden_payload(user_id, profile, secret_key)

print("\n=== Eden Payload Structure View ===\n")
print(json.dumps(payload, indent=2))
