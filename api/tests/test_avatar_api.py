# api/tests/test_avatar_api.py
# Eden Protocol – Avatar API Tests

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


def test_get_avatar():
    headers = get_auth_header()
    response = client.get("/api/avatar/seer_alch_011", headers=headers)
    assert response.status_code == 200
    data = response.json()
    assert data.get("user_id") == "seer_alch_011"
    assert "sacred_path" in data
    assert isinstance(data["sacred_path"], str)


def test_update_avatar():
    headers = get_auth_header()
    response = client.put("/api/avatar/seer_alch_011", json={
        "name": "Voice of the Abyss",
        "archetype": "Oracle"
    }, headers=headers)
    assert response.status_code == 200
    updated = response.json()
    assert updated.get("name") == "Voice of the Abyss"
    assert updated.get("archetype") == "Oracle"


def test_change_sacred_path():
    headers = get_auth_header()
    response = client.post("/api/avatar/seer_alch_011/path", json={
        "path": "Voidborne"
    }, headers=headers)
    assert response.status_code == 200
    path_change = response.json()
    assert path_change.get("sacred_path") == "Voidborne"
