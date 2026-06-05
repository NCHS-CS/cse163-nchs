#!/usr/bin/env python3
"""Migrate selected IDP pages from Jekyll markdown to MyST markdown."""

from __future__ import annotations

import argparse
import re
import shutil
from pathlib import Path
from urllib.parse import unquote

FILES = [
    "idp/machine-learning/index.md",
    "idp/machine-learning/feature-importance.md",
    "idp/machine-learning/assessing-accuracy.md",
    "idp/machine-learning/classification.md",
    "idp/machine-learning/regression-distance.md",
    "idp/machine-learning/classification-fully-random.md",
    "idp/machine-learning/when-to-avoid.md",
    "idp/visualizations/index.md",
    "idp/visualizations/activity.md",
    "idp/visualizations/barchart.md",
    "idp/visualizations/case_study_dist.md",
    "idp/visualizations/curve_of_best_fit.md",
    "idp/visualizations/geospatial.md",
    "idp/visualizations/lineplots.md",
    "idp/resources/README.md",
    "idp/resources/method_args.md",
    "idp/resources/collections.md",
    "idp/resources/flake8.md",
    "idp/resources/pandas_api.md",
    "idp/resources/pandas_df.md",
    "idp/resources/writing_comments.md",
    "idp/resources/f-strings.md",
]

ATTR_TO_DIRECTIVE = {
    "note-title": "note",
    "note": "note",
    "notice": "note",
    "important": "important",
}

TOC_MARKER_START = "# BEGIN IDP MIGRATION SECTIONS"
TOC_MARKER_END = "# END IDP MIGRATION SECTIONS"

TOC_BLOCK = (
    "    # BEGIN IDP MIGRATION SECTIONS\n"
    "    - title: Machine Learning\n"
    "      file: idp/machine-learning/index.md\n"
    "      children:\n"
    "        - title: Feature Importance\n"
    "          file: idp/machine-learning/feature-importance.md\n"
    "        - title: Assessing Accuracy\n"
    "          file: idp/machine-learning/assessing-accuracy.md\n"
    "        - title: Classification\n"
    "          file: idp/machine-learning/classification.md\n"
    "        - title: Regression - Distance Study\n"
    "          file: idp/machine-learning/regression-distance.md\n"
    "        - title: Classification - Fully Random\n"
    "          file: idp/machine-learning/classification-fully-random.md\n"
    "        - title: When to Avoid Using Machine Learning\n"
    "          file: idp/machine-learning/when-to-avoid.md\n"
    "    - title: Visualizations\n"
    "      file: idp/visualizations/index.md\n"
    "      children:\n"
    "        - title: Activity\n"
    "          file: idp/visualizations/activity.md\n"
    "        - title: Bar Charts\n"
    "          file: idp/visualizations/barchart.md\n"
    "        - title: Case Study on Distance\n"
    "          file: idp/visualizations/case_study_dist.md\n"
    "        - title: Curve of Best Fit\n"
    "          file: idp/visualizations/curve_of_best_fit.md\n"
    "        - title: Geospatial Plots\n"
    "          file: idp/visualizations/geospatial.md\n"
    "        - title: Line Plots\n"
    "          file: idp/visualizations/lineplots.md\n"
    "    - title: Other Resources\n"
    "      file: idp/resources/README.md\n"
    "      children:\n"
    "        - title: Arguments\n"
    "          file: idp/resources/method_args.md\n"
    "        - title: Collections\n"
    "          file: idp/resources/collections.md\n"
    "        - title: Flake8\n"
    "          file: idp/resources/flake8.md\n"
    "        - title: Pandas API\n"
    "          file: idp/resources/pandas_api.md\n"
    "        - title: Pandas DF\n"
    "          file: idp/resources/pandas_df.md\n"
    "        - title: Writing Comments\n"
    "          file: idp/resources/writing_comments.md\n"
    "        - title: f-strings\n"
    "          file: idp/resources/f-strings.md\n"
    "    # END IDP MIGRATION SECTIONS\n"
)

