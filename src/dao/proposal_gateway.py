"""
Proposal Gateway – Eden Protocol DAO Bridge

Converts symbolic user growth (quests, soulforms, reflections)
into structured DAO proposal drafts. Operates as a sacred bridge
between personal insight and civic transformation.

Author: Eden Council Compiler
"""

from datetime import datetime
from typing import Dict, List, Optional
from uuid import uuid4

# Threshold schema for automatic gating (can be used later for validation)
MODIFIER_THRESHOLDS = {
    "quest_completion": 1,
    "transformation": 3,
    "reflection": 2
}

def generate_dao_proposal_from_quest(user_id: str, quest_id: str, symbolic_payload: Dict) -> Dict:
    """
    Converts a completed symbolic quest into a DAO mod proposal.

    Args:
        user_id (str): The user submitting the proposal
        quest_id (str): The ID or title of the symbolic quest
        symbolic_payload (Dict): The full quest object returned from the engine

    Returns:
        Dict: DAO proposal dictionary
    """
    title = f"Integrate Quest: '{symbolic_payload.get('title', quest_id)}'"
    description = (
        f"User `{user_id}` completed the symbolic quest `{quest_id}`, titled '{symbolic_payload.get('title', 'Untitled')}'.\n\n"
        f"Proposal: Integrate this transformation into the DAO's core ritual layer or mod registry.\n"
        f"Suggested Impact Zone: `{symbolic_payload.get('impact_zone', 'tree_trait')}`\n"
        f"Alignment: `{symbolic_payload.get('sacred_path', 'Undeclared')}`"
    )

    return {
        "proposal_id": f"mod-{uuid4().hex[:8]}",
        "source_type": "QUEST",
        "title": title,
        "description": description,
        "proposed_by": user_id,
        "type": "MOD_PROPOSAL",
        "xp_required": 500,
        "truth_integrity_required": 70,
        "status": "pending",
        "soulbound": True,
        "submitted_at": datetime.utcnow().isoformat() + "Z",
        "sacred_path_alignment": symbolic_payload.get("sacred_path", "Undeclared"),
        "meta": {
            "impact_zone": symbolic_payload.get("impact_zone", "tree_trait"),
            "archetype": symbolic_payload.get("archetype", "Unknown"),
            "tags": symbolic_payload.get("symbolic_tags", [])
        },
        "vote_tally": {
            "approve": 0,
            "reject": 0,
            "abstain": 0
        },
        "zk_commit_hash": None
    }

def generate_dao_proposal_from_reflection(user_id: str, reflection_text: str, insight_tags: List[str]) -> Dict:
    """
    Converts a validated reflection into a DAO philosophical proposal.

    Args:
        user_id (str): User submitting the insight
        reflection_text (str): The full introspective message
        insight_tags (List[str]): Tags extracted from semantic memory or manual entry

    Returns:
        Dict: DAO proposal object
    """
    title = "Codify Inner Reflection as Ritual"
    description = (
        f"User `{user_id}` submitted a transformative reflection tagged with {insight_tags}.\n\n"
        "Proposal: Extract core insight and transcribe as a symbolic ritual, mod, or sacred axiom."
    )

    return {
        "proposal_id": f"insight-{uuid4().hex[:8]}",
        "source_type": "REFLECTION",
        "title": title,
        "description": description,
        "proposed_by": user_id,
        "type": "SHADOW_PROTOCOL",
        "xp_required": 700,
        "truth_integrity_required": 80,
        "status": "pending",
        "soulbound": True,
        "submitted_at": datetime.utcnow().isoformat() + "Z",
        "alignment_tags": insight_tags,
        "meta": {
            "text_excerpt": reflection_text[:120] + "..." if len(reflection_text) > 120 else reflection_text,
            "tags": insight_tags
        },
        "vote_tally": {
            "approve": 0,
            "reject": 0,
            "abstain": 0
        },
        "zk_commit_hash": None
    }

def generate_dao_proposal_from_transformation(user_id: str, soulform_id: str, token: Optional[str] = None) -> Dict:
    """
    Elevates a soulform transformation into an archetypal DAO upgrade proposal.

    Args:
        user_id (str): Initiating user
        soulform_id (str): Soulform that triggered transformation
        token (Optional[str]): Optional ritual seal or proof token

    Returns:
        Dict: DAO core ritual upgrade proposal
    """
    title = f"Elevate Soulform '{soulform_id}' to Archetype Tier"
    description = (
        f"User `{user_id}` achieved transformation into `{soulform_id}`.\n\n"
        "Proposal: Acknowledge this transformation as a systemic archetype, unlocking future quests or traits."
    )

    return {
        "proposal_id": f"trans-{uuid4().hex[:8]}",
        "source_type": "TRANSFORMATION",
        "title": title,
        "description": description,
        "proposed_by": user_id,
        "type": "CORE_UPGRADE",
        "xp_required": 1000,
        "truth_integrity_required": 90,
        "status": "pending",
        "soulbound": True,
        "submitted_at": datetime.utcnow().isoformat() + "Z",
        "transformation_id": soulform_id,
        "ritual_token": token or f"SOUL-{uuid4().hex[:6]}",
        "meta": {
            "soulform_id": soulform_id,
            "ritual_token": token or "auto"
        },
        "vote_tally": {
            "approve": 0,
            "reject": 0,
            "abstain": 0
        },
        "zk_commit_hash": None
    }
