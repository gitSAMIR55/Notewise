-- 001_mock_data.sql
-- Notewise Realistic Seed Data for Testing & Development
-- Author: Samir (Database + Prompts + QA Owner)

-- Ensure UUID extension exists
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- Clean existing seed entries if desired (safe for idempotent re-runs)
-- DELETE FROM recordings WHERE session_id LIKE 'seed-session-%';

-- ============================================================================
-- 1. RECORDING 1 (Done state - Complete pipeline with all artifacts)
-- Topic: Operating Systems - Virtual Memory & Paging
-- ============================================================================
INSERT INTO recordings (id, session_id, original_filename, raw_audio_path, cleaned_audio_path)
VALUES (
    'a1b2c3d4-e5f6-7a8b-9c0d-1e2f3a4b5c6d',
    'seed-session-001',
    'cs301_os_virtual_memory_paging.wav',
    'uploads/raw/seed-session-001/cs301_os_virtual_memory_paging.wav',
    'uploads/cleaned/seed-session-001/cs301_os_virtual_memory_paging_cleaned.wav'
) ON CONFLICT (id) DO NOTHING;

INSERT INTO jobs (id, recording_id, status, error_message, created_at, updated_at)
VALUES (
    'b2c3d4e5-f6a7-8b9c-0d1e-2f3a4b5c6d7e',
    'a1b2c3d4-e5f6-7a8b-9c0d-1e2f3a4b5c6d',
    'done',
    NULL,
    NOW() - INTERVAL '1 hour',
    NOW() - INTERVAL '50 minutes'
) ON CONFLICT (id) DO NOTHING;

INSERT INTO transcripts (id, job_id, full_text, segments, word_count)
VALUES (
    'c3d4e5f6-a7b8-9c0d-1e2f-3a4b5c6d7e8f',
    'b2c3d4e5-f6a7-8b9c-0d1e-2f3a4b5c6d7e',
    'Good morning class. Today we will dive deep into virtual memory management, focusing on paging architecture. Why do we need virtual memory? In early computing, programs were constrained by physical RAM size. Virtual memory separates user logical memory from physical memory. Each process is given an illusion of a contiguous address space. In paging, the logical address space is divided into fixed-size blocks called pages, typically 4 kilobytes. Physical memory is divided into fixed-size blocks of the identical size called frames. The Memory Management Unit uses a page table to translate logical page numbers to physical frame numbers. A page number acts as an index into the page table. When the processor accesses a page not currently present in RAM, a page fault occurs. The OS traps to the kernel, fetches the page from backing store into a free frame, updates the page table valid-invalid bit, and restarts the instruction. Remember this for your midterms: page fault handling involves disk I/O, which is orders of magnitude slower than memory access.',
    '[
        {"start": 0.0, "end": 6.5, "text": "Good morning class. Today we will dive deep into virtual memory management, focusing on paging architecture."},
        {"start": 6.8, "end": 14.2, "text": "Why do we need virtual memory? In early computing, programs were constrained by physical RAM size."},
        {"start": 14.5, "end": 22.0, "text": "Virtual memory separates user logical memory from physical memory. Each process is given an illusion of a contiguous address space."},
        {"start": 22.5, "end": 31.0, "text": "In paging, the logical address space is divided into fixed-size blocks called pages, typically 4 kilobytes."},
        {"start": 31.5, "end": 39.0, "text": "Physical memory is divided into fixed-size blocks of the identical size called frames."},
        {"start": 39.5, "end": 48.0, "text": "The Memory Management Unit uses a page table to translate logical page numbers to physical frame numbers."},
        {"start": 48.5, "end": 57.0, "text": "When the processor accesses a page not currently present in RAM, a page fault occurs."},
        {"start": 57.5, "end": 68.0, "text": "The OS traps to the kernel, fetches the page from backing store, updates the valid bit, and restarts the instruction."}
    ]'::jsonb,
    184
) ON CONFLICT (id) DO NOTHING;

