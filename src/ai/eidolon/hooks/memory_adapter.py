"""
Memory Adapter – Eidolon Short-to-Long-Term Memory Synchronizer

Merges recent session cache with long-term semantic embedding,
ensuring persistent insight and reflection continuity across sessions.
"""

from src.ai.eidolon.memory.session_cache import SessionCache
from src.ai.eidolon.memory.context_window import format_context_window
from src.ai.eidolon.memory.semantic_memory import embed_insight

# Initialize local memory cache
cache = SessionCache()

def sync_memory(user_id: str) -> str:
    """
    Retrieves recent dialogue, formats it into GPT context,
    and commits meaningful insights for long-term reflection embedding.
    
    Returns:
        Formatted context window (str) to be used by AI agents.
    """
    recent_turns = cache.get_recent_turns(user_id)
    if not recent_turns:
        return "[⏳] No recent memory found. Awaiting new session input..."

    context = format_context_window(recent_turns)

    # Step: Commit last meaningful insight
    last_user_turns = [t for t in recent_turns if t.get("role") == "user"]
    if last_user_turns:
        latest_input = last_user_turns[-1].get("content", "")
        if latest_input:
            embed_insight(user_id, latest_input, tags=["session_reflection"])

    return context

def append_turn(user_id: str, role: str, content: str, emotion: str = "neutral") -> None:
    """
    Logs a dialogue turn into the session cache and syncs context immediately.
    
    Args:
        user_id (str): Session user ID
        role (str): "user" or "eidolon"
        content (str): Raw message content
        emotion (str): Emotion tag (optional, default = "neutral")
    """
    cache.add_turn(user_id, role, content, emotion)

# === CLI Test ===
if __name__ == "__main__":
    print("\n🧠 Memory Adapter Test: Seer_Beta\n")

    append_turn("seer_beta", "user", "I think the trauma became part of my identity.", "resigned")
    append_turn("seer_beta", "eidolon", "Can we explore what identity would look like without the pain?", "curious")

    context_out = sync_memory("seer_beta")
    print("\n🪞 Synced Context Window:\n")
    print(context_out)
