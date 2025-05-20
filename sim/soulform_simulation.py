# sim/soulform_simulation.py
# Simulates Soulform Readiness Check → Ritual Trigger → Mint → XP Commit → Payload

import json
from datetime import datetime

from src.tree_of_life.tree_of_life_engine import get_default_tree
from src.soulform.soulform_eligibility import check_soulform_eligibility, get_default_thresholds
from src.eden_payload_generator.eden_payload_generator import generate_eden_payload
from infra.voice_response_stub import speak
from infra.xp.meritcoin_ledger import log_commit
from infra.xp.meritcoin_minter import mint_meritcoin


# === Setup: Simulated User and Trait Tree ===
user_id = "user_wyrm_009"
level = 8

valid_tree = {
    "discipline": 72,
    "resilience": 85,
    "mindfulness": 78,
    "expression": 66,
    "physical_care": 70,
    "emotional_regulation": 74
}

# === Check soulform eligibility ===
thresholds = get_default_thresholds()
eligible = check_soulform_eligibility(valid_tree, thresholds)

if eligible:
    speak("soulform_ready")

    # === Define soulform for simulation ===
    mock_soulform = {
        "id": "wyrm",
        "name": "Twilight Serpent",
        "element": "Air",
        "transformed_at": datetime.utcnow().isoformat() + "Z"
    }

    # === Mint the Soulform
    mint_result = mint_meritcoin(
        user_id=user_id,
        level=level,
        traits_snapshot=valid_tree,
        soulform_id=mock_soulform["id"]
    )

    if mint_result["success"]:
        print("\n✅ Soulform MeritCoin Minted:\n")
        print(json.dumps(mint_result["meritcoin"], indent=2))

        # === Log the transformation to the XP ledger
        commit_entry = log_commit(
            user_id=user_id,
            level=level,
            xp=950,
            reason="Completed Soulform Trial",
            traits_snapshot=valid_tree,
            soulform=mock_soulform
        )

        print("\n📜 XP Commit Logged:\n")
        print(json.dumps(commit_entry, indent=2))

        # === Generate symbolic payload for EdenQuest
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

    else:
        print("\n❌ Soulform Minting Failed:\n")
        print(json.dumps(mint_result, indent=2))

else:
    print("\n⚠️ Soulform Threshold Not Met – No Transformation Triggered.\n")
