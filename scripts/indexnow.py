"""Submit every sitemap URL to IndexNow (Bing, Yandex, Seznam, Naver, Yep, ...).

Run after the DNS cut-over, and again after large content changes.
The key file site/<key>.txt must be live at https://infosecurity.ch/<key>.txt.

Resilience notes (2026-10-06 incident): the first run from GitHub Actions
got a bare HTTP 403. That was NOT the runner's IP being blocked (the
mxmap.it IndexNow job runs daily from the same runner pool with HTTP 200):
it was the known COLD-START validation race — the key file had gone live
two minutes earlier, api.indexnow.org fetched a stale edge and briefly
cached the refusal. The exact same payload returned 200 from another
network minutes later. Hence this script now:
  1. pre-flights the keyLocation itself (clear, actionable error if the
     key is not being served correctly — e.g. DNS or deploy regressions);
  2. treats a first 403 as the cold-start case: waits 90s and retries once;
  3. treats 429/5xx as transient (warning, exit 0 — rerun the manual
     workflow later) and persistent 403/400/422 as configuration errors.

Usage: python scripts/indexnow.py
"""

import json
import re
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BASE = "https://infosecurity.ch"
INDEXNOW_KEY = next(p.stem for p in (ROOT / "site").glob("*.txt") if len(p.stem) == 32)
KEY_LOCATION = f"{BASE}/{INDEXNOW_KEY}.txt"
UA = "infosecurity.ch-indexnow/1.0 (+https://infosecurity.ch/)"


def preflight_key() -> None:
    """The engine validates keyLocation before accepting a submission; if WE
    cannot fetch our own key, submitting is pointless — fail with the real
    reason instead of a mystery 403."""
    req = urllib.request.Request(KEY_LOCATION, headers={"User-Agent": UA})
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            body = r.read().decode("utf-8", errors="ignore").strip()
    except Exception as e:  # noqa: BLE001
        sys.exit(f"keyLocation unreachable ({KEY_LOCATION}): {e} — DNS or deploy problem, not an IndexNow one")
    if body != INDEXNOW_KEY:
        sys.exit(f"keyLocation serves wrong content ({body[:40]!r}) — stale deploy or wrong file at {KEY_LOCATION}")
    print(f"preflight ok: {KEY_LOCATION} serves the key")


def submit(urls: list[str]) -> int:
    payload = {
        "host": BASE.removeprefix("https://"),
        "key": INDEXNOW_KEY,
        "keyLocation": KEY_LOCATION,
        "urlList": urls,
    }
    req = urllib.request.Request(
        "https://api.indexnow.org/indexnow",
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json; charset=utf-8", "User-Agent": UA},
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            return r.status
    except urllib.error.HTTPError as e:
        return e.code


def main() -> int:
    urls = []
    for f in sorted((ROOT / "site").glob("sitemap-*.xml")):
        urls += re.findall(r"<loc>([^<]+)</loc>", f.read_text(encoding="utf-8"))
    if not urls:
        sys.exit("no URLs found in site/sitemap-*.xml")
    if len(urls) > 10000:
        sys.exit(f"{len(urls)} URLs exceed the 10k-per-submission IndexNow limit: split needed")

    preflight_key()

    status = submit(urls)
    if status == 403:
        # Known cold-start: the engine may briefly cache a failed key
        # validation right after the key file is first published.
        print("::warning::HTTP 403 — cold-start validation race? Retrying once in 90s")
        time.sleep(90)
        status = submit(urls)

    if status in (200, 202):
        print(f"IndexNow: HTTP {status} for {len(urls)} URLs (shared with all IndexNow engines)")
        return 0
    if status in (400, 403, 422):
        print(f"IndexNow refused the submission: HTTP {status} — configuration problem (key/host/payload), see preflight above")
        return 1
    # 429 / 5xx: transient on their side; this is a manual workflow — rerun later.
    print(f"::warning::IndexNow transient HTTP {status} — rerun the workflow later")
    return 0


if __name__ == "__main__":
    sys.exit(main())
