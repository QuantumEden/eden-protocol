# api/services/quest_service.py
# Eden Protocol – Quest Engine Integration

from src.edenquest_engine.edenquest_engine import generate_symbolic_quests
from infra.voice_response_stub import speak
from datetime import datetime
from api.models.quest import QuestCompletion, QuestReflection

# Temporary in-memory store
QUEST_LOG = {}


class QuestService:

    def generate_quests(self, user_id: str) -> list:
        quests = generate_symbolic_quests(user_id)
        QUEST_LOG[user_id] = {q["id"]: q for q in quests}
        return quests

    def get_quest(self, user_id: str, quest_id: str) -> dict:
        user_quests = QUEST_LOG.get(user_id, {})
        return user_quests.get(quest_id, {"message": "Quest not found"})

    def accept_quest(self, user_id: str, quest_id: str) -> dict:
        quest = QUEST_LOG[user_id][quest_id]
        quest["status"] = "accepted"
        quest["accepted_at"] = datetime.utcnow().isoformat() + "Z"
        speak("quest_accepted")
        return quest

    def complete_quest(self, user_id: str, quest_id: str, payload: QuestCompletion) -> dict:
        quest = QUEST_LOG[user_id][quest_id]
        quest["status"] = "completed"
        quest["completed_at"] = datetime.utcnow().isoformat() + "Z"
        quest["xp_awarded"] = payload.xp
        speak("quest_completed")
        return {
            "message": f"Quest {quest['title']} completed",
            "quest": quest
        }

    def reflect_on_quest(self, user_id: str, quest_id: str, payload: QuestReflection) -> dict:
        quest = QUEST_LOG[user_id][quest_id]
        quest["reflection"] = {
            "insight": payload.insight,
            "emotion": payload.emotion,
            "submitted_at": datetime.utcnow().isoformat() + "Z"
        }
        speak("quest_reflection")
        return {
            "message": "Reflection received",
            "quest": quest
        }
