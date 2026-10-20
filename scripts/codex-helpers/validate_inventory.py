#!/usr/bin/env python3
"""Validate cross-references and basic invariants in 01_inventory."""

from __future__ import annotations

import csv
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
INV = ROOT / "01_inventory"


def rows(name: str) -> list[dict[str, str]]:
    with (INV / name).open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def main() -> None:
    errors: list[str] = []
    courses = rows("courses.csv")
    matches = rows("archive_matches.csv")
    members = rows("archive_files.csv")
    registry = yaml.safe_load((INV / "sources.yaml").read_text(encoding="utf-8"))
    sources = registry["sources"]

    course_ids = [row["course_id"] for row in courses]
    if len(course_ids) != len(set(course_ids)):
        errors.append("duplicate course_id in courses.csv")
    degree_ects = sum(float(row["ects"]) for row in courses if row["record_section"] == "degree")
    additional_ects = sum(float(row["ects"]) for row in courses if row["record_section"] == "additional_credit")
    if degree_ects != 123:
        errors.append(f"degree ECTS sum is {degree_ects}, expected 123")
    if additional_ects != 14:
        errors.append(f"additional ECTS sum is {additional_ects}, expected 14")

    archive_names = {row["archive"] for row in members}
    if archive_names != {row["archive"] for row in matches}:
        errors.append("archive_matches and archive_files do not cover the same archives")
    if len(matches) != len({row["archive"] for row in matches}):
        errors.append("duplicate archive in archive_matches.csv")
    if len(members) != len({(row["archive"], row["member_path"]) for row in members}):
        errors.append("duplicate archive/member pair in archive_files.csv")
    by_course = {row["course_id"]: row for row in courses}
    for row in courses:
        if row["archive"] and row["archive"] not in archive_names:
            errors.append(f"unknown archive referenced by {row['course_id']}: {row['archive']}")
    for row in matches:
        if row["matched_course_id"] and row["matched_course_id"] not in course_ids:
            errors.append(f"unknown course referenced by archive match: {row['matched_course_id']}")
        elif row["matched_course_id"] and by_course[row["matched_course_id"]]["archive"] != row["archive"]:
            errors.append(f"course/archive correspondence disagrees: {row['archive']}")
    registered_archives = []
    for source_id, source in sources.items():
        if not source.get("title") or not source.get("type") or not source.get("locations"):
            errors.append(f"source missing title, type or locations: {source_id}")
        if source.get("course_id") and source["course_id"] not in by_course:
            errors.append(f"source references unknown course: {source_id}")
        for reference in source.get("references", []):
            if reference not in sources:
                errors.append(f"source references unknown source: {source_id} -> {reference}")
        for name, location in source.get("locations", {}).items():
            if location.startswith(("https://", "http://")):
                continue  # Remote accessibility is separate from local structural checks.
            path = Path(location)
            if not path.is_absolute():
                path = INV / path
            if not path.exists():
                errors.append(f"missing source location: {source_id}.{name}: {location}")
            if name == "archive":
                registered_archives.append(path.name)
                if source.get("course_id") in by_course and by_course[source["course_id"]]["archive"] != path.name:
                    errors.append(f"source/course archive disagrees: {source_id}")
    if set(registered_archives) != archive_names or len(registered_archives) != len(archive_names):
        errors.append("source registry must account for every archive exactly once")

    if errors:
        raise SystemExit("Inventory validation failed:\n- " + "\n- ".join(errors))
    print(f"OK: {len(courses)} transcript rows, {len(archive_names)} archives, {len(members)} members")
    print(f"OK: {len(sources)} conceptual Sources; local locations and cross-references valid")
    print(f"ECTS totals: degree={degree_ects:g}, additional={additional_ects:g}")


if __name__ == "__main__":
    main()
