# 🎓 Notewise – AI-Powered Lecture Notes Generator

**Turn classroom lectures into organized, intelligent and exam-ready study materials.**

Notewise is an AI-powered web application designed to help students transform lengthy classroom lecture recordings into structured and easy-to-understand study resources.

The application uses speech-to-text technology and Large Language Models (LLMs) with prompt engineering to convert lecture recordings into meaningful notes, concise revision sheets, cheatsheets and interactive mindmaps. It also provides a lecture-based AI question-answering feature that allows students to ask questions and receive answers based on the uploaded lecture transcript.

---

## 📌 Problem Statement

Students often struggle to convert lengthy classroom lectures into organized and examination-oriented study materials. Manually listening to recordings, identifying important concepts, preparing notes and creating revision sheets requires considerable time and effort.

Traditional speech-to-text tools can convert audio into text, but they do not necessarily organize the information into meaningful learning resources.

**Notewise aims to bridge this gap** by providing an automated platform that converts classroom lecture recordings into structured academic content using AI and prompt engineering.

The system aims to reduce manual note-making effort, improve accessibility to lecture content and support efficient academic revision.

---

## 🎯 Project Objectives

- Convert classroom lecture recordings into readable text.
- Reduce background noise to improve transcription quality.
- Generate structured and point-to-point lecture notes.
- Extract important concepts, definitions and examples.
- Automatically generate concise revision cheatsheets.
- Create hierarchical mindmaps representing topics and subtopics.
- Provide an AI-powered question-answering interface based on lecture content.
- Allow students to view and export their generated study materials.

---

## ✨ Key Features

| Feature | Description |
|---|---|
| 🎙️ Audio Upload | Upload or record classroom lecture audio. |
| 🔇 Noise Reduction | Reduce unwanted background noise before transcription. |
| 📝 Speech-to-Text | Convert lecture recordings into readable transcripts. |
| 🧠 AI Notes Generation | Generate organized notes with key points, definitions and examples. |
| 📄 Smart Cheatsheet | Create short, exam-oriented revision material. |
| 🌳 Mindmap Generation | Generate hierarchical topic and subtopic mindmaps. |
| 💬 Lecture-Based Q&A | Ask questions and receive answers grounded in the lecture transcript. |
| 📥 PDF Export | Export generated study materials for offline revision. |

---

## ⚙️ How Notewise Works

The application follows an automated audio-to-study-material pipeline.

1. **Audio Upload:** The student uploads or records a classroom lecture.
2. **Audio Processing:** The uploaded recording is processed to reduce background noise.
3. **Speech Recognition:** A pretrained speech-to-text model converts the audio into a transcript.
4. **AI Content Generation:** The transcript is passed to an LLM with task-specific prompts.
5. **Structured Notes:** The system generates key points, definitions, explanations and examples.
6. **Cheatsheet Generation:** Important information is condensed into a quick revision sheet.
7. **Mindmap Generation:** Topics and subtopics are organized into a hierarchical structure.
8. **AI Question Answering:** Students can ask questions about the lecture and receive transcript-grounded answers.
9. **Storage and Export:** Generated content is saved and displayed through the web interface, with PDF export support.

---

## 🏗️ System Architecture

```text
              STUDENT
                 |
                 v
          AUDIO UPLOAD
                 |
                 v
        NODE.JS + EXPRESS
          (Backend Server)
                 |
                 v
        AUDIO PROCESSING
          Python FastAPI
                 |
          Noise Reduction
                 |
                 v
          SPEECH-TO-TEXT
          Whisper / STT
                 |
                 v
          LECTURE TRANSCRIPT
                 |
                 v
        LARGE LANGUAGE MODEL
          (LLM + Prompts)
                 |
       +---------+----------+
       |         |          |
       v         v          v
     NOTES   CHEATSHEET   MINDMAP
       |         |          |
       +---------+----------+
                 |
                 v
          LECTURE-BASED Q&A
                 |
                 v
           POSTGRESQL
                 |
                 v
           REACT FRONTEND
                 |
                 v
          STUDENT DASHBOARD
                 |
                 v
              PDF EXPORT
```

---

## 🛠️ Technology Stack

