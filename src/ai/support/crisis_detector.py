"""
Crisis Detector – Eidolon Ritual Safeguard Layer

Scans user input for crisis keywords or emotional distress signals.
Triggers escalation flags in the SessionTracker when activated.
"""

from typing import List

CRISIS_KEYWORDS: List[str] = [
    "suicide", "kill myself", "end it all", "i want to die",
    "i can't go on", "worthless", "nothing matters", "no reason to live",
    "hurt myself", "cutting", "overdose", "bleed", "jump off"
]

def detect_crisis_keywords(text: str) -> bool:
    """
    Returns True if any crisis phrase is detected in the message.
    """
    text_lower = text.lower()
    return any(phrase in text_lower for phrase in CRISIS_KEYWORDS)

# Example
if __name__ == "__main__":
    test = "I can't go on like this, I want to end it all."
    print("🚨 Crisis Detected:" if detect_crisis_keywords(test) else "✅ No crisis detected.")
