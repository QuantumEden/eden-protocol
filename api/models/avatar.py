# api/models/avatar.py
# Eden Protocol – Avatar Data Schemas

from pydantic import BaseModel, Field
from typing import Optional


class Avatar(BaseModel):
    user_id: str
    name: Optional[str] = Field(None, example="Seer of the Void")
    element: Optional[str] = Field(None, example="Air")
    sacred_path: Optional[str] = Field(None, example="Transhumanism")
    archetype: Optional[str] = Field(None, example="Visionary")
    transformed: Optional[bool] = False
    last_updated: Optional[str]
    history: Optional[list] = []


class UpdateAvatarRequest(BaseModel):
    name: Optional[str]
    element: Optional[str]
    archetype: Optional[str]
    transformed: Optional[bool]


class SacredPathChange(BaseModel):
    path: str = Field(..., example="Technognostic")
