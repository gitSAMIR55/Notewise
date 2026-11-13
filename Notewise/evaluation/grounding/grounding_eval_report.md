# 🛡️ Notewise Grounded Q&A Verification & Refusal Benchmark

**Conducted by:** Samir (Database, Prompt Engineering & QA Owner — Member 4)  
**Dataset:** 20 Verified Q&A Pairs (14 In-Scope, 6 Out-of-Scope)  
**Specification:** Contract-frozen Grounding & Anti-Hallucination Guardrails (`docs/api-contracts.md`)

---

## 📊 Benchmark Summary

| Evaluation Metric | Target Standard | Achieved Score | Evaluation Result |
| :--- | :---: | :---: | :---: |
| **In-Scope Grounding Traceability** | 100% | **100.0%** | ✅ PASSED |
| **Out-of-Scope Refusal Rate** | 100% | **100.0%** | ✅ PASSED |
| **Overall Contextual Faithfulness** | > 95% | **100.0%** | ✅ PASSED |

---

## 📋 Full Test Suite Verification Matrix

| Test ID | Lecture Domain | Query Type | Question | Verification Status |
| :---: | :--- | :---: | :--- | :---: |
| `qa_01` | OS: Virtual Memory & Paging | In-Scope | What is the primary motivation for virtual memory according to the lecture? | **PASS (Grounded)** |
| `qa_02` | OS: Virtual Memory & Paging | In-Scope | What is the typical size of a page mentioned in the lecture? | **PASS (Grounded)** |
| `qa_03` | OS: Virtual Memory & Paging | In-Scope | What is the difference between a page and a frame? | **PASS (Grounded)** |
| `qa_04` | OS: Virtual Memory & Paging | In-Scope | Which hardware unit performs the translation from logical page numbers to physical frame numbers? | **PASS (Grounded)** |
| `qa_05` | OS: Virtual Memory & Paging | In-Scope | When does a page fault occur? | **PASS (Grounded)** |
| `qa_06` | OS: Virtual Memory & Paging | In-Scope | What steps does the OS take to handle a page fault? | **PASS (Grounded)** |
| `qa_07` | OS: Virtual Memory & Paging | In-Scope | Why is page fault handling orders of magnitude slower than memory access? | **PASS (Grounded)** |
| `qa_08` | DBMS: Normalization & BCNF | In-Scope | What are the primary anomalies eliminated by database normalization? | **PASS (Grounded)** |
| `qa_09` | DBMS: Normalization & BCNF | In-Scope | What is the requirement for a relation to be in First Normal Form (1NF)? | **PASS (Grounded)** |
| `qa_10` | DBMS: Normalization & BCNF | In-Scope | What dependency does Second Normal Form (2NF) eliminate? | **PASS (Grounded)** |
| `qa_11` | DBMS: Normalization & BCNF | In-Scope | What is the condition for Third Normal Form (3NF)? | **PASS (Grounded)** |
| `qa_12` | DBMS: Normalization & BCNF | In-Scope | How is Boyce-Codd Normal Form (BCNF) stricter than 3NF? | **PASS (Grounded)** |
| `qa_13` | ML: Gradient Descent | In-Scope | What does the learning rate parameter alpha control in gradient descent? | **PASS (Grounded)** |
| `qa_14` | ML: Gradient Descent | In-Scope | What advantage does stochastic gradient descent provide over batch gradient descent? | **PASS (Grounded)** |
| `qa_15` | OS: Virtual Memory & Paging | Out-of-Scope | Who is the Prime Minister of the United Kingdom? | **PASS (Refusal Verified)** |
| `qa_16` | OS: Virtual Memory & Paging | Out-of-Scope | How do you implement quicksort in Python? | **PASS (Refusal Verified)** |
| `qa_17` | DBMS: Normalization & BCNF | Out-of-Scope | What is the capital city of Australia? | **PASS (Refusal Verified)** |
| `qa_18` | DBMS: Normalization & BCNF | Out-of-Scope | Can you recommend a recipe for chocolate chip cookies? | **PASS (Refusal Verified)** |
| `qa_19` | ML: Gradient Descent | Out-of-Scope | What is the distance between the Earth and the Moon in kilometers? | **PASS (Refusal Verified)** |
| `qa_20` | ML: Gradient Descent | Out-of-Scope | Explain quantum entanglement and Bell inequalities. | **PASS (Refusal Verified)** |

---

## 🧠 Architectural Grounding Mechanism

1. **Context Stuffed Prompting:**
   - Instead of fragile vector chunk retrieval that misses cross-sentence context, the complete lecture transcript is stuffed into the model's context window.
2. **Explicit Refusal Constraint:**
   - Prompt system rules mandate: *"If the question cannot be answered directly and strictly from the transcript text, respond ONLY with: 'This topic was not covered in the lecture.' and set `grounded: false`."*
3. **No External Hallucinations:**
   - Zero tolerance for external trivia or unmentioned technical extrapolations.
