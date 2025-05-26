# sim/edenquest_payload_test.py – Eden Protocol Simulation
# End-to-end test: payload ➝ quest ➝ modifiers ➝ soulform ➝ DAO hooks

import sys, os
import json
from datetime import datetime

# === Import Path Setup ===
base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, os.path.join(base_path, 'src'))
sys.path.insert(0, os.path.join(base_path, 'sim'))

# === Core Modules ===
from eden_payload_generator.eden_payload_generator import generate_eden_payload
from edenquest_engine.edenquest_engine import generate_quest
from token_router_stub import inject_soulform_payload

# === Mock User Profile ===
mock_profile = {
    "mbti": "INFJ",
    "iq": 132,
    "eq": 125,
    "moral": "care",
    "sacred_path": "Taoism",
    "group_opt_in": True,
    "disclosure": {
        "diagnosis": ["PTSD", "depression"],
        "trauma_tags": ["combat", "loss"],
        "service_connected": True
    },
    "current_soulform": {
        "id": "phoenix",
        "name": "Ashborn Phoenix",
        "elemental_affinity": "Fire",
        "activated_at": datetime.utcnow().isoformat() + "Z"
    }
}

# === Step 1: Generate Raw Payload ===
user_id = "seer_demo_001"
secret_key = "sacred_key_001"
payload = generate_eden_payload(user_id, mock_profile, secret_key)

# === Step 2: Inject Soulform Visuals ===
payload = inject_soulform_payload(user_id, mock_profile)

# === Step 3: Format Tree for Quest Engine ===
tree = {
    key: {"score": score}
    for key, score in payload.get("tree_traits", {}).items()
}

# === Step 4: Generate Symbolic Quest ===
quest = generate_quest(tree, mock_profile)

# === Output Results ===
print("\n=== 🔮 EdenQuest Test Output ===\n")
print(json.dumps({
    "payload": payload,
    "generated_quest": quest
}, indent=2))
