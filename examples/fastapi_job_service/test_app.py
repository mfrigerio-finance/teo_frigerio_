from fastapi.testclient import TestClient

from app import _by_key, _jobs, app

client = TestClient(app)


def setup_function() -> None:
    _jobs.clear()
    _by_key.clear()


def test_health() -> None:
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_idempotent_job_creation() -> None:
    body = {"idempotency_key": "request-123", "payload": {"task": "demo"}}

    first = client.post("/jobs", json=body)
    second = client.post("/jobs", json=body)

    assert first.status_code == 201
    assert second.status_code == 201
    assert first.json()["id"] == second.json()["id"]


def test_valid_state_transition() -> None:
    created = client.post(
        "/jobs",
        json={"idempotency_key": "request-456", "payload": {}},
    ).json()

    response = client.post(
        f"/jobs/{created['id']}/state",
        json={"state": "running"},
    )

    assert response.status_code == 200
    assert response.json()["state"] == "running"


def test_invalid_state_transition_returns_conflict() -> None:
    created = client.post(
        "/jobs",
        json={"idempotency_key": "request-789", "payload": {}},
    ).json()

    response = client.post(
        f"/jobs/{created['id']}/state",
        json={"state": "completed"},
    )

    assert response.status_code == 409
