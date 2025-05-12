import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

import json
from src.eden_payload_generator.eden_payload_generator import generate_eden_payload

# Simulated loop of sample user profiles
sample_profiles = [
    {
        "mbti": "INFJ",
        "iq": 135,
        "eq": 122,
        "moral": "care",
        "sacred_path": "Zen Buddhism",
        "group_opt_in": True
    },
    {
        "mbti": "INTP",
        "iq": 128,
        "eq": 110,
        "moral": "liberty",
        "sacred_path": "Custom Mythos",
        "group_opt_in": False
    }
]

user_id = "test_user_loop"
secret_key = "loop_key_xyz"

print("\n=== Eden Payload Loop Simulation ===\n")
for i, profile in enumerate(sample_profiles):
    print(f"--- Profile {i+1}: {profile['mbti']} ---")
    payload = generate_eden_payload(user_id, profile, secret_key)
    print(json.dumps(payload, indent=2))
    print("\n")
