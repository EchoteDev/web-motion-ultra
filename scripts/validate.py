#!/usr/bin/env python3
"""Validate skill packaging and local documentation links; no browser claims."""

from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit
import xml.etree.ElementTree as ET

import yaml


def validate(root: Path) -> list[str]:
    errors = []
    entries = sorted((root / "skills").glob("*/SKILL.md"))
    if not entries:
        errors.append("No skills/*/SKILL.md entry points found")
    for entry in entries:
        relative = entry.relative_to(root)
        text = entry.read_text(encoding="utf-8")
        match = re.match(r"\A---\n(.*?)\n---(?:\n|$)", text, re.S)
        if not match:
            errors.append(f"{relative}: missing YAML frontmatter")
            continue
        try:
            meta = yaml.safe_load(match.group(1))
        except yaml.YAMLError as exc:
            errors.append(f"{relative}: invalid YAML: {exc}")
            continue
        if not isinstance(meta, dict):
            errors.append(f"{relative}: frontmatter must be a mapping")
            continue
        name = meta.get("name")
        if not isinstance(name, str) or not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name) or len(name) > 64:
            errors.append(f"{relative}: invalid skill name")
        elif name != entry.parent.name:
            errors.append(f"{relative}: name must match its folder")
        description = meta.get("description")
        if not isinstance(description, str) or not description.strip() or len(description) > 1024:
            errors.append(f"{relative}: description must contain 1–1024 characters")
        ui_path = entry.parent / "agents/openai.yaml"
        if ui_path.exists():
            try:
                ui = yaml.safe_load(ui_path.read_text(encoding="utf-8"))["interface"]
                if not isinstance(ui, dict):
                    raise ValueError("interface must be a mapping")
                short = ui.get("short_description", "")
                if not isinstance(short, str) or not 25 <= len(short) <= 64:
                    errors.append(f"{ui_path.relative_to(root)}: short_description must have 25–64 characters")
                prompt = ui.get("default_prompt", "")
                if not isinstance(prompt, str) or f"${name}" not in prompt:
                    errors.append(f"{ui_path.relative_to(root)}: default_prompt must invoke the skill")
            except (yaml.YAMLError, KeyError, TypeError, ValueError) as exc:
                errors.append(f"{ui_path.relative_to(root)}: invalid UI metadata: {exc}")

    # Includes Markdown images; external URLs and in-page fragments are excluded.
    for doc in root.rglob("*.md"):
        if any(part.startswith(".") for part in doc.relative_to(root).parts[:-1]):
            continue
        text = doc.read_text(encoding="utf-8")
        for target in re.findall(r"\]\(([^\s)]+)\)", text):
            url = urlsplit(target)
            if url.scheme or url.netloc or not url.path:
                continue
            path = (doc.parent / unquote(url.path)).resolve()
            if not path.is_relative_to(root.resolve()) or not path.exists():
                errors.append(f"{doc.relative_to(root)}: missing or out-of-repository target: {target}")
    for svg in (root / "assets").glob("*.svg"):
        try:
            ET.parse(svg)
        except ET.ParseError as exc:
            errors.append(f"{svg.relative_to(root)}: invalid SVG XML: {exc}")
    return errors


if __name__ == "__main__":
    repo = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else Path(__file__).resolve().parents[1]
    failures = validate(repo)
    for failure in failures:
        print(f"ERROR: {failure}", file=sys.stderr)
    if failures:
        sys.exit(1)
    print("Validated skill metadata, UI invocation, local documentation links, and SVG assets.")
