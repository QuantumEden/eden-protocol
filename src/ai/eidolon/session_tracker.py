"""
Eidolon Session Tracker – Eden Protocol

Logs all user interactions, response summaries, and risk levels.
Tracks therapeutic trajectory and embeds Ritual Safeguard Layer logic.
"""

import datetime
from typing import Dict, List

# In-memory session log (to be replaced with DB in production)
SESSION_LOG: Dict[str, List[Dict]] = {}
RISK_LOG: Dict[str, Dict] = {}

class SessionTracker:
    def __init__(self):
        self.session_log = SESSION_LOG
        self.risk_log = RISK_LOG

    def log_interaction(self, user_id: str, user_input: str, ai_response: str) -> None:
        """
        Records an interaction between user and AI system.
        """
        entry = {
            "timestamp": datetime.datetime.utcnow().isoformat() + "Z",
            "input": user_input,
            "response": ai_response
        }
        self.session_log.setdefault(user_id, []).append(entry)

    def get_session_history(self, user_id: str) -> List[Dict]:
        """
        Retrieves the user's session log.
        """
        return self.session_log.get(user_id, [])

    def flag_risk(self, user_id: str, level: str, trigger: str) -> None:
        """
        Marks a session as elevated risk (ritual safeguard logic).
        """
        self.risk_log[user_id] = {
            "flagged_at": datetime.datetime.utcnow().isoformat() + "Z",
            "risk_level": level,
            "trigger": trigger,
            "acknowledged": False
        }

    def get_risk_status(self, user_id: str) -> Dict:
        """
        Returns the current risk status of a user.
        """
        return self.risk_log.get(user_id, {
            "risk_level": "none",
            "acknowledged": True
        })

    def acknowledge_risk(self, user_id: str) -> None:
        """
        Marks a flagged risk as acknowledged and handled.
        """
        if user_id in self.risk_log:
            self.risk_log[user_id]["acknowledged"] = True

# Manual test
if __name__ == "__main__":
    tracker = SessionTracker()
    tracker.log_interaction("user_alpha", "I feel broken.", "Tell me more about that feeling.")
    tracker.flag_risk("user_alpha", "medium", "expression of hopelessness")
    print(tracker.get_session_history("user_alpha"))
    print(tracker.get_risk_status("user_alpha"))
