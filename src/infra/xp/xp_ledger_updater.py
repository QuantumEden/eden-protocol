# xp_ledger_updater.py – Eden Protocol Infra
# Updates XP, level, and symbolic modifiers for a given user payload

from datetime import datetime

def update_xp_state(user_profile: dict, payload: dict, previous_state: dict = None) -> dict:
    """
    Applies XP, soulform, and tree growth logic based on quest results or DAO action.
    """

    level = previous_state.get("level", 1) if previous_state else 1
    xp = previous_state.get("xp", 0) if previous_state else 0
    tree = payload.get("tree_traits", {})
    awarded = payload.get("xp_awarded", 0)

    # XP growth
    new_xp = xp + awarded
    next_level_threshold = 100 + (level * 20)

    leveled_up = False
    while new_xp >= next_level_threshold:
        new_xp -= next_level_threshold
        level += 1
        next_level_threshold = 100 + (level * 20)
        leveled_up = True

    updated_state = {
        "user_id": user_profile.get("user_id", "unknown"),
        "updated_at": datetime.utcnow().isoformat() + "Z",
        "level": level,
        "xp": new_xp,
        "next_level": next_level_threshold,
        "locked": False,
        "quest_unlocked": payload.get("quest_unlocked", False),
        "soulform_modifier": None,
        "leap_event": leveled_up
    }

    # Optional soulform bonus
    soulform = user_profile.get("current_soulform")
    if soulform:
        affinity = soulform.get("elemental_affinity", "").lower()
        bonus = 0

        if affinity == "fire":
            bonus = 5
        elif affinity == "water":
            bonus = 3
        elif affinity == "air":
            bonus = 2
        elif affinity == "earth":
            bonus = 4

        updated_state["xp"] += bonus
        updated_state["soulform_modifier"] = {
            "affinity": affinity,
            "xp_bonus": bonus
        }

    return updated_state


# Example CLI simulation
if __name__ == "__main__":
    user_profile = {
        "user_id": "seer_011",
        "current_soulform": {
            "id": "phoenix",
            "name": "Ashborn Phoenix",
            "elemental_affinity": "Fire",
            "activated_at": "2025-05-14T16:00:00Z"
        }
    }

    previous_state = {
        "level": 6,
        "xp": 90
    }

    eden_payload = {
        "tree_traits": {
            "discipline": 91,
            "resilience": 93,
            "mindfulness": 89,
            "expression": 73,
            "physical_care": 64,
            "emotional_regulation": 88
        },
        "xp_awarded": 25,
        "quest_unlocked": True
    }

    result = update_xp_state(user_profile, eden_payload, previous_state)
    import json
    print(json.dumps(result, indent=2))
