# api/models/user.py
# Eden Protocol – User Identity Schema

from pydantic import BaseModel, Field


class User(BaseModel):
    username: str = Field(..., example="seer")
    role: str = Field(..., example="user")  # Can be "user", "mod", "admin"
    sacred_path: str = Field(..., example="Transhumanism")
