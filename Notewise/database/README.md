# Database & Prompt Design — Member 4 (Owner)

## 📌 Ownership & Responsibilities
- **Owner:** Member 4 (Database, Prompt Design, and QA Owner)
- **Tech Stack:** PostgreSQL (Supabase / Neon free tier), SQL migrations, Prompt Engineering, JSON Schema validation.
- **Scope:**
  1. Design and maintain the relational database schema (`recordings`, `jobs`, `transcripts`, `outputs`).
  2. Maintain reproducible SQL migrations in `migrations/`.
  3. Author and validate prompt specifications and JSON schemas for:
     - Exam Cheatsheet (`prompts/cheatsheet.prompt.md`)
     - Mindmap Hierarchical Tree (`prompts/mindmap.prompt.md`)
  4. Coordinate with Member 1 to ensure prompt output reliability and retry resilience.

---

## 📂 Folder Structure

```
database/
├── migrations/         # Versioned SQL scripts (001_initial_schema.sql)
├── seeds/              # Mock recordings, transcripts, and JSON outputs for testing
├── prompts/            # Cheatsheet & Mindmap prompt templates & JSON schemas
└── README.md
```

---

## 🛠️ Applying Migrations to Neon / Supabase
Run the migration script using `psql` or the Supabase/Neon SQL editor:
```bash
psql $DATABASE_URL -f migrations/001_initial_schema.sql
```

