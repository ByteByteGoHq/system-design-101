---
title: "Key Terms in Domain-Driven Design"
description: "Understand key concepts in Domain-Driven Design for better software."
image: "https://assets.bytebytego.com/diagrams/0163-ddd.png"
createdAt: "2024-02-28"
draft: false
categories:
  - software-architecture
tags:
  - "Domain-Driven Design"
  - "Software Design"
---

Have you heard of Domain-Driven Design (DDD), a major software design approach?

![](https://assets.bytebytego.com/diagrams/0163-ddd.png)

DDD was introduced in Eric Evans’ classic book “Domain-Driven Design: Tackling Complexity in the Heart of Software”. It explained a methodology to model a complex business. In this book, there is a lot of content, so I'll summarize the basics.

## The composition of domain objects:

*   **Entity:** a domain object that has ID and life cycle.

*   **Value Object:** a domain object without ID. It is used to describe the property of Entity.

*   **Aggregate:** a collection of Entities that are bounded together by Aggregate Root (which is also an entity). It is the unit of storage.

## The life cycle of domain objects:

*   **Repository:** storing and loading the Aggregate.

*   **Factory:** handling the creation of the Aggregate.

## Behavior of domain objects:

*   **Domain Service:** orchestrate multiple Aggregate.

*   **Domain Event:** a description of what has happened to the Aggregate. The publication is made public so others can consume and reconstruct it.
