# api/tests/test_world_tree_api.py
# Eden Protocol – World Tree System Tests (Updated)

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


def test_worldtree_status():
    headers = get_auth_header()
    r = client.get("/api/worldtree/status", headers=headers)
    assert r.status_code == 200
    data = r.json()
    assert "user_count" in data
    assert "status" in data
    assert isinstance(data["status"], str)


def test_worldtree_trait_averages():
    headers = get_auth_header()
    r = client.get("/api/worldtree/traits", headers=headers)
    assert r.status_code == 200
    data = r.json()
    assert "averages" in data
    assert isinstance(data["averages"], dict)
    for trait, score in data["averages"].items():
        assert isinstance(trait, str)
        assert isinstance(score, (int, float))


def test_worldtree_activity_log():
    headers = get_auth_header()
    r = client.get("/api/worldtree/activity", headers=headers)
    assert r.status_code == 200
    data = r.json()
    assert "events" in data
    assert isinstance(data["events"], list)
