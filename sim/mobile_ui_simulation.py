# /sim/mobile_ui_simulation.py

"""
This simulation emulates a mobile user’s progression through EdenQuest.
Useful for demonstrating state transitions, aura evolution, quest flow,
and DAO participation as visualized on the mobile app.
"""

from random import randint, choice
import json
from datetime import datetime

def generate_timestamp():
    return datetime.utcnow().isoformat() + "Z"

# Mock state
def generate_user_state():
    tree = {
        "discipline": randint(40, 80),
        "resilience": randint(30, 85),
        "mindfulness": randint(25, 90),
        "vitality": randint(50, 100),
        "emotional_regulation": randint(20, 90),
        "health_score": 0
    }
    tree["health_score"] = round(sum(tree.values()) / len(tree), 2)

    quest = {
        "title": choice(["Labyrinth of Doubt", "Sanctum of Stillness", "Tower of Judgment"]),
        "theme": choice(["Shadow", "Forgiveness", "Clarity"]),
        "symbol": choice(["🜁", "🜃", "🜂", "🜄"]),
        "goal": "Confront your reflection and name its fear.",
        "status": choice(["unlocked", "in_progress", "completed"]),
        "assigned_at": generate_timestamp()
    }

    dao = {
        "title": "Open Sanctuary Access for Trauma Survivors",
        "votes_for": randint(200, 800),
        "votes_against": randint(0, 300),
        "outcome": choice(["passed", "failed", "tie"]),
        "voted": choice([True, False])
    }

    meritcoin = {
        "level": randint(1, 25),
        "xp": randint(0, 1000),
        "next_level": 1000,
        "locked": tree["emotional_regulation"] < 40,
        "last_xp_gain": generate_timestamp()
    }

    return {
        "session_id": f"mobile_ui_{randint(1000,9999)}",
        "timestamp": generate_timestamp(),
        "avatar": {
            "mbti": "INFJ",
            "archetype": "Healer",
            "element": "Water",
            "primary_aura": "Blue",
            "secondary_aura": "Indigo",
            "eyes": "Fractal",
            "glyphs": ["☯", "🜄", "💧"]
        },
        "tree_of_life": tree,
        "edenquest": {
            "target_branch": "mindfulness",
            "quest": quest,
            "narrative_stage": choice(["Awakening", "Trial", "Revelation", "Transcendence"])
        },
        "meritcoin": meritcoin,
        "dao": dao,
        "world_tree": {
            "eden_vitality_index": round(randint(6800, 7400) / 100.0, 2),
            "user_count": randint(200, 300),
            "status": "Stable (Eden is Sustained)"
        }
    }

if __name__ == "__main__":
    user_payload = generate_user_state()
    print("\n[EDEN MOBILE UI SIMULATION]\n")
    print(json.dumps(user_payload, indent=2))
