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
- Reduce the time and effort required for manual note preparation.

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

Notewise follows a modular architecture consisting of a React frontend, Node.js backend, Python-based audio processing service and PostgreSQL database.

```text
                 STUDENT
                    |
                    v
              REACT FRONTEND
                    |
                    v
             NODE.JS + EXPRESS
               BACKEND API
                    |
             AUDIO UPLOAD
                    |
                    v
             PYTHON FASTAPI
              AUDIO SERVICE
                    |
              NOISE REDUCTION
                    |
                    v
              SPEECH-TO-TEXT
               WHISPER / STT
                    |
                    v
             LECTURE TRANSCRIPT
                    |
                    v
            LARGE LANGUAGE MODEL
              (LLM + PROMPTS)
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
                (RAG-BASED)
                    |
                    v
               POSTGRESQL
                    |
                    v
              STUDENT DASHBOARD
                    |
                    v
                 PDF EXPORT
```

*Note: The final architecture and service communication flow may be refined during implementation.*

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

### AI Techniques

- Prompt Engineering
- Large Language Models (LLMs)
- Speech Recognition
- Retrieval-Augmented Generation (RAG)
- Structured Output Generation

### Deployment

- Vercel (Frontend)
- Render / Railway (Backend)
- Supabase / Neon (PostgreSQL)

*Note: The final AI API providers, deployment platforms and supporting libraries will be selected during implementation.*

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

## 🔍 AI Architecture & Retrieval-Augmented Generation (RAG)

Notewise uses pretrained AI models for speech recognition and educational content generation.

The AI pipeline consists of the following stages:

### 1. Speech Recognition

A pretrained speech-to-text model such as Whisper converts classroom lecture recordings into textual transcripts.

### 2. LLM-Based Content Generation

The generated transcript is passed to a Large Language Model (LLM) using task-specific prompts to produce:

- Structured lecture notes.
- Important concepts and definitions.
- Revision cheatsheets.
- Hierarchical mindmaps.

### 3. Lecture-Based Question Answering

The system aims to use Retrieval-Augmented Generation (RAG) to retrieve relevant sections from the uploaded lecture transcript before generating answers.

The proposed RAG workflow includes:

1. Dividing the lecture transcript into smaller text chunks.
2. Generating vector embeddings for the text chunks.
3. Storing the embeddings in a searchable vector database or supported vector storage system.
4. Retrieving relevant transcript sections according to the student's question.
5. Providing the retrieved context to the LLM.
6. Generating an answer based on the retrieved lecture information.

This approach aims to keep answers relevant to the uploaded lecture and reduce unsupported AI-generated information.

*Note: RAG is a planned implementation approach and will be finalized during development.*

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

## 🔐 Security & Data Management

Notewise aims to maintain the security and integrity of uploaded lecture recordings and generated academic materials.

Key security considerations include:

- Validate uploaded audio files for supported formats and file size.
- Implement secure user authentication and authorization.
- Store lecture recordings and generated materials securely.
- Prevent unauthorized access to individual users' lecture data.
- Validate API requests and handle errors safely.
- Avoid exposing API keys and sensitive credentials in frontend code or public repositories.
- Ensure that students can access only their own lecture materials.

---

## 🧪 Testing & Evaluation Methodology

The performance of Notewise will be evaluated through functional testing and AI output quality assessment.

| Evaluation Parameter | Description |
|---|---|
| Transcription Accuracy | Evaluate speech-to-text performance using Word Error Rate (WER). |
| Notes Quality | Check generated notes for completeness, clarity and factual correctness. |
| Cheatsheet Relevance | Evaluate whether important lecture concepts are captured accurately. |
| Mindmap Accuracy | Verify the logical organization of topics and subtopics. |
| Q&A Reliability | Evaluate answer relevance and faithfulness to the uploaded lecture transcript. |
| Processing Time | Measure the time required to process recordings and generate study materials. |
| System Reliability | Test error handling, file uploads and processing status management. |

The system will be tested using different lecture recordings, including recordings with varying durations, speaking speeds and background noise levels.

The evaluation results will be used to identify areas for improvement in transcription quality, prompt design and overall system performance.

---

## ⚠️ Limitations

Although Notewise aims to automate lecture note preparation, certain limitations may affect its performance:

- Transcription accuracy may decrease when recordings contain heavy background noise or unclear speech.
- AI-generated notes may occasionally omit important information or misinterpret technical concepts.
- The quality of generated content depends on transcript accuracy and the capabilities of the selected language model.
- Processing time may increase for lengthy lecture recordings.
- Internet connectivity and third-party API availability may affect certain AI functionalities.
- Lecture-based question answering is limited by the information available in the uploaded lecture transcript.
- Large lecture recordings may require additional processing time and computational resources.

These limitations will be considered during testing and future development.

---

## 📈 Expected Outcomes

The expected outcomes of Notewise include:

- Automated conversion of lecture recordings into readable transcripts.
- Reduced manual effort in preparing academic notes.
- Structured and easy-to-understand lecture notes.
- Concise revision cheatsheets for examination preparation.
- Visual representation of topics through hierarchical mindmaps.
- Context-aware question answering based on lecture material.
- Downloadable study resources for offline learning and revision.
- An integrated platform for managing and accessing lecture-based study materials.

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
- Integration with learning management systems (LMS).

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
