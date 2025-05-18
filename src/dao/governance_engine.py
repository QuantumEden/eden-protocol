# src/dao/governance_engine.py
# Governance Engine – DAO Voting Logic for Eden Protocol

from typing import List, Dict, Any
from datetime import datetime
from uuid import uuid4

# === Step 1: Define DAO Proposal Creation ===
def create_proposal(title: str, description: str, proposer_id: str) -> Dict[str, Any]:
    return {
        "id": f"DAO-{uuid4().hex[:8]}",
        "title": title,
        "description": description,
        "proposed_by": proposer_id,
        "votes_for": 0,
        "votes_against": 0,
        "voter_log": {},
        "created_at": datetime.utcnow().isoformat() + "Z",
        "status": "open"
    }

# === Step 2: Cast Vote with XP-weighted Influence ===
def cast_vote(proposal: Dict[str, Any], user_id: str, vote: str, weight: int) -> None:
    if proposal["status"] != "open":
        return  # No voting allowed on closed proposals

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

# === Step 3: Finalize Proposal Outcome ===
def close_proposal(proposal: Dict[str, Any]) -> Dict[str, Any]:
    proposal["status"] = "closed"
    outcome = "passed" if proposal["votes_for"] > proposal["votes_against"] else "rejected"
    proposal["outcome"] = outcome
    proposal["closed_at"] = datetime.utcnow().isoformat() + "Z"
    return proposal

# === Optional: Standalone Simulation ===
if __name__ == "__main__":
    print("\n🗳️ DAO Proposal Simulation\n")

    prop = create_proposal(
        "Sanctify Shadow Grove",
        "Create lunar sanctum for users completing trauma reflection quests.",
        "seer_alch_001"
    )

    cast_vote(prop, "seer_alch_001", "for", 10)
    cast_vote(prop, "guardian_022", "against", 5)
    cast_vote(prop, "healer_echo_033", "for", 7)

    finalized = close_proposal(prop)

    import json
    print(json.dumps(finalized, indent=2))
