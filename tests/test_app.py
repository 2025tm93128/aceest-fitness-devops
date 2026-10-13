import pytest

from app import app, clients


@pytest.fixture
def client():
    app.config["TESTING"] = True
    clients.clear()

    with app.test_client() as test_client:
        yield test_client


def test_home_endpoint(client):
    response = client.get("/")

    assert response.status_code == 200
    assert response.get_json()["application"] == "ACEest Fitness & Gym"
    assert response.get_json()["status"] == "running"


def test_health_endpoint(client):
    response = client.get("/health")

    assert response.status_code == 200
    assert response.get_json() == {"status": "healthy"}


def test_get_programs(client):
    response = client.get("/programs")
    programs = response.get_json()

    assert response.status_code == 200
    assert len(programs) == 3
    assert programs[0]["name"] == "Weight Loss"


def test_add_client_successfully(client):
    response = client.post(
        "/clients",
        json={
            "name": "Test Client",
            "email": "test@example.com",
            "program_id": 1
        }
    )
    created_client = response.get_json()

    assert response.status_code == 201
    assert created_client["name"] == "Test Client"
    assert created_client["program"] == "Weight Loss"


def test_add_client_with_missing_fields(client):
    response = client.post(
        "/clients",
        json={"name": "Incomplete Client"}
    )

    assert response.status_code == 400
    assert response.get_json()["error"] == (
        "name, email and program_id are required"
    )


def test_add_client_with_invalid_program(client):
    response = client.post(
        "/clients",
        json={
            "name": "Test Client",
            "email": "test@example.com",
            "program_id": 99
        }
    )

    assert response.status_code == 400
    assert response.get_json()["error"] == "Invalid program_id"


def test_calculate_calories(client):
    response = client.post(
        "/calories",
        json={
            "weight_kg": 70,
            "duration_minutes": 30,
            "intensity": "moderate"
        }
    )
    result = response.get_json()

    assert response.status_code == 200
    assert result["estimated_calories"] == 168.0


def test_calculate_calories_with_invalid_intensity(client):
    response = client.post(
        "/calories",
        json={
            "weight_kg": 70,
            "duration_minutes": 30,
            "intensity": "extreme"
        }
    )

    assert response.status_code == 400
    assert response.get_json()["error"] == (
        "intensity must be low, moderate or high"
    )
