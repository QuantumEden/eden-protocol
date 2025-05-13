import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

import json
from eden_payload_generator.eden_payload_generator import generate_eden_payload

# Loop test for batch payload generation
for i in range(3):
    profile = {
        "mbti": "INTP",
        "iq": 135 + i,
        "eq": 115 + i,
        "moral": "freedom",
        "sacred_path": "Stoicism",
        "group_opt_in": i % 2 == 0
    }

    user_id = f"test_subject_{i:03d}"
    secret_key = f"loop_key_{i:03d}"

    payload = generate_eden_payload(user_id, profile, secret_key)

    print(f"\n=== Payload {i} ===\n")
    print(json.dumps(payload, indent=2))
