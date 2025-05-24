"""
CBT Reframing Agent – Eden Protocol Therapeutic Council

Identifies cognitive distortions and offers alternative perspectives
to help restructure limiting beliefs and thought patterns.
"""

from typing import Optional

def cbt_reframe(user_id: str, message: str, context: Optional[str] = None) -> str:
    """
    Responds with a CBT-style reframing prompt.
    """
    message_lower = message.lower()

    if "always" in message_lower or "never" in message_lower:
        return (
            "That sounds like a cognitive distortion called all-or-nothing thinking. "
            "Can you think of a time when this wasn’t completely true?"
        )
    elif "nobody cares" in message_lower or "i'm worthless" in message_lower:
        return (
            "Let's challenge that thought. What evidence supports it—and what might contradict it?"
        )
    elif "i failed" in message_lower:
        return (
            "Failure can be painful, but it also teaches us. What did this moment reveal about what you truly value?"
        )
    else:
        return (
            "What you're experiencing may stem from an automatic thought. "
            "Can we look at it from a more balanced angle together?"
        )

# Example
if __name__ == "__main__":
    print(cbt_reframe("reframer_099", "I always mess everything up."))
