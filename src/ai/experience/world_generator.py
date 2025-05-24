"""
World Generator – Eden Protocol Symbolic Experience Engine

Procedurally generates immersive symbolic environments for therapeutic exploration,
based on user profile, trauma archetype, and progression through the World Tree.
"""

from typing import Dict

def generate_world(user_id: str, soulform: str, traits: Dict[str, int]) -> Dict:
    """
    Returns a procedurally-generated symbolic world seed.
    """
    dominant_trait = max(traits, key=traits.get)
    trait_value = traits[dominant_trait]

    world = {
        "world_id": f"realm_{soulform}_{dominant_trait.lower()}",
        "name": f"{dominant_trait.capitalize()} Sanctum",
        "terrain": "mountain" if dominant_trait == "resilience" else "forest",
        "climate": "stormy" if trait_value < 60 else "clear",
        "tone": "reflective" if trait_value < 50 else "ascending",
        "emblem": soulform,
        "objectives": [
            "Symbol retrieval",
            "Shadow confrontation",
            "Totem reconstruction"
        ],
        "entry_condition": {
            "trait": dominant_trait,
            "minimum_value": 40
        }
    }

    return world

# Example
if __name__ == "__main__":
    traits = {"resilience": 72, "discipline": 55, "empathy": 48}
    result = generate_world("seer_tau", "phoenix", traits)
    print("🌍 Generated World:", result)
