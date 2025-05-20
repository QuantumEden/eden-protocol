# api/models/tree.py
# Eden Protocol – Tree of Life Schemas

from pydantic import BaseModel, Field
from typing import Dict


class TreeOfLife(BaseModel):
    discipline: int = Field(..., ge=0, le=100)
    resilience: int = Field(..., ge=0, le=100)
    mindfulness: int = Field(..., ge=0, le=100)
    expression: int = Field(..., ge=0, le=100)
    physical_care: int = Field(..., ge=0, le=100)
    emotional_regulation: int = Field(..., ge=0, le=100)


class TraitUpdate(BaseModel):
    trait: str
    amount: int = Field(5, ge=1, le=20)


class DecayRequest(BaseModel):
    decay_map: Dict[str, int]


class DisclosureReflection(BaseModel):
    truth_level: int = Field(..., ge=0, le=100)
    emotional_intensity: int = Field(..., ge=0, le=100)
