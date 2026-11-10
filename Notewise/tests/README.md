# End-to-End Testing Suite

## 📌 Scope & Ownership
- **Lead Owners:** Member 4 (QA) & Member 1 (Backend)
- **Purpose:** Validate complete pipeline execution across service boundaries (Audio upload $\to$ Noise reduction $\to$ Whisper chunking $\to$ Generation $\to$ Database persistence).

---

## 📂 Folder Structure

```
tests/
├── e2e/                # Integration test scripts (Jest / Supertest / Python requests)
│   ├── test_pipeline_happy_path.js
│   ├── test_partial_success_retry.js
│   └── test_grounded_qa_refusal.js
└── README.md
```

