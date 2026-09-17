"""Build site/ from the raw Wayback download in archive/.

Deterministic and repeatable: site/ is wiped and regenerated on every run.

- Same URLs as the original WordPress blog (/YYYYMMDD/slug/, /tag/x/, /it/..., ...):
  the downloader stored /a/b/ as a/b.html, GitHub Pages needs a/b/index.html.
- Cleanup of dead WordPress/Google Analytics/comment-form/Google+ bits, HTTPS everywhere.
- Modern SEO on every page: title, description, canonical, hreflang, robots,
  Open Graph, Twitter card, JSON-LD (BlogPosting / CollectionPage / Person).
- sitemap.xml (with hreflang alternates), robots.txt, RSS feed, llms.txt,
  llms-full.txt, per-post Markdown, redirect stubs for legacy URLs, 404 page.
- New restoration post (EN/IT/DE/FR).

Usage: python scripts/build_site.py
"""

import html
import json
import os
import re
import shutil
import urllib.parse
from datetime import datetime, timezone
from email.utils import format_datetime
from pathlib import Path

from bs4 import BeautifulSoup
from markdownify import markdownify

ROOT = Path(__file__).resolve().parent.parent
ARCHIVE = ROOT / "archive"
CONTENT = ROOT / "content"
SITE = ROOT / "site"
DOCS = ROOT / "docs"

BASE = "https://infosecurity.ch"
SITE_NAME = "infosecurity.ch"
BLOG_NAME = "Playhouse of privacy, security, hacking, encryption, intelligence and some business stuff"
RESTORE_DATE = "2026-09-17"
RESTORE_HUMAN = "17 September 2026"
INDEXNOW_KEY = "5b0e8c1f7a3d4e6b9c2a1f0d8e7b6a54"
OG_IMAGE = "/og-image.png"

AUTHOR = {
    "@type": "Person",
    "@id": f"{BASE}/#author",
    "name": "Fabio Pietrosanti",
    "alternateName": "naif",
    "url": "https://fabio.pietrosanti.it/",
    "sameAs": [
        "https://fabio.pietrosanti.it/",
        "https://www.linkedin.com/in/secret/",
        "https://x.com/fpietrosanti",
        "https://twitter.com/fpietrosanti",
        "https://github.com/fpietrosanti",
        "https://www.slideshare.net/fpietrosanti",
    ],
    "knowsAbout": [
        "Information security",
        "Privacy",
        "Encryption",
        "Voice encryption",
        "ZRTP",
        "Lawful interception",
        "Tor",
        "Whistleblowing",
    ],
}

NEW_POST = {
    "path": "/20260917/infosecurity-ch-restored/",
    "iso": f"{RESTORE_DATE}T12:00:00+02:00",
    "titles": {
        "en": "infosecurity.ch is back online: the blog has been restored",
        "it": "infosecurity.ch è di nuovo online: il blog è stato ripristinato",
        "de": "infosecurity.ch ist wieder online: der Blog wurde wiederhergestellt",
        "fr": "infosecurity.ch est de nouveau en ligne : le blog a été restauré",
    },
    "dates": {
        "en": "17 September 2026",
        "it": "17 settembre 2026",
        "de": "17. September 2026",
        "fr": "17 septembre 2026",
    },
}

# Posts removed by the author before the 2017/2018 site: intentionally not restored.
# Legacy URL -> current URL (static redirect stubs).
LEGACY_REDIRECTS = {
    "/20100908/remotely-intercepting-snom-voip-phones/": "/20100910/remotely-intercepting-snom-voip-phones/",
    "/20100926/not-every-elliptic-curve-is-the-same-trough-on-ecc-/": "/20100926/not-every-elliptic-curve-is-the-same-trough-on-ecc-security/",
    "/index.php/": "/",
    "/comments/feed/": "/feed.xml",
}

HREFLANG_FIX = {"iw": "he"}
LANG_RE = re.compile(r"^[a-z]{2}(-[A-Z]{2})?$")
POST_RE = re.compile(r"^/(\d{4})(\d{2})(\d{2})/([^/]+)/$")
MONTHS = "January February March April May June July August September October November December".split()


def langs_in_archive():
    out = []
    for d in sorted(os.listdir(ARCHIVE)):
        if LANG_RE.match(d) and d != "en" and (ARCHIVE / d).is_dir():
            out.append(d)
    return out


LANGS = langs_in_archive()
# content language of single pages that differ from their URL language
LANG_OVERRIDE = {"/20070210/uno-sguardo-a/": "it"}
THIN_PAGES = {"/privacy/", "/monitoring/"}  # WordPress placeholder pages from 2008


def read(p: Path) -> str:
    return p.read_text(encoding="utf-8", errors="replace")


def write(p: Path, s: str) -> None:
    p.parent.mkdir(parents=True, exist_ok=True)
    with open(p, "w", encoding="utf-8", newline="") as f:
        f.write(s)


def esc(s: str) -> str:
    return html.escape(s, quote=True)


SITEMAP_2017 = set()


def is_html_blob(p: Path) -> bool:
    try:
        head = p.read_bytes()[:600].lower()
    except OSError:
        return False
    return b"<html" in head or b"<!doctype html" in head


def split_lang(url: str):
    parts = url.strip("/").split("/", 1)
    if parts[0] in LANGS:
        rest = "/" + (parts[1] + "/" if len(parts) > 1 and parts[1] else "")
        return parts[0], rest
    return "en", url


def lang_url(lang: str, key: str) -> str:
    return key if lang == "en" else f"/{lang}{key}"


def text_of(fragment_html: str) -> str:
    soup = BeautifulSoup(fragment_html, "lxml")
    for el in soup.select(".google-src-text, script, style, .addtoany_share_save_container"):
        el.decompose()
    return re.sub(r"\s+", " ", soup.get_text(" ")).strip()


def clip(s: str, n: int = 158) -> str:
    s = s.strip()
    if len(s) <= n:
        return s
    cut = s[:n].rsplit(" ", 1)[0].rstrip(",;:.-–")
    return cut + "…"


def extract_between(s: str, start_pat: str, end_pat: str):
    m = re.search(start_pat, s, re.S)
    if not m:
        return None
    e = s.find(end_pat, m.end())
    return s[m.end() : e] if e != -1 else None


def entry_content(s: str):
    m = re.search(r'<div class="entry-content">', s)
    if not m:
        return None
    ends = [e for e in (s.find('<div class="clear"></div>', m.end()), s.find("</div> <!-- .entry-content -->", m.end())) if e != -1]
    return s[m.end() : min(ends)] if ends else None


def post_title(s: str):
    t = re.search(r'<h2 class="single-entry-title">(.*?)</h2>', s, re.S) or re.search(
        r'<h3 class="entry-title"><a[^>]*>(.*?)</a></h3>', s, re.S
    )
    return text_of(t.group(1)) if t else None


MOJIBAKE_RE = re.compile(
    "[\u00c2-\u00f4][\u0080-\u00bf\u0152\u0153\u0160\u0161\u0178\u017d\u017e\u0192\u02c6\u02dc"
    "\u2013\u2014\u2018\u2019\u201a\u201c\u201d\u201e\u2020\u2021\u2022\u2026\u2030\u2039\u203a\u20ac\u2122]+"
)


def fix_mojibake(s: str) -> str:
    """UTF-8 text that was decoded as cp1252 once more (old 2008 theme captures)."""

    def one(m):
        try:
            return m.group(0).encode("cp1252").decode("utf-8")
        except (UnicodeEncodeError, UnicodeDecodeError):
            return m.group(0)

    s = MOJIBAKE_RE.sub(one, s)
    return s.replace("\u00c3 ", "\u00e0").replace("\u00c3\u00a0", "\u00e0")


