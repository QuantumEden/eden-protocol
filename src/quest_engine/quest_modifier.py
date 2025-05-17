# quest_modifier.py – Eden Protocol Quest Customizer
# Applies soulform, archetype, and disclosure modifiers to generated quests

from typing import Dict, Any

def apply_quest_modifiers(quest: Dict[str, Any], user_profile: Dict[str, Any]) -> Dict[str, Any]:
    """
    Modifies the base quest object based on user's soulform, archetype, or sacred path.
    """
    soulform = user_profile.get("current_soulform", {})
    archetype = user_profile.get("archetype", "Strategist")
    path = user_profile.get("sacred_path", "None")

    # Soulform animation override
    if soulform:
        quest["aura_overlay"] = {
            "element": soulform.get("elemental_affinity", "None"),
            "effect": "flare_burst" if soulform.get("elemental_affinity") == "Fire" else "ethereal_wind"
        }
        quest["soulform_influence"] = f"Trial of {soulform.get('name', 'Unknown Form')}"

    # Archetype thematic overlay
    quest["archetype_influence"] = f"Path of the {archetype}"

    # Sacred path lore expansion
    if path != "None":
        quest["narrative_lens"] = f"Framed through {path}"

    return quest

# Optional CLI test
if __name__ == "__main__":
    mock_quest = {
        "title": "The Ashen Spire",
        "theme": "Pain endurance and symbolic rebirth",
        "goal": "Climb while weathering storms of memory"
    }

    mock_user = {
        "archetype": "Healer",
        "sacred_path": "Taoism",
        "current_soulform": {
            "id": "phoenix",
            "name": "Ashborn Phoenix",
            "elemental_affinity": "Fire"
        }
    }

    modified = apply_quest_modifiers(mock_quest, mock_user)
    import json
    print(json.dumps(modified, indent=2))
