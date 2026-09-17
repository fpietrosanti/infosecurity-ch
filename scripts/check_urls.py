"""Check that every historical URL in docs/url-inventory.txt is served by site/.

Mimics GitHub Pages resolution: /x/ -> x/index.html, /x -> x | x.html | x/ (301).
Shortlinks (/?p=N) must be present in site/redirects.json (handled by JS on the home page).
Old asset URLs (/wp-content, /wp-includes) whose query string was folded into the
file name by the downloader (foo_ver-1.2.css) are reported as warnings only.
Exit code 1 if any content URL is not covered.
"""

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SITE = ROOT / "site"
INVENTORY = ROOT / "docs" / "url-inventory.txt"


def served(path: str) -> bool:
    rel = path.lstrip("/")
    base = SITE / rel
    if path.endswith("/"):
        return (base / "index.html").is_file()
    return base.is_file() or base.with_name(base.name + ".html").is_file() or (base / "index.html").is_file()


def asset_variant(path: str) -> bool:
    base = SITE / path.lstrip("/")
    stem, dot, ext = base.name.rpartition(".")
    if not dot or not base.parent.is_dir():
        return False
    return any(p.name.startswith(stem + "_ver-") and p.name.endswith("." + ext) for p in base.parent.iterdir())


def main() -> int:
    if not INVENTORY.exists():
        print("no docs/url-inventory.txt yet, skipping")
        return 0
    redirects = json.loads((SITE / "redirects.json").read_text(encoding="utf-8"))
    missing, warnings, total = [], [], 0
    for line in INVENTORY.read_text(encoding="utf-8").splitlines():
        url = line.strip()
        if not url or url.startswith("#"):
            continue
        total += 1
        if url in redirects or served(url):
            continue
        if url.startswith("/outgoing/"):  # 404.html redirects any outbound-tracking path to its host
            continue
        if url.startswith(("/wp-content/", "/wp-includes/", "/avatar/")):
            if not asset_variant(url):
                warnings.append(url)
            continue
        missing.append(url)
    for url in warnings:
        print(f"warning: old asset URL not served {url}")
    for url in missing:
        print(f"MISSING {url}")
    print(f"{total} URLs checked, {len(missing)} missing, {len(warnings)} asset warnings")
    return 1 if missing else 0


if __name__ == "__main__":
    sys.exit(main())
