"""Check the generated site for broken internal references and mixed content.

- every internal href/src must resolve the way GitHub Pages resolves it
- flags http:// subresources (img/script/iframe/link), which browsers block on an HTTPS page

Usage: python scripts/check_links.py [--fail-on-mixed]
"""

import collections
import html
import re
import sys
import urllib.parse
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SITE = ROOT / "site"

# <link rel=canonical> is metadata, not a subresource: redirect stubs legitimately
# point at the http:// URL the old post linked to.
SUBRESOURCE = re.compile(
    r"<(?:img|script|iframe|embed|source|video|audio|link)\b(?![^>]*\brel=\"canonical\")[^>]*?\b(?:src|href)=\"(http://[^\"]+)\"",
    re.I,
)
REFERENCE = re.compile(r"<(?:a|img|script|iframe|embed|source|video|audio|link|form)\b[^>]*?\b(?:href|src|action)=\"([^\"]+)\"", re.I)


def resolves(path: str) -> bool:
    rel = urllib.parse.unquote(path).lstrip("/")
    if not rel or rel.endswith("/"):
        return (SITE / rel / "index.html").is_file()
    base = SITE / rel
    return base.is_file() or base.with_name(base.name + ".html").is_file() or (base / "index.html").is_file()


def main() -> int:
    broken = collections.defaultdict(set)
    mixed = collections.Counter()
    pages = 0
    for f in SITE.rglob("*.html"):
        if not f.is_file():  # the download has directories named *.html too
            continue
        pages += 1
        rel = "/" + f.relative_to(SITE).as_posix()
        page_url = rel[: -len("index.html")] if rel.endswith("/index.html") or rel == "/index.html" else rel
        s = f.read_text(encoding="utf-8", errors="replace")
        for m in SUBRESOURCE.finditer(s):
            mixed[urllib.parse.urlsplit(html.unescape(m.group(1))).hostname or "?"] += 1
        for m in REFERENCE.finditer(s):
            v = html.unescape(m.group(1)).strip()
            if v.startswith(("http:", "https:", "//", "#", "mailto:", "javascript:", "data:", "?")):
                continue
            target = urllib.parse.urlsplit(urllib.parse.urljoin("https://x" + page_url, v)).path
            if not resolves(target):
                broken[target].add(page_url)
    for target, where in sorted(broken.items(), key=lambda x: -len(x[1]))[:40]:
        print(f"BROKEN {target}  ({len(where)} page(s), e.g. {sorted(where)[0]})")
    for host, n in mixed.most_common(20):
        print(f"mixed-content http:// subresource from {host}: {n}")
    print(f"{pages} pages scanned, {len(broken)} broken internal targets, {sum(mixed.values())} http subresources")
    if "--fail-on-mixed" in sys.argv and mixed:
        return 1
    return 1 if broken else 0


if __name__ == "__main__":
    sys.exit(main())
