# tests/unit/synthesis_priority_test.py
# Ensures Psychiatrist insights override others when escalation is high

import pytest
from src.ai.council.synthesis import synthesize_responses

def test_psychiatrist_priority_overrides():
    inputs = {
        "CBT": {"success": True, "message": "Try reframing your thoughts."},
        "Jung": {"success": True, "message": "Your dreams reveal archetypal tension."},
        "Psychiatrist": {"success": True, "message": "⚠️ Crisis detected, immediate support required.", "escalation": "high"}
    }

    result = synthesize_responses(inputs, mode="clinical")
    assert result["success"]
    assert result["insight"][0]["source"] == "Psychiatrist"
    assert "Crisis" in result["narrative"]
