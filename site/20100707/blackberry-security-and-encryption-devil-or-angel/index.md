---
title: "Blackberry Security and Encryption: Devil or Angel?"
url: https://infosecurity.ch/20100707/blackberry-security-and-encryption-devil-or-angel/
date: 2010-07-07
author: Fabio Pietrosanti (naif)
language: en
tags: [business, encryption, hacking, mobile, privacy]
---

# Blackberry Security and Encryption: Devil or Angel?

Blackberry have good and bad reputation regarding his security capability, depending from which angle you look at it.

This post it’s a summarized set of information to let the reader the get picture, without taking much a position as RIM and Blackberry can be considered, depending on the point of view, an **extremely secure platform** or an **extremely dangerous one** .

[![bblock.jpg](https://infosecurity.ch/wp-content/uploads/2010/07/bblock-tm.jpg)](https://infosecurity.ch/wp-content/uploads/2010/07/bblock.jpg)

Let’s goes on.

On one side Blackberry it’s a platform plenty of encryption features, security features everywhere, device encrypted (with custom crypto), communication encrypted (with [custom proprietary protocols](http://docs.blackberry.com/en/admin/deliverables/16558/RIM_propietary_protocols_1107871_11.jsp) such as IPPP), very good Advanced Security Settings, Encryption framework from [Certicom](http://www.certicom.com/) ([now owned by RIM](http://www.digitalcommunitiesblogs.com/international_beat/2009/02/certicom-may-be-a-prized-posse.php)).

On the other side they does not provide only a device but an overlay access network, called BIS ([Blackberry Internet Service](http://docs.blackberry.com/en/smartphone_users/deliverables/16059/BlackBerry_Internet_Service-User_Guide-T987396-1026956-0510121134-001-3.1-US.pdf)), that’s a global worldwide wide area network where your blackberry enter while you browse or checkmail using **blackberry.net** AP.

When you, or an application, use the **blackberry.net** APN you are not just connecting to the internet with the carrier internet connection, but you are entering inside the RIM network that will proxy and act as a [gateway to reach the internet.](#)

The very same happen when you have a corporate use: Both the BB device and the corporate BES connect to the RIM network that act as a sort of [vpn concentration network](#).

So basically all the communications cross trough RIM service infrastructure in encrypted format with a set proprietary encryption and communication protocols.

Just as a notice, think that google to provide gtalk over **blackberry.net** APN, made an agreement in order to offer service inside the BB network to the BB users. When you install gtalk you get added 3 **[service books](http://www.mahalo.com/how-to-get-a-blackberry-service-book)** that point to [GTALKNA01](http://www.blackberryforums.com/general-blackberry-discussion/28639-google-talk-blackberry-now-available.html) that’s the name of GTALK gateway inside the RIM network to allow intra-BIS communication and act as a GTALK gateway to the internet.

The mobile operators usually are not even allowed to inspect the traffic between the Blackberry device and the Blackberry Network.

So RIM and Blackberry are somehow unique for their approach as they provide a platform, a network and a service all bundled together and you cannot just “get the device and the software” but the user and the corporate are always bound and connected to the service network.

That’s good and that’s bad, because it means that RIM provide extremely good security features and capabilities to protect information, device and access to information at various level **against third party**.

But it’s always difficult to estimate the threat and risk related to RIM itself and who could make political pressure against RIM.

Please consider that i am not saying “RIM is looking at your data” but making an objective risk analysis: for how the platform is done RIM have authority on the device, on the information on-the-device and on the information that cross the network. (Read my [Mobile Security Slides](http://www.slideshare.net/fpietrosanti/2010-mobile-security-whymca-developer-conference)).

For example let’s consider the very same context for Nokia phones.

Once the Nokia device is sold, Nokia does not have authority on the device, nor on the information on-the-device nor on the information that cross the network. But it’s also true that Nokia just provide the device and does not provide the value added services such as the Enterprise integration (The RIM VPN tunnel), the BIS access network and all the local and remote security provisioned features that Blackberry provide.

So it’s a matter of considering the risk context in the proper way when choosing the platform, with an example very similar to choosing Microsoft Exchange Server (on your own service) or whether getting a SaaS service like Google Apps.

In both case you need to trust the provider, but in first example you need to trust Microsoft that does not put a backdoor on the software while in the 2nd example you need to trust Google, as a platform and service provider, that does not access your information.

So it’s a different paradigm to be evaluated depending on your threat model.

If your threat model let you consider RIM as a trusted third party service provider (much like google) than it’s ok. If you have a very high risk context, like top-secret one, then let’s consider and evaluate carefully whether it’s not better to keep the Blackberry services fully isolated from the device or use another system without interaction with manufacturer servers and services.

Now, let’s get back to some research and some facts about blackberry and blackberry security itself.

First of all several governments had to deal with RIM in order to force them to provide access to the information that cross their service networks while other decided to directly ban Blackberry usage for high officials because of servers located in UK and USA, while other decided to install their own backdoors.

- [**Russian Secret Services** (FSB) reach an agreement with RIM and now FSB can eavesdrop Blackberry email and web traffic](http://www.mobilemarketingmagazine.co.uk/content/blackberry-debuts-russia?quicktabs_1=0) in Russia
- [**French Government** banned Blackberry for use by Government officials](http://www.pcworld.com/businesscenter/article/133198/security_concerns_prompt_french_blackberry_ban.html) and also [replaced the device for voice encryption use](http://www.phonearena.com/htmls/French-President-receiving-a-new-encrypted-phone-after-a-BlackBerry-ban-article-a_8654.html)
- [**Indian government** made pressure on RIM to reduce encryption capabilities](http://www.informationweek.com/news/mobility/messaging/showArticle.jhtml?articleID=208403978) and later announced that they [have cracked blackberry encryption](http://www.zdnet.com/blog/security/indias-government-at-last-weve-cracked-blackberrys-encryption/1964) . A summary on [India-RIM story by Bruce Schneier](http://www.schneier.com/blog/archives/2008/05/blackberry_givi_1.html).
- **United Arab Emirates (UAE)** Etisalat operator [tried to silently install a government spyware on all country blackberry](http://internetthought.blogspot.com/2009/07/etisalat-and-ss8-hacking-your.html) but they got caught
- **USA** [National Security Agency](http://www.nsa.gov/) initially [prohibited Obama to use Blackberry](http://www.maclife.com/article/news/president_his_pda) for his presidential works giving him a [Sectera Edge Secure Phone](http://news.cnet.com/obamas-new-blackberry-the-nsas-secure-pda/), after 2 years they managed to secure it with a custom encryption layer done specifically by NSA and [allowed Obama to use a custom secured blackberry](http://www.blackberrycool.com/2009/01/22/obama-to-keep-his-blackberry-get-a-super-encryption/)

There’s a lot of discussion when the topics are RIM Blackberry and Governments for various reasons.

Below a set of official Security related information on RIM blackberry platform:

- Official [Security Knowledgebase](http://na.blackberry.com/eng/ataglance/security/knowledgebase.jsp) on RIM website
- [Blackberry Internet Service security features](http://docs.blackberry.com/en/smartphone_users/deliverables/14212/BlackBerry_Internet_Service-Security_Feature_Overview--787371-0205030634-001-3.0-US.pdf)
- [Wireless Data Security](http://na.blackberry.com/eng/ataglance/security/features.jsp)

And here a set of unofficial Security and Hacking related information on RIM Blackberry platform:

- Hackish blackbox security analysis by FX of [Phenoelit](http://www.phenoelit-us.org/):  [Analysing Complex Systems - The Blackberry case](http://www.phenoelit-us.org/stuff/AnalysingComplexSystems.pdf)
- Accessing corporate intranets trough [Blackberry BBProxy Hack](http://www.blackberrytoday.com/articles/2006/8/2006-8-9-BBProxy-Hack-Exposes.html)
- [Blackberry Master Control Program](http://www.geckoandfly.com/6398/how-to-hack-and-modify-blackberry-settings-with-master-control-program/) little bit of hacking
- How to [bypass Blackberry IT Policy](http://www.blackberryinsight.com/2008/03/16/howto-remove-blackberrys-it-policy/)
- Blackberry Reversing research (mostly by Dr Bolsen, however no one have ever decompiled and published the whole RIMOS)
- - [Bypassing Blackberry COD Signature](http://drbolsen.wordpress.com/2007/07/31/bypass-signature-requirement/)
- - [Reversing Blackberry](http://drbolsen.wordpress.com/2006/07/26/blackberry-cod-file-format/) The COD format
  - [Blackberry Internal Folders Layout](http://drbolsen.wordpress.com/2007/05/16/blackberry-internal-folders-layout/)
  - [Blackberry decompilated COD binaries](http://drbolsen.wordpress.com/2007/01/30/how-it-looks-like/)
  - [Blackberry Coddec decompilation tool release](http://drbolsen.wordpress.com/2008/07/14/coddec-released/)

Because it’s 23.32 (GMT+1), i am tired, i think that this post will end up here.

I hope to have provided the reader a set of useful information and consideration to go more in depth in analyzing and considering the overall blackberry security (in the good and in the bad, it always depends on your threat model!).

Cheers

Fabio Pietrosanti (naif)

p.s. i am managing security technology development (voice encryption tech) on Blackberry platform, and i can tell you that from the development point of view it’s absolutely better than Nokia in terms of compatibility and speed of development, but use only RIMOS 5.0+ !
