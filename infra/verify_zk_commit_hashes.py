# verify_zk_commit_hashes.py – Eden Protocol Infra
# Simulates integrity checks against XP commit logs via hashed proof

import json
import hashlib
from os.path import dirname, join
import sys

# Inject path to access ledger loader
sys.path.insert(0, join(dirname(__file__), '..', 'infra'))

from meritcoin_ledger import load_ledger

def hash_commit(entry):
    """
    Hashes the symbolic components of an XP commit to simulate ZK integrity.
    """
    base_string = f"{entry['user_id']}-{entry['level']}-{entry['xp']}-{entry['reason']}"
    if "soulform" in entry:
        base_string += f"-{entry['soulform']['id']}-{entry['soulform']['element']}"
    return hashlib.sha256(base_string.encode('utf-8')).hexdigest()

def verify_ledger_integrity():
    ledger = load_ledger()
    failed = []

    for entry in ledger:
        try:
            proof = hash_commit(entry)
            entry["zk_proof"] = proof
        except Exception as e:
            entry["zk_proof"] = "INVALID"
            failed.append(entry)

    print("\n=== ZK Commit Integrity Hashes ===\n")
    print(json.dumps(ledger, indent=2))

    if failed:
        print("\n⚠️ Failed Hashes Detected:\n")
        print(json.dumps(failed, indent=2))
    else:
        print("\n✅ All XP commits passed symbolic hash verification.")

if __name__ == "__main__":
    verify_ledger_integrity()
