# Database Seeds — Notewise Test & Demo Data

Maintained by **Samir** (Database + Prompts + QA Owner).

## 📂 Overview

This directory provides reproducible seed fixtures for local development, test automation, and frontend stubbing:

- `001_mock_data.sql`: PostgreSQL seed script inserting three realistic lecture scenarios with UUID primary keys and JSONB output payloads.
- `seed_data.json`: Direct JSON format matching the frontend API contracts for mocking without active PostgreSQL connection.

---

## 🧪 Scenarios Included

| Scenario | Lecture Domain | Status | Completed Artifacts | Testing Purpose |
| :--- | :--- | :--- | :--- | :--- |
| **Lecture 1** | OS Virtual Memory & Paging | `done` | `notes`, `cheatsheet`, `mindmap`, `qa` | Happy path display, PDF export, Q&A testing |
| **Lecture 2** | DBMS Normalization & BCNF | `partial` | `notes`, `cheatsheet` (mindmap failed) | Partial success handling & `/retry` endpoint |
| **Lecture 3** | ML Gradient Descent | `queued` | None | Polling hook (`queued` $\to$ `processing`) |

---

## 🛠️ Usage

### To Seed Local PostgreSQL / Neon / Supabase:
```bash
psql $DATABASE_URL -f migrations/001_initial_schema.sql
psql $DATABASE_URL -f migrations/002_add_triggers_and_views.sql
psql $DATABASE_URL -f seeds/001_mock_data.sql
```

### To Verify in Python:
```bash
python database/verify_database.py
```
