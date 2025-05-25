"""
Diagnostic Daemon – Eden Protocol Monitoring Agent

Continuously audits session states, emotional volatility, and escalation markers
to detect instability, ritual breaches, or therapeutic stagnation.
"""

from datetime import datetime
from typing import Dict, List
from src.ai.support.emotion_memory import get_emotion_history
from api.services.chat_service import CHAT_SESSIONS

DIAGNOSTIC_FLAGS: Dict[str, List[Dict]] = {}

def run_diagnostic_daemon(user_id: str) -> List[Dict]:
    """
    Executes a diagnostic sweep of the user’s session history and emotion log.
    Returns list of flags if anomalies are detected.
    """
    flags = []
    emotion_log = get_emotion_history(user_id)

    # Emotional volatility scan
    if len(emotion_log) >= 4:
        recent = [e["emotion"] for e in emotion_log[-4:]]
        unique = set(recent)
        if len(unique) == 4:
            flags.append({
                "type": "emotional_volatility",
                "message": "User exhibits erratic emotional fluctuation over short time window.",
                "timestamp": datetime.utcnow().isoformat() + "Z"
            })

    # Chat stagnation detection
    for session in CHAT_SESSIONS.values():
        if session.user_id == user_id and len(session.turns) >= 6:
            last_few = session.turns[-3:]
            if all(t.content == last_few[0].content for t in last_few if t.role == "user"):
                flags.append({
                    "type": "stagnation_loop",
                    "message": "User repeating same concern or stuck in cognitive loop.",
                    "timestamp": datetime.utcnow().isoformat() + "Z"
                })

    DIAGNOSTIC_FLAGS[user_id] = flags
    return flags

def get_latest_flags(user_id: str) -> List[Dict]:
    """
    Returns the most recent diagnostic flags for a user.
    """
    return DIAGNOSTIC_FLAGS.get(user_id, [])

# Example
if __name__ == "__main__":
    flags = run_diagnostic_daemon("seer_beta")
    print("🧪 Diagnostic Flags:", flags)
