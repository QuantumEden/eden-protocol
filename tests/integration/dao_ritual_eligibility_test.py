# tests/integration/dao_ritual_eligibility_test.py
# DAO Ritual Eligibility Test – Eden Protocol Integration Test
# Simulates DAO entry logic under varying soulform, trait, and ritual thresholds

import sys, os, json
from datetime import datetime
from typing import List, Dict

# === Import patch for src
base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.insert(0, os.path.join(base_path, 'src'))

from eden_payload_generator.eden_payload_generator import generate_eden_payload

# === Constants for DAO Onboarding
DAO_LEVEL_MIN = 7
DAO_TRAIT_MIN = 50
DAO_REQUIRED_KEYS = ["sacred_path", "mbti", "eq", "iq"]

# === Mock Test Users
mock_users: List[Dict] = [
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
        "expected": False
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
        "expected": True
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
        "expected": False
    }
]

def test_dao_eligibility():
    """
    Validates that all mock users match expected DAO eligibility outcomes.
    """
    for mock in mock_users:
        user_id = mock["user_id"]
        profile = mock["profile"]
        expected = mock["expected"]

        result = generate_eden_payload(user_id, profile, secret_key="test_key_xyz")
        eligibility = result.get("eligible_for_dao", False)

        assert eligibility == expected, (
            f"❌ Eligibility mismatch for {user_id}\n"
            f"Expected: {expected}, Got: {eligibility}\n"
        )

        print(f"✅ {user_id}: Eligibility Passed – Expected: {expected}, Got: {eligibility}")

if __name__ == "__main__":
    print("\n🔍 DAO Ritual Eligibility Test –", datetime.utcnow().isoformat(), "UTC\n")
    test_dao_eligibility()
    print("\n🎯 All DAO eligibility simulations completed successfully.\n")
