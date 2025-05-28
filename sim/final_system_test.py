# sim/final_system_test.py – Full Eden Protocol Simulation Pass
# Ensures DAO, XP, Soulform, and Tree logic are integrated properly

import sys, os
import json
from datetime import datetime

# === Patch import paths ===
base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, os.path.join(base_path, 'src'))
sys.path.insert(0, os.path.join(base_path, 'infra'))

# === Core imports ===
from eden_payload_generator.eden_payload_generator import generate_eden_payload
from xp.meritcoin_minter import mint_meritcoin
from xp.meritcoin_ledger import log_commit

def run_full_test():
    print("\n🧪 Starting Full Protocol Integration Test –", datetime.utcnow().isoformat(), "UTC\n")

    user_id = "seer_077"
    secret_key = "eden_777_key"

    profile = {
        "mbti": "INFJ",
        "iq": 132,
        "eq": 125,
        "moral": "truth",
        "sacred_path": "Logotherapy",
        "group_opt_in": True,
        "disclosure": {
            "diagnosis": ["PTSD", "depression"],
            "trauma_tags": ["combat", "betrayal"],
            "service_connected": True
        },
        "current_soulform": {
            "id": "phoenix",
            "name": "Ashborn Phoenix",
            "elemental_affinity": "Fire",
            "activated_at": datetime.utcnow().isoformat() + "Z"
        }
    }

    # === Step 1: Generate Eden Payload ===
    payload = generate_eden_payload(user_id, profile, secret_key)
    print("\n✅ [1] Payload Generated\n")
    print(json.dumps(payload, indent=2))

    # === Step 2: Mint Symbolic MeritCoin ===
    tree = payload.get("tree_traits", {})
    soulform_id = profile.get("current_soulform", {}).get("id", "unknown")

    if not tree:
        print("\n❌ Missing tree_traits – cannot mint MeritCoin.\n")
        return

    result = mint_meritcoin(user_id, 8, tree, soulform_id=soulform_id)

    if not result["success"]:
        print("\n❌ [2] MeritCoin Minting Failed:", result["reason"])
        return

    print("\n✅ [2] MeritCoin Minted:")
    print(json.dumps(result["meritcoin"], indent=2))

    # === Step 3: Log DAO Ritual Commit ===
    commit = log_commit(
        user_id=user_id,
        level=8,
        xp=payload.get("xp_awarded", 0),
        reason="Integrated DAO Trial Complete",
        traits_snapshot=tree,
        soulform=profile.get("current_soulform", {}),
        timestamp=datetime.utcnow().isoformat() + "Z"
    )

    print("\n📜 [3] Ledger Commit Recorded:")
    print(json.dumps(commit, indent=2))

if __name__ == "__main__":
    run_full_test()
