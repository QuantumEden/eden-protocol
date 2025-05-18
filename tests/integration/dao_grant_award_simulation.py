# dao_grant_award_simulation.py – Eden Protocol Grant Dispenser Integration
# Simulates DAO-approved grant awards, including XP and symbolic MeritCoin

import sys, os, json
from datetime import datetime

# Fix relative import path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'src')))

from src.infra.dao.grant_dispenser import grant_xp, grant_meritcoin, get_grant_log
from infra.xp.meritcoin_ledger import log_commit  # ✅ FIXED: Corrected import path
from infra.xp.meritcoin_minter import mint_meritcoin  # ✅ FIXED: Corrected import path
from src.eden_payload_generator.eden_payload_generator import generate_eden_payload

# === Step 1: Simulate grant recipient profile
user_id = "builder_trial_005"
secret_key = "honorpath_key"
profile = {
    "mbti": "ISFP",
    "iq": 122,
    "eq": 105,
    "moral": "loyalty",
    "sacred_path": "Stoicism",
    "group_opt_in": True,
    "current_soulform": {
        "id": "wyrm",
        "name": "Twilight Serpent",
        "elemental_affinity": "Earth",
        "activated_at": datetime.utcnow().isoformat() + "Z"
    }
}

# === Step 2: Generate Eden payload
payload = generate_eden_payload(user_id, profile, secret_key)
print("\n🌿 DAO Payload Snapshot:")
print(json.dumps(payload, indent=2))

# === Step 3: Grant XP via DAO ritual system
xp_grant = grant_xp(user_id, 90, "Co-authored Sacred Architecture Proposal")
print("\n📈 DAO XP Grant Issued:")
print(json.dumps(xp_grant, indent=2))

# === Step 4: Attempt symbolic MeritCoin mint
mint = mint_meritcoin(user_id, level=8, tree_traits=payload["tree_traits"], soulform_id="wyrm")

if mint["success"]:
    print("\n🪙 DAO MeritCoin Minted:")
    print(json.dumps(mint["meritcoin"], indent=2))

    # === Step 5: Log grant-linked soulform commit
    commit = log_commit(
        user_id=user_id,
        level=8,
        xp=900,
        reason="DAO Grant Ritual Completion",
        soulform=profile["current_soulform"]
    )

    print("\n📜 Soulform XP Commit Logged:")
    print(json.dumps(commit, indent=2))

    # === Step 6: Add DAO grant to log
    merit_grant = grant_meritcoin(
        user_id,
        mint["meritcoin"]["meritcoin_id"],
        level=8,
        soulform_id="wyrm"
    )

    print("\n🔐 DAO Grant Log Entry:")
    print(json.dumps(merit_grant, indent=2))

else:
    print("\n❌ MeritCoin minting failed:", mint["reason"])

# === Final DAO log print
print("\n📚 Current DAO Grant Log:")
print(json.dumps(get_grant_log(), indent=2))

print("\n✅ DAO grant simulation complete.")
