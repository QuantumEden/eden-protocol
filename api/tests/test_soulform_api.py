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
    assert login.status_code == 200
    token = login.json()["access_token"]
    return {"Authorization": f"Bearer {token}"}


def test_soulform_status_and_eligibility():
    headers = get_auth_header()

    # Status
    status = client.get("/api/soulform/seer_alch_011", headers=headers)
    assert status.status_code == 200
    soulform_data = status.json()
    assert "soulform" in soulform_data

    # Eligibility
    eligibility = client.get("/api/soulform/seer_alch_011/eligibility", headers=headers)
    assert eligibility.status_code == 200
    eligibility_data = eligibility.json()
    assert "eligible" in eligibility_data
    assert isinstance(eligibility_data["eligible"], bool)


def test_trigger_transformation():
    headers = get_auth_header()

    result = client.post("/api/soulform/seer_alch_011/transform", headers=headers)
    assert result.status_code == 200
    data = result.json()

    if "soulform" in data:
        soulform = data["soulform"]
        assert soulform["id"] == "seraph"
        assert soulform["transformed"] is True
    else:
        assert "reason" in data
