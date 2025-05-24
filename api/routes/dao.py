# api/routes/dao.py
# Eden Protocol – DAO Governance Endpoints

from fastapi import APIRouter, Depends
from api.dependencies import get_current_user
from api.models.user import User
from api.models.dao import DAOCreation, DAOVoteRequest, DAOEnforcementAction
from api.services.dao_service import DAOService

router = APIRouter(prefix="/api/dao", tags=["dao"])


@router.get("/proposals")
def get_all_proposals(current_user: User = Depends(get_current_user)):
    return DAOService().get_all_proposals()


@router.get("/proposals/{proposal_id}")
def get_specific_proposal(proposal_id: str, current_user: User = Depends(get_current_user)):
    return DAOService().get_proposal(proposal_id)


@router.post("/proposals")
def create_proposal(payload: DAOCreation, current_user: User = Depends(get_current_user)):
    return DAOService().create_proposal(current_user.username, payload)


@router.post("/proposals/{proposal_id}/vote")
def vote_on_proposal(proposal_id: str, payload: DAOVoteRequest, current_user: User = Depends(get_current_user)):
    return DAOService().submit_vote(proposal_id, current_user.username, payload.vote)


@router.get("/user/{user_id}/votes")
def get_user_vote_history(user_id: str, current_user: User = Depends(get_current_user)):
    return DAOService().get_vote_history(user_id)


@router.get("/user/{user_id}/enforcement")
def get_user_enforcement_status(user_id: str, current_user: User = Depends(get_current_user)):
    return DAOService().get_enforcement_status(user_id)


@router.post("/enforcement/apply")
def apply_enforcement_action(payload: DAOEnforcementAction, current_user: User = Depends(get_current_user)):
    """
    This should only be called by the system after DAO vote passes,
    but route is exposed here for testing or moderation overrides.
    """
    return DAOService().apply_enforcement_action(payload)
