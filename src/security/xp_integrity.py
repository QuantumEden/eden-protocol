# /src/security/xp_integrity.py
"""
XP Integrity Engine – Symbolic Truth Validator for Eden Protocol (Security Layer)

This module ensures that XP gains are:
- Aligned with verified symbolic quests
- Derived from meaningful biometric/trait improvement
- Not fabricated or manipulated through invalid quests

Delegates mod XP cap enforcement and DAO validation to src.xp.xp_integrity.
"""

from typing import Tuple, Dict
from src.xp.xp_integrity import validate_xp_from_mod  # Cross-layer import

# === Core Symbolic Validators ===

def is_quest_validated(quest_completion: bool, biometric_data: Dict[str, int], trait_change: Dict[str, int]) -> bool:
    """
    Verifies that the user has made legitimate progress from a therapeutic standpoint.
    """
    if not quest_completion:
        return False

    # Require symbolic movement in biometric traits
    if biometric_data.get("mindfulness", 0) < 10 and trait_change.get("mindfulness", 0) <= 0:
        return False

    return True


def calculate_xp_gain(quest_theme: str, trait_change: Dict[str, int]) -> int:
    """
    Returns XP proportional to theme difficulty and trait growth magnitude.
    """
    base_xp = 50
    multiplier = {
        "Shadow": 2.0,
        "Discipline": 1.5,
        "Forgiveness": 1.3
    }.get(quest_theme, 1.0)

    total_trait_gain = sum([v for v in trait_change.values() if v > 0])
    return int(base_xp + (total_trait_gain * multiplier))


def validate_xp_submission(user_state: Dict, quest_completion: bool, biometric_data: Dict, trait_change: Dict) -> Tuple[bool, int, str]:
    """
    Main validator for EdenQuest XP claims.
    Combines psychometric, symbolic, and trait-based integrity checks.
    """
    if not is_quest_validated(quest_completion, biometric_data, trait_change):
        return False, 0, "❌ Quest validation failed: no meaningful biometric or trait movement."

    quest_theme = user_state.get("edenquest", {}).get("quest", {}).get("theme", "Unknown")
    xp = calculate_xp_gain(quest_theme, trait_change)
    return True, xp, f"✅ XP awarded: {xp} from '{quest_theme}' quest."


# === Optional: Mod XP Validator Bridge ===

def validate_mod_xp_bridge(user_id: str, mod_id: str, amount: int) -> Tuple[bool, str]:
    """
    Secure call to XP mod validator. Can be expanded for zero-knowledge audits later.
    """
    try:
        validate_xp_from_mod(user_id, mod_id, amount)
        return True, "✅ Mod XP validated successfully."
    except Exception as e:
        return False, f"❌ Mod XP validation failed: {str(e)}"


# === CLI Simulation ===
if __name__ == "__main__":
    # Mock therapeutic validation
    user_state = {
        "edenquest": {
            "quest": {"theme": "Shadow"}
        }
    }
    biometric_data = {"mindfulness": 15}
    trait_change = {"mindfulness": 5, "resilience": 2}
    quest_result = validate_xp_submission(user_state, True, biometric_data, trait_change)

    print("\n[🧪 XP INTEGRITY – SECURITY TEST]")
    print(f"Valid: {quest_result[0]}")
    print(f"XP: {quest_result[1]}")
    print(f"Message: {quest_result[2]}")

    # Mock mod XP bridge test
    mod_check = validate_mod_xp_bridge("seer_021", "tai_chi_001", 60)
    print("\n[🔐 MOD XP BRIDGE TEST]")
    print(f"Valid: {mod_check[0]}")
    print(f"Message: {mod_check[1]}")
