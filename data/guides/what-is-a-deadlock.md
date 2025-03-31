---
title: "What is a Deadlock?"
description: "Explore deadlocks: conditions, prevention, and recovery strategies."
image: "https://assets.bytebytego.com/diagrams/0411-what-is-a-deadlock.png"
createdAt: "2024-03-11"
draft: false
categories:
  - computer-fundamentals
tags:
  - "Concurrency"
  - "Databases"
---

A deadlock occurs when two or more transactions are waiting for each other to release locks on resources they need to continue processing. This results in a situation where neither transaction can proceed, and they end up waiting indefinitely.

![](https://assets.bytebytego.com/diagrams/0411-what-is-a-deadlock.png)

## Coffman Conditions

The Coffman conditions, named after Edward G. Coffman, Jr., who first outlined them in 1971, describe four necessary conditions that must be present simultaneously for a deadlock to occur:

*   Mutual Exclusion
*   Hold and Wait
*   No Preemption
*   Circular Wait

## Deadlock Prevention

*   Resource ordering: impose a total ordering of all resource types, and require that each process requests resources in a strictly increasing order.

*   Timeouts: A process that holds resources for too long can be rolled back.

*   Banker’s Algorithm: A deadlock avoidance algorithm that simulates the allocation of resources to processes and helps in deciding whether it is safe to grant a resource request based on the future availability of resources, thus avoiding unsafe states.

## Deadlock Recovery

*   Selecting a victim: Most modern Database Management Systems (DBMS) and Operating Systems implement sophisticated algorithms for detecting deadlocks and selecting victims, often allowing customization of the victim selection criteria via configuration settings. The selection can be based on resource utilization, transaction priority, cost of rollback etc.

*   Rollback: The database may roll back the entire transaction or just enough of it to break the deadlock. Rolled-back transactions can be restarted automatically by the database management system.
