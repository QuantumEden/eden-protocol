# api/tests/test_world_tree_api.py
# Eden Protocol – World Tree System Tests

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


def test_worldtree_status():
    headers = get_auth_header()
    response = client.get("/api/worldtree/status", headers=headers)
    assert response.status_code == 200
    data = response.json()
    assert "user_count" in data
    assert "status" in data


def test_worldtree_trait_averages():
    headers = get_auth_header()
    response = client.get("/api/worldtree/traits", headers=headers)
    assert response.status_code == 200
    data = response.json()
    assert "averages" in data
    assert isinstance(data["averages"], dict)


def test_worldtree_activity_log():
    headers = get_auth_header()
    response = client.get("/api/worldtree/activity", headers=headers)
    assert response.status_code == 200
    assert "events" in response.json()
