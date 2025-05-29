"""
Council Registry – Voice Index for Eden Protocol

Maps available therapeutic and psychoanalytic perspectives to their
interpretation functions. Used by Eidelon to summon insights from
various modalities as facets of a unified internal council.
"""

from typing import List, Dict
from .cbt import interpret as cbt_perspective
from .dbt import interpret as dbt_perspective
from .jungian import interpret as jung_perspective
from .logotherapy import interpret as logotherapy_perspective
from .freudian import interpret as freudian_perspective
from .psychiatrist import emergency_psy_eval as psychiatrist_triage  # updated routing

COUNCIL_REGISTRY = {
    "Psychiatrist": psychiatrist_triage,  # triage handler has final authority
    "CBT": cbt_perspective,
    "DBT": dbt_perspective,
    "Jung": jung_perspective,
    "Logotherapy": logotherapy_perspective,
    "Freud": freudian_perspective
}

def get_council_insights(user_id: str, context: str, agent_ids: List[str]) -> Dict[str, str]:
    """
    Gathers insights from selected council agents based on their expertise.

    Args:
        user_id (str): ID of the user seeking insights
        context (str): Current context or topic for analysis
        agent_ids (List[str]): List of agent identifiers to consult

    Returns:
        Dict[str, str]: Mapping of agent names to their insights
    """
    insights = {}
    message = f"Seeking insight on {context}" if context else "Seeking general insight"

    for agent_id in agent_ids:
        key = agent_id.lower()
        if key in ["freud", "freudian"]:
            insights["Freudian"] = COUNCIL_REGISTRY["Freud"](user_id, message, context)
        elif key in ["jung", "jungian"]:
            insights["Jungian"] = COUNCIL_REGISTRY["Jung"](user_id, message, context)
        elif key == "cbt":
            insights["CBT"] = COUNCIL_REGISTRY["CBT"](user_id, message, context)
        elif key == "dbt":
            insights["DBT"] = COUNCIL_REGISTRY["DBT"](user_id, message, context)
        elif key == "logotherapy":
            insights["Logotherapy"] = COUNCIL_REGISTRY["Logotherapy"](user_id, message, context)

    if not insights:
        insights["Freudian"] = COUNCIL_REGISTRY["Freud"](user_id, message, context)
        insights["Jungian"] = COUNCIL_REGISTRY["Jung"](user_id, message, context)

    return insights
