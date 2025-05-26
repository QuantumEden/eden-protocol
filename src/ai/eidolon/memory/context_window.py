"""
Context Window Formatter – Eidolon Short-Term Memory Compiler

Transforms recent session history into a formatted prompt context string
used by therapeutic agents during AI orchestration.
"""

from typing import List, Dict

def format_context_window(turns: List[Dict], max_turns: int = 12) -> str:
    """
    Converts a list of dialogue turns into a structured, token-efficient context block.

    Args:
        turns (List[Dict]): Recent dialogue turns with role, content, emotion
        max_turns (int): Max number of turns to include (default = 12)

    Returns:
        str: Formatted string for use in AI model prompt
    """
    # Slice most recent N turns
    trimmed = turns[-max_turns:] if max_turns else turns
    context_lines = []

    for turn in trimmed:
        role = turn.get("role", "unknown").strip().upper()
        content = turn.get("content", "").strip()
        emotion = turn.get("emotion", "neutral").strip()

        # Truncate long content entries
        if len(content) > 500:
            content = content[:497] + "..."

        # Add formatted line
        context_lines.append(f"{role} ({emotion}): {content}")

    return "\n".join(context_lines)

# === CLI Test ===
if __name__ == "__main__":
    mock_turns = [
        {"role": "user", "content": "I feel numb.", "emotion": "numb"},
        {"role": "eidolon", "content": "Let's explore what numbness means to you.", "emotion": "gentle"},
        {"role": "user", "content": "It feels like everything is muted. I can’t even cry.", "emotion": "muted"},
        {"role": "eidolon", "content": "That silence can sometimes hold the loudest truths. When did it begin?", "emotion": "calm"}
    ]

    print("\n🧠 Formatted Context Window:\n")
    print(format_context_window(mock_turns))
