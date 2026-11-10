# Evaluation & Benchmarking — Member 4 & QA

## 📌 Scope & Objectives
1. **Word Error Rate (WER) Analysis:**
   - Collect 3 real classroom audio excerpts (~3 minutes each).
   - Manually transcribe excerpts into ground truth files in `ground-truth/`.
   - Transcribe raw audio vs. cleaned audio (after noise reduction).
   - Calculate WER and compute percentage error reduction to prove the academic value of the noise-reduction stage.
2. **Human Usefulness Ratings:**
   - Collect feedback from 8–10 classmate testers using standardized rubrics (coverage, accuracy, clarity, exam-usefulness).
3. **Q&A Grounding Verification:**
   - Manually verify 20 Q&A pairs to ensure answers are strictly traceable to the transcript and out-of-scope questions are properly refused.

---

## 📂 Folder Structure

```
evaluation/
├── ground-truth/       # Verified manual transcripts (.txt) for the 3 test lectures
├── wer/                # Python scripts computing WER (using jiwer) comparing raw vs clean
├── surveys/            # Form templates and survey results from student testers
└── README.md
```

