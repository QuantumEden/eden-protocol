"""
Eden Payload Simulation – Minimal Diagnostic Test

Simulates a payload generation request for a symbolic INTJ profile
following the Hermetic sacred path. This tests core routing logic
in eden_payload_generator under basic user input conditions.
"""

import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

import json
from eden_payload_generator.eden_payload_generator import generate_eden_payload

# 🔍 Simulated User Profile
profile = {
    "mbti": "INTJ",
    "iq": 140,
    "eq": 120,
    "moral": "truth",
    "sacred_path": "Hermeticism",
    "group_opt_in": False
}

user_id = "observer_000"
secret_key = "vault_key_123"

# 🧪 Run Payload Generation
payload = generate_eden_payload(user_id, profile, secret_key)

print("\n=== Eden Protocol Payload Diagnostic ===\n")
print(json.dumps(payload, indent=2))
