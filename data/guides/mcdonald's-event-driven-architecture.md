---
title: 'McDonald’s Event-Driven Architecture'
description: 'Explore McDonald’s event-driven architecture for scalability and efficiency.'
image: 'https://assets.bytebytego.com/diagrams/0266-mcdonald-s-event-driven-architecture.png'
createdAt: '2024-02-18'
draft: false
categories:
  - real-world-case-studies
tags:
  - Event-Driven Architecture
  - Case Study
---

![](https://assets.bytebytego.com/diagrams/0266-mcdonald-s-event-driven-architecture.png)

Think you know everything about McDonald's? What about its event-driven architecture?

McDonald's standardizes events using the following components:

*   **Event Registry:** An event registry to define a standardized schema.
*   **Custom SDKs:** Custom software development kits (SDKs) to process events and handle errors.
*   **Event Gateway:** An event gateway that performs identity authentication and authorization.
*   **Utilities and Tools:** Utilities and tools to fix events, keep the cluster healthy, and perform administrative tasks.

To scale event processing, McDonald uses a regional architecture that provides global availability based on AWS. Within a region, producers shard events by domains, and each domain is processed by an MSK cluster. The cluster auto-scales based on MSK metrics (e.g., CPU usage), and the auto-scale workflow is based on step-functions and re-assignment tasks.

Reference: Behind the scenes: [McDonald’s event-driven architecture](https://medium.com/mcdonalds-technical-blog/behind-the-scenes-mcdonalds-event-driven-architecture-51a6542c0d86)
