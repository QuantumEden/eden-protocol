# api/routes/avatar.py
# Eden Protocol – Avatar Identity Endpoints

from fastapi import APIRouter, Depends, HTTPException
from api.models.avatar import Avatar, UpdateAvatarRequest, SacredPathChange
from api.dependencies import get_current_user
from api.services.avatar_service import AvatarService
from api.models.user import User

router = APIRouter(prefix="/api/avatar", tags=["avatar"])


@router.get("/{user_id}", response_model=Avatar)
def get_avatar(user_id: str, current_user: User = Depends(get_current_user)):
    avatar = AvatarService().get_avatar(user_id)
    if not avatar:
        raise HTTPException(status_code=404, detail="Avatar not found")
    return avatar


@router.put("/{user_id}", response_model=Avatar)
def update_avatar(user_id: str, update: UpdateAvatarRequest, current_user: User = Depends(get_current_user)):
    return AvatarService().update_avatar(user_id, update)


@router.get("/{user_id}/history")
def get_avatar_history(user_id: str, current_user: User = Depends(get_current_user)):
    return AvatarService().get_avatar_history(user_id)


@router.post("/{user_id}/path", response_model=Avatar)
def set_sacred_path(user_id: str, change: SacredPathChange, current_user: User = Depends(get_current_user)):
    return AvatarService().update_sacred_path(user_id, change.path)
