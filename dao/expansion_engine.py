# /dao/expansion_engine.py

import uuid
import datetime

# Simulated proposal ledger
proposals = []

# Create a new DAO proposal
def create_proposal(title: str, description: str) -> dict:
    proposal = {
        "id": str(uuid.uuid4()),
        "title": title,
        "description": description,
        "timestamp": datetime.datetime.utcnow().isoformat(),
        "votes_for": 0,
        "votes_against": 0,
        "voters": {}
    }
    proposals.append(proposal)
    return proposal

# Cast a symbolic vote on a DAO proposal
def vote(proposal_id: str, user_id: str, xp: int, vote: str):
    for p in proposals:
        if p["id"] == proposal_id:
            if user_id in p["voters"]:
                return False  # prevent double voting
            p["voters"][user_id] = vote
            if vote == "yes":
                p["votes_for"] += xp
            elif vote == "no":
                p["votes_against"] += xp
            return True
    return False

# Determine proposal outcome
def finalize(proposal_id: str) -> str:
    for p in proposals:
        if p["id"] == proposal_id:
            if p["votes_for"] > p["votes_against"]:
                return "passed"
            elif p["votes_for"] < p["votes_against"]:
                return "failed"
            else:
                return "tie"
    return "not found"

# Example usage
def simulate():
    prop = create_proposal("Deploy Eden Oracle", "Enable the mythic AI to guide users in quest selection.")
    print(f"Created Proposal: {prop['title']} (ID: {prop['id']})")
    vote(prop["id"], "user001", 540, "yes")
    vote(prop["id"], "user002", 200, "no")
    result = finalize(prop["id"])
    print(f"Proposal Result: {result}")

if __name__ == "__main__":
    simulate()
