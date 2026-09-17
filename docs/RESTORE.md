# Restoration notes

Restored on 2026-09-17 from a Wayback download (1,653 files): WordPress 4.8, theme codium-extend,
74 posts (2007–2017), Google-Translate proxy copies in 47 languages under `/<lang>/`.

## URL preservation

- The original permalinks are `/YYYYMMDD/slug/`, `/tag/x/`, `/category/a/b/`, `/author/naif/`,
  `/YYYY/MM/`, `/page/N/` and `/<lang>/...`. The downloader stored `/a/b/` as `a/b.html`; the
  build writes `a/b/index.html`, so the URL is identical and GitHub Pages redirects `/a/b` to `/a/b/` with a 301.
- `docs/url-inventory.txt` lists 1,305 historical URLs: Wayback CDX 200/301 captures plus the
  blog-shaped URLs in the downloaded sitemap. `check_urls.py` checks all of them in CI. The run on
  2026-09-17 found 0 missing.
- `docs/url-exclusions.txt` lists the URLs deliberately not served, with the reason for each (WordPress
  endpoints, crawler garbage, posts deleted by the author before 2017).
- Legacy URLs are served by redirect stubs (meta refresh + canonical + noindex):
  - every tracked outbound link `/outgoing/<host/path>/` → the external URL
  - `/<post-or-tag>/feed/` → the page itself
  - `/20100908/remotely-intercepting-snom-voip-phones/` → `/20100910/…`
  - the truncated ECC slug → the full slug
- Shortlinks `/?p=N` (74) and `/?s=term` are handled by a script on the home page. A static host
  never sees query strings.
- `404.html` covers three more cases:
  - broken old links such as `/tag/x/%20http://host/file.pdf` → the external file
  - any `/outgoing/…` path → its host
  - a missing translation `/<lang>/path/` → the English original
- `/feed/`, `/feed/rss/`, `/feed/rss2/`, `/feed/atom/` serve the RSS XML, so old subscribers keep
  working. The canonical feed is `/feed.xml`.

## Cleanup (content unchanged)

- Removed: dead Google Analytics (UA), WordPress emoji, XML-RPC/EditURI/wlwmanifest/oEmbed/shortlink
  headers, Akismet and comment-reply scripts, Google+ share buttons.
- Comment forms are replaced by a "comments are closed" notice. Existing comments stay.
- Search goes to DuckDuckGo, restricted to infosecurity.ch.
- All `http://infosecurity.ch` references are now HTTPS. Flash YouTube embeds became `youtube-nocookie` iframes.
- **Outbound links restored.** The downloader had replaced outbound links with local copies of
  third-party documents (NIST, RFCs, theses, law-firm PDFs…). The analytics `onclick` path still
  recorded each original target, so the build restores the real external URL and does not
  republish third-party files.
- **Spam link removed.** The old WordPress had been tampered with: in the 2011 Tor exit-node post, the
  `tor.infosecurity.ch` link pointed to a spam site (`prostosale.com`). The original target is restored.
- **Encoding fixed.** Mojibake (double-encoded UTF-8) in the 2007 Italian post and the 2009/08 archive
  page is repaired.
- Post-2018 Wayback captures show that a third-party restore was served on the domain in 2023, with
  copies of external documents at root paths. Those paths are excluded from the inventory.
- Not restored: two posts the author deleted before 2017. They exist only in 2010 captures:
  "Licensed by Israel Ministry of Defense? How things really works!" and "SIP VoIP firewall
  differencies…". Recovering them from Wayback is possible if wanted.

## SEO, multilingual, LLM

- Every indexable page gets:
  - a unique `<title>`, `meta description` and self `canonical`
  - `robots` with `max-image-preview:large`
  - the correct `lang` (the translations used `it-x-mtfrom-en`; `iw` is mapped to `he`)
  - `content-language`
  - `hreflang` alternates plus `x-default`, for all languages in which the page exists
  - Open Graph and Twitter card tags (generated `og-image.png`)
  - JSON-LD: `BlogPosting` (author Person with `sameAs`, dates, keywords, `translationOfWork` for
    translations), `WebSite` + `Blog` + `Person` on the home page, `CollectionPage` for archives,
    `ProfilePage` for the author page, `BreadcrumbList`.
- Post pages: the post title is the `h1`; the site title becomes a styled `div` with the same look.
- Non-content pages (redirect stubs, 2008 WordPress placeholder pages, crawler junk) are `noindex`.
- `sitemap.xml`: 809 URLs with `xhtml:link` hreflang alternates, `lastmod` on posts.
- `robots.txt`: allows everything, lists AI crawlers explicitly, and points to the sitemap.
- `llms.txt` (index with a summary of every post), `llms-full.txt` (full text of all posts) and
  `<post>/index.md` (clean Markdown per post, linked with `rel=alternate type=text/markdown`).
- IndexNow key file at `/<key>.txt`, plus `scripts/indexnow.py`.
- New post `/20260917/infosecurity-ch-restored/` in EN, IT, DE and FR, with the author's links. It is on
  the home pages, in Recent Posts and in the feed.

## DNS (EuroDNS) — current state 2026-09-17

- Apex `A 3.69.105.74`; wildcard `*.infosecurity.ch A 3.69.105.74`; wildcard TXT (SPF).
- `www A 69.89.27.218`.
- MX: Google Workspace. TXT: SPF + google-site-verification. No CAA.

Records to set (leave MX, SPF and google-site-verification untouched):

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

- Remove the old apex `A 3.69.105.74` and `www A 69.89.27.218` (a CNAME cannot coexist with an A record).
- Remove the wildcard `*` A record: GitHub advises against wildcard DNS.
- GitHub domain verification is a TXT record `_github-pages-challenge-fpietrosanti` with the value
  shown in GitHub → Settings → Pages → Add a domain. It overrides the wildcard TXT.
- `site/CNAME` contains `infosecurity.ch`. After DNS propagates, enable **Enforce HTTPS** in the repo's Pages settings.

After cut-over: run the "IndexNow ping" workflow. Add the site to Google Search Console (the
domain is already verified via TXT) and to Bing Webmaster Tools (import from GSC), then submit
`https://infosecurity.ch/sitemap.xml` there. Optionally do the same in Yandex Webmaster, Baidu
Ziyuan and Naver Search Advisor.
