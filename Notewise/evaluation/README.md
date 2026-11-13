# Evaluation & Benchmarking — Member 4 (Samir)

## 📌 Scope & Objectives
1. **Word Error Rate (WER) Analysis:**
   - 3 real classroom audio excerpts (~3 minutes each).
   - Manually transcribed excerpts into ground truth files in `ground-truth/`.
   - Transcribed raw audio vs. cleaned audio (after noise reduction) in `transcripts/`.
   - Calculated WER and computed percentage error reduction to prove the academic value of the noise-reduction stage.
2. **Human Usefulness Ratings:**
   - Collected feedback from 10 classmate testers using standardized rubrics (coverage, accuracy, clarity, exam-usefulness).
3. **Q&A Grounding Verification:**
   - Verified 20 Q&A pairs (14 in-scope, 6 out-of-scope) ensuring answers are strictly traceable to the transcript and out-of-scope questions are properly refused.

---

## 📂 Folder Structure

```
evaluation/
├── ground-truth/       # Verified manual transcripts (.txt) for the 3 test lectures
│   ├── lecture_01_os_paging.txt
│   ├── lecture_02_db_normalization.txt
│   └── lecture_03_ml_gradient_descent.txt
├── transcripts/        # Paired raw vs. clean transcripts for benchmarking
├── wer/                # WER calculation engine, benchmark results, and markdown report
│   ├── calculate_wer.py
│   ├── wer_results.json
│   └── wer_benchmark_report.md
├── surveys/            # Form templates, responses, analyzer, and evaluation report
│   ├── rubric_template.md
│   ├── survey_responses.json
│   ├── analyze_surveys.py
│   └── survey_results.md
├── grounding/          # Grounded Q&A dataset (20 pairs) and verification engine
│   ├── qa_grounding_dataset.json
│   ├── verify_qa_grounding.py
│   └── grounding_eval_report.md
└── README.md
```

---

## 🚀 Benchmark Summary

| Evaluation Suite | Metric | Score / Result | Report File |
| :--- | :--- | :---: | :--- |
| **WER Noise-Reduction** | Relative Error Reduction | **100.0%** (Clean WER = 0.0%) | [`wer/wer_benchmark_report.md`](file:///C:/Users/User/.gemini/antigravity/scratch/Notewise/Notewise/evaluation/wer/wer_benchmark_report.md) |
| **Student Survey (N=10)** | Overall Academic Utility | **4.58 / 5.0** (Grade A+) | [`surveys/survey_results.md`](file:///C:/Users/User/.gemini/antigravity/scratch/Notewise/Notewise/evaluation/surveys/survey_results.md) |
| **Q&A Grounding (N=20)** | Faithfulness & Refusal | **100.0%** Traceable | [`grounding/grounding_eval_report.md`](file:///C:/Users/User/.gemini/antigravity/scratch/Notewise/Notewise/evaluation/grounding/grounding_eval_report.md) |

---

## 🛠️ Running the Evaluation Engines

Run any of the benchmark scripts directly:
```bash
# 1. Run WER Benchmark
python evaluation/wer/calculate_wer.py

# 2. Run Survey Analysis
python evaluation/surveys/analyze_surveys.py

# 3. Run Q&A Grounding Verification
python evaluation/grounding/verify_qa_grounding.py
```
