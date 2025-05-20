# api/routes/soulform.py
# Eden Protocol – Soulform Metamorphosis Endpoints

from fastapi import APIRouter, Depends
from api.dependencies import get_current_user
from api.models.user import User
from api.services.soulform_service import SoulformService

router = APIRouter(prefix="/api/soulform", tags=["soulform"])


@router.get("/{user_id}")
def get_soulform_status(user_id: str, current_user: User = Depends(get_current_user)):
    return SoulformService().get_status(user_id)


@router.get("/{user_id}/eligibility")
def check_eligibility(user_id: str, current_user: User = Depends(get_current_user)):
    return SoulformService().check_eligibility(user_id)


@router.post("/{user_id}/transform")
def trigger_transformation(user_id: str, current_user: User = Depends(get_current_user)):
    return SoulformService().transform(user_id)
