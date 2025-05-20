# api/config.py
# Eden Protocol Configuration Loader

import os
from datetime import datetime
from dotenv import load_dotenv
from pydantic import BaseSettings

# Load environment variables from .env file (if present)
load_dotenv()

class Settings(BaseSettings):
    PROJECT_NAME: str = "Eden Protocol"
    API_VERSION: str = "1.0.0"
    ENVIRONMENT: str = os.getenv("ENVIRONMENT", "development")
    DEBUG: bool = os.getenv("DEBUG", "true").lower() == "true"
    JWT_SECRET_KEY: str = os.getenv("JWT_SECRET_KEY", "insecure_default")
    JWT_ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60
    REFRESH_TOKEN_EXPIRE_DAYS: int = 30

    ALLOWED_ORIGINS: list[str] = [
        "http://localhost",
        "http://localhost:3000",
        "http://127.0.0.1:8000",
        "https://eden-protocol.com"
    ]

    @staticmethod
    def now():
        return datetime.utcnow().isoformat() + "Z"

settings = Settings()
