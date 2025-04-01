---
title: "Typical Microservice Architecture"
description: "Explore a typical microservice architecture with key components."
image: "https://assets.bytebytego.com/diagrams/0396-typical-microservice-architecture.png"
createdAt: "2024-03-14"
draft: false
categories:
  - software-architecture
tags:
  - Microservices
  - Architecture
---

![](https://assets.bytebytego.com/diagrams/0396-typical-microservice-architecture.png)

The diagram above shows a typical microservice architecture.

## Key Components

*   **Load Balancer:** This distributes incoming traffic across multiple backend services.

*   **CDN (Content Delivery Network):** CDN is a group of geographically distributed servers that hold static content for faster delivery. The clients look for content in CDN first, then progress to backend services.

*   **API Gateway:** This handles incoming requests and routes them to the relevant services. It talks to the identity provider and service discovery.

*   **Identity Provider:** This handles authentication and authorization for users.

*   **Service Registry & Discovery:** Microservice registration and discovery happen in this component, and the API gateway looks for relevant services in this component to talk to.

*   **Management:** This component is responsible for monitoring the services.

*   **Microservices:** Microservices are designed and deployed in different domains. Each domain has its database.
