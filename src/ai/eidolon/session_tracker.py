"""
Eidolon Session Tracker – Eden Protocol

Logs all user interactions, response summaries, and risk levels.
Tracks therapeutic trajectory and embeds Ritual Safeguard Layer logic.
"""

import datetime
from typing import Dict, List

# In-memory logs (to be replaced with persistent storage)
SESSION_LOG: Dict[str, List[Dict]] = {}
RISK_LOG: Dict[str, Dict] = {}

class SessionTracker:
    def __init__(self):
        self.session_log = SESSION_LOG
        self.risk_log = RISK_LOG

    def log_interaction(self, user_id: str, user_input: str, ai_response: str, session_type: str = "dialogue") -> None:
        """
        Records an interaction between the user and AI system.

        Args:
            user_id (str): Unique identifier for the user.
            user_input (str): User's message.
            ai_response (str): AI's reply.
            session_type (str): Optional session category (e.g., 'dialogue', 'ritual', 'dream')
        """
        entry = {
            "timestamp": datetime.datetime.utcnow().isoformat() + "Z",
            "input": user_input,
            "response": ai_response,
            "type": session_type
        }
        self.session_log.setdefault(user_id, []).append(entry)

    def get_session_history(self, user_id: str) -> List[Dict]:
        """
        Retrieves full session history for a user.
        """
        return self.session_log.get(user_id, [])

    def flag_risk(self, user_id: str, level: str, trigger: str) -> None:
        """
        Flags a user as being at elevated risk due to a ritual safeguard trigger.

        Args:
            level (str): Risk level (e.g., 'low', 'medium', 'high').
            trigger (str): Phrase or condition that triggered the flag.
        """
        self.risk_log[user_id] = {
            "flagged_at": datetime.datetime.utcnow().isoformat() + "Z",
            "risk_level": level,
            "trigger": trigger,
            "acknowledged": False
        }

    def get_risk_status(self, user_id: str) -> Dict:
        """
        Returns the current risk flag for the user.
        """
        return self.risk_log.get(user_id, {
            "risk_level": "none",
            "acknowledged": True
        })

    def acknowledge_risk(self, user_id: str) -> None:
        """
        Marks an existing risk flag as acknowledged and handled.
        """
        if user_id in self.risk_log:
            self.risk_log[user_id]["acknowledged"] = True

# === CLI Manual Test ===
if __name__ == "__main__":
    tracker = SessionTracker()

    # Simulate session + escalation
    tracker.log_interaction("user_alpha", "I feel broken.", "Tell me more about that feeling.", session_type="dialogue")
    tracker.flag_risk("user_alpha", "medium", "expression of hopelessness")

    # Output before acknowledgment
    print("\n🧠 Session History:")
    print(tracker.get_session_history("user_alpha"))
    print("\n⚠️ Risk Status (pre-ack):")
    print(tracker.get_risk_status("user_alpha"))

    # Acknowledge and verify
    tracker.acknowledge_risk("user_alpha")
    print("\n✅ Risk Status (post-ack):")
    print(tracker.get_risk_status("user_alpha"))
