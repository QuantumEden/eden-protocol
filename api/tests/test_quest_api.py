# api/tests/test_quest_api.py
# Eden Protocol – Quest API Tests

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


def test_quest_lifecycle():
    headers = get_auth_header()

    # 1. Generate Quests
    r = client.get("/api/quests/seer_alch_011", headers=headers)
    assert r.status_code == 200
    quests = r.json()
    assert isinstance(quests, list) and len(quests) > 0

    # 2. Accept Quest
    quest_id = quests[0]["id"]
    accept = client.post(f"/api/quests/seer_alch_011/{quest_id}/accept", headers=headers)
    assert accept.status_code == 200
    assert accept.json()["status"] == "accepted"

    # 3. Complete Quest
    complete = client.post(f"/api/quests/seer_alch_011/{quest_id}/complete", json={
        "xp": 150,
        "notes": "Faced fear of failure and persisted"
    }, headers=headers)
    assert complete.status_code == 200
    assert complete.json()["quest"]["status"] == "completed"

    # 4. Reflect
    reflect = client.post(f"/api/quests/seer_alch_011/{quest_id}/reflection", json={
        "insight": "My resistance was rooted in shame.",
        "emotion": "Cathartic relief"
    }, headers=headers)
    assert reflect.status_code == 200
    assert "reflection" in reflect.json()["quest"]
