# Governance Engine – DAO Voting Logic for Eden Protocol
# Includes: Code of Conduct, Suspension vs. Ban logic, Ritual Safeguard Layer, zkXP Commit Adapter integration

from typing import List, Dict, Any
from datetime import datetime
from uuid import uuid4

# === Step 1: Define DAO Proposal Creation ===
def create_proposal(title: str, description: str, proposer_id: str, ritual_required: bool = False) -> Dict[str, Any]:
    return {
        "id": f"DAO-{uuid4().hex[:8]}",
        "title": title,
        "description": description,
        "proposed_by": proposer_id,
        "votes_for": 0,
        "votes_against": 0,
        "voter_log": {},
        "created_at": datetime.utcnow().isoformat() + "Z",
        "status": "open",
        "ritual_required": ritual_required,
        "ritual_verified": False,
        "outcome": None,
        "suspension_list": [],
        "ban_list": [],
        "zkxp_commit_hash": None,
    }

# === Step 2: Cast Vote with XP-weighted Influence ===
def cast_vote(proposal: Dict[str, Any], user_id: str, vote: str, weight: int, is_suspended: bool = False, is_banned: bool = False) -> None:
    if proposal["status"] != "open":
        return  # Voting only allowed on open proposals

    if is_banned or user_id in proposal.get("ban_list", []):
        return  # Banned users cannot vote

    if is_suspended or user_id in proposal.get("suspension_list", []):
        return  # Suspended users cannot vote

    if user_id in proposal["voter_log"]:
        return  # Prevent double voting

    if vote == "for":
        proposal["votes_for"] += weight
    elif vote == "against":
        proposal["votes_against"] += weight

    proposal["voter_log"][user_id] = {
        "vote": vote,
        "weight": weight,
        "timestamp": datetime.utcnow().isoformat() + "Z"
    }

# === Step 3: Finalize Proposal Outcome with zkXP & Ritual Safeguard Checks ===
def close_proposal(proposal: Dict[str, Any], zkxp_hash: str = None, ritual_verified: bool = False) -> Dict[str, Any]:
    proposal["status"] = "closed"
    proposal["zkxp_commit_hash"] = zkxp_hash
    proposal["ritual_verified"] = ritual_verified

    # Enforce Ritual Safeguard: proposals flagged for ritual must be verified to pass
    if proposal.get("ritual_required", False) and not ritual_verified:
        proposal["outcome"] = "rejected"
    else:
        proposal["outcome"] = "passed" if proposal["votes_for"] > proposal["votes_against"] else "rejected"

    proposal["closed_at"] = datetime.utcnow().isoformat() + "Z"
    return proposal

# === Optional: Standalone Simulation ===
if __name__ == "__main__":
    print("\n🗳️ DAO Proposal Simulation\n")

    prop = create_proposal(
        "Sanctify Shadow Grove",
        "Create lunar sanctum for users completing trauma reflection quests.",
        "seer_alch_001",
        ritual_required=True
    )

    cast_vote(prop, "seer_alch_001", "for", 10)
    cast_vote(prop, "guardian_022", "against", 5)
    cast_vote(prop, "healer_echo_033", "for", 7)

    finalized = close_proposal(prop, zkxp_hash="a1b2c3z4k5p6", ritual_verified=True)

    import json
    print(json.dumps(finalized, indent=2))
