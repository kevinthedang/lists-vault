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

def scan_nested(section_path):
    """Recursively scan folders and return a nested structure."""
    tree = {}

    for root, dirs, files in os.walk(section_path):
        rel_root = Path(root).relative_to(section_path)
        current = tree

        # Walk down the tree to the correct nested dict
        for part in rel_root.parts:
            current = current.setdefault(part, {})

        # Add markdown files
        md_files = [f for f in files if f.endswith(".md")]
        entries = []

        for file in md_files:
            full_path = Path(root) / file
            metadata = extract_metadata(full_path)

            title = metadata.get("title", file.replace(".md", "").replace("-", " ").title())
            description = metadata.get("description", "")

            entries.append({
                "title": title,
                "description": description,
                "path": full_path.relative_to(ROOT)
            })

        # Alphabetical sort by title
        entries.sort(key=lambda x: x["title"].lower())

        current["_files"] = entries

    return tree

def render_tree(tree, indent=0):
    """Render nested folder structure into Markdown."""
    md = ""
    prefix = "  " * indent

    # Render files first (alphabetical)
    for item in tree.get("_files", []):
        line = f"{prefix}* [{item['title']}]({item['path']})"
        if item["description"]:
            line += f" — {item['description']}"
        md += line + "\n"

    # Render subfolders (alphabetical)
    subfolders = sorted(
        (k for k in tree.keys() if k != "_files"),
        key=lambda x: x.lower()
    )

    for key in subfolders:
        md += f"{prefix}* {key.replace('-', ' ').title()}\n"
        md += render_tree(tree[key], indent + 1)

    return md

def build_section(section):
    section_path = ROOT / section
    if not section_path.exists():
        return ""

    tree = scan_nested(section_path)
    md = f"#### {section.capitalize()}\n"
    md += render_tree(tree)
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
