from src.avatar_identity_engine.identity_engine import generate_avatar
from src.tree_of_life.tree_of_life import initialize_tree_of_life, compute_health_score
from src.leveling_system.leveling_system import initialize_merit_profile
from src.paths.sacred_path_engine import apply_sacred_path_effects
from src.groupplay.group_state_engine import generate_group_state

def generate_eden_payload(user_id, profile, secret_key):
    """
    Generates a full symbolic Eden payload for a given user profile.
    This includes avatar traits, Tree of Life, XP, DAO role, and aura metadata.
    """
    # === Avatar Setup ===
    avatar = generate_avatar(profile)
    sacred_path = profile.get("sacred_path", "Undeclared")
    group_opt_in = profile.get("group_opt_in", False)

    # === Tree Initialization ===
    tree = initialize_tree_of_life()
    tree = apply_sacred_path_effects(tree, sacred_path)
    tree["health_index"] = compute_health_score(tree)

    # === XP & Merit ===
    meritcoin = initialize_merit_profile()

    # === Quest Stub ===
    edenquest = {
        "title": "Crossing the First Threshold",
        "theme": "Beginnings",
        "metaphor": "The Mirror Awakens",
        "growth_target": "Choose Sacred Path and Face First Reflection"
    }

    # === DAO Stub ===
    dao = {
        "last_proposal": "Expand Glyph Library for Healer Class",
        "status": "eligible",
        "vote_weight": 1
    }

    # === World Tree Stub ===
    world_tree = {
        "symbolic_state": "Harmonic",
        "eden_health": 0.93,
        "active_dao_users": 42
    }

    # === Group Ritual State ===
    group_state = generate_group_state(user_id, group_opt_in)

    # === Compile Payload ===
    return {
        "avatar": avatar,
        "token": f"{user_id}.{secret_key}.eden",
        "tree_of_life": tree,
        "meritcoin": meritcoin,
        "edenquest": edenquest,
        "dao": dao,
        "world_tree": world_tree,
        "group_state": group_state
    }
