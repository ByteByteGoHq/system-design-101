---
title: 'How NAT Enabled the Internet'
description: 'Explore how NAT facilitated the expansion of the internet.'
image: 'https://assets.bytebytego.com/diagrams/0231-http-header.png'
createdAt: '2024-01-29'
draft: false
categories:
  - api-web-development
tags:
  - NAT
  - Networking
---

![](https://assets.bytebytego.com/diagrams/0231-http-header.png)

Network Address Translation (NAT) is the process that has made the growth of the Internet possible.

But how does it work?

1. In a corporate or home setting, multiple devices (phones, computers, etc.) share one router with a single public IP address.
2. When a device wants to access the internet, it sends a request to your router. The request contains the device's private IP address.
3. The router’s NAT process replaces the private IP with the router’s public IP.
4. The modified request is sent to the internet.
5. When the response comes back, NAT checks its record and replaces the public IP with the correct private IP. It sends the response to the right device.

NAT has several important uses:

*   **Conserves public IP addresses:** Without NAT, IPv4 addresses would have been depleted much faster, severely limiting the growth of the Internet.
*   **Allows sharing:** It allows sharing a single public IP address across multiple devices.
*   **Acts as a basic firewall:** NAT acts as a basic firewall that hides internal IP addresses.
*   **Eases network management:** NAT also makes it easy to manage large networks.
