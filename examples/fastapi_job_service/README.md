# FastAPI Job Service Example

A small backend example focused on behaviour that matters in production services:

- input validation
- idempotent creation
- explicit state transitions
- conflict handling
- API tests

The service is intentionally small so the design choices are easy to inspect.

## Run locally

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app:app --reload
```

Then open `http://127.0.0.1:8000/docs`.

## Run tests

```bash
pytest -q
```

## Design notes

`POST /jobs` accepts an idempotency key so repeated client requests return the existing job instead of creating duplicates.

State transitions are explicit:

```text
queued -> running -> completed
   |         |
   +-------> failed
```

Invalid transitions return HTTP `409 Conflict` rather than silently mutating state.

This example uses in-memory storage to keep the repository compact. A production version would replace that boundary with persistent storage while preserving the same domain rules.
