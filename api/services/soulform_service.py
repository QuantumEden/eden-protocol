# api/services/soulform_service.py
# Eden Protocol – Soulform Transformation Logic

from src.soulform.soulform_eligibility import check_soulform_eligibility
from infra.voice_response_stub import speak
from datetime import datetime

# Temporary in-memory soulform state
SOULFORM_DB = {}


class SoulformService:

    def get_status(self, user_id: str) -> dict:
        soulform = SOULFORM_DB.get(user_id, {
            "id": "none",
            "name": "Untransformed",
            "element": "Neutral",
            "transformed": False
        })
        return {"user_id": user_id, "soulform": soulform}

    def check_eligibility(self, user_id: str) -> dict:
        # For now, just call the static threshold engine
        eligible, reason = check_soulform_eligibility(user_id)
        return {
            "user_id": user_id,
            "eligible": eligible,
            "reason": reason
        }

    def transform(self, user_id: str) -> dict:
        eligible, reason = check_soulform_eligibility(user_id)
        if not eligible:
            return {
                "message": "Transformation blocked",
                "reason": reason
            }

        soulform = {
            "id": "seraph",
            "name": "Wings of Conviction",
            "element": "Air",
            "transformed_at": datetime.utcnow().isoformat() + "Z",
            "transformed": True
        }

        SOULFORM_DB[user_id] = soulform
        speak("soulform_transform")

        return {
            "message": "Transformation successful",
            "soulform": soulform
        }
