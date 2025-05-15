# Token Router Stub – Simulated Soulform Payload Injector
# Phase 14 – Eden Protocol

import json
from typing import Dict

def inject_soulform_payload(payload: Dict[str, any], user_profile: Dict[str, any]) -> Dict[str, any]:
    """
    Appends soulform visuals to outbound payload if current_soulform is present in the user profile.
    """
    soulform = user_profile.get("current_soulform", None)
    if not soulform:
        return payload  # No transformation active

    payload["soulform_visuals"] = {
        "id": soulform.get("id"),
        "name": soulform.get("name"),
        "elemental_affinity": soulform.get("elemental_affinity"),
        "aura_effect": "Flare Pulse" if soulform.get("elemental_affinity") == "Fire" else "Wave Ripple",
        "body_shader": "Iridescent Ash" if soulform.get("id") == "phoenix" else "Default Shroud",
        "animation_override": "Ascend_SlowLoop"
    }

    return payload

# Optional CLI test
if __name__ == "__main__":
    sample_payload = {
        "archetype": "Strategist",
        "conviction_glyph": "☯",
        "tree_traits": {
            "discipline": 91,
            "resilience": 93,
            "mindfulness": 89,
            "expression": 73,
            "physical_care": 64,
            "emotional_regulation": 88
        },
        "xp_awarded": 100,
        "quest_unlocked": True,
        "disclosure_adjustment": {
            "resilience": 12,
            "emotional_regulation": 9
        }
    }

    test_profile = {
        "current_soulform": {
            "id": "phoenix",
            "name": "Ashborn Phoenix",
            "elemental_affinity": "Fire",
            "activated_at": "2025-05-14T17:00:00Z"
        }
    }

    routed = inject_soulform_payload(sample_payload, test_profile)
    print(json.dumps(routed, indent=2))
