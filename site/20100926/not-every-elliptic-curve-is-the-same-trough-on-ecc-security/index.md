---
title: "Not every elliptic curve is the same: trough on ECC security"
url: https://infosecurity.ch/20100926/not-every-elliptic-curve-is-the-same-trough-on-ecc-security/
date: 2010-09-26
author: Fabio Pietrosanti (naif)
language: en
tags: [encryption, voicesecurity, zrtp]
---

# Not every elliptic curve is the same: trough on ECC security

```

```

```

```

```

```

```

```

```
My own ECC curve security and selection analysis
```

![vn9jna1BdgrzDCYNBJHi09q09q.jpg](https://infosecurity.ch/wp-content/uploads/2010/09/vn9jna1BdgrzDCYNBJHi09q09q.jpg)

Most modern crypto use Elliptic Curve Cryptographic (ECC) that, with a smaller key size and reduce computation power, give equivalent security strength of traditional crypto system known as DH (Diffie-Hellman) or RSA (Rivest, Shamir and Adleman) .

Not everyone knows that ECC encryption is selected for any future encryption applications and that even TLS/SSL (encryption used for securing the web) is moving to ECC.

I found plenty of so called “proprietary encryption products” which abandoned RSA and DH to goes with ECC alternatives, that tend to arbitrary use ECC bit key size without even specifying which kind of ECC crypto get used.

However there is a [lot of confusion around Elliptic Curves,](http://www.thetechherald.com/article.php/200830/1573/Q&A-with-Bill-Lattin-of-Certicom) with a lot of different names and key size making difficult for a non-cryptographically-experienced-user to make your own figure when evaluating some crypto stuff.

Because of so diffused confusion i decided to make my own analysis to find out which are the best ECC encryption curves and right ECC key size to use.

This analysis would like to provide a security industry based choice among various curves and key sizes, leaving the mathematical and crypto analytical considerations that has been already been done during the years, summarizing the various choices taken in several standards and security protocols.

First the conclusion.

From my analysis **only the following ECC curves** are to be considered for use in encryption systems because are the only one selected among different authorities (ANSI, NSA, SAG, NIST, ECC BrainPool), different security protocol standards (IPSec, OpenPGP, ZRTP, Kerberos, SSL/TLS) and the only one matching NSA Suite B security requirements (de-facto standard also for NATO military environment):

- Elliptic Prime Curve 256 bit - P-256
- Elliptic Prime Curve 384 bit - P-384

with optional, just for really paranoid that want to get more key size bit, still not considered useful:

- Elliptic Prime Curve 521 bit - P-521

I would like to state that **Koblitz curves should be avoided**, in any key size (163 / 283 / 409 / 571) as they does not have enough warranty on crypto analytic activity and effectively they are:

- Not part of NSA Suite-B cryptography selection
- Not part of ECC Brainpool selection
- Not part of ANSI X9.62 selection
- Not part of OpenPGP ECC extension selection
- Not part of Kerberos extension for ECC curve selection

I invite the reader to follow trough my analysis to understand the fundamentals that could be understood even without deep technical background but at least with a good technological background a some basic bit of cryptography.

```

```

```

```

```
Here we go with the analysis
```

```

```

```

```

```

```

```

```

My goal is to make an analysis on what/how the open scientific and security community choose ECC crypto system for usage in security protocols and standards defined by IETF RFC (the ones who define Internet Standards in a open and peer-reviewed way).

Below a set of RFC introducing ECC into existing system that get analyzed to understand what’s better to use and what’s better to exclude:

- [RFC5639](http://www.rfc-editor.org/rfc/rfc5639.txt): ECC Brainpool Standard Curves & Curve Generation
- [RFC4869](http://www.ietf.org/rfc/rfc4869.txt): NSA Suite B Cryptographic Suites for IPsec
- [RFC5430](http://www.ietf.org/rfc/rfc5430.txt): NSA Suite B profile for Transport Layer Security (TLS)
- [RFC5008](http://www.ietf.org/rfc/rfc5008.txt): NSA Suite B in in Secure/Multipurpose Internet Mail Extensions (S/MIME)
- [RFC3766](http://www.ietf.org/rfc/rfc3766.txt): Determining Strengths For Public Keys Used For Exchanging Symmetric Keys
- [RFC5349](http://www.ietf.org/rfc/rfc5349.txt): Elliptic Curve Cryptography (ECC) Support for Public Key Cryptography for Initial Authentication in Kerberos (PKINIT)
- [RFC4492](http://www.ietf.org/rfc/rfc4492): Elliptic Curve Cryptography (ECC) Cipher Suites for Transport Layer Security (TLS)
- [ZRTP voice encryption](http://tools.ietf.org/html/draft-zimmermann-avt-zrtp) by Philip Zimmermann ECC curve
- ECC in OpenPGP (draft d[raft-jivsov-openpgp-ecc-06](http://tools.ietf.org/html/draft-jivsov-openpgp-ecc-06))
- ECC Curves selected by Microsoft for [Smartcard Kerberos login](http://technet.microsoft.com/en-us/library/ff404285%28WS.10%29.aspx)

We will use the choice made by scientist defining Internet Security Protocols to make part of our evaluation.  
Additionally it must be understood that the **Curve selection comes from different authorities** that made their own selection of Curves in order to tell to the industry what to use and what to skip:

- US [NIST](http://www.nist.gov/) (US National Institute of Standards) with [186-2](http://csrc.nist.gov/publications/fips/archive/fips186-2/fips186-2.pdf) (recently superseded in 2009 by the new [186-3](http://csrc.nist.gov/publications/fips/fips186-3/fips_186-3.pdf))
- US [ANSI](http://www.ansi.org/) (American National Standard Institute) with [X9.62](http://webstore.ansi.org/RecordDetail.aspx?sku=ANSI+X9.62%3A2005)
- US [NSA](http://www.nsa.gov/) (National Security Agency) [Suite-B Cryptography](http://www.nsa.gov/ia/programs/suiteb_cryptography/) for [TOP SECRET](http://en.wikipedia.org/wiki/Security_clearance#Top_Secret) information exchange
- International [SACG](http://www.secg.org/) (Standards for efficient cryptography group) with [Recommended Elliptic Curve Domain Parameters](http://docs.google.com/viewer?url=www.secg.org/collateral/sec2_final.pdf)
- German [ECC Brainpool](http://www.ecc-brainpool.org/) withECC Brainpool with their [Strict Security Requirements](http://docs.google.com/viewer?url=http://www.ecc-brainpool.org/download/Domain-parameters.pdf)
- [ECC Interoperability Forum](http://docs.google.com/viewer?url=www.filibeto.org/~aduritz/truetrue/solaris10/security/crypto/ecc/rsa-ecc-rev8.pdf) composed by Certicom, Microsoft, Redhat, Sun, NSA

We will use the choice made by scientist defining security requirements in the standardization agencies to make part of our evaluation.  
Additionally, something that most people does not know, but that it’s extremely relevant to our analysis, is that there are different kind of ECC curve cryptography and their “size” it’s different depending on the kind of curve:

- ECC Curves over Prime Field (often referred as **Elliptic Curve** and represented by **P-keysize**)
- ECC Curves over Binary Field (often referred as **Koblitz Curve** and represented by **K-keysize**)

Given a **security strength equivalence** the Elliptic Curve and the Kobliz Curve have different key size, for example when we read ECC 571 we are referring to Koblitz Curve with an equivalent strength to ECC 521 Prime curve.

A comparison of strength between Elliptic Curves and Kotbliz Curves is reported below (from [Mikey ECC internet Draft](http://tools.ietf.org/html/draft-ietf-msec-mikey-ecc)):

```
| Koblitz |  ECC  |  DH/DSA/RSA
|   163   |  192  |     1024
|   283   |  256  |     3072
|   409   |  384  |     7680
|   571   |  521  |    15360
```

Below there’s a comparison of all selected curves by all the various entities and their respective name (from [IETF RFC4492 for ECC usage for TLS](http://www.ietf.org/rfc/rfc4492)) :

```
Curve names chosen by different standards organizations
------------+---------------+-------------
SECG        |  ANSI X9.62   |  NIST
------------+---------------+-------------
sect163k1   |               |   NIST K-163
sect163r1   |               |
sect163r2   |               |   NIST B-163
sect193r1   |               |
sect193r2   |               |
sect233k1   |               |   NIST K-233
sect233r1   |               |   NIST B-233
sect239k1   |               |
sect283k1   |               |   NIST K-283
sect283r1   |               |   NIST B-283
sect409k1   |               |   NIST K-409
sect409r1   |               |   NIST B-409
sect571k1   |               |   NIST K-571
sect571r1   |               |   NIST B-571
secp160k1   |               |
secp160r1   |               |
secp160r2   |               |
secp192k1   |               |
secp192r1   |  prime192v1   |   NIST P-192
secp224k1   |               |
secp224r1   |               |   NIST P-224
secp256k1   |               |
secp256r1   |  prime256v1   |   NIST P-256
secp384r1   |               |   NIST P-384
secp521r1   |               |   NIST P-521
------------+---------------+-------------
```

What immediately appear is that there are only two curves selected by all authorities, and that there is a general dumping of koblitz curves by ANSI.The only commonly agreed among the 3 authorities are the following two ECC curve:

- secp192r1 / prime192v1 / NIST P-192
- secp256r1 / prime256v1 / NIST P-256

Of those selection of ECC curve for TLS the [RFC5430](http://www.ietf.org/rfc/rfc5430.txt) skipped completely koblitz curves and selected for usage only:

- P-256, P-384, P-521

The [ECC Brainpool](http://www.ecc-brainpool.org/) skipped completely Koblitz curves and selected for usage the following ECC Curves:

- P-160, P-192, P-224, P-256, P-320, P-384, P-512 (**that’s the only particular because it’s not P-521 but P-512, the only key-size referred by ECC brainpool. Tnx Ian Simons from [Athena SCS](http://athena-scs.com/))**

The OpenPGP internet draft for ECC usage in PGP d[raft-jivsov-openpgp-ecc-06](http://tools.ietf.org/html/draft-jivsov-openpgp-ecc-06) skipped completely Koblitz curves and selected the following ECC curves

- P-256, P-384, P-521

The Kerberos protocol extension for ECC use, defined in [RFC5349](http://www.faqs.org/rfcs/rfc5349.html) and defined by Microsoft for [smartcard logon](http://technet.microsoft.com/en-us/library/ff404285%28WS.10%29.aspx) skipped completely Koblitz curves and selected the following ECC curves:

- P-256, P-384, P-521

So, sounds clear that the right selection of ECC is for P-256, P-384 and P-521 while the Koblitz curve have been skipped for Top Secret use and for any security sensitive protocol (IPSec, OpenPGP, ZRTP, Kerberos, SSL/TLS).

**Why i made this analysis?**

I have done this analysis following a discussion i had regarding certain voice encryption products, all based on custom and proprietary protocols, that are all using Elliptic Curve Diffie Hellman 571 bit / ECDH 571 / 571-bit ECDH / Koblitz 571 bits .  
All them are using the K-571 that, as described before, has been removed from all security sensitive environment and protocols and being myself a designer of voice encryption stuff i think that their cryptographic choice is absolutely not the best security choice.  
Probably it has been done just for marketing purpose, because K-571 (Koblitz curve) seems stronger than P-521 (Elliptic curve based on Prime number). If you have “more bit” your marketing guys can claim to be “more secure”. Koblitz elliptic curve are faster than the top secret enabled prime elliptic curve and so give the product manager a chance to provide “more bit” in it’s own product while keeping the key exchange fast.

It’s a matter of philosophical choice.

I prefer to follow the trend of scientific community with the humility of not to considering myself a cryptographic expert, knowledgable more than the overall security and scientific community itself.

I prefer instead to use only algorithms that are approved for use in highly sensitive environments (top secret classification), that have been selected by all the authorities and working group analyzing encryption algorithms existing out-there and that represent the choice of almost all standard security protocols (IPSec, OpenPGP, ZRTP, Kerberos, SSL/TLS, etc).  
I prefer to count the amount of brains working on the crypto i use, that check that’s really secure, that evaluate whether there’s some weakness.

The number of brais working on Crypto widely diffused are of order of magnitude more than the number of brains working on crypto used by just few people (like Koblitz curve).  
So i am not demonizing who use ECDH 571 using Koblitz Curve, but for sure i can affirm that they did not taken the best choice in terms of security and that any security professionals doing a security benchmarking would consider the fact that Elliptic Curve Diffie Hellman 571 bit done with Koblitz Curve is not widely diffused, it’s dumped from standard security protocols and it’s not certified for top secret use.
