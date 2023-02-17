"""
Holds all test cases for main file
"""

from fastapi.testclient import TestClient

from .main import app

client = TestClient(app)


def test_health_api():
    """
    Assert health api
    """
    response = client.get("/api/v1/health")
    assert response.status_code == 200
    assert response.json() is True


def test_info_api():
    """
    Assert info api
    """
    response = client.get("/api/v1/info")
    assert response.status_code == 200
    response_json = response.json()
    assert response_json["title"] == "dummy_users"


def test_users_api():
    """
    Assert users api
    """
    response = client.get("/api/v1/users")
    assert response.status_code == 200
    response_json = response.json()
    assert isinstance(response_json, list)


def test_user_api():
    """
    Assert user api
    """
    response = client.get("/api/v1/users/1")
    assert response.status_code == 200
    response_json = response.json()
    assert isinstance(response_json, dict)
