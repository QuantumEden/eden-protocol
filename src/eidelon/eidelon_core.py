"""
Eidelon Core – Unified Introspective Response System

This is the central orchestration module that harmonizes:
- Daemon (symbolic diagnostics)
- Council (cognitive perspectives)
- Psychiatrist (oversight and triage)
- Symbolic runtime outputs

It acts as the reflective voice of the Eden Protocol.
"""

from typing import Optional, Dict, List

from src.ai.diagnostic.daemon import run_diagnostic_daemon, get_latest_flags
from src.ai.diagnostic.sandbox_executor import try_symbolic_execution
from src.ai.diagnostic.report_adapter import log_sandbox_result

from src.ai.council.registry import get_council_insights
from src.ai.council.synthesis import synthesize_council_response
from src.ai.council.psychiatrist import emergency_psy_eval, select_council_agents


def invoke_eidelon(user_id: str, context: str, symbolic_plan: Optional[str] = None, message: Optional[str] = None) -> Dict:
    """
    Master invocation of the Eidelon system. Integrates Daemon diagnostics,
    Psychiatric triage, Council perspectives, and symbolic repair feedback.

    Args:
        user_id (str): ID of the user under introspection
        context (str): Area of the system under evaluation
        symbolic_plan (str, optional): Patch logic if available
        message (str, optional): User input for psychiatric triage

    Returns:
        Dict: Unified insight report from the Eidelon system
    """
    print("🧠 Invoking Eidelon...")

    # === 1. Run symbolic diagnostics (Daemon) ===
    flags = run_diagnostic_daemon(user_id)
    symbolic_feedback = []
    if symbolic_plan:
        symbolic_feedback.append(try_symbolic_execution(symbolic_plan, context, user_id=user_id))

    # === 2. Psychiatric triage layer ===
    if message:
        triage_result = emergency_psy_eval(user_id, message)
        agent_ids = select_council_agents(triage_result["tags"])
    else:
        triage_result = {"response": "No message provided. Defaulting to introspective mode.", "tags": "", "escalation": "none"}
        agent_ids = ["freudian", "jungian"]  # Default

    # === 3. Summon Council insights from selected agents ===
    council_insights = get_council_insights(user_id=user_id, context=context, agent_ids=agent_ids)

    # === 4. Synthesize final message ===
    final_message = synthesize_council_response(flags, council_insights, symbolic_feedback)

    # === 5. Report ===
    log_sandbox_result(
        success=True,
        context="Eidelon Invocation",
        message=final_message,
        symbol="harmonized_consciousness"
    )

    return {
        "user_id": user_id,
        "context": context,
        "flags": flags,
        "psychiatry": triage_result,
        "council": council_insights,
        "symbolic": symbolic_feedback,
        "message": final_message
    }


# 🔥 Optional CLI run
if __name__ == "__main__":
    output = invoke_eidelon(
        user_id="seer_beta",
        context="self_diagnostic",
        message="I’ve been having panic attacks and racing thoughts."
    )
    print("🪞 Final Introspective Message:\n", output["message"])
