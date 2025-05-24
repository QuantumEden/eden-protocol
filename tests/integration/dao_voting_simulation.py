# dao_voting_simulation.py – Eden Protocol DAO Proposal and Voting Test
# Simulates DAO onboarding, proposal creation, and symbolic vote casting with ritual and zkXP integration

import sys, os, json
from datetime import datetime

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'src')))

from eden_payload_generator.eden_payload_generator import generate_eden_payload
from dao.group_vote_handler import GroupVoteHandler

# === Step 1: Create DAO-eligible payload
profile = {
    "mbti": "ENTJ",
    "iq": 145,
    "eq": 125,
    "moral": "justice",
    "sacred_path": "Ethical Pragmatism",
    "group_opt_in": True,
    "current_soulform": {
        "id": "seraph",
        "name": "Wings of Conviction",
        "elemental_affinity": "Air",
        "activated_at": datetime.utcnow().isoformat() + "Z"
    }
}

user_id = "justice_vote_777"
secret_key = "key_777"

payload = generate_eden_payload(user_id, profile, secret_key)

print("\n🌱 DAO-Eligible Payload:")
print(json.dumps(payload, indent=2))

assert payload["eligible_for_dao"] is True, "❌ Payload is not DAO eligible"

# === Step 2: Submit a proposal
vote_handler = GroupVoteHandler()

proposal = vote_handler.submit_proposal(
    group_id="eden_dao",
    proposal_title="Establish Lunar Shrine",
    proposal_type="ritual_structure",
    proposed_by=user_id,
    merit_level=payload["merit_level"],
    soulform_id="seraph",
    ritual_required=True
)

print("\n📜 Proposal Submitted:")
print(json.dumps(proposal, indent=2))

# === Step 3: Simulate symbolic voting
vote_handler.cast_vote(proposal["proposal_id"], "seer_011", True, 10, soulform_id="phoenix")
vote_handler.cast_vote(proposal["proposal_id"], "healer_022", True, 8, soulform_id="seraph")
vote_handler.cast_vote(proposal["proposal_id"], "rogue_999", False, 6, soulform_id="shadow")

# === Step 4: Tally with ritual and zkXP hash
zkxp_hash = "zkxp-vote-001"
tally = vote_handler.tally_votes(
    proposal_id=proposal["proposal_id"],
    zkxp_commit_hash=zkxp_hash,
    ritual_verified=True
)
status = vote_handler.get_proposal_status(proposal["proposal_id"])

print("\n🗳️ Vote Tally:")
print(json.dumps(tally, indent=2))
print("📌 Proposal Status:", status)

# === Final assertions
assert tally["result"] in ["approved", "rejected"], "❌ Invalid tally result"
assert isinstance(proposal["votes"], dict), "❌ Vote record not created"
assert len(proposal["votes"]) == 3, "❌ Incorrect number of votes recorded"

print("\n✅ DAO voting simulation complete.\n")
