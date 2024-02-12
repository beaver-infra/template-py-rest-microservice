"""
This module contains test cases for the main file APIs.
"""

from fastapi.testclient import TestClient

from .main import app

# Create a TestClient instance for interacting with FastAPI app
client = TestClient(app)


def test_health_api():
    """
    Test the health API endpoint.

    Asserts that the health endpoint returns a status code of 200 and the response is True.
    """
    response = client.get("/api/v1/health")
    assert response.status_code == 200
    assert response.json() is True


def test_info_api():
    """
    Test the info API endpoint.

    Asserts that the info endpoint returns a status code of 200 and
    the response title is "dummy_users".
    """
    response = client.get("/api/v1/info")
    assert response.status_code == 200
    response_json = response.json()
    assert response_json["title"] == "dummy_users"


def test_users_api():
    """
    Test the users API endpoint.

    Asserts that the users endpoint returns a status code of 200 and the response is a list.
    """
    response = client.get("/api/v1/users")
    assert response.status_code == 200
    response_json = response.json()
    assert isinstance(response_json, list)


def test_user_api():
    """
    Test the user API endpoint.

    Asserts that the user endpoint returns a status code of 200 and the response is a dictionary.
    """
    response = client.get("/api/v1/users/1")
    assert response.status_code == 200
    response_json = response.json()
    assert isinstance(response_json, dict)
