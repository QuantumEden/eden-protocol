# sim/mod_validation_simulation.py

"""
Mod Validation Simulation — Test and Verify Community Mod Effects

This simulation runs mock mod entries through:
- Manifest schema check
- XP and trait bounds validation
- DAO approval gating
- Tree of Life interaction simulation
"""

import sys, os
import json
from jsonschema import validate, ValidationError

# Fix for Codespaces and relative imports
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from schemas.mod_manifest import mod_manifest
from tree_of_life.tree_of_life_engine import TreeOfLife
from xp.xp_integrity import validate_xp_from_mod
from dao.mod_registry import is_mod_approved

MOD_TEST_PATH = "infra/mod_manifest_template.json"

def simulate_mod_activation(manifest_path):
    try:
        with open(manifest_path, 'r') as f:
            manifest = json.load(f)

        # Step 1 — Schema validation
        validate(instance=manifest, schema=mod_manifest)

        # Step 2 — DAO approval check
        if not is_mod_approved(manifest['mod_id']):
            raise PermissionError("Mod is not DAO-approved.")

        # Step 3 — XP validation logic
        validate_xp_from_mod(user_id="test_user", mod_id=manifest['mod_id'], amount=manifest['xp_value'])

        # Step 4 — Simulate trait effect
        tree = TreeOfLife()
        pre = tree.get_trait(manifest['target_trait'])
        tree.apply_mod_effect(manifest['target_trait'], manifest['xp_value'], manifest['mod_id'], "test_user")
        post = tree.get_trait(manifest['target_trait'])

        print(f"\n✅ Mod simulation successful! {manifest['target_trait']} increased from {pre} to {post}.\n")

    except ValidationError as ve:
        print("❌ Schema validation failed:", ve.message)
    except Exception as e:
        print("❌ Mod simulation error:", str(e))


if __name__ == "__main__":
    simulate_mod_activation(MOD_TEST_PATH)
