---
title: "PrivateGSM: Blackberry/iPhone/Nokia mobile voice encryption with ZRTP or SRTP/SDES"
url: https://infosecurity.ch/20101019/privategsm-blackberryiphonenokia-mobile-voice-encryption-with-zrtp-or-srtpsdes/
date: 2010-10-19
author: Fabio Pietrosanti (naif)
language: en
tags: [encryption, mobile, privacy, voicesecurity, zrtp]
---

# PrivateGSM: Blackberry/iPhone/Nokia mobile voice encryption with ZRTP or SRTP/SDES

I absolutely avoid to use my own personal blog to make promotion of any kind of product.

That time it’s not different, but i want to tell you facts about products i work on without fancy marketing, but staying technical.

Today, at [PrivateWave](http://www.privatewave.com/) where i am [CTO and co-founder](http://linkedin.com/in/secret), we released publicly mobile VoIP encryption products for Blackberry, iPhone and Nokia:

- The 1st ever Blackberry encrypted VoIP with [ZRTP](http://www.privatewave.com/security/security-protocols/zrtp.html) - **PrivateGSM VoIP Professional**
- The 1st ever iPhone encrypted VoIP with [ZRTP](http://www.privatewave.com/security/security-protocols/zrtp.html) - **PrivateGSM VoIP Professional**
- **The 1st ever Blackberry encrypted VoIP client with [SRTP with SDES key exchange over SIP/TLS](http://www.privatewave.com/security/security-protocols/srtp-sdes.html) - PrivateGSM VoIP Enterprise**

[![logo-privatewave-colore.png](https://infosecurity.ch/wp-content/uploads/2010/10/logo-privatewave-colore.png)](http://www.privatewave.com/)

At PrivateWave we use a different approach respect to most voice encryption company out there, read our [approach to security](http://www.privatewave.com/security/approch.html) .

The relevance of this products in the technology and industry landscape can be summarized as follow:

- It’s the first voice encryption company using only standards security protocols (and we expect the market will react, as it’s clear that proprietary tech coming from the heritage of CSD cannot provide same value)
- It’s the first approach in voice encryption to use only open source & standard encryption engine
- It’s the first voice encryption approach to provide different security model using different technologies (end-to-end for [ZRTP](http://www.privatewave.com/security/security-protocols/zrtp.html) and [end-to-site](http://www.privatewave.com/security/security-model/end-to-site.html) for [SRTP](http://www.privatewave.com/security/security-protocols/srtp-sdes.html))

Those suite of Mobile Secure Clients, designed for professional security use only using best telecommunication and security technologies, provide a high degree of protection along with good performance also in bad network conditions:

- Multiple security model: [end-to-end](http://www.privatewave.com/security/security-model/end-to-end.html) encryption with [ZRTP](http://www.privatewave.com/security/security-protocols/zrtp.html) and [end-to-site](http://www.privatewave.com/security/security-model/end-to-site.html) encryption with SRTP
- Voice encryption
- [Signaling encryption](http://www.privatewave.com/security/security-protocols/sip-tls.html)
- Digital certificate strict checking of [SIP/TLS](http://www.privatewave.com/security/security-protocols/sip-tls.html) (99% of voip clients does not do in-depth strict [TLS](http://en.wikipedia.org/wiki/Transport_Layer_Security) checking)
- [AMR 4.75kbit codec](http://en.wikipedia.org/wiki/Adaptive_Multi-Rate_audio_codec) (same technology and audio codec of standard GSM phone calls)
- Extremely optimized [jitter buffering](http://en.wikipedia.org/wiki/Jitter) (It works even in GPRS and via WiFi over Satellite)
- Automatic always-on reconnection using [Nokia Standby Techniques](https://docs.google.com/viewer?url=http://research.nokia.com/files/NRCTR2008002.pdf) for **strong battery saving**

The applications are:

- [PrivateGSM Professional](http://www.privatewave.com/products-services/private-gsm/versions-platforms.html) **- It does [end-to-end](http://www.privatewave.com/security/security-model/end-to-end.html) encryption with [ZRTP with ECDH384](http://www.privatewave.com/security/security-protocols/zrtp.html), strict cache verification and addressbook integration**
- [PrivateGSM Enterprise](http://www.privatewave.com/products-services/private-gsm/versions-platforms.html) - **It does [end-to-site](http://www.privatewave.com/security/security-model/end-to-site.html) encryption with [SRTP with SDES key exchange over SIP/TLS](http://www.privatewave.com/security/security-protocols/srtp-sdes.html)**
- [Enterprise VoIP Security Suite](http://www.privatewave.com/enterprise-voip-security-suite/enterprise-solution.html) - [Secure PBX System](http://www.privatewave.com/security/pbx-security.html) based on Asterisk with added VoIP Firewalls

[![icona-pgsm.png](https://infosecurity.ch/wp-content/uploads/2010/10/icona-pgsm.png)](http://www.privatewave.com/)

The supported mobile devices are:

- [Nokia S60](http://www.privatewave.com/support/mobile-devices/nokia.html)
- [iPhone](http://www.privatewave.com/support/mobile-devices/iphone.html) 3GS/4G with iOS 4.x
- [Blackberry](http://www.privatewave.com/support/mobile-devices/blackberry.html) with RIMOS 5 (several GSM models)

Regarding **[ZRTP](http://www.privatewave.com/security/security-protocols/zrtp.html)** we decided to stress and stretch all the security and paranoid feature of the protocol with some little addition:

- Use only [Elliptic Curve Diffie Hellmann](http://en.wikipedia.org/wiki/Elliptic_curve_cryptography) (ECDH) 384bit that are part of [NSA Suite-B](http://en.wikipedia.org/wiki/NSA_Suite_B_Cryptography) ([No Koblitz ECDH-571 curves!](https://infosecurity.ch/20100926/not-every-elliptic-curve-is-the-same-trough-on-ecc-security/))
- Use [AES256](http://en.wikipedia.org/wiki/Advanced_Encryption_Standard) in CTR mode
- Does cache verification and key continuity
- Strict addressbook integration extended respect to RFC with additional paranoid checking
- All security warning and security error cause the call to be hangup, cache cleared and user warned to re-check ZRTP security
- Use [Random Number Generator](http://en.wikipedia.org/wiki/Random_number_generation) in strict compliance with [FIPS security requirements](http://www.privatewave.com/security/security-protocols/random-number-generation.html) by using Phisical Source of Entropy (Microphone)

Our strict address book integration, goes beyond **[ZRTP RFC](http://tools.ietf.org/html/draft-zimmermann-avt-zrtp-22) specification,** that could be vulnerable to certain attacks when used on mobile phones because of user behavior of not to look at mobile screen.

Our paranoy way of using ZRTP mitigate such conditions, we will write about this later and/or will add specific details for RFC inclusion.

**Some words on PrivateGSM Professional** with end-to-end encryption with ZRTP

- User does not need to use the application: It’s i[ntegrated in the phone for dialing with a secure prefix](http://www.privatewave.com/products-services/private-gsm/blackberry-usage-mode.html) putting +801 in front of the number to call
- **It’s** [downloadable from the internet](http://m.privategsm.com/new-webdownload/) for self trial for 15 days (most voice encryption company does not provide free download)
- **Receiver is FREE** that means that only who make calls have to buy the application, receiver does not need to pay anything
- it does **[Traffic Obfuscation](http://www.privatewave.com/security/security-protocols/rtp-traffic-obfuscation.html)** to **Bypass [VoIP blocks over 2G/3G](http://www.voip-sol.com/10-isps-and-countries-known-to-have-blocked-voip/)**
- It’s [very narrowband:](http://www.privatewave.com/support/network-requirements/voip.html) Use as little as 100Kbyte/minutes

Read [technical sheet](https://docs.google.com/viewer?url=http://www.privatewave.com/media/0/29101080972386/privategsm_voip_techsheet_en.pdf) there!

To [download it](http://www.privatewave.com/products-services/private-gsm/try-privategsm.html) click here and just put your phone number

Those are the results of hard work of all my very skilled staff (16 persons worked on this 6 projects for 3 different platforms) on challenging technologies (voice encryption) in a difficult operating environment (dirty mobile networks and dirty mobile operating systems) for more than 2 years.

I am very proud of our staff!

**What next?**

In next weeks you will see releasing of major set of documentations such as integration with asterisks, freeswitch and other Security Enabled PBX, along with some exciting other security technology news that i am sure will be noticed ;)

It has been an hard work and more have to be done but i am confident that the security and opensource community will like such products and our transparent approach also with open important releases and open source integration that make a very politically neutral (backdoor free) technology.
