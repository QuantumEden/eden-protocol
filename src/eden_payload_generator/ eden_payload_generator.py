import random

def generate_eden_payload(user_profile: dict) -> dict:
    """
    Generates a symbolic payload from the user's psychometric profile.
    """
    mbti = user_profile.get("mbti", "INTJ")
    iq = user_profile.get("iq", 100)
    eq = user_profile.get("eq", 100)
    moral = user_profile.get("moral", "care")
    sacred_path = user_profile.get("sacred_path", "None")
    group_opt_in = user_profile.get("group_opt_in", False)
    disclosure = user_profile.get("disclosure", {})

    # Archetype classification logic
    archetype_map = {
        "NT": "Strategist",
        "NF": "Healer",
        "SJ": "Guardian",
        "SP": "Builder"
    }

    prefix = mbti[1:3]
    archetype = archetype_map.get(prefix, "Strategist")

    # Conviction glyph map (simplified)
    glyph_map = {
        "care": "💖",
        "justice": "⚖️",
        "loyalty": "🛡️",
        "truth": "☯",
        "liberty": "🗽"
    }

    conviction_glyph = glyph_map.get(moral.lower(), "☯")

    # Default trait scores (0–100 scale)
    base_traits = {
        "discipline": min(100, iq + 10),
        "resilience": min(100, eq + 5),
        "mindfulness": min(100, int(eq * 0.8)),
        "expression": min(100, int(eq * 0.75)),
        "physical_care": 50,
        "emotional_regulation": min(100, int(eq * 0.85))
    }

    # Disclosure adjustments (healing bonus)
    disclosure_adjustment = {}

    if "diagnosis" in disclosure:
        if "PTSD" in disclosure["diagnosis"]:
            base_traits["resilience"] += 10
            base_traits["emotional_regulation"] += 7
            disclosure_adjustment["resilience"] = 10
            disclosure_adjustment["emotional_regulation"] = 7

        if "depression" in disclosure["diagnosis"]:
            base_traits["expression"] += 6
            base_traits["mindfulness"] += 4
            disclosure_adjustment["expression"] = 6
            disclosure_adjustment["mindfulness"] = 4

    # Cap all traits at 100
    tree_traits = {trait: min(100, value) for trait, value in base_traits.items()}

    payload = {
        "archetype": archetype,
        "conviction_glyph": conviction_glyph,
        "tree_traits": tree_traits,
        "xp_awarded": random.randint(80, 120),
        "quest_unlocked": True,
        "disclosure_adjustment": disclosure_adjustment
    }

    return payload
