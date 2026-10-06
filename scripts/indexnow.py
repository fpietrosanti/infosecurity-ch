"""Submit every sitemap URL to IndexNow (Bing, Yandex, Seznam, Naver, Yep, ...).

Run once after the DNS cut-over, and again after large content changes.
The key file site/<key>.txt must be live at https://infosecurity.ch/<key>.txt.

Usage: python scripts/indexnow.py
"""

import json
import re
import sys
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BASE = "https://infosecurity.ch"
INDEXNOW_KEY = next(p.stem for p in (ROOT / "site").glob("*.txt") if len(p.stem) == 32)


def main() -> int:
    urls = []
    for f in sorted((ROOT / "site").glob("sitemap-*.xml")):
        urls += re.findall(r"<loc>([^<]+)</loc>", f.read_text(encoding="utf-8"))
    payload = {
        "host": BASE.removeprefix("https://"),
        "key": INDEXNOW_KEY,
        "keyLocation": f"{BASE}/{INDEXNOW_KEY}.txt",
        "urlList": urls,
    }
    req = urllib.request.Request(
        "https://api.indexnow.org/indexnow",
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "Content-Type": "application/json; charset=utf-8",
            "User-Agent": "infosecurity.ch-indexnow/1.0 (+https://infosecurity.ch/)",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            print(f"IndexNow: HTTP {r.status} for {len(urls)} URLs")
    except urllib.error.HTTPError as e:
        # 403 usually means the caller's IP is blocked (GitHub Actions runners are),
        # not a bad key: run this script from a normal network instead.
        print(f"IndexNow refused the submission: HTTP {e.code} {e.reason}")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
