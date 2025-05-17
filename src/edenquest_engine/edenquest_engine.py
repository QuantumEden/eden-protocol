# EdenQuest Engine
# Accepts user psychometric data and symbolic imbalance to generate therapeutic AI quests

from typing import Dict, Any

# Step 1: Symbolic quest pool (to be expanded or generated dynamically in future AI layer)
QUEST_LIBRARY = {
    "discipline": [
        {
            "title": "The Clockwork Labyrinth",
            "theme": "Time, routine, and self-control",
            "symbol": "A broken gear in a suspended pendulum tower",
            "goal": "Escape the maze by repeating precise timed movements"
        }
    ],
    "empathy": [
        {
            "title": "The Mirror Garden",
            "theme": "Emotional connection and vulnerability",
            "symbol": "An NPC who reflects your mood",
            "goal": "Revive withered blossoms by emotional attunement"
        }
    ],
    "resilience": [
        {
            "title": "The Ashen Spire",
            "theme": "Pain endurance and symbolic rebirth",
            "symbol": "A tower rising from a volcanic crater",
            "goal": "Climb while weathering storms of memory"
        }
    ],
    "mindfulness": [
        {
            "title": "The Silent Chamber",
            "theme": "Inner stillness and awareness",
            "symbol": "A glowing lotus in a soundless room",
            "goal": "Solve a puzzle that reacts only to breath and gaze"
        }
    ],
    "expression": [
        {
            "title": "The Echoing Hall",
            "theme": "Truth, vulnerability, and vocal integrity",
            "symbol": "A masked choir that sings your secrets",
            "goal": "Find the harmony that unlocks your own voice"
        }
    ],
    "physical_care": [
        {
            "title": "The Fractured Vessel",
            "theme": "Restoration of the body through ritual",
            "symbol": "A cracked urn that leaks light",
            "goal": "Restore the urn through movements and stillness"
        }
    ],
    "craft": [
        {
            "title": "The Forge of Forms",
            "theme": "Creation, repetition, and mastery",
            "symbol": "A shapeshifting anvil",
            "goal": "Forge a symbolic artifact from memory shards"
        }
    ]
}

# Step 2: Accept symbolic imbalance and generate quest output
def generate_quest(tree: Dict[str, Dict[str, int]]) -> Dict[str, Any]:
    # Determine the weakest branch
    weakest = min(tree.items(), key=lambda item: item[1]["score"])[0]
    quest_options = QUEST_LIBRARY.get(weakest, [])

    if not quest_options:
        return {
            "status": "no_quest",
            "reason": f"No symbolic quest available for branch: {weakest}"
        }

    quest = quest_options[0]  # Placeholder: will be randomized or AI-driven later
    return {
        "status": "quest_assigned",
        "target_branch": weakest,
        "quest": quest
    }

# Optional standalone test
if __name__ == "__main__":
    sample_tree = {
        "discipline": {"score": 80},
        "empathy": {"score": 45},
        "resilience": {"score": 60},
        "craft": {"score": 70},
        "mindfulness": {"score": 75},
        "physical_care": {"score": 68},
        "expression": {"score": 73}
    }

    quest = generate_quest(sample_tree)
    print("\n=== EdenQuest Assignment ===")
    for k, v in quest.items():
        print(f"{k}: {v}")
