"""
Interaction Logger – Eidolon Long-Term Log Archive

Stores validated therapeutic interactions as structured JSON logs,
serving as both a symbolic audit trail and recall interface.
"""

import json
import os
from datetime import datetime
from typing import Dict

# Directory to store interaction logs (update for production DB or cloud sync)
LOG_DIR = "./logs/interactions"

# Ensure directory exists
os.makedirs(LOG_DIR, exist_ok=True)

def log_interaction(user_id: str, agent: str, user_message: str, ai_response: str) -> str:
    """
    Logs a single therapeutic exchange to a JSON file.
    """
    log_entry = {
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "user_id": user_id,
        "agent": agent,
        "input": user_message,
        "response": ai_response
    }

    filename = f"{user_id}_log.json"
    filepath = os.path.join(LOG_DIR, filename)

    # Append to existing log or create new
    if os.path.exists(filepath):
        with open(filepath, "r") as f:
            log_data = json.load(f)
    else:
        log_data = []

    log_data.append(log_entry)

    with open(filepath, "w") as f:
        json.dump(log_data, f, indent=2)

    return filepath

def get_user_log(user_id: str) -> list:
    """
    Retrieves full interaction log for a user.
    """
    filepath = os.path.join(LOG_DIR, f"{user_id}_log.json")
    if os.path.exists(filepath):
        with open(filepath, "r") as f:
            return json.load(f)
    return []

# Debug test
if __name__ == "__main__":
    file_path = log_interaction(
        user_id="alpha_001",
        agent="CBT",
        user_message="I keep spiraling into worst-case scenarios.",
        ai_response="Let's reframe that. What's a more balanced possibility?"
    )
    print(f"✅ Logged to: {file_path}")
    print("📜 Full log:", get_user_log("alpha_001"))
