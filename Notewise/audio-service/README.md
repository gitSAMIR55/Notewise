# Python Audio Noise-Reduction Microservice — Member 3 (Owner)

## 📌 Ownership & Responsibilities
- **Owner:** Member 3 (Audio Processing Owner)
- **Tech Stack:** Python 3.10+, FastAPI, `uvicorn`, `noisereduce` (spectral gating), `soundfile`, `scipy`.
- **Scope:**
  1. Build a robust, isolated noise-reduction microservice using spectral gating algorithms.
  2. Implement frozen contract:
     - `GET /health` $\to$ `{"status": "ok"}`
     - `POST /clean` $\to$ Accepts multipart WAV (up to 100MB), strips noise, and streams back **raw binary WAV data**.
  3. Structured error handling for corrupted audio, oversized files, or processing exceptions.
  4. Collect real classroom audio recordings (fans, whispers, back-row echo) for testing in Week 1.
  5. Conduct before vs. after audio testing and SNR comparisons.

---

## 📂 Folder Structure

```
audio-service/
├── app/
│   ├── api/            # FastAPI route handlers (/health, /clean)
│   ├── core/           # Microservice configurations & constraints
│   ├── services/       # Spectral-gating noise reduction logic (noisereduce)
│   └── main.py         # FastAPI application entry point
├── samples/            # Real classroom test recordings (raw & cleaned)
├── tests/              # Unit tests for clean endpoint & audio validation
├── requirements.txt
├── .env.example
└── README.md
```

---

## 🛠️ Setup Instructions
1. Create and activate a Python virtual environment:
   ```bash
   python -m venv venv
   # On Windows:
   .\venv\Scripts\activate
   # On Linux/macOS:
   source venv/bin/activate
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the microservice:
   ```bash
   uvicorn app.main:app --reload --port 8000
   ```
4. Verify health endpoint:
   ```bash
   curl http://localhost:8000/health
   ```

