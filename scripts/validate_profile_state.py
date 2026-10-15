#!/usr/bin/env python3
"""Check transcript/profile links and project layout, not technical claim truth."""
from __future__ import annotations

import csv
from collections import Counter
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]


def read_rows(name: str) -> list[dict[str, str]]:
    with (ROOT / "01_inventory" / name).open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def main() -> None:
    courses = read_rows("courses.csv")
    states = read_rows("processing_manifest.csv")
    by_id = {r["course_id"]: r for r in courses}
    errors = []
    linked = set()
    if len(states) != len({r["course_id"] for r in states}):
        errors.append("Duplicate manifest identifiers")
    if set(by_id) != {r["course_id"] for r in states}:
        errors.append("Manifest does not cover exactly the transcript inventory")
    excluded = {"ma6018", "ma8102", "in2138", "sz0339", "sz0341", "additional-german-b1-2"}
    project_profiles = {"ma6018": "02_profiles/projects/thesis.md",
                        "ma8102": "02_profiles/projects/pyloworder.md"}
    related_projects = {"cit413042": "02_profiles/projects/case_studies_optimization.md"}
    for state in states:
        cid = state["course_id"]
        if cid not in by_id:
            continue
        row = by_id[cid]
        if state["profile_status"] != "complete_validated":
            if cid not in excluded:
                errors.append(f"{cid}: eligible course not completed")
            continue
        is_project = cid in project_profiles
        pattern = (re.escape(project_profiles[cid]) if is_project
                   else r"02_profiles/courses/[^;\s]+\.md")
        matches = re.findall(pattern, state["next_action"])
        if len(matches) != 1:
            errors.append(f"{cid}: expected one profile link")
            continue
        relative = matches[0]
        if not is_project:
            linked.add(relative)
        path = ROOT / relative
        if not path.is_file():
            errors.append(f"{cid}: missing {relative}")
            continue
        text = path.read_text(encoding="utf-8")
        if row["module_code"] and row["module_code"] not in text:
            errors.append(f"{cid}: missing official code")
        # Support the original table format and the neuroscience prose format.
        table = dict(re.findall(r"^\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|\s*$", text, re.M))
        if "ECTS" in table:
            if table["ECTS"] != row["ects"]:
                errors.append(f"{cid}: credits mismatch")
            if not re.match(re.escape(row["grade"]) + r"(?:\s|$)", table.get("Grade", "")):
                errors.append(f"{cid}: grade mismatch")
            if table.get("Profile status") != "complete_validated":
                errors.append(f"{cid}: profile/manifest status mismatch")
        elif not (f"{row['ects']} ECTS" in text and f"**grade:** {row['grade']}" in text):
            errors.append(f"{cid}: metadata not found")
        if not re.search(r"^## .*Technical", text, re.M | re.I):
            errors.append(f"{cid}: no technical section")
        if "thematic categor" not in text.lower():
            errors.append(f"{cid}: no thematic categories")
        if "validat" not in text.lower() or "source" not in text.lower():
            errors.append(f"{cid}: missing validation/source documentation")
        if row["archive"]:
            archive = ROOT / "00_sources/tum/archives" / row["archive"]
            if not archive.is_file() or row["archive"] not in text:
                errors.append(f"{cid}: primary archive missing or not cited")
    actual = {str(p.relative_to(ROOT)) for p in (ROOT / "02_profiles/courses").glob("*.md")
              if not p.name.startswith("_")}
    if actual != linked:
        errors.append(f"Unlinked or missing profiles: {sorted(actual ^ linked)}")
    for cid, relative in related_projects.items():
        state = next((r for r in states if r["course_id"] == cid), None)
        path = ROOT / relative
        if state is None or state["profile_status"] != "complete_validated" or relative not in state["next_action"]:
            errors.append(f"{cid}: related project not linked/completed in manifest")
        if not path.is_file():
            errors.append(f"{cid}: missing related project {relative}")
            continue
        project_text = path.read_text()
        project_table = dict(re.findall(r"^\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|\s*$", project_text, re.M))
        row = by_id[cid]
        if (row["module_code"] not in project_text or project_table.get("ECTS") != row["ects"]
                or project_table.get("Grade") != row["grade"]
                or project_table.get("Profile status") != "complete_validated"):
            errors.append(f"{cid}: related project metadata/status mismatch")
    expected_projects = set(project_profiles.values()) | set(related_projects.values()) | {"02_profiles/projects/scientific_paper.md"}
    actual_projects = {str(p.relative_to(ROOT)) for p in (ROOT / "02_profiles/projects").iterdir()
                       if p.is_file()}
    if actual_projects != expected_projects:
        errors.append(f"Project root differs from definitive set: {sorted(actual_projects ^ expected_projects)}")
    paper = ROOT / "02_profiles/projects/scientific_paper.md"
    if paper.is_file() and not re.search(
        r"^\|\s*Profile status\s*\|\s*complete_validated\s*\|", paper.read_text(), re.M
    ):
        errors.append("Scientific paper is not marked complete_validated")
    for name in ("thesis_analysis.md", "pyloworder_analysis.md"):
        if not (ROOT / "02_profiles/projects/_analysis" / name).is_file():
            errors.append(f"Missing relocated internal report: {name}")
    if errors:
        raise SystemExit("State validation failed:\n- " + "\n- ".join(errors))
    print(f"OK: {len(courses)} transcript entries; {len(linked)} saved validated profiles")
    completed_projects = [r["course_id"] for r in states
                          if r["course_id"] in project_profiles
                          and r["profile_status"] == "complete_validated"]
    if completed_projects:
        print(f"Project profiles linked and metadata checked separately: {completed_projects}")
    print(f"Related course/project pairs checked without duplicate academic rows: {list(related_projects)}")
    print(dict(Counter(r["profile_status"] for r in states)))
    print("Structural checks only; source-grounded technical review is documented in each profile.")


if __name__ == "__main__":
    main()
