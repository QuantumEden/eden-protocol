import random

def generate_group_state(opt_in: bool) -> dict:
    """
    Generates a symbolic multiplayer state object for a user.
    This does not reflect real-time activity but reflects opt-in communion status.
    """
    if not opt_in:
        return {
            "status": "unlinked",
            "synergy_score": 0.0
        }

    # Simulate symbolic aura resonance with others
    simulated_synergy = round(random.uniform(0.65, 0.95), 2)
    instance_id = f"echo_cathedral_{random.randint(100, 999)}"

    return {
        "status": "linked",
        "synergy_score": simulated_synergy,
        "ritual_instance": instance_id
    }
