---
title: "Gold-Lock Security Encryption Contest: be careful!"
url: https://infosecurity.ch/20091125/gold-lock-security-encryption-contest-be-careful/
date: 2009-11-25
author: Fabio Pietrosanti (naif)
language: en
tags: [cyberwarfare, mobile, privacy, voicesecurity]
---

# Gold-Lock Security Encryption Contest: be careful!

This post is to talk about the “unfair” marketing approach of Gold-Lock, an israeli company doing mobile voice encryption authorized by Israeli Ministry of Defence .

Following an announcement seen on Linkedin “Information Security Community” group:

> # GoldLock is offering US$ 100.000 and a job for an unencryption
>
> GoldLock, an israeli encryption and security company is offering US$ 100.000 and a job to anyone capable to decrypt a cellular conversation contained in a file provided in their site ( [https://www.gold-lock.com/app/en/?wicket:interface=:8](http://www.linkedin.com/redirect?url=https%3A%2F%2Fwww%2Egold-lock%2Ecom%2Fapp%2Fen%2F%3Fwicket%3Ainterface%3D%3A8&urlhash=ZzHD "New window will open") ::::).  
> The transcription must be sent back to GoldLock until February 1st, 2010.  
> The contest is open to all and any tools or technology may be used.  
> Good luck to all!!!

I commented:

> ### Not having a public protocol specification is not even scientifically serious to make a marketing tricks like this. I would say to gold-lock, let’s release the source code and let anyone compile the cryptographic engine if you trust not to to have something nasty inside… ;)

[Toni Koivunen](http://www.linkedin.com/profile?viewProfile=&key=550607&authToken=Kwcr&authType=name) from [F-secure](http://www.f-secure.com/) said:

> ### So… They will pay $100k if you get through the AES and the hassle with keys. If someone would pull it off they would certainly make a truckload more money elsewhere. Plus they would retain the rights to the code/technology that they created, which isn’t the case if they go for the $100k since the License pretty clearly says that: # An assignment letter to Gold Line, in a form satisfactory to Gold Line of your technology and the Work Plan (the “Technology”). Such assignment form shall enable Gold Line to transfer the rights on the Technology to Gold Line, including the right to register patents and all other rights. # A release and waiver form, in a form satisfactory to Gold Line, duly executed by you and any other participant of any rights to the Technology. Plus of course Gold Line retains the right to change the rules of the game with prior notice. Or needing to notify afterwards either. Sounds fair :)

[Michel Scovetta](http://www.linkedin.com/profile?viewProfile=&key=1485774&authToken=uadD&authType=name) from [Computer Associates](http://www.ca.com/) said:

> ### It sounds like the purpose of this is to get some cheap testing out of it, and to be able to say something like, “The best crypto experts in the world tried to break it, and were unable to.” According to some of the docs on Gold Lock’s website, they use ECC-256 and a “modified DH key exchange” (which tingles my spidey senses), SHA-256, and then XOR for the actual data encryption. They use practically blasphemous language like, “Each component of the Gold Lock Enterprise solution is tested and proven secure against any conceivable attack.” \*Proven\* secure? \*Any conceivable\* attack? Yikes! In another doc on their site, they talk about their first layer relying on 1024-bit RSA. GoDaddy doesn’t even allow 1024-bit keys to be used anymore when generating $20 SSL certificates. They quote 300 billion MIPS-years to break, but if my math is correct, that comes down to about 52 days on the top supercomputer right now. Not trivial, but this is an offline attack, so time is on the side of the attacker. The description then talks about the device generating 16k keys when you register the device. If the protocol is “secure”, then it should be “secure” with only a single key. If it’s not secure with a single key, then generating 16k keys could only make it 16k times more secure, which is far off from a proof of security. I agree with Fabio - a fair contest would be to include source code and the cryptographic specification. Also, as other contests have proven (e.g. SecureWebMail), the weakest point isn’t usually the cryptography. It’s all of the other stuff, and it doesn’t look like any of it is being disclosed for the contest. [http://xkcd.com/538/](http://www.linkedin.com/redirect?url=http%3A%2F%2Fxkcd%2Ecom%2F538%2F&urlhash=tsuz "New window will open") Mike

I would say that all those considerations from security experts from well known and established security companies bring us to consider that:

- Gold-lock is not transparent on their encryption at all and they work trough bad practice of [Security Trough Obscurity](http://en.wikipedia.org/wiki/Security_through_obscurity) (no one know what’s inside the product)
- Gold-lock is not playing a fair game by proposing this ‘security contest’
- Gold-lock being certified by Israeli ministry of defence may raise doubt related to possible relationship with the intelligence… Read by post [Certified by Israeli MInistry of Defense](https://infosecurity.ch/).

Voice security is a sensible matters and lacks of transparency and governmental relationship for cryptographic choices usually does not provide anything good…

Think about it…
