---
title: "RFC 6189: ZRTP is finally a standard!"
url: https://infosecurity.ch/20110411/rfc-6189-zrtp-is-finally-a-standard/
date: 2011-04-11
author: Fabio Pietrosanti (naif)
language: en
tags: [encryption, privacy, voicesecurity, zrtp]
---

# RFC 6189: ZRTP is finally a standard!

Finally [ZRTP](http://en.wikipedia.org/wiki/ZRTP) has been assigned an official RFC assignment, [RFC6189](http://tools.ietf.org/html/rfc6189) ZRTP: Media Path Key Agreement for Unicast Secure RTP.

It had as a dependency the [SRTP](http://en.wikipedia.org/wiki/Secure_Real-time_Transport_Protocol) with AES key size of 256bit that now has been defined as [RFC6188](http://tools.ietf.org/html/rfc6188).

It’s exciting to see the RFC finally released, as it’s an important milestone to set ZRTP as the official standard for end-to-end encryption much like [PGP](http://tools.ietf.org/html/rfc4880) has been for emails.

Now any organization in the world will be officially able to implement ZRTP for end-to-end protocol voice encryption

Currently 3 different public implementations of ZRTP protocol exists:

- [Philip Zimmermann’s](http://www.philipzimmermann.com/) [LibZRTP](http://zfoneproject.com/) (c code)
- [PrivateWave’s ZORG](http://www.zrtp.org/) (c++ code / Java code)
- [GNU Telephony ZRTP](http://www.gnutelephony.org/index.php/GNU_ZRTP) (c++ code / Java code)

Each of them provide different features of the protocol, but most important are known to be interoperable.

A new wave is coming to the voice encryption world, irrupting into a gray area where most of the companies doing phone encryption systems has been implementing custom encryption.

Now a standard has been setup and there are few reasons left to implementing something different.

Hurra [Mr. Zimmermann](http://www.philzimmermann.com/) and all the community of companies (like [PrivateWave](http://www.privatewave.com/security/security-protocols/zrtp.html)) and individuals (like [Werner Dittmann](http://programm.froscon.org/2008/events/169.en.html)) that worked on it!

Today it’s a great day, such kind of technology is now official and also with multiple existing implementation!

Philip, you did it again, my compliments to your pure spirit and determination :-)
