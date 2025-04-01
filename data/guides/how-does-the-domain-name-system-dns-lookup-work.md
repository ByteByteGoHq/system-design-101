---
title: "How Does the Domain Name System (DNS) Lookup Work?"
description: "Learn how DNS translates domain names to IP addresses for web access."
image: "https://assets.bytebytego.com/diagrams/0176-dns-look-up.png"
createdAt: "2024-03-08"
draft: false
categories:
  - computer-fundamentals
tags:
  - "DNS"
  - "Networking"
---

![](https://assets.bytebytego.com/diagrams/0176-dns-look-up.png)

DNS acts as an address book. It translates human-readable domain names ([google.com](http://google.com/)) to machine-readable IP addresses ([142.251.46.238](http://142.251.46.238/)).

To achieve better scalability, the DNS servers are organized in a hierarchical tree structure.

There are 3 basic levels of DNS servers:

*   Root name server (.). It stores the IP addresses of Top Level Domain (TLD) name servers. There are 13 logical root name servers globally.

*   TLD name server. It stores the IP addresses of authoritative name servers. There are several types of TLD names. For example, generic TLD (.com, .org), country code TLD (.us), test TLD (.test).

*   Authoritative name server. It provides actual answers to the DNS query. You can register authoritative name servers with domain name registrar such as GoDaddy, Namecheap, etc.

The diagram below illustrates how DNS lookup works under the hood:

1.  [google.com](http://google.com/) is typed into the browser, and the browser sends the domain name to the DNS resolver.

2.  The resolver queries a DNS root name server.

3.  The root server responds to the resolver with the address of a TLD DNS server. In this case, it is .com.

4.  The resolver then makes a request to the .com TLD.

5.  The TLD server responds with the IP address of the domain’s name server, [google.com](http://google.com/) (authoritative name server).

6.  The DNS resolver sends a query to the domain’s nameserver.

7.  The IP address for [google.com](http://google.com/) is then returned to the resolver from the nameserver.

8.  The DNS resolver responds to the web browser with the IP address ([142.251.46.238](http://142.251.46.238/)) of the domain requested initially.

DNS lookups on average take between 20-120 milliseconds to complete (according to YSlow).
