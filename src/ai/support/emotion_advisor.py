"""
Emotion Advisor – Eidolon Tone Adjustment Recommender

Interprets recent emotional vectors to guide tone, empathy level,
or silence-based response modes for therapeutic agents.
Also provides normalization for raw Hume API emotion payloads.
"""

from src.ai.support.emotion_memory import get_latest_emotion
from typing import Dict

# Canonical emotion classes used across Eden Protocol
VALID_EMOTIONS = {
    "joy": ["joy", "happy", "cheerful", "content"],
    "sadness": ["sad", "sorrow", "grief", "melancholy"],
    "anger": ["angry", "frustrated", "irritated", "rage"],
    "fear": ["afraid", "scared", "anxious", "worried"],
    "surprise": ["surprised", "shocked", "startled"],
    "disgust": ["disgust", "grossed_out", "repulsed"],
    "trust": ["trust", "safe", "secure"],
    "anticipation": ["excited", "curious", "engaged"],
    "neutral": ["neutral", "calm", "balanced"]
}

# Flat reverse mapping for incoming emotion normalization
EMOTION_LOOKUP = {alias: key for key, aliases in VALID_EMOTIONS.items() for alias in aliases}

def normalize_hume_emotions(raw_emotions: Dict[str, float]) -> Dict[str, float]:
    """
    Normalizes raw Hume emotion scores into Eden Protocol's schema.

    Args:
        raw_emotions (Dict[str, float]): Raw scores from Hume API

    Returns:
        Dict[str, float]: Aggregated, normalized emotion profile
    """
    normalized = {key: 0.0 for key in VALID_EMOTIONS}

    for raw_label, intensity in raw_emotions.items():
        if not isinstance(intensity, (int, float)):
            continue
        mapped_key = EMOTION_LOOKUP.get(raw_label.lower())
        if mapped_key:
            normalized[mapped_key] += min(100.0, float(intensity))

    for key, value in normalized.items():
        normalized[key] = round(min(value, 100.0), 2)

    return normalized

def recommend_tone(user_id: str) -> str:
    """
    Suggests a response tone based on the user's current affective state.
    """
    mood = get_latest_emotion(user_id)

    tone_map = {
        "anxious": "reassuring",
        "fearful": "calm",
        "angry": "neutral-direct",
        "sad": "gentle",
        "guilt": "accepting",
        "shame": "affirming",
        "hopeful": "curious",
        "happy": "playful",
        "neutral": "reflective"
    }

    return tone_map.get(mood, "reflective")

# Example
if __name__ == "__main__":
    user_id = "sage_echo_017"
    print("🎨 Recommended Tone:", recommend_tone(user_id))

    # Example normalized Hume payload
    raw = {
        "joy": 34.5,
        "sad": 12.1,
        "calm": 40.2,
        "startled": 8.9,
        "grossed_out": 5.5
    }
    print("\n🧠 Normalized Emotions:", normalize_hume_emotions(raw))
