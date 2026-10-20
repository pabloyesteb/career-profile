#!/usr/bin/env python3
"""Prepare regenerable, page-delimited course evidence without executing source code."""
from __future__ import annotations

import argparse
import csv
import io
import json
from pathlib import Path, PurePosixPath
import re
import subprocess
import tarfile
import zipfile

ROOT = Path(__file__).resolve().parents[2]


def safe_path(name: str) -> PurePosixPath:
    path = PurePosixPath(name)
    if path.is_absolute() or ".." in path.parts:
        raise ValueError(f"Unsafe archive member: {name}")
    return path


def prepare(course_id: str) -> None:
    with (ROOT / "00_sources/inventory/courses.csv").open() as handle:
        row = next(r for r in csv.DictReader(handle) if r["course_id"] == course_id)
    if not row["archive"]:
        raise ValueError("Course has no configured archive")
    archive = ROOT / "00_sources/raw/tum/archives" / row["archive"]
    cache = ROOT / ".cache" / course_id
    records = []

    def process(data: bytes, member: str, source_dir: Path, text_dir: Path,
                provenance: str, depth: int = 0) -> None:
        relative = safe_path(member)
        target = source_dir / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        if not target.exists():
            target.write_bytes(data)
        record = {"member": provenance, "bytes": len(data), "source": str(target.relative_to(ROOT))}
        if data.startswith(b"%PDF"):
            output = text_dir / (str(relative) + ".txt")
            output.parent.mkdir(parents=True, exist_ok=True)
            if not output.exists():
                result = subprocess.run(["pdftotext", "-layout", str(target), str(output)],
                                        capture_output=True, text=True)
                if result.returncode:
                    record["extraction_error"] = result.stderr[:500]
            info = subprocess.run(["pdfinfo", str(target)], capture_output=True, text=True)
            match = re.search(r"Pages:\s+(\d+)", info.stdout)
            if match:
                record["pages"] = int(match[1])
            if output.exists():
                record["text"] = str(output.relative_to(ROOT))
                pages = output.read_text().split("\f")
                if pages and not pages[-1].strip():
                    pages.pop()
                record["text_characters"] = sum(len(p.strip()) for p in pages)
                headings = []
                for number, page in enumerate(pages, 1):
                    lines = [re.sub(r"\s+", " ", x.strip()) for x in page.splitlines() if x.strip()]
                    headings.append(f"{number}: " + " | ".join(lines[:2])[:200])
                output.with_suffix(".pages.txt").write_text("\n".join(headings) + "\n")
        elif target.suffix.lower() in {".ipynb", ".json"}:
            try:
                obj = json.loads(data)
                if isinstance(obj, dict) and "cells" in obj:
                    output = text_dir / (str(relative) + ".cells.txt")
                    output.parent.mkdir(parents=True, exist_ok=True)
                    output.write_text("\n\n".join(
                        f"CELL {i} ({cell.get('cell_type', '?')})\n" + "".join(cell.get("source", []))
                        for i, cell in enumerate(obj["cells"], 1)))
                    record["cells"] = len(obj["cells"])
                    record["text"] = str(output.relative_to(ROOT))
            except (ValueError, TypeError):
                pass
        records.append(record)
        if depth < 2 and target.suffix.lower() in {".zip", ".imscc"} and zipfile.is_zipfile(io.BytesIO(data)):
            with zipfile.ZipFile(io.BytesIO(data)) as nested:
                for entry in nested.infolist():
                    safe_path(entry.filename)
                    if entry.is_dir() or "__MACOSX" in PurePosixPath(entry.filename).parts:
                        continue
                    process(nested.read(entry), entry.filename, cache / "nested" / relative,
                            cache / "nested_text" / relative, provenance + " :: " + entry.filename, depth + 1)
        elif depth < 2 and (str(target).endswith(".tar.gz") or str(target).endswith(".tar.xz")):
            with tarfile.open(fileobj=io.BytesIO(data), mode="r:*") as nested:
                for entry in nested:
                    safe_path(entry.name)
                    if not entry.isfile():
                        continue  # Never materialize links or special files.
                    stream = nested.extractfile(entry)
                    if stream is not None:
                        process(stream.read(), entry.name, cache / "nested" / relative,
                                cache / "nested_text" / relative,
                                provenance + " :: " + entry.name, depth + 1)

    with zipfile.ZipFile(archive) as zf:
        for entry in zf.infolist():
            safe_path(entry.filename)
            if entry.is_dir() or PurePosixPath(entry.filename).suffix.lower() in {".mp4", ".f4v"}:
                continue
            process(zf.read(entry), entry.filename, cache / "source", cache / "text", entry.filename)
    cache.mkdir(parents=True, exist_ok=True)
    (cache / "evidence_manifest.json").write_text(json.dumps(records, indent=2, ensure_ascii=False) + "\n")
    pdfs = [r for r in records if "pages" in r]
    print(f"{course_id}: {len(pdfs)} PDFs, {sum(r['pages'] for r in pdfs)} physical pages")
    for record in pdfs:
        print(f"{record['pages']:4} pages, {record.get('text_characters', 0):7} text chars | {record['member']}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("course_id")
    prepare(parser.parse_args().course_id)
