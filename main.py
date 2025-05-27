#!/usr/bin/env python3
"""
Eden Protocol: Ritual Ignition Sequence

This is the ceremonial entrypoint for the Eden Protocol.
It initiates the Daemon (Ego), consults the Council (Superego),
and synthesizes the insight through Eidelon (Unified Self).

Designed for symbolic testing, debugging, and enlightenment.
"""

from src.ai.diagnostic.daemon import run_diagnostic_daemon, get_latest_flags
from src.eidelon.eidelon_core import generate_eidelon_insight

def main():
    print("\n🜂 EIDELON IGNITION – INITIATING SYNTHETIC REFLECTION 🜂")

    # 🔍 Sample user ID for testing
    user_id = "seer_beta"

    # 🔧 Step 1: Run Daemon diagnostics
    print("→ Running Daemon diagnostic sweep...")
    flags = run_diagnostic_daemon(user_id)
    print(f"   🧪 Flags Detected: {flags if flags else 'None'}")

    # 🧠 Step 2: Generate symbolic insight from Eidelon
    print("→ Summoning Eidelon for reflection...")
    reflection = generate_eidelon_insight(user_id=user_id)

    # 🕯️ Step 3: Display final symbolic message
    print("\n╭──────────────────────────────────────────╮")
    print("│          EIDELON SYMBOLIC INSIGHT        │")
    print("╰──────────────────────────────────────────╯\n")
    print(reflection)

if __name__ == "__main__":
    main()
