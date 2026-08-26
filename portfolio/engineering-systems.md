# Software & Systems Engineering

## Engineering Profile

Hands-on software and systems work across backend engineering, data architecture, security controls, automation and deterministic financial logic.

The engineering approach starts from domain invariants and ownership, then carries them through APIs, persistence, authorization, failure handling and automated verification.

## Core Technologies

### Languages
- Python
- SQL
- TypeScript
- JavaScript

### Backend
- FastAPI
- REST APIs
- Pydantic
- WebSockets
- Domain services
- Repository pattern

### Data
- PostgreSQL
- SQLite
- SQLAlchemy
- Alembic
- Data modelling
- Versioned migrations
- Validation

### Security
- WebAuthn / FIDO2
- Hashed sessions
- Authorization
- Company / entity isolation
- Audit evidence
- Least-privilege and RBAC concepts

### Delivery & Verification
- Git
- Docker
- pytest
- Vitest
- Ruff
- React
- Vite
- Next.js
- Environment-based configuration
- Technical documentation

## Engineering Method

1. **Domain analysis** — actors, vocabulary, invariants, lifecycle states, ownership and decision rights.
2. **System boundaries** — separate interface, application, domain, integration and persistence responsibilities.
3. **Data architecture** — define keys, scope, constraints, provenance, migrations and system-of-record ownership.
4. **Security controls** — enforce authentication, authorization, isolation and audit at server/database boundaries.
5. **Failure semantics** — model stale, invalid, conflicting and unauthorized states explicitly.
6. **Verification** — test calculations, APIs, repositories, migrations, authorization invariants and provider contracts.

## Public Engineering Examples

### FastAPI Job Service
A compact public example demonstrating typed request validation, idempotent creation, explicit state transitions and API tests.

→ [`../examples/fastapi_job_service`](../examples/fastapi_job_service)

### Workflow Control Plane
A modular workflow-orchestration architecture focused on explicit service boundaries, execution semantics, auditing and replaceability.

→ [`LEONIDA22/workflow-engine`](https://github.com/LEONIDA22/workflow-engine)

### Shared Contracts
Versioned TypeScript contracts, schemas and events supporting the workflow-control-plane design.

→ [`LEONIDA22/workflow-shared-contracts`](https://github.com/LEONIDA22/workflow-shared-contracts)

## Selected Private / Sanitised Engineering Work

Professional materials also document selected implementation work across:

- Modular finance and tax backends
- Secure multi-entity administration
- WebAuthn/FIDO2 authentication and session security
- Append-only PostgreSQL audit controls
- Event-driven market-data systems
- Sequence-gap and freshness validation
- Depth-based VWAP and Decimal financial arithmetic
- Local-first job/document monitoring
- Structured tax-jurisdiction knowledge models

Client identities, private endpoints, credentials, production data and proprietary source code are excluded from public repositories.
