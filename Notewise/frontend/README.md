# Frontend Application — Member 2 (Lead)

## 📌 Ownership & Responsibilities
- **Owner:** Member 2 (Frontend Lead)
- **Tech Stack:** React, Vite, Tailwind CSS, Lucide React, Axios, html2pdf.js.
- **Scope:**
  1. Student audio uploader and browser mic recorder UI (supporting WAV, MP3, M4A, up to 100MB).
  2. Persistent browser session manager (using `localStorage` UUID).
  3. Job polling hook (`queued` $\to$ `processing` $\to$ `done` / `partial` / `failed`).
  4. Tabbed views for:
     - Structured Notes (Card layout: key points, definitions, examples, quick revision).
     - Exam Cheatsheet (Compact prioritized bullet sections).
     - Interactive Mindmap (Nested collapsible tree view).
     - Timestamped Transcript (Collapsible, synchronized segments).
     - Grounded Q&A Chat (Chat interface enforcing strict refusal messaging).
  5. Five essential view states across every tab: **loading, empty, error, partial-success, and success**.
  6. Client-side PDF export for notes and cheatsheet.
  7. Deployment to Vercel.

---

## 📂 Folder Structure

```
frontend/
├── src/
│   ├── components/     # UI widgets:
│   │   ├── AudioUploader.jsx
│   │   ├── StatusBanner.jsx
│   │   ├── NotesView.jsx
│   │   ├── CheatsheetView.jsx
│   │   ├── MindmapView.jsx
│   │   ├── TranscriptView.jsx
│   │   └── QAChat.jsx
│   ├── pages/          # Full page views (Dashboard, LectureDetail)
│   ├── hooks/          # Custom React hooks (useJobPolling, useSessionId)
│   ├── services/       # Axios API client methods (matching docs/api-contracts.md)
│   ├── utils/          # Client-side PDF generator & timestamp formatting
│   ├── types/          # Data schemas and contracts
│   ├── App.jsx         # App shell and navigation
│   └── main.jsx        # React root mounting
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
2. Copy `.env.example` to `.env`:
   ```bash
   cp .env.example .env
   ```
3. Start local development server:
   ```bash
   npm run dev
   ```

