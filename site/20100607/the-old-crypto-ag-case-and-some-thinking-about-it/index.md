---
title: "The (old) Crypto AG case and some thinking about it"
url: https://infosecurity.ch/20100607/the-old-crypto-ag-case-and-some-thinking-about-it/
date: 2010-06-07
author: Fabio Pietrosanti (naif)
language: en
tags: [cyberwarfare, encryption, policy, voicesecurity]
---

# The (old) Crypto AG case and some thinking about it

In the ’90, closed source and proprietary cryptography was ruling the world.

That’s before open source and scientifically approved encrypted technologies went out as a best practice to do crypto stuff.

I would like to remind when, in 1992, USA along with Israel was, together with switzerland, providing backdoored (proprietary and secret) technologies to Iranian government to tap their communications, cheating them to think that the used solution was **secure**, making also some consideration on this today in 2010.

![caq63crypto.t.jpg](https://infosecurity.ch/wp-content/uploads/2010/06/caq63crypto.t.jpg)

That’s called [The Crypto AG case](http://mediafilter.org/CAQ/caq63/caq63madsen.html), an historical fact involving the United States [National Security Agency](http://www.nsa.gov/) along with Signal Intelligence Division of [Israel Ministry of Defense](http://www.mod.gov.il/) that are strongly suspected to had made an agreement with the Swiss cryptography producer company [Crypto AG](http://en.wikipedia.org/wiki/Crypto_AG).

Basically those entities placed a backdoor in the **secure** crypto equipment that they provided to Iran to intercept Iranian communications.

Their crypto was based on secret and proprietary encryption algorithms developed by Crypto AG and eventually customized for Iranian government.

You can read some other facts about Crypto AG backdoor related issues:

[The demise of global telecommunication security](http://onlinejournal.org/Special_Reports/092105Madsen/092105madsen.html)

[The NSA-Crypto AG sting](http://english.ohmynews.com/ArticleView/article_view.asp?no=381337&rel_no=1)

[Breaking codes: an impossible task?](http://news.bbc.co.uk/2/hi/technology/3804895.stm) By [BBC](http://bbc.com/)

[Der Spiegel Crypto AG (german) article](http://jya.com/cryptoag.htm)

Now, in 2010, we all know and understand that secret and proprietary crypto does not work.

Just some reference by top worldwide cryptographic experts below:

[Secrecy, Security, Obscurity](http://www.schneier.com/crypto-gram-0205.html) by [Bruce Schneier](http://www.schneier.com/)

[Just say No to Proprietary cryptographic Algorithms](http://www.networkcomputing.com/data-protection/just-say-no-to-proprietary-cryptographic-algorithms.php) by Network Computing (Mike Fratto)

[Security Through Obscurity](http://www.cerias.purdue.edu/site/blog/post/security_through_obscurity/) by [Ceria Purdue University](http://www.cerias.purdue.edu/)

[Unlocking the Secrets of Crypto: Cryptography, Encryption and Cryptology explained](http://www.symantec.com/connect/articles/unlocking-secrets-crypto) by Symantec

Time change the way things are approached.

I like very much the famous [Philip Zimmermann](http://www.philzimmermann.com/) assertion:

> “Cryptography used to be an obscure science, of little relevance to everyday life. Historically, it always had a special role in military and diplomatic communications. But in the Information Age, cryptography is about political power, and in particular, about the power relationship between a government and its people. It is about the right to privacy, freedom of speech, freedom of political association, freedom of the press, freedom from unreasonable search and seizure, freedom to be left alone.”

Any scientist today accept and approve the *[Kerckhoffs’ Principle](http://en.wikipedia.org/wiki/Kerckhoffs%27_principle) that in 1883 in the [Cryptographie Militaire](http://www.petitcolas.net/fabien/kerckhoffs/la_cryptographie_militaire_i.htm) paper stated:*

> **The security of a cryptosystem should not depend on keeping the algorithm secret, but only on keeping the numeric key secret.**

It’s absolutely clear that the best practice for doing cryptography today obbly any serious person to do open cryptography, subject to public review and that follow the Kerckhoff principle.

So, what we should think about closed source, proprietary cryptography that’s based on security trough obscurity concepts?

I was EXTREMELY astonished when TODAY, in 2010, in the age of information society i read some paper on [Crypto AG](http://www.crypto.ch/) website.

I invite all to read the Crypto AG security paper called **[Sophisticated Security Architecture designed by Crypto AG](http://www.crypto.ch/fileadmin/01_crypto/Broschueren/Sec_Arch_broch_EN.pdf)** of which you can get a significant excerpt below:

> The design of this architecture **allows Crypto AG to provide a secret proprietary algorithm** that can be specified for each customer to assure the perfect degree of cryptographic security and optimum support for the customer’s security policy. In turn, the Security Architecture gives you the influence you need to be fully independent in respect of your encryption solution. You can determine all areas that are covered by cryptography and verify how the algorithm works.**The original secret proprietary algorithm of Crypto AG is the foundation of the Security Architecture**.

I have to say that their architecture is absolutely good from TLC point of view. Also they have done a very good job in making the design of the overall architecture in order to make a tamper-proof resistant crypto system by using dedicated [crypto processor](http://en.wikipedia.org/wiki/Secure_cryptoprocessor).  
However there is still something missing:

> T**he overall cryptographic concept is misleading, based on wrong encryption concepts**.

You may think that i am a troll telling this, but given the history of Crypto AG and given the fact that **all the scientific and security community does not approve security trough obscurity concepts**, it would legitimate to ask ourself:

Why they are still doing **security trough obscurity cryptography** with **secret and proprietary algorithms**?

Hey, i think that they have very depth knowledge on telecommunication and security, but given that the science tell us not to follow the secrecy of algorithms, i really have **serious doubt on why they are still providing proprietary encryption** and does not move to standard solutions (eventually with some kind of custom enhancement).
