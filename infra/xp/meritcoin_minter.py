# infra/xp/meritcoin_minter.py – Eden Protocol MeritCoin Minting Engine
# Mints a symbolic MeritCoin object if level + soulform + tree threshold is met

from typing import Dict

TRAIT_THRESHOLD = 50
LEVEL_REQUIREMENT = 7

def mint_meritcoin(user_id: str, level: int, tree_traits: Dict[str, int], soulform_id: str = None) -> Dict[str, any]:
    """
    Mints a MeritCoin for the user if all conditions are satisfied:
    - Minimum level met
    - All tree traits >= defined threshold
    - Optional: soulform_id provides identity stamp
    """
    eligible = level >= LEVEL_REQUIREMENT and all(score >= TRAIT_THRESHOLD for score in tree_traits.values())

    if not eligible:
        return {
            "success": False,
            "reason": "MeritCoin minting failed — requirements not met.",
            "level": level,
            "threshold": TRAIT_THRESHOLD,
            "traits": tree_traits
        }

    coin = {
        "user_id": user_id,
        "meritcoin": {
            "level": level,
            "tree_snapshot": tree_traits,
            "soulform_id": soulform_id or "none",
            "minted_at": "2025-05-18T00:00:00Z",  # replace with actual timestamp logic if needed
            "verified": True,
            "signature": f"MINT-{user_id[:4]}-{level}-{sum(tree_traits.values())}"
        }
    }

    return {
        "success": True,
        "meritcoin": coin["meritcoin"]
    }

# Optional: CLI test
if __name__ == "__main__":
    test_traits = {
        "discipline": 60,
        "resilience": 72,
        "mindfulness": 55,
        "expression": 58,
        "physical_care": 59,
        "emotional_regulation": 63
    }

    result = mint_meritcoin("user_0042", 8, test_traits, "phoenix")
    import json
    print(json.dumps(result, indent=2))
