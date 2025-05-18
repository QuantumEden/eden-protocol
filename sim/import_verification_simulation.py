# sim/import_verification_simulation.py
# Eden Protocol – Modular Import Audit Tool
# Detects outdated or incorrect import paths and suggests updates

import os

# === Constants ===
REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
SCRIPT_NAME = "import_verification_simulation.py"

# === Rules to Audit ===
AUDIT_RULES = [
    {
        "bad": "infra.meritcoin_minter",
        "fix": "infra.xp.meritcoin_minter"
    },
    {
        "bad": "quest_modifier",
        "fix": "src.quest_engine.quest_modifier"
    },
    {
        "bad": "xp.leveling_system",
        "fix": "src.leveling_system.leveling_system"
    },
    {
        "bad": "xp.meritcoin_ledger",
        "fix": "infra.xp.meritcoin_ledger"
    }
]

flagged_files = []

def scan_python_files():
    for dirpath, _, filenames in os.walk(REPO_ROOT):
        for fname in filenames:
            if fname.endswith(".py") and fname != SCRIPT_NAME:
                full_path = os.path.join(dirpath, fname)
                try:
                    with open(full_path, "r", encoding="utf-8") as f:
                        content = f.read()
                        for rule in AUDIT_RULES:
                            if rule["bad"] in content:
                                relative_path = os.path.relpath(full_path, REPO_ROOT)
                                flagged_files.append({
                                    "file": relative_path,
                                    "bad": rule["bad"],
                                    "fix": rule["fix"]
                                })
                except Exception as e:
                    print(f"⚠️ Skipped unreadable file {fname}: {e}")

# === Execution ===
if __name__ == "__main__":
    print("\n🔍 Running Eden Protocol Import Path Diagnostic...\n")
    scan_python_files()

    if flagged_files:
        print("🚨 Import issues found:\n")
        for entry in flagged_files:
            print(f" - {entry['file']}")
            print(f"   ⛔ Uses: {entry['bad']}")
            print(f"   ✅ Fix:  from {entry['fix']} import ...\n")
    else:
        print("✅ No broken or deprecated import paths found. Audit complete.")
