# sim/load_simulation_test.py – Eden Protocol Stress Simulation
# Simulates high-throughput user engagement and meritcoin minting

import sys, os
import json
import random
from time import time
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor

# Add src to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from eden_payload_generator.eden_payload_generator import generate_eden_payload
from infra.xp.meritcoin_minter import mint_meritcoin

# === Mock User Pool ===
mock_profiles = [
    {
        "user_id": f"load_test_{i:03}",
        "profile": {
            "mbti": random.choice(["INTJ", "INFJ", "ENFP", "ESTP"]),
            "iq": random.randint(110, 145),
            "eq": random.randint(100, 135),
            "moral": random.choice(["truth", "care", "justice", "loyalty"]),
            "sacred_path": random.choice(["Taoism", "Stoicism", "Logotherapy", "Hermeticism"]),
            "group_opt_in": bool(random.getrandbits(1)),
            "disclosure": {
                "diagnosis": ["PTSD"] if i % 3 == 0 else [],
                "trauma_tags": ["combat", "loss"] if i % 4 == 0 else [],
                "service_connected": i % 5 == 0
            }
        },
        "secret_key": f"stress_key_{i}"
    }
    for i in range(20)
]

# === Worker Function ===
def simulate_user(index: int, data: dict) -> dict:
    user_id = data["user_id"]
    profile = data["profile"]
    secret_key = data["secret_key"]
    timestamp = datetime.utcnow().isoformat() + "Z"

    try:
        payload = generate_eden_payload(user_id, profile, secret_key)
        tree = payload.get("tree_traits", {})
        level = 1 + payload["xp_awarded"] // 100
        soulform = profile.get("current_soulform", {}).get("id", "phoenix")

        result = mint_meritcoin(user_id, level, tree, soulform_id=soulform)

        return {
            "timestamp": timestamp,
            "user_id": user_id,
            "xp": payload["xp_awarded"],
            "level": level,
            "eligible": payload["eligible_for_dao"],
            "mint_success": result["success"],
            "reason": result.get("reason", None)
        }
    except Exception as e:
        return {
            "timestamp": timestamp,
            "user_id": user_id,
            "error": str(e)
        }

# === Run Load Simulation ===
if __name__ == "__main__":
    print("\n🚀 Running Eden Protocol Load Simulation...\n")
    start = time()

    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = [executor.submit(simulate_user, i, data) for i, data in enumerate(mock_profiles)]
        results = sorted([f.result() for f in futures], key=lambda r: r.get("user_id"))

    duration = time() - start

    print(json.dumps(results, indent=2))
    print(f"\n⏱️ Simulation completed in {duration:.2f} seconds.\n")
