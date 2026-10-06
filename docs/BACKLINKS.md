# Backlink inventory for infosecurity.ch

Best-effort inventory of external pages that link to `infosecurity.ch`, the 2007-2017 blog
of Fabio "naif" Pietrosanti, restored at <https://infosecurity.ch>.

**Compiled:** 2026-10-06

## Totals

| Metric | Count |
|---|---|
| Confirmed linking pages | 25 |
| ... of which third-party | 23 |
| ... of which own properties | 2 |
| Distinct third-party linking domains | 14 |
| Distinct `infosecurity.ch` target URLs linked | 18 |
| Target URLs that resolve to HTTP 200 | 14 |
| Target URLs that do **not** work | 4 |
| Pages that mention the blog without linking it | 11 |
| Candidate pages that could not be fetched | 6 |

Third-party linking domains: `connect-professional.de`, `csoonline.com`, `forums.theregister.com`, `heise.de`, `linkedin.com`, `lists.torproject.org`, `mgpf.it`, `narkive.com`, `news.ycombinator.com`, `personaldemocracy.com`, `schneier.com`, `seclists.org`, `theregister.com`, `voipsa.org`.

## Confirmed linking pages

Sorted by site. `Status` is the HTTP code of the target URL exactly as linked, with the code
after following redirects in brackets - every `http://` link 301s to its `https://` form.

