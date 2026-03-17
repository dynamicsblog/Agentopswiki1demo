#!/usr/bin/env python3
"""Simple local Markdown link checker for this repository."""

from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
MARKDOWN_FILES = list(ROOT.glob("*.md"))
LINK_RE = re.compile(r"\[[^\]]+\]\(([^)]+)\)")

errors: list[tuple[Path, str]] = []

for file_path in MARKDOWN_FILES:
    content = file_path.read_text(encoding="utf-8")
    for match in LINK_RE.finditer(content):
        href = match.group(1).strip()
        if href.startswith(("http://", "https://", "#", "mailto:")):
            continue

        target = href.split("#", 1)[0]
        resolved = (file_path.parent / target)
        if resolved.suffix == "":
            resolved = resolved.with_suffix(".md")

        if not resolved.exists():
            errors.append((file_path.relative_to(ROOT), href))

if errors:
    print("Broken local links found:")
    for source, href in errors:
        print(f"- {source}: {href}")
    sys.exit(1)

print(f"OK: checked {len(MARKDOWN_FILES)} markdown files; no broken local links.")
