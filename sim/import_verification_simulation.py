# sim/import_verification_simulation.py
# Eden Protocol – Import Path Audit Tool (Corrected Version)
# Detects improper imports of deprecated 'infra.meritcoin_minter' instead of 'infra.xp.meritcoin_minter'

import os

# Constants
REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
DEPRECATED_IMPORT = "from infra.meritcoin_minter"
CORRECTED_IMPORT = "from infra.xp.meritcoin_minter"

flagged_files = []

def scan_python_files():
    for dirpath, _, filenames in os.walk(REPO_ROOT):
        for fname in filenames:
            if fname.endswith(".py"):
                full_path = os.path.join(dirpath, fname)
                try:
                    with open(full_path, "r", encoding="utf-8") as f:
                        lines = f.readlines()
                        for i, line in enumerate(lines):
                            if DEPRECATED_IMPORT in line:
                                relative_path = os.path.relpath(full_path, REPO_ROOT)
                                flagged_files.append((relative_path, i + 1, line.strip()))
                                break
                except Exception as e:
                    print(f"⚠️ Skipped {full_path}: {e}")

if __name__ == "__main__":
    print("\n🔍 Scanning for deprecated 'meritcoin_minter' import paths...\n")
    scan_python_files()

    if flagged_files:
        print("🚨 Deprecated imports found! Please update to:")
        print(f"    ✅ '{CORRECTED_IMPORT}'\n")
        for file, line_number, line in flagged_files:
            print(f" - {file}:{line_number} → {line}")
    else:
        print("✅ No deprecated imports found. All references are clean.")
