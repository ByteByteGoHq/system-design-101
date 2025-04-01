---
title: How Netflix Really Uses Java
description: Explore Netflix's extensive use of Java in its microservices architecture.
image: 'https://assets.bytebytego.com/diagrams/0102-how-netflix-really-uses-java.png'
createdAt: '2024-03-04'
draft: false
categories:
  - real-world-case-studies
tags:
  - Java
  - Microservices
---

![](https://assets.bytebytego.com/diagrams/0102-how-netflix-really-uses-java.png)

Netflix is predominantly a Java shop.

Every backend application (including internal apps, streaming, and movie production apps) at Netflix is a Java application.

However, the Java stack is not static and has gone through multiple iterations over the years.

Here are the details of those iterations:

*   **API Gateway**

    Netflix follows a microservices architecture. Every piece of functionality and data is owned by a microservice built using Java (initially version 8)

*   **BFFs with Groovy & RxJava**

    Using a single gateway for multiple clients was a problem for Netflix because each client (such as TV, mobile apps, or web browser) had subtle differences.

    To handle this, Netflix used the Backend-for-Frontend (BFF) pattern. Zuul was moved to the role of a proxy

*   **GraphQL Federation**

    The Groovy and RxJava approach required more work from the UI developers in creating the Groovy scripts. Also, reactive programming is generally hard.
