"""
Treatment Plan Generator – Eidolon Council Integrator

Synthesizes insights from Freudian, Jungian, CBT, DBT, and Logotherapy agents
into a unified, symbolic treatment pathway tailored to the user's transformation arc.
"""

from typing import Dict, List

def generate_treatment_plan(user_id: str, recent_themes: List[str], soulform: str, merit_level: int) -> Dict:
    """
    Generates a symbolic, cross-modality treatment path based on reflection themes and soulform state.
    """
    base_plan = {
        "user_id": user_id,
        "soulform": soulform,
        "merit_level": merit_level,
        "core_themes": recent_themes,
        "modules": [],
        "recommendations": []
    }

    if "guilt" in recent_themes:
        base_plan["modules"].append("Freudian – unconscious guilt resolution")
        base_plan["recommendations"].append("Explore parent-based projections and suppressed memory scripts")

    if "fear" in recent_themes or "control" in recent_themes:
        base_plan["modules"].append("DBT – distress tolerance")
        base_plan["recommendations"].append("Practice radical acceptance and emotional labeling")

    if "identity" in recent_themes or "shadow" in recent_themes:
        base_plan["modules"].append("Jungian – archetype alignment")
        base_plan["recommendations"].append("Map current life events to mythic archetypes")

    if "meaning" in recent_themes or "hopelessness" in recent_themes:
        base_plan["modules"].append("Logotherapy – existential reorientation")
        base_plan["recommendations"].append("Identify small, service-oriented actions aligned with core values")

    if "distortion" in recent_themes or "failure" in recent_themes:
        base_plan["modules"].append("CBT – thought restructuring")
        base_plan["recommendations"].append("Track automatic negative thoughts and reframe daily")

    if not base_plan["modules"]:
        base_plan["modules"].append("Introductory Reflection Series")
        base_plan["recommendations"].append("Begin journaling daily and complete one Shadow Quest module")

    return base_plan

# Example
if __name__ == "__main__":
    plan = generate_treatment_plan(
        user_id="ascend_013",
        recent_themes=["guilt", "identity", "hopelessness"],
        soulform="seraph",
        merit_level=9
    )
    print("📜 Generated Plan:", plan)
