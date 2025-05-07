import json
from typing import Dict

# MBTI to archetype, subtype, and secondary aura mapping
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

def generate_avatar(profile: Dict[str, any]) -> Dict[str, str]:
    mbti = profile.get("mbti", "INTJ")
    iq = profile.get("iq", 100)
    eq = profile.get("eq", 100)
    moral = profile.get("moral", "care")

    archetype, subtype, secondary_aura = ARCHETYPE_DATA.get(mbti.upper(), ("Strategist", "The Architect / Magician", "Ivory"))
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
        "MBTI": mbti,
        "Archetype": archetype,
        "Subtype": subtype,
        "Element": element,
        "AuraPrimary": aura_primary,
        "AuraSecondary": secondary_aura,
        "EyeEffect": eye,
        "MoralTrait": moral,
        "XP": 0,
        "Level": 1
    }

    return avatar

# Optional CLI test
if __name__ == "__main__":
    test_profile = {
        "mbti": "INFJ",
        "iq": 126,
        "eq": 115,
        "moral": "fairness"
    }

    avatar = generate_avatar(test_profile)
    print(json.dumps(avatar, indent=2))
