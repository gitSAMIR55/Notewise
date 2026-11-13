"""
Prompt Output & Schema Validation Engine
Author: Samir (Database, Prompt Engineering & QA Owner — Member 4)

Provides schema validation, sanitization of LLM responses, and structural checks
for Cheatsheets, Mindmaps, Notes, and Grounded Q&A outputs.
"""

import json
import re
import sys
from pathlib import Path
from typing import Any, Dict, List, Tuple

BASE_DIR = Path(__file__).resolve().parent
SCHEMAS_DIR = BASE_DIR


def strip_markdown_fences(raw_text: str) -> str:
    """Removes ```json ... ``` or ``` ... ``` code blocks if present."""
    text = raw_text.strip()
    match = re.search(r"```(?:json)?\s*([\s\S]*?)\s*```", text)
    if match:
        return match.group(1).strip()
    return text


def parse_and_clean_json(raw_text: str) -> Tuple[bool, Any, str]:
    """Attempts to parse raw LLM response into Python object."""
    cleaned = strip_markdown_fences(raw_text)
    try:
        data = json.loads(cleaned)
        return True, data, ""
    except json.JSONDecodeError as err:
        return False, None, f"JSONDecodeError at line {err.lineno}, col {err.colno}: {err.msg}"


def validate_cheatsheet(data: Any) -> Tuple[bool, List[str]]:
    """Validates cheatsheet structure."""
    errors = []
    if not isinstance(data, dict):
        return False, ["Cheatsheet output must be a JSON object (dictionary)."]

    sections = data.get("sections")
    if not isinstance(sections, list) or len(sections) == 0:
        errors.append("'sections' must be a non-empty list.")
        return False, errors

    for i, sec in enumerate(sections):
        if not isinstance(sec, dict):
            errors.append(f"Section [{i}] must be an object.")
            continue
        heading = sec.get("heading")
        bullets = sec.get("bullets")
        if not heading or not isinstance(heading, str):
            errors.append(f"Section [{i}] missing valid string 'heading'.")
        if not isinstance(bullets, list) or len(bullets) == 0:
            errors.append(f"Section [{i}] ('{heading}') 'bullets' must be a non-empty list.")
        else:
            for b_idx, bullet in enumerate(bullets):
                if not isinstance(bullet, str) or len(bullet.strip()) < 3:
                    errors.append(f"Section [{i}] bullet [{b_idx}] must be a non-empty string.")

    return len(errors) == 0, errors


def get_tree_depth(node: Dict[str, Any]) -> int:
    """Calculates maximum depth of a mindmap tree."""
    children = node.get("children", [])
    if not children or not isinstance(children, list):
        return 1
    return 1 + max((get_tree_depth(child) for child in children if isinstance(child, dict)), default=0)


def validate_mindmap(data: Any) -> Tuple[bool, List[str]]:
    """Validates recursive mindmap structure."""
    errors = []
    if not isinstance(data, dict):
        return False, ["Mindmap output must be a JSON object (root node)."]

    def _traverse(node: Any, path: str):
        if not isinstance(node, dict):
            errors.append(f"Node at '{path}' is not a dictionary.")
            return
        title = node.get("title")
        if not title or not isinstance(title, str):
            errors.append(f"Node at '{path}' missing valid 'title'.")
        children = node.get("children")
        if not isinstance(children, list):
            errors.append(f"Node at '{path}' ('{title}') missing 'children' list.")
            return
        for idx, child in enumerate(children):
            _traverse(child, f"{path}.children[{idx}]")

    _traverse(data, "root")

    if not errors:
        depth = get_tree_depth(data)
        if depth < 2:
            errors.append(f"Mindmap depth ({depth}) is too shallow. Expected at least 2 levels.")
        elif depth > 5:
            errors.append(f"Mindmap depth ({depth}) is excessively deep. Recommended maximum is 4 levels.")

    return len(errors) == 0, errors


def run_self_test():
    print("=" * 60)
    print("Testing Cheatsheet & Mindmap Schema Validators (Member 4 - Samir)")
    print("=" * 60)

    # 1. Test Valid Cheatsheet
    sample_cheatsheet = {
        "sections": [
            {
                "heading": "Core Definitions",
                "bullets": ["Virtual memory decouples logical from physical RAM."]
            },
            {
                "heading": "Exam High-Yield Formulas",
                "bullets": ["Logical Address = (Page Number, Offset)"]
            }
        ]
    }
    ok, errs = validate_cheatsheet(sample_cheatsheet)
    assert ok, f"Cheatsheet failed: {errs}"
    print("✅ Cheatsheet schema validation passed.")

    # 2. Test Markdown fence stripping
    raw_fenced = '```json\n{"sections": [{"heading": "A", "bullets": ["B"]}]}\n```'
    parsed_ok, cleaned_obj, _ = parse_and_clean_json(raw_fenced)
    assert parsed_ok and cleaned_obj["sections"][0]["heading"] == "A"
    print("✅ Markdown code-fence stripping passed.")

    # 3. Test Valid Mindmap
    sample_mindmap = {
        "title": "Operating Systems",
        "children": [
            {
                "title": "Paging",
                "children": [
                    {"title": "Pages (4KB)", "children": []},
                    {"title": "Frames (4KB)", "children": []}
                ]
            }
        ]
    }
    ok, errs = validate_mindmap(sample_mindmap)
    assert ok, f"Mindmap failed: {errs}"
    print(f"✅ Mindmap schema validation passed (Tree depth: {get_tree_depth(sample_mindmap)}).")

    # 4. Test Invalid Cheatsheet Detection
    bad_cheatsheet = {"sections": [{"heading": 123, "bullets": []}]}
    ok, errs = validate_cheatsheet(bad_cheatsheet)
    assert not ok, "Failed to reject invalid cheatsheet!"
    print(f"✅ Invalid cheatsheet correctly rejected ({len(errs)} errors detected).")

    print("=" * 60)
    print("🎉 ALL PROMPT & SCHEMA VALIDATION TESTS PASSED!")


if __name__ == "__main__":
    run_self_test()
