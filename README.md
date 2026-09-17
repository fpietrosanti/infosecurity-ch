# infosecurity.ch

Restoration of **infosecurity.ch**, the 2007–2017 blog of Fabio (naif) Pietrosanti, from its
Web Archive copy. It is published as a static site on GitHub Pages at <https://infosecurity.ch>,
and every original URL still works.

## Layout

| Path | Purpose |
|------|---------|
| `archive/` | Raw Wayback download, untouched (git-ignored; source zip `infosecurity.ch_fabio_infosecurity.ch_cymlmjpzq5_backup.zip`) |
| `content/` | Hand-written additions: restoration post (EN/IT/DE/FR), historical PGP key |
| `scripts/build_site.py` | `archive/` + `content/` → `site/` (deterministic, wipes `site/`) |
| `scripts/check_urls.py` | Fails if any historical URL in `docs/url-inventory.txt` is not served (runs in CI) |
| `scripts/indexnow.py` | Submits the sitemap to IndexNow (also the manual "IndexNow ping" workflow) |
| `site/` | Generated website, deployed as-is by `.github/workflows/pages.yml` |
| `docs/RESTORE.md` | What the build does, decisions, DNS setup |
| `docs/wayback-cdx-2026-09-17.txt` | Wayback CDX listing of every captured URL (source of the inventory) |

## Rebuild

```bash
unzip -q infosecurity.ch_fabio_infosecurity.ch_cymlmjpzq5_backup.zip -d archive
pip install beautifulsoup4 lxml markdownify pillow
python scripts/build_site.py && python scripts/check_urls.py
python -m http.server 8000 -d site
```
