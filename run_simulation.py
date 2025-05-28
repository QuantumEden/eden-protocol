#!/usr/bin/env python3
"""
Eden Protocol Simulation Runner

This script sets PYTHONPATH dynamically and runs any simulation script
in a symbolic context. Ensures consistent runtime environment.

Usage:
    python3 run_simulation.py <simulation_script_path>
"""

import os
import sys
import subprocess
from datetime import datetime

# Define repo root and src for import paths
repo_root = os.path.dirname(os.path.abspath(__file__))
src_path = os.path.join(repo_root, "src")

# Set environment path for downstream imports
os.environ["PYTHONPATH"] = f"{repo_root}:{src_path}"

if len(sys.argv) < 2:
    print("❌ Usage: python3 run_simulation.py <simulation_script_path>")
    sys.exit(1)

script_path = sys.argv[1]

if not os.path.exists(script_path):
    print(f"❌ Simulation script not found: {script_path}")
    sys.exit(1)

print("\n🔁 Running Eden Simulation –", datetime.utcnow().isoformat(), "UTC")
print("📜 Script:", script_path)
print("🧠 PYTHONPATH:", os.environ["PYTHONPATH"])
print("—" * 60)

# Execute simulation script
result = subprocess.run([sys.executable, script_path])

# Exit with child return code
sys.exit(result.returncode)
