"""
Report Generator – Eden Protocol Diagnostic Engine

Aggregates session logs, emotion history, and system flags into a symbolic
report format for therapist review, DAO tribunal evidence, or ritual evaluation.
"""

from datetime import datetime
from typing import Dict, List
from src.ai.support.emotion_memory import get_emotion_history
from api.services.chat_service import get_chat_history
from src.ai.diagnostic.daemon import get_latest_flags

def generate_diagnostic_report(user_id: str, session_id: str) -> Dict:
    """
    Creates a symbolic diagnostic report of the user’s recent activity.
    Includes emotion traces, chat transcript, and detected flags.
    """
    report = {
        "user_id": user_id,
        "session_id": session_id,
        "generated_at": datetime.utcnow().isoformat() + "Z",
        "emotion_trace": get_emotion_history(user_id),
        "chat_transcript": [turn.dict() for turn in get_chat_history(session_id)],
        "diagnostic_flags": get_latest_flags(user_id),
        "status": "stable"  # Default status
    }

    if report["diagnostic_flags"]:
        report["status"] = "at-risk"

    return report

# Example
if __name__ == "__main__":
    from uuid import uuid4
    session_id = f"mock-session-{uuid4().hex[:6]}"
    result = generate_diagnostic_report("seer_beta", session_id)
    print("📋 Diagnostic Report:", result)
