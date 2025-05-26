"""
Eidolon Agent Router – Eden Protocol

Directs user input to the most appropriate therapeutic agent
based on message intent, user profile, and session context.
"""

from src.ai.council.freudian import freudian_analysis
from src.ai.council.jungian import jungian_reflection
from src.ai.council.cbt import cbt_reframe
from src.ai.council.dbt import dbt_balance
from src.ai.council.logotherapy import logotherapy_probe
from src.ai.council.psychiatrist import emergency_psy_eval

def route_to_agent(user_id: str, message: str, context: str, tone: str, persona: dict) -> dict:
    """
    Routes a message to the correct therapeutic agent.
    Selection is based on heuristics, context tags, and session tone.
    Returns a response and agent type, with fallback_to_gpt flag if no symbolic agent matched.
    """
    lowered = message.lower()

    if "meaning" in lowered or "purpose" in lowered:
        response = logotherapy_probe(user_id, message, context)
        agent = "Logotherapy"
        fallback = False

    elif "dream" in lowered or "archetype" in lowered:
        response = jungian_reflection(user_id, message, context)
        agent = "Jungian"
        fallback = False

    elif "trauma" in lowered or "childhood" in lowered:
        response = freudian_analysis(user_id, message, context)
        agent = "Freudian"
        fallback = False

    elif "distorted thought" in lowered or "catastrophizing" in lowered or "irrational" in lowered:
        response = cbt_reframe(user_id, message, context)
        agent = "CBT"
        fallback = False

    elif "trigger" in lowered or "emotional regulation" in lowered:
        response = dbt_balance(user_id, message, context)
        agent = "DBT"
        fallback = False

    elif "medication" in lowered or "diagnose me" in lowered or "psychiatrist" in lowered:
        response = emergency_psy_eval(user_id, message, context)
        agent = "Psychiatrist"
        fallback = False

    else:
        response = "🤖 No symbolic route matched. Handing off to GPT core orchestrator."
        agent = "Unrouted"
        fallback = True

    return {
        "response": response,
        "agent": agent,
        "fallback_to_gpt": fallback
    }

# Test routing (manual override)
if __name__ == "__main__":
    out = route_to_agent(
        user_id="demo007",
        message="I think my childhood trauma is still affecting me.",
        context="The user disclosed fear around abandonment.",
        tone="calm",
        persona={"mbti": "INFJ"}
    )
    print(out)
