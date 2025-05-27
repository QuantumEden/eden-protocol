# tests/integration/eidelon_response_test.py

"""
Integration Test – Eidelon Unified Response System

Tests if Eidelon can receive diagnostic flags from Daemon,
consult the AI Council, and produce a synthesized symbolic response.
"""

from src.eidelon.eidelon_core import generate_eidelon_insight

def test_eidelon_integration_response():
    """
    Simulates an introspection cycle from raw context input.
    """
    sample_context = {
        "user_id": "test_user_001",
        "user_input": "Why do I keep sabotaging myself in relationships?",
        "session_flags": ["emotional_volatility", "stagnation_loop"],
        "trait_profile": {
            "mbti": "INFJ",
            "iq": 132,
            "eq": 115,
            "moral": "care"
        }
    }

    result = generate_eidelon_insight(sample_context)
    print("\n🧠 Eidelon Response\n", result)

    assert isinstance(result, dict), "Expected response to be a dictionary"
    assert "reflection" in result, "Missing symbolic insight"
    assert "council" in result, "Missing council feedback"
    assert "daemon" in result, "Missing daemon flags"
    assert result["daemon"]["user_id"] == "test_user_001"
