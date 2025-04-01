---
title: "Top 6 Cloud Messaging Patterns"
description: "Explore 6 key cloud messaging patterns for distributed systems."
image: "https://assets.bytebytego.com/diagrams/0378-top-6-cloud-messaging-patterns.png"
createdAt: "2024-02-26"
draft: false
categories:
  - cloud-distributed-systems
tags:
  - "Cloud Messaging"
  - "Design Patterns"
---

How do services communicate with each other? The diagram below shows 6 cloud messaging patterns.

![](https://assets.bytebytego.com/diagrams/0378-top-6-cloud-messaging-patterns.png)

## Asynchronous Request-Reply

This pattern aims at providing determinism for long-running backend tasks. It decouples backend processing from frontend clients.

In the diagram below, the client makes a synchronous call to the API, triggering a long-running operation on the backend. The API returns an HTTP 202 (Accepted) status code, acknowledging that the request has been received for processing.

## Publisher-Subscriber

This pattern targets decoupling senders from consumers, and avoiding blocking the sender to wait for a response.

## Claim Check

This pattern solves the transmision of large messages. It stores the whole message payload into a database and transmits only the reference to the message, which will be used later to retrieve the payload from the database.

## Priority Queue

This pattern prioritizes requests sent to services so that requests with a higher priority are received and processed more quickly than those with a lower priority.

## Saga

Saga is used to manage data consistency across multiple services in distributed systems, especially in microservices architectures where each service manages its own database.

The saga pattern addresses the challenge of maintaining data consistency without relying on distributed transactions, which are difficult to scale and can negatively impact system performance.

## Competing Consumers

This pattern enables multiple concurrent consumers to process messages received on the same messaging channel. There is no need to configure complex coordination between the consumers. However, this pattern cannot guarantee message ordering.
