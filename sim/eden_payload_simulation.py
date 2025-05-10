# Eden Payload Simulation – Validate Full Data Output

from src.controllers.eden_payload_generator import generate_eden_payload
import json

print("\n=== Eden Protocol: Full Payload Simulation ===\n")

# Simulated input profile
profile = {
    "mbti": "INFJ",
    "iq": 133,
    "eq": 118,
    "moral": "care"
}

# Generate the full output package
payload = generate_eden_payload("user_alpha", profile, "eden_secret")

# Print it cleanly
print(json.dumps(payload, indent=2))