def load_sitemap_2017():
    sm = read(ARCHIVE / "sitemap.xml")
    return {re.sub(r"^https?://infosecurity\.ch", "", u) or "/" for u in re.findall(r"<loc>([^<]+)</loc>", sm)}


# --------------------------------------------------------------------------------------
# Pass 0: inventory of archive files -> (url, output path, kind)
# --------------------------------------------------------------------------------------


def map_archive():
    pages, files = [], []
    for root, _dirs, fnames in os.walk(ARCHIVE):
        for fn in fnames:
            src = Path(root) / fn
            rel = src.relative_to(ARCHIVE).as_posix()
            if rel in (".htaccess_live", ".htaccess_file_editor", "sitemap.xml", "robots.txt"):
                continue
            if rel == "index.html":
                pages.append(("/", "index.html", src))
            elif fn.endswith(".html"):
                base = rel[:-5]
                pages.append(("/" + base + "/", base + "/index.html", src))
            elif "." not in fn and is_html_blob(src):
                pages.append(("/" + rel + "/", rel + "/index.html", src))
            else:
                files.append((rel, src))
    return pages, files


def classify(url: str, s: str) -> str:
    lang, key = split_lang(url)
    title = (re.search(r"<title>(.*?)</title>", s, re.S) or [None, ""])[1]
    if url.startswith("/outgoing/"):
        return "outgoing"
    if (
        "Page not found" in title
        or "Wayback Machine" in title
        or ("codium-extend" not in s and url not in SITEMAP_2017)
        or "/_www." in url
        or "/download/misc/" in url
        or url.startswith(("/translate/", "/viewer-url-", "/en/", "/tor-sub/"))
    ):
        return "junk"
    if key == "/":
        return "home"
    if POST_RE.match(key):
        return "post"
    if re.match(r"^/\d{8}/[^/]+/", key):
        return "junk"  # comment pagination / odd captures below a post
    if url in THIN_PAGES:
        return "junk"
    if key in ("/author/",):
        return "page"
    return "list"


# --------------------------------------------------------------------------------------
# Pass 1: metadata (English posts, dates, shortlinks, outgoing link targets)
# --------------------------------------------------------------------------------------


def collect_metadata(pages):
    posts = {}
    iso_dates = {}
    shortlinks = {}
    outgoing = {}
    for url, _out, src in pages:
        s = restore_outbound(read(src))
        for m in re.finditer(
            r"pageTracker\._trackPageview\('(/outgoing/[^']*)'\);\"\s+href=\"([^\"]*)\"",
            s,
        ):
            outgoing.setdefault(m.group(1).rstrip("/") + "/", html.unescape(m.group(2)))
        lang, key = split_lang(url)
        if lang != "en":
            continue
        for m in re.finditer(
            r'<h2 class="entry-title"><a href="([^"]*)"[^>]*>.*?</h2>\s*<div class="entry-date"><abbr class="published" title="([^"]+)"',
            s,
            re.S,
        ):
            target = urllib.parse.urljoin(BASE + url, m.group(1))[len(BASE) :]
            iso_dates[target] = m.group(2)
        m = re.search(r"rel=['\"]shortlink['\"] href=['\"]https?://infosecurity\.ch/\?p=(\d+)", s)
        if m and classify(url, s) in ("post", "page"):
            shortlinks[m.group(1)] = url
        if classify(url, s) != "post":
            continue
        body = entry_content(s) or ""
        cats = sorted(set(re.findall(r"\bs-category-([a-z0-9-]+)", s)))
        tags = sorted(set(re.findall(r"\bs-tag-([a-z0-9-]+)", s)))
        posts[url] = {
            "url": url,
            "title": post_title(s) or url,
            "body": body,
            "description": clip(text_of(body)),
            "categories": cats,
            "tags": tags,
            "comments": len(re.findall(r'<li id="comment-\d+"', s)),
        }
    for url, p in posts.items():
        y, mo, d, _slug = POST_RE.match(url).groups()
        iso = iso_dates.get(url)
        if iso:
            iso = re.sub(r"\+0000$", "+00:00", iso)
        else:
            iso = f"{y}-{mo}-{d}T12:00:00+00:00"
        p["iso"] = iso
        img = re.search(r'<img[^>]+src="([^"]+)"', p["body"])
        p["image"] = urllib.parse.urljoin(BASE + url, img.group(1)) if img else None
    return posts, shortlinks, outgoing


# --------------------------------------------------------------------------------------
# HTML transforms
# --------------------------------------------------------------------------------------

REMOVE_PATTERNS = [
    r'<link rel=["\']pingback["\'][^>]*>\n?',
    r'<link rel=["\']EditURI["\'][^>]*>\n?',
    r'<link rel=["\']wlwmanifest["\'][^>]*>[ \t]*\n?',
    r'<link rel=["\']https://api\.w\.org/["\'][^>]*>\n?',
    r'<link rel=["\']shortlink["\'][^>]*>\n?',
    r'<link rel=["\']canonical["\'][^>]*>\n?',
    r'<link rel=["\']dns-prefetch["\'] href=["\'](?:https?:)?//s\.w\.org/?["\'][^>]*>\n?',
    r'<link rel=["\']alternate["\'] type=["\'](?:application/rss\+xml|application/atom\+xml|application/json\+oembed|text/xml\+oembed)["\'][^>]*>\n?',
    r'<meta name=["\']generator["\'][^>]*>\n?',
    r'<meta name=["\']robots["\'][^>]*>\n?',
    r'<meta name=["\']description["\'][^>]*>\n?',
    r'[ \t]*<script type="text/javascript">\s*window\._wpemojiSettings.*?</script>\n?',
    r'[ \t]*<style type="text/css">\s*img\.wp-smiley.*?</style>\n?',
    r"<!-- tracker added by Ultimate Google Analytics.*?pageTracker\._trackPageview\(\);\s*</script>\n?",
    r'<script type="text/javascript" src="[^"]*akismet/_inc/form[^"]*"></script>\n?',
    r'<script type="text/javascript" src="[^"]*wp-includes/js/wp-embed\.min[^"]*"></script>\n?',
    r'<script type="text/javascript" src="[^"]*wp-includes/js/comment-reply\.min[^"]*"></script>\n?',
    r'<a class="a2a_button_google_plus"[^>]*></a>',
]

COMMENTS_CLOSED = (
    '<div id="respond" class="comment-respond"><p class="comments-closed" '
    'style="padding:1em;background:#f4f4f4;border-left:4px solid #888">'
    f"Comments are closed. This blog is a historical archive, restored on {RESTORE_HUMAN} "
    f'(<a href="{NEW_POST["path"]}">read more</a>).</p></div><!-- #respond -->'
)

COMMENTS_CLOSED_P = f'<p class="comments-closed">Comments are closed (archive restored on {RESTORE_HUMAN}).</p>'

EXTRA_CSS = """<style>
.blogtitle{display:block;font-family:'PT+Sans&subset=latin',Helvetica,Verdana,Arial,Sans-Serif;font-size:4em;font-weight:bold;margin:0 0 0 8px}
div.blogtitle a,div.blogtitle a:link,div.blogtitle a:visited,div.blogtitle a:hover{color:#444;background:transparent}
h1.single-entry-title,h1.entry-title{color:#444}
@media screen and (max-width:900px),screen and (max-device-width:480px){div.blogtitle{margin:0 0 0 -8px}}
iframe.yt{max-width:100%}
</style>"""


