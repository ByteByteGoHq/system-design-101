---
title: "Unique ID Generator"
description: "Explore unique ID generation for scalable backend systems."
image: "https://assets.bytebytego.com/diagrams/0105-id-generator.png"
createdAt: "2024-02-16"
draft: false
categories:
  - cloud-distributed-systems
tags:
  - "ID Generation"
  - "System Design"
---

![](https://assets.bytebytego.com/diagrams/0105-id-generator.png)

IDs are very important for the backend. Do you know how to generate globally unique IDs?

In this post, we explore common requirements for IDs that are used in social media such as Facebook, Twitter, and LinkedIn.

## Requirements:

*   Globally unique

*   Roughly sorted by time

*   Numerical values only

*   64 bits

*   Highly scalable, low latency

The implementation details of the algorithms can be found online so we will not go into detail here.
