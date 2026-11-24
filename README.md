<h2><a href="https://knowledgeless.github.io/PDF_Merger/">Use Online PDF Merger </a></h2>

Merge as many PDFs as you want into one `merged_output.pdf` — in your browser,
or from the command line. No server, no sign-up, nothing uploaded anywhere.

## Two ways to use it

| | What it is | Needs |
|---|---|---|
| **[index.html](index.html)** | A web page — drag & drop your PDFs, click merge, the file downloads | Just a browser |
| **merge_pdfs.py** | Command line — point it at a folder | Python + pypdf |

---

# 1. Web version (no install)

Open [index.html](index.html) in any browser — double-click it, or host it on GitHub Pages
(*Settings → Pages → Branch: main → /root*) and share the link.

- Drag and drop PDFs onto the box, or click to pick several files.
- Reorder with the ↑ ↓ buttons, remove with ×.
- Hit **Merge & Download** — you get `merged_output.pdf`.

Your files never leave your computer. There is no server, no upload and no
account: the merging happens inside the browser tab.

---

# 2. Command line version

Merges every PDF in a folder — you give it the folder path, nothing else.
Works on Windows, macOS and Linux (Python 3.7+).

## Install

```bash
pip install pypdf
```

or

```bash
pip install -r requirements.txt
```

## Use

```bash
python3 merge_pdfs.py /path/to/your/folder
```

Windows:

```bash
python merge_pdfs.py "C:\Users\You\Documents\My PDFs"
```

Or just run it with no arguments and it will ask for the folder:

```bash
python3 merge_pdfs.py
```

## What it does

- Picks up every `.pdf` file in the folder (not sub-folders).
- Merges them **in order**, sorted by name the way a human would expect
  (`1.pdf`, `2.pdf`, `10.pdf` — not `1, 10, 2`).
- Prints the exact order before saving, so you can check it.
- Saves the result as `merged_output.pdf` inside the same folder.
- Skips files that are damaged or not real PDFs instead of crashing.
- Ignores an existing `merged_output.pdf`, so re-running is safe.

## Controlling the order

The order is alphabetical/numeric by filename. To force a specific order,
prefix your files with numbers:

```
01-cover.pdf
02-intro.pdf
03-chapter1.pdf
```
