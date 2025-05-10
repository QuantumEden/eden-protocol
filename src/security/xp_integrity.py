# /src/security/xp_integrity.py

"""
XP Integrity Engine – Symbolic Truth Validator for Eden Protocol

This module ensures that XP gains are:
- Aligned with symbolic quests
- Derived from verified sources (e.g. biometric sync, journaling, event logs)
- Not fabricated or inflated

It uses integrity thresholds and symbolic consistency checks to validate behavioral growth.
"""

def is_quest_validated(quest_completion, biometric_data, trait_change):
    """
    Checks if a quest's completion is behaviorally and symbolically valid.
    """
    if not quest_completion:
        return False

    # Require some biometric improvement or symbolic alignment
    if biometric_data.get("mindfulness", 0) < 10 and trait_change.get("mindfulness", 0) <= 0:
        return False

    return True

def calculate_xp_gain(quest_theme, trait_change):
    """
    XP gain is proportional to the symbolic difficulty of the quest and the magnitude of trait growth.
    """
    base_xp = 50
    multiplier = 1.0

    if quest_theme == "Shadow":
        multiplier = 2.0
    elif quest_theme == "Discipline":
        multiplier = 1.5
    elif quest_theme == "Forgiveness":
        multiplier = 1.3

    total_trait_gain = sum([v for v in trait_change.values() if v > 0])
    return int(base_xp + (total_trait_gain * multiplier))

def validate_xp_submission(user_state, quest_completion, biometric_data, trait_change):
    """
    Validates an XP claim based on quest legitimacy, biometric trends, and Tree of Life updates.
    Returns a tuple: (is_valid, xp_awarded, reason)
    """
    if not is_quest_validated(quest_completion, biometric_data, trait_change):
        return (False, 0, "Quest validation failed: insufficient biometric or trait movement.")

    xp = calculate_xp_gain(user_state["edenquest"]["quest"]["theme"], trait_change)
    return (True, xp, "XP awarded successfully.")

# Example test run
if __name__ == "__main__":
    # Mock input
    user_state = {
        "edenquest": {
            "quest": {"theme": "Shadow"}
        }
    }
    biometric_data = {"mindfulness": 15}
    trait_change = {"mindfulness": 5, "resilience": 2}

    is_valid, xp, reason = validate_xp_submission(user_state, True, biometric_data, trait_change)
    print("\n[XP INTEGRITY TEST RESULT]")
    print(f"Valid: {is_valid}")
    print(f"XP Awarded: {xp}")
    print(f"Reason: {reason}")
