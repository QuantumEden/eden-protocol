# /src/ai/quest_difficulty_calculator.py

"""
Quest Difficulty Calculator — Eden Protocol

Evaluates user's XP balance across traits to generate a symbolic 'resistance curve'.
Used to adjust challenge level, pacing, and narrative pressure in AI-generated quests.
"""

def calculate_resistance_curve(trait_xp: dict) -> dict:
    """
    Analyzes XP balance and returns difficulty multipliers per trait.
    Traits far below average receive intensified focus.

    Args:
        trait_xp (dict): Trait XP distribution. Example:
            {
                "discipline": 180,
                "empathy": 95,
                "resilience": 130,
                "mindfulness": 65,
                "vitality": 25,
                "expression": 25
            }

    Returns:
        dict: Normalized difficulty weightings per trait (0.0 to 1.0)
    """
    total_xp = sum(trait_xp.values())
    if total_xp == 0:
        return {trait: 1.0 for trait in trait_xp}  # maximal challenge if uninitiated

    avg_xp = total_xp / len(trait_xp)
    difficulty_curve = {}

    for trait, xp in trait_xp.items():
        # Traits far below average are prioritized for symbolic pressure
        gap = max(avg_xp - xp, 0)
        resistance_score = min(gap / avg_xp, 1.0)
        difficulty_curve[trait] = round(resistance_score, 3)

    return difficulty_curve


# Example
if __name__ == "__main__":
    test_xp = {
        "discipline": 180,
        "empathy": 95,
        "resilience": 130,
        "mindfulness": 65,
        "vitality": 25,
        "expression": 25
    }
    result = calculate_resistance_curve(test_xp)
    print("Resistance curve:", result)
