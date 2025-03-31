---
title: "Why Meta, Google, and Amazon Stop Using Leap Seconds"
description: "Explore why tech giants are moving away from leap seconds."
image: "https://assets.bytebytego.com/diagrams/0363-do-you-know-why-meta-google-and-amazon-all-stop-using-leap-seconds.jpeg"
createdAt: "2024-02-04"
draft: false
categories:
  - cloud-distributed-systems
tags:
  - "Time Synchronization"
  - "Leap Seconds"
---

![Leap Seconds](https://assets.bytebytego.com/diagrams/0363-do-you-know-why-meta-google-and-amazon-all-stop-using-leap-seconds.jpeg)

Every few years, there is a special phenomenon that the second after “23:59:59” is not “00:00:00” but “23:59:60”. It is called leap second, which could easily cause time-processing bugs if not handled carefully.

Do we always need to handle leap seconds? It depends on which time representation is used. Commonly used time representations include UTC, GMT, TAI, Unix Timestamp, Epoc time, TrueTime, and GPS time.
