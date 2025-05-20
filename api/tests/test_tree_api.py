# api/tests/test_tree_api.py
# Eden Protocol – Tree of Life API Tests

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


def test_get_tree():
    headers = get_auth_header()
    response = client.get("/api/tree/seer_alch_011", headers=headers)
    assert response.status_code == 200
    assert "discipline" in response.json()


def test_trait_growth():
    headers = get_auth_header()
    response = client.put("/api/tree/seer_alch_011/trait", json={
        "trait": "resilience",
        "amount": 7
    }, headers=headers)
    assert response.status_code == 200
    assert response.json()["resilience"] >= 7


def test_decay():
    headers = get_auth_header()
    response = client.post("/api/tree/seer_alch_011/decay", json={
        "decay_map": {
            "expression": 3,
            "physical_care": 2
        }
    }, headers=headers)
    assert response.status_code == 200
    assert "expression" in response.json()


def test_health_check():
    headers = get_auth_header()
    response = client.get("/api/tree/seer_alch_011/health", headers=headers)
    assert response.status_code == 200
    assert "health_score" in response.json()


def test_disclosure_reflection():
    headers = get_auth_header()
    response = client.post("/api/tree/seer_alch_011/reflection", json={
        "truth_level": 80,
        "emotional_intensity": 70
    }, headers=headers)
    assert response.status_code == 200
    assert "updated_traits" in response.json()
