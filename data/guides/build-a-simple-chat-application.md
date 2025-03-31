---
title: "Build a Simple Chat Application with Redis"
description: "Learn to build a simple chat application using Redis pub/sub."
image: "https://assets.bytebytego.com/diagrams/0314-redis-chat.jpg"
createdAt: "2024-03-04"
draft: false
categories:
  - how-it-works
tags:
  - Redis
  - Chat Application
---

![](https://assets.bytebytego.com/diagrams/0314-redis-chat.jpg)

How do we build a simple chat application using Redis?

The diagram below shows how we can leverage the pub-sub functionality of Redis to develop a chat application.

## Stage 1: Connection Initialization

*   Steps 1 and 2: Bob opens the chat application. A web socket is established between the client and the server.

*   Steps 3 and 4: The pub-sub server establishes several connections to Redis. One connection is used to update the Redis data models and publish messages to a topic. Other connections are used to subscribe and listen to updates for topics.

*   Steps 5 and 6: Bob’s client application requires the chat member list and the historical message list. The information is retrieved from Redis and sent to the client application.

*   Steps 7 and 8: Since Bob is a new member joining the chat application, a message is published to the “member\_add” topic, and as a result, other participants of the chat application can see Bob.

## Stage 2: Message Handling

*   Step 1: Bob sends a message to Alice in the chat application.

*   Step 2: The new chat message is added to Redis SortedSet by calling ‘zadd.’ The chat messages are sorted based on arrival time. The pub-sub server then publishes the chat message to the “messages” topic so subscribers can pick it up.

*   Step 3: Alice’s client application receives the chat message from Bob.
