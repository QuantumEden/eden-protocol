"""
Chat Service – Eden Protocol

Handles storage, retrieval, and lifecycle management for support chat sessions.
Interfaces with the session tracker and emotion memory for continuity.
"""

from typing import List, Optional
from datetime import datetime
from uuid import uuid4

from api.models.chat import ChatTurn, ChatSession
from src.ai.support.emotion_memory import record_emotion
from src.ai.eidolon.session_tracker import SessionTracker

# In-memory session store
CHAT_SESSIONS: dict[str, ChatSession] = {}
tracker = SessionTracker()

def start_chat_session(user_id: str) -> ChatSession:
    """
    Initializes a new support chat session.
    """
    session_id = f"session-{uuid4().hex[:8]}"
    session = ChatSession(
        session_id=session_id,
        user_id=user_id,
        turns=[],
        start_time=datetime.utcnow(),
        end_time=None
    )
    CHAT_SESSIONS[session_id] = session
    return session

def add_chat_turn(session_id: str, role: str, content: str, emotion: Optional[str] = "neutral") -> Optional[ChatTurn]:
    """
    Appends a dialogue turn to a session and logs emotion if from user.
    """
    session = CHAT_SESSIONS.get(session_id)
    if not session:
        return None

    turn = ChatTurn(
        user_id=session.user_id,
        role=role,
        content=content,
        emotion=emotion,
        timestamp=datetime.utcnow()
    )
    session.turns.append(turn)

    if role == "user":
        record_emotion(session.user_id, emotion, confidence=0.9)  # Confidence placeholder

    return turn

def end_chat_session(session_id: str) -> bool:
    """
    Marks a session as complete.
    """
    session = CHAT_SESSIONS.get(session_id)
    if session:
        session.end_time = datetime.utcnow()
        return True
    return False

def get_chat_history(session_id: str) -> List[ChatTurn]:
    """
    Returns full chat history for a session.
    """
    return CHAT_SESSIONS.get(session_id, ChatSession(session_id="", user_id="", turns=[], start_time=datetime.utcnow())).turns
