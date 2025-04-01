---
title: "Memcached vs Redis"
description: "Explore the key differences between Memcached and Redis for caching."
image: "https://assets.bytebytego.com/diagrams/0267-memcached-redis.jpg"
createdAt: "2024-02-25"
draft: false
categories:
  - caching-performance
tags:
  - "memcached"
  - "redis"
---

![](https://assets.bytebytego.com/diagrams/0267-memcached-redis.jpg)

Popular interview question - what are the differences between Redis and Memcached?

The diagram above illustrates the key differences. The advantages of data structures make Redis a good choice for:

*   Recording the number of clicks and comments for each post (hash)

*   Sorting the commented user list and deduping the users (zset)

*   Caching user behavior history and filtering malicious behaviors (zset, hash)

*   Storing boolean information of extremely large data into small space. For example, login status, membership status. (bitmap)
