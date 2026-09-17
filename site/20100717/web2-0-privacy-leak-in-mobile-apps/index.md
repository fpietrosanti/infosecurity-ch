---
title: "Web2.0 privacy leak in Mobile apps"
url: https://infosecurity.ch/20100717/web2-0-privacy-leak-in-mobile-apps/
date: 2010-07-17
author: Fabio Pietrosanti (naif)
language: en
tags: [hacking, mobile, policy, privacy]
---

# Web2.0 privacy leak in Mobile apps

You know that web2.0 world it’s plenty of leak of any kind (profiling, profiling, profiling) related to Privacy and users starts [being concerned](http://www.bit-tech.net/columns/2006/06/03/web_2_privacy/) about it.

Users continuously download applications without knowing the details of what they do, for example [iFart](http://ifartmobile.com/ifart-top-20-paid-app/) just because are cool, are fun and sometime are useful.

On mobile phones users install from 1000% up to 10.000% more applications than on a PC, and those apps [may contain malware](http://news.cnet.com/8301-27080_3-10446402-245.html) or other unexpected functionalities.

Recently infobyte analyzed [ubertwitter client](http://www.ubertwitter.com/) and discovered that the client was leaking and sending to their server many personal and sensitive data such as:

- Blackberry PIN

- Phone Number

- Email Address

- Geographic positioning information

Read about UbertTwitter [‘spyware’ features discovery here](http://blog.infobytesec.com/2010/07/ubertwitter-your-secret-spy.html) by [infoByte](http://www.infobytesec.com/) .

It’s plenty of applications leaking private and sensitive information but just nobody have a look at it.

Should mandatory [data retention and privacy policies](http://www.sans.org/reading_room/whitepapers/backup/electronic-data-retention-policy_514) became part of application development and submission guideline for mobile application?

Imho a users must not only be warned about the application capabilities and API usage but also what will do with which kind of information it’s going to handle inside the mobile phone.

Capabilities means authorizing the application to use a certain functionalities, for example to use GeoLocation API, but what the application will do and to who will provide such information once the user have authorized it?

That’s a security profiling level that mobile phone manufacturer does not provide and they should, because it focus on the information and not on the application authorization/permission respect to the usage of device capabilities.

p.s. yes! ok! I agree! This kind of post would require 3-4 pages long discussion as the topic is hot and quite articulated but it’s saturday morning and i gotta go!
