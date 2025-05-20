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
    proposal = create.json()["proposal"]
    proposal_id = proposal["id"]

    # View All
    list_response = client.get("/api/dao/proposals", headers=headers)
    assert list_response.status_code == 200
    assert any(p["id"] == proposal_id for p in list_response.json())

    # View Specific
    detail = client.get(f"/api/dao/proposals/{proposal_id}", headers=headers)
    assert detail.status_code == 200
    assert detail.json()["id"] == proposal_id

    # Vote
    vote = client.post(f"/api/dao/proposals/{proposal_id}/vote", json={
        "vote": "yes"
    }, headers=headers)
    assert vote.status_code == 200
    assert vote.json()["proposal"]["votes"]["yes"] >= 1

    # Vote History
    history = client.get("/api/dao/user/seer/votes", headers=headers)
    assert history.status_code == 200
    assert any(v["proposal_id"] == proposal_id for v in history.json())
