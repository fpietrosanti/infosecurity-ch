---
title: "Iphone jailbreaking crashing towers? FUD!"
url: https://infosecurity.ch/20090730/iphone-jailbreaking-crashing-towers-fud/
date: 2009-07-30
author: Fabio Pietrosanti (naif)
language: en
tags: [business, hacking, mobile]
---

# Iphone jailbreaking crashing towers? FUD!

It’s interesting to read a news about an [anti-jailbreaking statement by apple](http://www.wired.com/threatlevel/2009/07/jailbreak/) that say that with jailbreaked phones it may be possible to crash mobile operator’s towers:

*By tinkering with this code, “a local or international hacker could potentially initiate commands (such as a denial of service attack) that could crash the tower software, rendering the tower entirely inoperable to process calls or transmit data,”*

So fun, as the Baseband Processor interface of iPhone is precisely the same of Google android and all Windows Mobile powered devices:

Basically the operating system use AT commands (do you remember old hayes modem commands?) with [additional parameters](http://www.3gpp.org/ftp/Specs/html-info/27007.htm) documented and standardized by 3GPP that let more deep (but not that much deep) interaction with the mobile networks.

Please note that those AT commands are **standard and widely available on all phones** and **are the interface to the Baseband Processor**.

On iPhone that’s the list of commands that an from apple point of view could let “a international hacker to crash the tower software” :

[Undocumented commands on iPhone](http://code.google.com/p/iphone-elite/wiki/UndocumentedATcommands)

Damn, those European anarchist of Nokia are providing publicly also their AT command sets, and are AVAILABLE TO ANYONE:

[Nokia AT Commands](http://wiki.forum.nokia.com/index.php/AT_Commands)

Oh jesus! Also the terrorist oriented Microsoft corporation let third party to use AT commands:

[Windows Mobile AT Commands](http://stackoverflow.com/questions/262219/windows-mobile-6-at-commands)

It’s absolutely unacceptable that also RIM, canadian funky against USA, provide access to AT commands:

[Blackberry AT commands](http://www.blackberryforums.com/linux-users-corner/145794-commands.html)

And it’s unbelivable to see that Google Android also document how the system speak to the Baseband Processor and find on forums that it’s ease to access it:

[Google Android Basedband Processor](http://www.kandroid.org/android_pdk/telephony.html)

Not to speak to ALL other mobile manufactuer that use the very same approach and let any party to speak via AT commands to the baseband processor of the phone.

Is the baseband processor of iphone buggy and the AT&T tower software buggy so that it’s dangerous to let the user make experiment with it?

Probably yes, and so those are only excuse because the software involved are not robust enough.

Apple, be careful, you have the trust of your users because you are apple you always have done things for the user advantages.

Users does like telephone companies that are huge lobbies that try to restrict and control users as much as possible.

If you, Apple, start behaving like a phone company users will not trust you anymore.

Be careful with FUD statements.
