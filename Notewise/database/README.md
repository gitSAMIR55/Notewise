# Database & Prompt Design — Member 4 (Samir)

## 📌 Ownership & Responsibilities
- **Owner:** Samir (Member 4 — Database, Prompt Design, and QA Owner)
- **Tech Stack:** PostgreSQL (Supabase / Neon free tier), SQL migrations, Prompt Engineering, JSON Schema validation.
- **Scope:**
  1. Design and maintain the relational database schema (`recordings`, `jobs`, `transcripts`, `outputs`).
  2. Maintain reproducible SQL migrations in `migrations/`.
  3. Author and validate prompt specifications and JSON schemas for:
     - Exam Cheatsheet (`prompts/cheatsheet.prompt.md` & `prompts/cheatsheet.schema.json`)
     - Mindmap Hierarchical Tree (`prompts/mindmap.prompt.md` & `prompts/mindmap.schema.json`)
  4. Coordinate with Member 1 to ensure prompt output reliability and retry resilience.

---

## 📂 Folder Structure

```
database/
├── migrations/
│   ├── 001_initial_schema.sql           # Base tables: recordings, jobs, transcripts, outputs
│   └── 002_add_triggers_and_views.sql   # Updated_at trigger & pipeline monitoring view
├── seeds/
│   ├── 001_mock_data.sql               # PostgreSQL seed data (3 lecture scenarios)
│   ├── seed_data.json                  # JSON fixtures for frontend/backend offline mocking
│   └── README.md                       # Seeding documentation
├── prompts/
│   ├── cheatsheet.prompt.md            # Exam cheatsheet prompt engineering specification
│   ├── cheatsheet.schema.json          # JSON schema for cheatsheet
│   ├── mindmap.prompt.md               # Hierarchical taxonomy mindmap specification
│   ├── mindmap.schema.json             # JSON schema for mindmap
│   ├── notes.schema.json               # JSON schema for notes
│   ├── qa.schema.json                  # JSON schema for grounded Q&A
│   └── prompt_validator.py             # Schema validator & markdown fence stripping engine
├── verify_database.py                  # Database and fixtures syntax/schema checker
└── README.md
```

---

## 🛠️ Applying Migrations to Neon / Supabase

Run the migration scripts using `psql` or the Supabase/Neon SQL editor:
```bash
# 1. Apply core schema
psql $DATABASE_URL -f migrations/001_initial_schema.sql

# 2. Apply triggers and monitoring views
psql $DATABASE_URL -f migrations/002_add_triggers_and_views.sql

# 3. Seed mock data for development
psql $DATABASE_URL -f seeds/001_mock_data.sql
```

---

## 🧪 Verification & Self-Test

Validate SQL syntax, JSON schema constraints, and mock data consistency:
```bash
# Verify database schema & seeds
python database/verify_database.py

# Verify prompt schemas & output validator
python database/prompts/prompt_validator.py
```
