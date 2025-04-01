---
title: "How can Redis be used?"
description: "Explore various use cases of Redis beyond caching."
image: "https://assets.bytebytego.com/diagrams/0388-how-can-redis-be-used.png"
createdAt: "2024-03-06"
draft: false
categories:
  - caching-performance
tags:
  - Redis
  - Use Cases
---

![](https://assets.bytebytego.com/diagrams/0388-how-can-redis-be-used.png)

There is more to Redis than just caching.

Redis can be used in a variety of scenarios as shown in the diagram.

*   **Session**

    We can use Redis to share user session data among different services.

*   **Cache**

    We can use Redis to cache objects or pages, especially for hotspot data.

*   **Distributed lock**

    We can use a Redis string to acquire locks among distributed services.

*   **Counter**

    We can count how many likes or how many reads for articles.

*   **Rate limiter**

    We can apply a rate limiter for certain user IPs.

*   **Global ID generator**

    We can use Redis Int for global ID.

*   **Shopping cart**

    We can use Redis Hash to represent key-value pairs in a shopping cart.

*   **Calculate user retention**

    We can use Bitmap to represent the user login daily and calculate user retention.

*   **Message queue**

    We can use List for a message queue.

*   **Ranking**

    We can use ZSet to sort the articles.
