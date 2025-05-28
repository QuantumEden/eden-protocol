# api/tests/test_dao_api.py
# Eden Protocol – DAO Governance API Tests

from fastapi.testclient import TestClient
from api.main import app

client = TestClient(app)


def get_auth_header():
    login = client.post("/api/auth/login", json={
        "username": "seer",
        "password": "eden123"
    })
    assert login.status_code == 200
    token = login.json()["access_token"]
    return {"Authorization": f"Bearer {token}"}


def test_create_proposal_and_vote():
    headers = get_auth_header()

    # Create Proposal
    create = client.post("/api/dao/proposals", json={
        "title": "Unify Avatar with Tree",
        "description": "Mandate symbolic alignment before soulform unlock."
    }, headers=headers)
    assert create.status_code == 200
    proposal = create.json().get("proposal", {})
    proposal_id = proposal.get("id")
    assert proposal_id is not None

    # View All Proposals
    list_response = client.get("/api/dao/proposals", headers=headers)
    assert list_response.status_code == 200
    all_proposals = list_response.json()
    assert any(p.get("id") == proposal_id for p in all_proposals)

    # View Specific Proposal
    detail = client.get(f"/api/dao/proposals/{proposal_id}", headers=headers)
    assert detail.status_code == 200
    proposal_details = detail.json()
    assert proposal_details.get("id") == proposal_id

    # Submit Vote
    vote = client.post(f"/api/dao/proposals/{proposal_id}/vote", json={
        "vote": "yes"
    }, headers=headers)
    assert vote.status_code == 200
    updated_proposal = vote.json().get("proposal", {})
    assert updated_proposal.get("votes", {}).get("yes", 0) >= 1

    # Retrieve Vote History
    history = client.get("/api/dao/user/seer/votes", headers=headers)
    assert history.status_code == 200
    vote_history = history.json()
    assert any(v.get("proposal_id") == proposal_id for v in vote_history)
