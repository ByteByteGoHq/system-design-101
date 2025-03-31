---
title: "Must Know System Design Building Blocks"
description: "Essential system design components for building scalable applications."
image: "https://assets.bytebytego.com/diagrams/0285-must-know-system-design-building-blocks.png"
createdAt: "2024-02-11"
draft: false
categories:
  - cloud-distributed-systems
tags:
  - "system design"
  - "scalability"
---

![](https://assets.bytebytego.com/diagrams/0285-must-know-system-design-building-blocks.png)

These are divided into 6 broad categories

## Distributed Computing

*   Distributed message queues facilitate async communication and decouple services

*   Distributed caching improves performance by storing frequently accessed data in memory

*   A Distributed task scheduler manages and coordinates the execution of tasks

## Scalability and Performance

*   Scaling services help adjust the capacity of services to handle changes in demand

*   CDNs serve content from geographically closer locations to improve performance and reduce latency.

*   Consistent hashing minimizes the remapping of keys when nodes are added or removed

## Service Management

*   Service discovery enables services to find and communicate with each other without hard-coding network locations

## Networking and Communication

*   DNS translates human-readable domain names into IP addresses

*   Load Balancer distributes incoming network traffic across multiple servers

*   API Gateway acts as a single entry point for a group of microservices

## Data Storage and Management

*   Databases store and manage structured data

*   Object storage helps store complex objects like images, videos, and documents

*   Sharding helps horizontally partition data across multiple nodes

*   Replication helps horizontally scale the database by copying data to multiple nodes

## Observability and Resiliency

Gain insights into the system's internal state through metrics, logging, and tracing.
