# /src/mods/mod_loader.py

"""
Eden Mod Loader — DAO-Approved Symbolic Module Integrator

Loads, verifies, and registers symbolic mod content into the Eden Protocol runtime.
Each mod must include a valid mod_manifest.json and pass integrity + DAO checks.
"""

import json
import os
from src.dao.mod_registry import is_mod_approved

MOD_DIRECTORY = "community_mods"

class ModLoader:
    def __init__(self):
        self.loaded_mods = {}

    def load_mod(self, mod_id):
        mod_path = os.path.join(MOD_DIRECTORY, mod_id, "mod_manifest.json")
        if not os.path.exists(mod_path):
            raise FileNotFoundError(f"Missing manifest for mod: {mod_id}")

        with open(mod_path, 'r') as f:
            manifest = json.load(f)

        if not is_mod_approved(mod_id):
            raise PermissionError(f"Mod {mod_id} has not been DAO-approved.")

        self.loaded_mods[mod_id] = manifest
        print(f"✅ Loaded mod: {mod_id} — Trait: {manifest['target_trait']} | XP: {manifest['xp_value']}")
        return manifest

    def list_loaded(self):
        return list(self.loaded_mods.keys())


# Example use case
if __name__ == "__main__":
    loader = ModLoader()
    try:
        loader.load_mod("tai_chi_001")
    except Exception as e:
        print("Error loading mod:", str(e))
    print("Loaded mods:", loader.list_loaded())