-- Outputs for Recording 1 (Notes, Cheatsheet, Mindmap, QA)
INSERT INTO outputs (id, job_id, type, content)
VALUES 
(
    'd4e5f6a7-b8c9-0d1e-2f3a-4b5c6d7e8f9a',
    'b2c3d4e5-f6a7-8b9c-0d1e-2f3a4b5c6d7e',
    'notes',
    '{
        "key_points": [
            "Virtual memory decouples user logical address space from physical RAM.",
            "Pages represent fixed-size logical memory chunks (typically 4KB).",
            "Frames represent fixed-size physical memory blocks matching page size.",
            "The Memory Management Unit (MMU) uses page tables for address translation.",
            "Page faults trigger OS traps, disk fetch, page table update, and instruction restart."
        ],
        "definitions": [
            {
                "term": "Virtual Memory",
                "definition": "A memory management technique that provides an idealized abstraction of the storage resources that are actually available on a given machine."
            },
            {
                "term": "Paging",
                "definition": "A memory management scheme by which a computer stores and retrieves data from secondary storage for use in main memory in same-size blocks."
            },
            {
                "term": "Page Fault",
                "definition": "An interrupt raised by hardware when a running program accesses a memory page mapped into the virtual address space, but not loaded in physical RAM."
            }
        ],
        "examples": [
            "A standard 4KB page size mapping between virtual logical addresses and physical RAM frames."
        ],
        "quick_revision_sheet": [
            "Logical = Pages | Physical = Frames",
            "MMU: Logical Address (Page # + Offset) -> Physical Address (Frame # + Offset)",
            "Page Fault Service Time: Traps -> Disk I/O -> Update Valid Bit -> Restart"
        ]
    }'::jsonb
),
(
    'e5f6a7b8-c9d0-1e2f-3a4b-5c6d7e8f9a0b',
    'b2c3d4e5-f6a7-8b9c-0d1e-2f3a4b5c6d7e',
    'cheatsheet',
    '{
        "sections": [
            {
                "heading": "Core Definitions & Terminology",
                "bullets": [
                    "Pages: Fixed-size logical address blocks (typically 4 KB).",
                    "Frames: Fixed-size physical memory blocks matching page size.",
                    "MMU: Hardware chip performing virtual-to-physical address translation."
                ]
            },
            {
                "heading": "Paging Translation Formula",
                "bullets": [
                    "Logical Address = (Page Number p, Page Offset d)",
                    "Physical Address = (Frame Number f, Page Offset d)",
                    "Page size p_size must equal frame size f_size (power of 2)."
                ]
            },
            {
                "heading": "Page Fault Lifecycle (Exam High-Yield)",
                "bullets": [
                    "Step 1: Check internal page table valid-invalid bit (0 = invalid / page fault).",
                    "Step 2: Trap to OS kernel trap vector.",
                    "Step 3: Locate missing page on backing storage (swap disk).",
                    "Step 4: Bring missing page into a free physical frame.",
                    "Step 5: Update page table entry valid bit to 1.",
                    "Step 6: Restart instruction that caused page fault."
                ]
            },
            {
                "heading": "Common Exam Pitfalls & Pitfall Traps",
                "bullets": [
                    "Page offset is NEVER translated; only the page number is replaced with frame number.",
                    "Internal fragmentation can occur in the final page of a process (average half page).",
                    "External fragmentation is eliminated by paging because all allocation occurs in uniform blocks."
                ]
            }
        ]
    }'::jsonb
),
(
    'f6a7b8c9-d0e1-2f3a-4b5c-6d7e8f9a0b1c',
    'b2c3d4e5-f6a7-8b9c-0d1e-2f3a4b5c6d7e',
    'mindmap',
    '{
        "title": "Virtual Memory Management",
        "children": [
            {
                "title": "Motivation",
                "children": [
                    { "title": "Overcome RAM physical limits", "children": [] },
                    { "title": "Process isolation and protection", "children": [] },
                    { "title": "Contiguous address space illusion", "children": [] }
                ]
            },
            {
                "title": "Paging Architecture",
                "children": [
                    { "title": "Logical Pages (Fixed 4KB)", "children": [] },
                    { "title": "Physical Frames (Fixed 4KB)", "children": [] },
                    { "title": "Page Table Translation via MMU", "children": [] }
                ]
            },
            {
                "title": "Page Fault Handling",
                "children": [
                    { "title": "Hardware Trap on Invalid Bit", "children": [] },
                    { "title": "Backing Store Disk Fetch", "children": [] },
                    { "title": "Page Table Update & Instruction Restart", "children": [] }
                ]
            }
        ]
    }'::jsonb
),
(
    'a7b8c9d0-e1f2-3a4b-5c6d-7e8f9a0b1c2d',
    'b2c3d4e5-f6a7-8b9c-0d1e-2f3a4b5c6d7e',
    'qa',
    '{
        "verified_eval_pairs": [
            {
                "question": "What is the difference between pages and frames in paging?",
                "expected_answer": "Pages are fixed-size blocks in the logical address space (typically 4KB), while frames are fixed-size blocks of the same size in physical memory (RAM).",
                "grounded": true
            },
            {
                "question": "What sequence of events occurs during a page fault?",
                "expected_answer": "The OS traps to the kernel, fetches the required page from backing store into a free frame, updates the page table valid-invalid bit, and restarts the instruction.",
                "grounded": true
            },
            {
                "question": "Who invented the Python programming language?",
                "expected_answer": "This topic was not covered in the lecture.",
                "grounded": false
            }
        ]
    }'::jsonb
)
ON CONFLICT (job_id, type) DO NOTHING;

