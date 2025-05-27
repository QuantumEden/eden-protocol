#!/usr/bin/env python3
"""
Eden Protocol Simulation Runner

This script properly sets PYTHONPATH before running simulation scripts.
Usage: python3 run_simulation.py <simulation_script_path>
"""

import os
import sys
import subprocess

# Set PYTHONPATH to include the repository root and src directory
repo_root = os.path.dirname(os.path.abspath(__file__))
src_path = os.path.join(repo_root, "src")
os.environ["PYTHONPATH"] = f"{repo_root}:{src_path}"

if len(sys.argv) < 2:
    print("Usage: python3 run_simulation.py <simulation_script_path>")
    sys.exit(1)

script_path = sys.argv[1]
result = subprocess.run([sys.executable, script_path])
sys.exit(result.returncode)
