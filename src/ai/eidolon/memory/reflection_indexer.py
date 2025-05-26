"""
Reflection Indexer – Eidolon Ritual Reflection Tracker

Organizes introspective content, therapeutic milestones,
and symbolic rituals by date, category, and growth domain.
"""

from datetime import datetime
from typing import Dict, List
import hashlib
import json

# In-memory ritual reflection index
REFLECTION_DB: Dict[str, List[Dict]] = {}

def index_reflection(user_id: str, entry_type: str, title: str, content: str, tags: List[str]) -> Dict:
    """
    Stores a reflection entry categorized by ritual or milestone type.

    Args:
        user_id (str): User submitting the reflection
        entry_type (str): One of ['ritual', 'milestone', 'insight']
        title (str): Reflection title or label
        content (str): Full reflection content
        tags (List[str]): Symbolic, emotional, or cognitive tags

    Returns:
        Dict: Full stored entry including its reflection_id
    """
    clean_tags = sorted(set(tag.strip().lower() for tag in tags))
    
    entry = {
        "user_id": user_id,
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "type": entry_type,
        "title": title.strip(),
        "content": content.strip(),
        "tags": clean_tags
    }

    # Generate reflection_id
    reflection_id = hashlib.sha256(json.dumps(entry, sort_keys=True).encode()).hexdigest()
    entry["reflection_id"] = reflection_id

    REFLECTION_DB.setdefault(user_id, []).append(entry)
    return entry

def get_reflection_index(user_id: str) -> List[Dict]:
    """
    Retrieves all indexed reflections for a user.
    
    Args:
        user_id (str): Unique user identifier
    
    Returns:
        List[Dict]: All reflections indexed under this user
    """
    return REFLECTION_DB.get(user_id, [])

def filter_reflections(user_id: str, tag: str) -> List[Dict]:
    """
    Filters a user's reflections by a specific tag.

    Args:
        user_id (str): User to search
        tag (str): Tag to filter on

    Returns:
        List[Dict]: Matching reflection entries
    """
    return [
        r for r in REFLECTION_DB.get(user_id, [])
        if tag.lower() in r.get("tags", [])
    ]

# === CLI Test ===
if __name__ == "__main__":
    entry = index_reflection(
        "seer_777",
        entry_type="ritual",
        title="Mirror of Shame",
        content="Today I confronted the voice in my head that repeats my father's insults.",
        tags=["shame", "childhood", "healing"]
    )

    print("\n📘 Indexed Entry:")
    print(entry)

    print("\n📚 All Reflections for user_777:")
    print(get_reflection_index("seer_777"))

    print("\n🔍 Filter by tag: 'shame'")
    print(filter_reflections("seer_777", "shame"))
