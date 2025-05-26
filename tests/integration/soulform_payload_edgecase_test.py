# tests/integration/soulform_payload_edgecase_test.py – Soulform Edgecase Validator
# Tests invalid or malformed payloads for DAO ritual injection simulation

import sys, os, json
from jsonschema import validate, ValidationError
from datetime import datetime

# === Path Patch ===
current_dir = os.path.dirname(__file__)
repo_root = os.path.abspath(os.path.join(current_dir, '..', '..'))
sys.path.insert(0, os.path.join(repo_root, 'sim'))

# === Stub Import ===
from token_router_stub import inject_soulform_payload

# === Soulform Payload Schema ===
soulform_schema = {
    "type": "object",
    "required": ["user_id", "soulform", "timestamp", "success", "status"],
    "properties": {
        "user_id": {"type": "string"},
        "soulform": {
            "type": "object",
            "required": ["id", "name", "elemental_affinity", "activated_at"],
            "properties": {
                "id": {"type": "string"},
                "name": {"type": "string"},
                "elemental_affinity": {"type": "string"},
                "activated_at": {"type": "string", "format": "date-time"}
            }
        },
        "timestamp": {"type": "string", "format": "date-time"},
        "success": {"type": "boolean"},
        "status": {"type": "string"}
    }
}

# === Valid Soulform for Control Test
valid_soulform = {
    "id": "lupus_exemplar",
    "name": "Lupus Exemplar",
    "elemental_affinity": "Shadow",
    "activated_at": datetime.utcnow().isoformat() + "Z"
}

# === Edgecase: Incomplete payload
malformed_soulform = {
    "id": "lupus_exemplar",
    # Missing 'name'
    "elemental_affinity": 404,  # Wrong type
    "activated_at": "now"       # Invalid format
}

# === Step 1: Test valid payload
valid_response = inject_soulform_payload("user_777", valid_soulform)

try:
    validate(instance=valid_response, schema=soulform_schema)
    print("\n✅ Valid soulform payload passed schema check.")
except ValidationError as e:
    print(f"\n❌ Valid payload failed validation: {e.message}")
    assert False, "Valid payload should not fail."

# === Step 2: Test malformed payload
invalid_response = inject_soulform_payload("user_777", malformed_soulform)

try:
    validate(instance=invalid_response, schema=soulform_schema)
    print("\n❌ Malformed payload passed when it should have failed.")
    assert False, "Malformed payload passed schema validation unexpectedly."
except ValidationError as e:
    print("\n✅ Malformed soulform payload correctly rejected.")
    print(f"Error: {e.message}")
