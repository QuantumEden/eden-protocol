# EdenQuest Simulation – Therapeutic Quest Generation Test

from src.edenquest_engine.edenquest_engine import generate_quest

print("\n=== EdenQuest Simulation: Adaptive Quest Assignment ===\n")

# Sample user Tree of Life
user_tree = {
    "discipline": {"score": 88},
    "empathy": {"score": 92},
    "resilience": {"score": 40},  # weakest trait
    "craft": {"score": 77},
    "mindfulness": {"score": 70},
    "physical_care": {"score": 85},
    "expression": {"score": 90}
}

# Generate the quest
quest_result = generate_quest(user_tree)

# Output the result
print("=== Assigned Therapeutic Quest ===")
for key, value in quest_result.items():
    print(f"{key}: {value}")
