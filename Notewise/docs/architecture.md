# Notewise System Architecture & Technical Specifications

## 1. High-Level Pipeline Flow

```
[Student Classroom Audio (Phone WAV/MP3/M4A)]
                   │
                   ▼
       [1. Upload & Job Created]
                   │
                   ▼
     [2. Conversion to WAV (FFmpeg)]
                   │
                   ▼
  [3. Noise Reduction (Python Microservice)]
                   │
                   ▼
     [4. Chunking & Whisper Transcription]
                   │
                   ▼
       [5. Independent LLM Prompts]
          ├──> Notes Generation
          ├──> Cheatsheet Generation
          └──> Mindmap Generation
                   │
                   ▼
   [6. PostgreSQL (outputs table with JSONB)]
                   │
                   ▼
  [7. React Display, PDF Export & Grounded Q&A]
```

## 2. Key Architecture Principles

1. **Decoupled Python Audio Microservice:**
   - Isolated environment running Python `noisereduce` (spectral gating) and FastAPI.
   - Communicates with Express via a frozen binary WAV contract over HTTP.
2. **Audio Chunking Strategy:**
   - Lectures (60–90 minutes) are segmented into ~5-minute chunks split on silence using FFmpeg.
   - Chunks are transcribed using `whisper.cpp` (or OpenAI Whisper fallback) and concatenated with correct timestamp offsets.
3. **Context-Stuffed Grounded Q&A (No RAG):**
   - Transcripts of 60–90 min lectures fit comfortably within Gemini Flash's 1M token context window.
   - Avoids vector database and embedding complexity while ensuring zero hallucination outside lecture scope.
4. **Idempotency & Partial Success:**
   - State machine handles `queued -> processing -> done | partial | failed`.
   - Each generation artifact has an independent lifecycle. If one fails, the job is marked `partial`, and the `/retry` endpoint only fills the missing gaps.

