#!/usr/bin/env python3
"""Inventory ZIP archives without extracting or executing their contents."""

from __future__ import annotations

import argparse
import csv
import re
import stat
import zipfile
from collections import Counter, defaultdict
from pathlib import Path, PurePosixPath


MATERIAL_RULES = (
    ("solution", ("solution", "solutions", "loesung", "lösung", "musterloes", "sol_")),
    ("exercise", ("exercise", "exercises", "uebung", "übung", "sheet", "problem_set", "homework")),
    ("exam", ("exam", "examination", "klausur", "midterm", "final_exam")),
    ("project", ("project", "projekt", "assignment", "submission")),
    ("lecture_notes", ("lecture", "lectures", "script", "skript", "notes", "slides", "chapter")),
    ("syllabus_or_schedule", ("syllabus", "schedule", "timetable", "course_description", "module_description")),
    ("code", ("code", "src", "source", "notebook", "implementation")),
    ("data", ("data", "dataset", "results")),
)

CODE_EXTENSIONS = {".c", ".cc", ".cpp", ".h", ".hpp", ".java", ".jl", ".m", ".py", ".r", ".rs", ".sh"}
DOCUMENT_EXTENSIONS = {".doc", ".docx", ".html", ".md", ".odp", ".ods", ".odt", ".pdf", ".ppt", ".pptx", ".tex", ".txt", ".xls", ".xlsx"}


def classify(name: str) -> str:
    lowered = re.sub(r"[^\w]+", "_", name.casefold())
    suffix = PurePosixPath(name).suffix.casefold()
    if suffix in DOCUMENT_EXTENSIONS and re.search(r"(?:^|_)lect(?:ure)?\d+(?:_|$)", lowered):
        return "lecture_notes"
    for material, needles in MATERIAL_RULES:
        if any(re.search(rf"(?:^|_){re.escape(needle.strip('_'))}(?:s)?(?:_|$)", lowered) for needle in needles):
            return material
    if suffix in CODE_EXTENSIONS or suffix == ".ipynb":
        return "code"
    if suffix in DOCUMENT_EXTENSIONS:
        return "other_document"
    if suffix in {".csv", ".json", ".mat", ".npy", ".npz", ".tsv", ".xml", ".yaml", ".yml"}:
        return "data"
    if suffix in {".zip", ".tar", ".gz", ".tgz", ".bz2", ".7z", ".rar"}:
        return "nested_archive"
    if suffix in {".jpg", ".jpeg", ".png", ".gif", ".svg", ".mp4", ".mov", ".avi", ".mp3", ".wav"}:
        return "media"
    return "other"


def write_csv(path: Path, fieldnames: list[str], rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("archive_directory", type=Path)
    parser.add_argument("output_directory", type=Path)
    args = parser.parse_args()

    member_rows: list[dict[str, object]] = []
    summary_rows: list[dict[str, object]] = []
    fingerprints: dict[tuple[int, int], list[tuple[str, str]]] = defaultdict(list)

    for archive in sorted(args.archive_directory.glob("*.zip"), key=lambda p: p.name.casefold()):
        counts: Counter[str] = Counter()
        extensions: Counter[str] = Counter()
        top_levels: Counter[str] = Counter()
        unsafe = encrypted = symlinks = 0
        total_uncompressed = 0
        try:
            with zipfile.ZipFile(archive) as zf:
                bad_member = zf.testzip()
                for info in zf.infolist():
                    if info.is_dir():
                        continue
                    pure = PurePosixPath(info.filename)
                    parts = pure.parts
                    is_unsafe = pure.is_absolute() or ".." in parts
                    mode = info.external_attr >> 16
                    is_symlink = stat.S_ISLNK(mode)
                    material = classify(info.filename)
                    suffix = pure.suffix.casefold() or "[none]"
                    counts[material] += 1
                    extensions[suffix] += 1
                    top_levels[parts[0] if parts else "[root]"] += 1
                    unsafe += int(is_unsafe)
                    encrypted += int(bool(info.flag_bits & 0x1))
                    symlinks += int(is_symlink)
                    total_uncompressed += info.file_size
                    fingerprints[(info.CRC, info.file_size)].append((archive.name, info.filename))
                    member_rows.append({
                        "archive": archive.name,
                        "member_path": info.filename,
                        "size_bytes": info.file_size,
                        "compressed_bytes": info.compress_size,
                        "crc32": f"{info.CRC:08x}",
                        "extension": suffix,
                        "material_type": material,
                        "encrypted": bool(info.flag_bits & 0x1),
                        "symlink": is_symlink,
                        "unsafe_path": is_unsafe,
                    })
                summary_rows.append({
                    "archive": archive.name,
                    "archive_size_bytes": archive.stat().st_size,
                    "file_count": sum(counts.values()),
                    "uncompressed_bytes": total_uncompressed,
                    "material_types": "; ".join(f"{k}:{v}" for k, v in sorted(counts.items())),
                    "top_extensions": "; ".join(f"{k}:{v}" for k, v in extensions.most_common(12)),
                    "top_level_entries": "; ".join(f"{k}:{v}" for k, v in top_levels.most_common(12)),
                    "encrypted_files": encrypted,
                    "symlinks": symlinks,
                    "unsafe_paths": unsafe,
                    "zip_integrity": "ok" if bad_member is None else f"bad member: {bad_member}",
                })
        except (OSError, zipfile.BadZipFile) as exc:
            summary_rows.append({"archive": archive.name, "zip_integrity": f"ERROR: {exc}"})

    duplicate_rows: list[dict[str, object]] = []
    for (crc, size), members in fingerprints.items():
        if len(members) < 2 or size == 0:
            continue
        archives = {archive for archive, _ in members}
        duplicate_rows.append({
            "crc32": f"{crc:08x}",
            "size_bytes": size,
            "copy_count": len(members),
            "archive_count": len(archives),
            "locations": " | ".join(f"{a}::{m}" for a, m in members),
        })

    write_csv(args.output_directory / "archive_files.csv",
              ["archive", "member_path", "size_bytes", "compressed_bytes", "crc32", "extension", "material_type", "encrypted", "symlink", "unsafe_path"],
              member_rows)
    write_csv(args.output_directory / "archive_summary.csv",
              ["archive", "archive_size_bytes", "file_count", "uncompressed_bytes", "material_types", "top_extensions", "top_level_entries", "encrypted_files", "symlinks", "unsafe_paths", "zip_integrity"],
              summary_rows)
    write_csv(args.output_directory / "duplicate_files.csv",
              ["crc32", "size_bytes", "copy_count", "archive_count", "locations"],
              sorted(duplicate_rows, key=lambda r: (-int(r["copy_count"]), -int(r["size_bytes"]))))


if __name__ == "__main__":
    main()
