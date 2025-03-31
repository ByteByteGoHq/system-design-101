---
title: 'URL, URI, URN - Differences Explained'
description: 'Understand the differences between URL, URI, and URN with clear examples.'
image: 'https://assets.bytebytego.com/diagrams/0401-url-uri-urn.png'
createdAt: '2024-02-21'
draft: false
categories:
  - api-web-development
tags:
  - Networking
  - Web
---

![](https://assets.bytebytego.com/diagrams/0401-url-uri-urn.png)

The diagram above shows a comparison of URL, URI, and URN.

*   **URI**

    URI stands for Uniform Resource Identifier. It identifies a logical or physical resource on the web. URL and URN are subtypes of URI. URL locates a resource, while URN names a resource.

A URI is composed of the following parts:

```
scheme:[//authority]path[?query][#fragment]
```

*   **URL**

    URL stands for Uniform Resource Locator, the key concept of HTTP. It is the address of a unique resource on the web. It can be used with other protocols like FTP and JDBC.
*   **URN**

    URN stands for Uniform Resource Name. It uses the urn scheme. URNs cannot be used to locate a resource. A simple example given in the diagram is composed of a namespace and a namespace-specific string.
