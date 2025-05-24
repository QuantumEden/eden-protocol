# DAO Ritual Eligibility Test – Eden Protocol Integration Test
# Simulates DAO entry logic under varying soulform, trait, and ritual thresholds

import sys, os, json
from datetime import datetime
from typing import Dict

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'src')))

from eden_payload_generator.eden_payload_generator import generate_eden_payload

# === Constants for DAO Onboarding
DAO_LEVEL_MIN = 7
DAO_TRAIT_MIN = 50
DAO_REQUIRED_KEYS = ["sacred_path", "mbti", "eq", "iq"]

# === Mock Test Users
mock_users = [
    {
        "user_id": "user_shadow_006",
        "profile": {
            "mbti": "ISTJ",
            "iq": 110,
            "eq": 95,
            "moral": "loyalty",
            "sacred_path": "Discipline",
            "group_opt_in": True
        },
        "expected": False  # Below DAO level threshold
    },
    {
        "user_id": "user_trial_007",
        "profile": {
            "mbti": "ENFJ",
            "iq": 125,
            "eq": 120,
            "moral": "care",
            "sacred_path": "Compassion",
            "group_opt_in": True
        },
        "expected": True  # Valid merit and traits
    },
    {
        "user_id": "user_decay_008",
        "profile": {
            "mbti": "INTP",
            "iq": 130,
            "eq": 110,
            "moral": "truth",
            "sacred_path": "Inquiry",
            "group_opt_in": False,
            "disclosure": {
                "diagnosis": ["depression"],
                "trauma_tags": ["isolation"],
                "service_connected": False
            }
        },
        "expected": False  # Fails trait balance / tree integrity
    }
]

# === Begin DAO Entry Simulation
print("\n🔍 DAO Ritual Eligibility Test\n")

for mock in mock_users:
    result = generate_eden_payload(
        user_id=mock["user_id"],
        user_profile=mock["profile"],
        secret_key="test_key_xyz"
    )

    print(f"\n🧪 {mock['user_id']} Payload:")
    print(json.dumps(result, indent=2))

    eligibility = result.get("eligible_for_dao", False)
    assert eligibility == mock["expected"], f"❌ Eligibility mismatch for {mock['user_id']}"

    print(f"✅ Eligibility Check Passed – Expected: {mock['expected']}, Got: {eligibility}")

print("\n🎯 All DAO eligibility simulations complete.\n")