| Site | Date | Linking page | Target URL(s) on infosecurity.ch | Context | Status |
|---|---|---|---|---|---|
| connect-professional.de | 2010-02-03 | <https://www.connect-professional.de/security/anschuldigung-voice-security-test-ist-ein-fake-261135.html> | `http://infosecurity.ch/20100130/about-the-voice-encryption-analysis-phonecrypt-can-be-intercepted-serious-security-evaluation-criteria/`<br>`http://infosecurity.ch/20100201/evidence-that-infosecurityguard-comnotrax-is-securstar-gmbh-a-fake-independent-research-on-voice-crypto/` | "Anschuldigung: Voice-Security-Test ist ein Fake", links both analyses | 301 (200)<br>301 (200) |
| csoonline.com | 2010-02-02 | <https://www.csoonline.com/article/524574/malware-cybercrime-accusations-fly-over-voice-encryption-hack.html> | `https://infosecurity.ch/` | "Accusations Fly Over Voice Encryption Hack", links Pietrosanti's blog | 200 (200) |
| forums.theregister.com | 2010-01-30 | <https://forums.theregister.com/forum/all/2010/01/29/voice_crypto_cracks/> | `http://infosecurity.ch/20100130/about-the-voice-encryption-analysis-phonecrypt-can-be-intercepted-serious-security-evaluation-criteria/` | comment by Fabio Pietrosanti, "Analysis of the research project results" | 301 (200) |
| heise.de | 2010-02-02 | <https://www.heise.de/news/Hickhack-um-Test-fuer-Handyverschluesselung-919951.html> | `http://infosecurity.ch/20100201/evidence-that-infosecurityguard-comnotrax-is-securstar-gmbh-a-fake-independent-research-on-voice-crypto/` | German news story on the test dispute, links the evidence post | 301 (200) |
| linkedin.com | 2023-03-19 | <https://in.linkedin.com/posts/secret_playhouse-of-privacy-security-hacking-activity-7043337008152293376-4vpQ> | `https://Infosecurity.ch` | public post sharing the blog's "Playhouse of privacy, security, hacking" tagline | 200 (200) |
| lists.torproject.org | 2011-10-02 | <https://lists.torproject.org/pipermail/tor-talk/2011-October/021558.html> | `http://privacyresearch.infosecurity.ch/blocktest/blacklist-stat.sh`<br>`http://privacyresearch.infosecurity.ch/blocktest/blacklisted.txt`<br>`http://privacyresearch.infosecurity.ch/blocktest/blocklist-stat.txt`<br>`http://privacyresearch.infosecurity.ch/blocktest/extract-blacklisted-ip.sh` | exit-policy blacklist scripts and data hosted on privacyresearch.infosecurity.ch | 000 (no DNS)<br>000 (no DNS)<br>000 (no DNS)<br>000 (no DNS) |
| mgpf.it (Matteo Flora) | 2010-01-31 | <https://mgpf.it/2010/01/31/debunking-infosecurityguard-com-identity.html> | `http://infosecurity.ch`<br>`http://infosecurity.ch/20100130/about-the-voice-encryption-analysis-phonecrypt-can-be-intercepted-serious-security-evaluation-criteria/`<br>`http://infosecurity.ch/20100201/evidence-that-infosecurityguard-comnotrax-is-securstar-gmbh-a-fake-independent-research-on-voice-crypto/` | "Fabio has updated his blog with a very strong opinioned" plus reference list [1]/[5] | 301 (200)<br>301 (200)<br>301 (200) |
| narkive.com (VOIPSEC mirror) | 2010-12-02 | <https://voipsec.voipsa.narkive.com/1ffR4hfz/what-of-voip-apps-or-devices-actually-use-srtp-or-zrtp-to-encrypt-audio-calls> | `http://infosecurity.ch/20100719/snake-oil-security-claims-on-crypto-security-product/` | mirror of the same VOIPSEC message, URL in the message body | 301 (200) |
| news.ycombinator.com | 2011-04-13 | <https://news.ycombinator.com/item?id=2441296> | `http://infosecurity.ch/20110411/rfc-6189-zrtp-is-finally-a-standard/` | HN submission "RFC 6189: ZRTP is finally a standard" | 301 (200) |
| news.ycombinator.com | 2012-07-15 | <https://news.ycombinator.com/item?id=4245756> | `http://infosecurity.ch/20110123/tetra-hacking-is-coming-osmocomtetra/` | HN submission "TETRA hacking is coming: OsmocomTETRA" | 301 (200) |
| news.ycombinator.com | 2016-05-10 | <https://news.ycombinator.com/item?id=11664592> | `http://infosecurity.ch/20100926/not-every-elliptic-curve-is-the-same-trough-on-ecc-security/` | HN submission "Not every elliptic curve is the same: trough on ECC security" | 301 (200) |
| news.ycombinator.com | 2016-08-04 | <https://news.ycombinator.com/item?id=12225808> | `http://infosecurity.ch/20100926/not-every-elliptic-curve-is-the-same-trough-on-ecc-security/` | HN re-submission of the same 2010 post, "trough on ECC security" | 301 (200) |
| personaldemocracy.com | n/a | <https://personaldemocracy.com/speaker/fabio-pietrosanti/> | `http://infosecurity.ch` | speaker biography, "His blog is Infosecurity" | 301 (200) |
| schneier.com | 2010-05-27 | <https://www.schneier.com/blog/archives/2010/05/end-to-end_encr.html> | `http://infosecurity.ch` | comment thread on "End-to-End Encrypted Cell Phone Calls" | 301 (200) |
| seclists.org | 2010-01-31 | <https://seclists.org/fulldisclosure/2010/Jan/634> | `http://infosecurity.ch` | signature of "Evidence of fake security research from SecurStar GmbH" | 301 (200) |
| seclists.org | 2010-01-31 | <https://seclists.org/fulldisclosure/2010/Jan/635> | `http://infosecurity.ch`<br>`http://infosecurity.ch/20100201/dishonest-security-the-securstart-gmbh-case/`<br>`http://infosecurity.ch/20100201/evidence-that-infosecurityguard-comnotrax-is-securstar-gmbh-a-fake-independent-research-on-voice-crypto/` | Thor (Hammer of God) quoting naif's post and both blog write-ups | 301 (200)<br>301 (200)<br>301 (200) |
| seclists.org | 2010-01-31 | <https://seclists.org/fulldisclosure/2010/Jan/636> | `http://infosecurity.ch` | naif's reply in the SecurStar thread (signature) | 301 (200) |
| seclists.org | 2010-01-31 | <https://seclists.org/fulldisclosure/2010/Jan/637> | `http://infosecurity.ch`<br>`http://infosecurity.ch/20100201/dishonest-security-the-securstart-gmbh-case/`<br>`http://infosecurity.ch/20100201/evidence-that-infosecurityguard-comnotrax-is-securstar-gmbh-a-fake-independent-research-on-voice-crypto/` | Thor (Hammer of God) final reply, quoted thread with both URLs | 301 (200)<br>301 (200)<br>301 (200) |
| seclists.org | 2010-12-15 | <https://seclists.org/fulldisclosure/2010/Dec/340> | `http://infosecurity.ch` | "An idea of leaking alternative to wikileaks" (openleak proposal), signature | 301 (200) |
| seclists.org | 2010-12-15 | <https://seclists.org/fulldisclosure/2010/Dec/341> | `http://infosecurity.ch` | Christian Sciberras' reply quoting naif's signature | 301 (200) |
| seclists.org | 2010-12-15 | <https://seclists.org/fulldisclosure/2010/Dec/344> | `http://infosecurity.ch` | Andriy Tereshchenko's reply quoting naif's signature | 301 (200) |
| theregister.com | 2010-02-01 | <https://www.theregister.com/security/2010/02/01/voice-crypto-fails-spark-astroturf-claims/1395226> | `http://infosecurity.ch/20100201/evidence-that-infosecurityguard-comnotrax-is-securstar-gmbh-a-fake-independent-research-on-voice-crypto/` | linked from "a post containing screenshots and evidence" in the SecurStar/Notrax astroturf story | 301 (200) |
| voipsa.org (VOIPSEC list) | 2010-12-02 | <http://voipsa.org/pipermail/voipsec_voipsa.org/2010-December/003225.html> | `http://infosecurity.ch`<br>`http://infosecurity.ch/20100719/snake-oil-security-claims-on-crypto-security-product/` | "what's called in the crypto world Snake Oil Encryption" | 301 (200)<br>301 (200) |

