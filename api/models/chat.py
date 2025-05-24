"""
Chat Model – Eden Protocol

Defines shared Pydantic model schemas for therapeutic support chat records.
Used in session tracking, DB logging, and diagnostic generation.
"""

from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class ChatTurn(BaseModel):
    user_id: str
    role: str  # "user" or "eidolon"
    content: str
    emotion: Optional[str] = "neutral"
    timestamp: Optional[datetime] = datetime.utcnow()

class ChatSession(BaseModel):
    session_id: str
    user_id: str
    turns: list[ChatTurn]
    start_time: datetime
    end_time: Optional[datetime]
    escalated: bool = False
