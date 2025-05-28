import sys, os
import json
from datetime import datetime

# Add source directory to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from eden_payload_generator.eden_payload_generator import generate_eden_payload

def run_payload_loop_test():
    print("\n🔁 Eden Protocol – Batch Payload Generation Loop\n")

    for i in range(3):
        profile = {
            "mbti": "INTP",
            "iq": 135 + i,
            "eq": 115 + i,
            "moral": "freedom",
            "sacred_path": "Stoicism",
            "group_opt_in": i % 2 == 0
        }

        # Inject soulform test state on final loop
        if i == 2:
            profile["current_soulform"] = {
                "id": "phoenix",
                "name": "Ashborn Phoenix",
                "elemental_affinity": "Fire",
                "activated_at": datetime.utcnow().isoformat() + "Z"
            }

        user_id = f"test_subject_{i:03d}"
        secret_key = f"loop_key_{i:03d}"

        payload = generate_eden_payload(user_id, profile, secret_key)

        print(f"\n=== Payload {i} ({user_id}) ===")
        print(json.dumps(payload, indent=2))

    print("\n✅ Batch Payload Loop Complete\n")

if __name__ == "__main__":
    run_payload_loop_test()
