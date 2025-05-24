"""
Memory Adapter – Eidolon Short-to-Long-Term Memory Synchronizer

Merges recent session cache with long-term semantic embedding,
ensuring persistent insight and reflection continuity across sessions.
"""

from src.ai.eidolon.memory.session_cache import SessionCache
from src.ai.eidolon.memory.context_window import format_context_window
from src.ai.eidolon.memory.semantic_memory import embed_insight

# Local session memory instance
cache = SessionCache()

def sync_memory(user_id: str) -> str:
    """
    Retrieves recent dialogue, formats it into context,
    and commits semantic summary if a key insight is present.
    Returns the formatted context for immediate use.
    """
    recent_turns = cache.get_recent_turns(user_id)
    context = format_context_window(recent_turns)

    if recent_turns:
        # Check for meaningful insight in latest message
        last_user_turns = [t for t in recent_turns if t["role"] == "user"]
        if last_user_turns:
            latest_input = last_user_turns[-1]["content"]
            embed_insight(user_id, latest_input, tags=["session_reflection"])

    return context

def append_turn(user_id: str, role: str, content: str, emotion: str = "neutral") -> None:
    """
    Adds a turn to the session cache and syncs context immediately.
    """
    cache.add_turn(user_id, role, content, emotion)

# Example run
if __name__ == "__main__":
    append_turn("seer_beta", "user", "I think the trauma became part of my identity.", "resigned")
    append_turn("seer_beta", "eidolon", "Can we explore what identity would look like without the pain?", "curious")
    print(sync_memory("seer_beta"))
