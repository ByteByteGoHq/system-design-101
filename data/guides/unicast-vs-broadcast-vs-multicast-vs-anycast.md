---
title: 'Unicast vs Broadcast vs Multicast vs Anycast'
description: 'Understand the differences between unicast, broadcast, multicast, and anycast.'
image: 'https://assets.bytebytego.com/diagrams/0125-unicast-vs-broadcast-vs-multicast-vs-anycast.png'
createdAt: '2024-02-19'
draft: false
categories:
  - api-web-development
tags:
  - Network Communication
  - Protocols
---

![Unicast vs Broadcast vs Multicast vs Anycast](https://assets.bytebytego.com/diagrams/0125-unicast-vs-broadcast-vs-multicast-vs-anycast.png)

These are 4 network communication methods you must know.

*   **Unicast**

    Unique sender and a single receiver.

    For example, communication between two people in a party.

    Used in protocols such as HTTP, FTP, and SMTP.

*   **Broadcast**

    Single sender and multiple receivers.

    For example, a person at a party stands up on a podium and shouts a message to everyone. However, it doesn’t mean that every receiver gets the message.

    Used in Address Resolution Protocol, DHCP, and NTP

*   **Multicast**

    Sender to a specific group of devices in a network. This is a specialized case of broadcast routing.

    For example, a member of the group talks and listens to other members of the group within a party.

    Used in IPTV and video conference applications.

*   **Anycast**

    Sender to a single device or a specific group of devices.

    For example, saying thank you to one host out of a group of hosts organizing a party. All other hosts also expected to receive the thank you note.

    Used in DNS querying and CDNs.
