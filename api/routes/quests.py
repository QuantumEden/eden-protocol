# api/routes/quests.py
# Eden Protocol – Mythic Quest Endpoints

from fastapi import APIRouter, Depends, HTTPException
from api.dependencies import get_current_user
from api.models.user import User
from api.models.quest import QuestCompletion, QuestReflection
from api.services.quest_service import QuestService

router = APIRouter(prefix="/api/quests", tags=["quests"])


@router.get("/{user_id}")
def get_available_quests(user_id: str, current_user: User = Depends(get_current_user)):
    return QuestService().generate_quests(user_id)


@router.get("/{user_id}/{quest_id}")
def get_specific_quest(user_id: str, quest_id: str, current_user: User = Depends(get_current_user)):
    return QuestService().get_quest(user_id, quest_id)


@router.post("/{user_id}/{quest_id}/accept")
def accept_quest(user_id: str, quest_id: str, current_user: User = Depends(get_current_user)):
    return QuestService().accept_quest(user_id, quest_id)


@router.post("/{user_id}/{quest_id}/complete")
def complete_quest(user_id: str, quest_id: str, payload: QuestCompletion, current_user: User = Depends(get_current_user)):
    return QuestService().complete_quest(user_id, quest_id, payload)


@router.post("/{user_id}/{quest_id}/reflection")
def submit_reflection(user_id: str, quest_id: str, payload: QuestReflection, current_user: User = Depends(get_current_user)):
    return QuestService().reflect_on_quest(user_id, quest_id, payload)
