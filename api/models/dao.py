# api/models/dao.py
# Eden Protocol – DAO Governance Schemas

from pydantic import BaseModel, Field
from typing import Optional, Literal


class DAOCreation(BaseModel):
    title: str = Field(..., example="Mandate Tree Reflection Before Level 10")
    description: str = Field(..., example="Require all users to submit a reflective ritual before leveling beyond 10.")
    category: Literal["policy", "ritual", "suspension", "ban", "mod", "structure"] = Field(..., example="policy")
    enforcement: Optional[Literal["soft", "hard", "ritualized"]] = Field(None, example="ritualized")
    target_user_id: Optional[str] = Field(None, example="user_1234")  # Required for ban/suspension proposals


class DAOVoteRequest(BaseModel):
    vote: Literal["yes", "no"] = Field(..., example="yes")
    voter_id: Optional[str] = Field(None, example="seer_alch_009")  # Optional, used for zkXP proof binding


class DAOEnforcementAction(BaseModel):
    user_id: str = Field(..., example="seer_alch_009")
    action: Literal["suspend", "ban"] = Field(..., example="ban")
    reason: str = Field(..., example="Convicted of felony violating DAO code")
    approved_by: Optional[list[str]] = Field(None, example=["seer_alch_002", "seer_alch_007"])  # List of approving voters
    timestamp: Optional[str] = Field(None, example="2025-06-01T00:00:00Z")
