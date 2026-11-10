# Notewise — Classroom Lecture-to-Notes AI Platform

> **A student's noisy classroom recording goes in; exam-ready structured notes, a cheatsheet, a mindmap, and a lecture-grounded Q&A tutor come out.**

---

## 👥 Team Roles & Directory Mapping

The project is strictly separated into independent modules so each member can develop and test without blocking others:

| Member | Role | Workspace Directory | Scope |
| :--- | :--- | :--- | :--- |
| **PRATIK** | **Backend + AI Pipeline Lead** | [`backend/`](file:///d:/clg%20files/final%20year%20project/Notewise/backend) | Express REST APIs, job orchestration, audio chunking, Whisper transcription, notes prompt, deployment |
| **BIPRAJIT** | **Frontend Lead** | [`frontend/`](file:///d:/clg%20files/final%20year%20project/Notewise/frontend) | React UI, notes/cheatsheet/mindmap/transcript display, Q&A chat, PDF export |
| **SANKET** | **Audio Processing Owner** | [`audio-service/`](file:///d:/clg%20files/final%20year%20project/Notewise/audio-service) | Python FastAPI noise-reduction microservice (`noisereduce`), audio testing, sample collection |
| **SAMIR** | **Database + Prompts + QA Owner** | [`database/`](file:///d:/clg%20files/final%20year%20project/Notewise/database), [`evaluation/`](file:///d:/clg%20files/final%20year%20project/Notewise/evaluation), [`tests/`](file:///d:/clg%20files/final%20year%20project/Notewise/tests) | Postgres schema & migrations, cheatsheet/mindmap prompts, WER benchmarking, end-to-end testing |

---

## 📁 Repository Structure

```
Notewise/
├── backend/            # Express REST API, Job Orchestrator, Whisper & Gemini Runner (Member 1)
├── frontend/           # React + Tailwind CSS client application (Member 2)
├── audio-service/      # Python FastAPI noise reduction microservice (Member 3)
├── database/           # PostgreSQL migrations, seed data, and prompts (Member 4)
├── evaluation/         # Ground-truth transcripts, WER calculation, human evaluation (Member 4 + 3)
├── tests/              # End-to-end integration test suites (Member 4 + 1)
├── docs/               # System architecture and frozen API contracts
└── README.md           # Project overview and coordination guide
```

---

## 🚀 Quick Start Guide

Detailed setup and development instructions are contained within each component's directory:
- [Backend Setup Guide](file:///d:/clg%20files/final%20year%20project/Notewise/backend/README.md)
- [Frontend Setup Guide](file:///d:/clg%20files/final%20year%20project/Notewise/frontend/README.md)
- [Audio Service Setup Guide](file:///d:/clg%20files/final%20year%20project/Notewise/audio-service/README.md)
- [Database & QA Setup Guide](file:///d:/clg%20files/final%20year%20project/Notewise/database/README.md)

---

## 📑 Service Contracts

Refer to [`docs/api-contracts.md`](file:///d:/clg%20files/final%20year%20project/Notewise/docs/api-contracts.md) for frozen API specifications across Backend, Frontend, Audio Microservice, and LLM schemas.

