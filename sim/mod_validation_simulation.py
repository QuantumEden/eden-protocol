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
from datetime import datetime
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
    print("\n🔧 Mod Validation Simulation – Starting...\n")

    try:
        with open(manifest_path, 'r') as f:
            manifest = json.load(f)

        print("📄 Step 1 — Validating mod schema...")
        validate(instance=manifest, schema=mod_manifest)
        print("✅ Schema validation passed.")

        required_fields = ["mod_id", "target_trait", "xp_value"]
        for field in required_fields:
            if field not in manifest:
                raise KeyError(f"Missing required manifest field: {field}")

        print(f"\n🛡️ Step 2 — Checking DAO approval for mod: {manifest['mod_id']}...")
        if not is_mod_approved(manifest['mod_id']):
            raise PermissionError("Mod is not DAO-approved.")
        print("✅ DAO approval granted.")

        print(f"\n📊 Step 3 — Validating XP: {manifest['xp_value']} for trait: {manifest['target_trait']}")
        validate_xp_from_mod(user_id="test_user", mod_id=manifest['mod_id'], amount=manifest['xp_value'])
        print("✅ XP validation passed.")

        print(f"\n🌳 Step 4 — Simulating Tree of Life effect on: {manifest['target_trait']}")
        tree = TreeOfLife()
        pre = tree.get_trait(manifest['target_trait'])
        tree.apply_mod_effect(
            trait=manifest['target_trait'],
            xp=manifest['xp_value'],
            mod_id=manifest['mod_id'],
            user_id="test_user"
        )
        post = tree.get_trait(manifest['target_trait'])

        print(f"\n🎉 Mod successfully simulated at {datetime.utcnow().isoformat()}Z")
        print(f"Trait '{manifest['target_trait']}' increased from {pre} ➜ {post}\n")

    except ValidationError as ve:
        print(f"❌ Schema validation failed: {ve.message}")
    except PermissionError as pe:
        print(f"⛔ DAO check failed: {str(pe)}")
    except KeyError as ke:
        print(f"❗ Manifest key error: {str(ke)}")
    except Exception as e:
        print(f"💥 Mod simulation error: {str(e)}")


if __name__ == "__main__":
    simulate_mod_activation(MOD_TEST_PATH)
