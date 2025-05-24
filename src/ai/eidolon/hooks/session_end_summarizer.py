"""
Session End Summarizer – Eidolon Context Wrap & Commit Handler

Generates symbolic summaries of therapeutic sessions,
extracting key insights and committing them to long-term memory.
Formats output to align with interaction summary schema.
"""

from datetime import datetime
from typing import Dict, List
from src.ai.eidolon.memory.semantic_memory import embed_insight

def summarize_session(user_id: str, dialogue_log: List[Dict]) -> Dict:
    """
    Produces a summary from a session log and commits it as an insight.
    Returns structured metadata aligned with interaction_summary.schema.json.
    """
    if not dialogue_log:
        return {"status": "empty", "user_id": user_id}

    user_lines = [turn["content"] for turn in dialogue_log if turn["role"] == "user"]
    ai_lines = [turn["content"] for turn in dialogue_log if turn["role"] == "eidolon"]

    main_theme = extract_theme(user_lines)
    key_response = ai_lines[-1] if ai_lines else "N/A"

    summary = {
        "user_id": user_id,
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "theme": main_theme,
        "key_insight": key_response,
        "reflection_count": len(user_lines),
        "emotional_tone": extract_emotional_summary(dialogue_log)
    }

    embed_insight(user_id, key_response, tags=[main_theme])
    return summary

def extract_theme(lines: List[str]) -> str:
    """
    Naive keyword extraction to simulate thematic tagging.
    """
    for line in lines[::-1]:
        lowered = line.lower()
        if "guilt" in lowered: return "guilt"
        if "shame" in lowered: return "shame"
        if "control" in lowered: return "control"
        if "fear" in lowered: return "fear"
        if "loss" in lowered: return "loss"
        if "father" in lowered or "mother" in lowered: return "family"
    return "reflection"

def extract_emotional_summary(log: List[Dict]) -> str:
    """
    Basic majority rule on emotional tags.
    """
    emotions = [entry.get("emotion", "neutral") for entry in log]
    return max(set(emotions), key=emotions.count)

# Example
if __name__ == "__main__":
    sample_log = [
        {"role": "user", "content": "I still carry guilt about the war.", "emotion": "guilt"},
        {"role": "eidolon", "content": "Let us name that guilt. Only then can we begin to release it.", "emotion": "calm"}
    ]
    print(summarize_session("witness_001", sample_log))
