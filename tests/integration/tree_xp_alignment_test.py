# tests/integration/tree_xp_alignment_test.py – Eden Protocol Integration Test
# Validates that trait growth aligns with XP gain and soulform eligibility logic

import sys, os, json
from datetime import datetime

# === Path Patching for Imports ===
current_dir = os.path.dirname(__file__)
repo_root = os.path.abspath(os.path.join(current_dir, '..', '..'))
sys.path.insert(0, os.path.join(repo_root, 'src'))
sys.path.insert(0, os.path.join(repo_root, 'infra'))

# === Module Imports ===
from eden_payload_generator.eden_payload_generator import generate_eden_payload
from infra.xp.meritcoin_minter import mint_meritcoin
from infra.xp.meritcoin_ledger import log_commit

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

def test_tree_alignment():
    """
    Ensures soulform minting works when traits and level exceed thresholds.
    """
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

    payload = generate_eden_payload(user_id, mock_profile, secret_key="tree_align_secret")
    tree = payload["tree_traits"]
    level = 8
    soulform_id = mock_profile["current_soulform"]["id"]

    mint = mint_meritcoin(user_id, level, tree, soulform_id=soulform_id)
    assert mint["success"], "❌ Soulform minting failed despite level and valid traits"

    for trait, required in TREE_PASS_THRESHOLD.items():
        actual = tree.get(trait, 0)
        assert actual >= required, f"❌ Trait '{trait}' below threshold: {actual} < {required}"

    commit = log_commit(
        user_id=user_id,
        level=level,
        xp=1020,
        reason="Passed Celestial Trial",
        soulform=mock_profile["current_soulform"],
        traits_snapshot=tree
    )

    assert commit["user_id"] == user_id, "❌ Commit failed to log correctly"

    return payload, mint, commit


# === CLI Manual Diagnostic Run ===
if __name__ == "__main__":
    print("\n🌳 Running Tree Alignment Integration Test...\n")
    payload, mint, commit = test_tree_alignment()
    print("🌲 Tree Traits:", json.dumps(payload["tree_traits"], indent=2))
    print("\n🪙 Mint Result:", json.dumps(mint, indent=2))
    print("\n📜 Commit Log:", json.dumps(commit, indent=2))
    print("\n✅ Tree alignment test passed.\n")
