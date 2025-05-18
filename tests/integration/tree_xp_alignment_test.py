# Tree XP Alignment Test – Eden Protocol Integration Test
# Validates that trait growth aligns with XP gain and soulform eligibility logic

import sys, os, json
from datetime import datetime

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'src')))

from eden_payload_generator.eden_payload_generator import generate_eden_payload
from xp.meritcoin_minter import mint_meritcoin
from xp.meritcoin_ledger import log_commit

# === Constants
DAO_LEVEL_MIN = 7
TREE_PASS_THRESHOLD = {
    "discipline": 60,
    "resilience": 60,
    "mindfulness": 60,
    "expression": 50,
    "physical_care": 50,
    "emotional_regulation": 55
}

# === Mock User Profile
user_id = "user_alignment_023"
mock_profile = {
    "mbti": "ENFP",
    "iq": 128,
    "eq": 125,
    "moral": "justice",
    "sacred_path": "Logotherapy",
    "group_opt_in": True,
    "current_soulform": {
        "id": "dragon",
        "name": "Celestial Dragon",
        "elemental_affinity": "Air",
        "activated_at": datetime.utcnow().isoformat() + "Z"
    }
}

# === Step 1: Generate payload
payload = generate_eden_payload(user_id, mock_profile)
tree = payload["tree_traits"]

print("\n🌳 Tree of Life from Payload:")
print(json.dumps(tree, indent=2))

# === Step 2: Verify XP-soulform alignment
level = 8  # Mocked qualifying level
soulform_id = mock_profile["current_soulform"]["id"]

mint = mint_meritcoin(user_id, level, tree, soulform_id=soulform_id)
print("\n🪙 Mint Result:")
print(json.dumps(mint, indent=2))

if mint["success"]:
    # === Step 3: Log to Ledger
    commit = log_commit(
        user_id=user_id,
        level=level,
        xp=1020,
        reason="Passed Celestial Trial",
        soulform=mock_profile["current_soulform"]
    )
    print("\n📜 XP Commit Entry:")
    print(json.dumps(commit, indent=2))
else:
    print("\n❌ Soulform minting failed — check trait thresholds.")

# === Step 4: Validation
for trait, required in TREE_PASS_THRESHOLD.items():
    actual = tree.get(trait, 0)
    assert actual >= required, f"❌ Trait '{trait}' below threshold: {actual} < {required}"

assert mint["success"], "❌ Soulform minting failed despite passing level."

print("\n✅ Tree alignment test passed.\n")
