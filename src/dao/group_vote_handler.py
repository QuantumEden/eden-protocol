# 🔐 Group Vote Handler – Symbolic DAO Ritual Voting Engine

import random
import hashlib
from datetime import datetime


class GroupVoteHandler:
    def __init__(self):
        self.vote_log = []

    def generate_proposal_id(self, group_id: str, proposal_title: str) -> str:
        """
        Generates a unique hash ID for a group proposal.
        """
        seed = f"{group_id}_{proposal_title}_{datetime.utcnow().isoformat()}"
        return hashlib.sha256(seed.encode("utf-8")).hexdigest()

    def submit_proposal(self, group_id: str, proposal_title: str, proposal_type: str, proposed_by: str) -> dict:
        """
        Submits a new symbolic group proposal.
        """
        proposal_id = self.generate_proposal_id(group_id, proposal_title)
        proposal = {
            "proposal_id": proposal_id,
            "group_id": group_id,
            "title": proposal_title,
            "type": proposal_type,
            "votes": {},
            "status": "pending",
            "proposed_by": proposed_by,
            "created_at": datetime.utcnow().isoformat()
        }
        self.vote_log.append(proposal)
        return proposal

    def cast_vote(self, proposal_id: str, user_id: str, vote: bool) -> bool:
        """
        Casts a vote on a given proposal (True = Yes, False = No).
        """
        for proposal in self.vote_log:
            if proposal["proposal_id"] == proposal_id:
                if user_id in proposal["votes"]:
                    return False  # already voted
                proposal["votes"][user_id] = vote
                return True
        return False

    def tally_votes(self, proposal_id: str) -> dict:
        """
        Tally votes and update proposal status.
        """
        for proposal in self.vote_log:
            if proposal["proposal_id"] == proposal_id:
                votes = list(proposal["votes"].values())
                yes = votes.count(True)
                no = votes.count(False)
                total = yes + no
                if total == 0:
                    return {"result": "no quorum", "yes": 0, "no": 0}
                if yes > no:
                    proposal["status"] = "approved"
                    result = "approved"
                else:
                    proposal["status"] = "rejected"
                    result = "rejected"
                return {"result": result, "yes": yes, "no": no}
        return {"result": "not found"}

    def get_proposal_status(self, proposal_id: str) -> str:
        """
        Returns the current status of a proposal.
        """
        for proposal in self.vote_log:
            if proposal["proposal_id"] == proposal_id:
                return proposal["status"]
        return "not found"

    def get_vote_log(self) -> list:
        """
        Returns all recorded group proposals and votes.
        """
        return self.vote_log
