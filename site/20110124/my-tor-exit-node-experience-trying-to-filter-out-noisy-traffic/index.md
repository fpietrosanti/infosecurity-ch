---
title: "My TOR exit node experience trying to filter out noisy traffic"
url: https://infosecurity.ch/20110124/my-tor-exit-node-experience-trying-to-filter-out-noisy-traffic/
date: 2011-01-24
author: Fabio Pietrosanti (naif)
language: en
tags: [privacy]
---

# My TOR exit node experience trying to filter out noisy traffic

Early this year i decided that’s time to run a TOR exit node so i brought a VPS at [hetzner.de](http://hetzner.de/) (because they are listed as a [Good TOR ISP](https://trac.torproject.org/projects/tor/wiki/TheOnionRouter/GoodBadISPs))and setup the exit-node with nickname [privacyresearch.infosecurity.ch](http://88.198.109.35/) with a 100Mbit/s connection for first 1TB of monthly data, then 10MBit/s flat.

It also run [TOR2WEB](http://www.tor2web.org/) software on <http://tor.infosecurity.ch> .

I setup the [exit-policy](http://88.198.109.35/exitpolicy.txt) as suggested by running [exit-node with minimal harassment](https://blog.torproject.org/blog/tips-running-exit-node-minimal-harassment) and prepared an [abuse response template](https://trac.torproject.org/projects/tor/wiki/TheOnionRouter/TorAbuseTemplates).

In the first day i’ve been running the node i received immediately DMCA complain due to peer to peer traffic.

So i decided to filter-out some P2P traffic by using [OpenDPI](http://www.opendpi.org/) iptables module and DMCA complain automatically disappeared:

**iptables -A OUTPUT -m opendpi -edonkey -gadugadu -fasttrack -gnutella -directconnect -bittorrent -winmx -soulseek -j REJECT**

Then, because i am italian, i decided to avoid my TOR node to connect to the Italian internet address space in order to reduce the chance that a stupid prosecutor would wake me up at morning because did not understand that i am running a TOR node.

I tried, with the help of [hellais](http://twitter.com/hellais) that wrote a [script to make Exit Policy reject statement](https://github.com/hellais/blockfinder/blob/master/torexit.py), to reject all Italian netblocks based on [ioerror’s](http://www.appelbaum.net/) [blockfinder](https://github.com/ioerror/blockfinder) but we found that the [torrc configuration](https://www.torproject.org/docs/tor-manual.html) files with +1000 lines was making TOR crash.

We went to open a ticket to report the crash about our attempt to block TOR exit policy by country and [found a similar attempt](https://trac.torproject.org/projects/tor/ticket/993) where we contributed, but it still seems to be an open-issue.

The conclusion is that it’s not possible to make a Country Exit Policy for TOR exit node in a clean and polite way so i decided to go the dirty way by using [iptables/geoip](http://www.ducea.com/2009/03/18/iptables-geoip-match-on-debian-lenny/) . After fighting to make it compile properly, it was one line of iptables to block traffic going to italy:

**iptables -A OUTPUT -p tcp -m state -state NEW -m geoip -dst-cc IT -j REJECT**

Now from my exit-node no connection to italian networks will be done and i am safe against possibly stupid prosecutors not understanding TOR (i have an exception for all TOR node ip address applied before).

After some other days i started to receive complains due to portscan activities originated from my tor nodes.

From my own point of view i want to support anonymity network, not anonymous hacking attempt and so i want to filter-out portscan and attacks from originating from my node.That’s a complex matter that require some study, so in the meantime i installed [scanlogd](http://www.openwall.com/scanlogd/) and [snort](http://www.snort.org/) because i want to evaluate how many attacks, which kind of attacks are getting out from my TOR exit node.  
Later i will try to arrange some kind of filtering to be sure to be able to filter out major attacks.  
For what’s related to portscan it seems that there are no public tools to detect and filter **outgoing portscan** but only to filter **incoming portscan** so probably will need to write something ad-hoc.  
I will refer how things are going and if there will be some nice way to implement in a lightwave way [snort-inline](http://seclab.pl/pdf/Snort-Inline_and_IPTABLES.pdf) to selectively filter-out major attack attempt originating from my exit-node.

My goal is to keep an exit node running in long-term (at least 1TB of traffic per months donated to TOR), reducing the effort related to ISP complain and trying to do my best to run the exit-node with a reasonable liability.
