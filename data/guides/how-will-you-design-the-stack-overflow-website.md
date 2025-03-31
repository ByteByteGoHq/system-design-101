---
title: 'How to Design Stack Overflow'
description: 'Explore the architecture of Stack Overflow and its design considerations.'
image: 'https://assets.bytebytego.com/diagrams/0343-stack-overflow-architecture.png'
createdAt: '2024-02-20'
draft: false
categories:
  - real-world-case-studies
tags:
  - System Design
  - Architecture
---

![Image](https://assets.bytebytego.com/diagrams/0343-stack-overflow-architecture.png)

If your answer is on-premise servers and monolith, you would likely fail the interview, but that's how it is built in reality!

**What people think it should look like**
The interviewer is probably expecting something on the left side.

*   Microservice is used to decompose the system into small components.
*   Each service has its own database. Use cache heavily.
*   The service is sharded.
*   The services talk to each other asynchronously through message queues.
*   The service is implemented using Event Sourcing with CQRS.
*   Showing off knowledge in distributed systems such as eventual consistency, CAP theorem, etc.

**What it actually is**
Stack Overflow serves all the traffic with only 9 on-premise web servers, and it’s on monolith! It has its own servers and does not run on the cloud.

This is contrary to all our popular beliefs these days.