-- ============================================================================
-- 2. RECORDING 2 (Partial state - Demonstrating retry capability)
-- Topic: Database Management - Normalization (3NF & BCNF)
-- Notes & Cheatsheet completed; Mindmap failed (waiting for retry)
-- ============================================================================
INSERT INTO recordings (id, session_id, original_filename, raw_audio_path, cleaned_audio_path)
VALUES (
    'b1c2d3e4-f5a6-7b8c-9d0e-1f2a3b4c5d6e',
    'seed-session-002',
    'cs402_db_normalization_bcnf.mp3',
    'uploads/raw/seed-session-002/cs402_db_normalization_bcnf.mp3',
    'uploads/cleaned/seed-session-002/cs402_db_normalization_bcnf_cleaned.wav'
) ON CONFLICT (id) DO NOTHING;

INSERT INTO jobs (id, recording_id, status, error_message, created_at, updated_at)
VALUES (
    'c2d3e4f5-a6b7-8c9d-0e1f-2a3b4c5d6e7f',
    'b1c2d3e4-f5a6-7b8c-9d0e-1f2a3b4c5d6e',
    'partial',
    'Mindmap generation timed out after 30000ms',
    NOW() - INTERVAL '30 minutes',
    NOW() - INTERVAL '25 minutes'
) ON CONFLICT (id) DO NOTHING;

INSERT INTO transcripts (id, job_id, full_text, segments, word_count)
VALUES (
    'd3e4f5a6-b7c8-9d0e-1f2a-3b4c5d6e7f8a',
    'c2d3e4f5-a6b7-8c9d-0e1f-2a3b4c5d6e7f',
    'Welcome back students. Today we discuss database normalization up to Boyce-Codd Normal Form or BCNF. Why normalize? To eliminate insertion, deletion, and update anomalies and minimize redundant data storage. In First Normal Form or 1NF, every column contains atomic values. In Second Normal Form or 2NF, we are already in 1NF and there is no partial dependency; non-prime attributes must depend on the whole candidate key. In Third Normal Form or 3NF, for every functional dependency X determines Y, either X is a superkey or Y is a prime attribute. BCNF is stricter: for every non-trivial functional dependency X determines Y, X MUST be a superkey. Every relation in BCNF is in 3NF, but not every 3NF relation is in BCNF.',
    '[
        {"start": 0.0, "end": 5.0, "text": "Welcome back students. Today we discuss database normalization up to BCNF."},
        {"start": 5.2, "end": 12.0, "text": "Why normalize? To eliminate insertion, deletion, and update anomalies and minimize redundant data."},
        {"start": 12.5, "end": 18.0, "text": "In First Normal Form, every column contains atomic values with no repeating groups."},
        {"start": 18.5, "end": 26.0, "text": "In Second Normal Form, no non-prime attribute may partially depend on any candidate key."},
        {"start": 26.5, "end": 35.0, "text": "In Third Normal Form, transitive dependencies are eliminated: X is superkey or Y is prime attribute."},
        {"start": 35.5, "end": 45.0, "text": "In BCNF, for every functional dependency X determines Y, X strictly must be a superkey."}
    ]'::jsonb,
    145
) ON CONFLICT (id) DO NOTHING;

