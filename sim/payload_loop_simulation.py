import json
from eden_payload_generator.eden_payload_generator import generate_eden_payload

# Looping simulation for iterative payload validation
user_id = "observer_loop"
secret_key = "key_loop_test"

profiles = [
    {
        "mbti": "ISTJ",
        "iq": 120,
        "eq": 110,
        "moral": "authority",
        "sacred_path": "Judaism",
        "group_opt_in": False
    },
    {
        "mbti": "ENFP",
        "iq": 128,
        "eq": 133,
        "moral": "care",
        "sacred_path": "Hinduism",
        "group_opt_in": True
    },
    {
        "mbti": "INTP",
        "iq": 145,
        "eq": 102,
        "moral": "liberty",
        "sacred_path": "Gnosticism",
        "group_opt_in": False
    }
]

print("\n=== Eden Payload Loop Simulation ===\n")

for i, profile in enumerate(profiles):
    print(f"--- Payload {i+1} ({profile['mbti']}) ---")
    payload = generate_eden_payload(user_id, profile, secret_key)
    print(json.dumps(payload, indent=2))
    print("\n")