def restore_outbound(s: str) -> str:
    """The downloader replaced outbound links with local copies of third-party files
    (and the old site had one spam href injected). The analytics onclick path still
    records the original target: /outgoing/<host/path> or /downloads/<page>/%20<url>."""

    def fix(m):
        vp, href = m.group(1), m.group(2)
        target = None
        mm = re.search(r"%20(https?://.+)$", vp)
        if mm:
            target = mm.group(1)
        elif vp.startswith("/outgoing/"):
            dest = vp[len("/outgoing/") :]
            host = dest.split("/")[0].lower().removeprefix("www.")
            h = (urllib.parse.urlsplit(html.unescape(href)).hostname or "").lower().removeprefix("www.")
            if h != host:
                target = "http://" + dest
        if not target:
            return m.group(0)
        return m.group(0)[: m.start(2) - m.start(0)] + esc(target) + m.group(0)[m.end(2) - m.start(0) :]

    return re.sub(r"onclick=\"javascript:pageTracker\._trackPageview\('([^']*)'\);\"\s+href=\"([^\"]*)\"", fix, s)


def cleanup(s: str, outgoing_map: dict) -> str:
    s = restore_outbound(s)
    for pat in REMOVE_PATTERNS:
        s = re.sub(pat, "", s, flags=re.S)
    s = re.sub(r"\s*onclick=\"javascript:pageTracker\._trackPageview\('[^']*'\);\"", "", s)
    s = re.sub(r'(href=["\'])(?:https?:)?//+fonts\.googleapis\.com', r"\1https://fonts.googleapis.com", s)
    s = re.sub(r"http://(?:www\.)?infosecurity\.ch(?=[/\"'<\s:]|$)", "https://infosecurity.ch", s)
    s = re.sub(r"http%3A%2F%2F(?:www\.)?infosecurity\.ch", "https%3A%2F%2Finfosecurity.ch", s)
    s = re.sub(r"http:\\/\\/(?:www\.)?infosecurity\.ch", r"https:\\/\\/infosecurity.ch", s)
    s = re.sub(
        r'(src|value)="http://(www\.youtube\.com|img\.youtube\.com|static\.slidesharecdn\.com|[a-z0-9.]*gravatar\.com|s\.w\.org)',
        r'\1="https://\2',
        s,
    )
    # Flash YouTube embeds -> privacy-friendly iframe
    s = re.sub(
        r"<object\b(?:(?!</object>).)*?youtube\.com/v/([A-Za-z0-9_-]{6,})(?:(?!</object>).)*?</object>",
        lambda m: (
            f'<iframe class="yt" width="425" height="344" src="https://www.youtube-nocookie.com/embed/{m.group(1)}" '
            'title="YouTube video" loading="lazy" allowfullscreen></iframe>'
        ),
        s,
        flags=re.S,
    )
    # Comment form -> closed notice
    s = re.sub(r'<div id="respond"[^>]*>.*?</div><!-- #respond -->', COMMENTS_CLOSED, s, flags=re.S)
    s = re.sub(r'<form action="[^"]*" method="post" id="commentform".*?</form>', COMMENTS_CLOSED_P, s, flags=re.S)
    # 2008 theme comment form
    s = re.sub(
        r'<h4 id="respond" class="reply">.*?</form>',
        '<h4 id="respond" class="reply">Comments are closed</h4><p>This blog is a historical archive, restored on '
        f'{RESTORE_HUMAN}.</p>',
        s,
        flags=re.S,
    )
    # Search -> DuckDuckGo restricted to the site
    def search(m):
        f = re.sub(r'action="[^"]*"', 'action="https://duckduckgo.com/"', m.group(0), count=1)
        f = re.sub(r'\bname="s"', 'name="q"', f)
        return f.replace(">", '><input type="hidden" name="sites" value="infosecurity.ch"/>', 1)

    s = re.sub(r'<form[^>]*id="searchform".*?</form>', search, s, flags=re.S)
    if "\u00c3" in s:
        s = fix_mojibake(s)
    # Known mojibake in the 2009/08 archive page
    s = s.replace("27C3 \ufffd CCC", "27C3 – CCC").replace("\ufffdHackers\ufffd", "“Hackers”")
    return s


def insert_recent_post(s: str, lang: str) -> str:
    lang_v = lang if lang in NEW_POST["titles"] else "en"
    href = lang_url(lang_v, NEW_POST["path"])
    li = f'\n\t\t\t\t\t<li>\n\t\t\t\t<a href="{href}">{esc(NEW_POST["titles"][lang_v])}</a>\n\t\t\t\t\t\t</li>'
    return re.sub(
        r'(<li id="recent-posts-\d+" class="widget widget_recent_entries".*?<ul[^>]*>)',
        lambda m: m.group(1) + li,
        s,
        count=1,
        flags=re.S,
    )


def insert_footer_note(s: str) -> str:
    note = (
        f'<p>Archive restored on {RESTORE_HUMAN} &middot; <a href="{NEW_POST["path"]}">about the restoration</a> '
        '&middot; <a href="https://fabio.pietrosanti.it/" rel="author">Fabio Pietrosanti</a></p>'
    )
    return s.replace('<div id="footerlink"><div class="alignright">', '<div id="footerlink"><div class="alignright">' + note, 1)


def swap_headings(s: str) -> str:
    s = re.sub(
        r'<h1 id="blog-title" class="blogtitle">(.*?)</h1>',
        r'<div id="blog-title" class="blogtitle">\1</div>',
        s,
        count=1,
        flags=re.S,
    )
    s = re.sub(r'<h2 class="single-entry-title">(.*?)</h2>', r'<h1 class="single-entry-title">\1</h1>', s, count=1, flags=re.S)
    s = re.sub(r'<h2 class="entry-title">(.*?)</h2>', r'<h1 class="entry-title">\1</h1>', s, count=1, flags=re.S)
    return s


def set_html_lang(s: str, lang: str) -> str:
    code = HREFLANG_FIX.get(lang, lang)
    tag = re.search(r"<html\b[^>]*>", s)
    if not tag:
        return s
    t = re.sub(r'\s(?:xml:)?lang="[^"]*"', "", tag.group(0))
    t = t[:-1].rstrip("/").rstrip() + f' lang="{code}">'
    return s[: tag.start()] + t + s[tag.end() :]


def list_title(key: str) -> str:
    parts = [p for p in key.strip("/").split("/") if p]
    page = ""
    if "page" in parts:
        i = parts.index("page")
        page = f" – page {parts[i + 1]}" if i + 1 < len(parts) else ""
        parts = parts[:i]
    if not parts:
        return f"Latest posts{page}"
    if parts[0] == "tag" and len(parts) > 1:
        return f"Posts tagged “{parts[1]}”{page}"
    if parts[0] == "category" and len(parts) > 1:
        return f"Category: {' › '.join(parts[1:])}{page}"
    if parts[0] == "author" and len(parts) > 1:
        return f"Posts by {parts[1]}{page}"
    if re.fullmatch(r"\d{4}", parts[0]):
        if len(parts) > 1 and re.fullmatch(r"\d{2}", parts[1]):
            return f"Archive: {MONTHS[int(parts[1]) - 1]} {parts[0]}{page}"
        return f"Archive: {parts[0]}{page}"
    return " / ".join(parts) + page


