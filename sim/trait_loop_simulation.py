# sim/trait_loop_simulation.py
# Simulates Tree of Life growth → XP logging → soulform ritual trigger

from src.tree_of_life.tree_of_life_engine import grow_branch, get_default_tree
from src.xp.meritcoin_ledger import log_commit
from src.soulform.soulform_eligibility import check_soulform_eligibility, get_default_thresholds
from infra.voice_response_stub import speak

from datetime import datetime
import json
import random
import uuid

# Configuration
USER_ID = "seer_alch_011"
START_LEVEL = 9
XP_PER_GROWTH = 125
GROWTH_ITERATIONS = 6


def simulate_trait_growth_loop():
    """
    Simulates repeated trait growth and logs XP commits.
    Triggers soulform readiness if thresholds are met.
    """
    tree = get_default_tree()
    trait_keys = list(tree.keys())
    soulform_triggered = False

    for i in range(GROWTH_ITERATIONS):
        print(f"\n🌿 Growth Cycle {i+1} of {GROWTH_ITERATIONS}")
        
        # Choose random trait
        trait = random.choice(trait_keys)
        tree = grow_branch(tree, trait, amount=5)
        
        print(f"🧠 Trait '{trait}' grew to {tree[trait]}")

        # Simulate XP commit
        entry = log_commit(
            user_id=USER_ID,
            level=START_LEVEL + i,
            xp=XP_PER_GROWTH,
            reason=f"Trait {trait} grew in cycle {i+1}",
            traits_snapshot=tree
        )

        print(f"🪙 XP Commit Logged: {entry['meritcoin_id']}")

        # Check for soulform readiness
        if not soulform_triggered:
            thresholds = get_default_thresholds()
            if check_soulform_eligibility(tree, thresholds):
                print("✨ Soulform threshold reached!")
                speak("soulform_ready")
                soulform_triggered = True

    print("\n✅ Simulation complete.\n")
    print(json.dumps(tree, indent=2))


# === Execute Simulation ===
if __name__ == "__main__":
    print("🔁 Initiating Tree of Life growth simulation...")
    simulate_trait_growth_loop()
