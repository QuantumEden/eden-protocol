# api/services/auth_service.py
# Eden Protocol – Authentication Logic (JWT, password validation)

from datetime import timedelta
from api.models.user import User
from api.config import settings
from api.utils.security import (
    verify_password,
    create_access_token,
    create_refresh_token,
    decode_token
)


# Temporary mock user database
MOCK_USERS = {
    "seer": {
        "username": "seer",
        "hashed_password": "$2b$12$7KbhzWzpYlZLxFhE2RuMLeaDdvy8kLqU3Y2gJqD7StkRcgQ7zGHwe",  # 'eden123'
        "role": "user",
        "sacred_path": "Transhumanism"
    },
    "mod": {
        "username": "mod",
        "hashed_password": "$2b$12$AULzy88fzBBa0aNk8WdK.OvPKkB2F1F3j5bPdtQ4GeExLnc3Xyo2S",  # 'adminroot'
        "role": "mod",
        "sacred_path": "Technognostic"
    }
}


class AuthService:
    def authenticate_user(self, username: str, password: str) -> dict | None:
        """
        Authenticate user and return JWT tokens if valid.
        """
        user_data = MOCK_USERS.get(username)
        if not user_data or not verify_password(password, user_data["hashed_password"]):
            return None

        user = User(
            username=username,
            role=user_data["role"],
            sacred_path=user_data["sacred_path"]
        )

        access_token = create_access_token(user.dict(), expires_delta=timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES))
        refresh_token = create_refresh_token(user.dict(), expires_delta=timedelta(days=settings.REFRESH_TOKEN_EXPIRE_DAYS))

        return {
            "access_token": access_token,
            "refresh_token": refresh_token,
            "token_type": "bearer"
        }

    def refresh_access_token(self, refresh_token: str) -> dict | None:
        """
        Refresh access token using a valid refresh token.
        """
        try:
            payload = decode_token(refresh_token)
            user = User(**payload)

            access_token = create_access_token(user.dict(), expires_delta=timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES))
            return {
                "access_token": access_token,
                "refresh_token": refresh_token,
                "token_type": "bearer"
            }
        except Exception:
            return None
