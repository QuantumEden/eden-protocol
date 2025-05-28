# src/ai/council/synthesis.py

"""
Council Synthesis – Insight Aggregator for Eden Protocol

Combines symbolic insights from multiple psychological models
into a unified response. Eidelon uses this to balance tone,
precision, and depth depending on the mode of interpretation.
"""

from typing import Dict, List


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
