# api/tests/test_soulform_api.py
# Eden Protocol – Soulform Transformation API Tests

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


def test_soulform_status_and_eligibility():
    headers = get_auth_header()

    # Status
    status = client.get("/api/soulform/seer_alch_011", headers=headers)
    assert status.status_code == 200
    assert "soulform" in status.json()

    # Eligibility
    eligibility = client.get("/api/soulform/seer_alch_011/eligibility", headers=headers)
    assert eligibility.status_code == 200
    assert "eligible" in eligibility.json()


def test_trigger_transformation():
    headers = get_auth_header()

    result = client.post("/api/soulform/seer_alch_011/transform", headers=headers)
    assert result.status_code == 200
    data = result.json()

    if data.get("soulform"):
        assert data["soulform"]["id"] == "seraph"
        assert data["soulform"]["transformed"] is True
    else:
        assert "reason" in data  # Not eligible
