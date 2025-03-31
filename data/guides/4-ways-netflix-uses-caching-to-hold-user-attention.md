---
title: '4 Ways Netflix Uses Caching'
description: 'Explore how Netflix uses caching to maintain user engagement.'
image: 'https://assets.bytebytego.com/diagrams/0007-4-ways-netflix-uses-caching.png'
createdAt: '2024-02-25'
draft: false
categories:
  - real-world-case-studies
tags:
  - Caching
  - Netflix
---

![](https://assets.bytebytego.com/diagrams/0007-4-ways-netflix-uses-caching.png)

The goal of Netflix is to keep you streaming for as long as possible. But a user’s typical attention span is just 90 seconds.

They use EVCache (a distributed key-value store) to reduce latency so that the users don’t lose interest.

However, EVCache has multiple use cases at Netflix.

*   **Lookaside Cache**

    When the application needs some data, it first tries the EVCache client and if the data is not in the cache, it goes to the backend service and the Cassandra database to fetch the data.

    The service also keeps the cache updated for future requests.

*   **Transient Data Store**

    Netflix uses EVCache to keep track of transient data such as playback session information.

    One application service might start the session while the other may update the session followed by a session closure at the very end.

*   **Primary Store**

    Netflix runs large-scale pre-compute systems every night to compute a brand-new home page for every profile of every user based on watch history and recommendations.

    All of that data is written into the EVCache cluster from where the online services read the data and build the homepage.

*   **High Volume Data**

    Netflix has data that has a high volume of access and also needs to be highly available. For example, UI strings and translations that are shown on the Netflix home page.

    A separate process asynchronously computes and publishes the UI string to EVCache from where the application can read it with low latency and high availability.
