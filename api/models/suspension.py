"""
Suspension Model – Eden Protocol DAO Access Control

Defines schema for suspended or restricted DAO members.
Used to enforce symbolic bans, temporary lockouts, and status checks.
"""

from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class SuspensionRecord(BaseModel):
    user_id: str
    reason: str
    timestamp: datetime
    reinstated: bool = False
    reinstated_at: Optional[datetime] = None
