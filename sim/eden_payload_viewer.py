import json
from eden_payload_generator.eden_payload_generator import generate_eden_payload

# Basic visualization of a sacred path payload
profile = {
    "mbti": "ENFJ",
    "iq": 128,
    "eq": 133,
    "moral": "care",
    "sacred_path": "Mythic Psychotherapy",
    "group_opt_in": True
}

user_id = "oracle_999"
secret_key = "glyph_mirror_key"

payload = generate_eden_payload(user_id, profile, secret_key)

print("\n=== Eden Protocol Payload Viewer ===\n")
for k, v in payload.items():
    print(f"{k}: {json.dumps(v, indent=2) if isinstance(v, (dict, list)) else v}")