def seo_head(meta: dict) -> str:
    url = BASE + meta["url"]
    lines = [
        f"<title>{esc(meta['title'])}</title>",
        f'<meta name="description" content="{esc(meta["description"])}"/>',
        f'<link rel="canonical" href="{url}"/>',
        f'<meta name="robots" content="{meta["robots"]}"/>',
        '<meta name="author" content="Fabio Pietrosanti (naif)"/>',
        f'<meta http-equiv="content-language" content="{HREFLANG_FIX.get(meta["lang"], meta["lang"])}"/>',
    ]
    for code, href in meta.get("alternates", []):
        lines.append(f'<link rel="alternate" hreflang="{code}" href="{BASE}{href}"/>')
    if meta["indexable"]:
        img = meta.get("image") or BASE + OG_IMAGE
        og_type = "article" if meta["kind"] in ("post", "newpost") else "website"
        lines += [
            f'<meta property="og:type" content="{og_type}"/>',
            f'<meta property="og:site_name" content="{SITE_NAME}"/>',
            f'<meta property="og:title" content="{esc(meta["og_title"])}"/>',
            f'<meta property="og:description" content="{esc(meta["description"])}"/>',
            f'<meta property="og:url" content="{url}"/>',
            f'<meta property="og:image" content="{esc(img)}"/>',
            f'<meta property="og:locale" content="{meta["og_locale"]}"/>',
            '<meta name="twitter:card" content="summary_large_image"/>',
            '<meta name="twitter:creator" content="@fpietrosanti"/>',
            f'<meta name="twitter:title" content="{esc(meta["og_title"])}"/>',
            f'<meta name="twitter:description" content="{esc(meta["description"])}"/>',
            f'<meta name="twitter:image" content="{esc(img)}"/>',
        ]
        if og_type == "article":
            lines += [
                f'<meta property="article:published_time" content="{meta["iso"]}"/>',
                '<meta property="article:author" content="https://fabio.pietrosanti.it/"/>',
            ]
            lines += [f'<meta property="article:section" content="{esc(c)}"/>' for c in meta.get("categories", [])]
            lines += [f'<meta property="article:tag" content="{esc(t)}"/>' for t in meta.get("tags", [])]
        lines.append('<link rel="alternate" type="application/rss+xml" title="infosecurity.ch RSS" href="/feed.xml"/>')
        if meta.get("markdown"):
            lines.append(f'<link rel="alternate" type="text/markdown" href="{meta["markdown"]}"/>')
        lines.append('<link rel="author" href="https://fabio.pietrosanti.it/"/>')
        lines.append('<link rel="me" href="https://www.linkedin.com/in/secret/"/>')
        ld = json.dumps(meta["jsonld"], ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
        lines.append(f'<script type="application/ld+json">{ld}</script>')
    lines.append(EXTRA_CSS)
    return "\n".join(lines) + "\n"


def inject_head(s: str, block: str) -> str:
    s = re.sub(r"<title>.*?</title>\s*", "", s, count=1, flags=re.S)
    m = re.search(r'<meta http-equiv="Content-Type"[^>]*>\n?', s, re.I)
    if not m:
        m = re.search(r"<head\b[^>]*>\n?", s)
    if not m:
        return block + s
    return s[: m.end()] + block + s[m.end() :]


OG_LOCALES = {
    "en": "en_US", "it": "it_IT", "de": "de_DE", "fr": "fr_FR", "es": "es_ES", "pt": "pt_PT", "nl": "nl_NL",
    "ru": "ru_RU", "ja": "ja_JP", "ko": "ko_KR", "zh-CN": "zh_CN", "zh-TW": "zh_TW", "ar": "ar_AR", "pl": "pl_PL",
    "sv": "sv_SE", "da": "da_DK", "fi": "fi_FI", "no": "nb_NO", "cs": "cs_CZ", "sk": "sk_SK", "hu": "hu_HU",
    "ro": "ro_RO", "bg": "bg_BG", "el": "el_GR", "tr": "tr_TR", "uk": "uk_UA", "iw": "he_IL", "hi": "hi_IN",
    "th": "th_TH", "vi": "vi_VN", "id": "id_ID", "ms": "ms_MY", "tl": "tl_PH", "ca": "ca_ES", "gl": "gl_ES",
    "hr": "hr_HR", "sr": "sr_RS", "sl": "sl_SI", "lt": "lt_LT", "lv": "lv_LV", "et": "et_EE", "mt": "mt_MT",
    "ga": "ga_IE", "is": "is_IS", "mk": "mk_MK", "sq": "sq_AL", "be": "be_BY", "fa": "fa_IR",
}


def breadcrumb(items):
    return {
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": i + 1, "name": n, "item": BASE + u} for i, (n, u) in enumerate(items)
        ],
    }


BLOG_LD = {
    "@type": "Blog",
    "@id": f"{BASE}/#blog",
    "name": f"{SITE_NAME} – {BLOG_NAME}",
    "url": BASE + "/",
    "inLanguage": "en",
    "author": {"@id": f"{BASE}/#author"},
    "publisher": {"@id": f"{BASE}/#author"},
    "startDate": "2007-02-10",
    "about": ["Privacy", "Information security", "Hacking", "Encryption", "Interception", "Intelligence"],
}


# --------------------------------------------------------------------------------------
# Redirect stubs, feeds, sitemap, llms
# --------------------------------------------------------------------------------------


def stub_html(target: str) -> str:
    t = esc(target)
    canon = target if target.startswith("http") else BASE + target
    return (
        '<!doctype html><html lang="en"><head><meta charset="utf-8">'
        f"<title>Moved – infosecurity.ch</title>"
        f'<link rel="canonical" href="{esc(canon)}"><meta name="robots" content="noindex,follow">'
        f'<meta http-equiv="refresh" content="0; url={t}">'
        f"<script>location.replace({json.dumps(target)}+location.hash)</script>"
        f'</head><body><p>This page has moved: <a href="{t}">{t}</a></p></body></html>\n'
    )


def write_stub(path_url: str, target: str, overwrite=False) -> bool:
    out = SITE / path_url.strip("/") / "index.html"
    if out.exists() and not overwrite:
        return False
    write(out, stub_html(target))
    return True


def absolutize(fragment: str, page_url: str) -> str:
    def fix(m):
        v = html.unescape(m.group(2))
        if v.startswith(("#", "mailto:", "javascript:", "data:")):
            return m.group(0)
        return f'{m.group(1)}="{esc(urllib.parse.urljoin(BASE + page_url, v))}"'

    return re.sub(r'\b(href|src)="([^"]*)"', fix, fragment)


def clean_body(fragment: str, outgoing_map: dict) -> str:
    fragment = cleanup(fragment, outgoing_map)
    fragment = re.sub(r'<div class="addtoany_share_save_container.*?</div></div>', "", fragment, flags=re.S)
    return fragment.strip()


def rss(items, self_url):
    now = format_datetime(datetime.now(timezone.utc))
    out = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom" xmlns:content="http://purl.org/rss/1.0/modules/content/" xmlns:dc="http://purl.org/dc/elements/1.1/">',
        "<channel>",
        f"<title>{esc(SITE_NAME)} – {esc(BLOG_NAME)}</title>",
        f"<link>{BASE}/</link>",
        f'<atom:link href="{BASE}{self_url}" rel="self" type="application/rss+xml"/>',
        "<description>Blog of Fabio Pietrosanti (naif) on privacy, security, hacking, encryption and intelligence (2007–2017), restored in 2026.</description>",
        "<language>en</language>",
        f"<lastBuildDate>{now}</lastBuildDate>",
    ]
    for it in items:
        dt = datetime.fromisoformat(it["iso"])
        body = it["html"].replace("]]>", "]]]]><![CDATA[>")
        out += [
            "<item>",
            f"<title>{esc(it['title'])}</title>",
            f"<link>{BASE}{it['url']}</link>",
            f'<guid isPermaLink="true">{BASE}{it["url"]}</guid>',
            f"<pubDate>{format_datetime(dt)}</pubDate>",
            "<dc:creator>Fabio Pietrosanti (naif)</dc:creator>",
            *[f"<category>{esc(c)}</category>" for c in it.get("tags", [])],
            f"<description>{esc(it['description'])}</description>",
            f"<content:encoded><![CDATA[{body}]]></content:encoded>",
            "</item>",
        ]
    out += ["</channel>", "</rss>", ""]
    return "\n".join(out)


