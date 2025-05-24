"""
Support Chat Route – Eden Protocol API

Defines FastAPI route for initiating and handling therapeutic
chat sessions between users and the Eidolon system.
"""

from fastapi import APIRouter, Request
from pydantic import BaseModel
from typing import Dict
from src.ai.eidolon.core_orchestrator import process_user_input

router = APIRouter()

class ChatRequest(BaseModel):
    user_id: str
    message: str
    metadata: Dict

@router.post("/support/chat")
async def support_chat_handler(payload: ChatRequest):
    """
    Receives user message and metadata, returns Eidolon therapeutic response.
    """
    result = process_user_input(
        user_id=payload.user_id,
        message=payload.message,
        metadata=payload.metadata
    )
    return {"response": result}
