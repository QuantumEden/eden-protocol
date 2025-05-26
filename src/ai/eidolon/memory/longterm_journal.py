"""
Long-Term Journal – Eidolon Therapeutic Reflection Archive

Stores deep introspective entries, soulform transformations,
and trauma narratives in persistent textual format.
"""

import os
import json
import hashlib
from datetime import datetime
from typing import Dict, List, Optional

JOURNAL_DIR = "./logs/journals"
os.makedirs(JOURNAL_DIR, exist_ok=True)

def generate_journal_id(entry: Dict) -> str:
    """
    Generates a deterministic SHA-256 ID for a journal entry.
    """
    return hashlib.sha256(json.dumps(entry, sort_keys=True).encode()).hexdigest()

def write_journal_entry(
    user_id: str,
    title: str,
    content: str,
    soulform_id: Optional[str] = None,
    domain: Optional[str] = None,
    tags: Optional[List[str]] = None
) -> str:
    """
    Saves a long-form introspective journal entry to the archive.
    
    Args:
        user_id (str): User's unique ID
        title (str): Reflection title
        content (str): Full reflection body
        soulform_id (str): Associated transformation ID (if any)
        domain (str): Growth domain (e.g. identity, trauma, forgiveness)
        tags (List[str]): Optional metadata for indexing
    
    Returns:
        str: Path to journal file
    """
    clean_tags = sorted(set(tags)) if tags else []
    entry = {
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "title": title.strip(),
        "content": content.strip(),
        "soulform_id": soulform_id or "unspecified",
        "domain": domain or "general",
        "tags": clean_tags
    }

    entry["journal_id"] = generate_journal_id(entry)

    filename = f"{user_id}_journal.json"
    filepath = os.path.join(JOURNAL_DIR, filename)

    # Append or initialize file
    if os.path.exists(filepath):
        with open(filepath, "r", encoding="utf-8") as f:
            journal_data = json.load(f)
    else:
        journal_data = []

    journal_data.append(entry)

    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(journal_data, f, indent=2, ensure_ascii=False)

    return filepath

def read_journal(user_id: str) -> List[Dict]:
    """
    Retrieves all stored journal entries for a user.
    """
    filepath = os.path.join(JOURNAL_DIR, f"{user_id}_journal.json")
    if os.path.exists(filepath):
        with open(filepath, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def find_journal_by_tag(user_id: str, tag: str) -> List[Dict]:
    """
    Returns entries tagged with a specific keyword.
    """
    return [
        j for j in read_journal(user_id)
        if tag.lower() in [t.lower() for t in j.get("tags", [])]
    ]

# === Manual Test ===
if __name__ == "__main__":
    path = write_journal_entry(
        "initiate_042",
        title="The Day I Forgave Myself",
        content="I realized my guilt was never mine to carry. I laid it down in ritual silence.",
        soulform_id="seraph",
        domain="forgiveness",
        tags=["ritual", "guilt", "healing"]
    )

    print(f"\n📝 Journal saved to: {path}")
    print("\n📖 Full Journal:")
    print(read_journal("initiate_042"))

    print("\n🔍 Filtered by tag: 'ritual'")
    print(find_journal_by_tag("initiate_042", "ritual"))
