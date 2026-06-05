#!/usr/bin/env python3
"""Validate IDP migration fidelity and basic link/asset integrity."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from urllib.parse import unquote

from migrate_idp_content import FILES, transform_markdown


def extract_links(text: str) -> list[str]:
    no_comments = re.sub(r"<!--.*?-->", "", text, flags=re.DOTALL)
    return re.findall(r"\]\(([^)]+)\)", no_comments)


def link_exists(base_file: Path, link: str) -> bool:
    target = unquote(link).split("#", 1)[0].split("?", 1)[0]
    if not target:
        return True

    resolved = (base_file.parent / target).resolve()
    candidates = [resolved]

    if not resolved.suffix:
        candidates.append(resolved.with_suffix(".md"))
        candidates.append((resolved / "index.md").resolve())

    return any(path.exists() for path in candidates)


def check_page(old_root: Path, new_root: Path, rel: str) -> list[str]:
    errors: list[str] = []
    old_file = old_root / rel
    new_file = new_root / rel

    if not new_file.exists():
        return [f"Missing migrated file: {rel}"]

    old_text = old_file.read_text(encoding="utf-8")
    new_text = new_file.read_text(encoding="utf-8")
    expected = transform_markdown(old_text)

    if new_text != expected:
        errors.append(f"Fidelity mismatch: {rel}")

    if re.search(r"\{%\s*(tabs|tab|endtab|endtabs|include)\b", new_text):
        errors.append(f"Residual Jekyll tag found: {rel}")

    for link in extract_links(new_text):
        if re.match(r"^(https?://|mailto:|#)", link):
            continue

        if ".html" in link:
            errors.append(f"Relative .html link remains in {rel}: {link}")

        if link.startswith("../") or link.startswith("./"):
            if not link_exists(new_file, link):
                errors.append(f"Broken local link in {rel}: {link}")

    return errors


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--old-root", required=True, type=Path)
    parser.add_argument("--new-root", required=True, type=Path)
    args = parser.parse_args()

    old_root = args.old_root.resolve()
    new_root = args.new_root.resolve()

    all_errors: list[str] = []
    for rel in FILES:
        all_errors.extend(check_page(old_root, new_root, rel))

    if all_errors:
        print("Validation failed:")
        for err in all_errors:
            print(f"- {err}")
        sys.exit(1)

    print(f"Validation passed for {len(FILES)} pages")


if __name__ == "__main__":
    main()
