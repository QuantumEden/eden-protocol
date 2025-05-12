def apply_sacred_path_effects(profile: dict) -> dict:
    """
    Maps a user's sacred path to symbolic aura and glyph modifications.
    Should be called before avatar finalization.
    """
    path = profile.get("sacred_path", "Undeclared")

    sacred_effects = {
        "Zen Buddhism": {"aura_color": "#6DDCCF", "glyph": "🜄"},
        "Kabbalah": {"aura_color": "#E2C4F9", "glyph": "✡"},
        "Alchemy": {"aura_color": "#F1D37A", "glyph": "🜂"},
        "Christianity": {"aura_color": "#EAD1DC", "glyph": "✝"},
        "Taoism": {"aura_color": "#D0F0C0", "glyph": "☯"},
        "Judaism": {"aura_color": "#B0D0F0", "glyph": "✡"},
        "Norse Paganism": {"aura_color": "#C9C0BB", "glyph": "ᛟ"},
        "Custom": {"aura_color": "#FFFFFF", "glyph": "🜁"},
        "Undeclared": {"aura_color": "#AAAAAA", "glyph": "◎"}
    }

    effects = sacred_effects.get(path, sacred_effects["Undeclared"])
    profile["aura_color"] = effects["aura_color"]
    profile["glyph"] = effects["glyph"]

    return profile