### Frontend
- React.js
- Tailwind CSS
- JavaScript
- Markmap (mindmap visualization)
- jsPDF (PDF export)

### Backend
- Node.js
- Express.js
- REST APIs

### Database
- PostgreSQL

### AI & Audio Processing
- Python
- FastAPI
- noisereduce (background noise reduction)
- OpenAI Whisper API / local whisper.cpp (speech-to-text)
- OpenAI GPT-4o-mini / Google Gemini Flash (LLM-based content generation)

### Deployment
- Vercel (Frontend)
- Render / Railway (Backend)
- Supabase / Neon (PostgreSQL)

*Note: The final API providers and deployment platforms will be selected during implementation.*

---

## 👥 Team Members & Responsibilities

This project is being developed by a team of four B.Tech students.

| Member | Role | Responsibilities |
|---|---|---|
| **Biprajit** | Frontend & UI Lead | React interface, audio upload screen, processing status, notes display, mindmap visualization, Q&A interface and PDF export. |
| **Sanket** | Audio Processing Lead | Audio cleaning, noise reduction, Python FastAPI microservice, speech-to-text integration and audio testing. |
| **Samir** | Database, Prompt Engineering & QA | PostgreSQL schema, job-status tracking, cheatsheet and mindmap prompts, prompt optimization and end-to-end testing. |
| **Pratik** | Backend & Integration Lead | Node.js, Express APIs, backend architecture, notes-generation integration, service communication and complete pipeline integration. |

---

## 📂 Project Modules

The project is divided into the following major modules:

1. **Frontend Module:** Provides the interface through which students interact with Notewise.
2. **Audio Processing Module:** Handles audio validation, cleaning and preparation.
3. **Transcription Module:** Converts audio recordings into text.
4. **AI Content Generation Module:** Uses LLMs and prompt engineering to generate notes and revision resources.
5. **Database Module:** Stores lecture recordings, transcripts, generated outputs and processing status.
6. **Question Answering Module:** Answers student questions using the corresponding lecture transcript.
7. **Export Module:** Allows students to export their study materials as PDF documents.

---

## 🧠 Role of AI & Prompt Engineering

Prompt engineering is an important part of Notewise.

Instead of training a language model from scratch, the system uses existing pretrained LLMs and carefully designed prompts to generate different types of educational content.

Separate prompts are designed for:

- Structured lecture notes generation.
- Important concepts and definitions extraction.
- Cheatsheet generation.
- Hierarchical mindmap generation.
- Lecture-based question answering.

The generated outputs are intended to follow structured formats so that the frontend can display them consistently.

The project also aims to evaluate and improve prompt quality by testing output accuracy, completeness, relevance and unsupported information.

---

## 🔄 Job Processing Workflow

Each uploaded lecture moves through different processing stages.

| Status | Description |
|---|---|
| `QUEUED` | Audio is uploaded and waiting for processing. |
| `PROCESSING` | Audio cleaning, transcription or AI generation is in progress. |
| `COMPLETED` | Processing and content generation have finished successfully. |
| `FAILED` | Processing encountered an error. |

The application tracks these states so that students can monitor the progress of their recordings.

---

## 🔮 Future Enhancements

Potential future improvements include:

- Support for multiple languages.
- Automatic lecture summarization.
- AI-generated practice questions and quizzes.
- Flashcard generation.
- Speaker identification.
- Real-time lecture transcription.
- Personalized revision recommendations.
- Improved handling of lengthy lecture recordings.

---

## 🎓 Project Information

| Detail | Information |
|---|---|
| Project Name | Notewise |
| Project Type | B.Tech Final Year Project |
| Domain | Artificial Intelligence & Machine Learning |
| Core Technologies | React, Node.js, Python, PostgreSQL, LLMs |
| AI Approach | Pretrained AI Models & Prompt Engineering |
| Team Size | 4 Members |
| Development Duration | Approximately 16 Weeks |

---

## 📌 Project Status

**Development Phase – In Progress**

The project is being developed incrementally, beginning with the audio upload and transcription pipeline, followed by AI-powered content generation, database integration and frontend development.

---

## 📜 License

This project is developed for academic and educational purposes as part of a B.Tech final-year project.

---

**Notewise – Listen Less. Understand More. Revise Smarter.**
