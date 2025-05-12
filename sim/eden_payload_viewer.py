import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

import json
from eden_payload_generator.eden_payload_generator import generate_eden_payload

sample_user = {
    "mbti": "ENFP",
    "iq": 120,
    "eq": 130,
    "moral": "liberty",
    "sacred_path": "Taoism",
    "group_opt_in": True
}

user_id = "dreamer_777"
secret_key = "key_dreamscape"

payload = generate_eden_payload(user_id, sample_user, secret_key)

print("\n=== Eden Payload Viewer Output ===\n")
print(json.dumps(payload, indent=2))
