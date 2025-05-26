"""
MeritCoin Minter – Eden Protocol XP Engine

Handles symbolic minting of soulbound MeritCoins tied to verified growth.
Includes level gate, trait thresholds, soulform linking, and DAO sync compatibility.
"""

from datetime import datetime
import hashlib
from typing import Dict, Optional

# Minimum requirements for minting
MIN_LEVEL = 7
MIN_TRAITS = {
    "discipline": 60,
    "resilience": 60,
    "mindfulness": 60,
    "expression": 50,
    "physical_care": 50,
    "emotional_regulation": 55
}

# Optional in-memory ledger to prevent duplicate mints (simulate external db check)
MINT_HISTORY: Dict[str, Dict] = {}

def check_tree_threshold(tree: Dict[str, int]) -> bool:
    """
    Verifies that all required Tree of Life traits meet the minimum threshold.
    """
    for trait, threshold in MIN_TRAITS.items():
        if tree.get(trait, 0) < threshold:
            return False
    return True

def generate_meritcoin_id(user_id: str, level: int, soulform_id: Optional[str]) -> str:
    """
    Generates a unique, hash-based meritcoin ID to prevent duplication and ensure traceability.
    """
    payload = f"{user_id}|{level}|{soulform_id or 'none'}|{datetime.utcnow().isoformat()}"
    return "MERIT-" + hashlib.sha256(payload.encode()).hexdigest()[:12].upper()

def mint_meritcoin(user_id: str, level: int, tree_traits: Dict[str, int], soulform_id: Optional[str] = None) -> Dict:
    """
    Mints a symbolic MeritCoin if level and trait thresholds are met.
    
    Args:
        user_id (str): User's unique identifier
        level (int): User's current level
        tree_traits (Dict): Tree of Life trait scores
        soulform_id (Optional[str]): Active soulform transformation
    
    Returns:
        Dict: Minting result object
    """
    if level < MIN_LEVEL:
        return {"success": False, "reason": "Insufficient level"}

    if not check_tree_threshold(tree_traits):
        return {"success": False, "reason": "Tree of Life threshold not met"}

    # Optional: prevent re-minting per level + soulform combo
    ledger_key = f"{user_id}|L{level}|{soulform_id or 'none'}"
    if ledger_key in MINT_HISTORY:
        return {"success": False, "reason": "MeritCoin already minted for this transformation"}

    # Generate Mint
    coin_id = generate_meritcoin_id(user_id, level, soulform_id)
    mint = {
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "user_id": user_id,
        "meritcoin_id": coin_id,
        "level": level,
        "soulform_unlock": soulform_id or None,
        "status": "minted"
    }

    MINT_HISTORY[ledger_key] = mint
    return {"success": True, "meritcoin": mint}

# === CLI Test ===
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
