---
title: 'Proxy vs Reverse Proxy'
description: 'Understanding the differences between forward and reverse proxies.'
image: 'https://assets.bytebytego.com/diagrams/0196-forward-proxy-vs-reverse-proxy.png'
createdAt: '2024-03-01'
draft: false
categories:
  - api-web-development
tags:
  - Networking
  - Security
---

![](https://assets.bytebytego.com/diagrams/0196-forward-proxy-vs-reverse-proxy.png)

A forward proxy is a server that sits between user devices and the internet. A forward proxy is commonly used for:

*   **Protect clients**
*   **Avoid browsing restrictions**
*   **Block access to certain content**

A reverse proxy is a server that accepts a request from the client, forwards the request to web servers, and returns the results to the client as if the proxy server had processed the request. A reverse proxy is good for:

*   **Protect servers**
*   **Load balancing**
*   **Cache static contents**
*   **Encrypt and decrypt SSL communications**