def to_markdown(title, url, iso, tags, body_html, lang="en"):
    md = markdownify(body_html, heading_style="ATX", bullets="-")
    md = re.sub(r"\n{3,}", "\n\n", md).strip()
    front = [
        "---",
        f"title: {json.dumps(title, ensure_ascii=False)}",
        f"url: {BASE}{url}",
        f"date: {iso[:10]}",
        "author: Fabio Pietrosanti (naif)",
        f"language: {lang}",
    ]
    if tags:
        front.append(f"tags: [{', '.join(tags)}]")
    front += ["---", "", f"# {title}", "", md, ""]
    return "\n".join(front)


def og_image():
    from PIL import Image, ImageDraw, ImageFont

    W, H = 1200, 630
    img = Image.new("RGB", (W, H), (28, 30, 34))
    d = ImageDraw.Draw(img)
    fonts = Path(os.environ.get("WINDIR", "C:/Windows")) / "Fonts"

    def font(names, size):
        for n in names:
            for base in (fonts, Path("/usr/share/fonts/truetype/dejavu")):
                p = base / n
                if p.exists():
                    return ImageFont.truetype(str(p), size)
        return ImageFont.load_default()

    bold = font(["arialbd.ttf", "DejaVuSans-Bold.ttf"], 96)
    reg = font(["arial.ttf", "DejaVuSans.ttf"], 38)
    small = font(["arial.ttf", "DejaVuSans.ttf"], 30)
    d.rectangle([0, 0, 18, H], fill=(196, 48, 43))
    d.text((80, 150), "infosecurity.ch", font=bold, fill=(245, 245, 245))
    d.text((80, 290), "Privacy, security, hacking, encryption", font=reg, fill=(200, 200, 200))
    d.text((80, 345), "interception and intelligence", font=reg, fill=(200, 200, 200))
    d.text((80, 470), "Fabio Pietrosanti (naif)  ·  2007–2017  ·  restored 2026", font=small, fill=(150, 150, 150))
    img.save(SITE / "og-image.png", optimize=True)


# --------------------------------------------------------------------------------------
# Main build
# --------------------------------------------------------------------------------------


