# api/tests/test_auth_api.py
# Eden Protocol – Auth Endpoint Tests

import pytest
from fastapi.testclient import TestClient
from api.main import app

client = TestClient(app)


def test_login_success():
    response = client.post("/api/auth/login", json={
        "username": "seer",
        "password": "eden123"
    })
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data
    assert "refresh_token" in data
    assert data.get("token_type") == "bearer"


def test_login_failure():
    response = client.post("/api/auth/login", json={
        "username": "seer",
        "password": "wrongpass"
    })
    assert response.status_code == 401
    assert "detail" in response.json()


def test_token_refresh():
    login = client.post("/api/auth/login", json={
        "username": "seer",
        "password": "eden123"
    })
    assert login.status_code == 200
    tokens = login.json()
    refresh_token = tokens["refresh_token"]

    refresh = client.post("/api/auth/refresh", params={"refresh_token": refresh_token})
    assert refresh.status_code == 200
    refreshed = refresh.json()
    assert "access_token" in refreshed
    assert refreshed.get("token_type") == "bearer"


def test_protected_me():
    login = client.post("/api/auth/login", json={
        "username": "seer",
        "password": "eden123"
    })
    assert login.status_code == 200
    token = login.json()["access_token"]
    
    response = client.get("/api/auth/me", headers={"Authorization": f"Bearer {token}"})
    assert response.status_code == 200
    profile = response.json()
    assert profile.get("username") == "seer"
    assert "soulform" in profile or "traits" in profile
