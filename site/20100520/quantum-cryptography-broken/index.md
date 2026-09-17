---
title: "Quantum cryptography broken"
url: https://infosecurity.ch/20100520/quantum-cryptography-broken/
date: 2010-05-20
author: Fabio Pietrosanti (naif)
language: en
tags: [encryption, privacy, zrtp]
---

# Quantum cryptography broken

Quantum cryptography it’s something very challenging, encryption methods that leverage the law of phisycs to secure communications over fiber lines.

To oversimplify the system is based on the fact that if someone cut the fiber, put a tap in the middle, and joint together the other side of the fiber, the amount of “errors” that will be on the communications path will be higher than 20% .

So if QBER (Quantum Bit Error Rate) goes above 20% then it’s assumed that the system is intercepted.

Researcher at university of toronto [was able to cheat the system with a staying below the 20%, at 19.7%](http://www.networkworld.com/news/2010/052010-quantum-key-security-hacked-for.html?source=nww_rss) , thus tweaking the threshold used by the system to consider the communication channel secure vs compromised.

The product found vulnerable is called [Cerberis Layer2](http://www.idquantique.com/network-encryption/cerberis-layer2-encryption-and-qkd.html) and produced by the [Swiss ID Quantique](http://www.idquantique.com/).

Some possibile approach to detect the attack has been provided but probably, imho, such kind of systems does not have to be considered 100% reliable until the technology will be mature enough.

Traditional encryption has to be used together till several years, eventually bundled with quantum encryption whether applicable.

When we will see a quantum encryption systems on an RFC like we have seen for [ZRTP](http://en.wikipedia.org/wiki/ZRTP), [PGP](http://en.wikipedia.org/wiki/Pretty_Good_Privacy) and [SSL](http://en.wikipedia.org/wiki/Transport_Layer_Security) ?

-naif
