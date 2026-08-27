#!/usr/bin/env python3
"""Minimal, dependency-free checks for the static GitHub Pages site."""

from __future__ import annotations

import json
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
INDEX = ROOT / "index.html"
PRIVACY = ROOT / "privacy-policy" / "index.html"

REQUIRED_FILES = (
    "index.html",
    "styles.css",
    "design-tokens.css",
    "design-system.json",
    "script.js",
    "robots.txt",
    "sitemap.xml",
    "privacy-policy/index.html",
    "assets/logo-mark.svg",
    "assets/favicon.svg",
    "assets/og-image.svg",
    "assets/screenshots/screens-1.webp",
    "assets/screenshots/screens-2.webp",
    "assets/screenshots/screens-3.webp",
    "assets/screenshots/screens-4.webp",
)

REQUIRED_META_NAMES = {"description", "viewport", "twitter:card"}
REQUIRED_META_PROPERTIES = {
    "og:title",
    "og:description",
    "og:url",
    "og:image",
}
PRODUCTION_WEB_CLIENT_URL = "https://pawelwielga.github.io/panstwa-miasta-play/"
OBSOLETE_WEB_CLIENT_HOST = "play.panstwamiasta.dihor.pl"


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
    privacy_html = PRIVACY.read_text(encoding="utf-8") if PRIVACY.is_file() else ""
    script = (ROOT / "script.js").read_text(encoding="utf-8")
    tokens = (ROOT / "design-tokens.css").read_text(encoding="utf-8")
    design_system = json.loads((ROOT / "design-system.json").read_text(encoding="utf-8"))
    parser = SiteParser()
    parser.feed(html)

    if parser.html_lang != "pl":
        fail('The document language must be lang="pl".', errors)
    if parser.h1_count != 1:
        fail(f"Expected exactly one H1, found {parser.h1_count}.", errors)
    if parser.duplicate_ids:
        fail(f"Duplicate IDs: {sorted(parser.duplicate_ids)}", errors)
    if parser.has_meta_refresh:
        fail("The home page must not redirect with meta refresh.", errors)
    if parser.canonical != "https://pawelwielga.github.io/panstwa-miasta-website/":
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

    if "design-tokens.css" not in script:
        fail("script.js must load the pinned design token stylesheet.", errors)
    if design_system.get("localCopy") != "design-tokens.css":
        fail("design-system.json must identify design-tokens.css as the local copy.", errors)
    if f"@{design_system.get('version')}" not in script:
        fail("The script design-system marker must match design-system.json.", errors)

    design_commit = design_system.get("commit")
    if not isinstance(design_commit, str) or len(design_commit) != 40:
        fail("design-system.json must pin a full 40-character commit SHA.", errors)
    elif design_commit not in tokens:
        fail("design-tokens.css must identify the pinned design-system commit.", errors)

    for variable in (
        "--pm-color-primary",
        "--pm-color-background",
        "--pm-color-text-primary",
        "--pm-radius-standard",
    ):
        if variable not in tokens:
            fail(f"Missing shared token in design-tokens.css: {variable}", errors)

    if "Schematyczne makiety" in html:
        fail("The landing page still labels game views as schematic mockups.", errors)
    if "Aktualne zrzuty ekranu" not in html:
        fail("The landing page must identify the current Android screenshots.", errors)
    for screenshot_class in range(8):
        if f"game-screenshot--{screenshot_class}" not in html:
            fail(f"Missing current game screenshot slot: {screenshot_class}", errors)

    if "play.google.com" in html:
        fail("Google Play must not be linked before a real store URL is available.", errors)

    if PRODUCTION_WEB_CLIENT_URL not in html:
        fail("The production browser client URL must be exposed on the landing page.", errors)
    if OBSOLETE_WEB_CLIENT_HOST in html:
        fail("The obsolete browser client host must not be presented on the landing page.", errors)

    for required_privacy_term in ("PeerJS", "WebRTC", "GitHub Pages"):
        if required_privacy_term not in privacy_html:
            fail(
                f"The public privacy policy must describe online multiplayer dependency: {required_privacy_term}",
                errors,
            )

    if "1 lipca 2026" in privacy_html:
        fail("The public privacy policy still contains the pre-online update date.", errors)

    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1

    print(
        f"Validated {len(REQUIRED_FILES)} required files, "
        f"{len(parser.ids)} IDs and {len(parser.links)} references."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
