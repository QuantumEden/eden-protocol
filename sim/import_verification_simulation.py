# sim/import_verification_simulation.py
# Eden Protocol – Import Path Audit Tool
# Detects improper imports of deprecated 'infra.meritcoin_minter' instead of 'infra.xp.meritcoin_minter'

import os

# Constants
REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
TARGET_IMPORT_BAD = "infra.meritcoin_minter"
TARGET_IMPORT_GOOD = "infra.xp.meritcoin_minter"
SELF_PATH = os.path.abspath(__file__)

flagged_files = []

def scan_python_files():
    for dirpath, _, filenames in os.walk(REPO_ROOT):
        for fname in filenames:
            if fname.endswith(".py"):
                full_path = os.path.join(dirpath, fname)

                # ✅ Skip scanning this file to avoid false positives
                if os.path.abspath(full_path) == SELF_PATH:
                    continue

                with open(full_path, "r", encoding="utf-8") as f:
                    content = f.read()
                    if TARGET_IMPORT_BAD in content:
                        relative_path = os.path.relpath(full_path, REPO_ROOT)
                        flagged_files.append(relative_path)

if __name__ == "__main__":
    print("\n🔍 Scanning for invalid 'meritcoin_minter' import paths...\n")
    scan_python_files()

    if flagged_files:
        print("🚨 The following files import from 'infra.meritcoin_minter' and should be updated to:")
        print(f"    ✅ Use: 'from infra.xp.meritcoin_minter import ...'\n")
        for file in flagged_files:
            print(f" - {file}")
    else:
        print("✅ No incorrect imports found. All references are clean.")