def main():
    SITE.mkdir(exist_ok=True)
    for child in SITE.iterdir():  # keep the directory itself (a preview server may hold it open)
        shutil.rmtree(child) if child.is_dir() else child.unlink()

    global SITEMAP_2017
    SITEMAP_2017 = load_sitemap_2017()
    pages, files = map_archive()
    posts, shortlinks, outgoing_map = collect_metadata(pages)
    print(f"{len(pages)} pages, {len(files)} files, {len(posts)} posts, {len(LANGS)} languages")

    # static files
    for rel, src in files:
        dst = SITE / rel
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dst)

    # classify + availability map for hreflang
    info = []
    available = {}
    for url, out, src in pages:
        s = read(src)
        kind = classify(url, s)
        lang, key = split_lang(url)
        info.append((url, out, src, s, kind, lang, key))
        if kind in ("home", "post", "page", "list"):
            available.setdefault(key, set()).add(lang)
    for lang in NEW_POST["titles"]:
        available.setdefault(NEW_POST["path"], set()).add(lang)

    def alternates_for(key):
        langs = available.get(key, set())
        if len(langs) < 2:
            return []
        alts = [(HREFLANG_FIX.get(lg, lg), lang_url(lg, key)) for lg in sorted(langs, key=lambda x: (x != "en", x))]
        if "en" in langs:
            alts.append(("x-default", key))
        return alts

    sitemap = []
    newest_iso = max(p["iso"] for p in posts.values())

    for url, out, src, s, kind, lang, key in info:
        dst = SITE / out
        if kind == "outgoing":
            target = outgoing_map.get(url) or "http://" + url[len("/outgoing/") :].rstrip("/")
            write(dst, stub_html(target))
            continue

        s = cleanup(s, outgoing_map)
        indexable = kind in ("home", "post", "page", "list")
        en_post = posts.get(key)
        tail = re.search(r"<title>(.*?)</title>", s, re.S)
        tail = text_of(tail.group(1)) if tail else ""
        tail = tail.split("»")[-1].strip() if "»" in tail else ""

        if kind == "post":
            ptitle = post_title(s) or (en_post or {}).get("title", tail)
            body = entry_content(s) or ""
            desc = clip(text_of(body)) or (en_post or {}).get("description", "")
        elif kind == "home":
            ptitle = "Fabio Pietrosanti's blog on privacy, security, hacking, encryption & intelligence"
            first = entry_content(s) or ""
            desc = (
                "infosecurity.ch – the 2007–2017 blog of Fabio Pietrosanti (naif): privacy, security, hacking, "
                "encryption, voice interception, Tor and intelligence. Restored archive."
                if lang == "en"
                else clip(text_of(first))
            )
        elif kind == "page":
            ptitle = "About the author & blog"
            desc = (
                "The author of infosecurity.ch is Fabio Pietrosanti (naif): home page, LinkedIn, Twitter and SlideShare profiles."
            )
        elif kind == "list":
            ptitle = list_title(key) if lang == "en" or not tail or tail == BLOG_NAME else tail
            first = re.search(r'<h2 class="entry-title"><a[^>]*>(.*?)</a>', s, re.S)
            first_t = text_of(first.group(1)) if first else ""
            desc = clip(
                f"{list_title(key)} on infosecurity.ch, the blog of Fabio Pietrosanti (naif) on privacy, security, "
                f"hacking and encryption. Latest: {first_t}."
                if lang == "en"
                else f"{ptitle}: {text_of(entry_content(s) or '')}"
            )
        else:
            ptitle = tail or "infosecurity.ch"
            desc = f"{ptitle} – infosecurity.ch archive"

        if lang != "en" and kind in ("post", "home", "list", "page"):
            suffix = f" | {SITE_NAME} ({lang})"
        else:
            suffix = f" | {SITE_NAME}"
        full_title = (ptitle if kind != "home" or lang != "en" else ptitle) + suffix
        if kind == "home" and lang == "en":
            full_title = f"{SITE_NAME} – {ptitle}"

        meta = {
            "url": url,
            "lang": lang,
            "kind": kind,
            "title": full_title,
            "og_title": ptitle,
            "description": desc or f"{ptitle} – infosecurity.ch",
            "robots": "index,follow,max-image-preview:large,max-snippet:-1,max-video-preview:-1"
            if indexable
            else "noindex,follow",
            "indexable": indexable,
            "alternates": alternates_for(key) if indexable else [],
            "og_locale": OG_LOCALES.get(lang, "en_US"),
        }
        lang = LANG_OVERRIDE.get(url, lang)
        meta["lang"] = lang
        meta["og_locale"] = OG_LOCALES.get(lang, "en_US")
        in_lang = HREFLANG_FIX.get(lang, lang)
        if kind == "post":
            p = en_post or {}
            meta.update(
                iso=p.get("iso", ""),
                tags=p.get("tags", []),
                categories=p.get("categories", []),
                image=p.get("image"),
                markdown=f"{url}index.md" if lang == "en" else None,
            )
            art = {
                "@type": "BlogPosting",
                "@id": BASE + url + "#article",
                "headline": ptitle[:110],
                "description": meta["description"],
                "url": BASE + url,
                "mainEntityOfPage": BASE + url,
                "datePublished": p.get("iso", ""),
                "dateModified": p.get("iso", ""),
                "inLanguage": in_lang,
                "author": AUTHOR,
                "publisher": {"@id": f"{BASE}/#author"},
                "image": p.get("image") or BASE + OG_IMAGE,
                "isPartOf": {"@id": f"{BASE}/#blog"},
                "keywords": ", ".join(p.get("tags", [])),
                "articleSection": p.get("categories", []),
                "commentCount": p.get("comments", 0),
                "isAccessibleForFree": True,
            }
            if lang != "en":
                art["translationOfWork"] = {"@id": BASE + key + "#article"}
                art["translator"] = {"@type": "Organization", "name": "Google Translate (automatic translation)"}
            meta["jsonld"] = {
                "@context": "https://schema.org",
                "@graph": [art, breadcrumb([("Home", lang_url(lang, "/")), (ptitle, url)])],
            }
            if lang == "en":
                sitemap_lastmod = p.get("iso", "")[:10]
            else:
                sitemap_lastmod = None
        elif kind == "home":
            meta["jsonld"] = {
                "@context": "https://schema.org",
                "@graph": [
                    {
                        "@type": "WebSite",
                        "@id": f"{BASE}/#website",
                        "url": BASE + "/",
                        "name": SITE_NAME,
                        "alternateName": BLOG_NAME,
                        "inLanguage": [HREFLANG_FIX.get(x, x) for x in ["en"] + LANGS],
                        "publisher": {"@id": f"{BASE}/#author"},
                    },
                    BLOG_LD,
                    AUTHOR,
                ],
            }
            sitemap_lastmod = RESTORE_DATE
        elif kind == "page":
            meta["jsonld"] = {
                "@context": "https://schema.org",
                "@graph": [
                    {"@type": "ProfilePage", "url": BASE + url, "name": ptitle, "inLanguage": in_lang, "mainEntity": AUTHOR},
                    breadcrumb([("Home", lang_url(lang, "/")), (ptitle, url)]),
                ],
            }
            sitemap_lastmod = None
        elif kind == "list":
            meta["jsonld"] = {
                "@context": "https://schema.org",
                "@graph": [
                    {
                        "@type": "CollectionPage",
                        "url": BASE + url,
                        "name": ptitle,
                        "inLanguage": in_lang,
                        "isPartOf": {"@id": f"{BASE}/#blog"},
                        "author": {"@id": f"{BASE}/#author"},
                    },
                    breadcrumb([("Home", lang_url(lang, "/")), (ptitle, url)]),
                ],
            }
            sitemap_lastmod = None
        else:
            meta["jsonld"] = {}
            sitemap_lastmod = None

        s = set_html_lang(s, lang)
        s = inject_head(s, seo_head(meta))
        if kind in ("post", "page"):
            s = swap_headings(s)
        if indexable:
            s = insert_recent_post(s, lang)
            s = insert_footer_note(s)
        write(dst, s)
        if indexable:
            sitemap.append((url, sitemap_lastmod, meta["alternates"]))

    # ---- new restoration post (from the newest EN post as template) ----
    newest_url = max(posts, key=lambda u: posts[u]["iso"])
    tpl = read(SITE / newest_url.strip("/") / "index.html")
    new_items = {}
    for lang, title in NEW_POST["titles"].items():
        purl = lang_url(lang, NEW_POST["path"])
        body = read(CONTENT / "restored" / f"{lang}.html")
        desc = clip(text_of(body))
        page = tpl
        # head
        page = re.sub(r"<title>.*?</title>.*?(?=<style>\n\.blogtitle)", "", page, count=1, flags=re.S)
        alts = alternates_for(NEW_POST["path"])
        art = {
            "@type": "BlogPosting",
            "@id": BASE + purl + "#article",
            "headline": title,
            "description": desc,
            "url": BASE + purl,
            "mainEntityOfPage": BASE + purl,
            "datePublished": NEW_POST["iso"],
            "dateModified": NEW_POST["iso"],
            "inLanguage": lang,
            "author": AUTHOR,
            "publisher": {"@id": f"{BASE}/#author"},
            "image": BASE + OG_IMAGE,
            "isPartOf": {"@id": f"{BASE}/#blog"},
            "keywords": "infosecurity.ch, Fabio Pietrosanti, naif, blog archive, restoration",
            "isAccessibleForFree": True,
        }
        if lang != "en":
            art["translationOfWork"] = {"@id": BASE + NEW_POST["path"] + "#article"}
        meta = {
            "url": purl,
            "lang": lang,
            "kind": "newpost",
            "title": f"{title} | {SITE_NAME}",
            "og_title": title,
            "description": desc,
            "robots": "index,follow,max-image-preview:large,max-snippet:-1,max-video-preview:-1",
            "indexable": True,
            "alternates": alts,
            "og_locale": OG_LOCALES.get(lang, "en_US"),
            "iso": NEW_POST["iso"],
            "tags": [],
            "categories": [],
            "markdown": f"{purl}index.md",
            "jsonld": {
                "@context": "https://schema.org",
                "@graph": [art, breadcrumb([("Home", lang_url(lang, "/")), (title, purl)])],
            },
        }
        page = page.replace("<style>\n.blogtitle", seo_head(meta).split("<style>\n.blogtitle")[0] + "<style>\n.blogtitle", 1)
        page = set_html_lang(page, lang)
        # body
        start = page.find('<div id="nav-above" class="navigation">')
        end = page.find("<!-- #comments -->")
        prev_title = posts[newest_url]["title"]
        nav = (
            '<div id="nav-above" class="navigation">\n\t\t\t\t<div class="nav-previous">'
            f'<a href="{newest_url}" rel="prev"><span class="meta-nav">&laquo;</span> {esc(prev_title)}</a></div>\n\t\t\t</div>\n'
        )
        block = (
            nav
            + '\t\t\t<div id="post-restored" class="hentry p1 post publish author-naif">\n'
            + f'\t\t\t\t<h1 class="single-entry-title">{esc(title)}</h1>\n'
            + '\t\t\t\t<div class="linebreak"></div>\n\t\t\t\t<div class="entry-content">\n'
            + body
            + '\t\t\t\t\t<div class="clear"></div>\n\t\t\t\t</div>\n'
            + '\t\t\t\t<div class="entry-meta">\n\t\t\t\t\t<span class="meta-prep meta-prep-author">Posted on</span> '
            + f'<a href="{purl}" rel="bookmark"><span class="entry-date"><time datetime="{NEW_POST["iso"]}">{NEW_POST["dates"][lang]}</time></span></a>'
            + ' <span class="meta-sep">by</span> <span class="author vcard"><a class="url fn n" href="/author/naif/" rel="author">naif</a></span>.\n'
            + "\t\t\t\t</div>\n\t\t\t\t<div class=\"clear\"></div>\n\t\t\t</div><!-- .post -->\n"
            + nav.replace('id="nav-above"', 'id="nav-below"')
            + '\t\t\t<div id="comments">\n\t\t\t</div>'
        )
        page = page[:start] + block + page[end:]
        page = re.sub(r'<body class="[^"]*"', '<body class="wordpress single postid-restored"', page, count=1)
        write(SITE / purl.strip("/") / "index.html", page)
        write(SITE / purl.strip("/") / "index.md", to_markdown(title, purl, NEW_POST["iso"], [], body, lang))
        sitemap.append((purl, RESTORE_DATE, alts))
        new_items[lang] = {"url": purl, "title": title, "iso": NEW_POST["iso"], "description": desc, "body": body}

    # "next" link on the previously newest post (EN)
    prev_page = SITE / newest_url.strip("/") / "index.html"
    s = read(prev_page)
    nxt = (
        f'<div class="nav-next"><a href="{NEW_POST["path"]}" rel="next">{esc(NEW_POST["titles"]["en"])} '
        '<span class="meta-nav">&raquo;</span></a></div>'
    )
    s = re.sub(r'(<div id="nav-(?:above|below)" class="navigation">\s*<div class="nav-previous">.*?</div>)', lambda m: m.group(1) + "\n\t\t\t\t" + nxt, s, flags=re.S)
    write(prev_page, s)

    # new post on top of the home pages (en/it/de/fr)
    for lang, it in new_items.items():
        home = SITE / ("index.html" if lang == "en" else f"{lang}/index.html")
        s = read(home)
        entry = (
            '<div class="dp100"></div>\n\t\t\t<!-- Begin post -->\n'
            '\t\t\t<div id="post-restored" class="hentry p1 post publish author-naif">\n'
            f'\t\t\t\t<h2 class="entry-title"><a href="{it["url"]}" rel="bookmark">{esc(it["title"])}</a></h2>\n'
            f'\t\t\t\t<div class="entry-date"><abbr class="published" title="{NEW_POST["iso"]}">{NEW_POST["dates"][lang]}</abbr></div>\n'
            f'\t\t\t\t<div class="entry-content">\n{it["body"]}\t\t\t\t</div>\n'
            '\t\t\t\t<div class="clear"></div>\n\t\t\t</div>\n\t\t\t<!-- End post -->\n<div class="linebreak clear"></div>\n\t\t\t'
        )
        s = s.replace('<div id="content">', '<div id="content">\n\t\t\t' + entry, 1)
        write(home, s)

    # ---- legacy redirects ----
    n_stubs = 0
    for src_url, target in outgoing_map.items():  # every tracked outbound link
        if re.fullmatch(r"[A-Za-z0-9._~/%+,;=@-]+", src_url):  # skip query strings / odd chars
            n_stubs += write_stub(src_url, target)
    for src_url, target in LEGACY_REDIRECTS.items():
        n_stubs += write_stub(src_url, target)
    feed_parents = ["/"] + [u for u, *_ in sitemap if split_lang(u)[0] == "en"]
    for u in feed_parents:
        if u == "/":
            continue
        n_stubs += write_stub(u + "feed/", u)

    # ---- feeds ----
    feed_items = []
    en_new = new_items["en"]
    feed_items.append(
        {**en_new, "html": absolutize(en_new["body"], en_new["url"]), "tags": []}
    )
    for p in sorted(posts.values(), key=lambda x: x["iso"], reverse=True):
        feed_items.append({**p, "html": absolutize(clean_body(p["body"], outgoing_map), p["url"])})
    write(SITE / "feed.xml", rss(feed_items[:25], "/feed.xml"))
    for legacy in ("feed", "feed/rss", "feed/rss2", "feed/atom"):
        write(SITE / legacy / "index.html", rss(feed_items[:25], "/feed.xml"))

    # ---- markdown + llms ----
    full = [
        "# infosecurity.ch – full text of all posts",
        "",
        f"> Blog of Fabio Pietrosanti (naif), 2007–2017, restored on {RESTORE_DATE}. Source: {BASE}/",
        "",
    ]
    llms_posts = []
    for it in [dict(en_new, tags=[])] + sorted(posts.values(), key=lambda x: x["iso"], reverse=True):
        body = it["body"] if it["url"] == NEW_POST["path"] else clean_body(it["body"], outgoing_map)
        md = to_markdown(it["title"], it["url"], it["iso"], it.get("tags", []), absolutize(body, it["url"]))
        if it["url"] != NEW_POST["path"]:
            write(SITE / it["url"].strip("/") / "index.md", md)
        full += [md, "", "---", ""]
        llms_posts.append(f"- [{it['title']}]({BASE}{it['url']}index.md): {it['iso'][:10]} – {it['description']}")
    write(SITE / "llms-full.txt", "\n".join(full))
    llms = [
        "# infosecurity.ch",
        "",
        "> Personal blog of Fabio Pietrosanti (naif) about privacy, information security, hacking, encryption, "
        "voice interception, Tor and intelligence, written between 2007 and 2017 and restored as a static "
        f"archive on {RESTORE_DATE}. Posts are in English; pages under /<language-code>/ are automatic "
        "translations made in 2013–2014.",
        "",
        "Author: Fabio Pietrosanti (naif) – https://fabio.pietrosanti.it/ – https://www.linkedin.com/in/secret/ – "
        "https://x.com/fpietrosanti – https://github.com/fpietrosanti",
        "",
        "Each post is available as clean Markdown at `<post-url>index.md`.",
        "",
        "## Posts",
        "",
        *llms_posts,
        "",
        "## Optional",
        "",
        f"- [Full text of every post]({BASE}/llms-full.txt)",
        f"- [About the author]({BASE}/author/)",
        f"- [RSS feed]({BASE}/feed.xml)",
        f"- [Sitemap]({BASE}/sitemap.xml)",
        "",
    ]
    write(SITE / "llms.txt", "\n".join(llms))

    # ---- sitemap ----
    sm = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">',
    ]
    for u, lastmod, alts in sorted(sitemap, key=lambda x: (split_lang(x[0])[0] != "en", x[0])):
        sm.append("<url>")
        sm.append(f"<loc>{esc(BASE + u)}</loc>")
        if lastmod:
            sm.append(f"<lastmod>{lastmod}</lastmod>")
        for code, href in alts:
            sm.append(f'<xhtml:link rel="alternate" hreflang="{code}" href="{esc(BASE + href)}"/>')
        sm.append("</url>")
    sm += ["</urlset>", ""]
    write(SITE / "sitemap.xml", "\n".join(sm))

    # ---- robots.txt ----
    ai_bots = [
        "GPTBot", "OAI-SearchBot", "ChatGPT-User", "ClaudeBot", "Claude-SearchBot", "Claude-User", "anthropic-ai",
        "PerplexityBot", "Perplexity-User", "Google-Extended", "Applebot", "Applebot-Extended", "CCBot",
        "Amazonbot", "meta-externalagent", "DuckAssistBot", "MistralAI-User", "cohere-ai", "YouBot",
    ]
    robots = [
        f"# {SITE_NAME} – archive of Fabio Pietrosanti's blog (2007–2017), restored {RESTORE_DATE}",
        "# Search engines and AI assistants are welcome. See /llms.txt",
        "",
        "User-agent: *",
        "Allow: /",
        "",
        *[f"User-agent: {b}" for b in ai_bots],
        "Allow: /",
        "",
        f"Sitemap: {BASE}/sitemap.xml",
        "",
    ]
    write(SITE / "robots.txt", "\n".join(robots))

    # ---- misc ----
    shutil.copy2(CONTENT / "publickey.asc", SITE / "publickey.asc")
    write(SITE / f"{INDEXNOW_KEY}.txt", INDEXNOW_KEY)
    write(SITE / "CNAME", "infosecurity.ch\n")
    write(SITE / ".nojekyll", "")
    og_image()

    # shortlinks /?p=N and ?s= search handled on the home page (query strings never reach a static host)
    home = SITE / "index.html"
    s = read(home)
    script = (
        "<script>(function(){var q=new URLSearchParams(location.search),m="
        + json.dumps({k: v for k, v in sorted(shortlinks.items(), key=lambda x: int(x[0]))})
        + ',t=q.get("p")||q.get("page_id");if(t&&m[t]){location.replace(m[t]);return}'
        + 'var s=q.get("s");if(s){location.replace("https://duckduckgo.com/?sites=infosecurity.ch&q="+encodeURIComponent(s))}})();</script>\n'
    )
    s = s.replace("</head>", script + "</head>", 1)
    write(home, s)
    redirects = dict(LEGACY_REDIRECTS)
    redirects.update({f"/?p={k}": v for k, v in shortlinks.items()})
    write(SITE / "redirects.json", json.dumps(redirects, indent=1, sort_keys=True) + "\n")
    write(SITE / "404.html", page_404())
    build_inventory()
    prune_orphans(files, [(u, o) for u, o, _src, _s, kind, _lang, _key in info if kind == "junk"])

    print(f"sitemap URLs: {len(sitemap)}, redirect stubs: {n_stubs}, shortlinks: {len(shortlinks)}")


