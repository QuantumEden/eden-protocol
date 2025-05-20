# api/services/dao_service.py
# Eden Protocol – DAO Proposal + Voting Logic

from datetime import datetime
from api.models.dao import DAOCreation

# Temporary in-memory DAO ledger
DAO_REGISTRY = {}
VOTE_LOG = {}


class DAOService:

    def get_all_proposals(self) -> list:
        return list(DAO_REGISTRY.values())

    def get_proposal(self, proposal_id: str) -> dict:
        return DAO_REGISTRY.get(proposal_id, {"error": "Proposal not found"})

    def create_proposal(self, author_id: str, payload: DAOCreation) -> dict:
        proposal_id = f"prop_{len(DAO_REGISTRY) + 1:03d}"
        entry = {
            "id": proposal_id,
            "title": payload.title,
            "description": payload.description,
            "created_by": author_id,
            "created_at": datetime.utcnow().isoformat() + "Z",
            "votes": {"yes": 0, "no": 0},
            "voters": []
        }
        DAO_REGISTRY[proposal_id] = entry
        return {
            "message": "Proposal created",
            "proposal": entry
        }

    def submit_vote(self, proposal_id: str, user_id: str, vote: str) -> dict:
        proposal = DAO_REGISTRY.get(proposal_id)
        if not proposal:
            return {"error": "Proposal not found"}

        if user_id in proposal["voters"]:
            return {"error": "User has already voted"}

        if vote not in ["yes", "no"]:
            return {"error": "Invalid vote option"}

        proposal["votes"][vote] += 1
        proposal["voters"].append(user_id)

        VOTE_LOG.setdefault(user_id, []).append({
            "proposal_id": proposal_id,
            "vote": vote,
            "timestamp": datetime.utcnow().isoformat() + "Z"
        })

        return {
            "message": f"Vote '{vote}' recorded",
            "proposal": proposal
        }

    def get_vote_history(self, user_id: str) -> list:
        return VOTE_LOG.get(user_id, [])
