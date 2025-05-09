# Eden Payload Generator – Phase III Interface Bridge
# Creates a unified JSON-compatible bundle for external rendering

from src.avatar_identity_engine.identity_engine import generate_avatar
from src.tree_of_life.tree_of_life_engine import (
    initialize_tree_of_life,
    compute_health_score
)
from src.leveling_system.leveling_system import initialize_merit_profile
from src.edenquest_engine.edenquest_engine import generate_quest
from src.world_tree.world_tree_engine import generate_world_tree_report
from src.dao.governance_engine import create_proposal, cast_vote, close_proposal
from src.secure_enclave.secure_enclave import generate_signature, validate_signature, issue_verification_token


def generate_eden_payload(user_id: str, profile: dict, secret_key: str) -> dict:
    # Avatar Generation
    avatar = generate_avatar(profile)

    # Enclave Token Verification
    trait = avatar.get("mbti", "")
    signature = generate_signature(user_id, trait, secret_key)
    verified = validate_signature(user_id, trait, signature, secret_key)
    token = issue_verification_token(user_id, trait, verified)

    # Tree of Life & MeritCoin Setup
    tree = initialize_tree_of_life()
    tree["health_score"] = compute_health_score(tree)
    merit = initialize_merit_profile()

    # EdenQuest Assignment
    quest = generate_quest(tree)

    # DAO Sample Proposal Simulation
    proposal = create_proposal("Activate Eden AI", "Deploy Eden Protocol narrative system.", user_id)
    cast_vote(proposal, user_id, "for", merit["level"])
    dao = close_proposal(proposal)

    # World Tree Global Status
    world_tree = generate_world_tree_report([tree])

    return {
        "avatar": avatar,
        "token": token,
        "tree_of_life": tree,
        "meritcoin": merit,
        "edenquest": quest,
        "dao": dao,
        "world_tree": world_tree
    }


# Manual test example
if __name__ == "__main__":
    user_profile = {
        "mbti": "INTJ",
        "iq": 140,
        "eq": 120,
        "moral": "care"
    }
    payload = generate_eden_payload("user_sentinel", user_profile, "eden_secret")

    import json
    print("\n=== EDEN PAYLOAD ===")
    print(json.dumps(payload, indent=2))
