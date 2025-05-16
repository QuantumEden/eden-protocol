# world_tree_sync.py – Eden Protocol Infra
# Aggregates user Tree data into a unified World Tree snapshot

import os
import sys
import json

# Load local simulated data
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'sim')))
from eden_payload_viewer import get_all_mock_payloads  # must return list of payloads

TRAITS = [
    "discipline",
    "resilience",
    "mindfulness",
    "expression",
    "physical_care",
    "emotional_regulation"
]

def average_trait(payloads, trait):
    values = [
        user["tree_traits"][trait]
        for user in payloads
        if trait in user.get("tree_traits", {})
    ]
    return round(sum(values) / len(values)) if values else 0

def generate_world_tree_snapshot(payloads):
    return {
        "world_tree": {
            trait: average_trait(payloads, trait)
            for trait in TRAITS
        },
        "user_count": len(payloads)
    }

if __name__ == "__main__":
    mock_payloads = get_all_mock_payloads()  # List of Eden payloads
    world_tree_state = generate_world_tree_snapshot(mock_payloads)
    print(json.dumps(world_tree_state, indent=2))
