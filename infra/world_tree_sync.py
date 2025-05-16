# world_tree_sync.py – Eden Protocol Infra
# Aggregates all user Tree trait data into a symbolic World Tree snapshot

import os
import sys
import json

# Import mock payloads from simulation layer
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'sim')))
from eden_payload_viewer import get_all_mock_payloads

# Core trait categories reflected in the Tree of Life
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
    """
    Produces the symbolic World Tree health state
    based on user Tree trait averages.
    """
    return {
        "world_tree": {
            trait: average_trait(payloads, trait)
            for trait in TRAITS
        },
        "user_count": len(payloads)
    }

def export_snapshot_to_file(snapshot, filename="world_tree_snapshot.json"):
    """
    Saves the snapshot locally for UI testing or system sync.
    """
    path = os.path.join(os.path.dirname(__file__), filename)
    with open(path, "w") as f:
        json.dump(snapshot, f, indent=2)

if __name__ == "__main__":
    mock_payloads = get_all_mock_payloads()
    world_tree_state = generate_world_tree_snapshot(mock_payloads)

    print("\n=== World Tree Snapshot ===\n")
    print(json.dumps(world_tree_state, indent=2))

    # Optional: export for frontend development
    export_snapshot_to_file(world_tree_state)
