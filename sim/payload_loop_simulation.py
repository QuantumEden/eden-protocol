import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

import json
from eden_payload_generator.eden_payload_generator import generate_eden_payload

# Sample user profile for full pipeline test
test_profile = {
    "mbti": "INFJ",
    "iq": 135,
    "eq": 122,
    "moral": "care",
    "sacred_path": "Zen Buddhism",
    "group_opt_in": True
}

user_id = "test_user_001"
secret_key = "test_secret_key"

payload = generate_eden_payload(user_id, test_profile, secret_key)

print("\n=== Eden Payload Simulation ===\n")
print(json.dumps(payload, indent=2))
