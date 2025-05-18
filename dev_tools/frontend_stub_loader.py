# frontend_stub_loader.py – Eden Protocol UI Sync Simulation
# Simulates Eden Protocol backend payload generation for frontend display

import os
import sys
import json
import random

# Adjust path for local module access (assuming standard repo layout)
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from eden_payload_generator.eden_payload_generator import generate_eden_payload

# Simulated user session (normally captured during onboarding)
sample_user_id = f"user_{random.randint(1000, 9999)}"

sample_profile = {
    "mbti": "INTJ",
    "iq": 140,
    "eq": 120,
    "moral": "care",
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
        "activated_at": "2025-05-17T10:00:00Z"
    }
}

def main():
    print("\n🔄 Generating Eden Payload for Frontend...\n")
    payload = generate_eden_payload(
        user_id=sample_user_id,
        user_profile=sample_profile,  # ✅ Corrected parameter name
        secret_key="dev_stub_key_123"
    )

    print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()
