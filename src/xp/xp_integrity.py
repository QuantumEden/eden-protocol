# /src/xp/xp_integrity.py

"""
XP Integrity Validator — now with Mod XP Verification

Validates XP claims from core systems, shadow quests, and DAO-approved mods.
Ensures truth alignment and prevents symbolic inflation or unauthorized XP farming.
"""

try:
    from src.dao.mod_registry import get_approved_mod_ids
except ImportError:
    try:
        from dao.mod_registry import get_approved_mod_ids  # fallback for legacy import
    except ImportError:
        def get_approved_mod_ids():
            print("⚠️ WARNING: Fallback mod_registry import — returning placeholder mod list.")
            return ["tai_chi_001", "journal_ritual_002"]

MOD_XP_CAP = 100  # Max XP a mod can award per instance


def validate_xp(user_id: str, source: str, amount: int) -> bool:
    """
    Validates core XP gain from symbolic systems.
    """
    if amount < 0:
        raise ValueError("XP must be positive.")
    if amount > 500:
        raise ValueError("XP exceeds standard system bounds.")
    return True


def validate_xp_from_mod(user_id: str, mod_id: str, amount: int) -> bool:
    """
    Ensures DAO-approved mods are used and XP awarded is within symbolic limits.
    """
    approved = get_approved_mod_ids()
    if mod_id not in approved:
        raise PermissionError(f"Mod ID {mod_id} not DAO-approved.")
    if amount > MOD_XP_CAP:
        raise ValueError("Mod XP exceeds symbolic allowance.")
    return True


# CLI test block
if __name__ == "__main__":
    try:
        assert validate_xp("user123", "core_quest", 200)
        assert validate_xp_from_mod("user123", "tai_chi_001", 60)
        print("✅ XP validation passed.")
    except Exception as e:
        print("❌ XP validation failed:", str(e))
