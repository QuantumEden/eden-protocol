"""
Eidolon Core Orchestrator – Eden Protocol

Primary control unit for AI-driven therapeutic orchestration. This module:
- Routes user input to the appropriate therapeutic agents
- Applies Ritual Safeguard Layer checks
- Ensures session continuity via memory and emotion sync
"""

from src.ai.eidolon.agent_router import route_to_agent
from src.ai.eidolon.session_tracker import SessionTracker
from src.ai.eidolon.hooks.memory_adapter import sync_memory
from src.ai.support.crisis_detector import detect_crisis_keywords
from src.ai.support.emotion_advisor import recommend_tone
from src.ai.eidolon.personality_config import get_persona

# Initialize state
session_tracker = SessionTracker()

def process_user_input(user_id: str, message: str, metadata: dict) -> dict:
    """
    Handles user input, routes to therapeutic agent, and returns AI response.
    Embeds etiquette enforcement and mood-aware orchestration logic.
    """
    # === Ritual Safeguard: Red Flag Scan ===
    if detect_crisis_keywords(message):
        session_tracker.flag_risk(user_id, level="high", trigger="crisis_phrase")
        return {
            "response": "🛑 Crisis indicators detected. A guardian has been notified.",
            "escalated": True
        }

    # === Retrieve Persona and Recommend Tone ===
    persona = get_persona(user_id)
    tone_suggestion = recommend_tone(user_id)

    # === Synchronize Memory ===
    session_context = sync_memory(user_id)

    # === Route to Therapeutic Agent ===
    agent_result = route_to_agent(
        user_id=user_id,
        message=message,
        context=session_context,
        tone=tone_suggestion,
        persona=persona
    )

    # === Update Session Log ===
    session_tracker.log_interaction(user_id, message, agent_result["response"])

    return {
        "response": agent_result["response"],
        "agent": agent_result["agent"],
        "persona": persona,
        "tone": tone_suggestion
    }

# Optional test harness
if __name__ == "__main__":
    test_output = process_user_input(
        user_id="test_user",
        message="I feel like I'm falling apart.",
        metadata={"mbti": "INFJ", "soulform": "phoenix"}
    )
    print(test_output)
