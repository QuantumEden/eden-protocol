import os
from pydantic_settings import BaseSettings, SettingsConfigDict

class APIKeys(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    HUME_API_KEY: str
    HUME_SECRET_KEY: str
    ELEVENLABS_API_KEY: str
    PINECONE_API_KEY: str

keys = APIKeys()
