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

# Bootstrap Daemon first to ensure dynamic import resolution is active
from src.ai.diagnostic.daemon_bootstrap import bootstrap_daemon
bootstrap_daemon()

from src.ai.diagnostic.daemon import run_diagnostic_daemon
from src.ai.diagnostic.sandbox_executor import try_symbolic_execution
from src.ai.diagnostic.report_adapter import log_sandbox_result

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

    try:
        # === 1. Run symbolic diagnostics (Daemon) ===
        flags = run_diagnostic_daemon(user_id)
        symbolic_feedback = []
        if symbolic_plan:
            symbolic_feedback.append(try_symbolic_execution(symbolic_plan, context, user_id=user_id))

        # === 2. Psychiatric triage layer ===
        try:
            if message:
                from src.ai.council.psychiatrist import emergency_psy_eval, select_council_agents
                triage_result = emergency_psy_eval(user_id, message)
                agent_ids = select_council_agents(triage_result["tags"])
            else:
                triage_result = {
                    "response": "No message provided. Defaulting to introspective mode.",
                    "tags": "",
                    "escalation": "none"
                }
                agent_ids = ["freudian", "jungian"]
        except ImportError as e:
            from src.ai.diagnostic.import_hook import ImportErrorHandler
            insight = ImportErrorHandler.notify_eidelon("psychiatric_triage", str(e))
            triage_result = {
                "response": insight or "Import error in psychiatric system. Defaulting to introspective mode.",
                "tags": "",
                "escalation": "none"
            }
            agent_ids = ["freudian", "jungian"]

        # === 3. Summon Council insights ===
        try:
            from src.ai.council.registry import get_council_insights
            council_insights = get_council_insights(user_id=user_id, context=context, agent_ids=agent_ids)
        except ImportError as e:
            from src.ai.diagnostic.import_hook import ImportErrorHandler
            insight = ImportErrorHandler.notify_eidelon("council_insights", str(e))
            council_insights = {
                "Jung": insight or "The collective unconscious reveals patterns even in system failures."
            }

        # === 4. Synthesize final message ===
        try:
            from src.ai.council.synthesis import synthesize_council_response
            final_message = synthesize_council_response(flags, council_insights, symbolic_feedback)
        except ImportError as e:
            final_message = council_insights.get(
                "Jung",
                "Reflection continues even when synthesis pathways are disrupted."
            )

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

    except Exception as e:
        # Global fallback if even Eidelon invocation fails
        error_message = f"Exception during Eidelon invocation: {str(e)}"
        try:
            from src.ai.council.jungian import jungian_reflection
            insight = jungian_reflection(
                user_id=user_id,
                message=error_message,
                context="system_error"
            )
        except Exception:
            insight = "Even in system disruption, consciousness persists. The shadow of error reveals the structure of intention."

        return {
            "user_id": user_id,
            "context": context,
            "flags": [],
            "psychiatry": {
                "response": "Error in psychiatric system",
                "tags": "",
                "escalation": "none"
            },
            "council": {"Jung": insight},
            "symbolic": [],
            "message": insight
        }

def generate_eidelon_insight(user_id: str, context: str = "general_insight", message: str = None) -> str:
    """
    Wrapper function for invoke_eidelon that simplifies the interface for main.py.

    Args:
        user_id (str): ID of the user seeking insight
        context (str, optional): Context for the insight generation. Defaults to "general_insight".
        message (str, optional): User message to analyze. Defaults to None.

    Returns:
        str: The synthesized insight message from Eidelon
    """
    result = invoke_eidelon(
        user_id=user_id,
        context=context,
        message=message
    )
    return result.get("message", "No insight available at this time.")

# 🔥 Optional CLI run
if __name__ == "__main__":
    output = invoke_eidelon(
        user_id="seer_beta",
        context="self_diagnostic",
        message="I’ve been having panic attacks and racing thoughts."
    )
    print("🪞 Final Introspective Message:\n", output["message"])
