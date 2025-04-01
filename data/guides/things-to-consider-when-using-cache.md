---
title: "Things to Consider When Using Cache"
description: "Top 5 things to consider when using cache to build fast online systems."
image: "https://assets.bytebytego.com/diagrams/0362-things-to-consider-when-using-cache.png"
createdAt: "2024-02-23"
draft: false
categories:
  - caching-performance
tags:
  - "Caching"
  - "Performance"
---

![](https://assets.bytebytego.com/diagrams/0362-things-to-consider-when-using-cache.png)

Caching is one of the 𝐦𝐨𝐬𝐭 𝐜𝐨𝐦𝐦𝐨𝐧𝐥𝐲 used techniques when building fast online systems. When using a cache, here are the top 5 things to consider:

The first version of the cheatsheet was written by guest author [Love Sharma](https://twitter.com/Zonito87).

## Suitable Scenarios

*   In-memory solution

*   Read heavy system

*   Data is not frequently updated

## Caching Techniques

*   Cache aside

*   Write-through

*   Read-through

*   Write-around

*   Write-back

## Cache Eviction Algorithms

*   Least Recently Used (LRU)

*   Least Frequently Used (LFU)

*   First-in First-out (FIFO)

*   Random Replacement (RR)

## Key Metrics

*   Cache Hit Ratio

*   Latency

*   Throughput

*   Invalidation Rate

*   Memory Usage

*   CPU usage

*   Network usage

## Other Issues

*   Thunder herd on cold start

*   Time-to-live (TTL)
