#!/usr/bin/env python3
"""
Simple PDF Merger
-----------------
Give it a folder, it merges every PDF inside into one file called
merged_output.pdf (saved in that same folder).

Usage:
    python3 merge_pdfs.py /path/to/folder
    python3 merge_pdfs.py            <- it will ask you for the folder

Requires: pip install pypdf
"""

import os
import re
import sys

try:
    from pypdf import PdfWriter
except ImportError:
    sys.exit("pypdf is not installed. Run:  pip install pypdf")

OUTPUT_NAME = "merged_output.pdf"


def natural_key(name):
    """Sort names the way humans expect: 2.pdf before 10.pdf."""
    parts = re.split(r"(\d+)", name.lower())
    return [int(p) if p.isdigit() else p for p in parts]


def find_pdfs(folder):
    files = [
        f for f in os.listdir(folder)
        if f.lower().endswith(".pdf")
        and f.lower() != OUTPUT_NAME.lower()
        and os.path.isfile(os.path.join(folder, f))
    ]
    return sorted(files, key=natural_key)


def merge(folder):
    folder = os.path.abspath(os.path.expanduser(folder.strip().strip('"').strip("'")))

    if not os.path.isdir(folder):
        sys.exit(f"Not a folder: {folder}")

    pdfs = find_pdfs(folder)
    if not pdfs:
        sys.exit(f"No PDF files found in: {folder}")

    print(f"Folder: {folder}")
    print(f"Found {len(pdfs)} PDF file(s). Merging in this order:\n")

    writer = PdfWriter()
    merged_count = 0

    for i, name in enumerate(pdfs, start=1):
        path = os.path.join(folder, name)
        try:
            writer.append(path)
            print(f"  {i:>3}. {name}")
            merged_count += 1
        except Exception as e:
            print(f"  {i:>3}. {name}  -- SKIPPED ({e})")

    if merged_count == 0:
        sys.exit("\nNothing could be merged.")

    output_path = os.path.join(folder, OUTPUT_NAME)
    with open(output_path, "wb") as f:
        writer.write(f)
    writer.close()

    print(f"\nDone! {merged_count} file(s) merged into:\n{output_path}")


def main():
    if len(sys.argv) > 1:
        folder = " ".join(sys.argv[1:])
    else:
        folder = input("Enter the folder path containing your PDF files: ")
    merge(folder)


if __name__ == "__main__":
    main()
