# /src/utils/biometric_integration.py

"""
Biometric Integration Module for Eden Protocol

This module simulates how smartwatch and smart ring data (e.g., Oura, Apple Health,
Fitbit, Google Fit) is translated into symbolic updates to the Tree of Life system.

Real-world inputs like sleep, HRV, activity, and mindfulness influence core traits:
- Discipline
- Resilience
- Mindfulness
- Vitality
- Emotional Regulation

This data is processed and mapped to Tree of Life branches.
"""

def normalize(value, max_value=100):
    return min(max(value, 0), max_value)

# Sleep score → Discipline
def update_discipline_from_sleep(tree, sleep_score):
    updated = normalize(sleep_score)
    tree['discipline'] = updated
    return tree

# HRV → Resilience
def update_resilience_from_hrv(tree, hrv_value):
    scaled = normalize(hrv_value / 2)  # Example: 60ms → 30/100 scale
    tree['resilience'] = scaled
    return tree

# Meditation / mindfulness minutes → Mindfulness
def update_mindfulness_from_minutes(tree, minutes_today):
    boost = min(minutes_today, 30) * 3  # Up to 90% bonus
    tree['mindfulness'] = normalize(boost)
    return tree

# Physical activity → Vitality
def update_vitality_from_steps(tree, steps):
    base = min(steps, 10000) / 10000 * 100
    tree['vitality'] = normalize(base)
    return tree

# Respiratory trends → Emotional Regulation
def update_emotional_regulation(tree, breath_rate_trend):
    if breath_rate_trend == "stable":
        score = 80
    elif breath_rate_trend == "high":
        score = 55
    else:
        score = 40
    tree['emotional_regulation'] = normalize(score)
    return tree

# Readiness index (e.g., Oura recovery score) → holistic rebalance
def rebalance_tree_based_on_fatigue(tree, readiness_index):
    penalty = (100 - readiness_index) * 0.2
    for trait in tree:
        if trait != "health_score":
            tree[trait] = normalize(tree[trait] - penalty)
    return tree

# Example tree structure
def simulate():
    tree = {
        "discipline": 72,
        "resilience": 65,
        "mindfulness": 40,
        "vitality": 80,
        "emotional_regulation": 59,
        "health_score": 0
    }

    tree = update_discipline_from_sleep(tree, sleep_score=58)
    tree = update_resilience_from_hrv(tree, hrv_value=70)
    tree = update_mindfulness_from_minutes(tree, minutes_today=12)
    tree = update_vitality_from_steps(tree, steps=8400)
    tree = update_emotional_regulation(tree, breath_rate_trend="stable")
    tree = rebalance_tree_based_on_fatigue(tree, readiness_index=63)

    # Update health score (mean of all traits)
    traits = [v for k, v in tree.items() if k != 'health_score']
    tree['health_score'] = round(sum(traits) / len(traits), 2)

    print("\n[Biometric Integration Simulation]")
    for k, v in tree.items():
        print(f"{k.title()}: {v}")

if __name__ == "__main__":
    simulate()
