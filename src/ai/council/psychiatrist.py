"""
Psychiatric Evaluation Agent – Eden Protocol Therapeutic Council

Performs simulated psychiatric triage, severity estimation,
and guides escalation when risk or diagnostic thresholds are breached.
"""

from typing import Optional, Dict

def emergency_psy_eval(user_id: str, message: str, context: Optional[str] = None) -> Dict[str, str]:
    """
    Symbolic psychiatric evaluation using message pattern scanning.
    Returns a structured response with escalation flag and tag hints.
    
    Args:
        user_id (str): The user being evaluated
        message (str): Raw user input
        context (Optional[str]): Recent context or summary

    Returns:
        Dict[str, str]: Evaluation response, escalation signal, and diagnostic tags
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

    # === Crisis Check ===
    if any(flag in lowered for flag in crisis_flags):
        return {
            "response": (
                "⚠️ It sounds like you’re carrying more pain than one person should have to. "
                "You are not alone. I need you to know that help is available, and I want to connect you to a guardian."
            ),
            "escalation": "high",
            "tags": "crisis,triage,escalation"
        }

    # === Diagnostic Pattern Scan ===
    detected_tags = []
    for condition, phrases in diagnostic_flags.items():
        if any(p in lowered for p in phrases):
            detected_tags.append(condition)

    # === Identity Evaluation Logic ===
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

    # === Default Reflective Prompt ===
    return {
        "response": (
            "Let’s pause and evaluate how you’ve been feeling over the past few weeks. "
            "Are you having trouble sleeping, eating, concentrating, or enjoying anything?"
        ),
        "escalation": "none",
        "tags": ""
    }

# === CLI Test ===
if __name__ == "__main__":
    tests = [
        "I want to end it all.",
        "I've been having nightmares and flashbacks again.",
        "Can you diagnose me?",
        "I feel hopeless and worthless.",
        "I'm just tired lately."
    ]

    for t in tests:
        result = emergency_psy_eval("triage_007", t)
        print(f"\n🧪 Input: {t}")
        print("🧾 Output:", result)
