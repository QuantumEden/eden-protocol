import json
from eden_payload_generator.eden_payload_generator import generate_eden_payload

# Visual test for sacred_path propagation
profile = {
    "mbti": "INTJ",
    "iq": 140,
    "eq": 120,
    "moral": "truth",
    "sacred_path": "Hermeticism",
    "group_opt_in": False
}

user_id = "observer_000"
secret_key = "vault_key_123"

payload = generate_eden_payload(user_id, profile, secret_key)

print("\n=== Eden Protocol Payload Diagnostic ===\n")
print(json.dumps(payload, indent=2))
