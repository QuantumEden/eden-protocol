"""
Session Cache – Eidolon Short-Term Memory Module

Maintains a rolling window of recent dialogue and emotion data.
Used to construct real-time context windows for therapeutic agents.
"""

from collections import deque
from typing import Dict, List

# Configurable window size
CACHE_WINDOW = 8

class SessionCache:
    def __init__(self):
        self.cache: Dict[str, deque] = {}

    def add_turn(self, user_id: str, role: str, content: str, emotion: str = "neutral") -> None:
        """
        Appends a dialogue turn and optional emotion to the session buffer.
        """
        turn = {
            "role": role,  # "user" or "eidolon"
            "content": content,
            "emotion": emotion
        }
        if user_id not in self.cache:
            self.cache[user_id] = deque(maxlen=CACHE_WINDOW)
        self.cache[user_id].append(turn)

    def get_recent_turns(self, user_id: str) -> List[Dict]:
        """
        Returns the recent dialogue history for a user.
        """
        return list(self.cache.get(user_id, []))

    def clear(self, user_id: str) -> None:
        """
        Clears the cache for a given user.
        """
        if user_id in self.cache:
            self.cache[user_id].clear()

# Example test
if __name__ == "__main__":
    memory = SessionCache()
    memory.add_turn("user_001", "user", "I'm scared of what happens next.", "fear")
    memory.add_turn("user_001", "eidolon", "Let's explore that feeling together.", "supportive")
    print(memory.get_recent_turns("user_001"))
