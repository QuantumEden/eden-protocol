# api/services/dao_service.py
# Eden Protocol – DAO Proposal + Voting Logic

from datetime import datetime
from api.models.dao import DAOCreation, DAOEnforcementAction
import json
import os

DAO_REGISTRY = {}
VOTE_LOG = {}

USER_REGISTRY_PATH = os.path.join(os.path.dirname(__file__), "../../dao/user_registry.json")


def load_user_registry():
    if os.path.exists(USER_REGISTRY_PATH):
        with open(USER_REGISTRY_PATH, 'r') as f:
            return json.load(f)
    return {}


def save_user_registry(registry):
    with open(USER_REGISTRY_PATH, 'w') as f:
        json.dump(registry, f, indent=2)


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
            "voters": [],
            "enforcement_target": getattr(payload, "target_user", None),
            "enforcement_type": getattr(payload, "action_type", None)
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

        # Automatic enforcement check
        if proposal["enforcement_target"] and proposal["enforcement_type"]:
            total_votes = proposal["votes"]["yes"] + proposal["votes"]["no"]
            if total_votes >= 5 and proposal["votes"]["yes"] > proposal["votes"]["no"]:
                # Majority has voted yes
                action = DAOEnforcementAction(
                    target_user=proposal["enforcement_target"],
                    action_type=proposal["enforcement_type"],
                    initiated_by="DAO"
                )
                self.apply_enforcement_action(action)

        return {
            "message": f"Vote '{vote}' recorded",
            "proposal": proposal
        }

    def get_vote_history(self, user_id: str) -> list:
        return VOTE_LOG.get(user_id, [])

    def get_enforcement_status(self, user_id: str) -> dict:
        registry = load_user_registry()
        user = registry.get(user_id)
        if not user:
            return {"status": "active"}
        return {"status": user.get("status", "active")}

    def apply_enforcement_action(self, payload: DAOEnforcementAction) -> dict:
        registry = load_user_registry()
        registry[payload.target_user] = {
            "status": payload.action_type,
            "updated_at": datetime.utcnow().isoformat() + "Z",
            "source": payload.initiated_by
        }
        save_user_registry(registry)
        return {
            "message": f"User {payload.target_user} marked as {payload.action_type}"
        }
