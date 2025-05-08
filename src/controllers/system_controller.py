# Eden Protocol System Controller – Phase III Integration
# Central hub to orchestrate avatar, tree, leveling, quest, and governance modules

from src.avatar_identity_engine.identity_engine import generate_avatar
from src.tree_of_life.tree_of_life_engine import (
    initialize_tree_of_life,
    grow_branch,
    decay_tree,
    print_tree_summary
)
from src.leveling_system.leveling_system import (
    initialize_merit_profile,
    add_xp,
    apply_decay,
    lock_progress,
    unlock_progress,
    print_merit_status
)
from src.edenquest_engine.edenquest_engine import generate_quest
from src.world_tree.world_tree_engine import generate_world_tree_report
from src.dao.governance_engine import create_proposal, cast_vote, close_proposal
from src.secure_enclave.secure_enclave import generate_signature, validate_signature, issue_verification_token


# Step 1: Simulate full user lifecycle in the Eden Protocol
def run_protocol_cycle(user_id: str, profile_data: dict, secret_key: str):
    print(f"\n=== Eden Protocol Cycle: {user_id} ===")

    # Identity
    avatar = generate_avatar(profile_data)
    print("\n[Avatar Created]")
    print(avatar)

    # Secure Enclave Verification
    raw_trait = avatar.get("mbti", "")
    signature = generate_signature(user_id, raw_trait, secret_key)
    valid = validate_signature(user_id, raw_trait, signature, secret_key)
    token = issue_verification_token(user_id, raw_trait, valid)
    print("\n[Identity Token Issued]")
    print(token)

    # Initialize Tree of Life + Leveling Profile
    tree = initialize_tree_of_life()
    level = initialize_merit_profile()

    # Growth and decay simulation
    grow_branch(tree, "discipline", 10)
    decay_tree(tree)
    add_xp(level, 125)
    print_tree_summary(tree)
    print_merit_status(level)

    # EdenQuest assignment
    quest = generate_quest(tree)
    print("\n[EdenQuest Assigned]")
    print(quest)

    # DAO proposal simulation
    proposal = create_proposal("Expand Tree Visualization", "Fund symbolic UI layer", user_id)
    cast_vote(proposal, user_id, "for", level["level"])
    outcome = close_proposal(proposal)
    print("\n[DAO Outcome]")
    print(outcome)

    # World Tree Sample Integration
    global_status = generate_world_tree_report([tree])
    print("\n[World Tree Status]")
    print(global_status)

# Example usage (for manual test)
if __name__ == "__main__":
    profile = {
        "mbti": "INFJ",
        "iq": 135,
        "eq": 115,
        "moral": "care"
    }
    run_protocol_cycle("user_alpha", profile, "eden_secret")