LEGACY_VISUAL_PREFIX = "idp/static/visualizations tab/case study on distance/"
NORMALIZED_VISUAL_PREFIX = "idp/static/visualizations-tab/case-study-on-distance/"


def split_front_matter(text: str) -> tuple[dict[str, str], str]:
    match = re.match(r"\A---\s*\n(.*?)\n---\s*\n?", text, flags=re.DOTALL)
    if not match:
        return {}, text

    raw = match.group(1)
    body = text[match.end() :]
    front_matter: dict[str, str] = {}
    for line in raw.splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        front_matter[key.strip()] = value.strip()
    return front_matter, body


def convert_tabs(body: str) -> str:
    out: list[str] = []
    lines = body.split("\n")

    for line in lines:
        stripped = line.strip()

        match_tabs = re.fullmatch(r"\{%\s*tabs\s+([^\s%]+)\s*%\}", stripped)
        if match_tabs:
            out.append("::::{tab-set}")
            continue

        match_tab = re.fullmatch(r"\{%\s*tab\s+([^\s%]+)\s+(.+?)\s*%\}", stripped)
        if match_tab:
            label = match_tab.group(2)
            out.append(f":::{{tab-item}} {label}")
            continue

        if re.fullmatch(r"\{%\s*endtab\s*%\}", stripped):
            out.append(":::")
            continue

        if re.fullmatch(r"\{%\s*endtabs\s*%\}", stripped):
            out.append("::::")
            continue

        out.append(line)

    return "\n".join(out)


def convert_include_toc(body: str) -> str:
    return re.sub(
        r"^\{%\s*include\s+toc\.md\s*%\}\s*$",
        ":::{contents}\n:::",
        body,
        flags=re.MULTILINE,
    )


def strip_quote_prefix(line: str) -> str:
    if line.startswith("> "):
        return line[2:]
    if line.startswith(">"):
        return line[1:]
    return line


def collect_paragraph(lines: list[str], start: int) -> tuple[list[str], int]:
    collected: list[str] = []
    i = start
    while i < len(lines):
        line = lines[i]
        if line == "":
            break
        collected.append(line)
        i += 1
    return collected, i


def convert_attribute_callouts(body: str) -> str:
    lines = body.split("\n")
    out: list[str] = []
    i = 0

    while i < len(lines):
        line = lines[i]
        attr_match = re.fullmatch(r"\{:\s*\.([A-Za-z0-9_-]+)\s*\}", line.strip())
        if not attr_match:
            out.append(line)
            i += 1
            continue

        cls = attr_match.group(1)
        directive = ATTR_TO_DIRECTIVE.get(cls)
        if directive is None:
            out.append(line)
            i += 1
            continue

        i += 1

        if i < len(lines) and lines[i].startswith(">"):
            quote_lines: list[str] = []
            while i < len(lines) and lines[i].startswith(">"):
                quote_lines.append(strip_quote_prefix(lines[i]))
                i += 1

            non_empty_idx = next((idx for idx, item in enumerate(quote_lines) if item.strip()), None)
            title = ""
            content_lines = quote_lines

            if non_empty_idx is not None:
                title = quote_lines[non_empty_idx].strip()
                content_lines = quote_lines[non_empty_idx + 1 :]

            if title:
                out.append(f":::{{{directive}}} {title}")
            else:
                out.append(f":::{{{directive}}}")

            out.extend(content_lines)
            out.append(":::")
            continue

        paragraph, new_idx = collect_paragraph(lines, i)
        if paragraph:
            out.append(f":::{{{directive}}}")
            out.extend(paragraph)
            out.append(":::")
            i = new_idx
            continue

        out.append(line)

    return "\n".join(out)


def rewrite_links(body: str) -> str:
    def _replace(match: re.Match[str]) -> str:
        url = match.group(1)
        new_url = url

        if url == "curve_of_best_fit":
            new_url = "./curve_of_best_fit"
        elif not re.match(r"^(https?://|mailto:|#)", url):
            new_url = unquote(new_url)
            new_url = new_url.replace(
                "../static/visualizations tab/case study on distance/",
                "../static/visualizations-tab/case-study-on-distance/",
            )
            new_url = re.sub(r"\.html(?=($|#|\?))", "", new_url)

        return f"]({new_url})"

    return re.sub(r"\]\(([^)]+)\)", _replace, body)


