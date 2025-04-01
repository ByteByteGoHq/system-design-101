---
title: "Orchestration vs. Choreography in Microservices"
description: "Explore orchestration vs. choreography for microservice collaboration."
image: "https://assets.bytebytego.com/diagrams/0113-orchestration-vs-choreography-microservices.png"
createdAt: "2024-02-21"
draft: false
categories:
  - software-architecture
tags:
  - Microservices
  - Architecture
---

![](https://assets.bytebytego.com/diagrams/0113-orchestration-vs-choreography-microservices.png)

How do microservices collaborate and interact with each other?

There are two ways: 𝐨𝐫𝐜𝐡𝐞𝐬𝐭𝐫𝐚𝐭𝐢𝐨𝐧 and 𝐜𝐡𝐨𝐫𝐞𝐨𝐠𝐫𝐚𝐩𝐡𝐲.

Choreography is like having a choreographer set all the rules. Then the dancers on stage (the microservices) interact according to them. Service choreography describes this exchange of messages and the rules by which the microservices interact.

Orchestration is different. The orchestrator acts as a center of authority. It is responsible for invoking and combining the services. It describes the interactions between all the participating services. It is just like a conductor leading the musicians in a musical symphony. The orchestration pattern also includes the transaction management among different services.

## The benefits of orchestration:

*   **Reliability** - orchestration has built-in transaction management and error handling, while choreography is point-to-point communications and the fault tolerance scenarios are much more complicated.

*   **Scalability** - when adding a new service into orchestration, only the orchestrator needs to modify the interaction rules, while in choreography all the interacting services need to be modified.

## Some limitations of orchestration:

*   **Performance** - all the services talk via a centralized orchestrator, so latency is higher than it is with choreography. Also, the throughput is bound to the capacity of the orchestrator.

*   **Single point of failure** - if the orchestrator goes down, no services can talk to each other. To mitigate this, the orchestrator must be highly available.

Real-world use case: Netflix Conductor is a microservice orchestrator and you can read more details on the orchestrator design.
