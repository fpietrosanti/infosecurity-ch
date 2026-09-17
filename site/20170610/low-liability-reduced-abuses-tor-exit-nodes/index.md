---
title: "Low Liability - Reduced Abuses Tor Exit Nodes"
url: https://infosecurity.ch/20170610/low-liability-reduced-abuses-tor-exit-nodes/
date: 2017-06-10
author: Fabio Pietrosanti (naif)
language: en
tags: [privacy]
---

# Low Liability - Reduced Abuses Tor Exit Nodes

In 2011 i’ve [experimented running a Tor Exit by reducing my liability](https://infosecurity.ch/20110124/my-tor-exit-node-experience-trying-to-filter-out-noisy-traffic/), by reducing the source of abuses.

During those years I’ve been looking at different scenarios, I’ve to admit not always in-line with the [Tor Ethical Research Guidelines](https://blog.torproject.org/blog/ethical-tor-research-guidelines), posting various ideas on tor-talk mailing list, irc channel and opening up single trac ticketing features.

In particular the following tickets has been opened for this specific purposes:

- [Introduce OutboundExitAddress to enable exit-only traffic to go via a different IP address](https://trac.torproject.org/projects/tor/ticket/17975) (IMPLEMENTED!)
- [Enable Exit Policy by Autonomous System Numbers](https://trac.torproject.org/projects/tor/ticket/18267)
- [Enable Tor Browser users to become “easy to be run” Tor Exit relay](https://trac.torproject.org/projects/tor/ticket/18269)
- [Make Tor aware of the top-30 destinations of Tor Exit traffic](https://trac.torproject.org/projects/tor/ticket/18268)

So the proposed policy to reduce the liability and abuses is following those steps::

1. Block most outgoing web attacks without causing harms to regular traffic **- Reduce automated abuses sent because of hacking attempt**
2. Block most outgoing peer to peer traffic that’s highly likely generating **- Reduce automated abuses sent because of DMCA and Copyright Infrigment**
3. Block traffic going to the countries of origin of your residences **- Improve your personal legal resiliency against simple mistake done by local law enforcement agencies**
4. Block most outgoing portscan without causing harms to regular traffic **- Reduce automated abuses sent because of hacking attempt**

It would also be possibile to follow a whitelisting approach, rather than a blacklisting one:

1. Route whitelisted traffic going trough major internet company directly (let’s assume represent top tor destination, being normally top internet destination of traffic)
2. Divert non-whitelisted traffic back into Tor network with 1-hop link trough a high speed gateway

Those methods could enable volunteers to run Tor Exit Relay rather than just Tor Relay with no-exit policy also on budget VPS. Budget VPSs usually provide a tons of bandwidth but disconnect and block your account after the very first abuses related to your IP touch their ticketing system, and for that reason it’s nearly impossible to run Tor Exit Relay on it.

Each of the steps previously defined can now be technically experimented thanks to the new [OutboundBindAddressExit](https://blog.viraptor.info/tag/dns.html "Some testing of this directive by Own automatic phishing list and Tor-to-Tor tunneling") settings that would enable to “manipulate” (but with a good intention) Tor Exit Traffic easily.

Very particular care should be taken by defining in advance how to avoid disrupting Tor Exit traffic and determining if it effectively happened and why.

That experimenting should be done by publishing transparently what’s being done and where, because ***manipulating Tor Exit Traffic is against any Tor Community Standards or Ethics Research Guideline***.

The effective willingness to do that experiments means accepting critics and incorporating each of the critics back into the hacking of the methodology being tested.

It also means accepting that the Tor Directory Authority operators may just find this behaviour unacceptable and by majority of consensus promote to block and kick-out that Tor Exit Relay from the Tor Network.

I’d love that people would pick it up the various challenges posed by those kind of setup and start testing it. Otherwise with enough Sundays, I’ll do that and document success and failures! :-)

Ah, that’s a blog post done in 2017 with my last blog post being from 2011…. maybe I’m getting back writing thoughts on blog rather than spending those time on social media?
