---
title: "SecurStar GmbH Phonecrypt answers on the Infosecurityguard/Notrax case: absolutely unreasonable! :-)"
url: https://infosecurity.ch/20100201/answer-of-securstar-gmbh-on-the-infosecurityguardnotrax-case-absolutely-unreasonable/
date: 2010-02-01
author: Fabio Pietrosanti (naif)
language: en
tags: [business, encryption, hacking, marketing, privacy, voicesecurity]
---

# SecurStar GmbH Phonecrypt answers on the Infosecurityguard/Notrax case: absolutely unreasonable! :-)

UPDATE 20.04.2010: http://infosecurityguard.com has been disabled. Notrax identity became known to several guys in the voice security environments (cannot tell, but you can imagine, i was right!) and so our friends decided to trow away the website because of legal responsibility under UK and USA laws.

UPDATE: Nice summary of the whole story (i know, it’s long and complicated to read at 1st time) on [SIPVicious VoIP security blog](http://sipvicious.org/blog/2010/02/on-breaking-phonecall-encryption-and.html) by [Sandro Gauci](http://enablesecurity.com/).

Following my discoveries, Mr. Hafner, SecurStar chief exec, tried to ultimately defend their actions, [citing absolutely unreasonable excuses](http://www.theregister.co.uk/2010/02/01/voice_crypto_test_row_phreak_out/) to The Reg instead of publicly apologizing for what they have done: creating a fake independent security research to promote their [PhoneCrypt product](http://www.securstar.com/products_phonecrypt.php).

He tried to convince us that the person behind IP **217.7.213.59,** used by the author of infosecurityguard.com and pointing to their office DSL line, was this hacker Notrax, using their anonymous surfing service and not one of their employees at their office:

“SecurStar chief exec Wilfried Hafner denied any contact with Notrax. Notrax, he said, must have been using his firm’s anonymous browsing service, SurfSolo, to produce the results reported by Pietrosanti”

Let’s reflect a moment on this sentence… Would really an hacker looking for anonymity spend 64 EUR to [buy their anonymity surfing service called surfsolo](http://www.securstar.com/products_ssolo.php) instead of using the free and much more secure [TOR (the onion router)](http://www.torproject.org/)?Then let’s reflect on this other piece of information:

- The IP **217.7.213.59** is SecurStar GmbH’s office DSL line
- On **217.7.213.59** they have installed their VoIP/Asterisk PBX and internet gateway
- ****They promote their anonymous proxy service for “Anonymous p2p use” (<http://www.securstar.com/products_ssolo.php>). Who would let users do p2p from the office dsl line where they have installed their corporate VoIP PBX ? If you do VoIP you can’t let third party flood your line w/ p2p traffic, your phone calls would became obviously unreliable (yes, yes, you can do QoS, but you would not place an anonymous navigation proxy on your company office DSL line…).****
- ****Which company providing an anonymous navigation service would ever use their own office IP address? Just think how many times you would have the police knocking at your door and your employees as the prime suspects. (In past i used to run a TOR node, i know the risks…). Also think how many times you would find yourself blacklisted on google as a spyware bot.****
- Mr. Hafner also says “We have two million people using this product. Or he may have been an old customer of ours”. 2M users on a DSL line, really?
- ****I don’t use Surfsolo service, however their proxies are probably these ones:****

**surfsolo.securstar.net - 67.225.141.74**

**surfsolo.securstar.com - 69.16.211.133**

Frankly speaking I can easily understand that Mr. Hafner is going do whatever he can to protect his company from the scandal, but the “anonymous proxy” excuse is at the very least suspicious.

How does the fact that the “independent research” was semantically a product review of PhoneCrypt, along with the discovery that the author come from the SecurStar GmbH IP address offices, along with the anonymity of this Notrax guy (SecurStar calls him a “well known it security professional” in their press release..) sound to you?

It’s possible that earth will get an attack from outer space that’s going to destroy our life?

Statistically extremely difficult, but yes, possible. More or less like the “anonymous proxy” story told by Mr. Hafner to cover the fact that they are the ones behind the infosecurityguard.com fake “independent security review”.

Hey, I don’t need anything else to convince myself or to let the smart person have his own thoughts on this.

I just think that the best way for SecurStar to get out of this mess would probably be to provide public excuses to the hacking community for abusing the name and reputation of real independent security researches, for the sake of a marketing stunt.

Regards,

Fabio Pietrosanti

p.s. I am currently waiting for some other infos that will more precisely confirm that what Mr. Hafner is saying is not properly true. Stay tuned.