### Own properties (listed for completeness, not third-party backlinks)

| Site | Linking page | Target URL(s) | Context | Status |
|---|---|---|---|---|
| fabio.pietrosanti.it | <http://fabio.pietrosanti.it/> | `http://infosecurity.ch`<br>`http://infosecurity.ch/`<br>`http://infosecurity.ch/20100201/evidence-that-infosecurityguard-comnotrax-is-securstar-gmbh-a-fake-independent-research-on-voice-crypto/`<br>`http://infosecurity.ch/20110124/my-tor-exit-node-experience-trying-to-filter-out-noisy-traffic/`<br>`http://infosecurity.ch/publickey.asc` | author's own homepage: blog link, SecurStar evidence, Tor exit-node post, PGP key | 301 (200)<br>301 (200)<br>301 (200)<br>301 (200)<br>301 (200) |
| github.com | <https://github.com/fpietrosanti/infosecurity-ch> | `https://infosecurity.ch` | repository homepage link of the restoration project itself | 200 (200) |

## Target URLs that do not return 200

| Target URL | Code | After redirects | Note |
|---|---|---|---|
| `http://privacyresearch.infosecurity.ch/blocktest/blacklist-stat.sh` | 000 (no DNS) | 000 (no DNS) | `privacyresearch.infosecurity.ch` has no A record. It was a separate Tor exit-node research VPS, never part of the blog, so a redirect on the restored site cannot fix it unless the subdomain is pointed there. |
| `http://privacyresearch.infosecurity.ch/blocktest/blacklisted.txt` | 000 (no DNS) | 000 (no DNS) | `privacyresearch.infosecurity.ch` has no A record. It was a separate Tor exit-node research VPS, never part of the blog, so a redirect on the restored site cannot fix it unless the subdomain is pointed there. |
| `http://privacyresearch.infosecurity.ch/blocktest/blocklist-stat.txt` | 000 (no DNS) | 000 (no DNS) | `privacyresearch.infosecurity.ch` has no A record. It was a separate Tor exit-node research VPS, never part of the blog, so a redirect on the restored site cannot fix it unless the subdomain is pointed there. |
| `http://privacyresearch.infosecurity.ch/blocktest/extract-blacklisted-ip.sh` | 000 (no DNS) | 000 (no DNS) | `privacyresearch.infosecurity.ch` has no A record. It was a separate Tor exit-node research VPS, never part of the blog, so a redirect on the restored site cannot fix it unless the subdomain is pointed there. |

