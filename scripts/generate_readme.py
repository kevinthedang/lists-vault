#!/usr/bin/env python3
import os
import re
import yaml
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
README_PATH = ROOT / "README.md"

# Update when adding a new section to the lists-vault repository
SECTIONS = ["services", "tools", "hardware"]

HEADER = """<div align="center">
  <h1>Lists of Information</h1>
</div>

### List Directory

"""

def extract_metadata(md_path):
    """Extract YAML front-matter metadata from a markdown file."""
    with open(md_path, "r", encoding="utf-8") as f:
        content = f.read()

    pattern = r"^---\s*\n(.*?)\n---\s*\n"
    match = re.search(pattern, content, re.DOTALL)

    if not match:
        return {}

    try:
        return yaml.safe_load(match.group(1)) or {}
    except Exception:
        return {}

def build_section(section):
    section_path = ROOT / section
    if not section_path.exists():
        return ""

    md = f"#### {section.capitalize()}\n"
    entries = []
    
    # Only scan markdown files directly in the section folder
    for md_file in section_path.glob("*.md"):
        metadata = extract_metadata(md_file)

        title = metadata.get(
            "title",
            md_file.stem.replace("-", " ").title()
        )
        description = metadata.get("description", "")

        entries.append({
            "title": title,
            "description": description,
            "path": md_file.relative_to(ROOT)
        })

    # Sort alphabetically
    entries.sort(key=lambda x: x["title"].lower())

    # Add in
    for item in entries:
        line = f"* [{item['title']}]({item['path']})"
        if item["description"]:
            line += f" — {item['description']}"
        md += line + "\n"

    md += "\n"
    return md

def generate_readme():
    output = HEADER

    for section in SECTIONS:
        output += build_section(section)

    with open(README_PATH, "w", encoding="utf-8") as f:
        f.write(output)

    print("README.md updated successfully.")

if __name__ == "__main__":
    generate_readme()