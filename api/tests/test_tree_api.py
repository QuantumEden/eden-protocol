# api/tests/test_tree_api.py
# Eden Protocol – Tree of Life API Tests (Updated for Synchronicity Model)

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


def test_get_tree():
    headers = get_auth_header()
    r = client.get("/api/tree/seer_alch_011", headers=headers)
    assert r.status_code == 200
    body = r.json()
    assert isinstance(body, dict)
    assert "discipline" in body


def test_trait_growth():
    headers = get_auth_header()
    r = client.put("/api/tree/seer_alch_011/trait", json={
        "trait": "resilience",
        "amount": 7
    }, headers=headers)
    assert r.status_code == 200
    body = r.json()
    assert body["resilience"] >= 7


def test_decay():
    headers = get_auth_header()
    r = client.post("/api/tree/seer_alch_011/decay", json={
        "decay_map": {
            "expression": 3,
            "physical_care": 2
        }
    }, headers=headers)
    assert r.status_code == 200
    body = r.json()
    assert "expression" in body
    assert isinstance(body["expression"], int)


def test_health_check():
    headers = get_auth_header()
    r = client.get("/api/tree/seer_alch_011/health", headers=headers)
    assert r.status_code == 200
    body = r.json()
    assert "health_score" in body
    assert isinstance(body["health_score"], (int, float))


def test_disclosure_reflection():
    headers = get_auth_header()
    r = client.post("/api/tree/seer_alch_011/reflection", json={
        "truth_level": 80,
        "emotional_intensity": 70
    }, headers=headers)
    assert r.status_code == 200
    body = r.json()
    assert "updated_traits" in body
    assert isinstance(body["updated_traits"], dict)
