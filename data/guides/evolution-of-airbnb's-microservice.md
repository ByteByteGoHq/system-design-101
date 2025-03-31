---
title: 'Evolution of Airbnb’s Microservice Architecture'
description: 'Explore the evolution of Airbnb’s microservice architecture in detail.'
image: 'https://assets.bytebytego.com/diagrams/0014-airbnb-arch.jpg'
createdAt: '2024-03-05'
draft: false
categories:
  - real-world-case-studies
tags:
  - Microservices
  - Architecture
---

[![](https://assets.bytebytego.com/diagrams/0014-airbnb-arch.jpg)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F7c90c105-a6bf-46f4-b896-73390fcfe60b_3396x1839.jpeg)

Airbnb’s microservice architecture went through 3 main stages. This post is based on the tech talk by Jessica Tai.

**Monolith** (2008 - 2017)

Airbnb began as a simple marketplace for hosts and guests. This is built in a Ruby on Rails application - the monolith.

**What’s the challenge?**

*   Confusing team ownership + unowned code
*   Slow deployment

**Microservices** (2017 - 2020)

Microservice aims to solve those challenges. In the microservice architecture, key services include:

*   Data fetching service
*   Business logic data service
*   Write workflow service
*   UI aggregation service
*   Each service had one owning team

**What’s the challenge?**

Hundreds of services and dependencies were difficult for humans to manage.

**Micro + macroservices** (2020 - present)

This is what Airbnb is working on now. The micro and macroservice hybrid model focuses on the unification of APIs.

Reference: [The Human Side of Airbnb’s Microservice Architecture](https://www.infoq.com/presentations/airbnb-culture-soa/)
