"""
World Exporter – Eden Protocol UE5 Interface

Converts symbolic world data and NPC states into a structured
export format compatible with Unreal Engine 5 procedural instancing.
"""

import json
from typing import Dict, List

def export_to_ue5_format(world: Dict, npcs: List[Dict]) -> Dict:
    """
    Assembles a complete UE5-compatible export structure.
    """
    return {
        "world": {
            "id": world.get("world_id"),
            "name": world.get("name"),
            "terrain": world.get("terrain"),
            "climate": world.get("climate"),
            "tone": world.get("tone"),
            "entry_condition": world.get("entry_condition"),
            "objectives": world.get("objectives"),
            "emblem": world.get("emblem")
        },
        "npcs": [
            {
                "name": npc["name"],
                "role": npc["role"],
                "alignment": npc["alignment"],
                "appearance": npc["appearance"],
                "dialogue": npc.get("dialogue", "...")
            }
            for npc in npcs
        ]
    }

def export_to_json_file(user_id: str, data: Dict, path: str = "./ue5_exports/") -> str:
    """
    Writes the export payload to disk as a .json file.
    """
    import os
    os.makedirs(path, exist_ok=True)
    filename = f"{user_id}_world_export.json"
    filepath = os.path.join(path, filename)

    with open(filepath, "w") as f:
        json.dump(data, f, indent=2)

    return filepath

# Example
if __name__ == "__main__":
    sample_world = {
        "world_id": "realm_phoenix_discipline",
        "name": "Discipline Sanctum",
        "terrain": "forest",
        "climate": "clear",
        "tone": "ascending",
        "emblem": "phoenix",
        "objectives": ["Shadow confrontation", "Symbol retrieval"],
        "entry_condition": {"trait": "discipline", "minimum_value": 40}
    }

    sample_npcs = [
        {
            "name": "The Mirror",
            "role": "Wounded Reflection",
            "dialogue": "Do you see yourself through the eyes of those who harmed you?",
            "alignment": "neutral",
            "appearance": "silver-masked figure"
        }
    ]

    export_payload = export_to_ue5_format(sample_world, sample_npcs)
    path = export_to_json_file("seer_lambda", export_payload)
    print("🗂️ Exported to:", path)
