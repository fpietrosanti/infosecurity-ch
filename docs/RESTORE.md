# Restoration plan

## 1. Input

The Wayback copy (downloaded via an online service) goes unmodified into
`archive/`. It is never edited; `site/` is always regenerated/cleaned from it,
so the process is repeatable.

## 2. Cleanup of Wayback artifacts

Typical things to strip or fix in the downloaded HTML:

- Wayback toolbar / injected `<script>` and `<!-- BEGIN WAYBACK TOOLBAR -->` blocks
- Rewritten links: `https://web.archive.org/web/2018xxxxxx/http://www.infosecurity.ch/foo`
  → `/foo` (root-relative, so they work on both `github.io` and the custom domain)
- Absolute `http://infosecurity.ch/...` links → root-relative
- Missing assets (images/CSS/JS the archive never captured) → list them, recover
  individually from other snapshots, or replace
- Third-party embeds that no longer exist (old analytics, widgets) → remove
- Forms/dynamic endpoints (search, contact, comments) → remove or replace with static text

## 3. URL preservation on GitHub Pages

GitHub Pages is a plain static host, so every old URL must map to a real file:

| Old URL shape | How it is served |
|---------------|------------------|
| `/page.html` | file `site/page.html` |
| `/dir/` | file `site/dir/index.html` |
| `/dir` (no slash) | Pages auto-301s to `/dir/` when `site/dir/` exists |
| `/page` (no extension) | file `site/page.html` (Pages resolves it) |
| `/page.php`, `/page.asp`, … | **not served as HTML** by Pages (wrong MIME / download). Use `site/page.php/index.html` → Pages 301s `/page.php` to `/page.php/` |
| `/?p=123`, `/index.php?id=x` | query strings are ignored by Pages → client-side redirect map in `index.html`/`404.html` (`scripts/` will generate it) |
| URLs that changed/disappeared | `404.html` JS redirect map (`site/redirects.json`), plus a meta-refresh stub file where the path is known |

Notes:
- Paths are **case-sensitive** on Pages; if the old server was case-insensitive,
  add duplicates/redirect stubs for the variants seen in the inventory.
- `site/.nojekyll` disables Jekyll so files/dirs starting with `_` are published.
- Old `http://` links and `www.` host: Pages redirects `www` ↔ apex automatically
  once the custom domain is set and both DNS records exist; HTTPS is enforced.

`scripts/wayback_inventory.py` builds the authoritative list of old URLs
(from the Wayback CDX API) and `scripts/check_urls.py` fails if any of them
does not resolve to a file in `site/`. CI runs the check on every push.

## 4. DNS cut-over (EuroDNS) — last step, only after the site is verified on github.io

Current state (2026-09-16): apex `A 3.69.105.74`, `www A 69.89.27.218`,
MX = Google Workspace, TXT = SPF + google-site-verification.

**Do not touch MX, SPF, or the TXT records** — email for @infosecurity.ch depends on them.

Change only:

```
infosecurity.ch.      A     185.199.108.153
infosecurity.ch.      A     185.199.109.153
infosecurity.ch.      A     185.199.110.153
infosecurity.ch.      A     185.199.111.153
infosecurity.ch.      AAAA  2606:50c0:8000::153
infosecurity.ch.      AAAA  2606:50c0:8001::153
infosecurity.ch.      AAAA  2606:50c0:8002::153
infosecurity.ch.      AAAA  2606:50c0:8003::153
www.infosecurity.ch.  CNAME fpietrosanti.github.io.
```

Then add `site/CNAME` containing `infosecurity.ch`, set the custom domain in
repo Settings → Pages, verify the domain for the account (TXT
`_github-pages-challenge-fpietrosanti`), and enable "Enforce HTTPS".

## Preview caveat

Before the custom domain is set, Pages serves the repo at
`https://fpietrosanti.github.io/infosecurity-ch/` (sub-path), so root-relative
links (`/foo`) will look broken there. Verify locally with
`python -m http.server 8000 -d site` (root = `/`, like the final domain), and
use the github.io URL only to confirm the deploy works.
