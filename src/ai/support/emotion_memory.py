"""
Emotion Memory – Eidolon Session Emotion Tracker

Logs rolling emotional states per user using external emotion analysis (e.g., Hume API).
Supports mood-aware therapeutic modulation and longitudinal affective tracking.
"""

from datetime import datetime
from typing import Dict, List

# Stores time-stamped emotion vectors per session
EMOTION_LOG: Dict[str, List[Dict]] = {}

def record_emotion(user_id: str, emotion: str, confidence: float) -> None:
    """
    Appends an emotion entry to the user's rolling session log.
    """
    entry = {
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "emotion": emotion,
        "confidence": round(confidence, 2)
    }

    EMOTION_LOG.setdefault(user_id, []).append(entry)

def get_emotion_history(user_id: str) -> List[Dict]:
    """
    Retrieves all emotional entries for a given session.
    """
    return EMOTION_LOG.get(user_id, [])

def get_latest_emotion(user_id: str) -> str:
    """
    Returns the most recent dominant emotion for the user.
    """
    if user_id not in EMOTION_LOG or not EMOTION_LOG[user_id]:
        return "neutral"
    return EMOTION_LOG[user_id][-1]["emotion"]

# Example
if __name__ == "__main__":
    record_emotion("seer_phi", "anxious", 0.92)
    record_emotion("seer_phi", "hopeful", 0.73)
    print("🧠 Latest Emotion:", get_latest_emotion("seer_phi"))
    print("📉 Emotion History:", get_emotion_history("seer_phi"))
