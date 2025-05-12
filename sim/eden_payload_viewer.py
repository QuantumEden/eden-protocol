import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

import json
from src.eden_payload_generator.eden_payload_generator import generate_eden_payload

# Quick viewer for sacred path diagnostics
profile = {
    "mbti": "ISFP",
    "iq": 115,
    "eq": 130,
    "moral": "care",
    "sacred_path": "Norse Paganism",
    "group_opt_in": True
}

user_id = "viewer_user"
secret_key = "mirror_vault_key"

payload = generate_eden_payload(user_id, profile, secret_key)

print("\n=== Eden Payload Viewer ===\n")
print(json.dumps(payload.get("avatar", {}), indent=2))
print("\nTree of Life:")
print(json.dumps(payload.get("tree_of_life", {}), indent=2))
