# api/utils/formatters.py
# Eden Protocol – Standard Response Format

from api.config import settings
from typing import Any


def success_response(data: Any, message: str = "Operation successful") -> dict:
    return {
        "success": True,
        "data": data,
        "message": message,
        "timestamp": settings.now()
    }


def error_response(code: str, message: str) -> dict:
    return {
        "success": False,
        "error": {
            "code": code,
            "message": message
        },
        "timestamp": settings.now()
    }
