import json
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from src.eden_payload_generator.eden_payload_generator import generate_eden_payload

# Input a simplified viewer profile
test_profile = {
    "mbti": "ENTP",
    "iq": 128,
    "eq": 114,
    "moral": "liberty",
    "sacred_path": "Stoicism",
    "group_opt_in": True
}

user_id = "viewer_test_001"
secret_key = "secret_token_xyz"

payload = generate_eden_payload(user_id, test_profile, secret_key)

# Print out only the avatar and tree for UI viewer testing
print("\n=== Eden Viewer Output ===\n")
print("Avatar Block:")
print(json.dumps(payload.get("avatar", {}), indent=2))
print("\nTree of Life Block:")
print(json.dumps(payload.get("tree_of_life", {}), indent=2))
