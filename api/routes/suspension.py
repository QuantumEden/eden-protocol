"""
Suspension Route – Eden Protocol API

Defines endpoint to suspend or reinstate DAO member access
based on Ritual Safeguard logic, violations, or automated triggers.
"""

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from api.services.suspension_service import suspend_user, reinstate_user, get_suspension_status

router = APIRouter()

class SuspensionAction(BaseModel):
    user_id: str
    reason: str

@router.post("/dao/suspend")
async def suspend_member(action: SuspensionAction):
    success = suspend_user(action.user_id, action.reason)
    if not success:
        raise HTTPException(status_code=404, detail="User not found or already suspended.")
    return {"status": "suspended", "user_id": action.user_id}

@router.post("/dao/reinstate")
async def reinstate_member(action: SuspensionAction):
    success = reinstate_user(action.user_id)
    if not success:
        raise HTTPException(status_code=404, detail="User not found or not suspended.")
    return {"status": "reinstated", "user_id": action.user_id}

@router.get("/dao/status/{user_id}")
async def check_suspension(user_id: str):
    status = get_suspension_status(user_id)
    return {"user_id": user_id, "status": status}
