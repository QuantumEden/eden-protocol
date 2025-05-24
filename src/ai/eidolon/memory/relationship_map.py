"""
Relationship Map – Eidolon Symbolic NPC Memory Tracker

Stores relational dynamics with key symbolic entities (NPCs, avatars, voices).
Supports quest generation, dream recall, and psycho-spiritual continuity.
"""

from datetime import datetime
from typing import Dict, List

# NPC memory store
RELATIONSHIP_DB: Dict[str, List[Dict]] = {}

def remember_npc(user_id: str, npc_name: str, role: str, significance: str, traits: List[str]) -> Dict:
    """
    Logs or updates memory of a symbolic relationship (ally, guide, nemesis, etc.).
    """
    entry = {
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "npc_name": npc_name,
        "role": role,
        "significance": significance,
        "traits": traits
    }

    RELATIONSHIP_DB.setdefault(user_id, []).append(entry)
    return entry

def get_relationships(user_id: str) -> List[Dict]:
    """
    Retrieves all remembered NPCs for the user.
    """
    return RELATIONSHIP_DB.get(user_id, [])

def get_by_role(user_id: str, role: str) -> List[Dict]:
    """
    Filters remembered NPCs by symbolic role.
    """
    return [
        npc for npc in RELATIONSHIP_DB.get(user_id, [])
        if npc.get("role") == role
    ]

# Example
if __name__ == "__main__":
    remember_npc(
        user_id="dreamer_004",
        npc_name="Vesper",
        role="mentor",
        significance="Guided the user through the Ritual of Silence",
        traits=["wise", "stern", "mysterious"]
    )

    print("👤 NPCs:", get_relationships("dreamer_004"))
    print("🎓 Mentors:", get_by_role("dreamer_004", "mentor"))
