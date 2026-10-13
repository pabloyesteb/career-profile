#!/usr/bin/env python3
"""Validate cross-references and basic invariants in 01_inventory."""

from __future__ import annotations

import csv
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
INV = ROOT / "01_inventory"


def rows(name: str) -> list[dict[str, str]]:
    with (INV / name).open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def main() -> None:
    errors: list[str] = []
    courses = rows("courses.csv")
    matches = rows("archive_matches.csv")
    summaries = rows("archive_summary.csv")
    files = rows("files_manifest.csv")
    processing = rows("processing_manifest.csv")

    course_ids = [row["course_id"] for row in courses]
    if len(course_ids) != len(set(course_ids)):
        errors.append("duplicate course_id in courses.csv")
    if set(course_ids) != {row["course_id"] for row in processing}:
        errors.append("processing_manifest course IDs do not exactly cover courses.csv")
    degree_ects = sum(float(row["ects"]) for row in courses if row["record_section"] == "degree")
    additional_ects = sum(float(row["ects"]) for row in courses if row["record_section"] == "additional_credit")
    if degree_ects != 123:
        errors.append(f"degree ECTS sum is {degree_ects}, expected 123")
    if additional_ects != 14:
        errors.append(f"additional ECTS sum is {additional_ects}, expected 14")

    archive_names = {row["archive"] for row in summaries}
    if archive_names != {row["archive"] for row in matches}:
        errors.append("archive_matches and archive_summary do not cover the same archives")
    for row in courses:
        if row["archive"] and row["archive"] not in archive_names:
            errors.append(f"unknown archive referenced by {row['course_id']}: {row['archive']}")
    for row in matches:
        if row["matched_course_id"] and row["matched_course_id"] not in course_ids:
            errors.append(f"unknown course referenced by archive match: {row['matched_course_id']}")
    for row in files:
        actual = row["actual_path"]
        if actual and not (ROOT / actual).exists():
            errors.append(f"missing actual source path: {actual}")

    if errors:
        raise SystemExit("Inventory validation failed:\n- " + "\n- ".join(errors))
    print(f"OK: {len(courses)} transcript rows, {len(archive_names)} archives, all cross-references valid")
    print(f"ECTS totals: degree={degree_ects:g}, additional={additional_ects:g}")


if __name__ == "__main__":
    main()
