# api/models/auth.py
# Eden Protocol – Authentication Schemas

from pydantic import BaseModel, Field


class LoginRequest(BaseModel):
    username: str = Field(..., example="seer")
    password: str = Field(..., example="eden123")


class TokenResponse(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"


class RefreshTokenRequest(BaseModel):
    refresh_token: str