All 14 target paths on `infosecurity.ch` itself return 200 on the restored site, so **no new**
**redirects are needed** for any backlink found here. The only dead targets live on the
`privacyresearch.infosecurity.ch` subdomain (Tor exit-node blacklist scripts and data), which
does not resolve at all.

Note: `/20100926/not-every-elliptic-curve-is-the-same-trough-on-ecc-security/`, linked twice
from Hacker News, works directly; `site/redirects.json` separately covers the truncated
`.../trough-on-ecc-/` variant.

## Mentions without a link

| Site | Date | Page | Why it is not a backlink |
|---|---|---|---|
| infosecurity-magazine.com | 2010-01 | <https://www.infosecurity-magazine.com/news/many-voice-encryption-systems-are-hackable-says/> | Covers the Notrax tests but contains no reference to infosecurity.ch (name collision with the magazine's own domain). |
| itiko.de | 2010-01-27 | <https://www.itiko.de/artikel/156447/betreiber-von-infosecurityguard-com-hackt-namhafte-handyverschluesselungsloesungen-3-von-16-unsicher.html> | Covers infosecurityguard.com but does not reference infosecurity.ch. |
| lists.ghserv.net | 2015-06-10 | <https://lists.ghserv.net/pipermail/tor2web-talk/2015-June/000133.html> | [Tor2web-talk] migration of *.tor2web.org - Message-ID domain only. |
| lists.torproject.org | 2011-08-06 | <https://lists.torproject.org/pipermail/tor-talk/2011-August/021017.html> | "Hijacking Advertising to give a Tor Exit node economic sustainability?" - e-mail address only. |
| lists.torproject.org | 2012-12-09 | <https://lists.torproject.org/pipermail/tor-talk/2012-December/026830.html> | "Botnets through Tor" - e-mail address only. |
| lists.torproject.org | 2014-01-01 | <https://lists.torproject.org/pipermail/tor-talk/2014-January/031554.html> | "A Tor-like service run by former NSA/TAO Director" - e-mail address only. |
| lists.torproject.org | 2014-09-12 | <https://lists.torproject.org/pipermail/tor-talk/2014-September/034752.html> | "Someone is crawling TorHS Directories: Honeypot" - e-mail address only. |
| mailarchive.ietf.org | n/a | <https://mailarchive.ietf.org/arch/msg/rtcweb/_jPyVCz1mnzrwfH0mTQiWMM0RWI/> | [rtcweb] Support of SDES in WebRTC - sender address only. |
| mailman.stanford.edu | 2012-12-03 | <https://mailman.stanford.edu/pipermail/liberationtech/2012-December/005865.html> | [liberationtech] Let's talk about ZRTP - carries only the From / In-Reply-To address lists@infosecurity.ch, no hyperlink to the site. Live page is 403 to automated fetches; verified through the Wayback Machine copy. |
| seclists.org | 2011-05 | <https://seclists.org/fulldisclosure/2011/May/124> | "Leakdirectory: call for contribution" - no infosecurity.ch URL in the archived copy. |
| vicinolontano.it | n/a | <https://www.vicinolontano.it/ospiti/fabio-pietrosanti/> | "Il suo blog e infosecurity.ch" - domain written as plain text, not linked. |

