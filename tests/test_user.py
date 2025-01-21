import pytest
from fastapi.testclient import TestClient
from main import app


client = TestClient(app)

TEST_USER = {
    "username": "test_user",
    "password": "test_password"
}


def test_init_user():
    """Test del endpoint /init_user con registro exitoso."""

    response = client.post("/init_user", json=TEST_USER)
    
    print("result"*100)
    print(response.json())
    if response.status_code == 400:
        assert response.json()['detail'] == "Username already exist!"
    else:
        assert response.status_code == 200
        assert response.json()["msg"] == "User created successful"


def test_login_success():
    """Test del endpoint /login con credenciales válidas."""

    response = client.post("/login", json=TEST_USER)

    assert response.status_code == 200
    assert "token" in response.json()


def test_login_failure():
    """Test del endpoint /login con credenciales inválidas."""
    TEST_USER['password'] = "111"

    response = client.post("/login", json=TEST_USER)

    assert response.status_code == 400
    assert response.json()['detail'] == "Invalid username or password"
