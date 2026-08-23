#!/usr/bin/env python3
"""Extract book records from a public Google Scholar profile."""

from __future__ import annotations

import argparse
import html
import json
import re
from pathlib import Path
from urllib.request import Request, urlopen


DEFAULT_PROFILE_URL = (
    "https://scholar.google.com/citations?"
    "hl=pt-BR&user=rPn5O48AAAAJ&view_op=list_works"
)
ROW_PATTERN = re.compile(r'<tr class="gsc_a_tr">(?P<row>.*?)</tr>')
TITLE_PATTERN = re.compile(r'class="gsc_a_at">(?P<value>.*?)</a>')
GRAY_PATTERN = re.compile(r'<div class="gs_gray">(?P<value>.*?)</div>')
CITATIONS_PATTERN = re.compile(r'class="gsc_a_ac gs_ibl">(?P<value>.*?)</a>')
YEAR_PATTERN = re.compile(r'gsc_a_h gsc_a_hc gs_ibl">(?P<value>.*?)</span>')
TAG_PATTERN = re.compile(r"<.*?>")


def clean(value: str) -> str:
    """Decode HTML and normalize whitespace from a Scholar field."""
    return " ".join(html.unescape(TAG_PATTERN.sub("", value)).split())


def fetch_profile(url: str) -> str:
    """Return the Scholar profile HTML using a browser-like user agent."""
    request = Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urlopen(request, timeout=30) as response:
        return response.read().decode("utf-8")


def extract_books(profile_html: str) -> list[dict[str, str]]:
    """Extract rows whose title identifies them as a book."""
    books: list[dict[str, str]] = []

    for match in ROW_PATTERN.finditer(profile_html):
        row = match.group("row")
        title_match = TITLE_PATTERN.search(row)
        if title_match is None:
            continue

        title = clean(title_match.group("value"))
        if "livro" not in title.casefold():
            continue

        gray_fields = GRAY_PATTERN.findall(row)
        authors = clean(gray_fields[0]) if gray_fields else ""
        publication = clean(gray_fields[1]) if len(gray_fields) > 1 else ""
        citations_match = CITATIONS_PATTERN.search(row)
        year_match = YEAR_PATTERN.search(row)
        books.append(
            {
                "title": title,
                "authors": authors,
                "publication": publication,
                "citations": clean(citations_match.group("value"))
                if citations_match
                else "",
                "year": clean(year_match.group("value")) if year_match else "",
            }
        )

    return books


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Extract book records from a public Google Scholar profile."
    )
    parser.add_argument("--url", default=DEFAULT_PROFILE_URL, help="Scholar profile URL")
    parser.add_argument(
        "--output",
        type=Path,
        help="Optional JSON output file; otherwise writes JSON to standard output.",
    )
    args = parser.parse_args()

    books = extract_books(fetch_profile(args.url))
    result = json.dumps(books, ensure_ascii=False, indent=2) + "\n"

    if args.output:
        args.output.write_text(result, encoding="utf-8")
    else:
        print(result, end="")


if __name__ == "__main__":
    main()