-- Outputs for Recording 2 (Only notes and cheatsheet exist; mindmap missing)
INSERT INTO outputs (id, job_id, type, content)
VALUES 
(
    'e4f5a6b7-c8d9-0e1f-2a3b-4c5d6e7f8a9b',
    'c2d3e4f5-a6b7-8c9d-0e1f-2a3b4c5d6e7f',
    'notes',
    '{
        "key_points": [
            "Normalization eliminates redundancy and insertion, deletion, and update anomalies.",
            "1NF requires atomic column attributes.",
            "2NF eliminates partial dependency on composite candidate keys.",
            "3NF eliminates transitive dependencies (X is superkey OR Y is prime attribute).",
            "BCNF requires determinant X to be a superkey for all non-trivial dependencies."
        ],
        "definitions": [
            {
                "term": "Functional Dependency (FD)",
                "definition": "A relationship between attributes where the value of X uniquely determines the value of Y."
            },
            {
                "term": "BCNF",
                "definition": "Boyce-Codd Normal Form: A relation where for every non-trivial functional dependency X -> Y, X is a superkey."
            }
        ],
        "examples": [
            "Relation R(A, B, C) with FDs AB -> C and C -> B is in 3NF but violates BCNF."
        ],
        "quick_revision_sheet": [
            "1NF: Atomic values only",
            "2NF: 1NF + No partial dependencies",
            "3NF: 2NF + No transitive dependencies (X is superkey OR Y is prime)",
            "BCNF: Stricter 3NF (X MUST be superkey)"
        ]
    }'::jsonb
),
(
    'f5a6b7c8-d9e0-1f2a-3b4c-5d6e7f8a9b0c',
    'c2d3e4f5-a6b7-8c9d-0e1f-2a3b4c5d6e7f',
    'cheatsheet',
    '{
        "sections": [
            {
                "heading": "Normal Forms Comparison Matrix",
                "bullets": [
                    "1NF: Atomic attributes, no repeating groups.",
                    "2NF: 1NF + No partial dependencies on candidate keys.",
                    "3NF: 2NF + For every X -> Y, X is superkey OR Y is prime attribute.",
                    "BCNF: For every non-trivial X -> Y, X MUST be a superkey."
                ]
            },
            {
                "heading": "High-Yield BCNF vs 3NF Rule",
                "bullets": [
                    "All BCNF schemas are in 3NF.",
                    "Not all 3NF schemas are in BCNF (when Y is prime but X is not a superkey).",
                    "BCNF may lose functional dependency preservation during decomposition."
                ]
            }
        ]
    }'::jsonb
)
ON CONFLICT (job_id, type) DO NOTHING;

-- ============================================================================
-- 3. RECORDING 3 (Queued state - Freshly uploaded lecture)
-- Topic: Machine Learning - Gradient Descent
-- ============================================================================
INSERT INTO recordings (id, session_id, original_filename, raw_audio_path, cleaned_audio_path)
VALUES (
    'c1d2e3f4-a5b6-7c8d-9e0f-1a2b3c4d5e6f',
    'seed-session-003',
    'cs480_ml_gradient_descent.m4a',
    'uploads/raw/seed-session-003/cs480_ml_gradient_descent.m4a',
    NULL
) ON CONFLICT (id) DO NOTHING;

INSERT INTO jobs (id, recording_id, status, error_message, created_at, updated_at)
VALUES (
    'd2e3f4a5-b6c7-8d9e-0f1a-2b3c4d5e6f7a',
    'c1d2e3f4-a5b6-7c8d-9e0f-1a2b3c4d5e6f',
    'queued',
    NULL,
    NOW() - INTERVAL '2 minutes',
    NOW() - INTERVAL '2 minutes'
) ON CONFLICT (id) DO NOTHING;
