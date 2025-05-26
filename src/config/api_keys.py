# config/api_keys.py

"""
Secure API key loader for Eden Protocol integrations.
Keys are sourced from the .env file using pydantic-settings.
Do NOT hardcode secrets directly in code.
"""

from pydantic import BaseSettings

class APIKeys(BaseSettings):
    HUME_API_KEY: str
    HUME_SECRET_KEY: str
    ELEVENLABS_API_KEY: str
    PINECONE_API_KEY: str
    OPENAI_API_KEY: str  # Used for ChatGPT/GPT-4o integration

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        extra = "ignore"  # ✅ Safely ignores unexpected .env fields like PYTHONPATH

# Global access point for all loaded keys
keys = APIKeys()
