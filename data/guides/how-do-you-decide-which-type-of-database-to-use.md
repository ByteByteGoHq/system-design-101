---
title: "How to Decide Which Type of Database to Use"
description: "A guide to choosing the right database for your specific needs."
image: "https://assets.bytebytego.com/diagrams/0160-database-types.jpg"
createdAt: "2024-02-17"
draft: false
categories:
  - database-and-storage
tags:
  - database selection
  - database types
---

![](https://assets.bytebytego.com/diagrams/0160-database-types.jpg)

There are hundreds or even thousands of databases available today, such as Oracle, MySQL, MariaDB, SQLite, PostgreSQL, Redis, ClickHouse, MongoDB, S3, Ceph, etc. How do you select the architecture for your system? My short summary is as follows:

## Database Types

*   Relational database: Almost anything could be solved by them.

*   In-memory store: Their speed and limited data size make them ideal for fast operations.

*   Time-series database: Store and manage time-stamped data.

*   Graph database: It is suitable for complex relationships between unstructured objects.

*   Document store: They are good for large immutable data.

*   Wide column store: They are usually used for big data, analytics, reporting, etc., which needs denormalized data.
