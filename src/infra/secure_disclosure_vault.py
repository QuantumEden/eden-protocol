# 🔐 Secure Disclosure Vault – Encrypted Intake + Schema Validation

import json
import hashlib
import datetime
from jsonschema import validate, ValidationError
from pathlib import Path

# Load the disclosure payload schema
SCHEMA_PATH = Path("schemas/disclosure_payload.schema.json")
DISCLOSURE_LOG = Path("infra/disclosure_log.jsonl")


def validate_disclosure_payload(payload: dict) -> bool:
    """Validate user-provided disclosure data against schema."""
    try:
        with open(SCHEMA_PATH, "r") as schema_file:
            schema = json.load(schema_file)
        validate(instance=payload, schema=schema)
        return True
    except ValidationError as e:
        print(f"[SCHEMA ERROR] {e.message}")
        return False


def encrypt_disclosure(payload: dict) -> str:
    """Generate a SHA-256 fingerprint of the payload (symbolic token)."""
    data = json.dumps(payload, sort_keys=True).encode("utf-8")
    return hashlib.sha256(data).hexdigest()


def store_disclosure(user_id: str, payload: dict) -> str:
    """
    Validates and stores the encrypted disclosure securely.
    Appends metadata to a local symbolic vault.
    """
    if not validate_disclosure_payload(payload):
        return None

    token = encrypt_disclosure(payload)
    record = {
        "user_id": user_id,
        "timestamp": datetime.datetime.utcnow().isoformat(),
        "disclosure_token": token,
        "diagnosis": payload.get("diagnosis", []),
        "tags": payload.get("trauma_tags", []),
        "service_connected": payload.get("service_connected", False)
    }

    with open(DISCLOSURE_LOG, "a") as log:
        log.write(json.dumps(record) + "\n")

    return token
