# frontend_stub_loader.py

"""
Simulates Eden Protocol backend payload generation for frontend development.
Use this script to generate real-time test data for UI rendering engines.
"""

import json
import random
from eden_payload_generator import generate_eden_payload  # Fixed import path

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
    }
}

# Generate payload for frontend display
def main():
    print("\n🔄 Generating Eden Payload for Frontend...\n")
    payload = generate_eden_payload(
        user_id=sample_user_id,
        profile_dict=sample_profile,
        secret_key="dev_stub_key_123"
    )

    # Pretty print for developer testing
    print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()
