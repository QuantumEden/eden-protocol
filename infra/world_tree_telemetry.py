# world_tree_telemetry.py – Eden Protocol Infra
# Logs World Tree snapshots to a persistent telemetry record

import json
import os
from datetime import datetime
from typing import Dict

# Define where to save telemetry logs
TELEMETRY_LOG_PATH = os.path.join(os.path.dirname(__file__), "world_tree_telemetry_log.json")

def load_telemetry_log():
    if os.path.exists(TELEMETRY_LOG_PATH):
        with open(TELEMETRY_LOG_PATH, "r") as f:
            return json.load(f)
    return []

def save_telemetry_snapshot(source: str, snapshot: Dict[str, any]):
    log = load_telemetry_log()
    log.append({
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "source": source,
        "data": snapshot
    })
    with open(TELEMETRY_LOG_PATH, "w") as f:
        json.dump(log, f, indent=2)

# Optional CLI usage
if __name__ == "__main__":
    # Simulated snapshot input
    sample_snapshot = {
        "world_tree": {
            "discipline": 72,
            "resilience": 78,
            "mindfulness": 70,
            "expression": 66,
            "physical_care": 62,
            "emotional_regulation": 69
        },
        "user_count": 245
    }

    save_telemetry_snapshot("world_tree_sync.py", sample_snapshot)
    print(f"✅ Snapshot saved to: {TELEMETRY_LOG_PATH}")
