# quest_modifier.py – Eden Protocol Quest Customizer
# Applies soulform, archetype, and disclosure modifiers to generated quests

from typing import Dict, Any

def apply_quest_modifiers(quest: Dict[str, Any], user_profile: Dict[str, Any]) -> Dict[str, Any]:
    """
    Modifies the base quest object based on user's soulform, archetype, sacred path,
    and symbolic indicators of trauma disclosure or group alignment.
    """
    soulform = user_profile.get("current_soulform", {})
    archetype = user_profile.get("archetype", "Strategist")
    path = user_profile.get("sacred_path", "None")
    group_opt_in = user_profile.get("group_opt_in", False)
    disclosure = user_profile.get("disclosure", {})

    # Soulform animation and theme modifier
    if soulform:
        quest["aura_overlay"] = {
            "element": soulform.get("elemental_affinity", "None"),
            "effect": "flare_burst" if soulform.get("elemental_affinity") == "Fire" else "ethereal_wind"
        }
        quest["soulform_trial"] = f"Trial of the {soulform.get('name', 'Unseen Form')}"

    # Archetype thematic overlay
    quest["archetype_influence"] = f"Path of the {archetype}"

    # Sacred path lore alignment
    if path != "None":
        quest["narrative_lens"] = f"Framed through the lens of {path}"

    # Group resonance bonus
    if group_opt_in:
        quest["resonance"] = "Collective Aura Active"

    # Disclosure presence (symbolic quest weight)
    if disclosure.get("diagnosis") or disclosure.get("trauma_tags"):
        quest["shadow_weight"] = "High"
        quest["disclosure_gate"] = True
    else:
        quest["shadow_weight"] = "Low"
        quest["disclosure_gate"] = False

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
        "group_opt_in": True,
        "disclosure": {
            "diagnosis": ["PTSD"],
            "trauma_tags": ["combat"]
        },
        "current_soulform": {
            "id": "phoenix",
            "name": "Ashborn Phoenix",
            "elemental_affinity": "Fire"
        }
    }

    modified = apply_quest_modifiers(mock_quest, mock_user)
    import json
    print(json.dumps(modified, indent=2))
