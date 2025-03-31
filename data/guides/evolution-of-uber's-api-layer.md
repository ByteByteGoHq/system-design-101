---
title: Evolution of Uber's API Layer
description: Learn about the evolution of Uber's API layer.
image: 'https://assets.bytebytego.com/diagrams/0397-uber-api-layer.png'
createdAt: '2024-03-14'
draft: false
categories:
  - real-world-case-studies
tags:
  - API Gateway
  - Microservices
---

![](https://assets.bytebytego.com/diagrams/0397-uber-api-layer.png)

Uber’s API gateway went through 3 main stages.

First gen: the organic evolution. Uber's architecture in 2014 would have two key services: dispatch and API. A dispatch service connects a rider with a driver, while an API service stores the long-term data of users and trips.

Second gen: the all-encompassing gateway. Uber adopted a microservice architecture very early on. By 2019, Uber's products were powered by 2,200+ microservices as a result of this architectural decision.

Third gen: self-service, decentralized, and layered. As of early 2018, Uber had completely new business lines and numerous new applications. Freight, ATG, Elevate, groceries, and more are among the growing business lines. With a new set of goals comes the third generation.
