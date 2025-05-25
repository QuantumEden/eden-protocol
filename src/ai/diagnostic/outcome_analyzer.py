"""
Outcome Analyzer – Eden Protocol Progress Evaluation Module

Analyzes symbolic outputs across sessions to assess growth patterns,
ritual success, or stagnation based on user reflections and flags.
"""

from typing import Dict, List
from src.ai.eidolon.memory.reflection_indexer import get_reflection_index
from src.ai.diagnostic.daemon import get_latest_flags

def analyze_user_outcome(user_id: str) -> Dict:
    """
    Evaluates user transformation patterns based on reflections and flag history.
    Returns a summary of spiritual momentum and symbolic trajectory.
    """
    reflections = get_reflection_index(user_id)
    flags = get_latest_flags(user_id)

    outcome = {
        "user_id": user_id,
        "reflection_count": len(reflections),
        "flag_count": len(flags),
        "growth_signal": "neutral",
        "recommendation": "continue monitoring"
    }

    if len(reflections) >= 5 and len(flags) == 0:
        outcome["growth_signal"] = "ascending"
        outcome["recommendation"] = "unlock next ritual tier"
    elif len(flags) >= 2:
        outcome["growth_signal"] = "at-risk"
        outcome["recommendation"] = "schedule guardian intervention"
    elif len(reflections) > 0 and any("loop" in f["type"] for f in flags):
        outcome["growth_signal"] = "stalled"
        outcome["recommendation"] = "assign reflection break or dreamwork mod"

    return outcome

# Example
if __name__ == "__main__":
    summary = analyze_user_outcome("seer_beta")
    print("📈 Outcome Analysis:", summary)
