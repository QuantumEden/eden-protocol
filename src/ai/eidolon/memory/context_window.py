"""
Context Window Formatter – Eidolon Short-Term Memory Compiler

Transforms recent session history into a formatted prompt context string
used by therapeutic agents during AI orchestration.
"""

from typing import List, Dict

def format_context_window(turns: List[Dict]) -> str:
    """
    Converts a list of dialogue turns into a structured context block.
    Example:
    - USER: I feel alone.
    - EIDOLON: Tell me about when that feeling started.
    """
    context_lines = []
    for turn in turns:
        role = turn.get("role", "unknown").upper()
        content = turn.get("content", "")
        emotion = turn.get("emotion", "neutral")
        context_lines.append(f"{role} ({emotion}): {content}")

    return "\n".join(context_lines)

# Example test
if __name__ == "__main__":
    mock_turns = [
        {"role": "user", "content": "I feel numb.", "emotion": "numb"},
        {"role": "eidolon", "content": "Let's explore what numbness means to you.", "emotion": "gentle"},
    ]
    print(format_context_window(mock_turns))
