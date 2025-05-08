# Governance Engine – DAO Voting Logic for Eden Protocol

from typing import List, Dict, Any

# Step 1: Define proposal schema
def create_proposal(title: str, description: str, proposer_id: str) -> Dict[str, Any]:
    return {
        "id": proposer_id + "_" + title.lower().replace(" ", "_"),
        "title": title,
        "description": description,
        "votes_for": 0,
        "votes_against": 0,
        "voter_log": {},
        "status": "open"
    }

# Step 2: Cast a vote with weighted XP influence
def cast_vote(proposal: Dict[str, Any], user_id: str, vote: str, weight: int) -> None:
    if proposal["status"] != "open":
        return
    if user_id in proposal["voter_log"]:
        return  # prevent double voting

    if vote == "for":
        proposal["votes_for"] += weight
    elif vote == "against":
        proposal["votes_against"] += weight

    proposal["voter_log"][user_id] = vote

# Step 3: Close the proposal and return result
def close_proposal(proposal: Dict[str, Any]) -> Dict[str, Any]:
    proposal["status"] = "closed"
    outcome = "passed" if proposal["votes_for"] > proposal["votes_against"] else "rejected"
    proposal["outcome"] = outcome
    return proposal

# Optional test routine
if __name__ == "__main__":
    prop = create_proposal("Fund VR Hardware", "Allocate resources to subsidize EdenQuest XR kits", "user123")
    cast_vote(prop, "user123", "for", 5)
    cast_vote(prop, "user999", "against", 3)
    cast_vote(prop, "user555", "for", 10)
    result = close_proposal(prop)

    print("\n=== DAO Proposal Outcome ===")
    for k, v in result.items():
        print(f"{k}: {v}")
