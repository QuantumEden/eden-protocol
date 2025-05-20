# api/models/dao.py
# Eden Protocol – DAO Governance Schemas

from pydantic import BaseModel, Field


class DAOCreation(BaseModel):
    title: str = Field(..., example="Mandate Tree Reflection Before Level 10")
    description: str = Field(..., example="Require all users to submit a reflective ritual before leveling beyond 10.")


class DAOVoteRequest(BaseModel):
    vote: str = Field(..., example="yes", regex="^(yes|no)$")
