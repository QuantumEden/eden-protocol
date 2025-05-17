# xp_ledger_simulation.py – Eden Protocol Simulation
# Tests XP growth logic with soulform modifiers and symbolic quest states

import sys
import os
import json
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from infra.xp.xp_ledger_updater import update_xp_state

# Simulated EdenQuest payloads
mock_payloads = [
    {
        "user_id": "seer_011",
        "profile": {
            "user_id": "seer_011",
            "current_soulform": {
                "id": "phoenix",
                "name": "Ashborn Phoenix",
                "elemental_affinity": "Fire",
                "activated_at": "2025-05-14T16:00:00Z"
            }
        },
        "previous_state": {
            "level": 6,
            "xp": 90
        },
        "payload": {
            "tree_traits": {
                "discipline": 91,
                "resilience": 93,
                "mindfulness": 89,
                "expression": 73,
                "physical_care": 64,
                "emotional_regulation": 88
            },
            "xp_awarded": 25,
            "quest_unlocked": True
        }
    },
    {
        "user_id": "guardian_002",
        "profile": {
            "user_id": "guardian_002"
            # No soulform attached
        },
        "previous_state": {
            "level": 3,
            "xp": 45
        },
        "payload": {
            "tree_traits": {
                "discipline": 52,
                "resilience": 59,
                "mindfulness": 60,
                "expression": 50,
                "physical_care": 58,
                "emotional_regulation": 61
            },
            "xp_awarded": 40,
            "quest_unlocked": True
        }
    }
]

if __name__ == "__main__":
    print("=== XP Ledger Simulation – Eden Protocol ===\n")
    for mock in mock_payloads:
        result = update_xp_state(
            user_profile=mock["profile"],
            payload=mock["payload"],
            previous_state=mock["previous_state"]
        )

        print(f"User: {mock['user_id']}")
        print(json.dumps(result, indent=2))
        print("-" * 50)
