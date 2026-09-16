"""Build the list of historical URLs of infosecurity.ch from the Wayback CDX API.

Writes docs/url-inventory.txt: one root-relative path (with query string, if any)
per line, only for captures that returned HTTP 200 in the chosen period.

Usage: python scripts/wayback_inventory.py [--from 2010] [--to 2018]
"""

import argparse
import json
import time
import urllib.parse
import urllib.request
from pathlib import Path

CDX = "https://web.archive.org/cdx/search/cdx"
DOMAIN = "infosecurity.ch"
OUT = Path(__file__).resolve().parent.parent / "docs" / "url-inventory.txt"


def fetch(params: dict, retries: int = 5) -> list:
    url = CDX + "?" + urllib.parse.urlencode(params)
    for attempt in range(retries):
        try:
            with urllib.request.urlopen(url, timeout=120) as r:
                return json.loads(r.read().decode("utf-8") or "[]")
        except Exception as exc:  # archive.org is flaky / rate-limited
            wait = 30 * (attempt + 1)
            print(f"CDX error ({exc}); retry in {wait}s")
            time.sleep(wait)
    raise SystemExit("CDX API unavailable, try again later")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--from", dest="start", default="2000")
    ap.add_argument("--to", dest="end", default="2018")
    args = ap.parse_args()

    rows = fetch(
        {
            "url": f"{DOMAIN}/*",
            "matchType": "domain",
            "from": args.start,
            "to": args.end,
            "output": "json",
            "fl": "original,mimetype,statuscode",
            "filter": "statuscode:200",
            "collapse": "urlkey",
        }
    )
    paths = set()
    for original, _mime, _status in rows[1:]:
        u = urllib.parse.urlsplit(original)
        path = u.path or "/"
        paths.add(path + ("?" + u.query if u.query else ""))

    OUT.write_text("\n".join(sorted(paths)) + "\n", encoding="utf-8")
    print(f"{len(paths)} URLs -> {OUT}")


if __name__ == "__main__":
    main()
