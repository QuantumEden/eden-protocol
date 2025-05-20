# api/models/soulform.py
# Eden Protocol – Soulform Transformation Models

from pydantic import BaseModel, Field
from typing import Optional


class Soulform(BaseModel):
    id: str = Field(..., example="seraph")
    name: str = Field(..., example="Wings of Conviction")
    element: str = Field(..., example="Air")
    transformed_at: Optional[str]
    transformed: bool = True


class SoulformStatus(BaseModel):
    user_id: str
    soulform: Soulform


class SoulformEligibility(BaseModel):
    user_id: str
    eligible: bool
    reason: str
