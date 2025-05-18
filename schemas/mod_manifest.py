# schemas/mod_manifest.py
# Loader to expose the Eden Mod Manifest JSON schema to Python modules

import os
import json

# Determine absolute path to the JSON schema file
SCHEMA_PATH = os.path.join(os.path.dirname(__file__), 'mod_manifest.schema.json')

# Load and expose the schema as a Python dictionary
with open(SCHEMA_PATH, 'r', encoding='utf-8') as f:
    mod_manifest = json.load(f)
