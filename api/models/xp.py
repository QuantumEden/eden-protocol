# api/models/xp.py
# Eden Protocol – XP + MeritCoin Request Schemas

from pydantic import BaseModel, Field
from typing import Dict


class XPCommit(BaseModel):
    level: int = Field(..., ge=1)
    xp: int = Field(..., ge=1)
    reason: str = Field(..., example="Completed DAO ritual challenge")
    traits_snapshot: Dict[str, int]


class XPDisclosure(BaseModel):
    level: int = Field(..., ge=1)
    truth: int = Field(..., ge=0, le=100)
    vulnerability: int = Field(..., ge=0, le=100)
    traits_snapshot: Dict[str, int]


class XPModGrant(BaseModel):
    level: int = Field(..., ge=1)
    xp: int = Field(..., ge=10)
    traits_snapshot: Dict[str, int]
