# Frozen Service Contracts & Interfaces

These contracts are frozen early in the build (Phase 0) to guarantee all 4 team members can develop and mock dependencies in parallel without blocking each other.

---

## 1. Backend ↔ Python Noise-Reduction Service

- **Microservice Base URL:** `http://localhost:8000` (or `AUDIO_SERVICE_URL`)
- **Health Check:**
  - `GET /health`
  - Response (`200 OK`): `{"status": "ok"}`
- **Noise Reduction:**
  - `POST /clean`
  - **Request Type:** `multipart/form-data`
  - **Body Field:** `file` (Binary audio file, preferred: 16kHz WAV mono; max 100MB).
  - **Backend Pre-condition:** Node.js backend converts non-WAV inputs to 16kHz mono WAV using `ffmpeg` before forwarding.
  - **Success Response:**
    - HTTP Status: `200 OK`
    - Header: `Content-Type: audio/wav`
    - Body: **Raw binary WAV audio stream** (No base64 wrapper, no remote URL).
  - **Error Response:**
    - HTTP Status: `400 Bad Request` / `422 Unprocessable Entity` / `500 Internal Server Error`
    - Body: `{"error": "string", "detail": "string"}`

---

## 2. Frontend ↔ Backend REST API

- **Backend Base URL:** `http://localhost:5000` (or `VITE_API_URL`)
- **Browser Session Header / Query:** `x-session-id: <uuid>`

### 2.1 Upload Audio & Create Job
- `POST /api/recordings/upload`
- **Request:** `multipart/form-data` with `file` (WAV, MP3, M4A) and header `x-session-id`.
- **Response (`201 Created`):**
  ```json
  {
    "recording_id": "uuid",
    "job_id": "uuid",
    "status": "queued",
    "filename": "lecture_week1.m4a"
  }
  ```

### 2.2 Poll Job Status
- `GET /api/jobs/:job_id`
- **Response (`200 OK`):**
  ```json
  {
    "id": "uuid",
    "recording_id": "uuid",
    "status": "queued | processing | done | partial | failed",
    "error_message": null,
    "completed_artifacts": ["notes", "cheatsheet"],
    "created_at": "ISO-8601",
    "updated_at": "ISO-8601"
  }
  ```

### 2.3 Fetch Transcript
- `GET /api/jobs/:job_id/transcript`
- **Response (`200 OK`):**
  ```json
  {
    "id": "uuid",
    "full_text": "Welcome to class today we discuss...",
    "segments": [
      { "start": 0.0, "end": 4.5, "text": "Welcome to class today." },
      { "start": 4.6, "end": 10.2, "text": "We will discuss operating systems." }
    ],
    "word_count": 1250
  }
  ```

### 2.4 Fetch Generated Artifacts
- `GET /api/jobs/:job_id/outputs/:type` (`type` $\in$ `notes`, `cheatsheet`, `mindmap`)
- **Response (`200 OK`):**
  ```json
  {
    "type": "notes",
    "content": { ... }
  }
  ```

### 2.5 Grounded Q&A Chat
- `POST /api/jobs/:job_id/qa`
- **Request Body:**
  ```json
  {
    "question": "What is the difference between paging and segmentation?"
  }
  ```
- **Response (`200 OK`):**
  ```json
  {
    "question": "What is the difference between paging and segmentation?",
    "answer": "According to the lecture, paging divides memory into fixed-size frames while segmentation divides memory into variable-sized logical segments.",
    "grounded": true
  }
  ```
- **Refusal Response (If not covered):**
  ```json
  {
    "question": "Who won the 2024 World Cup?",
    "answer": "This topic was not covered in the lecture.",
    "grounded": false
  }
  ```

### 2.6 Retry Failed Outputs
- `POST /api/jobs/:job_id/retry`
- Only re-runs missing or failed artifacts without re-executing audio cleaning or transcription.

---

## 3. LLM JSON Schemas

### 3.1 Notes Schema
```json
{
  "key_points": ["string"],
  "definitions": [
    {
      "term": "string",
      "definition": "string"
    }
  ],
  "examples": ["string"],
  "quick_revision_sheet": ["string"]
}
```

### 3.2 Cheatsheet Schema
```json
{
  "sections": [
    {
      "heading": "string",
      "bullets": ["string"]
    }
  ]
}
```

### 3.3 Mindmap Schema
```json
{
  "title": "string",
  "children": [
    {
      "title": "string",
      "children": []
    }
  ]
}
```

