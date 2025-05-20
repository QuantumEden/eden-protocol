# api/models/world_tree.py
# Eden Protocol – World Tree Models (optional OpenAPI support)

from pydantic import BaseModel, Field
from typing import Dict, List


class WorldTreeStatus(BaseModel):
    user_count: int = Field(..., example=128)
    active_profiles: int = Field(..., example=128)
    status: str = Field(..., example="Living system engaged")


class TraitAverages(BaseModel):
    averages: Dict[str, float]
    samples: int = Field(..., example=128)


class WorldTreeEvent(BaseModel):
    type: str = Field(..., example="xp_commit")
    user: str = Field(..., example="seer_alch_011")
    timestamp: str = Field(..., example="2025-05-20T22:44:00Z")
