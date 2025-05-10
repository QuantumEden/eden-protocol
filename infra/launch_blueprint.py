# /infra/launch_blueprint.py

"""
Eden Protocol Launch Blueprint

This script sets up the core file structure, DAO engine, and identity hash pool
for a new instance of the Eden system. Intended for symbolic testnet or real-world
cohort deployment (e.g. 25 veteran users).
"""

import os
import shutil

DIRECTORY_STRUCTURE = [
    "eden_instance/src/user_profiles",
    "eden_instance/src/dao/vote_logs",
    "eden_instance/src/security/hashes",
    "eden_instance/sim/user_events",
    "eden_instance/data/trees",
    "eden_instance/data/quests",
    "eden_instance/data/xp_logs",
    "eden_instance/logs/system_events",
    "eden_instance/docs/init_manifest"
]

INIT_FILES = [
    ("eden_instance/docs/init_manifest/README.md", "# Eden Protocol Instance Manifest\n\nGenerated from launch_blueprint.py\n\nUse this directory to document symbolic traits, seed users, and DAO proposals."),
    ("eden_instance/logs/system_events/boot.log", "[BOOT] Eden instance generated. Awaiting user soulbinding...")
]

def create_structure():
    if os.path.exists("eden_instance"):
        shutil.rmtree("eden_instance")
    for path in DIRECTORY_STRUCTURE:
        os.makedirs(path, exist_ok=True)

    for file_path, content in INIT_FILES:
        with open(file_path, "w") as f:
            f.write(content)

    print("\n[EDEN INSTANCE CREATED]\n")
    print("Directory: eden_instance/")
    print("Subsystems: DAO | User | XP | Quests | Tree | Events")

if __name__ == "__main__":
    create_structure()