def separate_block_images(body: str) -> str:
    lines = body.split("\n")
    out: list[str] = []

    standalone_image = re.compile(r"!\[[^\]]*\]\([^)]+\)\s*$")

    for line in lines:
        stripped = line.strip()
        if stripped.startswith("![") and standalone_image.fullmatch(stripped):
            prev = out[-1] if out else ""
            prev_stripped = prev.strip()
            if (
                prev_stripped
                and not prev_stripped.startswith((":::", "```", "|", "-", "*", "+", ">", ":"))
                and not re.match(r"^\d+\.\s", prev_stripped)
            ):
                out.append("")
        out.append(line)

    return "\n".join(out)


def transform_markdown(text: str) -> str:
    front_matter, body = split_front_matter(text)

    body = convert_include_toc(body)
    body = convert_tabs(body)
    body = convert_attribute_callouts(body)
    body = rewrite_links(body)
    body = separate_block_images(body)

    title = front_matter.get("title", "")
    if title:
        transformed = f"---\ntitle: {title}\n---\n\n{body}"
    else:
        transformed = body

    if not transformed.endswith("\n"):
        transformed += "\n"
    return transformed


def extract_static_assets(source_text: str, source_file: Path, old_root: Path) -> set[Path]:
    assets: set[Path] = set()
    for target in re.findall(r"\]\(([^)]+)\)", source_text):
        if not target.startswith("../static/"):
            continue
        decoded = unquote(target)
        abs_path = (source_file.parent / decoded).resolve()
        try:
            rel = abs_path.relative_to(old_root)
        except ValueError:
            continue
        assets.add(rel)
    return assets


def destination_asset_variants(rel_asset: Path) -> list[Path]:
    rel_text = rel_asset.as_posix()
    variants = [rel_asset]
    if rel_text.startswith(LEGACY_VISUAL_PREFIX):
        variants.append(Path(rel_text.replace(LEGACY_VISUAL_PREFIX, NORMALIZED_VISUAL_PREFIX, 1)))
    return variants


def update_myst_toc(myst_path: Path) -> None:
    text = myst_path.read_text(encoding="utf-8")

    if TOC_MARKER_START in text and TOC_MARKER_END in text:
        text = re.sub(
            rf"\n?[ \t]*{re.escape(TOC_MARKER_START)}.*?[ \t]*{re.escape(TOC_MARKER_END)}\n?",
            "\n",
            text,
            flags=re.DOTALL,
        )

    needle = "    - title: Extras"
    if needle not in text:
        raise RuntimeError("Could not locate 'Extras' section in myst.yml")

    replacement = TOC_BLOCK + "\n" + needle
    text = text.replace(needle, replacement, 1)
    text = re.sub(r"\n{3,}(?=    # BEGIN IDP MIGRATION SECTIONS)", "\n\n", text)
    myst_path.write_text(text, encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--old-root", required=True, type=Path)
    parser.add_argument("--new-root", required=True, type=Path)
    args = parser.parse_args()

    old_root = args.old_root.resolve()
    new_root = args.new_root.resolve()

    copied_assets: set[Path] = set()

    for rel in FILES:
        old_file = old_root / rel
        new_file = new_root / rel

        source_text = old_file.read_text(encoding="utf-8")
        transformed = transform_markdown(source_text)

        new_file.parent.mkdir(parents=True, exist_ok=True)
        new_file.write_text(transformed, encoding="utf-8")

        copied_assets |= extract_static_assets(source_text, old_file, old_root)

    for rel_asset in sorted(copied_assets):
        src = old_root / rel_asset
        for rel_dst in destination_asset_variants(rel_asset):
            dst = new_root / rel_dst
            dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(src, dst)

    update_myst_toc(new_root / "myst.yml")

    print(f"Migrated pages: {len(FILES)}")
    print(f"Copied assets: {len(copied_assets)}")


if __name__ == "__main__":
    main()
