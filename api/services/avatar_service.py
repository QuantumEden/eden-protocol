# api/services/avatar_service.py
# Eden Protocol – Avatar Service Layer

from api.models.avatar import Avatar, UpdateAvatarRequest
from datetime import datetime

# === Temporary in-memory avatar store ===
AVATAR_DB = {
    "seer_alch_011": {
        "user_id": "seer_alch_011",
        "name": "Seer of the Void",
        "element": "Air",
        "sacred_path": "Transhumanism",
        "archetype": "Visionary",
        "transformed": False,
        "last_updated": datetime.utcnow().isoformat() + "Z",
        "history": []
    }
}


class AvatarService:

    def get_avatar(self, user_id: str) -> Avatar | None:
        data = AVATAR_DB.get(user_id)
        return Avatar(**data) if data else None

    def update_avatar(self, user_id: str, update: UpdateAvatarRequest) -> Avatar:
        avatar = AVATAR_DB.get(user_id)
        if not avatar:
            avatar = {"user_id": user_id, "history": []}
        for field, value in update.dict(exclude_unset=True).items():
            avatar[field] = value
        avatar["last_updated"] = datetime.utcnow().isoformat() + "Z"
        AVATAR_DB[user_id] = avatar
        return Avatar(**avatar)

    def get_avatar_history(self, user_id: str) -> list[dict]:
        avatar = AVATAR_DB.get(user_id)
        return avatar.get("history", []) if avatar else []

    def update_sacred_path(self, user_id: str, new_path: str) -> Avatar:
        avatar = AVATAR_DB.get(user_id)
        if not avatar:
            raise ValueError("Avatar not found")

        avatar["history"].append({
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "event": f"Sacred path changed to {new_path}"
        })
        avatar["sacred_path"] = new_path
        avatar["last_updated"] = datetime.utcnow().isoformat() + "Z"
        return Avatar(**avatar)
