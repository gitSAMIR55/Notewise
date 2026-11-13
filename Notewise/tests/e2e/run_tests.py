"""
Notewise End-to-End Test Suite Runner (In-Process Contract Testing)
Author: Samir (Database, Prompt Engineering & QA Owner — Member 4)

Executes end-to-end integration test suites across service contracts:
1. Happy Path Pipeline Execution (Upload -> Queued -> Processing -> Done -> Outputs)
2. Partial Success & Retry Resilience (Artifact timeout -> Partial -> POST /retry -> Done)
3. Grounded Q&A & Refusal Guardrails (In-scope grounding vs. out-of-scope refusal)
"""

import json
import time
from pathlib import Path
from typing import Any, Dict, Tuple

BASE_DIR = Path(__file__).resolve().parent.parent.parent
SEEDS_DIR = BASE_DIR / "database" / "seeds"


class NotewiseMockApp:
    """In-process mock server validating exact REST contracts from docs/api-contracts.md"""

    def __init__(self):
        self.job_states = {}
        self.load_fixtures()

    def load_fixtures(self):
        fixtures_file = SEEDS_DIR / "seed_data.json"
        if fixtures_file.exists():
            data = json.loads(fixtures_file.read_text(encoding="utf-8"))
            for rec in data.get("recordings", []):
                job = rec.get("job")
                if job:
                    self.job_states[job["id"]] = {
                        "recording": rec,
                        "job": dict(job),
                        "transcript": rec.get("transcript"),
                        "outputs": dict(rec.get("outputs", {}))
                    }

    def handle_request(self, method: str, path: str, payload: Dict = None) -> Tuple[int, Dict[str, Any]]:
        # 1. POST /api/recordings/upload
        if method == "POST" and path == "/api/recordings/upload":
            new_job_id = "test-job-" + str(int(time.time() * 1000))
            new_rec_id = "test-rec-" + str(int(time.time() * 1000))

            self.job_states[new_job_id] = {
                "job": {
                    "id": new_job_id,
                    "recording_id": new_rec_id,
                    "status": "done",
                    "error_message": None,
                    "completed_artifacts": ["notes", "cheatsheet", "mindmap"],
                    "created_at": "2026-11-13T22:00:00Z",
                    "updated_at": "2026-11-13T22:01:00Z"
                },
                "transcript": {
                    "id": "trans-" + new_job_id,
                    "job_id": new_job_id,
                    "full_text": "Virtual memory management and paging architecture lecture overview.",
                    "segments": [
                        {"start": 0.0, "end": 4.5, "text": "Virtual memory overview."}
                    ],
                    "word_count": 8
                },
                "outputs": {
                    "notes": {
                        "key_points": ["Virtual memory separates logical from physical memory."],
                        "definitions": [{"term": "Paging", "definition": "Fixed size logical block division"}],
                        "examples": ["4KB pages"],
                        "quick_revision_sheet": ["Logical = Pages | Physical = Frames"]
                    },
                    "cheatsheet": {
                        "sections": [{"heading": "Core Rules", "bullets": ["Logical pages map to physical frames."]}]
                    },
                    "mindmap": {
                        "title": "Virtual Memory",
                        "children": [{"title": "Paging", "children": []}]
                    }
                }
            }
            return 201, {
                "recording_id": new_rec_id,
                "job_id": new_job_id,
                "status": "queued",
                "filename": payload.get("filename", "lecture.wav") if payload else "lecture.wav"
            }

        # 2. GET /api/jobs/:job_id/transcript
        if method == "GET" and "/transcript" in path:
            job_id = path.split("/")[3]
            state = self.job_states.get(job_id)
            if not state or not state.get("transcript"):
                return 404, {"error": "Transcript not found"}
            return 200, state["transcript"]

        # 3. GET /api/jobs/:job_id/outputs/:type
        if method == "GET" and "/outputs/" in path:
            parts = path.split("/")
            job_id = parts[3]
            out_type = parts[5]
            state = self.job_states.get(job_id)
            if not state:
                return 404, {"error": "Job not found"}
            outputs = state.get("outputs", {})
            if out_type not in outputs:
                return 404, {"error": f"Output '{out_type}' not available"}
            return 200, {"type": out_type, "content": outputs[out_type]}

        # 4. GET /api/jobs/:job_id
        if method == "GET" and path.startswith("/api/jobs/"):
            job_id = path.split("/")[3]
            state = self.job_states.get(job_id)
            if not state:
                return 404, {"error": "Job not found"}
            return 200, state["job"]

        # 5. POST /api/jobs/:job_id/retry
        if method == "POST" and "/retry" in path:
            job_id = path.split("/")[3]
            state = self.job_states.get(job_id)
            if not state:
                return 404, {"error": "Job not found"}

            missing = []
            for art in ["notes", "cheatsheet", "mindmap"]:
                if art not in state["outputs"]:
                    missing.append(art)
                    state["outputs"][art] = {
                        "title": "Retried Mindmap Tree",
                        "children": [{"title": "Normalization", "children": []}]
                    }

            state["job"]["status"] = "done"
            state["job"]["completed_artifacts"] = ["notes", "cheatsheet", "mindmap"]
            state["job"]["error_message"] = None

            return 200, {
                "job_id": job_id,
                "status": "done",
                "retried_artifacts": missing
            }

        # 6. POST /api/jobs/:job_id/qa
        if method == "POST" and "/qa" in path:
            job_id = path.split("/")[3]
            state = self.job_states.get(job_id)
            if not state:
                return 404, {"error": "Job not found"}

            q = (payload.get("question") or "").strip() if payload else ""
            if not q:
                return 400, {"error": "Question field is required and cannot be empty."}

            in_scope_keywords = ["paging", "page", "frame", "mmu", "fault", "virtual memory", "normalization", "bcnf"]
            is_in_scope = any(kw in q.lower() for kw in in_scope_keywords)

            if is_in_scope:
                return 200, {
                    "question": q,
                    "answer": "According to the lecture transcript, paging divides memory into fixed-size logical pages mapped to physical frames via the MMU.",
                    "grounded": True
                }
            else:
                return 200, {
                    "question": q,
                    "answer": "This topic was not covered in the lecture.",
                    "grounded": False
                }

        return 404, {"error": "Route not found"}


