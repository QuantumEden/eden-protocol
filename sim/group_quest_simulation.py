import json
from datetime import datetime
from src.groupplay.group_state_engine import generate_group_state

# Sample symbolic group profiles (opted-in)
group_profiles = [
    {"username": "healer_alpha", "opt_in": True},
    {"username": "guardian_beta", "opt_in": True},
    {"username": "strategist_gamma", "opt_in": True},
    {"username": "builder_delta", "opt_in": True}
]

print(f"\n=== 🫂 Group Quest Ritual Simulation – {datetime.utcnow().isoformat()}Z ===\n")

for user in group_profiles:
    try:
        if not user.get("opt_in", False):
            print(f"-- {user['username']} skipped (not opted-in) --")
            continue

        group_state = generate_group_state(user["opt_in"])
        print(f"-- {user['username']} --")
        print(json.dumps(group_state, indent=2))
        print()

    except Exception as e:
        print(f"⚠️ Error processing {user['username']}: {e}")
