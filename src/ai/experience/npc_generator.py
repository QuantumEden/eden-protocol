"""
NPC Generator – Eden Protocol Symbolic Experience Engine

Creates symbolic non-player characters (NPCs) based on user archetypes,
emotional state, and recent session insights. Used for quest guidance,
mirror interactions, and therapeutic storytelling.
"""

from typing import Dict, List

def generate_npcs(user_id: str, archetype: str, mood: str) -> List[Dict]:
    """
    Generates a list of symbolic NPCs tied to the user's emotional tone and role.
    """
    npc_list = []

    if mood == "shame":
        npc_list.append({
            "name": "The Mirror",
            "role": "Wounded Reflection",
            "dialogue": "Do you see yourself through the eyes of those who harmed you?",
            "alignment": "neutral",
            "appearance": "silver-masked figure, radiating silence"
        })

    if archetype.lower() in ["healer", "sage"]:
        npc_list.append({
            "name": "Aurelia",
            "role": "Guiding Light",
            "dialogue": "Even broken wings remember how to fly.",
            "alignment": "mentor",
            "appearance": "robed figure surrounded by bioluminescent moths"
        })

    npc_list.append({
        "name": "The Shadowling",
        "role": "Echo of Doubt",
        "dialogue": "What will you become when no one is watching?",
        "alignment": "challenger",
        "appearance": "shifting silhouette with a cracked voice"
    })

    return npc_list

# Example
if __name__ == "__main__":
    print("🎭 NPCs:", generate_npcs("oracle_777", "Healer", "shame"))