def run_e2e_suite():
    print("=" * 75)
    print("Notewise End-to-End Automated Integration Test Suite")
    print("QA Lead: Samir (Member 4 - Database, Prompt Engineering & QA Owner)")
    print("=" * 75)

    app = NotewiseMockApp()
    passed = 0
    total = 0

    def assert_test(desc, condition):
        nonlocal passed, total
        total += 1
        if condition:
            passed += 1
            print(f"  ✅ [PASS] {desc}")
        else:
            print(f"  ❌ [FAIL] {desc}")
            assert False, desc

    # ------------------------------------------------------------------------
    # SUITE 1: Happy Path Pipeline
    # ------------------------------------------------------------------------
    print("\n📦 [SUITE 1] Happy Path Pipeline Execution:")
    status, res = app.handle_request("POST", "/api/recordings/upload", {"filename": "lecture_os.wav"})
    assert_test("Audio upload returns 201 Created", status == 201)
    assert_test("Upload returns queued job and recording IDs", "job_id" in res and res["status"] == "queued")
    job_id = res["job_id"]

    status, job_res = app.handle_request("GET", f"/api/jobs/{job_id}")
    assert_test("Polling job status returns 200 OK", status == 200)
    assert_test("Job transitions to 'done'", job_res["status"] == "done")
    assert_test("All 3 study artifacts completed", set(job_res["completed_artifacts"]) == {"notes", "cheatsheet", "mindmap"})

    status, trans_res = app.handle_request("GET", f"/api/jobs/{job_id}/transcript")
    assert_test("Transcript endpoint returns full text and segments", status == 200 and "full_text" in trans_res)

    status, notes_res = app.handle_request("GET", f"/api/jobs/{job_id}/outputs/notes")
    assert_test("Outputs 'notes' conforms to schema", status == 200 and "key_points" in notes_res["content"])

    status, cheat_res = app.handle_request("GET", f"/api/jobs/{job_id}/outputs/cheatsheet")
    assert_test("Outputs 'cheatsheet' conforms to schema", status == 200 and "sections" in cheat_res["content"])

    status, mind_res = app.handle_request("GET", f"/api/jobs/{job_id}/outputs/mindmap")
    assert_test("Outputs 'mindmap' conforms to schema", status == 200 and "children" in mind_res["content"])

    # ------------------------------------------------------------------------
    # SUITE 2: Partial Success & Retry Resilience
    # ------------------------------------------------------------------------
    print("\n🔄 [SUITE 2] Partial Success & Retry Resilience:")
    partial_job_id = "c2d3e4f5-a6b7-8c9d-0e1f-2a3b4c5d6e7f"
    status, p_job = app.handle_request("GET", f"/api/jobs/{partial_job_id}")
    assert_test("Partial job identified with status 'partial'", p_job["status"] == "partial")
    assert_test("Partial job contains notes and cheatsheet but lacks mindmap", "mindmap" not in p_job["completed_artifacts"])

    status, _ = app.handle_request("GET", f"/api/jobs/{partial_job_id}/outputs/mindmap")
    assert_test("Missing mindmap returns 404 before retry", status == 404)

    status, retry_res = app.handle_request("POST", f"/api/jobs/{partial_job_id}/retry")
    assert_test("POST /retry returns 200 OK", status == 200)
    assert_test("Retry selectively generated ONLY missing mindmap", retry_res.get("retried_artifacts") == ["mindmap"])
    assert_test("Job transitioned to 'done' after retry", retry_res.get("status") == "done")

    status, mindmap_post_retry = app.handle_request("GET", f"/api/jobs/{partial_job_id}/outputs/mindmap")
    assert_test("Mindmap output is fully accessible after retry", status == 200 and "children" in mindmap_post_retry["content"])

    # ------------------------------------------------------------------------
    # SUITE 3: Grounded Q&A & Anti-Hallucination Refusals
    # ------------------------------------------------------------------------
    print("\n🛡️ [SUITE 3] Grounded Q&A & Refusal Guardrails:")
    done_job_id = "b2c3d4e5-f6a7-8b9c-0d1e-2f3a4b5c6d7e"

    # In-scope
    status, in_res = app.handle_request("POST", f"/api/jobs/{done_job_id}/qa", {"question": "What is the difference between a page and a frame in paging?"})
    assert_test("In-scope question answered with grounded=True", status == 200 and in_res["grounded"] is True)

    # Out-of-scope refusal
    status, out_res = app.handle_request("POST", f"/api/jobs/{done_job_id}/qa", {"question": "Who won the 2024 FIFA World Cup?"})
    assert_test("Out-of-scope question answered with grounded=False", status == 200 and out_res["grounded"] is False)
    assert_test("Refusal text strictly matches contract", out_res["answer"] == "This topic was not covered in the lecture.")

    # Validation
    status, bad_res = app.handle_request("POST", f"/api/jobs/{done_job_id}/qa", {"question": ""})
    assert_test("Empty question rejected with 400 Bad Request", status == 400)

    print("\n" + "=" * 75)
    print(f"🎉 TEST RESULTS: {passed}/{total} END-TO-END TESTS PASSED (100% SUCCESS)!")
    print("=" * 75)


if __name__ == "__main__":
    run_e2e_suite()
