---
title: "Resiliency Patterns"
description: "Explore cloud design patterns for building resilient systems."
image: "https://assets.bytebytego.com/diagrams/0316-reliciency-patterns.jpg"
createdAt: "2024-02-08"
draft: false
categories:
  - cloud-distributed-systems
tags:
  - "Resilience"
  - "Design Patterns"
---

Have you noticed that the largest incidents are usually caused by something very small?

![](https://assets.bytebytego.com/diagrams/0316-reliciency-patterns.jpg)

A minor error starts the snowball effect that keeps building up. Suddenly, everything is down.

Here are 8 cloud design patterns to reduce the damage done by failures.

*   Timeout
*   Retry
*   Circuit breaker
*   Rate limiting
*   Load shedding
*   Bulkhead
*   Back pressure
*   Let it crash

These patterns are usually not used alone. To apply them effectively, we need to understand why we need them, how they work, and their limitations.
