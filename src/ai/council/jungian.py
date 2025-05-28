"""
Jungian Reflection Agent – Eden Protocol Therapeutic Council

Engages with archetypes, shadow work, symbolic dreams, and the individuation process.
Helps the user interpret meaning from recurring inner images and mythic narratives.
"""

from typing import Optional

def jungian_reflection(user_id: str, message: str, context: Optional[str] = None) -> str:
    """
    Responds with a Jungian-style insight or reflective question.
    """
    message_lower = message.lower()

    if "shadow" in message_lower:
        return (
            "The shadow is not your enemy, but a truth you have not yet embraced. "
            "What part of yourself have you tried hardest to hide?"
        )
    elif "dream" in message_lower:
        return (
            "Dreams speak the language of symbols. What recurring images or feelings arise in your dreams?"
        )
    elif "archetype" in message_lower or "hero" in message_lower:
        return (
            "Which archetype calls to you in this moment: the Hero, the Orphan, the Sage, the Trickster? "
            "Consider why that figure resonates now."
        )
    else:
        return (
            "Every experience shapes your myth. What role do you feel you're playing in your current story?"
        )

# Registry alias for compatibility
def interpret(user_id: str, message: str, context: Optional[str] = None) -> str:
    """
    Alias function for registry compatibility.
    """
    return jungian_reflection(user_id, message, context)

# Example
if __name__ == "__main__":
    print(jungian_reflection("dreamer_007", "I keep seeing a wolf in my dreams."))
