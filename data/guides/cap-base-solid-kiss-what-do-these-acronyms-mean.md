---
title: "CAP, BASE, SOLID, KISS, What do these acronyms mean?"
description: "Understanding common acronyms in system design: CAP, BASE, SOLID, and KISS."
image: "https://assets.bytebytego.com/diagrams/0350-cap-base-solid-kiss.png"
createdAt: "2024-03-09"
draft: false
categories:
  - cloud-distributed-systems
tags:
  - "System Design"
  - "Software Engineering"
---

The diagram below explains the common acronyms in system designs.

![diagram](https://assets.bytebytego.com/diagrams/0350-cap-base-solid-kiss.png)

*   **CAP**

    CAP theorem states that any distributed data store can only provide two of the following three guarantees:

    1.  Consistency - Every read receives the most recent write or an error.
    2.  Availability - Every request receives a response.
    3.  Partition tolerance - The system continues to operate in network faults.

    However, this theorem was criticized for being too narrow for distributed systems, and we shouldn’t use it to categorize the databases. Network faults are guaranteed to happen in distributed systems, and we must deal with this in any distributed systems.

    You can read more on this in “Please stop calling databases CP or AP” by Martin Kleppmann.

*   **BASE**

    The ACID (Atomicity-Consistency-Isolation-Durability) model used in relational databases is too strict for NoSQL databases. The BASE principle offers more flexibility, choosing availability over consistency. It states that the states will eventually be consistent.

*   **SOLID**

    SOLID principle is quite famous in OOP. There are 5 components to it.

    1.  SRP (Single Responsibility Principle)
        Each unit of code should have one responsibility.

    2.  OCP (Open Close Principle)
        Units of code should be open for extension but closed for modification.

    3.  LSP (Liskov Substitution Principle)
        A subclass should be able to be substituted by its base class.

    4.  ISP (Interface Segregation Principle)
        Expose multiple interfaces with specific responsibilities.

    5.  DIP (Dependency Inversion Principle)
        Use abstractions to decouple dependencies in the system.

*   **KISS**

    "Keep it simple, stupid!" is a design principle first noted by the U.S. Navy in 1960. It states that most systems work best if they are kept simple.
