import json
from src.avatar_identity_engine.identity_engine import generate_avatar

# Simulated user profiles for testing
sample_profiles = [
    {
        "mbti": "ISTP",
        "iq": 132,
        "eq": 95,
        "moral": "loyalty"
    },
    {
        "mbti": "ENFP",
        "iq": 110,
        "eq": 125,
        "moral": "care"
    },
    {
        "mbti": "INTJ",
        "iq": 142,
        "eq": 108,
        "moral": "fairness"
    },
    {
        "mbti": "ISFJ",
        "iq": 100,
        "eq": 115,
        "moral": "authority"
    },
    {
        "mbti": "ENTP",
        "iq": 120,
        "eq": 100,
        "moral": "liberty"
    }
]

# Execute simulation
print("\n=== Avatar Identity Engine Simulation ===\n")
for i, profile in enumerate(sample_profiles):
    print(f"--- Profile {i+1}: {profile['mbti']} ---")
    avatar = generate_avatar(profile)
    print(json.dumps(avatar, indent=2))
    print("\n")
