# api/services/tree_service.py
# Eden Protocol – Tree of Life Service

from src.tree_of_life.tree_of_life_engine import (
    get_default_tree,
    grow_branch,
    apply_decay,
    compute_health_score
)
from src.xp.meritcoin_ledger import log_commit
from infra.voice_response_stub import speak

from api.models.user import User

# Temporary in-memory user trait store
TREE_DB = {}


class TreeService:

    def get_user_tree(self, user_id: str) -> dict:
        return TREE_DB.get(user_id, get_default_tree())

    def update_trait(self, user_id: str, trait: str, amount: int) -> dict:
        tree = self.get_user_tree(user_id)
        updated = grow_branch(tree, trait, amount)
        TREE_DB[user_id] = updated

        log_commit(
            user_id=user_id,
            level=1,
            xp=100,
            reason=f"Trait '{trait}' improved by {amount}",
            traits_snapshot=updated
        )

        speak("tree_grow")
        return updated

    def apply_decay(self, user_id: str, decay_map: dict) -> dict:
        tree = self.get_user_tree(user_id)
        updated = apply_decay(tree, decay_map)
        TREE_DB[user_id] = updated
        return updated

    def get_health_score(self, user_id: str) -> dict:
        tree = self.get_user_tree(user_id)
        score = compute_health_score(tree)
        return {"user_id": user_id, "health_score": score}

    def apply_disclosure(self, user_id: str, data: dict) -> dict:
        """
        Applies a user’s reflective disclosure as symbolic growth.
        Future version may invoke more nuanced logic.
        """
        growth_map = {
            "mindfulness": int(data.truth_level * 0.3),
            "emotional_regulation": int(data.emotional_intensity * 0.2)
        }
        tree = self.get_user_tree(user_id)
        for trait, inc in growth_map.items():
            tree = grow_branch(tree, trait, inc)

        TREE_DB[user_id] = tree
        speak("xp_commit")
        return {
            "message": "Reflection applied",
            "updated_traits": tree
        }
