# /src/ai/quest_generator.py

"""
Therapeutic Quest Generator — Eden Protocol (Phase 11)

Simulates symbolic quest creation based on:
- User's avatar archetype
- Trait needing reinforcement
- Current XP tier and emotional difficulty
- Logotherapy and shadow work themes

In production, this module will be powered by fine-tuned LLMs.
"""

import uuid
import random
from datetime import datetime

# Core symbolic pool (normally this would be model-driven)
ENVIRONMENTS = {
    "discipline": ["Ash Temple", "Obsidian Cliff", "Halls of Judgment"],
    "empathy": ["Sanctuary of Echoes", "Weeping Meadow", "Chamber of Mirrors"],
    "resilience": ["Storm Vault", "Trial Wastes", "Scorched Arena"],
    "mindfulness": ["Stillwater Grove", "Garden of Breath", "Silent Spire"],
    "vitality": ["Crimson Grove", "Sunforge Basin", "Verdant Temple"],
    "expression": ["The Theater of Truth", "Gallery of Flame", "Voicewell"]
}

SYMBOLS = {
    "Builder": "🜂",
    "Guardian": "🜃",
    "Healer": "🜄",
    "Strategist": "🜁"
}

DIFFICULTY_TIERS = ["low", "moderate", "high", "mythic"]


def generate_symbolic_quest(user_id: str, archetype: str, trait: str, xp_total: int) -> dict:
    quest_id = str(uuid.uuid4())
    difficulty = DIFFICULTY_TIERS[min(xp_total // 300, 3)]  # 0-299: low, 300-599: moderate, etc.

    title = f"Trial of the {trait.capitalize()} Flame"
    environment = random.choice(ENVIRONMENTS.get(trait, ["Unknown Realm"]))
    symbol = SYMBOLS.get(archetype, "✶")
    xp_reward = random.randint(40, 90)
    theme = random.choice([
        "Face the buried self", "Transmute pain into meaning",
        "Break the illusion of control", "Witness the inner child"
    ])

    steps = [
        {"instruction": "Recite your core wound as a mantra.", "type": "ritual", "symbol": symbol},
        {"instruction": "Solve a symbolic puzzle related to your past.", "type": "puzzle", "symbol": symbol},
        {"instruction": "Reflect on a time you broke under pressure.", "type": "reflection", "symbol": symbol}
    ]

    return {
        "quest_id": quest_id,
        "title": title,
        "user_id": user_id,
        "archetype": archetype,
        "trait_focus": trait,
        "difficulty": difficulty,
        "environment": environment,
        "steps": steps,
        "xp_reward": xp_reward,
        "symbolic_theme": theme,
        "timestamp": datetime.utcnow().isoformat()
    }


# Example
if __name__ == "__main__":
    quest = generate_symbolic_quest("user_x42", "Healer", "resilience", 540)
    from pprint import pprint
    pprint(quest)
