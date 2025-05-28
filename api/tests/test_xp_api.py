# api/tests/test_xp_api.py
# Eden Protocol – XP + MeritCoin API Tests (Updated)

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


traits_snapshot = {
    "discipline": 60,
    "resilience": 72,
    "mindfulness": 69,
    "expression": 55,
    "physical_care": 65,
    "emotional_regulation": 71
}


def test_commit_xp():
    headers = get_auth_header()
    response = client.post("/api/xp/seer_alch_011/commit", json={
        "level": 5,
        "xp": 300,
        "reason": "Completed World Tree Calibration Ritual",
        "traits_snapshot": traits_snapshot
    }, headers=headers)
    assert response.status_code == 200
    data = response.json()
    assert "commit" in data
    assert "commit_hash" in data["commit"]
    assert data["commit"]["xp"] == 300


def test_disclosure_reward():
    headers = get_auth_header()
    response = client.post("/api/xp/seer_alch_011/disclosure", json={
        "level": 5,
        "truth": 80,
        "vulnerability": 70,
        "traits_snapshot": traits_snapshot
    }, headers=headers)
    assert response.status_code == 200
    data = response.json()
    assert "xp_awarded" in data
    assert data["xp_awarded"] > 0


def test_mod_xp_grant():
    headers = get_auth_header()
    response = client.post("/api/xp/seer_alch_011/validate/mod", json={
        "level": 6,
        "xp": 150,
        "traits_snapshot": traits_snapshot
    }, headers=headers)
    assert response.status_code == 200
    data = response.json()
    assert "commit" in data
    assert data["commit"]["xp"] == 150
    assert "mod_validated" in data["commit"]
