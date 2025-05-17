# edenquest_engine.py – Eden Protocol Quest Generator Core
# Accepts user psychometric data and symbolic imbalance to generate therapeutic AI quests

from typing import Dict, Any
from quest_modifier import apply_quest_modifiers  # Phase 14 modifier overlay

# === Step 1: Sample symbolic quest pool (replaceable by AI generator) ===
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
            "title": "The Stillwater Sanctum",
            "theme": "Inner silence and present awareness",
            "symbol": "A floating lotus amidst shifting waves",
            "goal": "Meditate to dispel illusionary distractions"
        }
    ],
    "expression": [
        {
            "title": "The Echoing Stage",
            "theme": "Truthful communication and emotional release",
            "symbol": "A hall of mirrors that echo unspoken thoughts",
            "goal": "Speak words that collapse false reflections"
        }
    ],
    "physical_care": [
        {
            "title": "The Body Temple Trial",
            "theme": "Health, rest, and physical reverence",
            "symbol": "A shrine built from sinew and bone",
            "goal": "Navigate terrain while honoring bodily signals"
        }
    ],
    "emotional_regulation": [
        {
            "title": "The Flame Cage",
            "theme": "Navigating fear and emotional control",
            "symbol": "A fireproof chamber with shifting walls",
            "goal": "Remain centered while the environment destabilizes"
        }
    ]
}

# === Step 2: Accept symbolic imbalance and generate quest ===
def generate_quest(tree: Dict[str, Dict[str, int]], user_profile: Dict[str, Any] = None) -> Dict[str, Any]:
    weakest = min(tree.items(), key=lambda item: item[1]["score"])[0]
    quest_options = QUEST_LIBRARY.get(weakest, [])

    if not quest_options:
        return {
            "status": "no_quest",
            "reason": f"No quest available for branch: {weakest}"
        }

    base_quest = {
        "title": quest_options[0]["title"],
        "theme": quest_options[0]["theme"],
        "symbol": quest_options[0]["symbol"],
        "goal": quest_options[0]["goal"]
    }

    # Base structure
    result = {
        "status": "quest_assigned",
        "target_branch": weakest,
        "quest": base_quest
    }

    # Step 3: Apply modifiers (archetype, soulform, disclosure)
    if user_profile:
        result["quest"] = apply_quest_modifiers(base_quest, user_profile)

    return result

# === Optional CLI test ===
if __name__ == "__main__":
    sample_tree = {
        "discipline": {"score": 80},
        "empathy": {"score": 45},
        "resilience": {"score": 60},
        "mindfulness": {"score": 72},
        "expression": {"score": 70},
        "physical_care": {"score": 65},
        "emotional_regulation": {"score": 68}
    }

    mock_profile = {
        "archetype": "Healer",
        "sacred_path": "Taoism",
        "group_opt_in": True,
        "disclosure": {
            "diagnosis": ["PTSD"],
            "trauma_tags": ["loss"]
        },
        "current_soulform": {
            "id": "phoenix",
            "name": "Ashborn Phoenix",
            "elemental_affinity": "Fire",
            "activated_at": "2025-05-14T17:00:00Z"
        }
    }

    quest = generate_quest(sample_tree, mock_profile)
    import json
    print(json.dumps(quest, indent=2))