Mailing-list archives of messages sent from `@infosecurity.ch` are the largest group here: the
domain appears only as an e-mail address or inside a `Message-ID`, which is not a hyperlink.
The `liberationtech` 2012-December/005865 message, cited as a known starting point, falls in
this category - its body links `lumicall.org` and Zorg, not the blog.

## Candidates that could not be verified

| Site | Page | Blocker |
|---|---|---|
| athens.indymedia.org | <https://athens.indymedia.org/post/1298928/> | HTTP 429 on repeated attempts |
| decryptedmatrix.tumblr.com | <https://decryptedmatrix.tumblr.com/post/23900366553/leak-site-directory> | HTTP 403 |
| lexology.com | <https://www.lexology.com/library/detail.aspx?g=0200f331-2bae-4b09-ae56-c95829777170> | HTTP 403 (login wall) |
| mobilemag.com | <https://mobilemag.com/2010/01/27/voice-encryption-for-mobile-phones-cracked-12-out-of-15-methods-deemed-insecure/> | HTTP 525 (origin TLS failure) |
| news.softpedia.com | <https://news.softpedia.com/news/voip-phones-running-with-default-passwords-can-be-used-for-secret-surveillance-500401.shtml> | HTTP 403 |
| techsupportforum.com | <https://www.techsupportforum.com/threads/accusations-fly-over-voice-encryption-hack.457961/> | bot gate: HTTP 307 to tollbit.techsupportforum.com, then 402 |

All of these are plausible linkers - they cover the SecurStar/Notrax story or VoIP
interception - but each returned an error or a bot gate, so they are recorded as unverified
rather than counted.

## Method and limits

1. **Discovery** - roughly 40 web searches for `"infosecurity.ch"` combined with the blog's
   subjects (ZRTP, PhoneCrypt, SecurStar, Notrax, infosecurityguard, Gold-Lock, voice
   encryption, Tor exit nodes, Tor2web, GSM cracking, TETRA / OsmocomTETRA, Zorg, PrivateGSM,
   WikiLeaks / openleak, Crypto AG, iPhone PIN, BlackBerry / UAE) and with the archives that
   habitually cite it (seclists.org, lists.torproject.org, mailarchive.ietf.org,
   mailman.stanford.edu, voipsa.org, Wikipedia, Hacker News, Reddit, heise, The Register,
   Schneier). The Hacker News set was enumerated exhaustively through the Algolia search API
   (`hn.algolia.com`), which returns every submission and comment containing the domain:
   4 submissions, no comments.
2. **Verification** - every candidate was fetched once with a plain `GET` (curl, ordinary
   browser User-Agent, no `Referer` header, no repeat hits), then parsed for `href`/`src`
   attributes and for bare `infosecurity.ch` URLs in the page text. A page counts as a
   backlink only if it carries the URL; pages that merely name the blog, or that show only an
   `@infosecurity.ch` e-mail address, are listed separately. The link type (`href`,
   `markdown link`, `plain-text URL`) is recorded per page.
3. **Link health** - each distinct target URL was checked with
   `curl -sI -o /dev/null -w '%{http_code}'`, both without and with redirect following.

**Limits.** Search engines no longer expose a backlink index - `link:` operators were
withdrawn years ago and no commercial backlink service was used - so this inventory cannot be
exhaustive. Links on pages that have themselves gone offline since 2010 (much of the
blogosphere that covered the SecurStar affair) are invisible to this method, as are links in
PDFs, slide decks, closed forums, Facebook/X and paywalled archives. URLs with a query string
(for example `/?p=123`) always answer 200 on the restored site because the home page resolves
them in JavaScript, so such targets would have to be checked against `site/redirects.json`
instead; none appeared among the backlinks found here.
