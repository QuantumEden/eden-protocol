# sim/edenquest_simulation.py
# EdenQuest Simulation – Therapeutic Quest Generation Test

import sys, os
import json
from datetime import datetime

# === Path Patching ===
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from edenquest_engine.edenquest_engine import generate_quest  # ✅ Verified import path

print("\n=== EdenQuest Simulation: Adaptive Quest Assignment ===")
print(f"🕰️ Timestamp: {datetime.utcnow().isoformat()}Z\n")

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

# Identify weakest trait
trigger_trait = min(user_tree.items(), key=lambda item: item[1]["score"])[0]

# Simulate therapeutic quest generation
quest_result = generate_quest(user_tree)

# Display the assigned quest and trigger logic
print(f"🧠 Weakest Trait Identified: {trigger_trait}\n")
print("🎯 Assigned Therapeutic Quest:")
print(json.dumps(quest_result, indent=2))
