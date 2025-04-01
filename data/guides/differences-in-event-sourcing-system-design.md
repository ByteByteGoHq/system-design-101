---
title: "Differences in Event Sourcing System Design"
description: "Explore the nuances of event sourcing system design and its benefits."
image: "https://assets.bytebytego.com/diagrams/0188-event-sourcing.jpeg"
createdAt: "2024-02-08"
draft: false
categories:
  - database-and-storage
tags:
  - "event sourcing"
  - "system design"
---

![](https://assets.bytebytego.com/diagrams/0188-event-sourcing.jpeg)

How do we design a system using the event sourcing paradigm? How is it different from normal system design? What are the benefits? We will talk about it in this post.

The diagram above shows the comparison of a normal CRUD system design with an event sourcing system design. We use an e-commerce system that can place orders and pay for the orders to demonstrate how event sourcing works.

The event sourcing paradigm is used to design a system with determinism. This changes the philosophy of normal system designs.
