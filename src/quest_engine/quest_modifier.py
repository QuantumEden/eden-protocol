# src/quest_engine/quest_modifier.py – Eden Protocol Quest Customizer
# Applies soulform, archetype, and disclosure modifiers to generated quests

from typing import Dict, Any
import copy

def apply_quest_modifiers(quest: Dict[str, Any], user_profile: Dict[str, Any]) -> Dict[str, Any]:
    """
    Modifies a symbolic quest using user metadata:
    - Soulform (elemental overlay)
    - Archetype (growth path influence)
    - Sacred Path (narrative lens)
    - Disclosure (trauma shadow tagging)
    - Group resonance flag

    Returns a modified quest dictionary.
    """
    # Work from a copy to avoid mutation
    modified_quest = copy.deepcopy(quest)

    soulform = user_profile.get("current_soulform", {})
    archetype = user_profile.get("archetype", "Strategist")
    path = user_profile.get("sacred_path", "None")
    group_opt_in = user_profile.get("group_opt_in", False)
    disclosure = user_profile.get("disclosure", {})

    # === Soulform Overlay ===
    if soulform:
        element = soulform.get("elemental_affinity", "None")
        modified_quest["aura_overlay"] = {
            "element": element,
            "effect": "flare_burst" if element == "Fire" else "ethereal_wind"
        }
        modified_quest["soulform_trial"] = f"Trial of the {soulform.get('name', 'Unseen Form')}"

    # === Archetype Thematic Influence ===
    modified_quest["archetype_influence"] = f"Path of the {archetype}"

    # === Sacred Path Narrative Lens ===
    if path != "None":
        modified_quest["narrative_lens"] = f"Framed through the lens of {path.lower()}"

    # === Group Resonance Activation ===
    if group_opt_in:
        modified_quest["resonance"] = "Collective Aura Active"

    # === Disclosure Weight & Symbolic Tags ===
    if disclosure.get("diagnosis") or disclosure.get("trauma_tags"):
        modified_quest["shadow_weight"] = "High"
        modified_quest["disclosure_gate"] = True
        modified_quest["symbolic_tags"] = list(set(disclosure.get("trauma_tags", []) + disclosure.get("diagnosis", [])))
    else:
        modified_quest["shadow_weight"] = "Low"
        modified_quest["disclosure_gate"] = False
        modified_quest["symbolic_tags"] = []

    return modified_quest

# === CLI Diagnostic Test ===
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
