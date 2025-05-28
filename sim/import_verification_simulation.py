# sim/import_verification_simulation.py
# Eden Protocol – Modular Import Audit Tool
# Detects outdated or incorrect import paths and suggests updates

import os
from datetime import datetime

# === Constants ===
REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
SCRIPT_NAME = "import_verification_simulation.py"
SKIP_DIRS = {'.git', '__pycache__'}

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
scanned_count = 0

def scan_python_files():
    global scanned_count
    for dirpath, dirnames, filenames in os.walk(REPO_ROOT):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
        for fname in filenames:
            if fname.endswith(".py") and fname != SCRIPT_NAME:
                full_path = os.path.join(dirpath, fname)
                scanned_count += 1
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
    print(f"\n🔍 Eden Protocol Import Path Diagnostic – {datetime.utcnow().isoformat()}Z\n")
    scan_python_files()

    print(f"🗂️  Scanned {scanned_count} Python files\n")

    if flagged_files:
        print("🚨 Import issues detected:\n")
        for entry in flagged_files:
            print(f" - {entry['file']}")
            print(f"   ⛔ Uses: {entry['bad']}")
            print(f"   ✅ Fix:  from {entry['fix']} import ...\n")
    else:
        print("✅ No broken or deprecated import paths found. Audit complete.")
