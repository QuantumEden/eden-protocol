# src/eidelon/eidelon_core.py

"""
Eidelon Core – Unified Introspective Response System

This is the central orchestration module that harmonizes:
- Daemon (symbolic diagnostics)
- Council (cognitive perspectives)
- Symbolic runtime outputs

It acts as the reflective voice of the Eden Protocol.
"""

from typing import Optional, Dict, List

from src.ai.diagnostic.daemon import run_diagnostic_daemon, get_latest_flags
from src.ai.council.registry import get_council_insights
from src.ai.council.synthesis import synthesize_council_response
from src.ai.diagnostic.sandbox_executor import try_symbolic_execution
from src.ai.diagnostic.report_adapter import log_sandbox_result


def invoke_eidelon(user_id: str, context: str, symbolic_plan: Optional[str] = None) -> Dict:
    """
    Master invocation of the Eidelon system. Integrates Daemon diagnostics,
    Council perspectives, and optional symbolic repair attempts.

    Args:
        user_id (str): ID of the user under introspection
        context (str): Area of the system under evaluation
        symbolic_plan (str, optional): Patch logic if available

    Returns:
        Dict: Unified insight report from the Eidelon system
    """
    print("🧠 Invoking Eidelon...")

    # 1. Run symbolic diagnostics (Daemon)
    flags = run_diagnostic_daemon(user_id)
    symbolic_feedback = []
    if symbolic_plan:
        symbolic_feedback.append(try_symbolic_execution(symbolic_plan, context, user_id=user_id))

    # 2. Summon insights from the Council (multimodal perspectives)
    council_insights = get_council_insights(user_id=user_id, context=context)

    # 3. Synthesize a response (blended conscious voice)
    final_message = synthesize_council_response(flags, council_insights, symbolic_feedback)

    # 4. Report and return
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
        "council": council_insights,
        "symbolic": symbolic_feedback,
        "message": final_message
    }


# 🔥 Optional CLI run
if __name__ == "__main__":
    output = invoke_eidelon("seer_beta", context="self_diagnostic")
    print("🪞 Final Introspective Message:\n", output["message"])
