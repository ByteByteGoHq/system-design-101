---
title: "DNS Record Types You Should Know"
description: "Learn about the most common and important DNS record types."
image: "https://assets.bytebytego.com/diagrams/0175-dns-record-types-you-should-know.png"
createdAt: "2024-03-09"
draft: false
categories:
  - computer-fundamentals
tags:
  - "DNS"
  - "Networking"
---

![](https://assets.bytebytego.com/diagrams/0175-dns-record-types-you-should-know.png)

Here are the 8 most commonly used DNS Record Types.

## A (Address) Record

Maps a domain name to an IPv4 address. It is one of the most essential records for translating human-readable domain names into IP addresses.

## CNAME (Canonical Name) Record

Used to alias one domain name to another. Often used for subdomains, pointing them to the main domain while keeping the actual domain name hidden.

## AAAA Record

Similar to an A record but maps a domain name to an IPv6 address. They are used for websites and services that support the IPv6 protocol.

## PTR Record

Provides reverse DNS lookup, mapping an IP address back to a domain name. It is commonly used in verifying the authenticity of a server.

## MX Record

Directs email traffic to the correct mail server.

## NS (Name Server) Record

Specifies the authoritative DNS servers for the domain. These records help direct queries to the correct DNS servers for further lookups.

## SRV (Service) Record

SRV record specifies a host and port for specific services such as VoIP. They are used in conjunction with A records.

## TXT (Text) Record

Allows the administrator to add human-readable text to the DNS records. It is used to include verification records, like SPF, for email security.
