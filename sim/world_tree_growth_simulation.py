# /sim/world_tree_growth_simulation.py

"""
World Tree Growth Simulation

This file models how collective user behavior impacts Eden’s symbolic global
nervous system — the World Tree. Based on XP gains, biometric discipline,
quest alignment, and truth integrity.
"""

import random

def simulate_world_tree_state(users):
    total_xp = sum([u["xp"] for u in users])
    avg_integrity = sum([u["truth_integrity"] for u in users]) / len(users)
    avg_shadow_quests = sum([u["shadow_completed"] for u in users]) / len(users)

    # Eden Vitality Index formula (symbolic weighting)
    vitality = 0.5 * (total_xp / (len(users) * 1000))  # XP normalized
    vitality += 0.3 * (avg_integrity / 100)
    vitality += 0.2 * (avg_shadow_quests / 3)  # Max 3/month
    vitality = round(min(vitality * 100, 100), 2)

    # Determine world state
    if vitality >= 85:
        state = "Radiant (Global Quests Unlocked)"
    elif vitality >= 60:
        state = "Stable (Eden Sustained)"
    elif vitality >= 40:
        state = "Waning (Shadow Quests Intensify)"
    else:
        state = "Withering (Decay Protocol Activated)"

    return {
        "eden_vitality_index": vitality,
        "world_state": state
    }

if __name__ == "__main__":
    # Simulated mock data (10 users)
    users = []
    for _ in range(10):
        users.append({
            "xp": random.randint(200, 1500),
            "truth_integrity": random.randint(50, 100),
            "shadow_completed": random.randint(0, 3)
        })

    result = simulate_world_tree_state(users)
    print("\n[WORLD TREE SIMULATION RESULT]")
    print(f"Eden Vitality Index: {result['eden_vitality_index']}%")
    print(f"Status: {result['world_state']}")
