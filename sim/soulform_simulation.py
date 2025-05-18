# soulform_simulation.py – Eden Protocol Symbolic Transformation Tester
# Stress-tests soulform logic integration with XP, Tree, and DAO systems

import sys, os
import json
from datetime import datetime

# === Import path fix ===
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from infra.xp.meritcoin_minter import mint_meritcoin
from infra.xp.meritcoin_ledger import log_commit
from src.eden_payload_generator.eden_payload_generator import generate_eden_payload

# === Mock Tree with threshold-passing values
valid_tree = {
    "discipline": 66,
    "resilience": 70,
    "mindfulness": 68,
    "expression": 53,
    "physical_care": 58,
    "emotional_regulation": 59
}

# === Sample soulform object
mock_soulform = {
    "id": "wyrm",
    "name": "Twilight Serpent",
    "elemental_affinity": "Air",
    "activated_at": datetime.utcnow().isoformat() + "Z"
}

# === Simulate soulform minting
user_id = "user_wyrm_009"
level = 8

mint_result = mint_meritcoin(user_id, level, valid_tree, soulform_id=mock_soulform["id"])

if mint_result["success"]:
    print("\n✅ Soulform MeritCoin Minted:\n")
    print(json.dumps(mint_result["meritcoin"], indent=2))

    # === Log the transformation event to the ledger
    commit_entry = log_commit(
        user_id=user_id,
        level=level,
        xp=950,
        reason="Completed Soulform Trial",
        soulform=mock_soulform
    )

    print("\n📜 Commit Logged:\n")
    print(json.dumps(commit_entry, indent=2))

else:
    print("\n❌ Minting Failed:\n")
    print(mint_result)

# === Optional: Generate payload with soulform included
mock_profile = {
    "mbti": "ENTP",
    "iq": 138,
    "eq": 110,
    "moral": "liberty",
    "sacred_path": "Transhumanism",
    "group_opt_in": True,
    "current_soulform": mock_soulform
}

payload = generate_eden_payload(user_id, mock_profile, secret_key="wormhole_key_999")
print("\n🌱 Payload with Soulform Overlay:\n")
print(json.dumps(payload, indent=2))
