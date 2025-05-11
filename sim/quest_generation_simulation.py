# /sim/quest_generation_simulation.py

"""
Eden Protocol Quest Simulation — Phase 11 Test Harness

Simulates full AI-driven symbolic quest generation with:
- XP tier input
- Archetype & trait state
- Difficulty curve evaluation
- Quest payload output

Connects:
- quest_generator.py
- quest_difficulty_calculator.py
- schema validation (optional)
"""

from src.ai.quest_generator import generate_symbolic_quest
from src.ai.quest_difficulty_calculator import calculate_resistance_curve
import json


def simulate_user_quest(user_id: str, archetype: str, trait_xp: dict):
    # Choose weakest trait as focus
    weakest_trait = min(trait_xp, key=trait_xp.get)
    total_xp = sum(trait_xp.values())

    print(f"\n📘 Generating quest for: {user_id} ({archetype})")
    print(f"⚔️ Weakest Trait: {weakest_trait} | XP total: {total_xp}")

    resistance_curve = calculate_resistance_curve(trait_xp)
    print("🧠 Resistance Curve:", resistance_curve)

    quest = generate_symbolic_quest(user_id, archetype, weakest_trait, total_xp)
    print("\n🧾 Generated Quest Payload:")
    print(json.dumps(quest, indent=2))


if __name__ == "__main__":
    sample_user = {
        "user_id": "seer123",
        "archetype": "Strategist",
        "trait_xp": {
            "discipline": 120,
            "empathy": 100,
            "resilience": 75,
            "mindfulness": 60,
            "vitality": 20,
            "expression": 30
        }
    }

    simulate_user_quest(
        sample_user["user_id"],
        sample_user["archetype"],
        sample_user["trait_xp"]
    )
