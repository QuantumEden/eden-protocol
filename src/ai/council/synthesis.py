# src/ai/council/synthesis.py

"""
Council Synthesis – Insight Aggregator for Eden Protocol

Combines symbolic insights from multiple psychological models
into a unified response. Eidelon uses this to balance tone,
precision, and depth depending on the mode of interpretation.
"""

from typing import Dict, List, Optional


def synthesize_responses(
    inputs: Dict[str, Dict],
    mode: str = "balanced"
) -> Dict:
    """
    Synthesizes multiple council insights into a single narrative.

    Args:
        inputs (dict): Map of perspective names to their response dicts
        mode (str): Strategy for combining responses
            • 'balanced' – even weighting across all sources
            • 'insightful' – prioritizes symbolic and long-form models (Jung, Logotherapy)
            • 'rational' – emphasizes logic-based models (CBT, DBT)
            • 'clinical' – privileges diagnostic/triage meta view

    Returns:
        dict: Synthesized interpretation
    """
    summary = []
    priority = []

    for name, response in inputs.items():
        if not response.get("success", True):
            continue

        content = response.get("message") or response.get("interpretation") or ""
        if not content:
            continue

        # Psychiatrist triage always takes lead if escalation exists
        if name == "Psychiatrist":
            escalation = response.get("escalation", "none")
            if escalation in ["medium", "high"]:
                return {
                    "success": True,
                    "mode": mode,
                    "escalation": escalation,
                    "insight": [{"source": name, "text": content}],
                    "narrative": content
                }

        # Mode-based prioritization
        if mode == "rational" and name in ["CBT", "DBT"]:
            priority.append((name, content))
        elif mode == "insightful" and name in ["Jung", "Logotherapy"]:
            priority.append((name, content))
        elif mode == "clinical" and name == "Psychiatrist":
            priority.insert(0, (name, content))  # Lead with clinical triage
        else:
            summary.append((name, content))

    # Fallback
    final = priority if priority else summary

    return {
        "success": True,
        "mode": mode,
        "insight": [
            {"source": name, "text": content} for name, content in final
        ],
        "narrative": " ".join(content for _, content in final)
    }


def synthesize_council_response(flags: dict, council_insights: dict, symbolic_feedback: Optional[List] = None) -> str:
    """
    Synthesizes diagnostic flags, council insights, and symbolic feedback into a unified response.
    
    This is the main integration point between Daemon diagnostics and Council perspectives,
    creating the final message that Eidelon delivers.
    
    Args:
        flags (dict): Diagnostic flags from the Daemon system
        council_insights (dict): Insights gathered from various council members
        symbolic_feedback (list, optional): Results from symbolic execution attempts
        
    Returns:
        str: Synthesized final message for user delivery
    """
    # Prepare inputs for the synthesize_responses function
    inputs = {}

    # Add council insights directly
    for agent_name, insight in council_insights.items():
        inputs[agent_name] = {"message": insight, "success": True}

    # Process diagnostic flags if present
    if flags:
        flag_message = "System diagnostics indicate: " + ", ".join(f"{k}={v}" for k, v in flags.items())
        inputs["Diagnostics"] = {"message": flag_message, "success": True}

    # Process symbolic feedback if present
    if symbolic_feedback:
        feedback_messages = []
        for feedback in symbolic_feedback:
            if isinstance(feedback, dict) and "message" in feedback:
                feedback_messages.append(feedback["message"])
            elif isinstance(feedback, str):
                feedback_messages.append(feedback)

        if feedback_messages:
            symbolic_message = "Symbolic execution results: " + " ".join(feedback_messages)
            inputs["Symbolic"] = {"message": symbolic_message, "success": True}

    # Use the existing synthesize_responses function to combine everything
    synthesis_result = synthesize_responses(inputs, mode="balanced")

    # Return the narrative as the final message
    return synthesis_result.get("narrative", "No insights available at this time.")
