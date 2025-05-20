# api/routes/auth.py
# Eden Protocol – Authentication Endpoints

from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel

from api.services.auth_service import AuthService
from api.dependencies import get_current_user
from api.models.user import User

router = APIRouter(prefix="/api/auth", tags=["auth"])


class LoginRequest(BaseModel):
    username: str
    password: str


class TokenResponse(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"


@router.post("/login", response_model=TokenResponse)
def login_user(credentials: LoginRequest):
    auth = AuthService()
    tokens = auth.authenticate_user(credentials.username, credentials.password)
    if not tokens:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    return tokens


@router.post("/refresh", response_model=TokenResponse)
def refresh_token(refresh_token: str):
    auth = AuthService()
    new_tokens = auth.refresh_access_token(refresh_token)
    if not new_tokens:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid refresh token")
    return new_tokens


@router.get("/me", response_model=User)
def get_profile(current_user: User = Depends(get_current_user)):
    return current_user
