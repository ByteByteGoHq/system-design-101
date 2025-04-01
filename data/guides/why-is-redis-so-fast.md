---
title: "Why is Redis so Fast?"
description: "Explore the key factors behind Redis's exceptional speed."
image: "https://assets.bytebytego.com/diagrams/0422-why-is-redis-so-fast.png"
createdAt: '2024-03-07'
draft: false
categories:
  - caching-performance
tags:
  - "Redis"
  - "Performance"
---

![](https://assets.bytebytego.com/diagrams/0422-why-is-redis-so-fast.png)

There are 3 main reasons as shown in the diagram above.

*   Redis is a RAM-based database. RAM access is at least 1000 times faster than random disk access.

*   Redis leverages IO multiplexing and single-threaded execution loop for execution efficiency.

*   Redis leverages several efficient lower-level data structures.
