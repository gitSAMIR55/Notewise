# End-to-End Testing Suite — QA Lead: Samir (Member 4)

## 📌 Scope & Ownership
- **Lead Owner:** Samir (Member 4 — Database, Prompt Engineering & QA Owner)
- **Co-Owner:** Member 1 (Backend & Integration Lead)
- **Purpose:** Validate complete pipeline execution across service boundaries (Audio upload $\to$ Noise reduction $\to$ Whisper chunking $\to$ Generation $\to$ Database persistence $\to$ Grounded Q&A).

---

## 📂 Folder Structure

```
tests/
├── e2e/
│   ├── test_pipeline_happy_path.js     # Jest/Supertest suite: Complete upload -> done pipeline
│   ├── test_partial_success_retry.js    # Jest/Supertest suite: Partial artifact failure & /retry
│   ├── test_grounded_qa_refusal.js     # Jest/Supertest suite: Grounded Q&A and strict refusal
│   └── run_tests.py                    # Standalone executable integration runner (20 assertions)
└── README.md
```

---

## 🧪 Test Suites Description

### 1. Happy Path Pipeline (`test_pipeline_happy_path.js`)
- `POST /api/recordings/upload` with audio buffer $\to$ verifies `201 Created` with `queued` status.
- `GET /api/jobs/:job_id` polling $\to$ verifies transition to `status: 'done'`.
- `GET /api/jobs/:job_id/transcript` $\to$ verifies timestamped segments and word count.
- `GET /api/jobs/:job_id/outputs/:type` $\to$ verifies structured schemas for `notes`, `cheatsheet`, and `mindmap`.

### 2. Partial Success & Retry Resilience (`test_partial_success_retry.js`)
- Verifies job state with `status: 'partial'` where one artifact failed (e.g. mindmap timeout).
- Confirms existing artifacts are accessible while missing artifact returns 404.
- `POST /api/jobs/:job_id/retry` $\to$ verifies that **ONLY** the missing artifact is regenerated without re-running audio cleaning or transcription.
- Confirms final transition to `done`.

### 3. Grounded Q&A & Anti-Hallucination Refusals (`test_grounded_qa_refusal.js`)
- Validates `POST /api/jobs/:job_id/qa`.
- In-scope queries return `grounded: true` with factual answers grounded in the lecture transcript.
- Out-of-scope queries return `grounded: false` and the exact frozen contract refusal:
  `"This topic was not covered in the lecture."`
- Validates 400 Bad Request error handling for empty questions.

---

## 🚀 Running the Tests

### Option A: Using the Standalone Python Runner (No external dependencies)
```bash
python tests/e2e/run_tests.py
```

### Option B: Using Jest & Supertest (Against running backend)
```bash
cd backend
npm test -- ../tests/e2e/test_pipeline_happy_path.js
npm test -- ../tests/e2e/test_partial_success_retry.js
npm test -- ../tests/e2e/test_grounded_qa_refusal.js
```
