# identity_engine.py – Eden Protocol Avatar Generator
# Converts psychometric traits into symbolic archetypal avatar state

import json
from typing import Dict
from datetime import datetime

ARCHETYPE_DATA = {
    "ISTP": ("Builder", "The Tactician / Warrior", "Scarlet"),
    "ESTP": ("Builder", "The Daredevil / Rebel", "Amber"),
    "ISFP": ("Builder", "The Artisan / Creator", "Orange"),
    "ESFP": ("Builder", "The Performer / Jester", "Crimson"),
    "ISTJ": ("Guardian", "The Inspector / Judge", "Olive"),
    "ESTJ": ("Guardian", "The Overseer / Ruler", "Bronze"),
    "ISFJ": ("Guardian", "The Protector / Caregiver", "Forest Green"),
    "ESFJ": ("Guardian", "The Consul / Host", "Emerald"),
    "INFP": ("Healer", "The Dreamer / Healer", "Teal"),
    "ENFP": ("Healer", "The Champion / Lover", "Aqua"),
    "INFJ": ("Healer", "The Mystic / Prophet", "Indigo"),
    "ENFJ": ("Healer", "The Mentor / Teacher", "Cobalt"),
    "INTJ": ("Strategist", "The Architect / Magician", "Ivory"),
    "INTP": ("Strategist", "The Logician / Sage", "Silver"),
    "ENTJ": ("Strategist", "The Commander / Ruler", "Platinum"),
    "ENTP": ("Strategist", "The Inventor / Trickster", "Pale Gold")
}

PRIMARY_AURA = {
    "Builder": "Red",
    "Guardian": "Green",
    "Healer": "Blue",
    "Strategist": "White"
}

ELEMENT = {
    "Builder": "Fire",
    "Guardian": "Earth",
    "Healer": "Water",
    "Strategist": "Air"
}

EYE_EFFECTS = {
    "exceptional": "Lightning Irises",
    "high": "Rotating Pupils",
    "average": "Gloss Finish",
    "low": "Dim Shimmer"
}

def generate_avatar(profile: Dict[str, any]) -> Dict[str, any]:
    mbti = profile.get("mbti", "INTJ")
    iq = profile.get("iq", 100)
    eq = profile.get("eq", 100)
    moral = profile.get("moral", "care")
    current_soulform = profile.get("current_soulform")

    archetype, subtype, aura_secondary = ARCHETYPE_DATA.get(
        mbti.upper(), ("Strategist", "The Architect / Magician", "Ivory")
    )

    aura_primary = PRIMARY_AURA[archetype]
    element = ELEMENT[archetype]

    if iq >= 130:
        eye = EYE_EFFECTS["exceptional"]
    elif iq >= 115:
        eye = EYE_EFFECTS["high"]
    elif iq >= 85:
        eye = EYE_EFFECTS["average"]
    else:
        eye = EYE_EFFECTS["low"]

    avatar = {
        "avatar_id": f"{mbti.upper()}_{datetime.utcnow().strftime('%Y%m%d%H%M%S')}",
        "mbti": mbti.upper(),
        "archetype": archetype,
        "subtype": subtype,
        "element": element,
        "aura_primary": aura_primary,
        "aura_secondary": aura_secondary,
        "eye_effect": eye,
        "moral_trait": moral.lower(),
        "xp": 0,
        "level": 1,
        "merit_score": 0,
        "zk_ready": True
    }

    if current_soulform:
        avatar["soulform_state"] = {
            "id": current_soulform.get("id"),
            "name": current_soulform.get("name"),
            "elemental_affinity": current_soulform.get("elemental_affinity"),
            "activated_at": current_soulform.get("activated_at")
        }

    return avatar

# Optional CLI test
if __name__ == "__main__":
    test_profile = {
        "mbti": "INFJ",
        "iq": 126,
        "eq": 115,
        "moral": "truth",
        "current_soulform": {
            "id": "phoenix",
            "name": "Ashborn Phoenix",
            "elemental_affinity": "Fire",
            "activated_at": "2025-05-14T16:00:00Z"
        }
    }

    avatar = generate_avatar(test_profile)
    print(json.dumps(avatar, indent=2))
