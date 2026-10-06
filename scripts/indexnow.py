"""Submit sitemap URLs to IndexNow — nightly rolling slices (Bing, Yandex, ...).

Richiesta 2026-10-06: "segmentare l'invio IndexNow e farlo a rotazione ogni
notte a chunk". Stesso pattern collaudato su mxmap.it: ogni notte si
sottomette UNA fetta (``--per-day``, default 30 URL) scelta in modo
deterministico (giorni-dall-epoca modulo numero di fette), con precedenza
alle pagine cambiate di recente (lastmod ≤3 giorni). Con ~814 URL il ciclo
completo dura ~27 notti (≈ mensile, come mxmap.it). Nota sulla composizione
(dall'altra sessione, 2026-10-06): 688 URL sono traduzioni statiche SENZA
lastmod (contenuto 2013-14, non cambia) — il ritmo mensile le tocca "di
rado" com'è giusto; i 76 post + 50 pagine portano lastmod, quindi ogni
modifica vera li fa risalire subito via delta-first. ``--full`` resta per i grandi cambi
(submission unica, cap 10k da protocollo).

La struttura dei sitemap NON è cablata: si legge ``site/sitemap.xml`` come
INDEX e si seguono i figli che dichiara (robusto ai restyling del sitemap;
fallback al glob ``sitemap-*.xml`` se l'index mancasse).

Resilienza (incidente 2026-10-06): il primo run da GitHub Actions prese un
403 secco. NON era l'IP dei runner bloccato (l'IndexNow di mxmap.it gira
ogni giorno dagli stessi runner con HTTP 200; lo stesso payload prese 200 da
un'altra rete pochi minuti dopo): era la race di validazione a freddo —
chiave pubblicata 2 minuti prima del ping, l'engine ha pescato un edge
stantio e cacheato il rifiuto. Quindi: (1) preflight della keyLocation con
errore parlante se la chiave non è servita (regressioni DNS/deploy);
(2) primo 403 → attesa 90s e un retry; (3) 429/5xx = transiente (warning,
exit 0 — il cron ritenta domani); 400/403/422 persistenti = errore di
configurazione (exit 1).

Usage:
  python scripts/indexnow.py [--per-day 100] [--full] [--dry-run]
Wired in .github/workflows/indexnow.yml (cron notturno + dispatch manuale).
"""

import argparse
import json
import re
import sys
import time
import urllib.error
import urllib.request
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SITE = ROOT / "site"
BASE = "https://infosecurity.ch"
INDEXNOW_KEY = next(p.stem for p in SITE.glob("*.txt") if len(p.stem) == 32)
KEY_LOCATION = f"{BASE}/{INDEXNOW_KEY}.txt"
UA = "infosecurity.ch-indexnow/2.0 (+https://infosecurity.ch/)"

_URL_RE = re.compile(
    r"<url>\s*<loc>\s*([^<\s]+)\s*</loc>(?:\s*<lastmod>\s*([^<\s]+)\s*</lastmod>)?"
)
_LOC_RE = re.compile(r"<loc>\s*([^<\s]+)\s*</loc>")


def collect_urls() -> dict[str, str]:
    """{url: lastmod} dai sitemap COMMITTATI, guidati dall'index."""
    index = SITE / "sitemap.xml"
    children: list[Path] = []
    if index.exists():
        xml = index.read_text(encoding="utf-8")
        if "<sitemapindex" in xml:
            for loc in _LOC_RE.findall(xml):
                rel = loc.removeprefix(BASE).lstrip("/")
                p = SITE / rel
                if p.exists():
                    children.append(p)
                else:
                    print(f"::warning::figlio dichiarato nell'index ma assente: {rel}")
        else:
            children = [index]  # urlset piatto
    if not children:  # fallback: index assente/vuoto
        children = sorted(SITE.glob("sitemap-*.xml"))
    pages: dict[str, str] = {}
    for child in children:
        for loc, lm in _URL_RE.findall(child.read_text(encoding="utf-8")):
            pages[loc] = lm or ""
    return pages


def todays_batch(pages: dict[str, str], per_day: int) -> tuple[int, int, int, list[str]]:
    """Delta-first (lastmod ≤3 giorni) + fetta rotante deterministica."""
    urls = sorted(pages)
    cutoff = date.fromordinal(date.today().toordinal() - 3).isoformat()
    delta = [u for u in urls if pages[u] >= cutoff]
    chunks = max(1, -(-len(urls) // per_day))  # ceil
    idx = date.today().toordinal() % chunks
    rotation = urls[idx * per_day : (idx + 1) * per_day]
    batch = list(dict.fromkeys(delta + rotation))[:9500]
    return idx, chunks, len(delta), batch


def preflight_key() -> None:
    req = urllib.request.Request(KEY_LOCATION, headers={"User-Agent": UA})
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            body = r.read().decode("utf-8", errors="ignore").strip()
    except Exception as e:  # noqa: BLE001
        sys.exit(
            f"keyLocation irraggiungibile ({KEY_LOCATION}): {e} — problema DNS/deploy, non di IndexNow"
        )
    if body != INDEXNOW_KEY:
        sys.exit(
            f"keyLocation serve contenuto sbagliato ({body[:40]!r}) — deploy stantio o file errato"
        )
    print(f"preflight ok: {KEY_LOCATION} serve la chiave")


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
    ap = argparse.ArgumentParser()
    ap.add_argument("--per-day", type=int, default=30)
    ap.add_argument("--full", action="store_true", help="tutto il sitemap in un colpo")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    pages = collect_urls()
    if not pages:
        sys.exit("nessun URL nei sitemap sotto site/ — build incompleta?")

    if args.full:
        batch = sorted(pages)
        if len(batch) > 10000:
            sys.exit(f"{len(batch)} URL oltre il limite 10k per submission: usa --per-day")
        print(f"[indexnow] FULL: {len(batch)} URL in una submission")
    else:
        idx, chunks, n_delta, batch = todays_batch(pages, args.per_day)
        print(
            f"[indexnow] URL nel sitemap: {len(pages)} | delta (≤3gg): {n_delta} "
            f"| fetta {idx + 1}/{chunks} | batch: {len(batch)} URL: "
            f"{batch[0]} … {batch[-1]}"
        )

    if args.dry_run:
        print("[indexnow] dry-run: nessuna submission")
        return 0

    preflight_key()

    status = submit(batch)
    if status == 403:
        print("::warning::HTTP 403 — possibile race di validazione: retry tra 90s")
        time.sleep(90)
        status = submit(batch)

    if status in (200, 202):
        print(f"IndexNow: HTTP {status} per {len(batch)} URL (condivisi con tutti i motori IndexNow)")
        return 0
    if status in (400, 403, 422):
        print(f"IndexNow rifiuta: HTTP {status} — configurazione (chiave/host/payload), vedi preflight")
        return 1
    print(f"::warning::IndexNow HTTP {status} transiente — il cron ritenta domani")
    return 0


if __name__ == "__main__":
    sys.exit(main())
