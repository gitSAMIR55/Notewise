"""
Database & Seed Verification Utility
Author: Samir (Database, Prompt Engineering & QA Owner)

Validates SQL syntax consistency, schema integrity, and verifies that seed
data conforms strictly to the frozen API schemas and database contracts.
"""

import json
import re
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
MIGRATIONS_DIR = BASE_DIR / "migrations"
SEEDS_DIR = BASE_DIR / "seeds"


def validate_sql_file(file_path: Path) -> bool:
    print(f"[SQL Check] Inspecting {file_path.name}...")
    if not file_path.exists():
        print(f"❌ Error: {file_path} does not exist.")
        return False

    content = file_path.read_text(encoding="utf-8")
    
    # Check for basic SQL constructs
    required_keywords = ["CREATE TABLE", "INDEX"] if "schema" in file_path.name else ["INSERT INTO"]
    for kw in required_keywords:
        if kw not in content.upper():
            print(f"⚠️ Warning: Keyword '{kw}' not found in {file_path.name}")

    # Check for unmatched parentheses
    open_paren = content.count("(")
    close_paren = content.count(")")
    if open_paren != close_paren:
        print(f"❌ Error: Unmatched parentheses in {file_path.name} ({open_paren} open vs {close_paren} close)")
        return False

    print(f"✅ {file_path.name} passed structural syntax check ({len(content.splitlines())} lines).")
    return True


def validate_seed_json() -> bool:
    json_path = SEEDS_DIR / "seed_data.json"
    print(f"\n[Seed JSON Check] Validating {json_path.name}...")
    if not json_path.exists():
        print(f"❌ Error: {json_path} does not exist.")
        return False

    try:
        data = json.loads(json_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        print(f"❌ Error decoding JSON: {e}")
        return False

    recordings = data.get("recordings", [])
    if len(recordings) < 3:
        print(f"❌ Error: Expected at least 3 seed recordings, found {len(recordings)}")
        return False

    statuses_found = set()
    for rec in recordings:
        rec_id = rec.get("id")
        job = rec.get("job")
        if not job:
            print(f"❌ Error: Recording {rec_id} missing job object")
            return False
        
        status = job.get("status")
        statuses_found.add(status)

        # Validate outputs structure if done or partial
        outputs = rec.get("outputs", {})
        if status == "done":
            for out_type in ["notes", "cheatsheet", "mindmap"]:
                if out_type not in outputs:
                    print(f"❌ Error: Done job {job.get('id')} missing '{out_type}' in outputs")
                    return False

            # Check notes schema
            notes = outputs["notes"]
            assert "key_points" in notes and isinstance(notes["key_points"], list)
            assert "definitions" in notes and isinstance(notes["definitions"], list)
            assert "examples" in notes and isinstance(notes["examples"], list)
            assert "quick_revision_sheet" in notes and isinstance(notes["quick_revision_sheet"], list)

            # Check cheatsheet schema
            cheatsheet = outputs["cheatsheet"]
            assert "sections" in cheatsheet and isinstance(cheatsheet["sections"], list)
            for sec in cheatsheet["sections"]:
                assert "heading" in sec and "bullets" in sec

            # Check mindmap schema
            mindmap = outputs["mindmap"]
            assert "title" in mindmap and "children" in mindmap

    expected_statuses = {"done", "partial", "queued"}
    if not expected_statuses.issubset(statuses_found):
        print(f"❌ Error: Missing test statuses: {expected_statuses - statuses_found}")
        return False

    print(f"✅ seed_data.json verified successfully with {len(recordings)} test scenarios ({statuses_found}).")
    return True


def run_checks():
    print("=" * 60)
    print("Notewise Database & Fixtures Verification (Member 4 - Samir)")
    print("=" * 60)

    all_passed = True

    # 1. Check migrations
    for sql_file in sorted(MIGRATIONS_DIR.glob("*.sql")):
        if not validate_sql_file(sql_file):
            all_passed = False

    # 2. Check seed sql
    for seed_file in sorted(SEEDS_DIR.glob("*.sql")):
        if not validate_sql_file(seed_file):
            all_passed = False

    # 3. Check seed JSON
    if not validate_seed_json():
        all_passed = False

    print("=" * 60)
    if all_passed:
        print("🎉 ALL DATABASE & SEED CHECKS PASSED!")
    else:
        print("❌ DATABASE VERIFICATION FAILED!")
        sys.exit(1)


if __name__ == "__main__":
    run_checks()
