# xp_ledger_updater.py – Eden Protocol Infra
# Applies XP changes, checks thresholds, enforces ritual lockouts

XP_THRESHOLDS = [100, 250, 500, 850, 1200, 1600, 2100, 2700, 3400, 4200]  # Levels 1–10
LOCKOUT_THRESHOLD = 42  # If average trait score drops below this, user is locked

def compute_next_level(current_level):
    if current_level < len(XP_THRESHOLDS):
        return XP_THRESHOLDS[current_level]
    return XP_THRESHOLDS[-1] + (current_level - len(XP_THRESHOLDS) + 1) * 1000

def apply_xp_change(user_state, xp_delta):
    xp = user_state.get("xp", 0) + xp_delta
    level = user_state.get("level", 1)
    next_level = user_state.get("next_level", compute_next_level(level))
    locked = user_state.get("locked", False)

    while xp >= next_level:
        level += 1
        xp -= next_level
        next_level = compute_next_level(level)

    return {
        "level": level,
        "xp": xp,
        "next_level": next_level,
        "locked": locked
    }

def check_lockout(tree_traits):
    avg = sum(tree_traits.values()) / len(tree_traits)
    return avg < LOCKOUT_THRESHOLD

def update_user_xp(user_id, user_state, tree_traits, xp_delta):
    locked = check_lockout(tree_traits)
    updated = apply_xp_change(user_state, xp_delta)
    updated["locked"] = locked
    return updated

# Example
if __name__ == "__main__":
    tree = {
        "discipline": 40,
        "resilience": 38,
        "mindfulness": 35,
        "expression": 44,
        "physical_care": 45,
        "emotional_regulation": 39
    }

    user_state = {
        "level": 3,
        "xp": 120,
        "next_level": 250,
        "locked": False
    }

    updated = update_user_xp("user_sage_002", user_state, tree, 90)
    print(updated)
