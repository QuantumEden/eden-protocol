# api/routes/world_tree.py
# Eden Protocol – World Tree Status Endpoints

from fastapi import APIRouter, Depends
from api.dependencies import get_current_user
from api.models.user import User
from api.services.tree_service import TREE_DB  # Reusing from local trait data

router = APIRouter(prefix="/api/worldtree", tags=["worldtree"])


@router.get("/status")
def get_global_status(current_user: User = Depends(get_current_user)):
    user_count = len(TREE_DB)
    active_traits = [user_tree for user_tree in TREE_DB.values()]
    return {
        "user_count": user_count,
        "active_profiles": len(active_traits),
        "status": "Living system engaged",
    }


@router.get("/traits")
def get_global_trait_averages(current_user: User = Depends(get_current_user)):
    from collections import defaultdict

    trait_totals = defaultdict(int)
    count = 0

    for tree in TREE_DB.values():
        for trait, value in tree.items():
            trait_totals[trait] += value
        count += 1

    if count == 0:
        return {"averages": {}}

    averages = {trait: round(total / count, 2) for trait, total in trait_totals.items()}
    return {"averages": averages, "samples": count}


@router.get("/activity")
def get_recent_activity(current_user: User = Depends(get_current_user)):
    return {
        "events": [
            {"type": "xp_commit", "user": "seer_alch_011", "timestamp": "2025-05-20T22:44:00Z"},
            {"type": "quest_complete", "user": "seer_alch_011", "timestamp": "2025-05-20T22:35:00Z"}
        ]
    }
