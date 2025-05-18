# sim/user_session_simulator.py
# Eden Protocol – User Session Simulation
# Simulates a complete symbolic session from psychometric profile to DAO readiness

import os, sys, json
from datetime import datetime
import random

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))

from eden_payload_generator.eden_payload_generator import generate_eden_payload
from xp.leveling_system.leveling_system import initialize_merit_profile, apply_xp
from infra.xp.meritcoin_minter import mint_meritcoin
from infra.xp.meritcoin_ledger import log_commit
from edenquest_engine.edenquest_engine import generate_quest

# === Simulate full onboarding session ===

user_id = f"user_session_{random.randint(1000, 9999)}"
secret_key = "simulated_key_888"

profile = {
    "mbti": "INTP",
    "iq": 135,
    "eq": 115,
    "moral": "justice",
    "sacred_path": "Taoism",
    "group_opt_in": True,
    "disclosure": {
        "diagnosis": ["PTSD"],
        "trauma_tags": ["combat", "betrayal"],
        "service_connected": True
    },
    "current_soulform": {
        "id": "seraph",
        "name": "Wings of Conviction",
        "elemental_affinity": "Air",
        "activated_at": datetime.utcnow().isoformat() + "Z"
    }
}

print("\n🔄 Starting User Session Simulation...\n")

# Step 1 – Generate Payload
payload = generate_eden_payload(user_id, profile, secret_key)
print("✅ Eden Payload:")
print(json.dumps(payload, indent=2))

# Step 2 – Initialize and apply XP
merit_profile = initialize_merit_profile()
apply_xp(merit_profile, payload["xp_awarded"])
print("\n📈 Updated Merit Profile:")
print(json.dumps(merit_profile, indent=2))

# Step 3 – Attempt Soulform Mint
mint = mint_meritcoin(user_id, merit_profile["level"], payload["tree_traits"], soulform_id="seraph")
print("\n🪙 Soulform Mint Result:")
print(json.dumps(mint, indent=2))

# Step 4 – Commit XP to Ledger
if mint["success"]:
    commit = log_commit(
        user_id=user_id,
        level=merit_profile["level"],
        xp=merit_profile["xp"],
        reason="Simulated Full Session",
        soulform=profile["current_soulform"]
    )
    print("\n📜 Commit Log:")
    print(json.dumps(commit, indent=2))

# Step 5 – Generate Quest
quest = generate_quest({k: {"score": v} for k, v in payload["tree_traits"].items()}, profile)
print("\n🧠 Therapeutic Quest:")
print(json.dumps(quest, indent=2))

print("\n✅ User session simulation complete.\n")
