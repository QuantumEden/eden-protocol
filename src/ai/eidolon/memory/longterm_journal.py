"""
Long-Term Journal – Eidolon Therapeutic Reflection Archive

Stores deep introspective entries, soulform transformations,
and trauma narratives in persistent textual format.
"""

import os
import json
from datetime import datetime
from typing import Dict, List

JOURNAL_DIR = "./logs/journals"
os.makedirs(JOURNAL_DIR, exist_ok=True)

def write_journal_entry(user_id: str, title: str, content: str, soulform_id: str = None) -> str:
    """
    Saves a new journal entry for the user with timestamp and optional soulform link.
    """
    entry = {
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "title": title,
        "content": content,
        "soulform_id": soulform_id or "unspecified"
    }

    filename = f"{user_id}_journal.json"
    filepath = os.path.join(JOURNAL_DIR, filename)

    # Append or initialize file
    if os.path.exists(filepath):
        with open(filepath, "r") as f:
            journal_data = json.load(f)
    else:
        journal_data = []

    journal_data.append(entry)

    with open(filepath, "w") as f:
        json.dump(journal_data, f, indent=2)

    return filepath

def read_journal(user_id: str) -> List[Dict]:
    """
    Returns all journal entries for the given user.
    """
    filepath = os.path.join(JOURNAL_DIR, f"{user_id}_journal.json")
    if os.path.exists(filepath):
        with open(filepath, "r") as f:
            return json.load(f)
    return []

# Example
if __name__ == "__main__":
    path = write_journal_entry(
        "initiate_042",
        title="The Day I Forgave Myself",
        content="I realized my guilt was never mine to carry. I laid it down in ritual silence.",
        soulform_id="seraph"
    )
    print(f"📝 Journal saved to: {path}")
    print("📖 Full Journal:", read_journal("initiate_042"))
