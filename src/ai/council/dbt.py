"""
DBT Balance Agent – Eden Protocol Therapeutic Council

Helps the user regulate emotions, tolerate distress, and cultivate mindfulness.
Blends radical acceptance with practical regulation tools.
"""

from typing import Optional

def dbt_balance(user_id: str, message: str, context: Optional[str] = None) -> str:
    """
    Responds with a DBT-informed prompt or exercise suggestion.
    """
    message_lower = message.lower()

    if "overwhelmed" in message_lower or "panic" in message_lower:
        return (
            "When you feel overwhelmed, try the TIPP skill—temperature, intense exercise, paced breathing, and paired muscle relaxation. "
            "Which of those do you feel willing to try right now?"
        )
    elif "angry" in message_lower or "rage" in message_lower:
        return (
            "Anger is valid, but it burns fast. Can you describe the unmet need beneath your anger?"
        )
    elif "regulate" in message_lower or "out of control" in message_lower:
        return (
            "Try describing what you're feeling using the ABC skill—accumulate positive emotions, build mastery, and cope ahead. "
            "Which letter feels most relevant today?"
        )
    else:
        return (
            "Let’s take a mindful pause. What are five things you can see, four you can touch, three you can hear, two you can smell, and one you can taste?"
        )

# Registry alias for compatibility
def interpret(user_id: str, message: str, context: Optional[str] = None) -> str:
    """
    Alias function for registry compatibility.
    """
    return dbt_balance(user_id, message, context)

# Example
if __name__ == "__main__":
    print(dbt_balance("balance_seeker", "I'm feeling panicked and can't calm down."))
