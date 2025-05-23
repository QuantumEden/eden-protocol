# Group Vote Handler – Eden Protocol DAO Ritual Voting Engine
# Symbolic proposal and truth-weighted voice system for group ritual governance
# Includes: Suspension/Ban Logic, Ritual Safeguard Layer, zkXP Commit Hash Integration

import hashlib
from datetime import datetime
from typing import Dict, List, Optional

MIN_PROPOSAL_LEVEL = 7
SOULFORM_WEIGHT_BONUS = 1.5

class GroupVoteHandler:
    def __init__(self):
        self.vote_log: List[Dict] = []

    def generate_proposal_id(self, group_id: str, proposal_title: str) -> str:
        seed = f"{group_id}_{proposal_title}_{datetime.utcnow().isoformat()}"
        return hashlib.sha256(seed.encode("utf-8")).hexdigest()

    def submit_proposal(
        self,
        group_id: str,
        proposal_title: str,
        proposal_type: str,
        proposed_by: str,
        merit_level: int,
        soulform_id: Optional[str] = None,
        ritual_required: bool = False
    ) -> Dict:
        if merit_level < MIN_PROPOSAL_LEVEL:
            return {
                "status": "rejected",
                "reason": "Proposer does not meet minimum MeritCoin level"
            }

        proposal_id = self.generate_proposal_id(group_id, proposal_title)
        proposal = {
            "proposal_id": proposal_id,
            "group_id": group_id,
            "title": proposal_title,
            "type": proposal_type,
            "status": "pending",
            "proposed_by": proposed_by,
            "merit_threshold": MIN_PROPOSAL_LEVEL,
            "created_at": datetime.utcnow().isoformat() + "Z",
            "soulform_required": soulform_id,
            "ritual_required": ritual_required,
            "ritual_verified": False,
            "zkxp_commit_hash": None,
            "suspension_list": [],
            "ban_list": [],
            "votes": {}
        }
        self.vote_log.append(proposal)
        return proposal

    def cast_vote(
        self,
        proposal_id: str,
        user_id: str,
        vote: bool,
        merit_level: int,
        soulform_id: Optional[str] = None,
        is_suspended: bool = False,
        is_banned: bool = False
    ) -> bool:
        for proposal in self.vote_log:
            if proposal["proposal_id"] == proposal_id:
                if user_id in proposal.get("ban_list", []) or is_banned:
                    return False  # Banned users may not vote
                if user_id in proposal.get("suspension_list", []) or is_suspended:
                    return False  # Suspended users may not vote
                if user_id in proposal["votes"]:
                    return False  # Prevent double voting

                weight = merit_level
                if soulform_id and soulform_id == proposal.get("soulform_required"):
                    weight *= SOULFORM_WEIGHT_BONUS

                proposal["votes"][user_id] = {
                    "vote": vote,
                    "weight": round(weight, 2),
                    "soulform": soulform_id,
                    "timestamp": datetime.utcnow().isoformat() + "Z"
                }
                return True
        return False

    def tally_votes(
        self,
        proposal_id: str,
        zkxp_commit_hash: Optional[str] = None,
        ritual_verified: bool = False
    ) -> Dict:
        for proposal in self.vote_log:
            if proposal["proposal_id"] == proposal_id:
                votes = proposal["votes"]
                yes = sum(v["weight"] for v in votes.values() if v["vote"])
                no = sum(v["weight"] for v in votes.values() if not v["vote"])

                proposal["zkxp_commit_hash"] = zkxp_commit_hash
                proposal["ritual_verified"] = ritual_verified

                if proposal["ritual_required"] and not ritual_verified:
                    proposal["status"] = "rejected"
                    return {
                        "result": "ritual unverified",
                        "yes_weight": round(yes, 2),
                        "no_weight": round(no, 2),
                        "total_votes": len(votes)
                    }

                if yes + no == 0:
                    proposal["status"] = "no quorum"
                    return {
                        "result": "no quorum",
                        "yes_weight": 0,
                        "no_weight": 0,
                        "total_votes": 0
                    }

                outcome = "approved" if yes > no else "rejected"
                proposal["status"] = outcome

                return {
                    "result": outcome,
                    "yes_weight": round(yes, 2),
                    "no_weight": round(no, 2),
                    "total_votes": len(votes)
                }
        return {"result": "not found"}

    def get_proposal_status(self, proposal_id: str) -> str:
        for proposal in self.vote_log:
            if proposal["proposal_id"] == proposal_id:
                return proposal["status"]
        return "not found"

    def get_vote_log(self) -> List[Dict]:
        return self.vote_log
