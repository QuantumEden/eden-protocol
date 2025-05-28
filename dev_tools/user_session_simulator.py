# dev_tools/user_session_simulator.py – Eden Protocol Dev Tool
# Simulates user payloads for interface validation and introspection

import sys
import os
import json
from datetime import datetime

# Ensure module resolution
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from eden_payload_generator.eden_payload_generator import generate_eden_payload
from src.ai.diagnostic.daemon import run_diagnostic_daemon
from src.eidelon.eidelon_core import invoke_eidelon

# Define mock user profiles
mock_users = [
    {
        "user_id": "user_alch_001",
        "profile": {
            "mbti": "INFJ",
            "iq": 135,
            "eq": 120,
            "moral": "truth",
            "sacred_path": "Hermeticism",
            "group_opt_in": True,
            "disclosure": {
                "diagnosis": ["PTSD"],
                "trauma_tags": ["combat", "insomnia"],
                "service_connected": True
            },
            "current_soulform": {
                "id": "phoenix",
                "name": "Ashborn Phoenix",
                "elemental_affinity": "Fire",
                "activated_at": "2025-05-14T11:00:00Z"
            }
        },
        "secret_key": "mock_key_phoenix"
    },
    {
        "user_id": "user_sage_002",
        "profile": {
            "mbti": "INTP",
            "iq": 142,
            "eq": 108,
            "moral": "justice",
            "sacred_path": "Stoicism",
            "group_opt_in": False,
            "disclosure": {
                "diagnosis": ["depression"],
                "trauma_tags": ["loss", "betrayal"],
                "service_connected": False
            },
            "current_soulform": {
                "id": "dragon",
                "name": "Verdant Wyrm",
                "elemental_affinity": "Air",
                "activated_at": "2025-05-12T08:00:00Z"
            }
        },
        "secret_key": "mock_key_dragon"
    }
]

def run_simulation():
    for user in mock_users:
        print(f"\n🌐 Simulating Eden Payload: {user['user_id']}")
        payload = generate_eden_payload(user['user_id'], user['profile'], user['secret_key'])
        print("📦 Payload Output:")
        print(json.dumps(payload, indent=2))

        print(f"\n🧠 Running Daemon Diagnostics for {user['user_id']}...")
        flags = run_diagnostic_daemon(user['user_id'])
        print(json.dumps(flags, indent=2))

        print(f"\n✨ Invoking Eidelon for {user['user_id']}...\n")
        introspection = invoke_eidelon(user['user_id'], context="user_session_simulation")
        print(json.dumps(introspection, indent=2))

if __name__ == "__main__":
    run_simulation()
