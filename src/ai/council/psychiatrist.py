"""
Psychiatric Evaluation Agent – Eden Protocol Therapeutic Council

Performs simulated psychiatric triage, severity estimation, and
guides escalation when risk or diagnostic thresholds are breached.
"""

from typing import Optional, Dict

def emergency_psy_eval(user_id: str, message: str, context: Optional[str] = None) -> str:
    """
    Performs a symbolic psychiatric evaluation and determines escalation potential.
    """
    red_flags = ["suicidal", "kill myself", "end it all", "worthless", "can't go on", "die"]

    if any(flag in message.lower() for flag in red_flags):
        return (
            "⚠️ It sounds like you’re carrying more pain than one person should have to. "
            "You are not alone. I need you to know that help is available, and I want to connect you to a guardian."
        )
    
    if "diagnose" in message.lower() or "mental illness" in message.lower():
        return (
            "A diagnosis is not an identity—it’s a starting point. "
            "Would you like to explore possible patterns or talk to a professional?"
        )

    return (
        "Let’s pause and evaluate how you’ve been feeling over the past few weeks. "
        "Are you having trouble sleeping, eating, concentrating, or enjoying anything?"
    )

# Example
if __name__ == "__main__":
    print(emergency_psy_eval("triage_007", "I want to end it all."))
