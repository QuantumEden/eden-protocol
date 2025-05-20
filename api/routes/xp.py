# api/routes/xp.py
# Eden Protocol – XP + MeritCoin Endpoints

from fastapi import APIRouter, Depends
from api.dependencies import get_current_user
from api.models.user import User
from api.services.xp_service import XPService
from api.models.xp import XPCommit, XPDisclosure, XPModGrant

router = APIRouter(prefix="/api/xp", tags=["xp"])


@router.post("/{user_id}/commit")
def commit_xp(user_id: str, payload: XPCommit, current_user: User = Depends(get_current_user)):
    return XPService().commit(user_id, payload)


@router.post("/{user_id}/disclosure")
def apply_disclosure_reward(user_id: str, payload: XPDisclosure, current_user: User = Depends(get_current_user)):
    return XPService().apply_disclosure_reward(user_id, payload)


@router.post("/{user_id}/validate/mod")
def grant_xp_mod(user_id: str, payload: XPModGrant, current_user: User = Depends(get_current_user)):
    return XPService().mod_grant(user_id, payload, mod_id=current_user.username)
