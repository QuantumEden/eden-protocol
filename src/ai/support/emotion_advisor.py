"""
Emotion Advisor – Eidolon Tone Adjustment Recommender

Interprets recent emotional vectors to guide tone, empathy level,
or silence-based response modes for therapeutic agents.
"""

from src.ai.support.emotion_memory import get_latest_emotion

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
