# infosecurity.ch

Restoration of the 2018 **infosecurity.ch** website from its Web Archive copy,
republished as a static site on GitHub Pages with the original URLs preserved.

## Layout

| Path | Purpose |
|------|---------|
| `site/` | The published website (deployed as-is by GitHub Actions) |
| `archive/` | Raw Wayback download, untouched (git-ignored, kept locally only) |
| `scripts/wayback_inventory.py` | Lists every URL the archive knows for the domain → `docs/url-inventory.txt` |
| `scripts/check_urls.py` | Verifies every inventoried URL resolves to a file in `site/` |
| `docs/RESTORE.md` | Restoration plan, URL-preservation rules, DNS cut-over |

## Status

- [x] Repository + GitHub Pages deploy pipeline
- [ ] Receive Web Archive copy → `archive/`
- [ ] Clean Wayback artifacts, normalize to `site/`
- [ ] URL inventory + 100% old-URL coverage check
- [ ] Custom domain `infosecurity.ch` (DNS on EuroDNS; **keep Google MX/SPF records**)

## Local preview

```bash
python -m http.server 8000 -d site
```
