"""Check that every old URL in docs/url-inventory.txt is served by site/.

Mimics GitHub Pages resolution: /x -> x, x.html, x/index.html.
URLs with a query string are checked against site/redirects.json (if present),
since Pages ignores query strings.
Exit code 1 if any URL is not covered.
"""

import json
import sys
import urllib.parse
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SITE = ROOT / "site"
INVENTORY = ROOT / "docs" / "url-inventory.txt"
REDIRECTS = SITE / "redirects.json"


def served(path: str) -> bool:
    rel = urllib.parse.unquote(path).lstrip("/")
    base = SITE / rel
    if path.endswith("/"):
        return (base / "index.html").is_file()
    return (
        base.is_file()
        or base.with_name(base.name + ".html").is_file()
        or (base / "index.html").is_file()
    )


def main() -> int:
    if not INVENTORY.exists():
        print("no docs/url-inventory.txt yet, skipping")
        return 0
    redirects = (
        json.loads(REDIRECTS.read_text(encoding="utf-8")) if REDIRECTS.exists() else {}
    )
    missing = []
    for line in INVENTORY.read_text(encoding="utf-8").splitlines():
        url = line.strip()
        if not url or url.startswith("#"):
            continue
        if url in redirects:
            continue
        if "?" in url or not served(url):
            missing.append(url)
    for url in missing:
        print(f"MISSING {url}")
    print(f"{len(missing)} uncovered URL(s)")
    return 1 if missing else 0


if __name__ == "__main__":
    sys.exit(main())
