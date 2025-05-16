# meritcoin_minter.py – Eden Protocol Infra
# Handles symbolic minting of MeritCoin tokens based on verified progress

from datetime import datetime

MIN_LEVEL = 7
MIN_TRAITS = {
    "discipline": 60,
    "resilience": 60,
    "mindfulness": 60,
    "expression": 50,
    "physical_care": 50,
    "emotional_regulation": 55
}

def check_tree_threshold(tree):
    for trait, threshold in MIN_TRAITS.items():
        if tree.get(trait, 0) < threshold:
            return False
    return True

def mint_meritcoin(user_id, level, tree_traits, soulform_id=None):
    if level < MIN_LEVEL:
        return {"success": False, "reason": "Insufficient level"}

    if not check_tree_threshold(tree_traits):
        return {"success": False, "reason": "Tree of Life threshold not met"}

    mint = {
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "user_id": user_id,
        "meritcoin_id": f"MERIT-{user_id.upper()}-{datetime.utcnow().strftime('%Y%m%d%H%M%S')}",
        "level": level,
        "soulform_unlock": soulform_id if soulform_id else None,
        "status": "minted"
    }

    return {"success": True, "meritcoin": mint}

# Example
if __name__ == "__main__":
    mock_tree = {
        "discipline": 65,
        "resilience": 72,
        "mindfulness": 70,
        "expression": 51,
        "physical_care": 60,
        "emotional_regulation": 60
    }

    result = mint_meritcoin(
        user_id="user_alch_001",
        level=8,
        tree_traits=mock_tree,
        soulform_id="phoenix"
    )

    print(result)
