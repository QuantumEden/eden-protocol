# full_protocol_simulation.py – Eden Protocol Integration Test
# Simulates full user lifecycle: traits → XP → Merit → Soulform → DAO → Quest

import json
from datetime import datetime

# Import all required components
from src.eden_payload_generator.eden_payload_generator import generate_eden_payload
from infra.xp.meritcoin_minter import mint_meritcoin
from infra.xp.meritcoin_ledger import log_commit
from src.edenquest_engine.edenquest_engine import generate_quest
from src.quest_engine.quest_modifier import apply_quest_modifiers
from src.leveling_system.leveling_system import initialize_merit_profile, apply_xp
from src.dao.mod_registry import is_mod_approved
from src.tree_of_life.tree_of_life_engine import TreeOfLife

print("\n🌱 Eden Protocol – Full Stack Ritual Simulation\n")

# Step 1: Define mock user profile
user_id = "initiate_dragon_042"
secret_key = "divine_sigil_xyz"

user_profile = {
    "mbti": "INTJ",
    "iq": 144,
    "eq": 124,
    "moral": "truth",
    "sacred_path": "Hermeticism",
    "group_opt_in": True,
    "disclosure": {
        "diagnosis": ["PTSD", "depression"],
        "trauma_tags": ["combat", "identity_loss"],
        "service_connected": True
    },
    "current_soulform": {
        "id": "dragon",
        "name": "Emerald Sentinel",
        "elemental_affinity": "Earth",
        "activated_at": datetime.utcnow().isoformat() + "Z"
    }
}

# Step 2: Generate Eden payload
print("🔍 Generating payload...")
payload = generate_eden_payload(user_id, user_profile, secret_key)
print(json.dumps(payload, indent=2))

# Step 3: Mint MeritCoin
print("\n🪙 Attempting to mint MeritCoin...")
tree = payload["tree_traits"]
level = 8
mint_result = mint_meritcoin(user_id, level, tree, soulform_id="dragon")

if mint_result["success"]:
    print("✅ Minting successful:")
    print(json.dumps(mint_result["meritcoin"], indent=2))
else:
    print("❌ Minting failed:", mint_result["reason"])

# Step 4: Log XP commit
print("\n📜 Logging symbolic XP commit...")
commit = log_commit(
    user_id=user_id,
    level=level,
    xp=1020,
    reason="Trial of the Earth Spire",
    soulform=user_profile["current_soulform"]
)
print(json.dumps(commit, indent=2))

# Step 5: Generate quest from tree imbalance
print("\n🧭 Generating therapeutic quest...")
symbolic_tree = {
    k: {"score": v} for k, v in tree.items()
}
raw_quest = generate_quest(symbolic_tree)
modified_quest = apply_quest_modifiers(raw_quest["quest"], user_profile)

print(json.dumps(modified_quest, indent=2))

# Step 6: Check DAO eligibility
print("\n🗳️ DAO Eligibility Check:")
if payload["eligible_for_dao"]:
    print("✅ User is eligible for DAO proposal access.")
else:
    print("❌ User is not yet eligible for DAO. Traits or level too low.")

print("\n✅ Full integration test complete.")