EXCLUDED_URLS = [
    (r"^/wp-(json|admin|login|cron|comments-post|trackback)", "WordPress backend endpoint, not content"),
    (r"^//", "malformed crawler URL"),
    (r"^/xmlrpc\.php", "WordPress XML-RPC endpoint"),
    (r"^/cgi-sys/", "hosting provider suspended page"),
    (r"^/\.well-known/", "server probe, never existed"),
    (r"(%20| )https?:/", "broken link in old posts; 404.html redirects to the external URL"),
    (r"^/\?p=106$", "shortlink of a post deleted by the author before 2017"),
    (r"^/Tor-Scan-", "one-off 2011 scan dump, not captured"),
    (r"^/sea/docs/", "external document captured by mistake"),
    (r"/licensed-by-israel-ministry-of-defense-how-things-really-work", "post deleted by the author before 2017"),
    (r"/sip-voip-firewall-differencies-between-telephony-and-security-world", "post deleted by the author before 2017"),
    (r"^/\d{8}/[^/]+/\d+/?$", "WordPress comment-page artefact"),
]


def blog_path(path: str) -> bool:
    _lang, key = split_lang(path if path.endswith("/") else path + "/")
    return bool(
        re.match(
            r"^/(\d{8}/|\d{4}/|tag/|category/|author/|page/|outgoing/|feed/|comments/|wp-content/|wp-includes/|avatar/"
            r"|privacy/|monitoring/|index\.php|publickey\.asc|favicon\.ico|\?p=|$)",
            key if not path.startswith("/?") else path,
        )
    )


