import json
from eden_payload_generator.eden_payload_generator import generate_eden_payload

# Sample user profiles for full pipeline loop test
sample_profiles = [
    {
        "mbti": "ISTP",
        "iq": 132,
        "eq": 95,
        "moral": "loyalty",
        "sacred_path": "Zen Buddhism",
        "group_opt_in": True
    },
    {
        "mbti": "ENFP",
        "iq": 110,
        "eq": 125,
        "moral": "care",
        "sacred_path": "Mystic Humanism",
        "group_opt_in": False
    },
    {
        "mbti": "INTJ",
        "iq": 142,
        "eq": 108,
        "moral": "fairness",
        "sacred_path": "Hermeticism",
        "group_opt_in": True
    },
    {
        "mbti": "ISFJ",
        "iq": 100,
        "eq": 115,
        "moral": "authority",
        "sacred_path": "Orthodox Christianity",
        "group_opt_in": False
    },
    {
        "mbti": "ENTP",
        "iq": 120,
        "eq": 100,
        "moral": "liberty",
        "sacred_path": "Chaos Gnosticism",
        "group_opt_in": True
    }
]

print("\n=== Eden Protocol Payload Loop ===\n")
for i, profile in enumerate(sample_profiles):
    user_id = f"test_user_{i+1:03}"
    secret_key = "loop_test_key"
    payload = generate_eden_payload(user_id, profile, secret_key)
    print(f"\n--- Payload for {user_id} ({profile['mbti']}) ---")
    print(json.dumps(payload, indent=2))
