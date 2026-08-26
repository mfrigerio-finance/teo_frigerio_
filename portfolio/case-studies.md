# Sanitised Case Studies

These case studies are intentionally written without client names, private infrastructure, credentials, proprietary code or confidential operating data.

## 1. Finance & Reporting Automation

### Problem
Recurring reporting required substantial manual preparation across spreadsheets, source data and management outputs.

### Approach
- Structured reporting logic around explicit inputs, transformations and outputs
- Used Excel, Power Query and VBA to reduce repetitive handling
- Preserved reconciliation and exception visibility
- Kept management outputs connected to source data and financial meaning

### Result
A documented engagement reported a **40% reduction in manual reporting time**.

### Capabilities demonstrated
FP&A · management reporting · automation · reconciliation · process improvement · Excel · Power Query · VBA

---

## 2. Finance & ERP Transformation

### Problem
Finance requirements, operational processes, data structures and system behaviour needed to remain aligned through transformation.

### Approach
- Mapped as-is processes, pain points and ownership
- Translated finance requirements into target processes and acceptance criteria
- Connected accounting logic, master data, integrations and reporting needs
- Supported UAT, defect analysis, reconciliation and control validation
- Documented decisions and operating procedures for adoption

### Capabilities demonstrated
Finance transformation · SAP/ERP environments · requirements · process design · integration · UAT · controls · data · adoption

---

## 3. Modular Finance & Tax Platform

### Problem
A local-first platform needed to combine finance, entity, accounting, compliance and market workspaces without collapsing domain boundaries.

### Approach
- Separated typed APIs, domain services and persistence
- Used Python, FastAPI, PostgreSQL and repository abstractions
- Implemented monetary logic with Decimal arithmetic
- Made cost-basis selection explicit
- Rejected overselling and inconsistent allocation states rather than silently defaulting
- Built rerunnable migrations and automated API/repository/calculation tests

### Capabilities demonstrated
Python · FastAPI · PostgreSQL · domain architecture · deterministic financial logic · migrations · testing

---

## 4. Multi-Entity Security & Audit

### Problem
A private administration system required strict company-by-company isolation and durable audit evidence.

### Approach
- Implemented WebAuthn/FIDO2 authentication contracts
- Stored bearer sessions as hashes with expiry and revocation
- Compared authenticated company scope with requested route scope server-side
- Propagated company keys through persistence layers
- Used PostgreSQL triggers to reject update/delete operations on append-only audit events

### Capabilities demonstrated
WebAuthn/FIDO2 · authorization · scoped persistence · PostgreSQL · auditability · security-by-design

---

## 5. Event-Driven Market Data

### Problem
A market scanner needed to distinguish executable conditions from theoretical top-of-book spreads.

### Approach
- Used REST discovery and WebSocket L2 feeds
- Applied snapshot/delta logic and sequence-gap invalidation
- Enforced freshness checks and reconnect/backoff behaviour
- Calculated depth-based BUY/SELL VWAP with Decimal arithmetic
- Included fees, balances and safety buffers before publishing candidates
- Explicitly excluded order placement and withdrawal functionality

### Capabilities demonstrated
Python · WebSockets · realtime state · market data · Decimal arithmetic · failure semantics · quantitative systems

---

## 6. Local-First Monitoring & Document Automation

### Problem
A monitoring workspace needed to structure local documents and public-source data while respecting access boundaries.

### Approach
- Built local PDF, DOCX and TXT extraction workflows
- Used public RSS/Atom, JSON/ATS and HTML adapters
- Added scheduled scanning with exponential backoff
- Kept authentication/CAPTCHA bypass outside the design boundary

### Capabilities demonstrated
React · TypeScript · FastAPI · SQLite · automation · public-source integration · responsible operational boundaries

---

## Working Style Across Case Studies

The recurring pattern is:

**Frame → Analyse → Design → Deliver → Improve**

Financial and technical claims are kept separate from assumptions. Controls are placed at the layer that can enforce them. Unknown or stale states are made visible instead of silently accepted.
