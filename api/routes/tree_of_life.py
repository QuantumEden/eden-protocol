# api/routes/tree_of_life.py
# Eden Protocol – Tree of Life Endpoints

from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from typing import Dict

from api.dependencies import get_current_user
from api.models.user import User
from api.services.tree_service import TreeService

router = APIRouter(prefix="/api/tree", tags=["tree"])


class TraitUpdate(BaseModel):
    trait: str
    amount: int = 5


class DecayRequest(BaseModel):
    decay_map: Dict[str, int]


class DisclosureReflection(BaseModel):
    truth_level: int  # 0–100
    emotional_intensity: int  # 0–100


@router.get("/{user_id}")
def get_tree(user_id: str, current_user: User = Depends(get_current_user)):
    return TreeService().get_user_tree(user_id)


@router.put("/{user_id}/trait")
def update_trait(user_id: str, update: TraitUpdate, current_user: User = Depends(get_current_user)):
    return TreeService().update_trait(user_id, update.trait, update.amount)


@router.post("/{user_id}/decay")
def apply_decay(user_id: str, decay: DecayRequest, current_user: User = Depends(get_current_user)):
    return TreeService().apply_decay(user_id, decay.decay_map)


@router.get("/{user_id}/health")
def compute_health(user_id: str, current_user: User = Depends(get_current_user)):
    return TreeService().get_health_score(user_id)


@router.post("/{user_id}/reflection")
def apply_disclosure(user_id: str, data: DisclosureReflection, current_user: User = Depends(get_current_user)):
    return TreeService().apply_disclosure(user_id, data)
