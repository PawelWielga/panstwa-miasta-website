#!/usr/bin/env python3
"""Minimal, dependency-free checks for the static GitHub Pages site."""

from __future__ import annotations

import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
INDEX = ROOT / "index.html"

REQUIRED_FILES = (
    "index.html",
    "styles.css",
    "script.js",
    "CNAME",
    "robots.txt",
    "sitemap.xml",
    "privacy-policy/index.html",
    "assets/logo-mark.svg",
    "assets/favicon.svg",
    "assets/og-image.svg",
)

REQUIRED_META_NAMES = {"description", "viewport", "twitter:card"}
REQUIRED_META_PROPERTIES = {
    "og:title",
    "og:description",
    "og:url",
    "og:image",
}


class SiteParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.ids: set[str] = set()
        self.duplicate_ids: set[str] = set()
        self.links: list[str] = []
        self.meta_names: set[str] = set()
        self.meta_properties: set[str] = set()
        self.canonical: str | None = None
        self.has_meta_refresh = False
        self.html_lang: str | None = None
        self.h1_count = 0

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = dict(attrs)
        element_id = values.get("id")
        if element_id:
            if element_id in self.ids:
                self.duplicate_ids.add(element_id)
            self.ids.add(element_id)

        if tag == "html":
            self.html_lang = values.get("lang")
        elif tag == "h1":
            self.h1_count += 1
        elif tag == "a" and values.get("href"):
            self.links.append(values["href"] or "")
        elif tag in {"img", "script", "link"}:
            ref = values.get("src") or values.get("href")
            if ref:
                self.links.append(ref)

        if tag == "meta":
            name = values.get("name")
            prop = values.get("property")
            equiv = (values.get("http-equiv") or "").lower()
            if name:
                self.meta_names.add(name)
            if prop:
                self.meta_properties.add(prop)
            if equiv == "refresh":
                self.has_meta_refresh = True

        if tag == "link" and values.get("rel") == "canonical":
            self.canonical = values.get("href")


def resolve_local_path(reference: str) -> Path | None:
    parsed = urlparse(reference)
    if parsed.scheme or parsed.netloc or reference.startswith(("mailto:", "tel:")):
        return None

    path = parsed.path
    if not path or path == "/":
        return INDEX

    if path.startswith("/"):
        path = path[1:]

    target = ROOT / path
    if path.endswith("/"):
        target /= "index.html"
    return target


def fail(message: str, errors: list[str]) -> None:
    errors.append(message)


def main() -> int:
    errors: list[str] = []

    for relative in REQUIRED_FILES:
        if not (ROOT / relative).is_file():
            fail(f"Missing required file: {relative}", errors)

    if not INDEX.is_file():
        for error in errors:
            print(f"ERROR: {error}")
        return 1

    html = INDEX.read_text(encoding="utf-8")
    parser = SiteParser()
    parser.feed(html)

    if parser.html_lang != "pl":
        fail("The document language must be lang=\"pl\".", errors)
    if parser.h1_count != 1:
        fail(f"Expected exactly one H1, found {parser.h1_count}.", errors)
    if parser.duplicate_ids:
        fail(f"Duplicate IDs: {sorted(parser.duplicate_ids)}", errors)
    if parser.has_meta_refresh:
        fail("The home page must not redirect with meta refresh.", errors)
    if parser.canonical != "https://panstwamiasta.dihor.pl/":
        fail(f"Unexpected canonical URL: {parser.canonical!r}", errors)

    missing_meta_names = REQUIRED_META_NAMES - parser.meta_names
    missing_meta_properties = REQUIRED_META_PROPERTIES - parser.meta_properties
    if missing_meta_names:
        fail(f"Missing meta names: {sorted(missing_meta_names)}", errors)
    if missing_meta_properties:
        fail(f"Missing Open Graph properties: {sorted(missing_meta_properties)}", errors)

    for reference in parser.links:
        if reference.startswith("#"):
            fragment = reference[1:]
            if fragment and fragment not in parser.ids:
                fail(f"Broken fragment link: {reference}", errors)
            continue

        target = resolve_local_path(reference)
        if target is not None and not target.exists():
            fail(f"Broken local reference: {reference} -> {target.relative_to(ROOT)}", errors)

    cname = (ROOT / "CNAME").read_text(encoding="utf-8").strip() if (ROOT / "CNAME").exists() else ""
    if cname != "panstwamiasta.dihor.pl":
        fail(f"Unexpected CNAME value: {cname!r}", errors)

    if "play.google.com" in html:
        fail("Google Play must not be linked before a real store URL is available.", errors)
    if 'href="https://play.panstwamiasta.dihor.pl' in html:
        fail("The planned browser client must not be exposed as an active link.", errors)

    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1

    print(f"Validated {len(REQUIRED_FILES)} required files, {len(parser.ids)} IDs and {len(parser.links)} references.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
