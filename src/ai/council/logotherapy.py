"""
Logotherapy Probe – Eden Protocol Therapeutic Council

Guides the user toward meaning-making in suffering, crisis, and healing.
Inspired by Viktor Frankl’s existential analysis.
"""

from typing import Optional

def logotherapy_probe(user_id: str, message: str, context: Optional[str] = None) -> str:
    """
    Responds with a logotherapy-style prompt, helping users search for meaning.
    """
    message_lower = message.lower()

    if "meaning" in message_lower or "purpose" in message_lower:
        return (
            "The search for meaning is not found in answers—but in the stance you take toward the pain. "
            "What small action could turn this moment into something sacred?"
        )
    elif "suffering" in message_lower or "hopeless" in message_lower:
        return (
            "Even in suffering, we can choose our response. What value are you still capable of embodying today?"
        )
    elif "lost" in message_lower:
        return (
            "Sometimes we feel lost because we’ve outgrown the path we were on. "
            "What principle do you wish to live by, even now?"
        )
    else:
        return (
            "Every moment contains a question. Not 'Why is this happening?' but 'Who am I becoming through this?'"
        )

# Registry alias for compatibility
def interpret(user_id: str, message: str, context: Optional[str] = None) -> str:
    """
    Alias function for registry compatibility.
    """
    return logotherapy_probe(user_id, message, context)

# Example
if __name__ == "__main__":
    print(logotherapy_probe("alpha_witness", "I don’t see the point of any of this anymore."))
