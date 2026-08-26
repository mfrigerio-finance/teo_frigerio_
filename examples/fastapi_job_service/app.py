from enum import StrEnum
from uuid import UUID, uuid4

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field

app = FastAPI(title="Job Service", version="1.0.0")


class JobState(StrEnum):
    queued = "queued"
    running = "running"
    completed = "completed"
    failed = "failed"


class JobCreate(BaseModel):
    idempotency_key: str = Field(min_length=8, max_length=128)
    payload: dict[str, object]


class Job(BaseModel):
    id: UUID
    idempotency_key: str
    state: JobState
    payload: dict[str, object]


_jobs: dict[UUID, Job] = {}
_by_key: dict[str, UUID] = {}


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/jobs", response_model=Job, status_code=status.HTTP_201_CREATED)
def create_job(command: JobCreate) -> Job:
    existing_id = _by_key.get(command.idempotency_key)
    if existing_id is not None:
        return _jobs[existing_id]

    job = Job(
        id=uuid4(),
        idempotency_key=command.idempotency_key,
        state=JobState.queued,
        payload=command.payload,
    )
    _jobs[job.id] = job
    _by_key[job.idempotency_key] = job.id
    return job


@app.get("/jobs/{job_id}", response_model=Job)
def get_job(job_id: UUID) -> Job:
    job = _jobs.get(job_id)
    if job is None:
        raise HTTPException(status_code=404, detail="job not found")
    return job


class StateChange(BaseModel):
    state: JobState


_ALLOWED_TRANSITIONS: dict[JobState, set[JobState]] = {
    JobState.queued: {JobState.running, JobState.failed},
    JobState.running: {JobState.completed, JobState.failed},
    JobState.completed: set(),
    JobState.failed: set(),
}


@app.post("/jobs/{job_id}/state", response_model=Job)
def change_state(job_id: UUID, change: StateChange) -> Job:
    job = _jobs.get(job_id)
    if job is None:
        raise HTTPException(status_code=404, detail="job not found")

    if change.state not in _ALLOWED_TRANSITIONS[job.state]:
        raise HTTPException(
            status_code=409,
            detail=f"invalid transition: {job.state} -> {change.state}",
        )

    updated = job.model_copy(update={"state": change.state})
    _jobs[job_id] = updated
    return updated
