#!/usr/bin/env python3
"""Validate metadata, status, headings, and primary evidence for pilot profiles."""

from __future__ import annotations

import csv
import zipfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PILOTS = {
    "ma3001": {
        "profile": "02_profiles/courses/ma3001-functional-analysis.md",
        "members": ["Materials/Lecture notes.pdf", "Materials/Distributions.pdf", "Mock Exam/Mock Exam.pdf"],
    },
    "ma4502": {
        "profile": "02_profiles/courses/ma4502-combinatorial-optimization.md",
        "members": ["Lecture Notes/lecture notes.pdf", "Problem Sheets/Exercise Sheet 11/exercise_sheet_11.pdf"],
    },
    "ma5348": {
        "profile": "02_profiles/courses/ma5348-numerical-methods-uncertainty-quantification.md",
        "members": [
            "Lecture Notes/Lecture Notes (Updated on 15.07.24)",
            "Lecture Notes/Slides on Multilevel BLUE (27.06.24)",
            "Oral exam/Topics and sample questions (08.07.24)",
            "Problem Sheets/SG_matlab.zip",
        ],
    },
}
REQUIRED_HEADINGS = [
    "## Module metadata",
    "## Evidence base and material structure",
    "## Technical content",
    "## Thematic categories",
    "## Coverage validation",
    "## Sources",
]


def csv_by_id(path: Path) -> dict[str, dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return {row["course_id"]: row for row in csv.DictReader(handle)}


def main() -> None:
    courses = csv_by_id(ROOT / "01_inventory/courses.csv")
    processing = csv_by_id(ROOT / "01_inventory/processing_manifest.csv")
    errors: list[str] = []

    for course_id, spec in PILOTS.items():
        course = courses[course_id]
        state = processing[course_id]
        profile_path = ROOT / spec["profile"]
        text = profile_path.read_text(encoding="utf-8")
        expected_table_values = {
            "Module code": course["module_code"],
            "ECTS": course["ects"],
            "Grade": course["grade"],
            "Profile status": "complete_validated",
        }
        for field, value in expected_table_values.items():
            if f"| {field} | {value} |" not in text:
                errors.append(f"{course_id}: missing or inconsistent {field}={value}")
        for heading in REQUIRED_HEADINGS:
            if heading not in text:
                errors.append(f"{course_id}: missing heading {heading}")
        if state["profile_status"] != "complete_validated":
            errors.append(f"{course_id}: processing status is {state['profile_status']}")
        if spec["profile"] not in state["next_action"]:
            errors.append(f"{course_id}: processing manifest does not link profile")

        archive_path = ROOT / "00_sources/tum/archives" / course["archive"]
        with zipfile.ZipFile(archive_path) as zf:
            names = set(zf.namelist())
        for member in spec["members"]:
            if member not in names:
                errors.append(f"{course_id}: missing cited primary member {member}")

    if errors:
        raise SystemExit("Pilot profile validation failed:\n- " + "\n- ".join(errors))
    print(f"OK: {len(PILOTS)} pilot profiles match transcript metadata and processing status")
    print("OK: required sections and cited primary archive members are present")


if __name__ == "__main__":
    main()
