"""
Semantic Memory – Eidolon Long-Term Insight Embedding

Embeds distilled therapeutic insights into a vector database
for long-term recall and symbolic evolution tracking.
"""

from typing import Dict, List
import hashlib
import json
from datetime import datetime

# Simulated in-memory vector store (to be replaced with Chroma or Pinecone)
SEMANTIC_DB: Dict[str, Dict] = {}

def embed_insight(user_id: str, insight: str, tags: List[str]) -> str:
    """
    Encodes an insight into the semantic memory layer.
    
    Args:
        user_id (str): The user to associate the insight with.
        insight (str): The raw reflective content to encode.
        tags (List[str]): Symbolic or diagnostic tags (e.g. ["grief", "identity"])
    
    Returns:
        str: Deterministic insight ID (SHA-256 hash)
    """
    entry = {
        "user_id": user_id,
        "insight": insight.strip(),
        "tags": sorted(tags),
        "timestamp": datetime.utcnow().isoformat() + "Z"
    }

    # Prevent duplicate entries
    insight_key = hashlib.sha256(json.dumps(entry, sort_keys=True).encode()).hexdigest()
    if insight_key not in SEMANTIC_DB:
        SEMANTIC_DB[insight_key] = entry

    return insight_key

def retrieve_insight(insight_key: str) -> Dict:
    """
    Retrieves a single embedded insight from memory.
    
    Args:
        insight_key (str): The hash ID of the embedded insight
    
    Returns:
        Dict: The full insight record, or empty if not found
    """
    return SEMANTIC_DB.get(insight_key, {})

def list_user_insights(user_id: str) -> List[Dict]:
    """
    Retrieves all insights associated with a specific user.
    
    Args:
        user_id (str): The user's unique ID
    
    Returns:
        List[Dict]: A list of embedded insight entries
    """
    return [
        {"id": k, **v}
        for k, v in SEMANTIC_DB.items()
        if v.get("user_id") == user_id
    ]

# === Manual Test ===
if __name__ == "__main__":
    insight = "I fear abandonment due to my father's silence."
    tags = ["trauma", "abandonment", "identity"]

    key = embed_insight("user_777", insight, tags)
    print("🧠 Insight ID:", key)

    recall = retrieve_insight(key)
    print("📤 Recalled Entry:", recall)

    all_entries = list_user_insights("user_777")
    print("📚 All Entries:", all_entries)
