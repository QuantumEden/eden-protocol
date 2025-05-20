# api/dependencies.py
# Eden Protocol Shared Dependencies (Auth + Context)

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt

from api.config import settings
from api.models.user import User
from api.utils.security import decode_token


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/auth/login")


async def get_current_user(token: str = Depends(oauth2_scheme)) -> User:
    """
    Dependency to retrieve the current authenticated user from a JWT token.
    Raises HTTP 401 if token is invalid or user cannot be parsed.
    """
    try:
        payload = decode_token(token)
        user = User(**payload)
        return user
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate token",
            headers={"WWW-Authenticate": "Bearer"},
        )


def require_role(role: str):
    """
    Dependency factory for role-based route restriction.
    Example: `Depends(require_role("mod"))`
    """
    def dependency(user: User = Depends(get_current_user)):
        if user.role != role:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Access denied for your role."
            )
        return user
    return dependency
