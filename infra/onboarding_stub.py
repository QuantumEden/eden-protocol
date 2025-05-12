import uuid
import datetime

def create_initial_session(user_id: str, sacred_path: str, group_opt_in: bool = False) -> dict:
    """
    Generates a starter session payload with symbolic alignment.
    """
    aura_defaults = {
        "Zen Buddhism": "#6DDCCF",
        "Christianity": "#EAD1DC",
        "Alchemy": "#F1D37A",
        "Taoism": "#D0F0C0",
        "Judaism": "#B0D0F0",
        "Norse Paganism": "#C9C0BB",
        "Undeclared": "#AAAAAA"
    }

    return {
        "session_id": str(uuid.uuid4()),
        "user_id": user_id,
        "sacred_path": sacred_path,
        "aura_color": aura_defaults.get(sacred_path, "#AAAAAA"),
        "current_screen": "onboarding_intro",
        "onboarding_complete": False,
        "group_opt_in": group_opt_in,
        "last_sync": datetime.datetime.utcnow().isoformat()
    }

# Example usage
if __name__ == "__main__":
    session = create_initial_session("test_user_001", "Alchemy", True)
    print(session)
