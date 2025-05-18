# sim/import_path_checker.py
# Eden Protocol – Import Path Consistency Checker
# Scans for deprecated or incorrect import references (e.g., infra.meritcoin_minter instead of infra.xp.meritcoin_minter)

import os

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

# 🔍 Path rules to validate
IMPORT_RULES = {
    "infra.meritcoin_minter": "infra.xp.meritcoin_minter",
    "infra.meritcoin_ledger": "infra.xp.meritcoin_ledger",
    "quest_modifier": "src.quest_engine.quest_modifier",
    "leveling_system": "src.leveling_system.leveling_system",
    "eden_payload_generator": "src.eden_payload_generator.eden_payload_generator"
}

flagged_usages = []

def scan_repo_for_import_errors():
    for dirpath, _, filenames in os.walk(REPO_ROOT):
        for fname in filenames:
            if fname.endswith(".py"):
                fpath = os.path.join(dirpath, fname)
                with open(fpath, "r", encoding="utf-8") as f:
                    content = f.read()
                    for bad_path, correct_path in IMPORT_RULES.items():
                        if bad_path in content and correct_path not in content:
                            rel_path = os.path.relpath(fpath, REPO_ROOT)
                            flagged_usages.append((rel_path, bad_path, correct_path))

if __name__ == "__main__":
    print("\n🔎 Running Import Path Consistency Audit...\n")
    scan_repo_for_import_errors()

    if not flagged_usages:
        print("✅ All import paths conform to Phase 17 standards.")
    else:
        print("🚨 Import path issues detected:\n")
        for file, bad, correct in flagged_usages:
            print(f" - {file}")
            print(f"   → Replace `{bad}` with `{correct}`\n")
