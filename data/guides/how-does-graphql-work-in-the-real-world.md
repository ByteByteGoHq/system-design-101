---
title: How GraphQL Works at LinkedIn
description: Learn how LinkedIn uses GraphQL to improve its development workflow.
image: 'https://assets.bytebytego.com/diagrams/0209-graphql-linkedin.jpeg'
createdAt: '2024-02-12'
draft: false
categories:
  - api-web-development
tags:
  - GraphQL
  - LinkedIn
---

![](https://assets.bytebytego.com/diagrams/0209-graphql-linkedin.jpeg)

The diagram above shows how LinkedIn adopts GraphQL.

“Moving to GraphQL was a huge initiative that changed the development workflow for thousands of engineers...” \[1\]

The overall workflow after adopting GraphQL has 3 parts:

## Part 1 - Edit and Test a Query

**Steps 1-2:** The client-side developer develops a query and tests with backend services.

## Part 2 - Register a Query

**Steps 3-4:** The client-side developer commits the query and publishes the query to the query registry.

## Part 3 - Use in Production

**Step 5:** The query is released together with the client code.

**Steps 6-7:** The routing metadata is included with each registered query. The metadata is used at the traffic routing tier to route the incoming requests to the correct service cluster.

**Step 8:** The registered queries are cached at service runtime.

**Step 9:** The sample query goes to the identity service first to retrieve members and then goes to the organization service to retrieve company information.

LinkedIn doesn’t deploy a GraphQL gateway for two reasons:

1.  Prevent an additional network hop
2.  Avoid single point of failure
