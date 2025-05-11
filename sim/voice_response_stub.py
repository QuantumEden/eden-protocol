# /sim/voice_response_stub.py

from datetime import datetime
import random

# 🧠 Voice Archetypes
VOICE_ROLES = {
    "mentor": {
        "name": "Mentor",
        "tone": "Wise, encouraging, firm but compassionate",
        "examples": [
            "Every shadow you face was once a friend. Seek not to slay it — understand it.",
            "You were not meant to break the world, only to rebuild it through yourself.",
            "Today’s discomfort is tomorrow’s sanctuary — if you let it shape you."
        ]
    },
    "echo": {
        "name": "Echo",
        "tone": "Dissonant, distorted, emotionally charged (antagonist or inner critic)",
        "examples": [
            "You’ll fail again, just like last time. Why even try?",
            "This is who you are — broken, lost, pretending to evolve.",
            "What happens when they see the real you?"
        ]
    },
    "inner_voice": {
        "name": "Inner Voice",
        "tone": "Reflective, uncertain, emotionally neutral or curious",
        "examples": [
            "Why did I avoid the truth again?",
            "This path scares me, but maybe that's the point.",
            "What would I become if I actually finished this quest?"
        ]
    }
}

# 🧪 Simulate Dialogue Output
def simulate_voice_response(role_key, context=None):
    role = VOICE_ROLES.get(role_key)
    if not role:
        return f"[UNKNOWN VOICE ROLE: {role_key}]"

    message = random.choice(role["examples"])
    return f"\n🗣️ {role['name']} ({role['tone']}):\n💬 {message}\n📅 {datetime.now().isoformat()}"

# 🔂 Simulate all three voices
if __name__ == "__main__":
    print(simulate_voice_response("mentor"))
    print(simulate_voice_response("echo"))
    print(simulate_voice_response("inner_voice"))