def build_inventory():
    """Every historical URL (Wayback CDX 200/301 + 2017 sitemap) -> docs/url-inventory.txt."""
    cdx = read(DOCS / "wayback-cdx-2026-09-17.txt").splitlines()
    # The downloader's sitemap and post-2018 captures (a 2023 third-party restore on the
    # same domain) also list copies of external documents: keep only blog-shaped paths.
    urls = {u for u in SITEMAP_2017 if blog_path(u)}
    for line in cdx:
        parts = line.split(" ")
        if len(parts) < 3 or parts[2] not in ("200", "301"):
            continue
        u = urllib.parse.urlsplit(parts[1])
        if (u.hostname or "").removeprefix("www.") != "infosecurity.ch":
            continue
        path = urllib.parse.unquote(u.path) or "/"
        if parts[0][:4] >= "2019" and not blog_path(path):
            continue
        if u.query:
            if path == "/" and re.fullmatch(r"p=\d+", u.query):
                urls.add(f"/?{u.query}")
                continue
            if not path.startswith(("/wp-content/", "/wp-includes/")):
                continue
        # a 301 on a slash-less path is Apache adding the trailing slash
        if parts[2] == "301" and not path.endswith("/") and not re.search(r"\.[A-Za-z0-9]{1,5}$", path.rsplit("/", 1)[-1]):
            path += "/"
        urls.add(path)
    keep, excluded = [], []
    for path in sorted(urls):
        reason = next((r for pat, r in EXCLUDED_URLS if re.search(pat, path)), None)
        (excluded if reason else keep).append((path, reason))
    write(DOCS / "url-inventory.txt", "\n".join(sorted({p for p, _ in keep})) + "\n")
    write(DOCS / "url-exclusions.txt", "\n".join(sorted({f"{p}\t{r}" for p, r in excluded})) + "\n")
    print(f"URL inventory: {len(keep)} checked, {len(excluded)} excluded")


DOWNLOADER_ARTIFACTS = {".htaccess", "nginx.txt", "files_count.xml"}
KEEP_PREFIXES = ("wp-content/", "wp-includes/", "ruffle/", "translate/", "avatar/", "menu/", "images/", "swf/", "favicon.ico")


def prune_orphans(files, junk_pages):
    """Drop downloader artefacts and third-party documents/pages no page links to any more
    (they were local copies of external links, restored to their original URLs)."""
    inventory = set((DOCS / "url-inventory.txt").read_text(encoding="utf-8").split())
    refs = set()
    for f in SITE.rglob("*"):
        if not f.is_file() or f.suffix not in (".html", ".css", ".js"):
            continue
        rel = "/" + f.relative_to(SITE).as_posix()
        page_url = rel[: -len("index.html")] if rel.endswith("/index.html") or rel == "/index.html" else rel
        for m in re.finditer(r'(?:href|src|value|data)\s*=\s*["\']([^"\']+)', read(f)):
            v = html.unescape(m.group(1))
            if v.startswith(("http:", "https:", "//", "#", "mailto:", "javascript:", "data:")):
                continue
            u = urllib.parse.urljoin("https://x" + page_url, v)
            refs.add(urllib.parse.unquote(urllib.parse.urlsplit(u).path))
    removed = 0
    for rel, _src in files:
        p = "/" + rel
        if rel in DOWNLOADER_ARTIFACTS or (
            not rel.startswith(KEEP_PREFIXES) and p not in refs and p not in inventory
        ):
            target = SITE / rel
            if target.exists():
                target.unlink()
                removed += 1
    for url, out in junk_pages:
        if not blog_path(url) and url not in refs and url not in inventory and (SITE / out).exists():
            (SITE / out).unlink()
            removed += 1
    for d in sorted((d for d in SITE.rglob("*") if d.is_dir()), key=lambda x: len(x.parts), reverse=True):
        if not any(d.iterdir()):
            d.rmdir()
    print(f"pruned {removed} orphan third-party/downloader files")


def page_404():
    langs = "|".join(re.escape(x) for x in LANGS)
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex">
<title>Page not found | infosecurity.ch</title>
<link rel="stylesheet" href="/wp-content/themes/codium-extend/style.css">
<script>
(function () {{
  var path = location.pathname, dec = path;
  try {{ dec = decodeURIComponent(path); }} catch (e) {{}}
  // old broken links such as "/tag/x/ http://host/file.pdf"
  var ext = dec.match(/\\s(https?:\\/\\/?\\S+?)\\/?$/);
  if (ext) {{ location.replace(ext[1].replace(/^(https?:)\\/(?!\\/)/, "$1//")); return; }}
  // outbound links tracked by the old analytics plugin
  var out = dec.match(/^\\/outgoing\\/(.+?)\\/?$/);
  if (out) {{ location.replace("http://" + out[1]); return; }}
  if (!/\\/$/.test(path) && !/\\.[A-Za-z0-9]+$/.test(path)) {{ location.replace(path + "/" + location.search + location.hash); return; }}
  fetch("/redirects.json").then(function (r) {{ return r.json(); }}).then(function (map) {{
    if (map[path]) {{ location.replace(map[path] + location.hash); return; }}
    // translation that was never generated: fall back to the English original
    var m = path.match(/^\\/({langs})(\\/.*)$/);
    if (m) {{ location.replace(m[2] + location.hash); }}
  }}).catch(function () {{}});
}})();
</script>
</head>
<body>
<div id="wrapper" style="padding:2em">
<h1 style="font-size:2.5em">Page not found</h1>
<p>This URL does not exist on the restored <a href="/">infosecurity.ch</a> archive.</p>
<form action="https://duckduckgo.com/" method="get"><input type="hidden" name="sites" value="infosecurity.ch">
<input type="text" name="q" aria-label="Search infosecurity.ch"> <input type="submit" value="Search"></form>
</div>
</body>
</html>
"""


if __name__ == "__main__":
    main()
