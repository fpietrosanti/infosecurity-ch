---
title: "ESSOR, European Secure Software Defined Radio (SDR)"
url: https://infosecurity.ch/20100925/essor-european-secure-software-defined-radio-sdr/
date: 2010-09-25
author: Fabio Pietrosanti (naif)
language: en
tags: [hacking, mobile]
---

# ESSOR, European Secure Software Defined Radio (SDR)

I had a look at [European Defense Agency](http://www.eda.europa.eu/) website and found the [ESSOR](http://www.eda.europa.eu/genericitem.aspx?Area=Organisation&ID=593) project, a working project funded for 106mln EUR to develop strategic defense communication products based on new [Software Defined Radio](http://en.wikipedia.org/wiki/Software-defined_radio) approach.

SDR approach is a revolutionary system that’s completely changing the way scientist and industry is approach any kind of wireless technology.

Basically instead of burning hardware chip that implement most of the radio frequency protocols and techniques, they are pushed in “software” to specialized radio hardware that can work on a lot of different frequency, acting as radio interface for a lot of different radio protocols.

For example the USRP (Universal Software Radio Peripheral) from [Ettus Research](http://www.ettus.com/) that cost 1000-2000USD fully loaded, trough the opensource [GnuRadio](http://gnuradio.org/) framework, have seen opensource implementation of:

- [GSM](http://openbts.sf.net/)
- [Bluetooth](http://sourceforge.net/projects/gr-bluetooth/)
- [WiFi](http://docs.google.com/viewer?url=userver.ftw.at%2F~zemen%2Fpapers%2FFuxjaeger10-WSR-paper.pdf)

And a lot more protocols and transmission technologies.

That kind of new approach to Radio Transmission System is destinated to change the way radio system are implemented, giving new capability such as to upgrade the “radio protocol itself” in software in order to provide “radio protocol” improvements.

In the short terms we have also seen very strong security research using SDR technologies such as the [GSM cracking](https://svn.berlin.ccc.de/projects/airprobe/) and the [Bluetooth Sniffing](http://www.usenix.org/event/woot07/tech/full_papers/spill/spill_html/).

We can expect that other technologies, weak by design but protected by the restriction to hardware devices to hack the low level protocols, will be soon get hacked. In the first list i would really like to see the hacking of TETRA, a technology born with closed mindset and secret encryption algorithms, something i really dislike ;-)
