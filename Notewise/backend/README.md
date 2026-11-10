# Backend Service — Member 1 (Lead)

## 📌 Ownership & Responsibilities
- **Owner:** Member 1 (Backend and AI Pipeline Lead)
- **Tech Stack:** Node.js, Express.js, FFmpeg, PostgreSQL (`pg`), Whisper (`whisper.cpp` / API), Gemini API.
- **Scope:**
  1. Express REST APIs (upload, jobs, transcripts, outputs, Q&A, retry).
  2. Job queue & state machine orchestration (`queued` $\to$ `processing` $\to$ `done` / `partial` / `failed`).
  3. Pre-processing audio with FFmpeg (conversion to WAV & silence chunking ~5 mins).
  4. Integration with Member 3's Python audio service (`POST /clean`).
  5. Local Whisper transcription with timestamp offsets.
  6. LLM generation execution (Gemini Flash) using prompt templates.
  7. Notes prompt engineering and structured JSON output validation.
  8. Deployment on Render / Railway.

---

## 📂 Folder Structure

```
backend/
├── src/
│   ├── config/         # Database and environment configurations
│   ├── controllers/    # Request & response handlers (recordings, jobs, outputs, qa)
│   ├── routes/         # Express endpoint definitions
│   ├── services/       # Core business logic:
│   │   ├── jobQueue.js       # Asynchronous job state manager
│   │   ├── audioClient.js    # Communicates with Python Audio Microservice
│   │   ├── chunker.js        # Silence-based 5-minute audio splitting (FFmpeg)
│   │   ├── whisperService.js # Whisper.cpp & fallback API runner
│   │   └── llmService.js     # Gemini Flash integration with retry
│   ├── prompts/        # Member 1's notes prompt & schema definition
│   ├── utils/          # Shared helpers (logger, response formatters)
│   └── server.js       # App entry point
├── .env.example
├── package.json
└── README.md
```

---

## 🛠️ Setup Instructions
1. Install dependencies:
   ```bash
   npm install
   ```
2. Copy `.env.example` to `.env` and fill in credentials:
   ```bash
   cp .env.example .env
   ```
3. Start the development server:
   ```bash
   npm run dev
   ```

