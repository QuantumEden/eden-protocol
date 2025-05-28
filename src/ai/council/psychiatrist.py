"""
Psychiatric Evaluation & Triage Agent – Eden Protocol Therapeutic Council

Performs symbolic psychiatric evaluation, determines diagnostic tags,
and dynamically selects appropriate psychologist agents from the Council.
"""

from typing import Optional, Dict, List
from . import registry

def emergency_psy_eval(user_id: str, message: str, context: Optional[str] = None) -> Dict[str, str]:
    """
    Symbolic psychiatric triage based on pattern detection.
    Returns structured response with escalation flags and diagnostic tags.
    """
    lowered = message.lower()

    crisis_flags = [
        "suicidal", "kill myself", "end it all", "worthless", "can't go on", "die", "jump off", "give up"
    ]
    diagnostic_flags = {
        "depression": ["hopeless", "numb", "empty", "nothing matters", "self-hate"],
        "anxiety": ["panic", "overwhelmed", "racing thoughts", "can't breathe", "tight chest"],
        "trauma": ["flashbacks", "combat", "nightmares", "hypervigilant", "triggered"]
    }

    if any(flag in lowered for flag in crisis_flags):
        return {
            "response": (
                "⚠️ It sounds like you’re carrying more pain than one person should have to. "
                "You are not alone. I need you to know that help is available, and I want to connect you to a guardian."
            ),
            "escalation": "high",
            "tags": "crisis,triage,escalation"
        }

    detected_tags = []
    for condition, phrases in diagnostic_flags.items():
        if any(p in lowered for p in phrases):
            detected_tags.append(condition)

    if "diagnose" in lowered or "mental illness" in lowered:
        return {
            "response": (
                "A diagnosis is not an identity—it’s a starting point. "
                "Would you like to explore possible patterns or talk to a professional?"
            ),
            "escalation": "low",
            "tags": "identity,diagnostic_query"
        }

    if detected_tags:
        tag_summary = ", ".join(sorted(set(detected_tags)))
        return {
            "response": (
                f"🧠 I’m detecting themes that may point to: {tag_summary}. "
                "Would you like to explore how these patterns affect your daily life?"
            ),
            "escalation": "medium",
            "tags": tag_summary
        }

    return {
        "response": (
            "Let’s pause and evaluate how you’ve been feeling over the past few weeks. "
            "Are you having trouble sleeping, eating, concentrating, or enjoying anything?"
        ),
        "escalation": "none",
        "tags": ""
    }


def select_council_agents(diagnostic_tags: str) -> List[str]:
    """
    Selects psychologist agents from the Council based on diagnostic tag relevance.
    Uses the Council Registry metadata to match focus areas.

    Args:
        diagnostic_tags (str): Comma-separated tags from psy_eval

    Returns:
        List[str]: IDs of council members to activate
    """
    if not diagnostic_tags:
        return ["freudian", "jungian"]  # default symbolic base

    tags = {tag.strip().lower() for tag in diagnostic_tags.split(",")}
    selected = []

    for agent_id, agent_meta in registry.COUNCIL_AGENTS.items():
        focus_tags = set(agent_meta.get("focus_areas", []))
        if focus_tags.intersection(tags):
            selected.append(agent_id)

    # Fallback if no match
    return selected if selected else ["freudian", "jungian"]


# === CLI Diagnostic Mode ===
if __name__ == "__main__":
    samples = [
        "I want to end it all.",
        "My trauma won't go away.",
        "Can you diagnose me?",
        "I'm numb and anxious lately.",
        "Nothing’s wrong. Just tired."
    ]

    for msg in samples:
        triage = emergency_psy_eval("seer_001", msg)
        selected = select_council_agents(triage["tags"])
        print(f"\n🧪 Input: {msg}")
        print("🧾 Triage:", triage)
        print("🧠 Council Selected:", selected)
