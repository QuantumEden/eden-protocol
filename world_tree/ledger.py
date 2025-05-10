# /world_tree/ledger.py

import json
import os

# Simulated world state tracking for collective Eden vitality
user_snapshots = {}

# Register or update a user's symbolic wellness profile
def update_user_state(user_id: str, tree_of_life: dict):
    user_snapshots[user_id] = tree_of_life

# Compute collective Eden vitality index (0–100 scale)
def compute_eden_vitality() -> float:
    if not user_snapshots:
        return 0.0
    total_score = 0
    for tree in user_snapshots.values():
        total_score += tree.get("health_score", 0)
    avg_score = total_score / len(user_snapshots)
    return round(avg_score, 2)

# Export global state snapshot
def export_world_state(filepath="data/world_tree_state.json"):
    state = {
        "user_count": len(user_snapshots),
        "eden_vitality_index": compute_eden_vitality(),
        "status": interpret_status(compute_eden_vitality()),
        "snapshot": user_snapshots
    }
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, "w") as f:
        json.dump(state, f, indent=2)

# Determine Eden's symbolic health status
def interpret_status(score: float) -> str:
    if score >= 85:
        return "Transcendent Growth"
    elif score >= 70:
        return "Stable (Eden is Sustained)"
    elif score >= 50:
        return "Flickering (Integrity Waning)"
    else:
        return "Critical Collapse"

# Example usage
def simulate():
    update_user_state("user001", {"health_score": 74.2})
    update_user_state("user002", {"health_score": 62.7})
    update_user_state("user003", {"health_score": 85.4})
    export_world_state()
    print("Eden Vitality:", compute_eden_vitality())

if __name__ == "__main__":
    simulate()
