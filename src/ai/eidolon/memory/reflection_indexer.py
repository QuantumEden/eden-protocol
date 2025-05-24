"""
Reflection Indexer – Eidolon Ritual Reflection Tracker

Organizes introspective content, therapeutic milestones,
and symbolic rituals by date, category, and growth domain.
"""

from datetime import datetime
from typing import Dict, List

# In-memory ritual reflection index
REFLECTION_DB: Dict[str, List[Dict]] = {}

def index_reflection(user_id: str, entry_type: str, title: str, content: str, tags: List[str]) -> Dict:
    """
    Stores a reflection entry categorized by ritual or milestone type.
    """
    entry = {
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "type": entry_type,
        "title": title,
        "content": content,
        "tags": tags
    }

    REFLECTION_DB.setdefault(user_id, []).append(entry)
    return entry

def get_reflection_index(user_id: str) -> List[Dict]:
    """
    Retrieves all indexed reflections for a user.
    """
    return REFLECTION_DB.get(user_id, [])

def filter_reflections(user_id: str, tag: str) -> List[Dict]:
    """
    Filters reflection entries by tag.
    """
    return [
        r for r in REFLECTION_DB.get(user_id, [])
        if tag in r.get("tags", [])
    ]

# Test
if __name__ == "__main__":
    index_reflection(
        "seer_777",
        entry_type="ritual",
        title="Mirror of Shame",
        content="Today I confronted the voice in my head that repeats my father's insults.",
        tags=["shame", "childhood", "healing"]
    )
    print("📚 All Reflections:", get_reflection_index("seer_777"))
    print("🔍 Filter (shame):", filter_reflections("seer_777", "shame"))
