---
title: "About the SecurStar GmbH Phonecrypt voice encryption analysis (criteria, errors and different results)"
url: https://infosecurity.ch/20100130/about-the-voice-encryption-analysis-phonecrypt-can-be-intercepted-serious-security-evaluation-criteria/
date: 2010-01-30
author: Fabio Pietrosanti (naif)
language: en
tags: [business, encryption, marketing, mobile, privacy, voicesecurity, zrtp]
---

# About the SecurStar GmbH Phonecrypt voice encryption analysis (criteria, errors and different results)

This article want to clarify and better explain the finding at infosecurityguard.com regaring voice encryption product evaluation.  
This article want to tell you a different point of view other than infosecurityguard.com and explaining which are the rational with extensive explaination from security point of view.  
Today i read news saying: “PhoneCrypt: Basic Vulnerability Found in 12 out of 15 Voice Encryption Products and went to read the website [infosecurityguard](http://infosecurityguard.com/).

Initially it appeared to my like a great research activity but then i started reading deeply the read about it.I found that it’s not properly a security research but there is are concrete elements that’s a marketing campaign well done in order to attract public media and publicize a product.  
Imho they was able to cheat journalists and users because the marketing campaign was absolutely well done not to be discovered on 1st read attempt. I personally considered it like a valid one on 1st ready (they cheated me initially!).

But if you go deeply… you will understand that:  
**- it’s a camouflage marketing initiative arranged by SecurStar GmbH and not a independent security research  
- they consider a only security context where local device has been compromised (no software can be secured in that case, like saying SSL can be compromised if you have a trojan!)  
- they do not consider any basic security and cryptographic security criteria**

However a lot of important website reported it:

- [The Register](http://www.theregister.co.uk/2010/01/29/voice_crypto_cracks/)
- [Network World](http://www.networkworld.com/news/2010/012810-leading-voice-encryption-programs-hacked.html)
- [Slashdot](http://yro.slashdot.org/story/10/01/28/2317254/80-of-Cell-Phone-Encryption-Solutions-Insecure?from=rss)
- [InfoSecurity Magazine](http://www.infosecurity-magazine.com/view/6826/many-voice-encryption-systems-are-hackable-says-anonymous-researcher/)

This article is quite long, if you read it you will understand better what’s going on around infosecurityguard.com research and research result.

I want to to tell you why and how (imho) they are wrong.

## The research missed to consider Security, Cryptography and Transparency!

Well, all this research sound much like being focused on the marketing goal to say that their PhoneCrypt product is the “super” product best of all the other ones.  
Any security expert that would have as duty the “software evaluation” in order to protect the confidentiality of phone calls will evaluate other different characteristics of the product and the technology.

Yes, it’s true that most of the product described by SecurStar in their anonymous marketing website called http://infosecurityguard.com have some weakness.  
But the relevant weakness are others and PhoneCrypt unfortunately, like most of the described products suffer from this.  
Let’s review which characteristics are needed basic cryptography and security requirement (the best practice, the foundation and the basics!)

## a - Security Trough Obscurity does not work

A basic rule in cryptography cames from 1883 by Auguste Kerckhoffs:

**In a well-designed cryptographic system, only the key needs to be secret; there should be no secrecy in the algorithm.**

**Modern cryptographers have embraced this principle, calling anything else “security by obscurity.”**

Read what Bruce Schneir, recognized expert and cryptographer in the world say [about this](http://www.schneier.com/crypto-gram-0205.html)

Any security expert will tell you that’s true. Even a novice university student will tell you that’s true. Simply because that’s the only way to do cryptography.

Almost all product described in the review by SecurStar GmbH, include PhoneCrypt, does not provide precise details about their cryptographic technologies.

Precise details are:

- Detailed specification of cryptographic algorithm (that’s not just saying “we use [AES](http://en.wikipedia.org/wiki/Advanced_Encryption_Standard)“)
- Detailed specification of cryptographic protocol (that’s not just saying “we use [Diffie Hellman](http://en.wikipedia.org/wiki/Diffie%E2%80%93Hellman_key_exchange)” )
- Detailed specification of measuring the cryptographic strenght (that’s not just saying “we have 10000000 bit [key size](http://en.wikipedia.org/wiki/Key_size)“)

Providing precise details means having extensive documentation with theoretical and practical implications documenting ANY single way of how the algorithm works, how the protocol works with precise specification to replicate it for interoperability testing.  
It means that scientific community should be able to play with the technology, audit it, hack it.  
If we don’t know anything about the cryptographic system in details, how can we know which are the weakness and strength points?

Mike Fratto, Site editor of Network Computing, made a great article on [“Saying NO to proprietary cryptographic systems”](http://www.networkcomputing.com/data-protection/just-say-no-to-proprietary-cryptographic-algorithms.php) .  
Cerias Purdue University [tell this](http://www.cerias.purdue.edu/site/blog/post/security_through_obscurity/).

## b - NON peer reviewed and NON scientifically approved Cryptography does not work

In any case and in any condition you do cryptography you need to be sure that someone else will check, review, analyze, distruct and reconstract from scratch your technology and provide those information free to the public for open discussion.  
That’s exactly how AES was born and like [US National Institute of Standard make crypto does](http://www.networkworld.com/news/2007/012307-nist-cryptographic-algorithm.html) (with public contest with public peer review where only the best evaluated win).  
A public discussion with a public contest where the a lot of review by most famous and expert cryptographer in the world, hackers (with their name,surname and face, not like Notrax) provide their contribution, tell what they thinks.  
That’s called “peer review”.

If a cryptographic technology has an extended and important peer review, distributed in the world coming from universities, private security companies, military institutions, hackers and all coming from different part of the world (from USA to Europe to Russia to South America to Middle east to China) and all of them agree that a specific technology it’s secure…  
Well, in that case we can consider the technology secure because a lot of entities with good reputation and authority coming from a lot of different place in the world have publicly reviewed, analyzed and confirmed that a technology it’s secure.

How a private company can even think to invent on it’s own a secure communication protocol when it’s scientifically stated that it’s not possible to do it in a “proprietary and closed way” ?  
[IBM tell you that peer review it’s required for cryptography](http://www.ibm.com/developerworks/library/s-crypt04.html).  
[Bruce Schneier tell you](http://www.schneier.com/essay-037.html) that “Good cryptographers know that nothing substitutes for extensive peer review and years of analysis.”  
Philip Zimmermann will tell you to [beware of Snake Oil](https://philzimmermann.com/EN/essays/SnakeOil.html) where the story is: “Every software engineer fancies himself a cryptographer, which has led to the proliferation of really bad crypto software.”

## c - Closed source cryptography does not work

As you know any kind of “serious” and with “good reputation” cryptographic technology is implemented in opensource.  
There are usually multiple implementation of the same cryptographic algorithm and cryptographic protocol to be able to review all the way it works and certify the interoperability.  
Supposing to use a standard with precise and extended details on “how it works”, that has been “peer reviewed” by the scientific community BUT that has been re-implemented from scratch by a not so smart programmer and the implementation it’s plenty of bugs.

Well, if the implementation is “opensource” this means that it can be reviewed, improved, tested, audited and the end user will certaintly have in it’s own had a piece of technology “that works safely” .

[Google release opensource crypto toolkit](http://blogs.zdnet.com/security/?p=1684)  
[Mozilla release opensource crypto toolkit](http://www.mozilla.org/projects/security/pki/)  
[Bruce Schneier tell you that Cryptography must be opensource](http://www.schneier.com/crypto-gram-9909.html#OpenSourceandSecurity).

## Another cryptographic point of view

I don’t want to convince anyone but just provide facts related to science, related to cryptography and security in order to reduce the effect of misinformation done by security companies whose only goes is to sell you something and not to do something that make the world a better.

When you do secure products, if they are not done following the proper approach people could die.  
It’s absolutely something irresponsible not to use best practice to do crypto stuff.

To summarize let’s review the infosecurityguard.com review from a security best pratice point of view.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Product name** | **Security Trough Obscurity** | **Public peer review** | **Open Source** | **Compromise locally?** |
| Caspertec | **Obscurity** | No public review | **Closed** | Yes |
| CellCrypt | **Obscurity** | No public review | **Closed** | Yes |
| Cryptophone | **Transparency** | Limited public review | **Public** | Yes |
| Gold-Lock | **Obscurity** | No public review | **Closed** | Yes |
| Illix | **Obscurity** | No public review | **Closed** | Yes |
| No1.BC | **Obscurity** | No public review | **Closed** | Yes |
| PhoneCrypt | **Obscurity** | No public review | **Closed** | Yes |
| Rode&Swarz | **Obscurity** | No public review | **Closed** | Yes |
| Secure-Voice | **Obscurity** | No public review | **Closed** | Yes |
| SecuSmart | **Obscurity** | No public review | **Closed** | Yes |
| SecVoice | **Obscurity** | No public review | **Closed** | Yes |
| SegureGSM | **Obscurity** | No public review | **Closed** | Yes |
| SnapCell | **Obscurity** | No public review | **Closed** | Yes |
| Tripleton | **Obscurity** | No public review | **Closed** | Yes |
| Zfone | **Transparency** | Public review | **Open** | Yes |
| ZRTP | **Transparency** | Public review | **Open** | Yes |

\*Green means that it match basic requirement for a cryptographic secure system

\* Red / Broken means that it does not match basic requirement for a cryptographic secure system

That’s my analysis using a evaluation method based on cryptographic and security parameters not including the local compromise context that i consider useless.

However, to be clear, those are only basic parameters to be used when considering a voice encryption product (just to avoid being in a situation that appears like i am promoting other products). So it may absolutely possible that a product with good crypto (**transparency, peer reviewed and opensource)** is absolutely a not secure product because of whatever reason (badly written, not usable causing user not to use it and use cleartext calls, politically compromised, etc, etc).  
I think i will prepare a broader criteria for voice crypto technologies and voice crypto products, so it would be much easier and much practical to have a full transparent set of criterias to evaluate it.

But those are really the basis of security to be matched for a good voice encryption system!  
Read some useful past slides on [security protocols used in voice encryption systems](http://www.slideshare.net/fpietrosanti/2009-voice-security-and-privacy-security-summit-milan) (2nd part).

Now read below some more practical doubt about their research.

## The security concept of the review is misleading: any hacked device can be always intercepted!

I think that the guys completely missed the point: **ANY KIND OF SOFTWARE RUNNING ON A COMPROMISED OPERATING SYSTEM CAN BE INTERCEPTED**

Now they are pointing out that also Zfone from Philip Zimmermann is broken (a pc software), just because they install a trojan on a PC like in a mobile phone?  
Any security software rely on the fact that the underlying operating system is somehow trusted and preserve the integrity of the environment where the software run.

- If you have a disk encryption system but your PC if infected by a trojan, the computer is already compromised.
- If you have a voice encryption system but your PC is infected by a trojan, the computer is already compromised.
- If you have a voice encryption system but your mobile phone is infected by a trojan, the mobile phone is already compromised.

No matter which software you are running, in such case the security of your operating environment is compromised and in one way or another way all the information integrity and confidentiality is compromised.

Like i explained above how to intercept PhoneCrypt.

The only things that can protect you from this threat is running in a closed operating system with Trust Computing capability, implementing it properly.  
For sure on any “Open” operating system such us Windows, Windows Mobile, Linux, iPhone or Android there’s no chance to really protect a software.  
On difficult operating system such as Symbian OS or RimOS maybe the running software can be protected (at least partially)

That’s the reason for which the security concept that guys are leveraging to carry on their marketing campaign has no clue.  
It’s just because they control the environment, they know [Flexispy](http://www.flexispy.com/) software and so they adjusted their software not to be interceptable when Flexispy is installed.  
If you develop a trojan with the other techniques i described above you will 100% intercept PhoneCrypt.

On that subject also [Dustin Tamme](http://dtrammell.wordpress.com/)l, Security researcher of [BreakPoint Systems](http://www.breakingpointsystems.com/), pointed on on VoIP Security Alliance mailing lists that the [security analysis is based on wrong concepts](http://voipsa.org/pipermail/voipsec_voipsa.org/2010-January/003093.html).

## The PhoneCrypt can be intercepted: it’s just that they don’t wanted to tell you!

PhoneCrypt can be intercepted with “on device spyware”.  
**Why?** Because Windows Mobile is an unsecure operating environment and PhoneCrypt runs on Windows Mobile.  
Windows Mobile does not use Trusted Computing and so any software can do anything.  
The platform choice for a secure telephony system is important.  
**How?** I quickly discussed with some knowledgeable windows mobile hackers about 2 different way to intercept PhoneCrypt with an on-device spyware (given the unsecure Windows Mobile Platform).

**a) Inject a malicious DLL into the software and intercept from within the Phonecrypt itself.**

In Windows Mobile any software can be subject to DLL code injection.

What an attacker can do is to inject into the PhoneCrypt software (or any software running on the phone), hooking the Audio related functions acting as a “function proxy” between the PhoneCrypt and the real API to record/play audio.

It’s a matter of “hooking” only 2 functions, the one that record and the one that play audio.

Read the official Microsoft documentation on [how to do DLL injection on Windows Mobile processes.](http://msdn.microsoft.com/en-us/library/aa909244.aspx) or forum discussing the technique of injecting DLL on windows mobile processes.

That’s simple, any programmer will tell you to do so.

They simply decided that’s better not to make any notice about this.

**b) Create a new audio driver that simply act as a proxy to the real one and intercept PhoneCrypt**

In Windows Mobile you can create new Audio Drivers and new Audio Filters.

What an attacker can do is to load a new audio driver that does not do anything else than passing the real audio driver function TO/FROM the realone. In the meantime intercept everything recorded and everything played :-)

Here there is an example on how to do [Audio driver for Windows Mobile](http://blogs.msdn.com/medmedia/archive/2007/01/03/windows-ce-audio-driver-samples.aspx) .

Here a software that implement what i explain here for Windows [“Virtual Audio Cable”](http://software.muzychenko.net/eng/vac.html) .

The very same concept apply to Windows Mobile. Check the book [“Mobile Malware Attack and Defense”](http://books.google.com/books?id=Nd1RcGWMKnEC&pg=PT306&lpg=PT306&dq=PerformCallback4+%22and+defense%22&source=bl&ots=81c3xmKbA7&sig=5mlstFtcqOtIsp5f_oAR3tEmPrA&hl=en&ei=gmxjS9nTGpDL_Qb1haXoAw&sa=X&oi=book_result&ct=result&resnum=1&ved=0CAcQ6AEwAA#v=onepage&q=&f=false) at that link explaining techniques to play with those techniques.

They simply decided that’s better not to make any notice to that way of intercepting phone call on PhoneCrypt .

Those are just 2 quick ideas, more can be probably done.

## Sounds much like a marketing activity - Not a security research.

I have to tell you. I analyzed the issue very carefully and on most aspects. All this things about the voice encryption analisys sounds to me like a marketing campaign of SecurStar GmbH to sell PhoneCrypt and gain reputation. A well articulated and well prepared campaign to attract the media saying, in an indirect way cheating the media, that PhoneCrypt is the only one secure. You see the [press releases of SecurStar and of the “Security researcher Notrax telling that PhoneCrypt is the only secure product”](http://www.businesswire.com/portal/site/home/permalink/?ndmViewId=news_view&newsId=20100127005098&newsLang=en) . SecurStar PhoneCrypt is the only product the anonymous hacker “Notrax” consider secure of the “software solutions”.  
The only “software version” in competition with:

- [SnapCell](http://www.snapshield.com/) - No one can buy it. A security company that does not even had anymore a webpage. The company does not almost exist anymore.

- [rohde-schawarz](http://www2.rohde-schwarz.com/) - A company that have in his list price and [old outdated hardware secure phone](http://www2.rohde-schwarz.com/en/products/secure_communications/voice_and_data_encryption/TopSec_GSM.html) . No one would buy it, it’s not good for genera use.

Does it sounds strange that only those other products are considered secure along with PhoneCrypt .

Also… let’s check the kind of multimedia content in the different reviews available of [Gold-Lock,](http://infosecurityguard.com/?p=85) [Cellcrypt](http://infosecurityguard.com/?p=140) and [Phonecrypt](http://infosecurityguard.com/?p=116) in order to understand how much the marketing guys pressed to make the PhoneCrypt review the most attractive:

|  |  |  |  |
| --- | --- | --- | --- |
| **Application** | **Screenshots of application** | **Video with demonstration of interception** | **Network demonstration** |
| **PhoneCrypt** | **5** | **0** | **1** |  |
| **CellCrypt** | **0** | **2** | **0** |
| **GoldLock** | **1** | **2** | **0** |

It’s clear that PhoneCrypt is reviewed showing more features explicitly shown and major security features product description than the other.

## Too much difference between them, should we suspect it’s a marketing tips?

But again other strange things analyzing the way it was done…  
If it was “an impartial and neutral review” we should see good and bad things on all the products right?

Ok, see the table below regarding the opinion indicated in **each paragraph** of the different reviews available of Gold-Lock, CellCrypt and Phonecrypt (are the only available) to see if are positive or negative.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Application** | **Number of paragraphs** | **Positive paragraphs** | **Negative paragraphs** | **Neutral paragraphs** |
| **PhoneCrypt** | **9** | **9** | **0** | **0** |
| **CellCrypt** | **12** | **0** | **10** | **2** |
| **GoldLock** | **9** | **0** | **8** | **1** |

Detailed paragraphs opinion analysis of [Phonecrypt](http://infosecurityguard.com/?p=116)

|  |  |
| --- | --- |
| **Paragraph of review** | **Opinion expressed** |
| **From their website** | **Positive Marketing feedback** |
| **Apple iPhone** | **Positive Marketing feedback** |
| **Disk Encryption or voice Encryption** | **Positive Marketing feedback** |
| **PBX Compatibility? Really** | **Positive Marketing feedback** |
| **Cracking <10. Not.** | **Positive Marketing feedback** |
| **Good thinking!** | **Positive Marketing feedback** |
| **A little network action** | **Positive Marketing feedback** |
| **UI** | **Positive Marketing feedback** |
| **Good Taste** | **Positive Marketing feedback** |

Detailed paragraphs opinion analysis of [Gold-Lock 3G](http://infosecurityguard.com/?p=85)

|  |  |
| --- | --- |
| **Paragraph of review** | **Opinion expressed** |
| **From their website** | **Negative Marketing feedback** |
| **Licensed by The israeli Ministry of Denfese** | **Negative Marketing feedback** |
| **Real Company or Part Time hobby** | **Negative Marketing feedback** |
| **16.000 bit authentication** | **Negative Marketing feedback** |
| **DH 256** | **Negative Marketing feedback** |
| **Downad & Installation!** | **Neutral Marketing feedback** |
| **Cracking it <10** | **Negative Marketing feedback** |
| **Marketing BS101** | **Negative Marketing feedback** |
| **Cool video stuff** | **Negative Marketing feedback** |

Detailed paragraphs opinion analysis of [CellCrypt](http://infosecurityguard.com/?p=140)

|  |  |
| --- | --- |
| **Paragraph of review** | **Opinion expressed** |
| **From their website** | **Neutral Marketing feedback** |
| **A little background about cellcrypt** | **Negative Marketing feedback** |
| **Master of Marketing** | **Negative Marketing feedback** |
| **Secure Voice calling** | **Negative Marketing feedback** |
| **Who’s buying their wares** | **Negative Marketing feedback** |
| **Downad & Installation!** | **Neutral Marketing feedback** |
| **My Demo environment** | **Negative Marketing feedback** |
| **Did they forget some code** | **Negative Marketing feedback** |
| **Cracking it <5** | **Negative Marketing feedback** |
| **Room Monitoring w/ FlexiSpy** | **Negative Marketing feedback** |
| **Cellcrypt unique features..** | **Negative Marketing feedback** |
| **Plain old interception** | **Negative Marketing feedback** |
| **The Haters out there** | **Negative Marketing feedback** |

Now it’s clear that from their point of view on PhoneCrypt there is no single bad point while the other are always described in a negative way.  
No single good point. Strange?  
All those considerations along with the next ones really let me think that’s **very probably** **a marketing review** **and not an independent review.**

## Other similar marketing attempt from SecurStar

SecurStar GmbH is known to have used in past marketing activity leveraging this kind of “technical speculations”, abusing of partial information and fake unconfirmed hacking stuff to make marketing/media coverage.  
Imho a rare mix of unfairness in leveraging the difficult for people to really understand the complexity of security and cryptography.

They already used in past Marketing activities like the one about creating a trojan for Windows Mobile and saying that their software is secure from the trojan that they wrote.  
[Read about their marketing tricks of 2007](http://www.prnewswire.co.uk/cgi/news/release?id=184415)

They developed a Trojan (RexSpy) for Windows Mobile, made a demonstration capability of the trojan and later on told that they included “Anti-Trojan” capability to their PhoneCrypt software.They never released informations on that trojan, not even proved that it exists.

The researcher Collin Mulliner told at that time that [it sounds like a marketing tips](http://www.mulliner.org/blog/blosxom.cgi/index.html?find=rexspy&plugin=find&path=) (also because he was not able to get from SecurStar CEO Hafner any information about that trojan):

“This makes you wonder if this is just a marketing thing.”

Now, let’s try to make some logical reassignment.  
It’s part of the way they do marketing, an very unfriendly and unpolite approach with customers, journalist and users trying to provide wrong security concepts for a market advantage. Being sure that who read don’t have all the skills to do in depth security evaluation and find the truth behind their marketing trips.

## Who is the hacker notrax?

It sounds like a camouflage of a fake identity required to have an “independent hacker” that make an “independent review” that is more strong on reputation building.  
Read about his bio:

¾ Human, ¼ Android (Well that would be cool at least.) I am just an enthusiast of pretty much anything that talks binary and if it has a RS232 port even better. During the day I masquerade as an engineer working on some pretty cool projects at times, but mostly I do the fun stuff at night. I have been thinking of starting an official blog for about 4.5 years to share some of the things I come across, can’t figure out, or just cross my mind. Due to my day job and my nighttime meddling, I will update this when I can. I hope some find it useful, if you don’t, well you don’t.

There are no information about this guy on google.  
Almost any hacker that get public have articles online, post in mailing archive and/or forum or some result of their activity.  
For notrax, nothing is available.

Additionally let’s look at the domain…  
The domain infosecurityguard.com is privacy protected by domainsbyproxy to prevent understanding who is the owner.  
The domain has been created 2 months ago on 01-Dec-09 on godaddy.com registrar.

What’s also very interesting to notice that this “unknown hacker with no trace on google about him that appeared on December 2009 on the net” is referred on [SecurStar GmbH Press Release](http://www.businesswire.com/portal/site/home/permalink/?ndmViewId=news_view&newsId=20100127005098&newsLang=en) as a “An IT security expert”.

Maybe they “know personally” who’s this anonymous notrax? :)

Am i following my own conspiracy thinking or maybe there’s some reasonable doubt that everything was arrange in that funny way just for a marketing activity?

## Social consideration

If you are a security company you job have also a social aspects, you should also work to make the world a better place (sure to make business but “not being evil”). You cannot cheat the skills of the end users in evaluating security making fake misleading information.

You should do awareness on end users, to make them more conscious of security issues, giving them the tools to understand and decide themselves.

Hope you had fun reading this article and you made your own consideration about this.

Fabio Pietrosanti (naif)

p.s. Those are my personal professional opinion, let’s speak about technology and security, not marketing.  
p.p.s. i am not that smart in web writing, so sorry for how the text is formatted and how the flow of the article is unstructured!
