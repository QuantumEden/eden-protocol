# src/soulform/soulform_eligibility.py
# Soulform Eligibility Checker – Evaluates if a user is ready to undergo transformation

from typing import Dict


def check_soulform_eligibility(
    traits: Dict[str, int],
    thresholds: Dict[str, int],
    minimum_traits_met: int = 5
) -> bool:
    """
    Check if a user qualifies for soulform transformation based on trait thresholds.

    Args:
        traits: Dictionary of user's trait scores.
        thresholds: Minimum required values for each trait.
        minimum_traits_met: Number of thresholds that must be exceeded.

    Returns:
        True if user meets or exceeds the minimum number of trait thresholds, False otherwise.
    """
    qualified_traits = [
        trait for trait, min_value in thresholds.items()
        if traits.get(trait, 0) >= min_value
    ]
    
    return len(qualified_traits) >= minimum_traits_met


def get_default_thresholds() -> Dict[str, int]:
    """
    Provides default transformation thresholds for soulform readiness.

    Returns:
        A dictionary of trait thresholds.
    """
    return {
        "discipline": 70,
        "resilience": 70,
        "mindfulness": 70,
        "expression": 70,
        "physical_care": 70,
        "emotional_regulation": 70
    }


# === CLI Test Mode ===
if __name__ == "__main__":
    print("🧪 Soulform Eligibility Check")

    user_traits = {
        "discipline": 72,
        "resilience": 85,
        "mindfulness": 78,
        "expression": 66,
        "physical_care": 70,
        "emotional_regulation": 74
    }

    thresholds = get_default_thresholds()
    eligible = check_soulform_eligibility(user_traits, thresholds)

    print(f"Eligible for transformation: {'✅ Yes' if eligible else '❌ No'}")
