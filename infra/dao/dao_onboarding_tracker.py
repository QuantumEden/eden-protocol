# infra/dao/dao_onboarding_tracker.py
# Tracks user progression into DAO via symbolic milestones

import json
from datetime import datetime
from typing import Dict, Any

ONBOARDING_LOG = []

MIN_LEVEL = 7
REQUIRED_TRAITS = {
    "discipline": 50,
    "resilience": 50,
    "mindfulness": 50,
    "expression": 50,
    "physical_care": 50,
    "emotional_regulation": 50
}

def is_eligible_for_dao(level: int, traits: Dict[str, int], hero_quest_complete: bool) -> bool:
    if level < MIN_LEVEL:
        return False
    if not hero_quest_complete:
        return False
    for trait, minimum in REQUIRED_TRAITS.items():
        if traits.get(trait, 0) < minimum:
            return False
    return True

def record_onboarding(user_id: str, level: int, traits: Dict[str, int], sacred_path: str, hero_quest_complete: bool) -> Dict[str, Any]:
    eligibility = is_eligible_for_dao(level, traits, hero_quest_complete)

    record = {
        "user_id": user_id,
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "level": level,
        "traits": traits,
        "sacred_path": sacred_path,
        "hero_quest_complete": hero_quest_complete,
        "eligible": eligibility
    }

    ONBOARDING_LOG.append(record)
    return record

def get_onboarding_log() -> list:
    return ONBOARDING_LOG

# Optional test
if __name__ == "__main__":
    mock_traits = {
        "discipline": 58,
        "resilience": 62,
        "mindfulness": 55,
        "expression": 50,
        "physical_care": 51,
        "emotional_regulation": 60
    }

    entry = record_onboarding(
        user_id="user_dao_011",
        level=8,
        traits=mock_traits,
        sacred_path="Taoism",
        hero_quest_complete=True
    )

    print(json.dumps(entry, indent=2))
