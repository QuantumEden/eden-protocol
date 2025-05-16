import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

import json
from eden_payload_generator.eden_payload_generator import generate_eden_payload

# === Single Payload Viewer ===

profile = {
    "mbti": "INTJ",
    "iq": 140,
    "eq": 120,
    "moral": "truth",
    "sacred_path": "Hermeticism",
    "group_opt_in": True
}

user_id = "seer_011"
secret_key = "vault_key_456"

payload = generate_eden_payload(user_id, profile, secret_key)

print("\n=== Eden Payload Structure View ===\n")
print(json.dumps(payload, indent=2))


# === Group Payload Export ===

def get_all_mock_payloads():
    """
    Returns a list of payloads for mock users to feed into system-wide modules
    like world_tree_sync.py, DAO merit maps, or UI simulators.
    """
    mock_users = [
        {
            "user_id": "seer_011",
            "profile": {
                "mbti": "INTJ",
                "iq": 140,
                "eq": 120,
                "moral": "truth",
                "sacred_path": "Hermeticism",
                "group_opt_in": True
            },
            "secret_key": "vault_key_456"
        },
        {
            "user_id": "healer_022",
            "profile": {
                "mbti": "INFJ",
                "iq": 132,
                "eq": 128,
                "moral": "care",
                "sacred_path": "Logotherapy",
                "group_opt_in": False
            },
            "secret_key": "echo_bond_022"
        },
        {
            "user_id": "warrior_033",
            "profile": {
                "mbti": "ESTP",
                "iq": 118,
                "eq": 97,
                "moral": "loyalty",
                "sacred_path": "Stoicism",
                "group_opt_in": True
            },
            "secret_key": "rebel_helm_033"
        }
    ]

    payloads = []
    for mock in mock_users:
        payload = generate_eden_payload(
            user_id=mock["user_id"],
            profile=mock["profile"],
            secret_key=mock["secret_key"]
        )
        payloads.append(payload)

    return payloads
