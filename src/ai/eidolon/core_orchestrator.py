# src/ai/eidolon/core_orchestrator.py
"""
Eidolon Core Orchestrator – Eden Protocol

Primary control unit for AI-driven therapeutic orchestration. This module:
- Routes user input to the appropriate therapeutic agents
- Applies Ritual Safeguard Layer checks
- Interfaces with OpenAI GPT-4o for therapeutic dialogue
- Ensures session continuity via memory and emotion sync
"""

import openai
from src.config.api_keys import keys
from src.ai.eidolon.agent_router import route_to_agent
from src.ai.eidolon.session_tracker import SessionTracker
from src.ai.eidolon.hooks.memory_adapter import sync_memory
from src.ai.support.crisis_detector import detect_crisis_keywords
from src.ai.support.emotion_advisor import recommend_tone
from src.ai.eidolon.personality_config import get_persona

# Initialize session and OpenAI API client
session_tracker = SessionTracker()
client = openai.OpenAI(api_key=keys.OPENAI_API_KEY)

def call_gpt4o(prompt: str, persona: str, tone: str) -> str:
    """
    Sends a prompt to GPT-4o and returns the generated therapeutic response.
    Updated to use OpenAI API v1.0+
    """
    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {
                    "role": "system",
                    "content": (
                        f"You are Eidelon, a therapeutic AI trained in CBT, Logotherapy, "
                        f"and Jungian psychology. Respond with a {tone} tone and a {persona} perspective."
                    )
                },
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"⚠️ AI error: {str(e)}"

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

    # === Backup with GPT-4o if fallback is triggered ===
    if agent_result.get("fallback_to_gpt", False):
        ai_response = call_gpt4o(message, persona, tone_suggestion)
        agent_result = {
            "response": ai_response,
            "agent": "gpt-4o"
        }

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
