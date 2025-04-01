---
title: 'What is the Journey of a Slack Message?'
description: 'Explore the journey of a Slack message from sender to receiver.'
image: 'https://assets.bytebytego.com/diagrams/0338-slack-message-journey.jpg'
createdAt: '2024-03-08'
draft: false
categories:
  - real-world-case-studies
tags:
  - System Design
  - Messaging
---

![](https://assets.bytebytego.com/diagrams/0338-slack-message-journey.jpg)

In a recent technical article, Slack explains how its real-time messaging framework works. Here is my short summary:

A Slack message travels through five important servers:

*   **WebApp:** defines the API that a Slack client could use
*   **Admin Server (AS):** finds the correct Channel Server using channel ID
*   **Channel Server (CS):** maintains the history of message channel
*   **Gateway Server (GS):** deployed in each geographic region. Maintain WebSocket channel subscription
*   **Envoy:** service proxy for cloud-native applications

*   Because there are too many channels, the Channel Server (CS) uses consistent hashing to allocate millions of channels to many channel servers.
*   Slack messages are delivered through WebApp and Admin Server to the correct Channel Server.
*   Through Gate Server and Envoy (a proxy), the Channel Server will push messages to message receivers.
*   Message receivers use WebSocket, which is a bi-directional messaging mechanism, so they are able to receive updates in real-time.
