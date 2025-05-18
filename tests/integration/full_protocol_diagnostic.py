# tests/integration/full_protocol_diagnostic.py
# 🔍 Full System Diagnostic – Validates Eden Protocol Phase 17 components in unison

import sys, os, json
from datetime import datetime

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'src')))

# ✅ FIXED IMPORTS
from src.eden_payload_generator.eden_payload_generator import generate_eden_payload
from src.leveling_system.leveling_system import initialize_merit_profile, apply_xp, lock_progress, unlock_progress
from infra.xp.meritcoin_minter import mint_meritcoin
from infra.xp.meritcoin_ledger import log_commit
from src.edenquest_engine.edenquest_engine import generate_quest
from src.quest_engine.quest_modifier import apply_quest_modifiers
from src.biometrics.biometric_integrity_check import log_biometric_event, verify_biometric_signature

# === Phase 17 Diagnostic Run ===

# Step 1: Payload Generation
mock_profile = {
    "mbti": "INFJ",
    "iq": 138,
    "eq": 118,
    "moral": "truth",
    "sacred_path": "Taoism",
    "group_opt_in": True,
    "disclosure": {
        "diagnosis": ["PTSD"],
        "trauma_tags": ["combat"],
        "service_connected": True
    },
    "current_soulform": {
        "id": "phoenix",
        "name": "Ashborn Phoenix",
        "elemental_affinity": "Fire",
        "activated_at": datetime.utcnow().isoformat() + "Z"
    }
}

user_id = "seer_diag_001"
secret_key = "diagnostic_key_999"

payload = generate_eden_payload(user_id, mock_profile, secret_key)

print("\n🌱 Phase 17 Payload:")
print(json.dumps(payload, indent=2))

# Step 2: XP Subsystem Test
profile = initialize_merit_profile()
apply_xp(profile, 150)

print("\n📈 Merit Profile (After XP Gain):")
print(json.dumps(profile, indent=2))

# Step 3: Minting Test
tree = payload["tree_traits"]
mint = mint_meritcoin(user_id, level=8, tree_traits=tree, soulform_id="phoenix")

print("\n🪙 MeritCoin Mint Output:")
print(json.dumps(mint, indent=2))

# Step 4: Ledger Log Test
if mint["success"]:
    commit = log_commit(
        user_id=user_id,
        level=8,
        xp=1100,
        reason="Passed Soulform Trial",
        soulform=mock_profile["current_soulform"]
    )
    print("\n📜 Commit Logged:")
    print(json.dumps(commit, indent=2))

# Step 5: Quest Generation
sample_tree = {
    "discipline": {"score": 70},
    "empathy": {"score": 82},
    "resilience": {"score": 48},
    "expression": {"score": 74},
    "mindfulness": {"score": 72},
    "physical_care": {"score": 66},
    "emotional_regulation": {"score": 69}
}

quest = generate_quest(sample_tree, mock_profile)

print("\n🧠 Therapeutic Quest Generated:")
print(json.dumps(quest, indent=2))

# Step 6: Biometric Signature Test
bio_log = log_biometric_event(user_id, "My sacred phrase for DAO onboarding", context="DAO oath")
verified = verify_biometric_signature("My sacred phrase for DAO onboarding", bio_log["signature_hash"])

print("\n🔐 Biometric Verification:")
print(json.dumps(bio_log, indent=2))
print("✅ Signature Verified:", verified)
