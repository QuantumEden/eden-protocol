# sim/edenquest_simulation.py
# EdenQuest Simulation – Therapeutic Quest Generation Test

import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from edenquest_engine.edenquest_engine import generate_quest  # ✅ Verified import path

print("\n=== EdenQuest Simulation: Adaptive Quest Assignment ===\n")

# Sample user Tree of Life with symbolic score values
user_tree = {
    "discipline": {"score": 88},
    "empathy": {"score": 92},
    "resilience": {"score": 40},  # weakest trait triggers quest generation
    "craft": {"score": 77},
    "mindfulness": {"score": 70},
    "physical_care": {"score": 85},
    "expression": {"score": 90}
}

# Simulate therapeutic quest generation
quest_result = generate_quest(user_tree)

# Display the assigned quest
print("\n=== Assigned Therapeutic Quest ===")
for key, value in quest_result.items():
    print(f"{key}: {value}")
