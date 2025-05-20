# api/models/quest.py
# Eden Protocol – Quest Interaction Schemas

from pydantic import BaseModel, Field


class QuestCompletion(BaseModel):
    xp: int = Field(..., ge=50, description="XP awarded for completing the quest")
    notes: str = Field(..., example="Completed inner challenge. Overcame fear of rejection.")


class QuestReflection(BaseModel):
    insight: str = Field(..., example="I realized my trauma stems from fear of being vulnerable.")
    emotion: str = Field(..., example="Relief, followed by intense sadness and clarity.")
