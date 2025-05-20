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
    assert data["token_type"] == "bearer"


def test_login_failure():
    response = client.post("/api/auth/login", json={
        "username": "seer",
        "password": "wrongpass"
    })
    assert response.status_code == 401


def test_token_refresh():
    login = client.post("/api/auth/login", json={
        "username": "seer",
        "password": "eden123"
    })
    assert login.status_code == 200
    refresh_token = login.json()["refresh_token"]

    refresh = client.post("/api/auth/refresh", params={"refresh_token": refresh_token})
    assert refresh.status_code == 200
    assert "access_token" in refresh.json()


def test_protected_me():
    login = client.post("/api/auth/login", json={
        "username": "seer",
        "password": "eden123"
    })
    token = login.json()["access_token"]
    response = client.get("/api/auth/me", headers={"Authorization": f"Bearer {token}"})
    assert response.status_code == 200
    assert response.json()["username"] == "seer"
