"""
Semantic Memory – Eidolon Long-Term Insight Embedding

Embeds distilled therapeutic insights into a vector database
for long-term recall and symbolic evolution tracking.
"""

from typing import Dict
import hashlib
import json

# Simulated in-memory vector store (replace with Chroma or Pinecone backend)
SEMANTIC_DB: Dict[str, Dict] = {}

def embed_insight(user_id: str, insight: str, tags: list) -> str:
    """
    Encodes an insight with metadata into the semantic memory system.
    Returns a deterministic hash key for recall.
    """
    entry = {
        "user_id": user_id,
        "insight": insight,
        "tags": tags,
    }

    insight_key = hashlib.sha256(json.dumps(entry, sort_keys=True).encode()).hexdigest()
    SEMANTIC_DB[insight_key] = entry
    return insight_key

def retrieve_insight(insight_key: str) -> Dict:
    """
    Retrieves an embedded insight by its hash key.
    """
    return SEMANTIC_DB.get(insight_key, {})

def list_user_insights(user_id: str) -> list:
    """
    Lists all semantic entries associated with a user.
    """
    return [
        {"id": k, **v}
        for k, v in SEMANTIC_DB.items()
        if v.get("user_id") == user_id
    ]

# Test run
if __name__ == "__main__":
    key = embed_insight("user_777", "I fear abandonment due to my father's silence.", ["trauma", "abandonment"])
    print("🧠 Insight ID:", key)
    print("📤 Recall:", retrieve_insight(key))
    print("📚 All Entries:", list_user_insights("user_777"))
